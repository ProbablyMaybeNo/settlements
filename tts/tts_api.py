# -*- coding: utf-8 -*-
"""Talk to a running Tabletop Simulator over its External Editor API.

This is the live connection. TTS listens on 127.0.0.1:39999 for commands, and
pushes messages back to a listener on 127.0.0.1:39998 — the same channel the
Atom / VS Code TTS plugins use. It is script-level: it can push Lua, run Lua and
read what TTS prints. It cannot move objects by hand or click menus.

    py -3.13 tts_api.py ping                    is TTS listening?
    py -3.13 tts_api.py push                    send Global.lua (Save & Play)
    py -3.13 tts_api.py pull                    fetch the scripts TTS currently has
    py -3.13 tts_api.py exec "print(#getAllObjects())"
    py -3.13 tts_api.py exec-file probe.lua
    py -3.13 tts_api.py listen 30               watch TTS output for 30s

PROTOCOL NOTE: the message IDs below are from the documented External Editor API
(editor->TTS 0 get / 1 save&play / 3 execute; TTS->editor 2 print / 3 error /
5 return). They are transcribed from the spec, not yet verified against a live
build on this machine — `ping` then `exec` is the two-minute check that they are
right, and any mismatch will surface there rather than silently.

CAUTION: `push` uses Save & Play, which RELOADS the currently-open table with the
new scripts. Unsaved hand-placed objects in that session are lost. Save first.
"""
import argparse
import json
import os
import socket
import sys
import time

HOST = '127.0.0.1'
TTS_PORT = 39999        # TTS listens here (we send)
EDITOR_PORT = 39998     # we listen here (TTS sends)
HERE = os.path.dirname(os.path.abspath(__file__))
GLOBAL_GUID = '-1'      # the Global script

MSG_GET, MSG_SAVE_PLAY, MSG_CUSTOM, MSG_EXEC = 0, 1, 2, 3
INBOUND = {0: 'pushing object', 1: 'new game', 2: 'print', 3: 'ERROR',
           4: 'custom', 5: 'return', 6: 'game saved', 7: 'object created'}


def send(payload, timeout=5.0):
    """Fire one JSON command at TTS. Each command is its own connection."""
    data = json.dumps(payload).encode('utf-8')
    with socket.create_connection((HOST, TTS_PORT), timeout=timeout) as s:
        s.sendall(data)


def is_up(timeout=1.0):
    try:
        with socket.create_connection((HOST, TTS_PORT), timeout=timeout):
            return True
    except OSError:
        return False


def listen(seconds=10.0, quiet=False):
    """Collect messages TTS pushes back. Returns the list of decoded payloads."""
    out = []
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        srv.bind((HOST, EDITOR_PORT))
    except OSError as e:
        print(f'cannot bind {EDITOR_PORT}: {e}\n'
              '  Something else holds it — most likely a VS Code/Atom TTS plugin. '
              'Close it and retry.', file=sys.stderr)
        return out
    srv.listen(8)
    srv.settimeout(0.5)
    deadline = time.time() + seconds
    while time.time() < deadline:
        try:
            conn, _ = srv.accept()
        except socket.timeout:
            continue
        with conn:
            conn.settimeout(2.0)
            chunks = []
            try:
                while True:
                    b = conn.recv(65536)
                    if not b:
                        break
                    chunks.append(b)
            except socket.timeout:
                pass
        raw = b''.join(chunks).decode('utf-8', 'replace').strip()
        if not raw:
            continue
        try:
            msg = json.loads(raw)
        except json.JSONDecodeError:
            if not quiet:
                print(f'  <non-JSON> {raw[:400]}')
            continue
        out.append(msg)
        if not quiet:
            kind = INBOUND.get(msg.get('messageID'), msg.get('messageID'))
            body = msg.get('message') or msg.get('errorMessagePrefix') or ''
            if msg.get('messageID') == 5:
                body = msg.get('returnValue', '')
            if msg.get('messageID') == 1 and 'scriptStates' in msg:
                body = f"{len(msg['scriptStates'])} script state(s)"
            print(f'  [{kind}] {body}')
    srv.close()
    return out


def require_up():
    if is_up():
        return True
    print('TTS is not listening on 127.0.0.1:39999.\n'
          '  Launch Tabletop Simulator and load a table (Single Player is fine).\n'
          '  The API only listens while the game is running.', file=sys.stderr)
    return False


def cmd_ping(_):
    up = is_up()
    print(f'TTS API on {HOST}:{TTS_PORT}: {"UP" if up else "closed"}')
    if up:
        print('  sending a no-op Lua execute to confirm the channel round-trips...')
        send({'messageID': MSG_EXEC, 'guid': GLOBAL_GUID,
              'script': 'print("[tts_api] handshake ok — "..#getAllObjects()..'
                        '" objects on the table")'})
        listen(4.0)
    return 0 if up else 1


def cmd_push(args):
    if not require_up():
        return 1
    path = args.file or os.path.join(HERE, 'Global.lua')
    with open(path, encoding='utf-8') as fh:
        lua = fh.read()
    print(f'pushing {os.path.basename(path)} ({len(lua):,} chars) as the Global script')
    print('  (Save & Play reloads the open table — unsaved changes there are lost)')
    send({'messageID': MSG_SAVE_PLAY,
          'scriptStates': [{'guid': GLOBAL_GUID, 'script': lua, 'ui': ''}]})
    listen(6.0)
    return 0


def cmd_pull(args):
    if not require_up():
        return 1
    send({'messageID': MSG_GET})
    msgs = listen(6.0, quiet=True)
    for m in msgs:
        for st in m.get('scriptStates', []) or []:
            g = st.get('guid', '?')
            name = st.get('name', 'Global' if g == GLOBAL_GUID else g)
            script = st.get('script', '') or ''
            print(f'--- {name} ({g}) — {len(script):,} chars')
            if args.write and script.strip():
                fn = os.path.join(HERE, 'pulled',
                                  ('Global' if g == GLOBAL_GUID else f'{name}.{g}') + '.lua')
                os.makedirs(os.path.dirname(fn), exist_ok=True)
                with open(fn, 'w', encoding='utf-8') as fh:
                    fh.write(script)
                print(f'    -> {fn}')
    if not msgs:
        print('no reply — TTS may not have a table loaded yet')
    return 0


def cmd_exec(args):
    if not require_up():
        return 1
    lua = args.code
    if args.code and os.path.isfile(args.code):
        with open(args.code, encoding='utf-8') as fh:
            lua = fh.read()
    send({'messageID': MSG_EXEC, 'guid': args.guid, 'script': lua})
    listen(args.wait)
    return 0


def cmd_listen(args):
    print(f'listening on {HOST}:{EDITOR_PORT} for {args.seconds:g}s — '
          'anything TTS prints or errors appears here')
    listen(args.seconds)
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('ping').set_defaults(fn=cmd_ping)
    p = sub.add_parser('push'); p.add_argument('file', nargs='?'); p.set_defaults(fn=cmd_push)
    p = sub.add_parser('pull'); p.add_argument('--write', action='store_true')
    p.set_defaults(fn=cmd_pull)
    p = sub.add_parser('exec'); p.add_argument('code')
    p.add_argument('--guid', default=GLOBAL_GUID)
    p.add_argument('--wait', type=float, default=5.0); p.set_defaults(fn=cmd_exec)
    p = sub.add_parser('listen'); p.add_argument('seconds', nargs='?', type=float, default=10.0)
    p.set_defaults(fn=cmd_listen)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == '__main__':
    sys.exit(main())

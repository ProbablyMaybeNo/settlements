"""Serve the Rules Wall with live write-back into the Obsidian vault.

    py -3.13 scripts/wall_server.py            # http://127.0.0.1:8790
    py -3.13 scripts/wall_server.py --port 9000 --read-only

Click any cell, type, press Enter. The edit goes straight into the vault note
the cell came from — the same note Obsidian has open, so it updates live and the
15-minute sync task commits it like any other rules change.

Three safety rules, because this writes to the source of truth:

1. **The vault, never the mirror.** `rules-vault/` is robocopied over every 15
   minutes; an edit there is silently destroyed. This refuses to run against it.
2. **Optimistic concurrency.** Every save sends the cell text the browser was
   showing. If the line on disk no longer contains it, the write is refused and
   the browser reverts — so an edit made in Obsidian meanwhile is never clobbered.
3. **Structure is preserved.** Only the one cell inside the one line changes.
   Pipes inside wikilink aliases are masked before the split, so
   `[[Note#Head|Label]]` is never mistaken for a column boundary.
"""
import io
import json
import os
import re
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_rules_wall as W  # noqa: E402

PORT = 8790
if "--port" in sys.argv:
    PORT = int(sys.argv[sys.argv.index("--port") + 1])
READ_ONLY = "--read-only" in sys.argv
ROOT = W.VAULT


def cell_write(note, lineno, col, expected, text):
    """Replace one cell on one line. Returns the re-rendered HTML for that cell.

    Raises ValueError with a human-readable reason on any mismatch — the caller
    turns that into a 409 and the browser reverts the cell.
    """
    if os.path.normcase(ROOT).startswith(os.path.normcase(W.MIRROR)):
        raise ValueError("refusing to write to the repo mirror")
    if not re.fullmatch(r"[A-Za-z0-9 ,'&—–.()-]+", note):
        raise ValueError("bad note name")

    path = os.path.join(ROOT, note + ".md")
    if not os.path.isfile(path):
        raise ValueError("no such note: " + note)

    raw = io.open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)
    if lineno < 0 or lineno >= len(lines):
        raise ValueError("line %d is past the end of %s — reload" % (lineno, note))

    line = lines[lineno]
    prefix = ""
    m = re.match(r"^(>\s?)", line)
    if m:
        prefix, line = m.group(1), line[m.end():]

    if line.lstrip().startswith("|"):
        masked = re.sub(r"\[\[[^\]]*\]\]|`[^`]*`",
                        lambda mm: mm.group(0).replace("|", W.SENT), line)
        lead = masked[:len(masked) - len(masked.lstrip())]
        core = masked.strip()
        trailing = core.endswith("|")
        parts = core.strip("|").split("|")
        if col >= len(parts):
            raise ValueError("column %d does not exist on that line — reload" % col)
        if parts[col].strip().replace(W.SENT, "|") != expected.strip():
            raise ValueError("that line changed on disk — reload the wall")
        parts[col] = " " + text.replace("|", W.SENT) + " "
        rebuilt = lead + "|" + "|".join(parts) + ("|" if trailing else "")
        new_line = prefix + rebuilt.replace(W.SENT, "|")
        rendered = text
    else:
        m2 = re.match(r"^(\s*-\s+)\*\*([^*]+)\*\*(\s*[—:-]?\s*)(.*)$", line)
        if not m2:
            raise ValueError("line %d is not an editable row — reload" % lineno)
        bullet, name, sep, desc = m2.groups()
        cur = name.strip() if col == 0 else desc.strip()
        if cur != expected.strip():
            raise ValueError("that line changed on disk — reload the wall")
        if col == 0:
            new_line = prefix + bullet + "**" + text + "**" + sep + desc
        else:
            new_line = prefix + bullet + "**" + name + "**" + (sep or " — ") + text
        rendered = text

    lines[lineno] = new_line
    tmp = path + ".wall-tmp"
    io.open(tmp, "w", encoding="utf-8", newline="").write(nl.join(lines))
    os.replace(tmp, path)
    return W.inline(rendered)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *a):
        if "POST" in (a[0] if a else ""):
            sys.stderr.write("  %s\n" % (fmt % a))

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        blob = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(blob)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(blob)

    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/index.html"):
            return self._send(404, '{"error":"not found"}')
        page, stats, total = W.build(ROOT, editable=not READ_ONLY)
        self._send(200, page, "text/html; charset=utf-8")

    def do_POST(self):
        if self.path != "/cell":
            return self._send(404, '{"error":"not found"}')
        if READ_ONLY:
            return self._send(403, '{"error":"server is running --read-only"}')
        try:
            n = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(n) or b"{}")
            html = cell_write(req["note"], int(req["line"]), int(req["col"]),
                              req.get("old", ""), req.get("text", ""))
            sys.stderr.write("  saved %s:%s col %s\n"
                             % (req["note"], req["line"], req["col"]))
            self._send(200, json.dumps({"ok": True, "html": html}))
        except ValueError as e:
            self._send(409, json.dumps({"error": str(e)}))
        except Exception as e:  # noqa: BLE001 - surface anything to the browser
            self._send(500, json.dumps({"error": "%s: %s" % (type(e).__name__, e)}))


if __name__ == "__main__":
    _, stats, total = W.build(ROOT, editable=not READ_ONLY)
    print("Rules Wall  ->  http://127.0.0.1:%d/" % PORT)
    print("  source : %s" % ROOT)
    print("  content: %d tables, %d entries" % (total, stats["rows"]))
    print("  mode   : %s" % ("READ-ONLY" if READ_ONLY else "EDITABLE - saves into the vault"))
    print("  Ctrl+C to stop.\n")
    try:
        webbrowser.open("http://127.0.0.1:%d/" % PORT)
    except Exception:
        pass
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")

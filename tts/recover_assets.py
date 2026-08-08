# -*- coding: utf-8 -*-
"""Recover Workshop mod assets whose original download failed, into TTS's cache.

TTS caches every asset it fetches in `Mods/Models/<url-with-punctuation-stripped>.obj`.
So if we can get the bytes by ANY route and write them under that exact name, TTS
finds them on next load and the "Custom Model" popups stop — no editing the mod, no
re-hosting, nothing for you to click.

RECOVERY ROUTES, each measured on this machine rather than assumed:

  pastebin.com/XXXX        -> pastebin.com/raw/XXXX     WORKS. The plain URL serves
                             an HTML viewer page; /raw/ serves the .obj text.
  paste.ee (https)         -> http:// fallback. The host's TLS handshake fails with
                             WRONG_VERSION_NUMBER from Python, so try plain http.
  cloud-N.steamusercontent -> steamusercontent-a.akamaihd.net. Steam retired the old
                             hostname (403). Some UGC ids still exist on Akamai and
                             return 200; others are 404, meaning the file was deleted
                             from Steam entirely and is not recoverable.
  anything                 -> web.archive.org/web/2id_/<url>. Last resort for hosts
                             that are simply gone.

CONTENT IS VALIDATED, NOT TRUSTED. Several dead hosts answer 200 with a 400-byte
HTML error page. A saved error page is worse than a missing file: TTS caches it and
you get an invisible model instead of a popup. So every download must actually look
like OBJ geometry (v/f/vn lines) before it is written.

    py -3.13 recover_assets.py --id 1940563574            # dry run, report only
    py -3.13 recover_assets.py --id 1940563574 --write    # actually save to cache
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
import urllib.request

TTS = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                   'Tabletop Simulator', 'Mods')
WORKSHOP = os.path.join(TTS, 'Workshop')
CACHE = os.path.join(TTS, 'Models')
CACHE_RAW = os.path.join(TTS, 'Models Raw')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'


def cache_stem(url):
    return re.sub(r'[^A-Za-z0-9]', '', url or '')


def cached(url):
    stem = cache_stem(url)
    for d in (CACHE, CACHE_RAW):
        if os.path.isfile(os.path.join(d, stem + '.obj')):
            return True
    return False


def routes(url):
    """Every way we know of to get this file, best first."""
    out = [('as-is', url)]
    m = re.match(r'https?://cloud-\d+\.steamusercontent\.com(/.*)', url)
    if m:
        out.append(('steam-akamai',
                    'https://steamusercontent-a.akamaihd.net' + m.group(1)))
    if 'pastebin.com/' in url and '/raw/' not in url:
        out.append(('pastebin-raw', url.replace('pastebin.com/', 'pastebin.com/raw/')))
    if url.startswith('https://paste.ee/'):
        out.append(('paste.ee-http', 'http://' + url[len('https://'):]))
    if url.startswith('http://paste.ee/'):
        out.append(('paste.ee-https', 'https://' + url[len('http://'):]))
    if url.startswith('http://'):
        out.append(('https-upgrade', 'https://' + url[len('http://'):]))
    out.append(('wayback', 'https://web.archive.org/web/2id_/' + url))
    return out


def looks_like_obj(b):
    """Validate CONTENT, not status code.

    Dead hosts love answering 200 with an HTML error page, and a cached error page
    is worse than a missing file — TTS keeps it and you get an invisible model with
    no popup to tell you why. OBJ is text with vertex and face lines; some packs
    ship binary-ish variants, so also accept anything large that is not HTML."""
    if not b or len(b) < 200:
        return False
    head = b[:2048].lstrip()
    if head[:1] == b'<' or b'<html' in head.lower() or b'<!doctype' in head.lower():
        return False
    text = head.decode('utf-8', 'replace')
    has_v = re.search(r'(?m)^\s*v\s+-?\d', text) is not None
    has_f = re.search(r'(?m)^\s*f\s+\d', text) is not None
    if has_v or has_f or text.startswith('#'):
        return True
    return len(b) > 20000            # probably a binary mesh variant


def fetch(url, timeout=20, cap=40 * 1024 * 1024):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if not (200 <= r.status < 400):
            raise OSError(f'status {r.status}')
        return r.read(cap)


def recover(item):
    url, name = item
    tried = []
    for tag, alt in routes(url):
        try:
            b = fetch(alt)
        except Exception as e:
            tried.append(f'{tag}:{type(e).__name__}')
            continue
        if looks_like_obj(b):
            return dict(url=url, name=name, ok=True, via=tag, alt=alt,
                        size=len(b), data=b, tried=tried)
        tried.append(f'{tag}:not-obj({len(b)}b)')
    return dict(url=url, name=name, ok=False, tried=tried)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--id', required=True, help='workshop mod id')
    ap.add_argument('--write', action='store_true',
                    help='save recovered files into TTS\'s cache')
    ap.add_argument('--workers', type=int, default=10)
    ap.add_argument('--limit', type=int, default=None)
    args = ap.parse_args()

    path = os.path.join(WORKSHOP, f'{args.id}.json')
    if not os.path.isfile(path):
        print(f'no such mod: {path}', file=sys.stderr)
        return 1
    with open(path, encoding='utf-8', errors='replace') as fh:
        mod = json.load(fh)

    urls, stack = {}, list(mod.get('ObjectStates') or [])
    while stack:
        o = stack.pop()
        if not isinstance(o, dict):
            continue
        stack.extend(o.get('ContainedObjects') or [])
        cm = o.get('CustomMesh') or {}
        if cm.get('MeshURL'):
            urls[cm['MeshURL']] = (o.get('Nickname') or '').strip() or '(unnamed)'

    todo = [(u, n) for u, n in urls.items() if not cached(u)]
    # count BEFORE --limit truncates, or the "already cached" figure is a lie
    n_missing = len(todo)
    if args.limit:
        todo = todo[:args.limit]
    print(f'{mod.get("SaveName")}: {len(urls)} meshes, '
          f'{len(urls) - n_missing} already cached, {n_missing} missing'
          + (f' (sampling {len(todo)})' if args.limit else ''))
    if not todo:
        return 0
    print(f'trying up to {len(routes("http://x/y"))} routes each, '
          f'{args.workers} at a time — content is validated, not just the status code\n')

    got, lost = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, r in enumerate(ex.map(recover, todo), 1):
            (got if r['ok'] else lost).append(r)
            if i % 25 == 0 or i == len(todo):
                print(f'  {i}/{len(todo)}  recovered {len(got)}')

    print(f'\nRECOVERED {len(got)} of {len(todo)}')
    by_via = {}
    for r in got:
        by_via.setdefault(r['via'], []).append(r)
    for via, rows in sorted(by_via.items(), key=lambda kv: -len(kv[1])):
        mb = sum(x['size'] for x in rows) / 1048576
        print(f'  via {via:<16} {len(rows):>4}  ({mb:.1f} MB)')

    if lost:
        hosts = {}
        for r in lost:
            h = re.sub(r'^https?://([^/]+).*', r'\1', r['url'])
            hosts.setdefault(h, []).append(r['name'])
        print(f'\nUNRECOVERABLE {len(lost)} — the file is gone from every route:')
        for h, names in sorted(hosts.items(), key=lambda kv: -len(kv[1])):
            uniq = sorted(set(names))
            print(f'  {h:<40} {len(names):>4}  {", ".join(uniq[:4])}'
                  + (' ...' if len(uniq) > 4 else ''))

    if not args.write:
        print(f'\n(dry run — re-run with --write to save {len(got)} file(s) into '
              f'{CACHE})')
        return 0

    os.makedirs(CACHE, exist_ok=True)
    written = 0
    for r in got:
        dst = os.path.join(CACHE, cache_stem(r['url']) + '.obj')
        try:
            with open(dst, 'wb') as fh:
                fh.write(r['data'])
            written += 1
        except Exception as e:
            print(f'  write failed for {r["name"]}: {e}')
    print(f'\nwrote {written} file(s) into {CACHE}')
    print('TTS reads that cache by filename, so RESTART TTS (or reload the mod) and '
          'those models will appear with no popup.')
    print('Then re-run browse_models.py to see them in the gallery.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

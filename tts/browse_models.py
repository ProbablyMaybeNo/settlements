# -*- coding: utf-8 -*-
"""Browse the models in a TTS mod as an HTML gallery — without loading the mod.

TTS has no model browser. The only way to see what a pack contains is to load its
table and fly the camera around 900 objects, which is exactly the thing that
triggers a popup storm when the pack has dead asset links.

This renders them instead. Two things make it cheap:

  * TTS ALREADY CACHED THE MESHES. Every model it has ever fetched sits in
    `Mods/Models/` as a .obj, named after its URL with the punctuation stripped.
    So there is nothing to download, and even assets whose original host is now
    dead still render — TTS grabbed them while the host was alive.
  * NO RENDER DEPENDENCIES. matplotlib and pyglet are not installed and Blender
    would take ~40 minutes for 800 models, so this uses a small orthographic
    software renderer: project, z-sort, flat-shade by face normal. Fast, and
    plenty to recognise a piece by.

    py -3.13 browse_models.py                      # every subscribed mod
    py -3.13 browse_models.py --id 1940563574      # one mod
    py -3.13 browse_models.py --size 200 --open    # bigger thumbs, then open it
"""
import argparse
import html
import json
import os
import re
import sys
import webbrowser

import numpy as np
import trimesh
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
TTS = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                   'Tabletop Simulator', 'Mods')
WORKSHOP = os.path.join(TTS, 'Workshop')
CACHE = os.path.join(TTS, 'Models')
CACHE_RAW = os.path.join(TTS, 'Models Raw')
OUT = os.path.join(HERE, 'assets', 'gallery')


def cache_name(url):
    """TTS names its cache files after the URL with every non-alphanumeric
    character removed. Derived by inspection of the live cache, not documented."""
    return re.sub(r'[^A-Za-z0-9]', '', url or '')


def find_cached(url):
    stem = cache_name(url)
    if not stem:
        return None
    for d in (CACHE, CACHE_RAW):
        p = os.path.join(d, stem + '.obj')
        if os.path.isfile(p):
            return p
    # some entries land with a different extension or truncated name
    for d in (CACHE, CACHE_RAW):
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.startswith(stem[:80]) and f.lower().endswith(('.obj', '.bin')):
                return os.path.join(d, f)
    return None


def render(mesh, px, bg=(24, 24, 27)):
    """Orthographic 3/4 view, flat-shaded by face normal, painter's algorithm."""
    img = Image.new('RGB', (px, px), bg)
    d = ImageDraw.Draw(img)
    v = np.asarray(mesh.vertices, dtype=np.float64)
    f = np.asarray(mesh.faces)
    if len(f) == 0:
        return img

    # centre, then rotate: 30 deg down, 40 deg around, so nothing reads as a
    # flat slab and you can tell a tower from a footprint
    v = v - v.mean(axis=0)
    ay, ax = np.radians(40), np.radians(30)
    Ry = np.array([[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]])
    Rx = np.array([[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]])
    v = v @ Ry.T @ Rx.T

    span = max(v.max(axis=0) - v.min(axis=0))
    if span <= 0:
        return img
    s = (px * 0.82) / span
    xy = v[:, :2] * s
    xy[:, 1] *= -1                      # screen y grows downward
    xy += px / 2.0

    tri = v[f]
    depth = tri[:, :, 2].mean(axis=1)
    n = np.cross(tri[:, 1] - tri[:, 0], tri[:, 2] - tri[:, 0])
    ln = np.linalg.norm(n, axis=1)
    ln[ln == 0] = 1
    n = n / ln[:, None]
    light = np.array([0.35, 0.55, 0.75])
    light = light / np.linalg.norm(light)
    shade = np.clip(n @ light, 0, 1) * 0.75 + 0.25

    for i in np.argsort(depth):            # far to near
        a, b, c = xy[f[i]]
        g = shade[i]
        col = (int(150 * g + 30), int(152 * g + 30), int(146 * g + 28))
        d.polygon([tuple(a), tuple(b), tuple(c)], fill=col)
    return img


def mod_assets(path):
    with open(path, encoding='utf-8', errors='replace') as fh:
        mod = json.load(fh)
    out, stack = [], list(mod.get('ObjectStates') or [])
    while stack:
        o = stack.pop()
        if not isinstance(o, dict):
            continue
        stack.extend(o.get('ContainedObjects') or [])
        cm = o.get('CustomMesh') or {}
        if cm.get('MeshURL'):
            out.append(dict(nick=(o.get('Nickname') or '').strip() or '(unnamed)',
                            mesh=cm['MeshURL'], diffuse=cm.get('DiffuseURL', '') or ''))
    seen, uniq = set(), []
    for r in out:
        if r['mesh'] in seen:
            continue
        seen.add(r['mesh'])
        uniq.append(r)
    return mod.get('SaveName') or os.path.basename(path)[:-5], uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--id', action='append', help='workshop id (repeatable)')
    ap.add_argument('--size', type=int, default=150, help='thumbnail px')
    ap.add_argument('--open', action='store_true', help='open the gallery when done')
    ap.add_argument('--limit', type=int, default=None)
    args = ap.parse_args()

    if not os.path.isdir(WORKSHOP):
        print(f'no workshop dir: {WORKSHOP}', file=sys.stderr)
        return 1
    os.makedirs(os.path.join(OUT, 'thumbs'), exist_ok=True)

    files = []
    for f in sorted(os.listdir(WORKSHOP)):
        if not f.endswith('.json') or f.startswith('WorkshopFileInfos'):
            continue
        if args.id and not any(f.startswith(str(i)) for i in args.id):
            continue
        files.append(os.path.join(WORKSHOP, f))

    mods, done, missing, failed = [], 0, 0, 0
    index, counter = {}, 0
    for path in files:
        name, assets = mod_assets(path)
        # STABLE ORDER. Numbers are only useful if they mean the same thing every
        # run, so sort by mesh URL — the one field that never changes — rather
        # than by nickname, which is blank for most of these.
        assets.sort(key=lambda a: a['mesh'])
        if args.limit:
            assets = assets[:args.limit]
        rows = []
        print(f'--- {name}  ({len(assets)} models)')
        for a in assets:
            stem = cache_name(a['mesh'])[:90]
            thumb_rel = os.path.join('thumbs', stem + '.png')
            thumb_abs = os.path.join(OUT, thumb_rel)
            status = 'cached'
            if not os.path.isfile(thumb_abs):
                src = find_cached(a['mesh'])
                if src is None:
                    status = 'not cached'
                    missing += 1
                else:
                    try:
                        m = trimesh.load(src, force='mesh', process=False)
                        if m is None or not hasattr(m, 'faces') or len(m.faces) == 0:
                            raise ValueError('no geometry')
                        render(m, args.size).save(thumb_abs, optimize=True)
                        done += 1
                    except Exception as e:
                        status = f'render failed: {type(e).__name__}'
                        failed += 1
            dims = ''
            if status == 'cached' and os.path.isfile(thumb_abs):
                src = find_cached(a['mesh'])
                try:
                    m = trimesh.load(src, force='mesh', process=False)
                    e = m.extents
                    dims = f'{e[0]:.0f}x{e[1]:.0f}x{e[2]:.0f}'
                except Exception:
                    pass
            counter += 1
            rows.append(dict(num=counter, nick=a['nick'],
                             thumb=thumb_rel.replace(os.sep, '/'),
                             status=status, dims=dims,
                             host=re.sub(r'^https?://([^/]+).*', r'\1', a['mesh'])))
            index[str(counter)] = dict(mod=name, nick=a['nick'], mesh=a['mesh'],
                                       diffuse=a['diffuse'], dims=dims, status=status)
        mods.append((name, rows))
        print(f'    {sum(1 for r in rows if r["status"] == "cached")} renderable')

    # --- the gallery ------------------------------------------------------
    css = """
    body{background:#18181b;color:#e4e4e7;font:14px/1.5 -apple-system,Segoe UI,sans-serif;margin:0;padding:24px}
    h1{font-size:20px;margin:0 0 4px} h2{font-size:16px;margin:32px 0 12px;
      border-bottom:1px solid #3f3f46;padding-bottom:6px;color:#fafafa}
    .meta{color:#a1a1aa;font-size:13px;margin-bottom:20px}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}
    .card{background:#27272a;border:1px solid #3f3f46;border-radius:8px;padding:8px;
      text-align:center;overflow:hidden}
    .card img{width:100%;height:auto;border-radius:4px;background:#18181b;display:block}
    .n{font-size:12px;margin-top:4px;color:#d4d4d8;overflow-wrap:anywhere}
    .num{position:absolute;top:6px;left:6px;background:#fbbf24;color:#18181b;
      font-weight:700;font-size:13px;padding:1px 7px;border-radius:4px}
    .card{position:relative}
    .d{font-size:11px;color:#a1a1aa}
    .bad{color:#f87171;font-size:11px;padding:24px 4px;display:block}
    input{background:#27272a;border:1px solid #52525b;color:#fafafa;padding:8px 12px;
      border-radius:6px;width:280px;font-size:14px;margin-bottom:8px}
    """
    js = """
    const box=document.getElementById('q');
    box.addEventListener('input',()=>{const v=box.value.toLowerCase();
      document.querySelectorAll('.card').forEach(c=>{
        c.style.display=c.dataset.n.includes(v)?'':'none';});
      document.querySelectorAll('h2').forEach(h=>{
        const g=h.nextElementSibling;
        h.style.display=[...g.querySelectorAll('.card')].some(c=>c.style.display!=='none')?'':'none';
        g.style.display=h.style.display;});});
    """
    total = sum(len(r) for _, r in mods)
    parts = [f'<!doctype html><meta charset="utf-8"><title>TTS model gallery</title>',
             f'<style>{css}</style>',
             f'<h1>TTS model gallery</h1>',
             f'<div class="meta">{total} models across {len(mods)} mod(s) · '
             f'rendered from TTS\'s own local cache, so no network and no dead-host '
             f'problem · {done} newly rendered, {missing} not cached, {failed} failed'
             f'</div>',
             '<div class="meta">Every tile has a <b>number</b> — tell Claude the '
             'numbers you want (e.g. "add 12, 40, 55-60") and they get spawned as '
             'a bag on the table.</div>',
             '<input id="q" placeholder="filter by name or number...">']
    for name, rows in mods:
        parts.append(f'<h2>{html.escape(name)} <span class="d">'
                     f'({len(rows)})</span></h2><div class="grid">')
        for r in rows:
            n = html.escape(r['nick'])
            if r['status'] == 'cached':
                parts.append(
                    f'<div class="card" data-n="{n.lower()} {r["num"]}">'
                    f'<span class="num">{r["num"]}</span>'
                    f'<img src="{r["thumb"]}" loading="lazy" alt="{n}">'
                    f'<div class="n">{n}</div>'
                    f'<div class="d">{r["dims"]}</div></div>')
            else:
                parts.append(
                    f'<div class="card" data-n="{n.lower()} {r["num"]}">'
                    f'<span class="num">{r["num"]}</span>'
                    f'<span class="bad">{html.escape(r["status"])}</span>'
                    f'<div class="n">{n}</div>'
                    f'<div class="d">{html.escape(r["host"])}</div></div>')
        parts.append('</div>')
    parts.append(f'<script>{js}</script>')

    out_html = os.path.join(OUT, 'index.html')
    with open(out_html, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(parts))
    # the number -> asset map, so a pick like "#42" is resolvable later
    idx_path = os.path.join(OUT, 'numbers.json')
    with open(idx_path, 'w', encoding='utf-8') as fh:
        json.dump(index, fh, indent=1)
    print(f'\n{total} models · {done} newly rendered · {missing} not in cache · '
          f'{failed} failed')
    print(f'gallery: {out_html}')
    print(f'numbers: {idx_path}')
    if args.open:
        webbrowser.open('file:///' + out_html.replace(os.sep, '/'))
    return 0


if __name__ == '__main__':
    sys.exit(main())

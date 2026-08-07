# -*- coding: utf-8 -*-
"""Inventory subscribed Workshop mods and pull out reusable assets.

WHY THIS BEATS THE FILE PIPELINE FOR WORKSHOP CONTENT. `import_models.py` converts
files you downloaded. Workshop mods need none of that: every custom object already
carries its MeshURL / ColliderURL / DiffuseURL pointing at a CDN, already has a
collider the author built, and already works in multiplayer because the assets are
hosted. Reading those URLs out of the mod JSON and re-using them is strictly less
work and strictly better than re-converting geometry.

    py -3.13 scan_mods.py                       # inventory everything subscribed
    py -3.13 scan_mods.py --id 1210066713       # one mod
    py -3.13 scan_mods.py --grep soldier        # find objects by name
    py -3.13 scan_mods.py --id 1210066713 --emit units.json

LICENCE, PLAINLY: these are other people's models. Fine for private play — that is
what the Workshop is for. Not fine in a commercial Settlements release. For
anything shipped, our own OpenSCAD terrain (`make_models.py`) is the answer.
"""
import argparse
import json
import os
import sys
from collections import Counter

WORKSHOP = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                        'Tabletop Simulator', 'Mods', 'Workshop')
HERE = os.path.dirname(os.path.abspath(__file__))

# Rough buckets, by keyword in the object's nickname. Crude on purpose — it is a
# sorting aid for a human picking pieces, not a classifier to trust.
BUCKETS = {
    'infantry': ('soldier', 'infantry', 'trooper', 'marine', 'rifle', 'gunner', 'squad',
                 'sniper', 'officer', 'medic', 'engineer', 'militia', 'civilian', 'man',
                 'woman', 'figure', 'mini'),
    'building': ('building', 'house', 'shop', 'store', 'garage', 'warehouse', 'tower',
                 'apartment', 'office', 'church', 'school', 'factory', 'hangar', 'ruin',
                 'shed', 'barn', 'home', 'motel', 'diner', 'station'),
    'scatter':  ('crate', 'barrel', 'barricade', 'sandbag', 'fence', 'wall', 'debris',
                 'rubble', 'dumpster', 'bin', 'container', 'pallet', 'tyre', 'tire',
                 'rock', 'tree', 'bush', 'hedge', 'planter', 'sign', 'pole', 'lamp'),
    'vehicle':  ('car', 'truck', 'van', 'tank', 'apc', 'humvee', 'jeep', 'bus',
                 'vehicle', 'trailer', 'helicopter', 'drone'),
    'token':    ('token', 'marker', 'counter', 'chip', 'objective', 'flag'),
}


def bucket_of(name):
    n = (name or '').lower()
    for b, keys in BUCKETS.items():
        if any(k in n for k in keys):
            return b
    return 'other'


def walk(states, out, depth=0):
    """Recurse ObjectStates and ContainedObjects (bags hold most of the good stuff)."""
    for o in states or []:
        if not isinstance(o, dict):
            continue
        nick = (o.get('Nickname') or '').strip()
        kind = o.get('Name') or ''
        mesh = o.get('CustomMesh') or {}
        image = o.get('CustomImage') or {}
        t = o.get('Transform') or {}
        rec = None
        if mesh.get('MeshURL'):
            rec = dict(nickname=nick or '(unnamed)', kind=kind,
                       mesh=mesh.get('MeshURL', ''),
                       collider=mesh.get('ColliderURL', '') or '',
                       diffuse=mesh.get('DiffuseURL', '') or '',
                       convex=bool(mesh.get('Convex', False)),
                       scale=[round(float(t.get(f'scale{a}', 1) or 1), 3) for a in 'XYZ'],
                       asset='model')
        elif image.get('ImageURL'):
            rec = dict(nickname=nick or '(unnamed)', kind=kind,
                       mesh='', collider='', diffuse=image.get('ImageURL', ''),
                       convex=False,
                       scale=[round(float(t.get(f'scale{a}', 1) or 1), 3) for a in 'XYZ'],
                       asset='image')
        if rec:
            rec['bucket'] = bucket_of(nick)
            out.append(rec)
        walk(o.get('ContainedObjects'), out, depth + 1)


def load_mod(path):
    with open(path, encoding='utf-8', errors='replace') as fh:
        return json.load(fh)


def mod_files(only_id=None):
    if not os.path.isdir(WORKSHOP):
        return []
    fs = []
    for f in sorted(os.listdir(WORKSHOP)):
        if not f.endswith('.json') or f.startswith('WorkshopFileInfos'):
            continue
        if only_id and not f.startswith(str(only_id)):
            continue
        fs.append(os.path.join(WORKSHOP, f))
    return fs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--id', help='only this workshop id')
    ap.add_argument('--grep', help='only objects whose nickname contains this')
    ap.add_argument('--bucket', help='only this bucket: ' + ', '.join(BUCKETS) + ', other')
    ap.add_argument('--emit', help='write the matching records to this json file')
    ap.add_argument('--max-mb', type=float, default=40.0,
                    help='skip mods larger than this (baked map saves are huge and '
                         'mostly contain one flat table image)')
    args = ap.parse_args()

    files = mod_files(args.id)
    if not files:
        print(f'no mods found in {WORKSHOP}', file=sys.stderr)
        return 1

    everything = []
    for path in files:
        mb = os.path.getsize(path) / 1048576
        mid = os.path.basename(path)[:-5]
        if mb > args.max_mb and not args.id:
            print(f'-- {mid}  ({mb:.0f} MB)  SKIPPED, over --max-mb')
            continue
        try:
            mod = load_mod(path)
        except Exception as e:
            print(f'-- {mid}  unreadable: {type(e).__name__}')
            continue
        recs = []
        walk(mod.get('ObjectStates'), recs)
        name = mod.get('SaveName') or mid
        uniq = {}
        for r in recs:
            key = (r['nickname'], r['mesh'] or r['diffuse'])
            uniq.setdefault(key, r)
        recs = list(uniq.values())
        for r in recs:
            r['mod'] = name
            r['mod_id'] = mid
        everything.extend(recs)
        counts = Counter(r['bucket'] for r in recs)
        print(f'-- {name}  ({mid}, {mb:.1f} MB)')
        print(f'   {len(recs)} unique custom assets  ' +
              '  '.join(f'{b}:{c}' for b, c in counts.most_common()))

    sel = everything
    if args.grep:
        g = args.grep.lower()
        sel = [r for r in sel if g in r['nickname'].lower()]
    if args.bucket:
        sel = [r for r in sel if r['bucket'] == args.bucket]

    print(f'\n{"=" * 92}')
    print(f'{len(sel)} asset(s)' + (' matching your filter' if (args.grep or args.bucket) else ''))
    by_bucket = {}
    for r in sel:
        by_bucket.setdefault(r['bucket'], []).append(r)
    for b in sorted(by_bucket, key=lambda k: -len(by_bucket[k])):
        rows = by_bucket[b]
        print(f'\n[{b}]  {len(rows)}')
        for r in sorted(rows, key=lambda x: x['nickname'])[:24]:
            col = 'collider' if r['collider'] else ('convex' if r['convex'] else 'NO COLLIDER')
            print(f'   {r["nickname"][:44]:<44} {r["kind"][:14]:<14} {col:<12} '
                  f'scale {r["scale"][0]:g}  [{r["mod"][:24]}]')
        if len(rows) > 24:
            print(f'   ... and {len(rows) - 24} more')

    if args.emit:
        out = args.emit if os.path.isabs(args.emit) else os.path.join(HERE, args.emit)
        with open(out, 'w', encoding='utf-8') as fh:
            json.dump(sel, fh, indent=2)
        print(f'\nwrote {len(sel)} records -> {out}')
        print('These carry live MeshURL/ColliderURL/DiffuseURL, so build_table.py can')
        print('place them directly — no conversion, and they work in multiplayer.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

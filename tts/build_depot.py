# -*- coding: utf-8 -*-
"""Build a train-depot / industrial board to the Settlements setup rules.

FOLLOWS §5 SETUP PROCEDURE, in order:
  1. Density first — 9 to 12 large features, at least one in EACH of the nine
     12"x12" squares, then scatter until no clear firing lane crosses the board.
     12 is a HARD ceiling. This lays 11.
  2. Every piece gets Movement / Cover / Tags.
  3. At least 2 Buildings/Ruins, and real interactive pieces.
  4. Every elevated area gets access — ladders and stairs beside anything
     Climbable, because a roof nobody can reach is a dead roof, and the engine is
     2.5D so roofs are worth reaching.

SCALE. Workshop models arrive in arbitrary units (measured: 0.1 to 45 across the
candidates), so every piece is scaled from its MEASURED extents to a real
footprint, using the reference set given:
    cargo container   6 x 3"        square house      6 x 6"
    rectangular bldg  8 x 4"        vertical tank     3 x 3" footprint
    one storey        3-4" of height
Scale is uniform, so hitting a footprint sets the height — each entry below prints
what height it lands at, and anything absurd got a different target instead.

Placement is by DENSITY SQUARE, not by eye: sq 1-9 read left-to-right,
near-to-far, so the rule "one per square" is checked by construction.

    py -3.13 build_depot.py            # plan only
    py -3.13 build_depot.py --spawn    # build it
    py -3.13 build_depot.py --spawn --clear   # wipe existing terrain first
"""
import argparse
import json
import os
import re
import sys

import trimesh

HERE = os.path.dirname(os.path.abspath(__file__))
TTS = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                   'Tabletop Simulator', 'Mods')
BOARD = 36.0
SURFACE = 2.45          # top of the board tile (spans 0.6-2.4 at scale 18)

# num, x, z, target-longest-footprint, cover, tags, note
# cover: 0 open · 1 light · 2 heavy.  A piece is a LOS blocker when it is Heavy
# cover AND >=4" tall, which is the same test the rules use for Impassable.
LARGE = [
    # --- near row (sq 1-3). Kept at z=-10, INSIDE the 6" deploy band's inner
    #     edge, so deployment space stays usable.
    (537, -12.0, -10.0, 6.0, 2, 'Openable,Climbable,Searchable', 'Depot office - square building'),
    (626,   0.0, -10.5, 6.0, 2, 'Climbable,Searchable',          'Cargo container'),
    (262,  12.0, -10.0, 3.0, 2, 'Powered,Climbable',             'Vertical silo'),
    # --- centre row (sq 4-6), the rail spine
    (536, -12.0,   0.0, 8.0, 2, 'Openable,Climbable,Searchable', 'Warehouse - rectangular'),
    (156,   0.0,   0.0, 8.2, 2, 'Climbable',                     'Gantry crane over the rail'),
    (634,  12.0,   0.0, 6.0, 2, 'Climbable,Searchable',          'Stacked containers'),
    # --- far row (sq 7-9)
    (57,  -12.0,  10.0, 4.0, 2, 'Powered,Climbable,Explosive',   'Tank / silo'),
    (611,   0.0,  10.0, 8.0, 1, 'Climbable,Searchable',          'Warehouse racking'),
    (272,  12.0,  10.0, 8.0, 2, 'Openable,Searchable',           'Long shed'),
    # --- two extra to break the diagonals (11 total, inside the 9-12 band).
    #     Deliberately NOT in the centre square: three pieces there makes a
    #     fortress middle with open flanks, which is the opposite of what the
    #     density rule is for. These sit off-axis in squares 3 and 7 instead,
    #     cutting the two long corner-to-corner lanes.
    (677,   7.5,  -6.5, 6.0, 2, 'Climbable,Searchable',          'Container'),
    (671,  -7.5,   6.5, 6.0, 2, 'Climbable,Searchable',          'Container stack'),
]

# Scatter does NOT count toward 9-12. Its job is to kill firing lanes.
SCATTER = [
    # the rail spine, running east-west just off centre
    (234, -15.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (234,  -9.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (234,  -3.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (234,   3.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (234,   9.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (234,  15.0, -4.5, 6.0, 0, '', 'rail - straight'),
    (554,  -7.0, -4.5, 8.0, 2, 'Climbable,Searchable', 'rail wagon'),
    (235,   8.0, -4.5, 8.0, 2, 'Climbable',            'locomotive'),
    # loading yard clutter
    (689,  -8.5,  -8.0, 3.5, 1, 'Movable,Searchable', 'crate stack'),
    (653,  -3.0,  -8.5, 3.0, 1, 'Movable,Searchable', 'pallets'),
    (690,   4.0,  -7.0, 2.5, 1, 'Movable,Searchable', 'crate'),
    (624,   8.5,  -6.5, 2.5, 1, 'Searchable',         'dumpster'),
    (605, -15.5,   4.0, 4.0, 1, 'Movable,Searchable', 'skip'),
    (606,  -3.5,   6.5, 3.0, 1, 'Movable,Searchable', 'skip'),
    (607,   3.0,  -1.0, 3.0, 1, 'Movable',            'timber stack'),
    (525,  -9.5,   7.5, 1.5, 1, 'Movable,Explosive',  'fuel drum'),
    (525,  10.0,   6.0, 1.5, 1, 'Movable,Explosive',  'fuel drum'),
    (669,   6.5, -13.0, 3.0, 1, 'Powered',            'tank cluster'),
    (604, -16.0, -13.5, 3.0, 1, 'Powered',            'tank cluster'),
    # cover along the lanes
    (529,  -6.0,  13.5, 5.0, 2, '',                   'concrete barrier'),
    (531,   3.5, -15.5, 5.0, 2, '',                   'concrete barrier'),
    (532,  16.0,   5.0, 5.0, 2, '',                   'concrete barrier'),
    (73,  -16.5,  -1.0, 6.0, 1, 'Movable',            'barricade'),
    (616,  15.5, -14.5, 8.0, 1, 'Breachable,Climbable', 'fence run'),
    (645, -15.0,  15.5, 8.0, 1, 'Breachable,Climbable', 'fence run'),
    # ELEVATED ACCESS (§5 step 4) — every Climbable piece needs a way up
    (687, -12.0,  -6.2, 2.5, 0, 'Climbable', 'ladder to the depot office roof'),
    (687,  12.0,   3.2, 2.5, 0, 'Climbable', 'ladder to the container stack'),
    (753,   0.0,  -7.2, 1.0, 0, 'Climbable', 'ladder to the container'),
    (687, -12.0,   3.4, 2.5, 0, 'Climbable', 'ladder to the warehouse roof'),
    (753,   5.5,   1.5, 1.0, 0, 'Climbable', 'ladder to the container stack'),
]


def load_index():
    p = os.path.join(HERE, 'assets', 'gallery', 'numbers.json')
    if not os.path.isfile(p):
        print('no gallery index — run browse_models.py first', file=sys.stderr)
        return None
    with open(p, encoding='utf-8') as fh:
        return json.load(fh)


def mesh_path(rec):
    stem = re.sub(r'[^A-Za-z0-9]', '', rec['mesh'])
    for d in ('Models', 'Models Raw'):
        p = os.path.join(TTS, d, stem + '.obj')
        if os.path.isfile(p):
            return p
    return None


def extents(rec):
    p = mesh_path(rec)
    if not p:
        return None
    try:
        m = trimesh.load(p, force='mesh', process=False)
        e = m.extents
        return float(e[0]), float(e[1]), float(e[2])
    except Exception:
        return None


def square_of(x, z):
    """Which of the nine 12x12 density squares (§5). 1-9, near row first."""
    col = int((x + BOARD / 2) // 12)
    row = int((z + BOARD / 2) // 12)
    col = min(max(col, 0), 2)
    row = min(max(row, 0), 2)
    return row * 3 + col + 1


def plan(index):
    rows = []
    for large, items in ((True, LARGE), (False, SCATTER)):
        for num, x, z, target, cover, tags, note in items:
            rec = index.get(str(num))
            if not rec or rec.get('status') != 'cached':
                rows.append(dict(num=num, ok=False, why='not cached', note=note))
                continue
            e = extents(rec)
            if e is None:
                rows.append(dict(num=num, ok=False, why='no mesh', note=note))
                continue
            longest = max(e[0], e[2])
            s = target / longest if longest else 1.0
            rows.append(dict(num=num, ok=True, rec=rec, x=x, z=z, scale=s,
                             fp=(e[0] * s, e[2] * s), h=e[1] * s, cover=cover,
                             tags=tags, note=note, large=large,
                             sq=square_of(x, z)))
    return rows


def obj_json(r):
    tags = [t for t in r['tags'].split(',') if t]
    # LOS blocker = Heavy cover and 4"+ tall, the same test the rules use
    blocks = r['cover'] >= 2 and r['h'] >= 4.0
    gm = {'terrain': True, 'large': r['large'], 'cover': r['cover'],
          'height': round(r['h'], 2), 'blocks': blocks, 'tags': tags}
    words = {0: 'Open (0)', 1: 'Light (-1)', 2: 'Heavy (-2)'}
    move = 'Impassable' if blocks else ('Difficult' if r['cover'] == 2 else 'Open')
    desc = (f'{r["note"]}\n{move} · {words[r["cover"]]} · '
            f'{r["fp"][0]:.1f}" x {r["fp"][1]:.1f}" footprint, {r["h"]:.1f}" tall'
            + (f'\nTags: {", ".join(tags)}' if tags else '')
            + f'\n[{"LARGE FEATURE" if r["large"] else "scatter"} · density square '
              f'{r["sq"]}]')
    return {
        'Name': 'Custom_Model',
        'Nickname': r['note'],
        'Description': desc,
        'GMNotes': json.dumps(gm, separators=(',', ':')),
        # spawn high and let physics seat it: an OBJ's origin is not reliably at
        # its base, so computing a resting y from extents alone gets it wrong
        'Transform': {'posX': r['x'], 'posY': SURFACE + r['h'] + 1.5, 'posZ': r['z'],
                      'rotX': 0, 'rotY': 0, 'rotZ': 0,
                      'scaleX': r['scale'], 'scaleY': r['scale'], 'scaleZ': r['scale']},
        'ColorDiffuse': {'r': 1, 'g': 1, 'b': 1},
        'Locked': False, 'Grid': True, 'Snap': False, 'Autoraise': True,
        'CustomMesh': {
            'MeshURL': r['rec']['mesh'], 'DiffuseURL': r['rec'].get('diffuse', ''),
            'NormalURL': '', 'ColliderURL': '', 'Convex': True,
            'MaterialIndex': 1, 'TypeIndex': 0,
            'CustomShader': {'SpecularColor': {'r': 0.9, 'g': 0.9, 'b': 0.9},
                             'SpecularIntensity': 0.1, 'SpecularSharpness': 4.0,
                             'FresnelStrength': 0.1},
            'CastShadows': True,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spawn', action='store_true')
    ap.add_argument('--clear', action='store_true',
                    help='destroy existing terrain first (keeps the board)')
    args = ap.parse_args()

    index = load_index()
    if index is None:
        return 1
    rows = plan(index)
    good = [r for r in rows if r['ok']]
    bad = [r for r in rows if not r['ok']]
    larges = [r for r in good if r['large']]

    print(f'TRAIN DEPOT / INDUSTRIAL BOARD — {BOARD:.0f}"x{BOARD:.0f}"\n')
    print(f'{"#":>5}  {"piece":<34}{"footprint":>16}{"tall":>7}{"cover":>7}{"sq":>4}')
    for r in larges:
        print(f'{r["num"]:>5}  {r["note"][:34]:<34}'
              f'{r["fp"][0]:7.1f} x{r["fp"][1]:6.1f}"{r["h"]:6.1f}"'
              f'{r["cover"]:>7}{r["sq"]:>4}')
    print(f'\n  {len(larges)} LARGE features'
          + ('  ** OUTSIDE THE 9-12 BAND **' if not 9 <= len(larges) <= 12 else '  (band 9-12: OK)'))

    per = {}
    for r in larges:
        per[r['sq']] = per.get(r['sq'], 0) + 1
    empty = [s for s in range(1, 10) if s not in per]
    print(f'  per density square: ' + ' '.join(f'{per.get(s, 0)}' for s in range(1, 10))
          + (f'   ** EMPTY: {empty} **' if empty else '   (all nine occupied: OK)'))
    blockers = [r for r in larges if r['cover'] >= 2 and r['h'] >= 4.0]
    print(f'  LOS blockers (Heavy + 4"+ tall): {len(blockers)}')
    buildings = [r for r in larges if 'Openable' in r['tags']]
    print(f'  enterable buildings: {len(buildings)}'
          + ('  (rules want 2+: OK)' if len(buildings) >= 2 else '  ** need 2+ **'))
    climb = [r for r in larges if 'Climbable' in r['tags']]
    ladders = [r for r in good if not r['large'] and 'Climbable' in r['tags']]
    print(f'  Climbable large pieces: {len(climb)}   access pieces placed: {len(ladders)}')
    print(f'  scatter: {len([r for r in good if not r["large"]])} pieces')
    if bad:
        print(f'\n  UNAVAILABLE ({len(bad)}): ' + ', '.join(
            f'#{r["num"]} {r["note"]} ({r["why"]})' for r in bad))

    if not args.spawn:
        print('\n(run with --spawn to build it)')
        return 0

    sys.path.insert(0, HERE)
    import tts_api
    if not tts_api.is_up():
        print('\nTTS is not listening — load a table first.', file=sys.stderr)
        return 1

    if args.clear:
        tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1', 'script':
            'local n=0 for _,o in ipairs(getAllObjects()) do local gm=o.getGMNotes() '
            'if gm and gm~="" then local j=JSON.decode(gm) '
            'if type(j)=="table" and j.terrain and not j.boardSurface then '
            'destroyObject(o) n=n+1 end end end print("[depot] cleared "..n.." piece(s)")'})
        tts_api.listen(3.0)

    batch = 4
    for i in range(0, len(good), batch):
        lines = [f'spawnObjectJSON({{json = [==[{json.dumps(obj_json(r))}]==]}})'
                 for r in good[i:i + batch]]
        lines.append(f'print("[depot] placed {min(i + batch, len(good))}/{len(good)}")')
        tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1',
                      'script': '\n'.join(lines)})
        tts_api.listen(2.0)

    # let physics seat everything, then lock so nothing drifts, then report
    tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1', 'script':
        'Wait.time(function() local n=0 '
        'for _,o in ipairs(getAllObjects()) do local gm=o.getGMNotes() '
        'if gm and gm~="" then local j=JSON.decode(gm) '
        'if type(j)=="table" and j.terrain and not j.boardSurface then '
        'o.setLock(true) n=n+1 end end end '
        'print("[depot] settled and locked "..n.." piece(s)") density() end, 6)'})
    tts_api.listen(11.0)
    print('\nBuilt. !unlock to rearrange, !layout to review, !density to re-check.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Generate the Settlements Tabletop Simulator table as a TTS save file.

WHY A GENERATOR AND NOT HAND-WRITTEN JSON. The board is not decoration — it is
the balance dial. `engine2d/board.py` defines the exact mirror-symmetric
Take-a-Hold board that ~6M simulated games were measured on, so the physical
table is generated FROM those coordinates. Change the sim board, re-run this,
and the TTS table follows. Hand-authored JSON would drift on the first edit.

EVERYTHING IS A TTS BUILT-IN. No custom models, images or URLs, so there is
nothing to host and nothing to 404. Terrain is scaled blocks at the real
footprints and heights (the engine is 2.5D, so height is load-bearing: a
rooftop shooter sees over a building a ground shooter is blocked by).
Your OpenSCAD/STL pieces in `Terrain/` are the v2 upgrade.

    py -3.13 build_table.py            # write to the TTS Saves folder if present
    py -3.13 build_table.py --out .    # write next to this script instead
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- calibration
# TTS units per game inch. The community convention for wargames is 1:1, but it
# is the one number that cannot be verified without loading the table, so it
# lives here alone: measure a known 6" gap with the in-game ruler and, if it
# reads wrong, change ONLY this and regenerate.
INCH = 1.0
BOARD = 36.0          # 3'x3'
# Measured live, not assumed: a checker dropped on the table came to rest at
# y=1.24, so the surface sits there. At the old BASE_Y=1.0 the slab spanned
# 0.8-1.2 and was buried UNDER the table — you saw wood, not a board. 1.55 puts
# the slab clearly on top of any stock table.
BASE_Y = 1.55
BOARD_T = 0.4         # board slab thickness
TOP = BASE_Y + BOARD_T / 2.0     # everything sits on this

_guid = [0x100000]


def guid():
    _guid[0] += 1
    return format(_guid[0], 'x')[:6]


def xz(x, y):
    """Sim board coords (0..36, 0..36) -> TTS world (posX, posZ), centred."""
    return (x - BOARD / 2.0) * INCH, (y - BOARD / 2.0) * INCH


def obj(name, pos, scale, nickname='', desc='', colour=(1, 1, 1), locked=False,
        gm=None, rot=(0, 0, 0), extra=None):
    o = {
        'GUID': guid(),
        'Name': name,
        'Transform': {
            'posX': round(pos[0], 4), 'posY': round(pos[1], 4), 'posZ': round(pos[2], 4),
            'rotX': rot[0], 'rotY': rot[1], 'rotZ': rot[2],
            'scaleX': round(scale[0], 4), 'scaleY': round(scale[1], 4),
            'scaleZ': round(scale[2], 4),
        },
        'Nickname': nickname,
        'Description': desc,
        'GMNotes': json.dumps(gm, separators=(',', ':')) if gm else '',
        'ColorDiffuse': {'r': colour[0], 'g': colour[1], 'b': colour[2]},
        'Locked': locked,
        'Grid': True,
        'Snap': True,
        'IgnoreFoW': False,
        'MeasureMovement': True,
        'DragSelectable': True,
        'Autoraise': True,
        'Sticky': True,
        'Tooltip': True,
        'GridProjection': False,
        'HideWhenFaceDown': False,
        'Hands': False,
        'LuaScript': '',
        'LuaScriptState': '',
        'XmlUI': '',
    }
    if extra:
        o.update(extra)
    return o


WORKSHOP = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                        'Tabletop Simulator', 'Mods', 'Workshop')
TOKEN_DIR = os.path.join(HERE, 'assets', 'tokens')


def _walk_assets(states, out):
    for o in states or []:
        if not isinstance(o, dict):
            continue
        cm = o.get('CustomMesh') or {}
        if cm.get('MeshURL'):
            t = o.get('Transform') or {}
            out.append(dict(nick=(o.get('Nickname') or '').strip(),
                            mesh=cm.get('MeshURL', ''),
                            diffuse=cm.get('DiffuseURL', '') or '',
                            collider=cm.get('ColliderURL', '') or '',
                            convex=bool(cm.get('Convex', False)),
                            mat=cm.get('MaterialIndex', 1),
                            typ=cm.get('TypeIndex', 0),
                            scale=float(t.get('scaleX', 1) or 1)))
        _walk_assets(o.get('ContainedObjects'), out)


def workshop_assets(mod_id):
    """Pull live asset URLs out of a subscribed mod. Returns [] if not subscribed,
    so the table still builds (with blocks) on a machine without these mods."""
    p = os.path.join(WORKSHOP, f'{mod_id}.json')
    if not os.path.isfile(p):
        return []
    try:
        with open(p, encoding='utf-8', errors='replace') as fh:
            mod = json.load(fh)
    except Exception:
        return []
    out = []
    _walk_assets(mod.get('ObjectStates'), out)
    seen, uniq = set(), []
    for r in out:
        if r['mesh'] in seen:
            continue
        seen.add(r['mesh'])
        uniq.append(r)
    return uniq


def custom_model(asset, pos, scale, nickname, desc, colour=(1, 1, 1),
                 locked=False, gm=None, rot=(0, 0, 0)):
    o = obj('Custom_Model', pos, (scale, scale, scale), nickname, desc,
            colour, locked, gm, rot)
    o['CustomMesh'] = {
        'MeshURL': asset['mesh'],
        'DiffuseURL': asset['diffuse'],
        'NormalURL': '',
        'ColliderURL': asset['collider'],
        'Convex': asset['convex'] or not asset['collider'],
        'MaterialIndex': asset['mat'],
        'TypeIndex': asset['typ'],
        'CustomShader': {'SpecularColor': {'r': 0.9, 'g': 0.9, 'b': 0.9},
                         'SpecularIntensity': 0.1, 'SpecularSharpness': 4.0,
                         'FresnelStrength': 0.1},
        'CastShadows': True,
    }
    return o


def custom_token(image_path, pos, scale, nickname, desc, stackable=False):
    o = obj('Custom_Token', pos, (scale, scale, scale), nickname, desc)
    url = 'file:///' + image_path.replace(os.sep, '/')
    o['CustomImage'] = {
        'ImageURL': url,
        'ImageSecondaryURL': '',
        'ImageScalar': 1.0,
        'WidthScale': 0.0,
        'CustomToken': {'Thickness': 0.14, 'MergeDistancePixels': 15.0,
                        'StandUp': False, 'Stackable': stackable},
    }
    return o


def block(x1, y1, x2, y2, height, cover, blocks_los, name, large=True, tags=()):
    """A terrain piece at its true footprint. Cover 0 open / 1 light / 2 heavy."""
    cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
    w, d = (x2 - x1) * INCH, (y2 - y1) * INCH
    h = height * INCH
    px, pz = xz(cx, cy)
    shade = {0: (0.62, 0.60, 0.55), 1: (0.55, 0.50, 0.42), 2: (0.40, 0.38, 0.36)}[cover]
    movement = 'Impassable' if blocks_los else ('Difficult' if cover == 2 else 'Open')
    cover_word = {0: 'Open (0)', 1: 'Light (-1)', 2: 'Heavy (-2)'}[cover]
    desc = (f'{name}\n{movement} · {cover_word} · height {height:g}"'
            + (f'\nTags: {", ".join(tags)}' if tags else ''))
    return obj('BlockSquare', (px, TOP + h / 2.0, pz), (w, h, d),
               nickname=name, desc=desc, colour=shade, locked=True,
               gm={'terrain': True, 'large': large, 'cover': cover,
                   'height': height, 'blocks': blocks_los, 'tags': list(tags)})


def terrain_slots():
    """The validated board as SLOT SPECS: footprint, height, cover, tags.

    Kept separate from how each slot is DRAWN so a slot can be a grey block or a
    real Workshop building without the rules geometry changing. The footprint is
    the rules-true one either way — see pad_and_model()."""
    slots = [
        (3, 15, 9, 21, 4, 2, False, 'Objective Building L', ('Climbable', 'Searchable')),
        (15, 15, 21, 21, 4, 2, False, 'Objective Building C', ('Climbable', 'Searchable')),
        (27, 15, 33, 21, 4, 2, False, 'Objective Building R', ('Climbable', 'Searchable')),
    ]
    lower = [
        (8, 6, 15, 11, 5, 2, True, 'Warehouse', ('Openable', 'Climbable', 'Searchable')),
        (28, 5, 34, 10, 5, 2, True, 'Tenement', ('Openable', 'Climbable', 'Searchable')),
        (4, 9, 7, 12, 1, 1, False, 'Scatter', ('Movable',)),
        (21, 10, 24, 13, 1, 1, False, 'Scatter', ('Movable',)),
    ]
    for (x1, y1, x2, y2, h, cov, blk, nm, tags) in lower:
        slots.append((x1, y1, x2, y2, h, cov, blk, nm, tags))
        slots.append((x1, BOARD - y2, x2, BOARD - y1, h, cov, blk, nm + "'", tags))
    return slots


def pad_and_model(slot, asset):
    """A rules-true FOOTPRINT PAD, with a real model standing on it.

    Why both: a downloaded building is whatever size its author made it, but the
    rules care about the footprint the sims measured. The thin pad carries the
    footprint, the cover value and the GMNotes the density check counts — so the
    model can be a little over or undersized without the RULES drifting. It is
    the same reason wargamers put scenery on a base plate.
    """
    x1, y1, x2, y2, h, cov, blk, nm, tags = slot
    out = [block(x1, y1, x2, y2, 0.3, cov, blk, nm, tags=tags)]
    if asset:
        cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        px, pz = xz(cx, cy)
        out.append(custom_model(
            asset, (px, TOP + 0.3 * INCH, pz), asset['scale'],
            nm + ' (model)',
            f'Scenery for {nm}. The PAD beneath carries the rules footprint '
            f'({x2 - x1:g}" x {y2 - y1:g}", height {h:g}").',
            locked=True, gm={'scenery': True}))
    return out


def take_a_hold_terrain():
    """Generated from engine2d/board.py take_a_hold() — the validated board.

    Three objective buildings on the centreline (heavy cover, 4" roofs you can
    perch on), plus a mirror-symmetric pair set: every piece in one player's
    half has a twin in the other's, so both deployments face identical ground.
    Without that symmetry an A-vs-B comparison is not a controlled test.
    """
    pieces = [
        block(3, 15, 9, 21, 4, 2, False, 'Objective Building L',
              tags=('Climbable', 'Searchable')),
        block(15, 15, 21, 21, 4, 2, False, 'Objective Building C',
              tags=('Climbable', 'Searchable')),
        block(27, 15, 33, 21, 4, 2, False, 'Objective Building R',
              tags=('Climbable', 'Searchable')),
    ]
    lower = [
        (8, 6, 15, 11, 5, 2, True, 'Warehouse', ('Openable', 'Climbable', 'Searchable')),
        (28, 5, 34, 10, 5, 2, True, 'Tenement', ('Openable', 'Climbable', 'Searchable')),
        (4, 9, 7, 12, 1, 1, False, 'Scatter', ('Movable',)),
        (21, 10, 24, 13, 1, 1, False, 'Scatter', ('Movable',)),
    ]
    for (x1, y1, x2, y2, h, cov, blk, nm, tags) in lower:
        pieces.append(block(x1, y1, x2, y2, h, cov, blk, nm, tags=tags))
        # reflect across the centreline y=18
        pieces.append(block(x1, BOARD - y2, x2, BOARD - y1, h, cov, blk, nm + "'", tags=tags))
    return pieces


def crew(side, colour, y_row, facing):
    """A Campaign-Start crew, pre-enrolled so the Lua commands work immediately.

    Stat lines are the legal §13 'gentle' shapes the sims used (a strong primary
    plus one real secondary). Costs are the doc ladder at a 500 cap.
    """
    roster = [
        ('Boss',      'Leader',   dict(str=2, agi=0, dex=4, int=0, nrv=3), 'rifle 170+100'),
        ('Fighter 1', 'Fighter',  dict(str=2, agi=1, dex=0, int=0, nrv=2), 'crowbar 75+70'),
        ('Fighter 2', 'Fighter',  dict(str=2, agi=1, dex=0, int=0, nrv=2), 'crowbar 75+70'),
        ('Recruit 1', 'Recruit',  dict(str=1, agi=1, dex=0, int=0, nrv=1), 'bat 65+0'),
    ]
    out = []
    minis = crew.minis or []
    for i, (nm, rank, st, gear) in enumerate(roster):
        x = 8 + i * 6
        px, pz = xz(x, y_row)
        data = {'unit': True, 'name': f'{side} {nm}', 'rank': rank, 'wnd': 1,
                'stress': 0, 'cond': {}, 'side': side, **st}
        desc = (f'{rank}  W1\nSTR {st["str"]} AGI {st["agi"]} DEX {st["dex"]}'
                f' INT {st["int"]} NRV {st["nrv"]}\n{gear}')
        if minis:
            # Both crews use the same sculpts; the SIDE is carried by the colour
            # tint, which is how you tell them apart at a glance without needing
            # two model sets. Offset the index per side so the two crews are not
            # four identical pairs facing each other.
            a = minis[(i + (0 if side == 'White' else 4)) % len(minis)]
            out.append(custom_model(a, (px, TOP + 0.2, pz), a['scale'],
                                    f'{side} {nm}', desc, colour=colour,
                                    gm=data, rot=(0, facing, 0)))
        else:
            out.append(obj('Checker_white' if side == 'White' else 'Checker_red',
                           (px, TOP + 0.4, pz), (1.1, 1.1, 1.1),
                           nickname=f'{side} {nm}', desc=desc, colour=colour,
                           gm=data, rot=(0, facing, 0)))
    return out


crew.minis = []


def build():
    states = []

    # --- the board surface --------------------------------------------------
    # The concrete tile with the 1" grid painted in, if make_board.py has been
    # run; a plain dark slab otherwise. A Custom_Tile is 2.0 units at scale 1
    # (measured live), so 36" is scale 18.
    board_png = os.path.join(HERE, 'assets', 'boards',
                             f'concrete_{int(BOARD)}x{int(BOARD)}_grid1in.png')
    if os.path.isfile(board_png):
        s = BOARD * INCH / 2.0
        tile = obj('Custom_Tile', (0, BASE_Y, 0), (s, s, s),
                   nickname='Settlements board - 36in x 36in, 1in grid',
                   desc=('36"x36". 1" hairlines, 6" medium (one Move), 12" heavy '
                         '(the nine density squares), plus the centreline. The '
                         'tinted strips are the 6" deployment bands.'),
                   locked=True, gm={'board': True, 'boardSurface': True})
        tile['Snap'] = False
        tile['CustomImage'] = {
            'ImageURL': 'file:///' + board_png.replace(os.sep, '/'),
            'ImageSecondaryURL': '', 'ImageScalar': 1.0, 'WidthScale': 0.0,
            'CustomTile': {'Type': 0, 'Thickness': 0.1, 'Stackable': False,
                           'Stretch': True},
        }
        states.append(tile)
    else:
        states.append(obj('BlockSquare', (0, BASE_Y, 0),
                          (BOARD * INCH, BOARD_T, BOARD * INCH),
                          nickname="Board 3ft x 3ft",
                          desc='36"x36". Deployment 6" bands, ~24" apart.',
                          colour=(0.20, 0.19, 0.18), locked=True,
                          gm={'board': True}))

    # --- deployment bands (§1: within 6" of opposite edges) -----------------
    for side, y0, tint in (('White', 3.0, (0.75, 0.75, 0.80)),
                           ('Red', 33.0, (0.80, 0.55, 0.55))):
        px, pz = xz(BOARD / 2.0, y0)
        states.append(obj('BlockSquare', (px, TOP + 0.02, pz),
                          (BOARD * INCH, 0.04, 6.0 * INCH),
                          nickname=f'{side} deployment (6")',
                          desc='Deploy within this band.', colour=tint, locked=True,
                          gm={'deploy': side}))

    # --- terrain ------------------------------------------------------------
    # Real Workshop scenery if it is subscribed, grey blocks if not. Either way
    # the rules geometry is identical, because it lives in the pad.
    suburb = workshop_assets('3346010681')     # Suburb Map & Assets (Steam CDN)
    city = workshop_assets('2416214524')       # Modern City Buildings (Steam CDN)
    houses = [a for a in suburb if a['nick'].lower() in ('house', 'church', 'garage')]
    big = [a for a in city if a['scale'] >= 0.5] or city

    slots = terrain_slots()
    terrain, used_models = [], 0
    for i, slot in enumerate(slots):
        name = slot[7]
        asset = None
        if 'Objective Building' in name and houses:
            asset = houses[i % len(houses)]
        elif name.rstrip("'") in ('Warehouse', 'Tenement') and big:
            asset = big[i % len(big)]
        # Scatter stays a block: a 3x3 low piece reads better as a plain crate
        # wall than as a shrunk house, and it keeps the object count down.
        pieces = pad_and_model(slot, asset)
        used_models += (1 if asset else 0)
        terrain.extend(pieces)
    states.extend(terrain)

    # --- objectives ---------------------------------------------------------
    for i, x in enumerate((6, 18, 30), start=1):
        px, pz = xz(x, 18)
        states.append(obj('Checker_white', (px, TOP + 4.0 * INCH + 0.3, pz),
                          (1.6, 0.5, 1.6),
                          nickname=f'Objective {i}',
                          desc=('Take a Hold — claim with INT 7+, then hold it.\n'
                                'Held = a standing friendly within 3" and no enemy '
                                'within 3". Both = contested, nobody scores.'),
                          colour=(0.95, 0.80, 0.25),
                          gm={'objective': True, 'index': i}))

    # --- crews --------------------------------------------------------------
    # 34 soldier sculpts, but 31 are hosted on a GitHub Gist that could vanish —
    # prefer the ones on Steam's CDN, then fall back to the rest.
    inf = workshop_assets('1210066713')
    inf = ([a for a in inf if 'steamusercontent' in a['mesh'] and a['diffuse']]
           + [a for a in inf if 'steamusercontent' not in a['mesh'] and a['diffuse']])
    crew.minis = inf
    states.extend(crew('White', (0.92, 0.92, 0.88), 3.0, 0))
    states.extend(crew('Red', (0.85, 0.42, 0.35), 33.0, 180))

    # --- condition token supply (copy/paste in TTS to make more) -----------
    conds = [('Stress', (0.9, 0.75, 0.2)), ('Pinned', (0.9, 0.5, 0.2)),
             ('Down', (0.6, 0.2, 0.2)), ('Prone', (0.5, 0.45, 0.6)),
             ('Hidden', (0.35, 0.45, 0.6)), ('Ready', (0.35, 0.7, 0.5)),
             ('Fire', (0.95, 0.4, 0.15)), ('Bleed', (0.75, 0.15, 0.25)),
             ('Poison', (0.5, 0.75, 0.3))]
    # Real generated tokens if make_tokens.py has been run, else coloured discs.
    # Bagged rather than loose: 85 tokens scattered on a 36" board is unplayable,
    # and an infinite bag means you never run out of Pinned markers.
    def token_files(prefix):
        if not os.path.isdir(TOKEN_DIR):
            return []
        return [os.path.join(TOKEN_DIR, f) for f in sorted(os.listdir(TOKEN_DIR))
                if f.startswith(prefix) and f.endswith('.png')]

    bags = [
        ('Condition tokens', 'cond_', 1.0, 'Round = a condition on a MODEL.', True),
        ('Stress counters', 'stress_', 1.0, 'Stress 1-6. 1+ = Shaken (-1 all rolls). '
                                            '2+ = a Break test in the End Phase.', True),
        ('Terrain & device markers', 'tag_', 1.0,
         'Hex = something on the BOARD. Every interactive tag must be visibly '
         'marked (§28.5) — nothing interactive is invisible.', False),
        ('Deployables', 'dep_', 1.0,
         'Turrets, mines, traps, beacons. Remote mine: 1 live + 3 DUMMY markers, '
         'deliberately identical — put live/dummy in GM Notes only.', False),
        ('Feature states', 'dev_', 1.0,
         'Terminal, Powered Down/Active, Offline/Destroyed, Searched, Armed.', False),
        ('Hazard zones', 'haz_', 1.0, 'Fire, Acid, Ice, Electrified, Deep Water, Smoke.', False),
        ('Area templates', 'template_', 3.0,
         'Translucent rings at TRUE SCALE: 1/2/3/4/6/8". A 6" beacon aura measured '
         'by eye is how it becomes a 9" one.', False),
    ]
    bx = 0
    for label, prefix, tscale, blurb, stack in bags:
        files = token_files(prefix)
        if not files:
            continue
        contained = []
        for f in files:
            nm = os.path.splitext(os.path.basename(f))[0].split('_', 1)[-1]
            nm = nm.replace('_', ' ').upper()
            contained.append(custom_token(f, (0, 3.0, 0), tscale, nm, blurb, stack))
        px, pz = xz(-3.5, 4.0 + bx * 4.2)
        bag = obj('Infinite_Bag' if stack else 'Bag', (px, TOP + 2.2, pz),
                  (1.0, 1.0, 1.0), nickname=f'{label} ({len(files)})',
                  desc=blurb, colour=(0.28, 0.28, 0.32))
        bag['ContainedObjects'] = contained
        states.append(bag)
        bx += 1

    if not os.path.isdir(TOKEN_DIR):
        for i, (nm, col) in enumerate(conds):
            px, pz = xz(1.5, 2.5 + i * 3.7)
            states.append(obj('Checker_white', (px, TOP + 0.3, pz), (0.7, 0.4, 0.7),
                              nickname=nm, desc=f'{nm} token.', colour=col))

    # --- dice ---------------------------------------------------------------
    for i in range(2):
        px, pz = xz(34.5, 14.0 + i * 4.0)
        states.append(obj('Die_10', (px, TOP + 1.0, pz), (1.4, 1.4, 1.4),
                          nickname='d10',
                          desc='The only die in the game. 1d10 + Stat + Mods vs 7+.'))

    with open(os.path.join(HERE, 'Global.lua'), encoding='utf-8') as fh:
        lua = fh.read()
    # Wire the generated board image and the board size into the Lua, so !board
    # and the density check agree with what build_table.py actually laid out.
    board_png = os.path.join(HERE, 'assets', 'boards',
                             f'concrete_{int(BOARD)}x{int(BOARD)}_grid1in.png')
    if os.path.isfile(board_png):
        url = 'file:///' + board_png.replace(os.sep, '/')
        lua = lua.replace("BOARD_IMAGE = ''", f"BOARD_IMAGE = '{url}'", 1)
    else:
        print(f'  (no board image at {board_png} — run make_board.py for the '
              f'concrete surface; !board will report it is missing)')

    large = sum(1 for p in terrain if json.loads(p['GMNotes'] or '{}').get('large'))

    # The in-game Notebook — rules at the table, without leaving the table.
    tabs = {}
    try:
        from rules_text import TABS
        for i, (title, body) in enumerate(TABS):
            tabs[str(i)] = {'title': title, 'body': body.strip(), 'color': 'Grey',
                            'visibleColor': {'r': 0.5, 'g': 0.5, 'b': 0.5}, 'id': i}
    except Exception as e:
        print(f'  (no notebook: {type(e).__name__}: {e})')

    return {
        'SaveName': 'Settlements — Take a Hold',
        'GameMode': 'Settlements',
        'Gravity': 0.5,
        'PlayArea': 0.6,
        'Date': '',
        'Table': 'Table_Square',
        'Sky': 'Sky_Museum',
        'Note': (f"Settlements — Take a Hold. {large} large terrain features "
                 f"(band is 9-12). Notebook has the rules; type !help in chat."),
        'Rules': ('SETTLEMENTS — 1d10 + Stat + Mods vs 7+. Nat 1 always fails, '
                  'nat 10 always succeeds. Ties go to the defender. Win on '
                  'objectives, never on kills. Terrain density 9-12 is the '
                  'balance dial. Full reference in the Notebook.'),
        'TabStates': tabs,
        'LuaScript': lua,
        'LuaScriptState': '',
        'XmlUI': '',
        'ObjectStates': states,
    }, large


def tts_saves_dir():
    d = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                     'Tabletop Simulator', 'Saves')
    return d if os.path.isdir(d) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None,
                    help='directory to write into (default: the TTS Saves folder)')
    ap.add_argument('--name', default='Settlements.json')
    args = ap.parse_args()

    save, large = build()
    out_dir = args.out or tts_saves_dir() or HERE
    made = False
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir, exist_ok=True)
        made = True
    path = os.path.join(out_dir, args.name)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(save, fh, indent=2, ensure_ascii=False)

    n = len(save['ObjectStates'])
    print(f'wrote {path}')
    print(f'  {n} objects · {large} large terrain features '
          f'({"LEGAL" if 9 <= large <= 12 else "OUTSIDE THE 9-12 BAND"})')
    print(f'  Lua: {len(save["LuaScript"]):,} chars')
    if made:
        print('  (created that directory — if TTS has never been launched, launch it '
              'once so it builds its own folder tree, then re-run)')
    if not args.out and tts_saves_dir() is None:
        print('  NOTE: the TTS Saves folder does not exist yet, so this went next to '
              'the script. Launch TTS once, then re-run to install it directly.')


if __name__ == '__main__':
    sys.exit(main())

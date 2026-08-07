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
    for i, (nm, rank, st, gear) in enumerate(roster):
        x = 8 + i * 6
        px, pz = xz(x, y_row)
        data = {'unit': True, 'name': f'{side} {nm}', 'rank': rank, 'wnd': 1,
                'stress': 0, 'cond': {}, 'side': side, **st}
        desc = (f'{rank}  W1\nSTR {st["str"]} AGI {st["agi"]} DEX {st["dex"]}'
                f' INT {st["int"]} NRV {st["nrv"]}\n{gear}')
        out.append(obj('Checker_white' if side == 'White' else 'Checker_red',
                       (px, TOP + 0.4, pz), (1.1, 1.1, 1.1),
                       nickname=f'{side} {nm}', desc=desc, colour=colour,
                       gm=data, rot=(0, facing, 0)))
    return out


def build():
    states = []

    # --- the board slab -----------------------------------------------------
    states.append(obj('BlockSquare', (0, BASE_Y, 0),
                      (BOARD * INCH, BOARD_T, BOARD * INCH),
                      nickname="Board — 3'x3'",
                      desc="36\"x36\". Deployment 6\" bands, ~24\" apart.",
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
    terrain = take_a_hold_terrain()
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
    states.extend(crew('White', (0.90, 0.90, 0.92), 3.0, 0))
    states.extend(crew('Red', (0.75, 0.25, 0.25), 33.0, 180))

    # --- condition token supply (copy/paste in TTS to make more) -----------
    conds = [('Stress', (0.9, 0.75, 0.2)), ('Pinned', (0.9, 0.5, 0.2)),
             ('Down', (0.6, 0.2, 0.2)), ('Prone', (0.5, 0.45, 0.6)),
             ('Hidden', (0.35, 0.45, 0.6)), ('Ready', (0.35, 0.7, 0.5)),
             ('Fire', (0.95, 0.4, 0.15)), ('Bleed', (0.75, 0.15, 0.25)),
             ('Poison', (0.5, 0.75, 0.3))]
    # Kept ON the board. At x=-22 they were off a board that only spans +/-18, so
    # they slid off the table edge and piled up in mid-air (seen at y~7).
    for i, (nm, col) in enumerate(conds):
        px, pz = xz(1.5, 2.5 + i * 3.7)
        states.append(obj('Checker_white', (px, TOP + 0.3, pz), (0.7, 0.4, 0.7),
                          nickname=nm,
                          desc=f'{nm} token. Copy/paste (Ctrl+C, Ctrl+V) for more.',
                          colour=col))

    # --- dice ---------------------------------------------------------------
    for i in range(2):
        px, pz = xz(34.5, 14.0 + i * 4.0)
        states.append(obj('Die_10', (px, TOP + 1.0, pz), (1.4, 1.4, 1.4),
                          nickname='d10',
                          desc='The only die in the game. 1d10 + Stat + Mods vs 7+.'))

    with open(os.path.join(HERE, 'Global.lua'), encoding='utf-8') as fh:
        lua = fh.read()

    large = sum(1 for p in terrain if json.loads(p['GMNotes']).get('large'))
    return {
        'SaveName': 'Settlements — Take a Hold',
        'GameMode': 'Settlements',
        'Gravity': 0.5,
        'PlayArea': 0.6,
        'Date': '',
        'Table': 'Table_Square',
        'Sky': 'Sky_Museum',
        'Note': (f"Settlements — Take a Hold. {large} large terrain features "
                 f"(band is 9-12). Type !help in chat."),
        'Rules': '',
        'TabStates': {},
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

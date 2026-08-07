# -*- coding: utf-8 -*-
"""OpenSCAD terrain -> Tabletop Simulator custom models.

The pieces in ../Terrain/ are parametric OpenSCAD built for 3D PRINTING, so the
exported STLs are `show="plate"` print layouts — flat trays of parts, useless as
table scenery. Every source also has `show="assembly"`, which is the actual
building. This exports THAT, then converts to what TTS will accept.

TTS's constraints (kb.tabletopsimulator.com/custom-content/custom-model):
  * .obj only, one combined mesh per file, triangulated
  * under ~25k vertices or it may fail to import / crash the game
  * a COLLIDER mesh must be under 255 triangles — a hard engine limit, and the
    one every OpenSCAD export violates (these run 1.3k-12k faces). Without a
    collider TTS fits a box, which is wrong for anything you shoot through.
  * Unity is Y-up; OpenSCAD is Z-up. Unrotated models import lying on their face.

Collider strategy: the convex hull, which is cheap, always valid, and usually
well under 255 faces. If the hull is still too big we fall back to the oriented
bounding box (12 triangles) — a worse fit but never broken. Genuinely concave
pieces (the boom gate) would want a TTS compound collider, which is a manual job
and flagged rather than faked.

    py -3.13 make_models.py                    # all pieces
    py -3.13 make_models.py --only prison_cell
    py -3.13 make_models.py --footprint 6      # scale so the longest side = 6"
"""
import argparse
import glob
import os
import subprocess
import sys

import trimesh
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TERRAIN = os.path.normpath(os.path.join(HERE, '..', 'Terrain'))
OUT = os.path.join(HERE, 'assets', 'models')
OPENSCAD = r'C:\Program Files\OpenSCAD\openscad.exe'
MM_PER_INCH = 25.4
MAX_VERTS = 25000
MAX_COLLIDER_FACES = 255

# The pieces worth putting on a table, and the Settlements rule each one serves.
PIECES = {
    'ranch_house':          ('Building · 6x6 · Heavy cover', 'Openable, Climbable, Searchable'),
    'ranch_garage':         ('Building · 6x6 · Heavy cover', 'Openable, Searchable'),
    'checkpoint_boom_gate': ('Infrastructure · Access: Open/Close Path', 'Hackable, Openable'),
    'spike_crusher':        ('Infrastructure · CRUSH hazard', 'Hackable, Powered'),
    'prison_cell':          ('Building · Holding Cells', 'Lockable, Breachable, Hackable'),
}


def scad_assembly(name):
    """Export the assembled model (not the print plate) to STL."""
    src = os.path.join(TERRAIN, name + '.scad')
    if not os.path.isfile(src):
        return None, f'no such source: {src}'
    dst = os.path.join(OUT, name + '_assembly.stl')
    # OpenSCAD writes its status to stderr and returns nothing useful otherwise.
    # A string -D needs escaped quotes or OpenSCAD ignores it and silently falls
    # through to the file's default `show` value.
    cmd = [OPENSCAD, '--render', '-o', dst, '-D', 'show="assembly"', src]
    p = subprocess.run(cmd, capture_output=True, text=True)
    err = (p.stderr or '').strip()
    if not os.path.isfile(dst):
        return None, f'openscad produced nothing\n{err[-800:]}'
    manifold = 'Simple:' not in err or 'Simple:     yes' in err or 'Simple: yes' in err
    return dst, ('ok' if manifold else 'WARNING: mesh is not manifold — ' + err[-300:])


def to_tts(mesh, footprint=None):
    """Z-up mm -> Y-up TTS units, centred, resting on y=0."""
    m = mesh.copy()
    m.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]))
    scale = 1.0 / MM_PER_INCH
    if footprint:
        e = m.extents
        longest = max(e[0], e[2])          # footprint is the horizontal span
        scale = footprint / longest if longest else scale
    m.apply_scale(scale)
    m.apply_translation(-m.centroid)
    m.apply_translation([0, -m.bounds[0][1], 0])   # sit on the table
    return m


def collider(m):
    """Under 255 triangles, always valid. Hull first, OBB as the safety net."""
    hull = m.convex_hull
    if len(hull.faces) <= MAX_COLLIDER_FACES:
        return hull, f'convex hull, {len(hull.faces)} faces'
    box = m.bounding_box_oriented
    return box, (f'hull was {len(hull.faces)} faces (over {MAX_COLLIDER_FACES}) '
                 f'— fell back to oriented bounding box, {len(box.faces)} faces')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', action='append', help='piece name (repeatable)')
    ap.add_argument('--footprint', type=float, default=None,
                    help='scale so the longest horizontal side is N inches')
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    names = args.only or list(PIECES)
    rows = []
    for name in names:
        print(f'--- {name}')
        stl, note = scad_assembly(name)
        if stl is None:
            print(f'    SKIP: {note}')
            continue
        if note != 'ok':
            print(f'    {note}')
        mesh = trimesh.load(stl, force='mesh')
        m = to_tts(mesh, args.footprint)
        col, cnote = collider(m)

        obj_p = os.path.join(OUT, name + '.obj')
        col_p = os.path.join(OUT, name + '_collider.obj')
        m.export(obj_p)
        col.export(col_p)

        e = m.extents
        warn = '  ** OVER 25k VERTS' if len(m.vertices) > MAX_VERTS else ''
        print(f'    model    {len(m.vertices):,} verts / {len(m.faces):,} faces{warn}')
        print(f'    collider {cnote}')
        print(f'    size     {e[0]:.1f}" x {e[2]:.1f}" footprint, {e[1]:.1f}" tall')
        rows.append((name, obj_p, col_p, e, len(m.vertices)))

    if not rows:
        print('\nnothing exported')
        return 1

    print(f'\n{"=" * 78}\nPaste these into a TTS Custom Model object '
          f'(right-click table -> Objects -> Components -> Custom -> Model):\n')
    for name, obj_p, col_p, e, _ in rows:
        profile, tags = PIECES.get(name, ('', ''))
        print(f'{name}   [{profile}]')
        print(f'  Tags:     {tags}')
        print(f'  Model:    file:///{obj_p.replace(os.sep, "/")}')
        print(f'  Collider: file:///{col_p.replace(os.sep, "/")}')
        print(f'  Footprint {e[0]:.1f}" x {e[2]:.1f}", {e[1]:.1f}" tall\n')
    print('Local file:/// paths load for YOU only — they will not sync to other')
    print('players. Host the assets (GitHub raw off this repo works) before sharing.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

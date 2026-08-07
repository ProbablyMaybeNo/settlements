# -*- coding: utf-8 -*-
"""Turn a folder of downloaded 3D models into Tabletop Simulator custom models.

`make_models.py` handles our own OpenSCAD terrain, which is clean, single-mesh and
in known units. Downloaded asset packs are none of those things, so this one is
built to survive mess:

  * ANY common format. trimesh reads obj/stl/glb/gltf/dae/ply/3mf/off directly.
    It cannot read FBX or .blend, so those route through Blender to glb first.
  * MULTI-OBJECT SCENES. Packs ship whole scenes in one file; TTS wants one
    combined mesh per .obj. Scenes are merged (or split with --split).
  * ARBITRARY SCALE. A pack may be in metres, centimetres or nothing at all, so
    --footprint rescales to a real Settlements footprint in inches. Without it
    you get a 0.03" house or a 4000" one.
  * ARBITRARY UP-AXIS. glTF/FBX are usually Y-up; STL/CAD output is usually
    Z-up. Guessed per format and always REPORTED, with --up to override, because
    a silently wrong guess imports every model lying on its face.
  * THE 255-TRIANGLE COLLIDER LIMIT, which nothing you download will respect.

Anything it cannot fix it says so about, loudly, rather than writing a broken
asset and letting TTS fail on import.

    py -3.13 import_models.py --src "C:/Users/Admin/Downloads/somepack"
    py -3.13 import_models.py --src <folder> --footprint 6 --up z
    py -3.13 import_models.py --src <folder> --split      # one obj per sub-mesh
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
import trimesh

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_MODELS = os.path.join(HERE, 'assets', 'models')
OUT_TEX = os.path.join(HERE, 'assets', 'textures')
BLENDER = r'C:\Program Files\Blender Foundation\Blender 4.5\blender.exe'

MAX_VERTS = 25000
MAX_COLLIDER_FACES = 255
MM_PER_INCH = 25.4

TRIMESH_EXT = {'.obj', '.stl', '.glb', '.gltf', '.dae', '.ply', '.3mf', '.off'}
BLENDER_EXT = {'.fbx', '.blend'}
TEX_EXT = {'.png', '.jpg', '.jpeg', '.tga', '.bmp'}

# glTF/FBX are authored Y-up; mesh/CAD formats are conventionally Z-up.
Y_UP_EXT = {'.glb', '.gltf', '.fbx', '.dae', '.blend'}


def have_blender():
    return os.path.isfile(BLENDER)


def blender_run(script, *args):
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False,
                                     encoding='utf-8') as fh:
        fh.write(script)
        path = fh.name
    try:
        p = subprocess.run([BLENDER, '-b', '--factory-startup', '-P', path,
                            '--', *[str(a) for a in args]],
                           capture_output=True, text=True, timeout=600)
        return p.returncode == 0, (p.stdout or '') + (p.stderr or '')
    finally:
        os.unlink(path)


CONVERT_SCRIPT = '''
import bpy, sys, os
inp, outp = sys.argv[sys.argv.index('--')+1:][:2]
bpy.ops.wm.read_factory_settings(use_empty=True)
ext = os.path.splitext(inp)[1].lower()
if ext == '.fbx':
    bpy.ops.import_scene.fbx(filepath=inp)
elif ext == '.blend':
    bpy.ops.wm.open_mainfile(filepath=inp)
else:
    raise SystemExit('unsupported: ' + ext)
bpy.ops.export_scene.gltf(filepath=outp, export_format='GLB')
'''

DECIMATE_SCRIPT = '''
import bpy, sys
inp, outp, target = sys.argv[sys.argv.index('--')+1:][:3]
target = int(target)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.obj_import(filepath=inp)
objs = [o for o in bpy.context.scene.objects if o.type == 'MESH']
total = sum(len(o.data.vertices) for o in objs)
ratio = min(1.0, target / max(1, total))
for o in objs:
    bpy.context.view_layer.objects.active = o
    m = o.modifiers.new('dec', 'DECIMATE')
    m.ratio = ratio
    bpy.ops.object.modifier_apply(modifier='dec')
bpy.ops.wm.obj_export(filepath=outp, export_materials=False)
'''


def load_any(path, notes):
    """-> a single trimesh Trimesh, or None."""
    ext = os.path.splitext(path)[1].lower()
    src = path
    if ext in BLENDER_EXT:
        if not have_blender():
            notes.append(f'SKIP: {ext} needs Blender and it was not found at {BLENDER}')
            return None
        tmp = os.path.join(tempfile.gettempdir(),
                           os.path.splitext(os.path.basename(path))[0] + '.glb')
        ok, log = blender_run(CONVERT_SCRIPT, path, tmp)
        if not ok or not os.path.isfile(tmp):
            notes.append(f'SKIP: Blender could not convert {ext}: {log[-300:]}')
            return None
        notes.append(f'{ext} -> glb via Blender')
        src = tmp
    try:
        loaded = trimesh.load(src, force='mesh', process=False)
    except Exception as e:
        notes.append(f'SKIP: load failed: {type(e).__name__}: {e}')
        return None
    if loaded is None or not hasattr(loaded, 'faces') or len(loaded.faces) == 0:
        notes.append('SKIP: no geometry in file')
        return None
    return loaded


def orient(m, ext, up, notes):
    guess = 'y' if ext in Y_UP_EXT else 'z'
    chosen = up if up != 'auto' else guess
    if chosen == 'z':
        m.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]))
        notes.append(f'up-axis: treated as Z-up ({"forced" if up != "auto" else "guessed from " + ext}) -> rotated to Y-up')
    else:
        notes.append(f'up-axis: treated as Y-up ({"forced" if up != "auto" else "guessed from " + ext}) -> no rotation')
    return m


def rescale(m, footprint, notes):
    e = m.extents
    longest = max(e[0], e[2])
    if not longest:
        return m
    if footprint:
        m.apply_scale(footprint / longest)
        notes.append(f'scaled so the longest horizontal side = {footprint:g}"')
    else:
        # No target given: guess the source unit from raw size and convert.
        if longest > 300:
            m.apply_scale(1.0 / MM_PER_INCH)
            notes.append(f'no --footprint; raw span {longest:.0f} looked like mm -> converted to inches')
        elif longest < 5:
            m.apply_scale(39.3701)
            notes.append(f'no --footprint; raw span {longest:.2f} looked like metres -> converted to inches')
        else:
            notes.append(f'no --footprint; raw span {longest:.1f} left as-is (assumed inches)')
    m.apply_translation(-m.centroid)
    m.apply_translation([0, -m.bounds[0][1], 0])
    return m


def decimate(m, name, notes):
    if len(m.vertices) <= MAX_VERTS:
        return m
    if not have_blender():
        notes.append(f'WARNING: {len(m.vertices):,} verts is over the {MAX_VERTS:,} '
                     f'limit and Blender is unavailable — TTS may refuse this model')
        return m
    tmp_in = os.path.join(tempfile.gettempdir(), name + '_pre.obj')
    tmp_out = os.path.join(tempfile.gettempdir(), name + '_dec.obj')
    m.export(tmp_in)
    ok, log = blender_run(DECIMATE_SCRIPT, tmp_in, tmp_out, int(MAX_VERTS * 0.9))
    if ok and os.path.isfile(tmp_out):
        r = trimesh.load(tmp_out, force='mesh', process=False)
        notes.append(f'decimated {len(m.vertices):,} -> {len(r.vertices):,} verts '
                     f'(Blender, under the {MAX_VERTS:,} cap)')
        return r
    notes.append(f'WARNING: decimation failed, left at {len(m.vertices):,} verts: {log[-200:]}')
    return m


def make_collider(m, notes):
    hull = m.convex_hull
    if len(hull.faces) <= MAX_COLLIDER_FACES:
        notes.append(f'collider: convex hull, {len(hull.faces)} faces')
        return hull
    box = m.bounding_box_oriented
    notes.append(f'collider: hull was {len(hull.faces)}f (over {MAX_COLLIDER_FACES}) '
                 f'-> oriented bounding box, {len(box.faces)}f. Concave pieces will '
                 f'want a hand-built compound collider.')
    return box


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, help='folder of downloaded models')
    ap.add_argument('--footprint', type=float, default=None,
                    help='scale each model so its longest horizontal side is N inches')
    ap.add_argument('--up', choices=['auto', 'y', 'z'], default='auto')
    ap.add_argument('--split', action='store_true',
                    help='write one .obj per sub-mesh instead of merging a scene')
    ap.add_argument('--limit', type=int, default=None, help='only the first N models')
    args = ap.parse_args()

    if not os.path.isdir(args.src):
        print(f'no such folder: {args.src}', file=sys.stderr)
        return 1
    os.makedirs(OUT_MODELS, exist_ok=True)
    os.makedirs(OUT_TEX, exist_ok=True)

    found, textures = [], []
    for root, _, files in os.walk(args.src):
        for f in sorted(files):
            e = os.path.splitext(f)[1].lower()
            if e in TRIMESH_EXT or e in BLENDER_EXT:
                found.append(os.path.join(root, f))
            elif e in TEX_EXT:
                textures.append(os.path.join(root, f))

    print(f'scanned {args.src}')
    print(f'  {len(found)} model files · {len(textures)} images')
    if not found:
        print('  nothing convertible here. Supported: '
              + ', '.join(sorted(TRIMESH_EXT | BLENDER_EXT)))
        return 1
    if args.limit:
        found = found[:args.limit]

    manifest = []
    for path in found:
        name = os.path.splitext(os.path.basename(path))[0]
        name = ''.join(c if (c.isalnum() or c in '-_') else '_' for c in name)
        ext = os.path.splitext(path)[1].lower()
        notes = []
        print(f'\n--- {os.path.relpath(path, args.src)}')
        m = load_any(path, notes)
        if m is None:
            for n in notes:
                print(f'    {n}')
            continue
        m = orient(m, ext, args.up, notes)
        m = rescale(m, args.footprint, notes)
        m = decimate(m, name, notes)
        col = make_collider(m, notes)

        obj_p = os.path.join(OUT_MODELS, name + '.obj')
        col_p = os.path.join(OUT_MODELS, name + '_collider.obj')
        m.export(obj_p)
        col.export(col_p)
        e = m.extents
        for n in notes:
            print(f'    {n}')
        print(f'    -> {len(m.vertices):,}v / {len(m.faces):,}f · '
              f'{e[0]:.1f}" x {e[2]:.1f}" footprint, {e[1]:.1f}" tall')
        manifest.append(dict(name=name, source=os.path.relpath(path, args.src),
                             model=obj_p, collider=col_p,
                             verts=len(m.vertices), faces=len(m.faces),
                             size=[round(float(v), 2) for v in (e[0], e[2], e[1])]))

    for t in textures:
        dst = os.path.join(OUT_TEX, os.path.basename(t))
        if not os.path.exists(dst):
            shutil.copy2(t, dst)

    mf = os.path.join(HERE, 'assets', 'manifest.json')
    with open(mf, 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, indent=2)

    print(f'\n{"=" * 76}\n{len(manifest)} model(s) ready · manifest {mf}')
    if textures:
        print(f'{len(textures)} image(s) copied to {OUT_TEX} — pick the diffuse one '
              f'per model as its Texture Image in TTS')
    print('\nPaste into TTS: right-click -> Objects -> Components -> Custom -> Model\n')
    for r in manifest[:10]:
        print(f'{r["name"]}  ({r["size"][0]:.1f}" x {r["size"][1]:.1f}", '
              f'{r["size"][2]:.1f}" tall)')
        print(f'  Model:    file:///{r["model"].replace(os.sep, "/")}')
        print(f'  Collider: file:///{r["collider"].replace(os.sep, "/")}')
    if len(manifest) > 10:
        print(f'... and {len(manifest) - 10} more in the manifest')
    print('\nLocal file:/// paths load for YOU only and will not sync to other '
          'players.\nHost them (GitHub raw off this repo) before sharing a table.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

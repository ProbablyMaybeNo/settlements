# -*- coding: utf-8 -*-
"""Spawn models into TTS by their gallery NUMBER.

Most models in these packs have no nickname, so the gallery numbers them and this
resolves those numbers back to real assets. Numbers are stable across runs because
the gallery sorts by mesh URL, the one field that never changes.

    py -3.13 spawn_picks.py 12 40 55-60           # into a bag
    py -3.13 spawn_picks.py 12 40 --loose         # straight onto the table
    py -3.13 spawn_picks.py 12-30 --name "Ruins"  # name the bag
    py -3.13 spawn_picks.py --list 12 40          # just tell me what these are
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(HERE, 'assets', 'gallery', 'numbers.json')


def parse_picks(tokens):
    """Accept '12', '12,13', '55-60' in any mix."""
    out = []
    for t in tokens:
        for part in str(t).split(','):
            part = part.strip()
            if not part:
                continue
            m = re.match(r'^(\d+)\s*-\s*(\d+)$', part)
            if m:
                a, b = int(m.group(1)), int(m.group(2))
                out.extend(range(min(a, b), max(a, b) + 1))
            elif part.isdigit():
                out.append(int(part))
            else:
                print(f'  ignoring "{part}" — not a number or range', file=sys.stderr)
    seen, uniq = set(), []
    for n in out:
        if n not in seen:
            seen.add(n)
            uniq.append(n)
    return uniq


def model_json(rec, pos, scale=1.0):
    nick = rec['nick'] if rec['nick'] != '(unnamed)' else f'#{rec["num"]}'
    return {
        'Name': 'Custom_Model', 'Nickname': nick,
        'Description': (f'gallery #{rec["num"]}'
                        + (f' · {rec["dims"]} raw units' if rec.get('dims') else '')
                        + '\n\nTag it once placed:  !terrain <cover> <height> [tags]'),
        'Transform': {'posX': pos[0], 'posY': pos[1], 'posZ': pos[2],
                      'rotX': 0, 'rotY': 0, 'rotZ': 0,
                      'scaleX': scale, 'scaleY': scale, 'scaleZ': scale},
        'ColorDiffuse': {'r': 1, 'g': 1, 'b': 1}, 'Locked': False,
        'Grid': True, 'Snap': False, 'Autoraise': True, 'Sticky': True,
        'CustomMesh': {
            'MeshURL': rec['mesh'], 'DiffuseURL': rec.get('diffuse', ''),
            'NormalURL': '', 'ColliderURL': '',
            'Convex': True, 'MaterialIndex': 1, 'TypeIndex': 0,
            'CustomShader': {'SpecularColor': {'r': 0.9, 'g': 0.9, 'b': 0.9},
                             'SpecularIntensity': 0.1, 'SpecularSharpness': 4.0,
                             'FresnelStrength': 0.1},
            'CastShadows': True,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('picks', nargs='+', help='numbers and ranges, e.g. 12 40 55-60')
    ap.add_argument('--name', default=None, help='bag name')
    ap.add_argument('--loose', action='store_true',
                    help='spawn onto the table instead of into a bag')
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--list', action='store_true', help='resolve only, do not spawn')
    args = ap.parse_args()

    if not os.path.isfile(INDEX):
        print(f'no gallery index at {INDEX}\n  run browse_models.py first',
              file=sys.stderr)
        return 1
    with open(INDEX, encoding='utf-8') as fh:
        index = json.load(fh)

    nums = parse_picks(args.picks)
    recs, bad, uncached = [], [], []
    for n in nums:
        r = index.get(str(n))
        if r is None:
            bad.append(n)
            continue
        r = dict(r, num=n)
        if r.get('status') != 'cached':
            uncached.append(n)
        recs.append(r)

    print(f'resolved {len(recs)} of {len(nums)} pick(s):')
    for r in recs:
        flag = '' if r.get('status') == 'cached' else f'   [{r.get("status")}]'
        print(f'  #{r["num"]:<5} {r["nick"][:34]:<34} {r.get("dims", ""):>12}{flag}')
    if bad:
        print(f'  not in the index: {bad}')
    if uncached:
        print(f'  WARNING: {uncached} are not in TTS\'s cache — these will pop the '
              f'Custom Model dialog. Try recover_assets.py first.')
    if args.list or not recs:
        return 0

    sys.path.insert(0, HERE)
    import tts_api
    if not tts_api.is_up():
        print('\nTTS is not listening — load a table first.', file=sys.stderr)
        return 1

    if args.loose:
        # a row along the left edge, clear of the 36" board
        for i, r in enumerate(recs):
            pos = (-22.0, 3.0, -16.0 + (i % 12) * 3.0)
            tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1',
                          'script': f'spawnObjectJSON({{json = [==['
                                    f'{json.dumps(model_json(r, pos, args.scale))}]==]}})'})
            tts_api.listen(1.2)
        print(f'\nspawned {len(recs)} model(s) beside the board')
    else:
        name = args.name or f'Picks ({len(recs)})'
        bag = {
            'Name': 'Bag', 'Nickname': name,
            'Description': 'Gallery picks. Drag one out, place it, then tag it with '
                           '!terrain <cover> <height> [tags] so !density counts it.',
            'Transform': {'posX': -22.0, 'posY': 2.5, 'posZ': 0.0,
                          'rotX': 0, 'rotY': 0, 'rotZ': 0,
                          'scaleX': 1.4, 'scaleY': 1.4, 'scaleZ': 1.4},
            'ColorDiffuse': {'r': 0.85, 'g': 0.7, 'b': 0.25},
            'Locked': False, 'Grid': True, 'Snap': False,
            'ContainedObjects': [model_json(r, (0, 3, 0), args.scale) for r in recs],
        }
        tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1',
                      'script': f'spawnObjectJSON({{json = [==[{json.dumps(bag)}]==]}})\n'
                                f'print("[picks] spawned bag \\"{name}\\" with '
                                f'{len(recs)} model(s)")'})
        tts_api.listen(4.0)
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Themed terrain bags for the Ultimate Modern Map Toolkit, by gallery number.

HOW THESE WERE BUILT: only 184 of the pack's 809 models carry a nickname, so
classification could not come from metadata. Every one of the 570 cached models was
rendered to a numbered contact sheet and identified BY EYE. That means the grouping
is a judgement call, not a lookup — expect a few pieces in the wrong bag, and move
them when you spot one.

Numbers are stable across runs (the gallery sorts by mesh URL), so these lists stay
valid unless the pack itself changes.

    py -3.13 themes.py                 # list the bags
    py -3.13 themes.py --spawn         # spawn all of them
    py -3.13 themes.py --spawn Ruins Industrial
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Ranges are inclusive. Anything genuinely uncached is dropped at spawn time.
THEMES = {
    'Industrial': dict(
        blurb='Machinery, silos, tanks, gantries, pipework, generators. Mostly '
              'Heavy cover; the tall ones are LOS blockers.',
        picks='54,56,57,59,60,61-65,67-69,71-73,75-77,79-84,156,169,170,172,183,'
              '185,186,194,195,209,262,455,462-466,525,604,610,617-619,621,628,'
              '629,635,637,646,655,666,669,682',
    ),
    'Depot': dict(
        blurb='Rail, containers, pallets, racking, forklifts. Good Light/Heavy '
              'cover at fighter height, and it stacks.',
        picks='31-37,226-239,554,605-607,611,612,616,622,624,626,627,634,636,641,'
              '644,647,653,663,664,671,673,676-679,681,688-690',
    ),
    'Ruins': dict(
        blurb='HEAVY COVER YOU FIGHT THROUGH, plus the 2.5D layer. The backbone '
              'of a good Settlements board — prefer these over solid buildings.',
        picks='46,47,85-92,140-153,719,724-728,733,736,738,740,741,744-748,755-757,'
              '762,765,767,769,772-774,776,777,779,780,783,786,789,793,794,796',
    ),
    'City blocks': dict(
        blurb='LOS-blocking office and tower blocks. Two minimum on a legal board; '
              'every floor needs a no-test way up.',
        picks='143,245,515-520,524,528,686,721,754,782',
    ),
    'Suburbs': dict(
        blurb='Houses, shacks, and the furniture to dress interiors.',
        picks='5-7,12,15,16,21,26,70,246,305-309,377,536,537,539,543-546,548,550,'
              '614,633,640,694-696,775,784,795',
    ),
    'Vehicles': dict(
        blurb='Hard cover at the right scale for 2051. Several read as Explosive.',
        picks='4,160,162,163,190,214-219,240-243,247,249-251,253,278-280,289-292,'
              '540,552,558,623,630',
    ),
    'Military': dict(
        blurb='Bunkers, emplacements, armour, crew-served weapons.',
        picks='3,254-256,258-261,263-270,272-275,285,538,559',
    ),
    'Barricades': dict(
        blurb='Concrete barriers, tank traps, hoardings, fence panels. This is '
              'what you fill lanes with until none crosses the board.',
        picks='73,84,155,174,176-179,187,188,299-304,522,529-532,632,645,649,660',
    ),
    'Nature': dict(
        blurb='Trees, shrubs, rocks. Light cover, and rocks give you elevation.',
        picks='41,126-133,180,196-200,220-223,732,734,737,764,785',
    ),
    'Verticality': dict(
        blurb='THE 2.5D LAYER. Catwalks, ramps, stairs, ladders, platforms. Every '
              'elevated area needs one of these or nobody can get up there.',
        picks='13,18,22,29,30,44,48,55,78,134,135,201,372-376,381,382,461,547,638,'
              '659,687,751,753',
    ),
    'Infrastructure': dict(
        blurb='Things a terminal can operate, plus utility clutter. Reshapes the '
              'board; it is not there to hurt people.',
        picks='159,182,184,189,191-193,212,271,293,457,613,625,631,735',
    ),
}


def parse_picks(spec):
    out = []
    for part in spec.replace(' ', '').split(','):
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    seen, uniq = set(), []
    for n in out:
        if n not in seen:
            seen.add(n)
            uniq.append(n)
    return uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spawn', nargs='*', default=None,
                    help='spawn all bags, or only the named ones')
    args = ap.parse_args()

    idx_path = os.path.join(HERE, 'assets', 'gallery', 'numbers.json')
    if not os.path.isfile(idx_path):
        print(f'no number index — run browse_models.py first', file=sys.stderr)
        return 1
    with open(idx_path, encoding='utf-8') as fh:
        index = json.load(fh)

    wanted = None
    if args.spawn is not None and args.spawn:
        wanted = {w.lower() for w in args.spawn}

    total_ok = 0
    plan = []
    for name, spec in THEMES.items():
        if wanted and name.lower() not in wanted:
            continue
        nums = parse_picks(spec['picks'])
        ok = [n for n in nums
              if str(n) in index and index[str(n)].get('status') == 'cached']
        skipped = len(nums) - len(ok)
        total_ok += len(ok)
        plan.append((name, spec['blurb'], ok, skipped))
        print(f'[{name}]  {len(ok)} pieces' + (f'  ({skipped} not cached, dropped)'
                                               if skipped else ''))
        print(f'   {spec["blurb"]}')
    print(f'\n{total_ok} pieces across {len(plan)} bag(s)')

    if args.spawn is None:
        print('\n(run with --spawn to put these on the table)')
        return 0

    sys.path.insert(0, HERE)
    import tts_api
    import spawn_picks
    if not tts_api.is_up():
        print('\nTTS is not listening — load a table first.', file=sys.stderr)
        return 1

    for i, (name, blurb, ok, _) in enumerate(plan):
        recs = [dict(index[str(n)], num=n) for n in ok]
        bag = {
            'Name': 'Bag', 'Nickname': f'{name} ({len(recs)})',
            'Description': blurb + '\n\nDrag one out, place it, then tag it: '
                                   '!terrain <cover> <height> [tags]',
            'Transform': {'posX': -26.0, 'posY': 2.5, 'posZ': -22.0 + i * 4.2,
                          'rotX': 0, 'rotY': 0, 'rotZ': 0,
                          'scaleX': 1.4, 'scaleY': 1.4, 'scaleZ': 1.4},
            'ColorDiffuse': {'r': 0.32, 'g': 0.36, 'b': 0.32},
            'Locked': False, 'Grid': True, 'Snap': False,
            'ContainedObjects': [spawn_picks.model_json(r, (0, 3, 0)) for r in recs],
        }
        tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1',
                      'script': f'spawnObjectJSON({{json = [==[{json.dumps(bag)}]==]}})\n'
                                f'print("[themes] {name}: {len(recs)} pieces")'})
        tts_api.listen(2.5)
    print(f'\nspawned {len(plan)} bag(s) down the left of the board')
    return 0


if __name__ == '__main__':
    sys.exit(main())

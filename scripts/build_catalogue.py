# -*- coding: utf-8 -*-
"""Generate "_Rules Catalogue" — every table and mechanic in one readable note.

WHY THIS IS GENERATED, AND HOW EDITING WORKS. The note is built from Obsidian
**block embeds** (`![[Note#^tbl-anchor]]`), not copies. So:

    edit a table in its own note  ->  the Catalogue updates automatically

That direction is the one Obsidian supports, and it is the right one anyway: each
table keeps exactly one home, and the Catalogue is a lens over them. Editing a
table *inside* the Catalogue view is not possible — an embed is read-only — so
every section here prints the source link right beside the embed, and clicking it
takes you to the editable original.

The generator's real job is coverage. It scans every note for `^tbl-` anchors and
warns about any table it could not place, so the Catalogue cannot silently go
stale when a new table is added. Tables with no anchor cannot be embedded at all,
so it lists those too and tells you to add one.

    py -3.13 scripts/build_catalogue.py            # write into the vault
    py -3.13 scripts/build_catalogue.py --check    # report coverage only
"""
import argparse
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

VAULT = os.path.join(os.path.expanduser('~'), 'Documents', 'Obsidian Vault',
                     'Settlements', 'Rules System')
OUT_NAME = '_Rules Catalogue.md'

# The spine of the document: what a reader wants in the order they want it.
# (section title, blurb, [ (note, anchor, caption), ... ])
SECTIONS = [
    ('1 · The engine — one mechanic, everywhere',
     'Everything below resolves through this. If a rule needs its own resolution '
     'method, it is wrong.',
     [('Rules Engine', None, 'The core test, turn structure and house conventions'),
      ('Initiative & Activation', 'tbl-reaction-options', 'Reactions — what a Ready token buys'),
      ('Movement', 'tbl-terrain-movement', 'Movement tests — the AGI checks'),
      ]),

    ('2 · Building a fighter — what the player actually chooses',
     'Read this block top to bottom to see the whole customisation surface: rank '
     'buys stat points, stat points unlock skill tiers, and Credits buy the body '
     'and the gun. Nothing else is priced.',
     [('Unit Design', 'tbl-stat-scale', 'The stat scale — what each +1 buys'),
      ('Unit Design', 'tbl-ranks-build-budget', 'Ranks: stat points, tier caps, Orders, Credits'),
      ('List Building', 'tbl-the-four-ranks', 'Match Play bodies — the richer starting kit'),
      ('List Building', 'tbl-the-four-ranks-campaign', 'Campaign Start bodies — lean, meant to grow'),
      ('List Building', 'tbl-budget', 'Crew Rating caps by format'),
      ('Skill Paths', 'tbl-how-it-works-skills-ride-the-stat-line', 'How skills attach to stats'),
      ('Skill Paths', 'tbl-the-five-paths', 'The five paths'),
      ('Progression', 'tbl-level-track', 'The 10-Level campaign track'),
      ]),

    ('3 · Skills — the full catalogue, by path and tier',
     'This is the block to study for tier balance. T1 is a reliable option or a '
     'narrow exception; T2 is role-defining; T3 is campaign-earned and '
     'fight-swinging. A skill is always a verb or a conditional exception — never '
     'a flat stat bump.',
     [('Skill Paths', None, 'Every skill, all five paths, T1 through T3')]),

    ('4 · Weapons — built, not bought',
     'Pick a class, spend Credits on characteristics, name the result. The class '
     'sets damage, range and rank gate; characteristics do the rest.',
     [('Weapons', 'tbl-1-weapon-classes', 'Classes — the chassis'),
      ('Weapons', 'tbl-rank-gates-the-class', 'Rank gates which classes you may hold'),
      ('Weapons', 'tbl-damage-armour', 'Damage & armour characteristics'),
      ('Weapons', 'tbl-to-hit', 'To-hit characteristics'),
      ('Weapons', 'tbl-payload-replaces-the-non-wounding-result', 'Payloads — replace the non-wound result'),
      ('Weapons', 'tbl-area', 'Area'),
      ('Weapons', 'tbl-handling', 'Handling'),
      ('Weapons', 'tbl-drawbacks-refund-points-take-no-slot-max-2-p', 'Drawbacks — refund Credits'),
      ('Weapons', 'tbl-3-armor', 'Armour'),
      ('Weapons', 'tbl-4-hacking-gear', 'Hacking gear'),
      ('Weapons', 'tbl-5-sample-armoury', 'Sample armoury — worked builds'),
      ('Weapons', 'tbl-6-cut-and-why', 'Cut, and why — so it does not creep back'),
      ]),

    ('5 · Damage, conditions and morale — what a hit actually does',
     'Every hit does something. A hit either wounds or delivers its payload, never '
     'both, and a failed wound becomes Stress — which is the entire fear system.',
     [('Damage', None, 'The Injury roll, Down/Out, and WND'),
      ('Conditions', None, 'Every condition, and the no-stacking rule'),
      ('Morale', 'tbl-break-test-end-phase-2-stress', 'Break test and the nerve states'),
      ]),

    ('6 · Deployables — the gear you plant on the board',
     'Bought like a weapon, carried by a fighter, set up with an INT test. This is '
     'where INT earns its combat role.',
     [('Deployables', 'tbl-build-rating-some-things-are-harder-to-build', 'Build rating'),
      ('Deployables', 'tbl-family-a-turrets', 'Turrets'),
      ('Deployables', 'tbl-chassis-how-it-delivers', 'Mines — chassis'),
      ('Deployables', 'tbl-payload-what-it-does-on-detonation', 'Mines — payload'),
      ('Deployables', 'tbl-family-c-traps', 'Traps'),
      ('Deployables', 'tbl-family-d-beacons', 'Beacons'),
      ]),

    ('7 · Terrain — the most powerful dial in the game',
     'Density alone swung win rate 66 points in simulation, more than any points '
     'cost could. Nine to twelve large features, one per 12" square.',
     [('Terrain', 'tbl-the-three-properties', 'The three independent properties'),
      ('Terrain', 'tbl-cover', 'Cover values'),
      ('Terrain', 'tbl-terrain-types', 'Terrain types and their defaults'),
      ('Terrain', 'tbl-hazards-the-dangerous-overlay', 'Hazards'),
      ('Terrain Interaction', 'tbl-interaction-verbs', 'Interact verbs and their stats'),
      ('Terrain Interaction', 'tbl-stat-ownership', 'Which stat owns which verb'),
      ('Terrain Interaction', 'tbl-searching-and-looting', 'Searching'),
      ('Terrain Interaction', 'tbl-in-battle-repair-settlement-hook', 'Feature damage and repair'),
      ('Infrastructure', 'tbl-infrastructure-vs-deployables', 'Infrastructure vs Deployables'),
      ('Infrastructure', 'tbl-the-five-categories', 'The five categories, eight verbs'),
      ]),

    ('8 · Scenarios and the battle layer',
     'You win on objectives, never on kills.',
     [('Scenarios', 'tbl-the-scenario-template', 'The scenario template'),
      ('Scenarios', 'tbl-the-twist-roll-1d6-at-setup', 'The Twist'),
      ('Events', 'tbl-battlefield-events', 'Battlefield events'),
      ('Hacking', 'tbl-range-bands', 'Hacking range bands'),
      ]),

    ('9 · The settlement — 23 structures and what they cost',
     'Space is the scarcest resource: 23 entries against room for about ten.',
     [('Settlement', 'tbl-choosing-a-location', 'Founding locations'),
      ('Structures', 'tbl-the-settlement-canvas', 'The canvas'),
      ('Structures', 'tbl-footprint-classes', 'Footprint classes'),
      ('Structures', 'tbl-starting-structures-five', 'The free starting four'),
      ('Structures', 'tbl-sustain-keep-people-alive-keep-the-grid-up', 'Sustain'),
      ('Structures', 'tbl-convert-turn-one-resource-into-another-and-m', 'Convert'),
      ('Structures', 'tbl-operate-what-you-can-do-outside-the-walls', 'Operate'),
      ('Structures', 'tbl-recover-people-come-back', 'Recover'),
      ('Structures', 'tbl-defend-this-is-the-raid-board', 'Defend — the raid board'),
      ('Structures', 'tbl-hq-tiers', 'HQ tiers'),
      ('Structures', 'tbl-upgrade-ladders', 'Upgrade ladders'),
      ('Structures', 'tbl-worker-benefits', 'Worker benefits'),
      ('Structures', 'tbl-space-budget', 'Space budget'),
      ]),

    ('10 · Economy, campaign and territory',
     'Credits buy what you own; Crew Rating gates what you field.',
     [('Economy', 'tbl-three-resources', 'The three resources'),
      ('Economy', 'tbl-power-draw-by-tier', 'Power draw by tier'),
      ('Economy', 'tbl-storage-containers', 'Storage containers'),
      ('Campaign', 'tbl-post-battle-the-fate-table', 'The Fate table'),
      ('Campaign', 'tbl-glorious-deeds', 'Glorious Deeds'),
      ('Territory', 'tbl-the-territory-card', 'The territory card'),
      ('Territory', 'tbl-the-default-loot-table', 'The default loot table'),
      ('Territory', 'tbl-control-states', 'Control states'),
      ]),

    ('11 · Guard rails — the numbers nothing may exceed',
     'These are load-bearing. Every one of them exists because something broke '
     'without it.',
     [('Out of Scope — What Settlements is NOT', 'tbl-4-rejected-ideas-log',
       'The rejected/allowed log, including the WND 3 ceiling')]),

    ('12 · What the simulations found',
     'Balance evidence, so a number can be argued with rather than asserted.',
     [('Crew Sim — Findings', 'tbl-1-terrain-is-a-bigger-lever-than-any-point-c', 'Terrain density beats any points cost'),
      ('Crew Sim — Findings', 'tbl-2-the-final-balance-table', 'The archetype balance table'),
      ('List Building', 'tbl-validation', 'Spread by board legality'),
      ('Skill Sim — Findings', None, 'Skill value measurements'),
      ('Dice Mechanic — Sim Findings', None, 'The core-test curve'),
      ]),
]


def anchors_in(note_text):
    return set(re.findall(r'^\^([a-z0-9-]+)\s*$', note_text, re.M))


def scan_vault():
    notes, all_anchors, unanchored = {}, {}, []
    for f in sorted(os.listdir(VAULT)):
        if not f.endswith('.md') or f.startswith('_Rules Catalogue'):
            continue
        stem = f[:-3]
        s = io.open(os.path.join(VAULT, f), encoding='utf-8').read()
        notes[stem] = s
        all_anchors[stem] = anchors_in(s)
        lines = s.split('\n')
        for i, ln in enumerate(lines):
            if (re.match(r'^\s*\|.+\|\s*$', ln) and i + 1 < len(lines)
                    and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i + 1])):
                found = False
                for j in range(i, min(i + 40, len(lines))):
                    if re.match(r'^\^[a-z0-9-]+\s*$', lines[j].strip()):
                        found = True
                        break
                    if j > i + 2 and lines[j].startswith('#'):
                        break
                if not found:
                    head = ''
                    for k in range(i, -1, -1):
                        if lines[k].startswith('#'):
                            head = lines[k].lstrip('#').strip()
                            break
                    unanchored.append((stem, head[:50]))
    return notes, all_anchors, unanchored


def build(notes, all_anchors):
    used, missing = set(), []
    out = [
        '---',
        'type: catalogue',
        'title: Rules Catalogue',
        'tags:',
        '  - settlements/catalogue',
        '---',
        '# 📚 Rules Catalogue — every table in one place',
        '',
        '> [!info] This is a LENS, not a copy',
        '> Every table below is a live **block embed** of the real table in its own'
        ' note. **Edit the source and this page updates automatically.** Embeds are'
        ' read-only in place, so each block prints its source link — click through'
        ' to edit.',
        '>',
        '> Generated by `scripts/build_catalogue.py`. Re-run it after adding a'
        ' table; it reports anything it could not place, so this page cannot go'
        ' quietly stale.',
        '',
        '> [!tip] Reading this for design review',
        '> §2 is the whole customisation surface a player touches. §3 is the block'
        ' for judging whether T1/T2/T3 are correctly spaced. §11 is every hard'
        ' ceiling in the game, and §12 is the evidence behind the numbers.',
        '',
        '**Ruling order:** [[Full Rules System v1]] wins over any phase note. Where'
        ' this catalogue and the master note disagree, the master note is right and'
        ' this page needs regenerating.',
        '',
        '---',
        '',
        '## Contents',
        '',
    ]
    for title, _, _ in SECTIONS:
        slug = title.split('·')[-1].strip().replace(' ', '%20')
        out.append(f'- [[#{title}|{title}]]')
    out.append('')
    out.append('---')
    out.append('')

    for title, blurb, items in SECTIONS:
        out.append(f'## {title}')
        out.append('')
        out.append(f'*{blurb}*')
        out.append('')
        for note, anchor, caption in items:
            if note not in notes:
                missing.append((note, anchor, 'note not found'))
                continue
            if anchor and anchor not in all_anchors.get(note, set()):
                missing.append((note, anchor, 'anchor not found'))
                out.append(f'> [!warning] Missing anchor `^{anchor}` in [[{note}]] — '
                           f'{caption}')
                out.append('')
                continue
            out.append(f'**{caption}** · source: [[{note}]]')
            out.append('')
            out.append(f'![[{note}#^{anchor}]]' if anchor else f'![[{note}]]')
            out.append('')
            if anchor:
                used.add((note, anchor))
        out.append('---')
        out.append('')

    # coverage: which anchored tables never made it into the document
    every = {(n, a) for n, anc in all_anchors.items() for a in anc}
    orphan = sorted(every - used)
    out.append('## Coverage')
    out.append('')
    out.append(f'{len(used)} tables embedded · {len(orphan)} anchored tables not '
               f'placed in a section.')
    out.append('')
    if orphan:
        out.append('> [!question] Anchored tables this catalogue does not show')
        out.append('> Either add them to a section in `build_catalogue.py`, or '
                   'accept them as note-local detail.')
        out.append('>')
        for n, a in orphan:
            out.append(f'> - [[{n}]] `^{a}`')
        out.append('')
    return '\n'.join(out), missing, orphan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='report only, do not write')
    args = ap.parse_args()

    if not os.path.isdir(VAULT):
        print(f'no vault at {VAULT}', file=sys.stderr)
        return 1
    notes, all_anchors, unanchored = scan_vault()
    text, missing, orphan = build(notes, all_anchors)

    print(f'scanned {len(notes)} notes')
    print(f'embedded {text.count("![[")} blocks')
    if missing:
        print(f'\nCOULD NOT EMBED ({len(missing)}):')
        for n, a, why in missing:
            print(f'  {n} ^{a}: {why}')
    if orphan:
        print(f'\nANCHORED BUT NOT PLACED ({len(orphan)}):')
        for n, a in orphan[:18]:
            print(f'  [[{n}]] ^{a}')
        if len(orphan) > 18:
            print(f'  ... +{len(orphan) - 18} more')
    if unanchored:
        print(f'\nTABLES WITH NO ANCHOR — cannot be embedded at all ({len(unanchored)}):')
        seen = {}
        for n, h in unanchored:
            seen.setdefault(n, 0)
            seen[n] += 1
        for n, c in sorted(seen.items(), key=lambda kv: -kv[1]):
            print(f'  {n}: {c}')

    if args.check:
        print('\n(--check: nothing written)')
        return 0
    out = os.path.join(VAULT, OUT_NAME)
    io.open(out, 'w', encoding='utf-8', newline='').write(text)
    print(f'\nwrote {out}  ({len(text):,} chars)')
    return 0


if __name__ == '__main__':
    sys.exit(main())

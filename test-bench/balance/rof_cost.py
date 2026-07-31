# -*- coding: utf-8 -*-
"""What does RoF 2 actually COST? Rebuild the list to pay for it, no to-hit penalty."""
import sys, random
from collections import Counter

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

CFG = {'rof': {}}
STATS = Counter()
for w in cs.WEAPONS.values():
    w.setdefault('rof', 1)


def shoot_rof(att, dfn, dfn_allies, T):
    W = cs.WEAPONS[att['weapon']]
    if W['rng'] == 0: return False
    if abs(att['pos'] - dfn['pos']) > W['rng']: return False
    if not cs.can_see(T): return False
    cov = cs.cover_of(T)
    if dfn['down']: cov = min(cov, -2)
    mod = att['dex'] + cov - cs.shaken(att)
    n = CFG['rof'].get(att['weapon'], 1)
    hits = sum(1 for _ in range(n) if cs.core(mod))
    if hits:
        cs.injure(att, dfn, True, dfn_allies, T)
        if hits > 1 and not (dfn['down'] or dfn['out']):
            cs.add_stress(dfn, hits - 1)
            STATS['extra'] += hits - 1
    return True

_ob = cs.break_test
def bt(u):
    was = (u['out'], u['down'])
    _ob(u)
    if u['out'] and not was[0] and not was[1]: STATS['bug'] += 1
cs.shoot = shoot_rof
cs.break_test = bt

F = cs.fighter

# baseline Cadre = 100 pts exactly
def CADRE():
    return [F('Leader', 'rifle', 'light', dex=4, str=2),
            F('Specialist', 'rifle', 'light', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2)]

# --- RoF variants, each PAYING for the upgrade by giving something up --------
def CADRE_NOARM():          # riflemen drop Light armour  (-12 pts of kit)
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'rifle', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2)]

def CADRE_NOARM_FISTS():    # + both Fighters lose pistols (-8 more)
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'rifle', dex=4),
            F('Fighter', 'fists', dex=2),
            F('Fighter', 'fists', dex=2)]

def CADRE_3():              # drop a whole Fighter (-12 pts)
    return [F('Leader', 'rifle', 'light', dex=4, str=2),
            F('Specialist', 'rifle', 'light', dex=4),
            F('Fighter', 'pistol', dex=2)]

def CADRE_3_NOARM():        # drop a Fighter AND the armour (-24 pts)
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'rifle', dex=4),
            F('Fighter', 'pistol', dex=2)]

VARIANTS = [
    ('baseline (no RoF)',        CADRE,            {},            0),
    ('RoF2, nothing given up',   CADRE,            {'rifle': 2},  0),
    ('RoF2, riflemen no armour', CADRE_NOARM,      {'rifle': 2}, 12),
    ('RoF2, no armour + fists',  CADRE_NOARM_FISTS,{'rifle': 2}, 20),
    ('RoF2, 3 models',           CADRE_3,          {'rifle': 2}, 12),
    ('RoF2, 3 models no armour', CADRE_3_NOARM,    {'rifle': 2}, 24),
]

FOES = ['Pyramid mob (11)', 'Fighter horde (9 STR)', 'Standard (6)']
N = 2000

def run(build, foe, density, seed=20260713):
    random.seed(seed); STATS.clear()
    w = d = 0
    for _ in range(N):
        res, *_ = cs.battle(build(), cs.LISTS[foe](), density)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / N, STATS['bug'] / N, STATS['extra'] / N

print("=" * 100)
print("WHAT DOES RoF 2 COST?   No to-hit penalty. The list PAYS in dropped kit/models.")
print("=" * 100)
print(f"\nBaseline Cadre = 100 pts. 'given up' = points of kit removed to fund RoF.\n")
print(f"    {'variant':<28}{'models':>7}{'pts':>6}{'gave up':>9}"
      + "".join(f"{f.split(' (')[0][:12]:>13}" for f in FOES))

for density in ('medium', 'dense'):
    print(f"\n  [{density.upper()}]")
    base = {}
    for label, build, rof, given in VARIANTS:
        CFG['rof'] = rof
        crew = build()
        cells = []
        for foe in FOES:
            wr, bug, ex = run(build, foe, density)
            if label.startswith('baseline'):
                base[foe] = wr
                cells.append(f"{wr*100:12.0f} ")
            else:
                cells.append(f"{wr*100:7.0f}({(wr-base[foe])*100:+3.0f})")
        print(f"    {label:<28}{len(crew):>7}{cs.crew_cost(crew):>6}{given:>9}"
              + "".join(cells))

print("\n" + "=" * 100)
print("Reading: find the variant whose deltas sit near 0 — that's what RoF 2 is worth.")
print("=" * 100)

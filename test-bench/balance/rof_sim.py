# -*- coding: utf-8 -*-
"""Rate of Fire test harness — extends crew_sim without modifying it.

RoF(N): roll N dice to hit. First hit resolves in full (Injury roll / Pin).
Each ADDITIONAL hit = +1 Stress on the same target. No extra Injury rolls.
Extra hits are wasted if the target goes Down from the first hit.
"""
import sys, random
from collections import Counter

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

CFG = {'rof': {}, 'penalty': 0}
STATS = Counter()

for w in cs.WEAPONS.values():
    w.setdefault('rof', 1)


def shoot_rof(att, dfn, dfn_allies, T):
    W = cs.WEAPONS[att['weapon']]
    rng = W['rng']
    if rng == 0: return False
    if abs(att['pos'] - dfn['pos']) > rng: return False
    if not cs.can_see(T): return False
    cov = cs.cover_of(T)
    if dfn['down']: cov = min(cov, -2)
    mod = att['dex'] + cov - cs.shaken(att) + CFG['penalty']
    n = CFG['rof'].get(att['weapon'], 1)
    hits = sum(1 for _ in range(n) if cs.core(mod))
    if hits:
        STATS['hits'] += hits
        cs.injure(att, dfn, True, dfn_allies, T)
        extra = hits - 1
        if extra and not (dfn['down'] or dfn['out']):
            cs.add_stress(dfn, extra)
            STATS['extra_stress'] += extra
    STATS['shots'] += 1
    return True


_orig_break = cs.break_test

def break_test_counted(u):
    was = (u['out'], u['down'], u['stress'])
    _orig_break(u)
    if u['out'] and not was[0] and not was[1]:
        STATS['bugouts'] += 1
    elif u['skip'] and was[2] >= 2:
        STATS['breaks'] += 1

cs.shoot = shoot_rof
cs.break_test = break_test_counted


def run(rn, cn, density, n=1500, seed=20260713):
    random.seed(seed)
    STATS.clear()
    w = d = 0; rounds = 0; sa = 0; sb = 0
    for _ in range(n):
        res, rnd, ea, eb = cs.battle(cs.LISTS[rn](), cs.LISTS[cn](), density)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
        rounds += rnd; sa += ea; sb += eb
    return dict(wr=(w + 0.5 * d) / n, rounds=rounds / n, sa=sa / n, sb=sb / n,
                bugouts=STATS['bugouts'] / n, breaks=STATS['breaks'] / n,
                extra=STATS['extra_stress'] / n, shots=STATS['shots'] / n)


SCENARIOS = [
    ("baseline",        {},                            0),
    ("rifle RoF2",      {'rifle': 2},                   0),
    ("rifle RoF2 (-1)", {'rifle': 2},                  -1),
    ("rifle RoF2 (-2)", {'rifle': 2},                  -2),
    ("rifle+sg RoF2",   {'rifle': 2, 'shotgun': 2},     0),
    ("rifle RoF3",      {'rifle': 3},                   0),
]

MATCHUPS = [
    ('Cadre (4, pure DEX)', 'Pyramid mob (11)'),
    ('Cadre (4, pure DEX)', 'Standard (6)'),
    ('Standard (6)',        'Pyramid mob (11)'),
    ('Cadre (4, pure DEX)', 'Fighter horde (9 STR)'),
]

print("=" * 96)
print("RATE OF FIRE — balance probe   (extends crew_sim.py, original untouched)")
print("RoF(N): N hit dice - first hit resolves fully - each extra hit = +1 Stress")
print("=" * 96)

print("\n[1] STRESS ECONOMY — validated baseline is 0.6 BugOuts/battle on a LEGAL board")
print(f"    {'scenario':<18}{'density':<9}{'BugOut/bat':>12}{'Break/bat':>11}"
      f"{'xStress/bat':>13}{'rounds':>9}")
for name, rof, pen in SCENARIOS:
    CFG['rof'], CFG['penalty'] = rof, pen
    for density in ('medium', 'dense'):
        r = run('Cadre (4, pure DEX)', 'Pyramid mob (11)', density)
        print(f"    {name:<18}{density:<9}{r['bugouts']:>12.2f}{r['breaks']:>11.2f}"
              f"{r['extra']:>13.2f}{r['rounds']:>9.1f}")

print("\n[2] ELITE vs SWARM — does RoF shift the archetype balance?")
print("    (win% for the FIRST list; baseline delta in brackets)")
base = {}
for name, rof, pen in SCENARIOS:
    CFG['rof'], CFG['penalty'] = rof, pen
    print(f"\n    {name}")
    print(f"      {'matchup':<44}{'open':>10}{'medium':>10}{'dense':>10}")
    for a, b in MATCHUPS:
        cells = []
        for density in ('open', 'medium', 'dense'):
            r = run(a, b, density)
            key = (a, b, density)
            if name == 'baseline':
                base[key] = r['wr']
                cells.append(f"{r['wr']*100:9.0f} ")
            else:
                d = (r['wr'] - base[key]) * 100
                cells.append(f"{r['wr']*100:5.0f}({d:+3.0f})")
        label = f"{a.split(' (')[0]} vs {b.split(' (')[0]}"
        print(f"      {label:<44}" + "".join(cells))

print("\n[3] LETHALITY — survivors at end of battle (Cadre vs Pyramid, medium)")
print(f"    {'scenario':<18}{'Cadre alive':>13}{'Mob alive':>12}{'rounds':>9}")
for name, rof, pen in SCENARIOS:
    CFG['rof'], CFG['penalty'] = rof, pen
    r = run('Cadre (4, pure DEX)', 'Pyramid mob (11)', 'medium')
    print(f"    {name:<18}{r['sa']:>13.2f}{r['sb']:>12.2f}{r['rounds']:>9.1f}")

print("\n" + "=" * 96)

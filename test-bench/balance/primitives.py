# -*- coding: utf-8 -*-
"""Primitive exchange-rate probe.

Q1  What is +1 to-hit worth vs +1 Damage vs +1 Armour?  (sets the anchor)
Q2  What is +1 Stress worth, and how non-linear is it?
Q3  Is armour's value hidden by the 6-round clock?
"""
import sys, random, copy
from collections import Counter

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

BASE_W = copy.deepcopy(cs.WEAPONS)
BUFF = {'hit': 0, 'dmg': 0, 'arm': 0, 'stress': 0}
STATS = Counter()

# ---- patched injure: honours dmg/arm/stress buffs, records target Stress ----
def injure(att, dfn, ranged, dfn_allies, T):
    sk = cs.shaken(att)
    dmg = cs.WEAPONS[att['weapon']]['dmg'] + (BUFF['dmg'] if att.get('buffed') else 0)
    arm = cs.ARMOUR[dfn['armour']][0] - (BUFF['arm'] if dfn.get('buffed') else 0)
    STATS[f"hit_at_stress_{min(dfn['stress'],3)}"] += 1
    STATS['hits'] += 1
    if cs.core(dmg + arm - sk):
        dfn['w'] -= 1
        if dfn['w'] <= 0:
            cs.go_down(dfn, ranged, dfn_allies, T)
        else:
            cs.add_stress(dfn, 1)
        return True
    if ranged: dfn['pinned'] = True
    cs.add_stress(dfn, 1)
    if BUFF['stress'] and att.get('buffed'):
        cs.add_stress(dfn, BUFF['stress'])
    return False

cs.injure = injure

_ob = cs.break_test
def bt(u):
    was = (u['out'], u['down'])
    _ob(u)
    if u['out'] and not was[0] and not was[1]: STATS['bug'] += 1
cs.break_test = bt


def tag(crew, hit_bonus):
    for f in crew:
        f['buffed'] = True
        f['dex'] += hit_bonus
        f['str'] += hit_bonus
    return crew


def run(mk_a, mk_b, density, hit=0, n=2000, rounds=6, seed=20260713):
    random.seed(seed); STATS.clear()
    w = d = 0
    for _ in range(n):
        A = tag(mk_a(), hit)
        B = mk_b()
        res, *_ = cs.battle(A, B, density, max_rounds=rounds)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / n


LISTS = {
    'Cadre (4)':   cs.CADRE,
    'Standard (6)': cs.STANDARD,
    'Pyramid (11)': cs.PYRAMID_MOB,
}
FOE = cs.PYRAMID_MOB
FOE2 = cs.CADRE

CONDITIONS = [
    ('baseline',        dict(hit=0, dmg=0, arm=0, stress=0)),
    ('+1 to-hit',       dict(hit=1, dmg=0, arm=0, stress=0)),
    ('+1 Damage',       dict(hit=0, dmg=1, arm=0, stress=0)),
    ('+1 Armour',       dict(hit=0, dmg=0, arm=1, stress=0)),
    ('+1 Stress on hit',dict(hit=0, dmg=0, arm=0, stress=1)),
]

print("=" * 92)
print("PRIMITIVE EXCHANGE RATES — each buff given FREE to side A; compare the deltas")
print("Equal deltas => equal cost. This sets the relative scale, not the absolute anchor.")
print("=" * 92)

for density in ('medium', 'dense'):
    print(f"\n  [{density.upper()}]   win% for the buffed list (delta vs its own baseline)")
    print(f"    {'buff':<20}" + "".join(f"{k:>22}" for k in LISTS))
    base = {}
    for label, cfg in CONDITIONS:
        BUFF.update({k: v for k, v in cfg.items() if k != 'hit'})
        cells = []
        for lname, mk in LISTS.items():
            foe = FOE2 if lname == 'Pyramid (11)' else FOE
            wr = run(mk, foe, density, hit=cfg['hit'])
            if label == 'baseline':
                base[lname] = wr
                cells.append(f"{wr*100:21.1f} ")
            else:
                cells.append(f"{wr*100:15.1f}({(wr-base[lname])*100:+5.1f})")
        print(f"    {label:<20}" + "".join(cells))

print("\n" + "=" * 92)
print("Q3  IS ARMOUR HIDDEN BY THE 6-ROUND CLOCK?   Cadre(4) vs Pyramid(11), medium")
print("=" * 92)
print(f"    {'rounds':<9}{'baseline':>11}{'+1 Armour':>12}{'delta':>9}{'+1 Damage':>12}{'delta':>9}")
for rounds in (6, 10, 16):
    BUFF.update(dmg=0, arm=0, stress=0)
    b = run(cs.CADRE, FOE, 'medium', rounds=rounds)
    BUFF.update(arm=1)
    a = run(cs.CADRE, FOE, 'medium', rounds=rounds)
    BUFF.update(arm=0, dmg=1)
    dm = run(cs.CADRE, FOE, 'medium', rounds=rounds)
    BUFF.update(dmg=0)
    print(f"    {rounds:<9}{b*100:10.1f} {a*100:11.1f} {(a-b)*100:+8.1f}"
          f"{dm*100:11.1f} {(dm-b)*100:+8.1f}")

print("\n" + "=" * 92)
print("Q2  STRESS NON-LINEARITY — what Stress is a target ALREADY on when hit?")
print("=" * 92)
BUFF.update(dmg=0, arm=0, stress=0)
for density in ('medium', 'dense'):
    random.seed(20260713); STATS.clear()
    for _ in range(1500):
        cs.battle(cs.CADRE(), FOE(), density)
    tot = STATS['hits'] or 1
    dist = [STATS[f'hit_at_stress_{i}'] / tot for i in range(4)]
    print(f"    {density:<8} target already at:  "
          + "  ".join(f"{i}{'+' if i==3 else ''} Stress {d:5.1%}" for i, d in enumerate(dist)))
print("\n    (a hit landing on a target already at 1+ Stress can push it over the")
print("     Break-test threshold of 2 — that is where +1 Stress earns its price)")
print("=" * 92)

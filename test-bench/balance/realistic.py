# -*- coding: utf-8 -*-
"""Re-run the primitive exchange rates against REALISTIC lists — everyone armed.

The stock sim lists give 10 of 11 models a bat because at 100 pts an 11-model
crew has ~9 pts/model and a pistol costs 4. No real player fields that.
"""
import sys, random, copy
from collections import Counter

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

BUFF = {'dmg': 0, 'arm': 0, 'stress': 0}
STATS = Counter()
F = cs.fighter

def injure(att, dfn, ranged, dfn_allies, T):
    sk = cs.shaken(att)
    dmg = cs.WEAPONS[att['weapon']]['dmg'] + (BUFF['dmg'] if att.get('buffed') else 0)
    arm = cs.ARMOUR[dfn['armour']][0] - (BUFF['arm'] if dfn.get('buffed') else 0)
    if cs.core(dmg + arm - sk):
        dfn['w'] -= 1
        if dfn['w'] <= 0: cs.go_down(dfn, ranged, dfn_allies, T)
        else: cs.add_stress(dfn, 1)
        return True
    if ranged: dfn['pinned'] = True
    cs.add_stress(dfn, 1)
    if BUFF['stress'] and att.get('buffed'): cs.add_stress(dfn, BUFF['stress'])
    return False
cs.injure = injure

# ---- realistic lists: EVERY model that can hold a gun, holds one -------------
def GUNLINE4():      # 100 — the elite shooters (unchanged, already realistic)
    return [F('Leader', 'rifle', 'light', dex=4, str=2),
            F('Specialist', 'rifle', 'light', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2)]

def FIRETEAM6():     # 98 — mixed, all armed
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'shotgun', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'bat', str=1)]

def SQUAD8():        # 100 — max models with everyone armed
    return [F('Leader', 'shotgun', dex=2, str=2, nrv=2),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'bat', str=1)]

def MOB11():         # 97 — the stock melee horde, for comparison
    return cs.PYRAMID_MOB()

LISTS = {'Gunline (4)': GUNLINE4, 'Fireteam (6)': FIRETEAM6,
         'Squad (8)': SQUAD8, 'Mob (11, melee)': MOB11}

def tag(crew, hit):
    for f in crew:
        f['buffed'] = True; f['dex'] += hit; f['str'] += hit
    return crew

def run(mk_a, mk_b, density, hit=0, n=2000, seed=20260713):
    random.seed(seed)
    w = d = 0
    for _ in range(n):
        res, *_ = cs.battle(tag(mk_a(), hit), mk_b(), density)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / n

print("=" * 100)
print("REALISTIC LISTS — points check")
print("=" * 100)
for n, mk in LISTS.items():
    c = mk()
    guns = sum(1 for f in c if cs.WEAPONS[f['weapon']]['rng'] > 0)
    print(f"    {n:<18}{len(c):>3} models  {cs.crew_cost(c):>4} pts   {guns}/{len(c)} armed")

print("\n" + "=" * 100)
print("[A] THE MATRIX — row wins % vs column (medium / dense)")
print("=" * 100)
for density in ('medium', 'dense'):
    print(f"\n  [{density.upper()}]")
    print(f"    {'':<18}" + "".join(f"{n.split(' (')[0][:12]:>14}" for n in LISTS))
    for rn, rmk in LISTS.items():
        cells = []
        for cn, cmk in LISTS.items():
            if rn == cn: cells.append(f"{'—':>14}"); continue
            BUFF.update(dmg=0, arm=0, stress=0)
            cells.append(f"{run(rmk, cmk, density)*100:13.1f} ")
        print(f"    {rn:<18}" + "".join(cells))

print("\n" + "=" * 100)
print("[B] PRIMITIVE VALUE per model buffed  (delta / models) — realistic lists only")
print("=" * 100)
PRIMS = [('+1 to-hit', dict(hit=1, dmg=0, arm=0, stress=0)),
         ('+1 Damage', dict(hit=0, dmg=1, arm=0, stress=0)),
         ('+1 Armour', dict(hit=0, dmg=0, arm=1, stress=0)),
         ('+1 Stress', dict(hit=0, dmg=0, arm=0, stress=1))]
TEST = ['Gunline (4)', 'Fireteam (6)', 'Squad (8)']

for density in ('medium', 'dense'):
    print(f"\n  [{density.upper()}]  total delta, and (per model)")
    print(f"    {'primitive':<14}" + "".join(f"{n:>24}" for n in TEST))
    base = {}
    for lname in TEST:
        BUFF.update(dmg=0, arm=0, stress=0)
        foe = SQUAD8 if lname != 'Squad (8)' else GUNLINE4
        base[lname] = (run(LISTS[lname], foe, density), len(LISTS[lname]()))
    print(f"    {'baseline':<14}" + "".join(f"{base[n][0]*100:23.1f} " for n in TEST))
    for label, cfg in PRIMS:
        BUFF.update({k: v for k, v in cfg.items() if k != 'hit'})
        cells = []
        for lname in TEST:
            foe = SQUAD8 if lname != 'Squad (8)' else GUNLINE4
            wr = run(LISTS[lname], foe, density, hit=cfg['hit'])
            b, m = base[lname]
            d = (wr - b) * 100
            cells.append(f"{d:+13.1f} ({d/m:+5.2f})")
        print(f"    {label:<14}" + "".join(cells))

print("\n" + "=" * 100)

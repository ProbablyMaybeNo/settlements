# -*- coding: utf-8 -*-
"""Pricing problem or list-building problem?

Melee-only crews, all legal at ~100 pts, trading bodies for armour.
If an armoured build already wins, armour is fine and players just build badly.
"""
import sys, random

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

F = cs.fighter

def heavy_fix(crew):
    for f in crew:
        if f['armour'] == 'heavy':
            f['mov'] = 5.0          # Cumbersome: -1 MOV (not modelled in ARMOUR)
    return crew

# ---- all melee-only, all legal under the pyramid, all <=100 pts -------------
def BARE11():           # 93 — max bodies, no protection
    return [F('Leader', 'sledge', str=4, nrv=2)] + \
           [F('Fighter', 'bat', str=2) for _ in range(5)] + \
           [F('Recruit', 'bat') for _ in range(5)]

def IMPROV8():          # 99 — everyone in scrap
    return heavy_fix(
        [F('Leader', 'sledge', 'improvised', str=4, nrv=2)] +
        [F('Fighter', 'bat', 'improvised', str=2) for _ in range(4)] +
        [F('Recruit', 'bat', 'improvised') for _ in range(3)])

def LIGHT6():           # 98 — proper armour, six bodies
    return heavy_fix(
        [F('Leader', 'sledge', 'light', str=4, nrv=2)] +
        [F('Fighter', 'bat', 'light', str=2) for _ in range(3)] +
        [F('Recruit', 'bat', 'light') for _ in range(2)])

def HEAVY5():           # 97 — armoured fist, five bodies, -1 MOV
    return heavy_fix(
        [F('Leader', 'sledge', 'heavy', str=4, nrv=2)] +
        [F('Fighter', 'bat', 'heavy', str=2) for _ in range(3)] +
        [F('Recruit', 'bat')])

def MIXED8():           # 96 — armoured core, bare chaff
    return heavy_fix(
        [F('Leader', 'sledge', 'light', str=4, nrv=2)] +
        [F('Fighter', 'bat', 'improvised', str=2) for _ in range(4)] +
        [F('Recruit', 'bat', 'improvised')] +
        [F('Recruit', 'bat') for _ in range(2)])

MELEE = {'Bare 11': BARE11, 'Improvised 8': IMPROV8, 'Light 6': LIGHT6,
         'Heavy 5': HEAVY5, 'Mixed 8': MIXED8}

def FIRETEAM6():
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'shotgun', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'bat', str=1)]

FOES = {'Gunline (4)': cs.CADRE, 'Fireteam (6)': FIRETEAM6}

def run(a, b, density, n=2500, seed=20260713):
    random.seed(seed)
    w = d = 0
    for _ in range(n):
        res, *_ = cs.battle(a(), b(), density)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / n

print("=" * 92)
print("MELEE: TRADE BODIES FOR ARMOUR — is it a pricing problem or a build problem?")
print("=" * 92)
print(f"\n    {'build':<15}{'models':>7}{'pts':>5}{'armour':>12}")
for n, mk in MELEE.items():
    c = mk()
    arm = c[0]['armour']
    print(f"    {n:<15}{len(c):>7}{cs.crew_cost(c):>5}{arm:>12}")

print(f"\n{'=' * 92}")
print("win % for the melee build")
print(f"    {'build':<15}" + "".join(f"{f'{k} {d}':>20}"
      for k in FOES for d in ('med', 'dense')))
for n, mk in MELEE.items():
    cells = []
    for k, foe in FOES.items():
        for density in ('medium', 'dense'):
            cells.append(f"{run(mk, foe, density)*100:19.1f} ")
    print(f"    {n:<15}" + "".join(cells))

print(f"\n{'=' * 92}")
print("MELEE vs MELEE — which build is actually the best melee crew?")
print(f"    {'':<15}" + "".join(f"{n[:11]:>13}" for n in MELEE))
for rn, rmk in MELEE.items():
    cells = []
    for cn, cmk in MELEE.items():
        if rn == cn: cells.append(f"{'—':>13}"); continue
        cells.append(f"{run(rmk, cmk, 'medium')*100:12.1f} ")
    print(f"    {rn:<15}" + "".join(cells))
print("    (medium density)")
print("=" * 92)

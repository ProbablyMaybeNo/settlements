# -*- coding: utf-8 -*-
"""AUDIT FIX 3 + Part D test 2 — Campaign Start @ 500 under the fixed pyramid.

FIX 3: Campaign Start keeps the Specialist ratio (every Specialist needs two
fighters of lower rank); only the Recruit ratio is waived. This harness fields:

  OldElite   Leader + 2 Specialists in heavy armour — LEGAL under the old loose
             pyramid ("one Leader, min 3 models, no ratio"), ILLEGAL under FIX 3.
             The degenerate the fix exists to close.
  Fix3Elite  Leader + Specialist + 2 Fighters — the most elite FIX-3-legal start.
  + the five standard archetypes (all FIX-3-legal).

PASS (Part D test 2): with FIX 3 crews only, no archetype's mean win > 60%.
The OldElite row is measured alongside to show what the fix removes.

Second half of test 2 — Level pacing ("a fighter reaches ~Level 3 by battle 3"):
estimated from the sim's own casualty/survival aggregates + the §26.1 triggers
(kill, survive, objective held, Glorious Deed), printed as arithmetic at the end.
"""
import itertools
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.dirname(HERE)
ENG = os.path.join(BENCH, 'engine2d')
sys.path.insert(0, BENCH)
sys.path.insert(0, ENG)
os.chdir(ENG)

import data
from points.weapons import WeaponBuild, weapon_cost
from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
BUDGET = 500

BUILDS = {
    'bat':     WeaponBuild('Baseball Bat', 'light_melee'),
    'crowbar': WeaponBuild('Crowbar', 'one_handed_melee', ('breaching',)),
    'sledge':  WeaponBuild('Sledgehammer', 'heavy_melee'),
    'pistol':  WeaponBuild('Pistol', 'sidearm'),
    'rifle':   WeaponBuild('Rifle', 'standard_ranged'),
}
for k, b in BUILDS.items():
    data.WEAPONS[k]['cost'] = weapon_cost(b)
for k, v in {'none': 0, 'light': 60, 'heavy': 100}.items():
    data.ARMOUR[k]['cost'] = v
for rank, cost in dict(Recruit=65, Fighter=75, Specialist=125, Leader=170).items():
    data.RANKS[rank]['cost'] = cost


def C(rank, weapon='bat', armour='none'):
    return data.unit_cost(rank, weapon, armour)


def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


# Fixed legal lists (greedy fill hits 500-cap quantization traps — a known issue
# from the campaign500 grid work; hand-built lists keep every crew legal).
# Prices: bat 0 / pistol 40 / crowbar 70 / sledge 80 / rifle 100; light armour 60.
def old_elite(side):
    """Leader + 2 Specialists, exactly 500 — LEGAL pre-FIX-3, ILLEGAL after."""
    crew = [Unit('Boss', side, 'Leader', 'pistol', dex=4, nrv=3, str=2),
            Unit('S0', side, 'Specialist', 'pistol',
                 skills=('pin_them_down_T2',), dex=4, nrv=2, int=1),
            Unit('S1', side, 'Specialist', 'bat',
                 skills=('super_slam_T2',), str=4, nrv=2, agi=1)]
    return _p(crew)


def fix3_elite(side):
    """Leader + Specialist + 2 Fighters (485) — the most elite FIX-3-legal start."""
    crew = [Unit('Boss', side, 'Leader', 'bat', str=4, nrv=3, agi=2),
            Unit('S0', side, 'Specialist', 'pistol',
                 skills=('pin_them_down_T2',), dex=4, nrv=2, int=1),
            Unit('F0', side, 'Fighter', 'bat', skills=('knockback',),
                 str=2, nrv=2, agi=1),
            Unit('F1', side, 'Fighter', 'bat', skills=('knockback',),
                 str=2, nrv=2, agi=1)]
    return _p(crew)


def swarm(side):
    """Leader + 5 Recruits (495) — maximum bodies."""
    crew = [Unit('Boss', side, 'Leader', 'bat', str=4, nrv=3, agi=2)]
    crew += [Unit(f'R{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1)
             for i in range(5)]
    return _p(crew)


def line(side):
    """Leader sledge + Fighter crowbar + Fighter bat (470)."""
    crew = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=3, agi=2),
            Unit('F0', side, 'Fighter', 'crowbar', skills=('knockback',),
                 str=2, nrv=2, agi=1),
            Unit('F1', side, 'Fighter', 'bat', skills=('knockback',),
                 str=2, nrv=2, agi=1)]
    return _p(crew)


def gunline(side):
    """Leader rifle + 2 Fighter pistols (500)."""
    crew = [Unit('Boss', side, 'Leader', 'rifle', dex=4, nrv=3, str=2),
            Unit('F0', side, 'Fighter', 'pistol', skills=('ready_to_react',),
                 dex=2, nrv=2, agi=1),
            Unit('F1', side, 'Fighter', 'pistol', skills=('ready_to_react',),
                 dex=2, nrv=2, agi=1)]
    return _p(crew)


def armoured(side):
    """Leader + 2 Fighters, all in light armour with bats (500)."""
    crew = [Unit('Boss', side, 'Leader', 'bat', 'light', str=4, nrv=3, agi=2),
            Unit('F0', side, 'Fighter', 'bat', 'light', skills=('knockback',),
                 str=2, nrv=2, agi=1),
            Unit('F1', side, 'Fighter', 'bat', 'light', skills=('knockback',),
                 str=2, nrv=2, agi=1)]
    return _p(crew)


CREWS = {'OldElite': old_elite, 'Fix3Elite': fix3_elite, 'Swarm': swarm,
         'Line': line, 'Gunline': gunline, 'Armoured': armoured}
FIX3_LEGAL = [n for n in CREWS if n != 'OldElite']
names = list(CREWS)


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


class Breakthrough(Game):
    def score_objectives(self, rnd):
        if rnd >= 2:
            self.vp[0] += sum(1 for u in self._standing(0) if u.pos[1] > 18.0)
            self.vp[1] += sum(1 for u in self._standing(1) if u.pos[1] < 18.0)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {'Hold': (Game, dict()), 'Hold+Claim': (Game, dict(claim=True)),
             'Annihilate': (Annihilate, dict()), 'Breakthrough': (Breakthrough, dict())}

# pacing aggregates: per-battle enemy casualties + own survivors, by crew
PACE = {n: dict(kills=0.0, survivors=0.0, models=0.0, battles=0) for n in names}


def versus(aname, bname, GameCls, kw, n, seed=20260807):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        a0 = i % 2 == 0
        A, B = (CREWS[aname], CREWS[bname]) if a0 else (CREWS[bname], CREWS[aname])
        g = GameCls(A(0), B(1), board, **kw)
        r = g.play()
        w0 = r['winner'] == 'A'
        w1 = r['winner'] == 'B'
        win_a = w0 if a0 else w1
        win_b = w1 if a0 else w0
        wa += win_a
        wb += win_b
        dr += (not win_a and not win_b)
        for side, nm in ((0, aname if a0 else bname), (1, bname if a0 else aname)):
            PACE[nm]['kills'] += sum(1 for u in g.sides[1 - side] if u.out or u.down)
            PACE[nm]['survivors'] += sum(1 for u in g.sides[side] if u.standing())
            PACE[nm]['models'] += len(g.sides[side])
            PACE[nm]['battles'] += 1
    return (wa + 0.5 * dr) / n


print('=' * 106)
print(f"AUDIT FIX 3 — CAMPAIGN START @ 500, FIXED PYRAMID   "
      f"({N} games/pairing, {len(SCENARIOS)} scenarios, sides swapped)")
print('=' * 106)
for n in names:
    c = CREWS[n](0)
    legal = '' if n in FIX3_LEGAL else '   << ILLEGAL under FIX 3'
    print(f"  {n:<11}{len(c)} models, {sum(u.cost for u in c)} credits{legal}")

t0 = time.time()
per_sc = {}
for sc, (GameCls, kw) in SCENARIOS.items():
    w = {n: {} for n in names}
    for a, b in itertools.combinations(names, 2):
        v = versus(a, b, GameCls, kw, N)
        w[a][b] = v
        w[b][a] = 1 - v
    per_sc[sc] = {n: sum(w[n].values()) / (len(names) - 1) for n in names}

means = {n: sum(per_sc[s][n] for s in SCENARIOS) / len(SCENARIOS) for n in names}
print(f"\n  {'crew':<11}" + ''.join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
for n in names:
    print(f"  {n:<11}" + ''.join(f"{per_sc[s][n] * 100:12.0f} " for s in SCENARIOS)
          + f"{means[n] * 100:7.0f}")

fx = {n: means[n] for n in FIX3_LEGAL}
spread = (max(fx.values()) - min(fx.values())) * 100
worst = max(fx, key=fx.get)
print(f"\n  FIX-3-legal field only: spread {spread:.0f}, best {worst} "
      f"at {fx[worst] * 100:.0f}%, floor {min(fx.values()) * 100:.0f}% "
      f"({min(fx, key=fx.get)})")
print(f"  PASS criterion (no FIX-3-legal archetype > 60%): "
      f"{'PASS' if max(fx.values()) <= 0.60 else 'FAIL'}")
print(f"  OldElite (the closed degenerate) scored {means['OldElite'] * 100:.0f}% "
      f"across the same field")

# --- Level pacing arithmetic (Part D test 2, second criterion) ---------------
print(f"\n{'-' * 106}")
print("  LEVEL PACING — §26.1 triggers per fighter per battle, from sim aggregates")
print(f"  {'crew':<11}{'kills/fighter':>15}{'survive%':>10}{'est trig/battle':>17}{'battles to L3':>15}")
for n in names:
    p = PACE[n]
    if not p['battles']:
        continue
    kpf = p['kills'] / p['models']
    surv = p['survivors'] / p['models']
    # triggers: own kills + surviving + ~0.5 objective-held + ~0.3 Deed (both flat
    # estimates — objectives/Deeds aren't attributed per fighter in the engine)
    trig = kpf + surv + 0.5 + 0.3
    to3 = 3 / trig
    print(f"  {n:<11}{kpf:>15.2f}{surv * 100:>9.0f}%{trig:>17.2f}{to3:>15.1f}")
print("  PASS criterion: a typical fighter reaches ~Level 3 by battle 3 "
      "(battles-to-L3 <= ~3)")
print(f"\n  elapsed {time.time() - t0:.0f}s")
print('=' * 106)

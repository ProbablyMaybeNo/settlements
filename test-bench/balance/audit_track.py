# -*- coding: utf-8 -*-
"""AUDIT FIX 4 (new sim) — stat-gated skill tiers: does the all-in Primary rush
outperform a rounded build at equal Credits?

FIX 4 final shape: Primary derived at creation; Levels 1/4/8 are floating +1s
(any stat, Primary included); Levels 2/5/9 forced Primary; skill slots at 3/6/10
roll on whatever tier the chosen path's stat has unlocked (+2 T1 / +4 T2 / +6 T3).

Three Level-10 careers from the same Fighter body (str2, nrv2, agi1; 75cr + 245
track = 320cr each before weapons):

  RUSH     all floaters into STR -> STR 6 by L5, Tough at the L6 slot, WND 3.
           (L8/L9 overflow past the +6 cap is wasted into NRV — priced but idle.)
  ROUNDED  floaters into AGI -> STR 5 / AGI 4, Fleet (T2 AGI) at the L10 slot,
           WND 2, MOV 8. The audit's layered-build example.
  SPECIAL  a Specialist body (str4) on the same track to L9 (125+190=315cr):
           hits STR 6 at L5 naturally, Tough at L6, WND 3, AGI 3.

WHAT THE ENGINE SEES: stats, WND (Tough folded in) and MOV (Fleet folded in).
Other rolled skills are stubbed — both crews lose them equally. The core FIX 4
trade (capstone durability vs speed+breadth) IS modelled.

PASS (audit playtest flag): RUSH vs ROUNDED mean within 35-65% — the rush is a
legitimate specialist, not a dominant strategy.
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

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300

BUILDS = {
    'bat':     WeaponBuild('Baseball Bat', 'light_melee'),
    'crowbar': WeaponBuild('Crowbar', 'one_handed_melee', ('breaching',)),
    'pistol':  WeaponBuild('Pistol', 'sidearm'),
}
for k, b in BUILDS.items():
    data.WEAPONS[k]['cost'] = weapon_cost(b)
for rank, cost in dict(Recruit=65, Fighter=75, Specialist=125, Leader=170).items():
    data.RANKS[rank]['cost'] = cost

TRACK_COST_L10 = 245
TRACK_COST_L9 = 190


def rush(n, side):
    u = Unit(f'RU{n}', side, 'Fighter', 'crowbar', skills=('tough_T3', 't2_str'),
             str=6, nrv=3, agi=1, wnd=3)
    u.cost += TRACK_COST_L10
    return u


def rounded(n, side):
    u = Unit(f'RO{n}', side, 'Fighter', 'crowbar', skills=('fleet_T2', 't1_str', 't2_str'),
             str=5, agi=4, nrv=2, wnd=2, mov=8.0)
    u.cost += TRACK_COST_L10
    return u


def special(n, side):
    u = Unit(f'SP{n}', side, 'Specialist', 'crowbar', skills=('tough_T3', 't2_str'),
             str=6, agi=3, nrv=2, wnd=3)
    u.cost += TRACK_COST_L9
    return u


def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


def crew_rush(side):
    return _p([rush(i, side) for i in range(4)])


def crew_rounded(side):
    return _p([rounded(i, side) for i in range(4)])


def crew_special(side):
    return _p([special(i, side) for i in range(4)])


CREWS = {'RUSH': crew_rush, 'ROUNDED': crew_rounded, 'SPECIAL': crew_special}
names = list(CREWS)


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {'Hold': (Game, dict()), 'Hold+Claim': (Game, dict(claim=True)),
             'Annihilate': (Annihilate, dict())}


def versus(a, b, GameCls, kw, n, seed=20260807):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = GameCls(CREWS[a](0), CREWS[b](1), board, **kw).play()
            x, y = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(CREWS[b](0), CREWS[a](1), board, **kw).play()
            x, y = r['winner'] == 'B', r['winner'] == 'A'
        wa += x
        wb += y
        dr += (not x and not y)
    return (wa + 0.5 * dr) / n


print('=' * 96)
print(f"AUDIT FIX 4 — RUSH vs ROUNDED vs SPECIALIST at Level 10/9, equal-ish Credits")
print(f"({N} games/pairing/scenario, sides swapped)")
print('=' * 96)
for n in names:
    c = CREWS[n](0)
    u = c[0]
    print(f"  {n:<9}{len(c)}x {u.rank}  str{u.stats['str']} agi{u.stats['agi']} "
          f"nrv{u.stats['nrv']}  WND {u.wnd}  MOV {u.base_mov:.0f}  "
          f"{u.cost}cr each -> {sum(x.cost for x in c)}cr crew")

t0 = time.time()
pair = {}
print(f"\n  {'matchup':<22}" + ''.join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
for a, b in itertools.combinations(names, 2):
    per = {}
    for sc, (GameCls, kw) in SCENARIOS.items():
        per[sc] = versus(a, b, GameCls, kw, N)
    mean = sum(per.values()) / len(per)
    pair[(a, b)] = mean
    print(f"  {a} vs {b:<12}" + ''.join(f"{per[s] * 100:12.0f} " for s in SCENARIOS)
          + f"{mean * 100:7.0f}   ({a}'s win %)")

rr = pair[('RUSH', 'ROUNDED')]
# Per-scenario breakdown for the flagged matchup (re-run to expose skew)
print(f"\n  PASS criterion A: RUSH vs ROUNDED mean within 35-65%  ->  "
      f"{rr * 100:.0f}%  ->  {'PASS' if 0.35 <= rr <= 0.65 else 'FAIL'}")
# Soft flag from Ross verdict / prior run: Annihilate was ~90% for RUSH.
# A mean-pass that hides a single-scenario wipe still fails the spirit of the test.
rush_ann = versus('RUSH', 'ROUNDED', Annihilate, dict(), N, seed=20260807 + 1)
print(f"  PASS criterion B: no single scenario > 75% for RUSH vs ROUNDED  ->  "
      f"Annihilate {rush_ann * 100:.0f}%  ->  "
      f"{'PASS' if rush_ann <= 0.75 else 'FAIL — WND-3 wall dominates kill missions'}")
print(f"  (SPECIAL row answers the audit's literal flag — the +6 Fighter vs a "
      f"rounded Specialist-track career)")
print(f"\n  elapsed {time.time() - t0:.0f}s")
print('=' * 96)

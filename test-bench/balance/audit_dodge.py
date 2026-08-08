# -*- coding: utf-8 -*-
"""AUDIT FIX 5 — is Dodge over-loaded, and does half-MOV fix it? (2.5D engine)

Spec (SETTLEMENTS-FULL-RULES-AUDIT.md, FIX 5): AGI-stacked crew (2x AGI+4 w/ Fleet)
vs the archetype set, four Dodge variants:
    off    no Dodge reaction exists (baseline)
    full   v1 as written  — won dodge repositions up to FULL MOV
    half   FIX 5 proposal — won dodge repositions up to HALF MOV (round down)
    prone  fallback       — won dodge dives prone (heavy cover vs ranged until next activation)

ACCEPTANCE: the Dodge carrier gains <= +8 win-points over its own no-Dodge baseline.

Dodge is a universal Reaction (v1 s3) — every Ready shooter on BOTH sides may use it;
the AI only dodges when the opposed AGI-vs-DEX bet beats eating the plain to-hit roll
(losing the opposed roll is an auto-hit per RAW). Match Play @1000, Match ladder,
armour 60/100. Fleet is modelled as MOV 8; the carrier Specialists are AGI+4 (T2
unlocked, so Fleet is legal at creation under FIX 6's tiers-reached rule).
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
import engine
from engine import Game, Unit
from board import dist, take_a_hold
from policies import BALANCED

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 150
BUDGET = 1000

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
for rank, cost in dict(Recruit=65, Fighter=95, Specialist=165, Leader=245).items():
    data.RANKS[rank]['cost'] = cost


def C(rank, weapon='bat', armour='none'):
    return data.unit_cost(rank, weapon, armour)


class DodgyPolicy:
    """The dodge-fisher: sit on the objective and bank Ready instead of shooting
    whenever an enemy gun threatens — the deliberate play FIX 5 worries about.
    (Ready is what makes Dodge legal, v1 s3; this is the AGI-tank posture.)"""
    name = 'dodgy'

    def _threatened(self, g, u):
        from data import WEAPONS
        for e in g._standing(1 - u.side):
            if e.has_gun() and dist(e.pos, u.pos) <= WEAPONS[e.weapon]['rng'] \
                    and g.sight(e, u):
                return True
        return False

    def act(self, g, u):
        if u.pinned:
            if g.clear_pin(u):
                if self._threatened(g, u):
                    u.ready = True
                else:
                    g.take_action(u)
            return
        eng = g.engaged(u)
        if eng:
            g.fight(u, eng[0])
            return
        if dist(u.pos, u.goal) > 2.5:
            g.move_to(u, u.goal, u.mov)
        if not u.standing():
            return
        if g.try_claim(u):
            return
        if self._threatened(g, u):
            u.ready = True                    # fish for the dodge
        else:
            tgt = g.best_target(u)
            if tgt:
                g.shoot(u, tgt)
            else:
                u.ready = True


DODGY = DodgyPolicy()


def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


def carrier(side):
    """The Dodge carrier: 2x AGI+4 Specialists with Fleet (MOV 8) + rifles,
    played as objective-sitting dodge-tanks (DodgyPolicy)."""
    a1 = Unit('A1', side, 'Specialist', 'rifle', skills=('fleet_T2',),
              agi=4, dex=2, nrv=1, mov=8.0)
    a2 = Unit('A2', side, 'Specialist', 'rifle', skills=('fleet_T2',),
              agi=4, dex=2, nrv=1, mov=8.0)
    a1.policy = DODGY
    a2.policy = DODGY
    a1.dodge_hold = True                     # decline snap-shots; save Ready for the Dodge
    a2.dodge_hold = True
    crew = [Unit('Boss', side, 'Leader', 'rifle', skills=('dead_eye_T3',),
                 dex=4, nrv=3, agi=2), a1, a2]
    spent = C('Leader', 'rifle') + 2 * C('Specialist', 'rifle')
    i = 0
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(Unit(f'R{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1))
        spent += C('Recruit', 'bat')
        i += 1
    for u in crew:
        if u.policy is None:
            u.policy = BALANCED
    return crew


def swarm(side):
    crew = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=3, agi=2)]
    spent = C('Leader', 'sledge')
    i = 0
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(Unit(f'R{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1))
        spent += C('Recruit', 'bat')
        i += 1
    return _p(crew)


def line(side):
    crew = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=3, agi=2)]
    spent = C('Leader', 'sledge')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(Unit(f'F{i}', side, 'Fighter', 'crowbar',
                         skills=('knockback',), str=2, nrv=2, agi=1))
        spent += C('Fighter', 'crowbar')
        i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(Unit(f'R9{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1))
        spent += C('Recruit', 'bat')
        i += 1
    return _p(crew)


def gunline(side):
    crew = [Unit('Boss', side, 'Leader', 'rifle', dex=4, nrv=3, str=2)]
    spent = C('Leader', 'rifle')
    i = 0
    while spent + C('Fighter', 'rifle') <= BUDGET:
        crew.append(Unit(f'F{i}', side, 'Fighter', 'rifle',
                         skills=('ready_to_react',), dex=2, nrv=2, agi=1))
        spent += C('Fighter', 'rifle')
        i += 1
    while spent + C('Recruit', 'pistol') <= BUDGET:
        crew.append(Unit(f'R9{i}', side, 'Recruit', 'pistol', dex=1, agi=1, nrv=1))
        spent += C('Recruit', 'pistol')
        i += 1
    return _p(crew)


def armoured(side):
    crew = [Unit('Boss', side, 'Leader', 'sledge', 'light', str=4, nrv=3, agi=2)]
    spent = C('Leader', 'sledge', 'light')
    i = 0
    while spent + C('Fighter', 'bat', 'light') <= BUDGET:
        crew.append(Unit(f'F{i}', side, 'Fighter', 'bat', 'light',
                         skills=('knockback',), str=2, nrv=2, agi=1))
        spent += C('Fighter', 'bat', 'light')
        i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(Unit(f'R9{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1))
        spent += C('Recruit', 'bat')
        i += 1
    return _p(crew)


def mixed(side):
    crew = [Unit('Boss', side, 'Leader', 'rifle', dex=4, nrv=3, str=2),
            Unit('S0', side, 'Specialist', 'rifle',
                 skills=('pin_them_down_T2',), dex=4, nrv=2, int=1)]
    spent = C('Leader', 'rifle') + C('Specialist', 'rifle')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(Unit(f'F{i}', side, 'Fighter', 'crowbar',
                         skills=('knockback',), str=2, nrv=2, agi=1))
        spent += C('Fighter', 'crowbar')
        i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(Unit(f'R9{i}', side, 'Recruit', 'bat', str=1, agi=1, nrv=1))
        spent += C('Recruit', 'bat')
        i += 1
    return _p(crew)


OPPONENTS = {'Swarm': swarm, 'Line': line, 'Gunline': gunline,
             'Armoured': armoured, 'Mixed': mixed}


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {'Hold': (Game, dict()), 'Hold+Claim': (Game, dict(claim=True)),
             'Annihilate': (Annihilate, dict())}

VARIANTS = ['off', 'full', 'half', 'prone']


def set_variant(v):
    engine.DODGE_ON = (v != 'off')
    engine.DODGE_MOVE = v if v != 'off' else 'full'


def run_variant(v):
    set_variant(v)
    random.seed(20260807)
    per_opp = {}
    tries = saves = 0
    for oname, ofn in OPPONENTS.items():
        w = d = tot = 0
        for GameCls, kw in SCENARIOS.values():
            for i in range(N):
                board = take_a_hold()
                if i % 2 == 0:
                    g = GameCls(carrier(0), ofn(1), board, **kw)
                    r = g.play()
                    win, loss = r['winner'] == 'A', r['winner'] == 'B'
                else:
                    g = GameCls(ofn(0), carrier(1), board, **kw)
                    r = g.play()
                    win, loss = r['winner'] == 'B', r['winner'] == 'A'
                w += win
                d += (not win and not loss)
                tot += 1
                tries += g.stat['dodge_try']
                saves += g.stat['dodge_save']
        per_opp[oname] = (w + 0.5 * d) / tot
    mean = sum(per_opp.values()) / len(per_opp)
    return per_opp, mean, tries, saves


print('=' * 100)
print(f"AUDIT FIX 5 — DODGE VARIANTS   carrier = Leader + 2x AGI+4 Fleet Specialist + Recruits @1000")
print(f"({N} games/pairing/scenario x {len(SCENARIOS)} scenarios x {len(OPPONENTS)} opponents, sides swapped)")
print('=' * 100)
c = carrier(0)
print(f"  carrier: {len(c)} models, {sum(u.cost for u in c)} credits "
      f"(Fleet = MOV 8 on the two AGI Specialists)")

t0 = time.time()
base_mean = None
print(f"\n  {'variant':<10}" + ''.join(f"{n:>10}" for n in OPPONENTS)
      + f"{'MEAN':>8}{'delta':>8}{'dodges (won/tried)':>22}")
results = {}
for v in VARIANTS:
    per_opp, mean, tries, saves = run_variant(v)
    if base_mean is None:
        base_mean = mean
    delta = (mean - base_mean) * 100
    results[v] = delta
    print(f"  {v:<10}" + ''.join(f"{per_opp[n] * 100:9.0f} " for n in OPPONENTS)
          + f"{mean * 100:7.0f} {delta:+7.1f}"
          + f"{saves:>12,}/{tries:<9,}")

print(f"\n  ACCEPTANCE: carrier delta <= +8 win-points over 'off' baseline")
for v in ('full', 'half', 'prone'):
    verdict = 'PASS' if results[v] <= 8.0 else 'FAIL'
    print(f"    {v:<7} {results[v]:+5.1f}  ->  {verdict}")
print(f"\n  elapsed {time.time() - t0:.0f}s")
print('=' * 100)

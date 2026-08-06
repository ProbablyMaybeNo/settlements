# -*- coding: utf-8 -*-
"""DOES GROWING A CREW AT 500 ACTUALLY FEEL LIKE GROWING? (2.5D engine)

The 500 cap exists for a design reason, stated directly: a player should start
with something small and watch it become something real. Every sim so far has
tested 500 as a PERMANENT format and asked "is it balanced?". That is not what
FULL-RULES-SYSTEM-V1 §16 describes. §16 says a Campaign Start crew "Begins at
500 Crew Rating, GROWING over the campaign (§25.5, §29)" — but no rule anywhere
defines the growth, and §25.5, the only place that sets a cap at battle time,
lists just "standard 1000, raid 750, pitched 1500". The ramp is promised and
never written, so it has never been tested.

This harness tests the arc instead of the snapshot, in three parts:

  A · ARITHMETIC — the shrink. Levels cost Credits (§26.1: 15/stat point,
      20/35/55 per skill tier, 45 for the Level-7 wound; +245 for a full track).
      At a FIXED cap, every Level a fighter gains buys the crew one fewer body.
      This is pure arithmetic and needs no dice: it prints crew size vs Level.

  B · SIMULATION — is the late-campaign game still a game? Both crews levelled
      to the same rung at a fixed 500 cap. If a 500 campaign converges on
      two-model crews, the format dies of attrition rather than imbalance.

  C · THE RAMP — the cap that holds a crew's SIZE constant as it levels. This is
      the number §16 owes and does not have. Derived from the Level track's own
      Credit costs, then checked in the engine for spread at each rung.

WHAT IT CANNOT SEE: the engine implements only Tier-1 skills, so the skills
bought at Levels 3/6/10 cost Credits here but deliver no ability. Levelled crews
are therefore measured with their FULL price and PART of their power — every
veteran result below is a LOWER BOUND on how strong a levelled crew really is.
Stat bumps and the Level-7 wound do resolve mechanically.
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

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
MODE = sys.argv[2] if len(sys.argv) > 2 else 'all'

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
    data.ARMOUR[k]['cost'] = v          # the adopted price, not ticks.py's 30/60
for rank, cost in dict(Recruit=65, Fighter=75, Specialist=125, Leader=170).items():
    data.RANKS[rank]['cost'] = cost

# §26.1 — what each Level grants and what it costs.
LEVEL_TRACK = [
    ('sec', 15), ('pri', 15), ('skill', 20), ('sec', 15), ('pri', 15),
    ('skill', 35), ('wnd', 45), ('sec', 15), ('pri', 15), ('skill', 55),
]
CUM = []
_t = 0
for _g, _c in LEVEL_TRACK:
    _t += _c
    CUM.append(_t)                      # CUM[k-1] = cost of reaching Level k


def level_cost(k):
    return 0 if k <= 0 else CUM[min(k, 10) - 1]


def levelled_stats(base, primary, secondary, k):
    """Apply k Levels to a stat line. Stats cap at +6 (§13); the L7 wound applies."""
    st = dict(base)
    wnd = 1
    for i in range(min(k, 10)):
        grant = LEVEL_TRACK[i][0]
        if grant == 'pri':
            st[primary] = min(6, st.get(primary, 0) + 1)
        elif grant == 'sec':
            st[secondary] = min(6, st.get(secondary, 0) + 1)
        elif grant == 'wnd':
            wnd = 2
    st['wnd'] = wnd
    return st


# --------------------------------------------------------------------------
# UNITS — same stat lines as campaign500_fixes.py, plus a Level parameter.
# --------------------------------------------------------------------------
def mk(name, side, rank, weapon, armour, base, primary, secondary, skills, k):
    st = levelled_stats(base, primary, secondary, k)
    u = Unit(name, side, rank, weapon, armour, skills=skills, **st)
    u.cost += level_cost(k)             # a Level's Credits ride on the fighter
    u.level = k
    return u


def recruit(n, side, k=0, weapon='bat', armour='none', melee=True):
    base = dict(str=1, agi=1, nrv=1) if melee else dict(dex=1, agi=1, nrv=1)
    return mk(f'R{n}', side, 'Recruit', weapon, armour, base,
              'str' if melee else 'dex', 'nrv', (), k)


def fighter(n, side, k=0, weapon='bat', armour='none', melee=True):
    base = dict(str=2, nrv=2, agi=1) if melee else dict(dex=2, nrv=2, agi=1)
    sk = ('knockback',) if melee else ('ready_to_react',)
    return mk(f'F{n}', side, 'Fighter', weapon, armour, base,
              'str' if melee else 'dex', 'nrv', sk, k)


def leader(side, k=0, weapon='rifle', armour='none', melee=False):
    base = dict(str=4, nrv=3, agi=2) if melee else dict(dex=4, nrv=3, str=2)
    sk = ('the_muscle_T3',) if melee else ('dead_eye_T3',)
    return mk('Boss', side, 'Leader', weapon, armour, base,
              'str' if melee else 'dex', 'nrv', sk, k)


def ucost(rank, weapon, armour, k):
    return data.unit_cost(rank, weapon, armour) + level_cost(k)


def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


# --------------------------------------------------------------------------
# CREWS — one Leader, then fill with the archetype's body, every model at the
# same Level k, greedily rebuilt to `cap`.
# --------------------------------------------------------------------------
def build(kind, side, k, cap):
    if kind == 'Line':
        crew = [leader(side, k, 'sledge', melee=True)]
        spent = ucost('Leader', 'sledge', 'none', k)
        body = ('Fighter', 'crowbar', 'none', True)
    elif kind == 'Swarm':
        crew = [leader(side, k, 'sledge', melee=True)]
        spent = ucost('Leader', 'sledge', 'none', k)
        body = ('Recruit', 'bat', 'none', True)
    elif kind == 'Gunline':
        crew = [leader(side, k, 'rifle')]
        spent = ucost('Leader', 'rifle', 'none', k)
        body = ('Fighter', 'rifle', 'none', False)
    elif kind == 'Armoured':
        crew = [leader(side, k, 'sledge', 'light', melee=True)]
        spent = ucost('Leader', 'sledge', 'light', k)
        body = ('Fighter', 'bat', 'light', True)
    else:
        raise ValueError(kind)

    rank, weapon, armour, melee = body
    i = 0
    while spent + ucost(rank, weapon, armour, k) <= cap:
        f = fighter(i, side, k, weapon, armour, melee) if rank == 'Fighter' \
            else recruit(i, side, k, weapon, armour, melee)
        crew.append(f)
        spent += ucost(rank, weapon, armour, k)
        i += 1
    # tail-fill with the cheapest legal body so no budget is left unspent
    j = 90
    while spent + ucost('Recruit', 'bat', 'none', k) <= cap:
        crew.append(recruit(j, side, k, melee=melee))
        spent += ucost('Recruit', 'bat', 'none', k)
        j += 1
    return _p(crew)


KINDS = ['Line', 'Swarm', 'Gunline', 'Armoured']


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {'Hold': (Game, dict()), 'Hold+Claim': (Game, dict(claim=True)),
             'Annihilate': (Annihilate, dict())}


def versus(fa, fb, n, seed=20260806):
    random.seed(seed)
    wa = wb = dr = 0
    per = max(1, n // len(SCENARIOS))
    for GameCls, kw in SCENARIOS.values():
        for i in range(per):
            board = take_a_hold()
            if i % 2 == 0:
                r = GameCls(fa(0), fb(1), board, **kw).play()
                x, y = r['winner'] == 'A', r['winner'] == 'B'
            else:
                r = GameCls(fb(0), fa(1), board, **kw).play()
                x, y = r['winner'] == 'B', r['winner'] == 'A'
            wa += x; wb += y; dr += (not x and not y)
    tot = per * len(SCENARIOS)
    return (wa + 0.5 * dr) / tot


def spread_at(k, cap):
    """Mean win % per archetype when BOTH crews are at Level k and cap."""
    w = {n: {} for n in KINDS}
    for a, b in itertools.combinations(KINDS, 2):
        v = versus(lambda s, a=a: build(a, s, k, cap), lambda s, b=b: build(b, s, k, cap), N)
        w[a][b] = v
        w[b][a] = 1 - v
    means = {n: sum(w[n].values()) / (len(KINDS) - 1) for n in KINDS}
    return means, (max(means.values()) - min(means.values())) * 100


print("=" * 104)
print(f"THE GROWTH ARC AT 500 — is the campaign a ramp or a squeeze?  ({N} games/pairing, 2.5D)")
print("=" * 104)
print("  Level track costs (§26.1), cumulative:")
print("    " + "  ".join(f"L{i+1} +{CUM[i]}" for i in range(10)))

t0 = time.time()

if MODE in ('all', 'A'):
    print(f"\n{'=' * 104}")
    print("A · THE SHRINK — crew size vs Level at a FIXED cap (arithmetic, no dice)")
    print("=" * 104)
    for cap in (500, 1000):
        print(f"\n  cap {cap}:")
        print(f"    {'archetype':<11}" + "".join(f"{'L' + str(k):>6}" for k in range(0, 11, 1)))
        for kind in KINDS:
            row = [len(build(kind, 0, k, cap)) for k in range(0, 11)]
            print(f"    {kind:<11}" + "".join(f"{v:6d}" for v in row))
        print(f"    {'(min legal crew is 3 models)':<11}")

if MODE in ('all', 'B'):
    print(f"\n{'=' * 104}")
    print("B · IS THE LATE-CAMPAIGN GAME STILL A GAME? — both crews at Level k, cap 500")
    print("=" * 104)
    print(f"  {'Level':<8}" + "".join(f"{n[:8]:>10}" for n in KINDS)
          + f"{'SPREAD':>9}{'sizes':>16}")
    for k in (0, 2, 5, 7, 10):
        means, sp = spread_at(k, 500)
        sizes = "/".join(str(len(build(n, 0, k, 500))) for n in KINDS)
        print(f"  L{k:<7}" + "".join(f"{means[n] * 100:9.0f} " for n in KINDS)
              + f"{sp:8.0f}{sizes:>16}")

if MODE in ('all', 'C'):
    print(f"\n{'=' * 104}")
    print("C · THE RAMP — the cap that keeps a crew the SAME SIZE as it levels")
    print("=" * 104)
    print("  For each Level, the smallest cap (rounded up to 25) at which each archetype")
    print("  fields as many models as it did at Level 0 on a 500 cap.")
    base_sizes = {n: len(build(n, 0, 0, 500)) for n in KINDS}
    print(f"\n  Level-0 sizes at 500: " + "  ".join(f"{n} {base_sizes[n]}" for n in KINDS))
    print(f"\n  {'Level':<8}" + "".join(f"{n[:9]:>11}" for n in KINDS) + f"{'MAX':>8}")
    ramp = {}
    for k in range(0, 11):
        need = {}
        for kind in KINDS:
            cap = 500
            while cap <= 3000 and len(build(kind, 0, k, cap)) < base_sizes[kind]:
                cap += 25
            need[kind] = cap
        ramp[k] = max(need.values())
        print(f"  L{k:<7}" + "".join(f"{need[n]:11d}" for n in KINDS) + f"{ramp[k]:8d}")
    print("\n  >>> a cap that rides this curve keeps the crew whole while it grows;")
    print("      a cap frozen at 500 makes every Level cost you a body.")

    print(f"\n  spread at each proposed rung (both crews at that Level):")
    print(f"  {'Level':<8}{'cap':>7}" + "".join(f"{n[:8]:>10}" for n in KINDS) + f"{'SPREAD':>9}")
    for k in (0, 2, 5, 7, 10):
        cap = min(1500, ramp[k])
        means, sp = spread_at(k, cap)
        print(f"  L{k:<7}{cap:>7}" + "".join(f"{means[n] * 100:9.0f} " for n in KINDS)
              + f"{sp:8.0f}")

print(f"\n  elapsed {time.time() - t0:.0f}s")
print("=" * 104)

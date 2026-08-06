# -*- coding: utf-8 -*-
"""CAMPAIGN START — 500 Crew Rating rank-ladder sweep (2.5D engine)

Validates the Campaign Start ladder proposed in FULL-RULES-SYSTEM-V1 §16, which
the document itself flags as "first-draft, backed out from the skill Credit
values, not a validated number":

    Recruit 65 · Fighter 75 · Specialist 125 · Leader 170     @ 500 CR

Rules being tested (FULL-RULES-SYSTEM-V1 §13 / §16 Campaign Start column):
  * stat points 3 / 5 / 7 / 9,  Orders 0 / 0 / 1 / 2
  * exactly ONE starting skill per rank: none / T1 / T2 / T3
  * composition: exactly one Leader, minimum three models, NO ratio requirement
    (the Match Play pyramid is deliberately dropped for a green crew)

WHY THIS FILE EXISTS. `engine2d/data.py` hand-sets its own 100-scale prices, so
the simulator has never priced a crew with the costing engine. Everything here
takes weapon/armour/equipment prices from `points/` so one table drives both.

WHAT THE SIM CAN AND CANNOT SEE. It prices BODIES — stat points, Orders and
model count all resolve mechanically. It CANNOT price the starting skill: only
four skills are implemented in the engine (knockback, stare_down, keep_moving,
hacker) and all four are Tier 1, so a Specialist's T2 and a Leader's T3 do
nothing here. Every ladder below is therefore a measurement of the BODY, and the
skill premium has to be added on top analytically. Read the spread, not the
absolute prices.
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
from points.ticks import ARMOUR_CREDITS, EQUIPMENT_CREDITS, HACK_GEAR_CREDITS
from points.weapons import WeaponBuild, weapon_cost

from engine import Game, Unit
from board import take_a_hold, dist
from policies import BALANCED

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
MODE = sys.argv[2] if len(sys.argv) > 2 else 'ladder'   # 'ladder' | 'budget'
BUDGET = 500

# --------------------------------------------------------------------------
# ONE PRICE AUTHORITY — the engine's weapons, costed by points/ instead of by
# the hand-set 100-scale numbers in data.py. Builds match what the engine
# actually implements for each weapon, not what the sample armoury calls it.
# --------------------------------------------------------------------------
BUILDS = {
    'fists':   WeaponBuild('Fists', 'unarmed'),
    'bat':     WeaponBuild('Baseball Bat', 'light_melee'),
    'crowbar': WeaponBuild('Crowbar', 'one_handed_melee', ('breaching',)),
    'sledge':  WeaponBuild('Sledgehammer', 'heavy_melee'),
    'pistol':  WeaponBuild('Pistol', 'sidearm'),
    'rifle':   WeaponBuild('Rifle', 'standard_ranged'),
    'molotov': WeaponBuild('Molotov', 'thrown', ('incendiary', 'blast'), ('single_use',)),
}

for key, build in BUILDS.items():
    data.WEAPONS[key]['cost'] = weapon_cost(build)

data.ARMOUR['none']['cost'] = ARMOUR_CREDITS['none']
data.ARMOUR['light']['cost'] = ARMOUR_CREDITS['light']
data.ARMOUR['heavy']['cost'] = ARMOUR_CREDITS['heavy']

data.EQUIPMENT['breach_kit']['cost'] = HACK_GEAR_CREDITS['breach_kit']
data.EQUIPMENT['exploit_suite']['cost'] = HACK_GEAR_CREDITS['exploit_suite']
data.EQUIPMENT['med_kit']['cost'] = EQUIPMENT_CREDITS['med_kit']

# Deployables have no entry in the costing engine at all. The old 100-scale
# numbers x10 is the same anchor the master doc uses for its turret table, and
# it is flagged there as unmeasured. No turret crew is run below because of it.

# --------------------------------------------------------------------------
# THE LADDERS UNDER TEST
# --------------------------------------------------------------------------
LADDERS = {
    # the master doc's proposal: Match Play prices minus the skills removed
    'doc':       dict(Recruit=65, Fighter=75,  Specialist=125, Leader=170),
    # Match Play prices unchanged - what D22/D27 imply (a skill carries no cost
    # of its own, so removing skills should not refund anything)
    'matchplay': dict(Recruit=65, Fighter=95,  Specialist=165, Leader=245),
    # the body formula with the starting skill actually charged into the bundle
    'charged':   dict(Recruit=65, Fighter=115, Specialist=200, Leader=300),
    # --- body-scale sweep on the Match Play SHAPE. Gear prices are measured and
    # fixed, so scaling only the bodies is the one lever that restores crew size
    # at half the budget. x0.5 is the scale at which a 500 CR crew has the same
    # body:gear ratio the 1000 CR game was balanced at.
    'x0.75':     dict(Recruit=49, Fighter=71,  Specialist=124, Leader=184),
    'x0.5':      dict(Recruit=33, Fighter=48,  Specialist=83,  Leader=123),
    'x0.35':     dict(Recruit=23, Fighter=33,  Specialist=58,  Leader=86),
}

# --------------------------------------------------------------------------
# STAT LINES — legal under the §13 tier caps (Recruit no tiered stat, Fighter
# 2xT1, Specialist 1xT2 + 2xT1, Leader 1xT3 + 2xT2 + 4xT1) and shaped GENTLE
# (a strong primary plus one real secondary), which engine2d/run.py measured as
# beating both forced-spread and stacked allocations.
#
# SKILLS: one per rank at the rank's tier. Only Tier 1 skills exist in the
# engine, so Specialist/Leader entries are named for the record and do nothing.
# --------------------------------------------------------------------------
def recruit(n, side, weapon='bat', armour='none', melee=True):
    st = dict(str=1, agi=1, nrv=1) if melee else dict(dex=1, agi=1, nrv=1)
    return Unit(f'R{n}', side, 'Recruit', weapon, armour, **st)


def fighter(n, side, weapon='bat', armour='none', melee=True):
    if melee:
        return Unit(f'F{n}', side, 'Fighter', weapon, armour,
                    skills=('knockback',), str=2, nrv=2, agi=1)
    return Unit(f'F{n}', side, 'Fighter', weapon, armour,
                skills=('ready_to_react',), dex=2, nrv=2, agi=1)


def specialist(n, side, weapon='rifle', armour='none', melee=False):
    if melee:
        return Unit(f'S{n}', side, 'Specialist', weapon, armour,
                    skills=('super_slam_T2',), str=4, nrv=2, agi=1)
    return Unit(f'S{n}', side, 'Specialist', weapon, armour,
                skills=('pin_them_down_T2',), dex=4, nrv=2, int=1)


def leader(side, weapon='rifle', armour='none', melee=False):
    if melee:
        return Unit('Boss', side, 'Leader', weapon, armour,
                    skills=('the_muscle_T3',), str=4, nrv=3, agi=2)
    return Unit('Boss', side, 'Leader', weapon, armour,
                skills=('dead_eye_T3',), dex=4, nrv=3, str=2)


def C(rank, weapon='bat', armour='none', equip=()):
    return data.unit_cost(rank, weapon, armour, equip)


def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


def _fill(crew, side, spent, melee=True):
    """Spend the tail of the budget on bodies with the free Light Melee weapon,
    so no archetype is judged on a list that left a buyable model unbought."""
    i = 90
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side, melee=melee))
        spent += C('Recruit', 'bat')
        i += 1
    return crew


# --------------------------------------------------------------------------
# CREWS — each fills to 500 at whatever the current ladder prices are. Only
# rule enforced: exactly one Leader, minimum three models.
# --------------------------------------------------------------------------
def swarm(side):
    """Leader + as many Recruits as fit. The list the loosened pyramid unlocks."""
    crew = [leader(side, 'sledge', melee=True)]
    spent = C('Leader', 'sledge')
    i = 0
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side)); spent += C('Recruit', 'bat'); i += 1
    return _p(crew)


def line(side):
    """Leader + Fighters, melee. The middle of the ladder."""
    crew = [leader(side, 'sledge', melee=True)]
    spent = C('Leader', 'sledge')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(fighter(i, side, 'crowbar')); spent += C('Fighter', 'crowbar'); i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side)); spent += C('Recruit', 'bat'); i += 1
    return _p(crew)


def elite(side):
    """Leader + Specialists with rifles. The other list the loosened pyramid
    unlocks - under the Match Play pyramid each Specialist needed two lower
    ranks beneath it, so this crew was illegal."""
    crew = [leader(side, 'rifle', 'light')]
    spent = C('Leader', 'rifle', 'light')
    i = 0
    while spent + C('Specialist', 'rifle', 'light') <= BUDGET:
        crew.append(specialist(i, side, 'rifle', 'light')); spent += C('Specialist', 'rifle', 'light'); i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side)); spent += C('Recruit', 'bat'); i += 1
    return _p(crew)


def gunline(side):
    """Leader + rifle Fighters, then pistols, then bodies."""
    crew = [leader(side, 'rifle')]
    spent = C('Leader', 'rifle')
    i = 0
    while spent + C('Fighter', 'rifle') <= BUDGET:
        crew.append(fighter(i, side, 'rifle', melee=False)); spent += C('Fighter', 'rifle'); i += 1
    while spent + C('Fighter', 'pistol') <= BUDGET:
        crew.append(fighter(i, side, 'pistol', melee=False)); spent += C('Fighter', 'pistol'); i += 1
    while spent + C('Recruit', 'pistol') <= BUDGET:
        crew.append(recruit(i, side, 'pistol', melee=False)); spent += C('Recruit', 'pistol'); i += 1
    return _p(_fill(crew, side, spent, melee=False))


def armoured(side):
    """Everyone in light plate, melee. Tests whether armour is affordable at 500."""
    crew = [leader(side, 'sledge', 'light', melee=True)]
    spent = C('Leader', 'sledge', 'light')
    i = 0
    while spent + C('Fighter', 'bat', 'light') <= BUDGET:
        crew.append(fighter(i, side, 'bat', 'light')); spent += C('Fighter', 'bat', 'light'); i += 1
    while spent + C('Recruit', 'bat', 'light') <= BUDGET:
        crew.append(recruit(i, side, 'bat', 'light')); spent += C('Recruit', 'bat', 'light'); i += 1
    return _p(_fill(crew, side, spent))


def mixed(side):
    """The shape the rules text imagines: Leader, a Specialist, Fighters, filler.
    The Specialist is only bought if it leaves room for two more bodies, so this
    crew degrades to a Leader-plus-filler list instead of blowing the budget."""
    crew = [leader(side, 'rifle')]
    spent = C('Leader', 'rifle')
    if spent + C('Specialist', 'rifle') + 2 * C('Recruit', 'bat') <= BUDGET:
        crew.append(specialist(0, side, 'rifle'))
        spent += C('Specialist', 'rifle')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(fighter(i, side, 'crowbar')); spent += C('Fighter', 'crowbar'); i += 1
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side)); spent += C('Recruit', 'bat'); i += 1
    return _p(crew)


CREWS = {'Swarm': swarm, 'Line': line, 'Elite': elite,
         'Gunline': gunline, 'Armoured': armoured, 'Mixed': mixed}


# --------------------------------------------------------------------------
# SCENARIOS
# --------------------------------------------------------------------------
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


SCENARIOS = {
    'Hold':         (Game, dict()),
    'Hold+Claim':   (Game, dict(claim=True)),
    'Annihilate':   (Annihilate, dict()),
    'Breakthrough': (Breakthrough, dict()),
}


def versus(a, b, GameCls, kw, n, seed=20260805):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = GameCls(a(0), b(1), board, **kw).play()
            x, y = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(b(0), a(1), board, **kw).play()
            x, y = r['winner'] == 'B', r['winner'] == 'A'
        wa += x; wb += y; dr += (not x and not y)
    return (wa + 0.5 * dr) / n


def measure(label, header):
    """Run every pairing across every scenario at the current prices/budget."""
    sizes, spends = {}, {}
    for n in names:
        c = CREWS[n](0)
        sizes[n] = len(c)
        spends[n] = sum(u.cost for u in c)
    print(f"\n{'=' * 108}")
    print(f"[{label}]  {header}")
    print("  crews: " + "  ".join(f"{n} {sizes[n]}mdl/{spends[n]}cr" for n in names))
    illegal = [n for n in names if sizes[n] < 3]
    if illegal:
        print(f"  !! below the 3-model minimum: {', '.join(illegal)}")
    over = [n for n in names if spends[n] > BUDGET]
    if over:
        print(f"  !! OVER BUDGET: {', '.join(over)}")

    per_sc = {}
    for sc, (GameCls, kw) in SCENARIOS.items():
        w = {n: {} for n in names}
        for a, b in itertools.combinations(names, 2):
            v = versus(CREWS[a], CREWS[b], GameCls, kw, N)
            w[a][b] = v
            w[b][a] = 1 - v
        per_sc[sc] = {n: sum(w[n].values()) / (len(names) - 1) for n in names}

    means = {n: sum(per_sc[s][n] for s in SCENARIOS) / len(SCENARIOS) for n in names}
    spread = (max(means.values()) - min(means.values())) * 100
    print(f"  {'crew':<10}" + "".join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
    for n in names:
        print(f"  {n:<10}" + "".join(f"{per_sc[s][n] * 100:12.0f} " for s in SCENARIOS)
              + f"{means[n] * 100:7.0f}")
    print(f"  >>> SPREAD {spread:.0f} points   "
          f"(best {max(means, key=means.get)}, worst {min(means, key=means.get)})")
    return means, spread, sizes


names = list(CREWS)
print("=" * 108)
print(f"CAMPAIGN START — 500 CR SWEEP [{MODE}]   ({N} games/pairing, sides swapped, 2.5D engine)")
print("=" * 108)
print("\n  prices from points/ (one authority):")
print("    " + "  ".join(f"{k} {data.WEAPONS[k]['cost']}" for k in BUILDS))
print("    light armour " + str(data.ARMOUR['light']['cost'])
      + " · heavy " + str(data.ARMOUR['heavy']['cost']))

t0 = time.time()
results = {}

if MODE == 'budget':
    # Is 500 the problem, or is the ladder? Hold the doc's Campaign Start ladder
    # fixed and move only the cap. If the spread collapses as the cap rises, the
    # budget is the binding constraint and no ladder can fix it.
    for rank, cost in LADDERS['doc'].items():
        data.RANKS[rank]['cost'] = cost
    for cap in (500, 625, 750, 875, 1000, 1250):
        BUDGET = cap
        results[f'{cap}cr'] = measure(f'{cap} CR', "doc ladder R65/F75/S125/L170")
    axis = 'cap'
elif MODE == 'armour':
    # The Armoured list wins at every cap tested. Armour has two live prices -
    # 30/60 in points/ticks.py [measured, source file missing] and 60/100 in
    # FULL-RULES-SYSTEM-V1 §15. Hold everything else fixed and swap only these.
    for rank, cost in LADDERS['doc'].items():
        data.RANKS[rank]['cost'] = cost
    for tag, (lt, hv) in {'engine 30/60': (30, 60), 'doc 60/100': (60, 100)}.items():
        data.ARMOUR['light']['cost'] = lt
        data.ARMOUR['heavy']['cost'] = hv
        results[tag] = measure(tag, f"doc ladder @ 500 CR, light {lt} / heavy {hv}")
    axis = 'armour'
elif MODE == 'catalogue':
    # The sweep the ladder run did NOT do: scale BODIES AND GEAR TOGETHER at a
    # fixed 500 cap. The ladder sweep moved body prices only, so a rifle stayed
    # at 100 - 20% of a 500 crew against 10% of a 1000 one - and gear, not the
    # rank ladder, became the binding constraint.
    #
    # Base = Match Play bodies (the validated shape) + the points/ gear prices,
    # everything multiplied by k and rounded to the nearest 5 so the result is a
    # price list a player could actually read off a card.
    BASE_BODY = dict(Recruit=65, Fighter=95, Specialist=165, Leader=245)
    BASE_WEAP = {k: data.WEAPONS[k]['cost'] for k in BUILDS}
    BASE_ARM = {k: data.ARMOUR[k]['cost'] for k in ('none', 'light', 'heavy')}
    BASE_EQ = {k: data.EQUIPMENT[k]['cost'] for k in data.EQUIPMENT}

    def r5(v):
        return int(round(v / 5.0) * 5)

    for k in (1.0, 0.8, 0.67, 0.5, 0.4):
        for rank, c in BASE_BODY.items():
            data.RANKS[rank]['cost'] = r5(c * k)
        for w, c in BASE_WEAP.items():
            data.WEAPONS[w]['cost'] = r5(c * k)
        for a, c in BASE_ARM.items():
            data.ARMOUR[a]['cost'] = r5(c * k)
        for e, c in BASE_EQ.items():
            data.EQUIPMENT[e]['cost'] = r5(c * k)
        lead_rifle = data.RANKS['Leader']['cost'] + data.WEAPONS['rifle']['cost']
        head = (f"x{k}  R{data.RANKS['Recruit']['cost']}"
                f"/F{data.RANKS['Fighter']['cost']}"
                f"/S{data.RANKS['Specialist']['cost']}"
                f"/L{data.RANKS['Leader']['cost']}"
                f"  rifle {data.WEAPONS['rifle']['cost']}"
                f" · pistol {data.WEAPONS['pistol']['cost']}"
                f" · light armour {data.ARMOUR['light']['cost']}"
                f"  >> Leader+rifle = {lead_rifle} ({lead_rifle * 100 // BUDGET}% of the crew)")
        results[f'x{k}'] = measure(f'x{k}', head)
    axis = 'scale'
elif MODE == 'rifle':
    # What is a rifle actually worth? CLASS_CREDITS is marked "legacy x10" in
    # ticks.py - inherited from the old 10-point Standard Ranged, never measured,
    # unlike the characteristics bolted onto it. Sweep the class price at a fixed
    # 500 cap on the doc ladder and find where the shooting list reaches parity.
    # The sidearm is scaled with it (same class family, same legacy provenance)
    # so a gunline's fallback weapon does not stay stranded at the old ratio.
    for rank, cost in LADDERS['doc'].items():
        data.RANKS[rank]['cost'] = cost
    for rifle in (100, 85, 70, 55, 40):
        data.WEAPONS['rifle']['cost'] = rifle
        data.WEAPONS['pistol']['cost'] = int(round(rifle * 0.4 / 5) * 5)
        head = (f"rifle {rifle} · pistol {data.WEAPONS['pistol']['cost']}"
                f"  >> Leader+rifle = {170 + rifle}"
                f" ({(170 + rifle) * 100 // BUDGET}% of the crew)"
                f" · rifle = {rifle * 100 // 170}% of a Leader body")
        results[f'rifle{rifle}'] = measure(f'rifle {rifle}', head)
    axis = 'rifle'
elif MODE == 'damage':
    # Decouple the chassis from the damage. CLASS_CREDITS bundles +3 Damage into
    # Standard Ranged's 100, and prices each melee damage step at 40 (0/40/80 for
    # +1/+2/+3) against the MEASURED atom of 15. So what is the 18" chassis worth
    # on its own? Drop the rifle to +1 Damage - the same damage as a free bat,
    # but at 18" - and sweep its price to find parity. Whatever it settles at IS
    # the range premium, with damage removed from the question.
    for rank, cost in LADDERS['doc'].items():
        data.RANKS[rank]['cost'] = cost
    base_dmg = data.WEAPONS['rifle']['dmg']
    for dmg, price in ((1, 35), (1, 50), (1, 65), (1, 80), (3, 80)):
        data.WEAPONS['rifle']['dmg'] = dmg
        data.WEAPONS['rifle']['cost'] = price
        data.WEAPONS['pistol']['cost'] = 40 if dmg == 3 else 25
        head = (f"rifle = +{dmg} Damage @ 18\" for {price} Credits"
                f"   (chassis {price - 15 * (dmg - 1)} + {15 * (dmg - 1)} damage"
                f" at the measured 15/step)")
        results[f'+{dmg}dmg@{price}'] = measure(f'+{dmg}dmg @{price}', head)
    data.WEAPONS['rifle']['dmg'] = base_dmg
    axis = 'rifle build'
elif MODE == 'rebuild':
    # THE REBUILD TEST - the method balance/rof_cost.py used to price Rate of
    # Fire 2, and the only one that survives a weak archetype. Two identical
    # crews. One carries a +1 Damage rifle at a fixed 35; the other carries a
    # +3 Damage rifle at price P and PAYS for it by fielding fewer bodies.
    # Sweep P. The price at which the upgraded crew falls back to 50% is what
    # +2 Damage on a rifle is worth. No archetype opinion involved: the two
    # lists are the same list.
    for rank, cost in LADDERS['doc'].items():
        data.RANKS[rank]['cost'] = cost
    BASE_PRICE, BASE_DMG = 35, 1

    # Separate weapon KEYS, not a mutated shared entry. engine.py resolves
    # WEAPONS[u.weapon]['dmg'] at fire time, so two crews sharing one key would
    # both shoot whichever profile was written last - the two lists would differ
    # in price and be identical in damage.
    def make(dmg, price, key):
        data.WEAPONS[key] = dict(rng=18, dmg=dmg, kind='ranged', cost=price,
                                 traits=('loud', 'two_handed'))

        def build(side):
            crew = [leader(side, key)]
            spent = C('Leader', key)
            i = 0
            while spent + C('Fighter', key) <= BUDGET and i < 2:
                crew.append(fighter(i, side, key, melee=False))
                spent += C('Fighter', key); i += 1
            return _p(_fill(crew, side, spent, melee=False))
        return build

    print(f"\n  baseline = +{BASE_DMG} Damage rifle at {BASE_PRICE} Credits, "
          f"rebuilt to {BUDGET} CR. The upgraded crew buys +2 Damage and pays in bodies.")
    print(f"\n  {'+3 dmg price':<14}{'premium':>9}{'models':>9}{'vs baseline':>14}")
    base = make(BASE_DMG, BASE_PRICE, 'rifle_base')
    for price in (35, 50, 65, 80, 95, 110, 125):
        up = make(3, price, f'rifle_up{price}')
        n_up, n_base = len(up(0)), len(base(0))
        wins = [versus(up, base, G, kw, N) for G, kw in SCENARIOS.values()]
        mean = sum(wins) / len(wins)
        print(f"  {price:<14}{price - BASE_PRICE:>+9}{n_up:>6} v{n_base:<2}"
              f"{mean * 100:>13.1f}%"
              + ("   <-- parity" if abs(mean - 0.5) < 0.025 else ""))

    # Same test on RANGE, damage held at +1 on both sides. This is the number
    # that has never been measured anywhere in the system: what the 18" chassis
    # is worth on its own, which IS the price of a "+1 Damage rifle".
    def mk_range(rng, price, key):
        data.WEAPONS[key] = dict(rng=rng, dmg=1, kind='ranged', cost=price,
                                 traits=('loud',) + (('two_handed',) if rng > 8 else ()))

        def build(side):
            crew = [leader(side, key)]
            spent = C('Leader', key)
            i = 0
            while spent + C('Fighter', key) <= BUDGET and i < 2:
                crew.append(fighter(i, side, key, melee=False))
                spent += C('Fighter', key); i += 1
            return _p(_fill(crew, side, spent, melee=False))
        return build

    print(f"\n  baseline = +1 Damage at 8\" for 15 Credits. The upgraded crew buys"
          f" the same weapon at 18\" and pays in bodies.")
    print(f"\n  {'18\" price':<14}{'premium':>9}{'models':>9}{'vs baseline':>14}")
    rbase = mk_range(8, 15, 'short_base')
    for price in (15, 30, 45, 60, 75, 90):
        up = mk_range(18, price, f'long{price}')
        n_up, n_base = len(up(0)), len(rbase(0))
        wins = [versus(up, rbase, G, kw, N) for G, kw in SCENARIOS.values()]
        mean = sum(wins) / len(wins)
        print(f"  {price:<14}{price - 15:>+9}{n_up:>6} v{n_base:<2}"
              f"{mean * 100:>13.1f}%"
              + ("   <-- parity" if abs(mean - 0.5) < 0.025 else ""))
    raise SystemExit(0)
else:
    for label, ladder in LADDERS.items():
        for rank, cost in ladder.items():
            data.RANKS[rank]['cost'] = cost
        header = (f"R{ladder['Recruit']}/F{ladder['Fighter']}"
                  f"/S{ladder['Specialist']}/L{ladder['Leader']}")
        results[label] = measure(label, header)
    axis = 'ladder'

print(f"\n{'=' * 108}")
print(f"SWEEP SUMMARY — mean win % by crew, and the spread at each {axis}")
print(f"  {axis:<11}" + "".join(f"{n[:9]:>10}" for n in names) + f"{'SPREAD':>9}")
for label, (means, spread, sizes) in results.items():
    print(f"  {label:<11}" + "".join(f"{means[n] * 100:9.0f} " for n in names) + f"{spread:8.0f}")
print(f"\n  crew sizes by {axis}:")
for label, (_, _, sizes) in results.items():
    print(f"  {label:<11}" + "  ".join(f"{n} {sizes[n]}" for n in names))
best = min(results.items(), key=lambda kv: kv[1][1])
print(f"\n  TIGHTEST SPREAD: {best[0]} at {best[1][1]:.0f} points")
print(f"  elapsed {time.time() - t0:.0f}s")
print("=" * 108)

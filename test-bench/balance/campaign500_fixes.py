# -*- coding: utf-8 -*-
"""CAMPAIGN START @ 500 — can it be FIXED without raising the cap? (2.5D engine)

`campaign500.py` established the problem: at a 500 cap the doc ladder produces a
46-point archetype spread, a Gunline that wins 18%, and crews of 2-4 models. Its
two suggested fixes -- raise the cap to 625-750, or cut the Leader's price -- were
both left untested. This harness tests them, plus four more, because the design
brief is explicit: 500 is wanted for the FEEL of growing a crew from nothing, so
raising the cap is the fallback, not the first answer.

THREE METHOD CHANGES FROM campaign500.py
  1. ARMOUR IS 60/100, NOT 30/60. campaign500.py pulls armour from points/ticks.py,
     which still carries the 30/60 that its own `armour` mode measured as WRONG
     (Armoured 64% -> 51%, spread 46 -> 37). FULL-RULES-SYSTEM-V1 §15 and the vault
     both print 60/100. Every published 500-cap number was therefore measured under
     a price the project has since rejected, which inflates the baseline spread.
     60/100 is used throughout here. ticks.py is still owed the correction.
  2. A ROOFTOP ARCHETYPE. The engine is 2.5D (see-over LOS, height advantage,
     falls) but every crew in campaign500.py walks on the ground, so verticality
     was never in the 500 question at all. Rooftop fields the Gunline's exact list
     under the ROOF policy, which isolates one thing: does height rescue a shooting
     list that cannot afford bodies?
  3. THE FLOOR, NOT JUST THE SPREAD. Spread hides which end is broken. A 40-point
     spread from one archetype at 18% is a different disease from the same spread
     spent evenly. Every table prints the worst archetype's win % (FLOOR) and the
     smallest legal crew (MIN MDL) beside the spread.

WHAT IT STILL CANNOT SEE (inherited, unchanged)
  Only Tier-1 skills exist in the engine, so a Specialist's T2 and a Leader's T3
  do nothing. Every number is a measurement of BODIES -- stat points, Orders and
  model count. The sim therefore UNDERVALUES Specialists and Leaders, which means
  any Founder price it recommends is a FLOOR for that rank, not a final price.
  Deployables are excluded (the costing engine has no price for them).

MODES
  baseline  the honest 500 baseline: doc ladder, armour 60/100
  cap       cap sweep 500 -> 1000 at corrected armour. Is 500 still uniquely bad?
  founder   a cheap Campaign-Start boss rank. Sweeps price x (Orders, stat points)
  noleader  drop the mandatory-Leader rule entirely
  freegear  a founding weapon allowance (scavenged kit costs no Crew Rating)
  rifle     sweep the rifle's unmeasured legacy-x10 class price
  combo     stack whatever won, and check it holds at 500 AND at 1000
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
from points.ticks import EQUIPMENT_CREDITS, HACK_GEAR_CREDITS
from points.weapons import WeaponBuild, weapon_cost

from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED, ROOF

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
MODE = sys.argv[2] if len(sys.argv) > 2 else 'baseline'
BUDGET = 500

BUILDS = {
    'fists':   WeaponBuild('Fists', 'unarmed'),
    'bat':     WeaponBuild('Baseball Bat', 'light_melee'),
    'crowbar': WeaponBuild('Crowbar', 'one_handed_melee', ('breaching',)),
    'sledge':  WeaponBuild('Sledgehammer', 'heavy_melee'),
    'pistol':  WeaponBuild('Pistol', 'sidearm'),
    'rifle':   WeaponBuild('Rifle', 'standard_ranged'),
    'molotov': WeaponBuild('Molotov', 'thrown', ('incendiary', 'blast'), ('single_use',)),
}
BASE_WEAPON_COST = {}
for key, build in BUILDS.items():
    data.WEAPONS[key]['cost'] = weapon_cost(build)
    BASE_WEAPON_COST[key] = data.WEAPONS[key]['cost']

# THE CORRECTION: the adopted price, not ticks.py's superseded 30/60.
ADOPTED_ARMOUR = {'none': 0, 'light': 60, 'heavy': 100}
for k, v in ADOPTED_ARMOUR.items():
    data.ARMOUR[k]['cost'] = v

data.EQUIPMENT['breach_kit']['cost'] = HACK_GEAR_CREDITS['breach_kit']
data.EQUIPMENT['exploit_suite']['cost'] = HACK_GEAR_CREDITS['exploit_suite']
data.EQUIPMENT['med_kit']['cost'] = EQUIPMENT_CREDITS['med_kit']

DOC_LADDER = dict(Recruit=65, Fighter=75, Specialist=125, Leader=170)

# The boss rank is swappable so `founder` mode can replace the mandatory Leader
# with a cheaper green one without touching any crew builder.
BOSS = dict(rank='Leader', stats=dict(dex=4, nrv=3, str=2),
            melee_stats=dict(str=4, nrv=3, agi=2))
REQUIRE_BOSS = True


def apply_ladder(ladder):
    for rank, cost in ladder.items():
        data.RANKS[rank]['cost'] = cost


def set_free_classes(free):
    """A founding weapon allowance: listed weapons cost 0 Crew Rating.

    Every builder below gives each model exactly one weapon, so zeroing a weapon's
    cost is exactly 'the first weapon is free' for these lists -- it is not a
    general free-arsenal rule, and it would not be one at the table either."""
    for key in BASE_WEAPON_COST:
        data.WEAPONS[key]['cost'] = 0 if key in free else BASE_WEAPON_COST[key]


# --------------------------------------------------------------------------
# UNITS — stat lines legal under §13 tier caps, 'gentle' shape (strong primary
# plus one real secondary), which engine2d measured as beating forced-spread.
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


def boss(side, weapon='rifle', armour='none', melee=False):
    """The crew's one command model — a Leader, or a Founder in `founder` mode."""
    st = dict(BOSS['melee_stats'] if melee else BOSS['stats'])
    skill = ('the_muscle_T3',) if melee else ('dead_eye_T3',)
    return Unit('Boss', side, BOSS['rank'], weapon, armour, skills=skill, **st)


def C(rank, weapon='bat', armour='none', equip=()):
    return data.unit_cost(rank, weapon, armour, equip)


def BC(weapon='rifle', armour='none'):
    return C(BOSS['rank'], weapon, armour)


def _p(crew, policy=BALANCED, gun_policy=None):
    for u in crew:
        u.policy = gun_policy if (gun_policy and u.has_gun()) else policy
    return crew


def _fill(crew, side, spent, melee=True):
    i = 90
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side, melee=melee))
        spent += C('Recruit', 'bat')
        i += 1
    return crew


# --------------------------------------------------------------------------
# CREWS — each greedily fills to the cap at whatever prices are set. The only
# composition rule enforced is REQUIRE_BOSS (one command model) + min 3 models.
# --------------------------------------------------------------------------
def swarm(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'sledge', melee=True)); spent += BC('sledge')
    i = 0
    while spent + C('Recruit', 'bat') <= BUDGET:
        crew.append(recruit(i, side)); spent += C('Recruit', 'bat'); i += 1
    return _p(crew)


def line(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'sledge', melee=True)); spent += BC('sledge')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(fighter(i, side, 'crowbar')); spent += C('Fighter', 'crowbar'); i += 1
    return _p(_fill(crew, side, spent))


def elite(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'rifle', 'light')); spent += BC('rifle', 'light')
    i = 0
    while spent + C('Specialist', 'rifle', 'light') <= BUDGET:
        crew.append(specialist(i, side, 'rifle', 'light'))
        spent += C('Specialist', 'rifle', 'light'); i += 1
    return _p(_fill(crew, side, spent))


def _gunline_list(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'rifle')); spent += BC('rifle')
    i = 0
    while spent + C('Fighter', 'rifle') <= BUDGET:
        crew.append(fighter(i, side, 'rifle', melee=False)); spent += C('Fighter', 'rifle'); i += 1
    while spent + C('Fighter', 'pistol') <= BUDGET:
        crew.append(fighter(i, side, 'pistol', melee=False)); spent += C('Fighter', 'pistol'); i += 1
    while spent + C('Recruit', 'pistol') <= BUDGET:
        crew.append(recruit(i, side, 'pistol', melee=False)); spent += C('Recruit', 'pistol'); i += 1
    return crew, spent


def gunline(side):
    crew, spent = _gunline_list(side)
    return _p(_fill(crew, side, spent, melee=False))


def rooftop(side):
    """The Gunline's EXACT list, roof-seeking. Isolates the 2.5D question: does
    height advantage + see-over LOS rescue a shooting crew that is body-starved?"""
    crew, spent = _gunline_list(side)
    return _p(_fill(crew, side, spent, melee=False), gun_policy=ROOF)


def armoured(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'sledge', 'light', melee=True)); spent += BC('sledge', 'light')
    i = 0
    while spent + C('Fighter', 'bat', 'light') <= BUDGET:
        crew.append(fighter(i, side, 'bat', 'light')); spent += C('Fighter', 'bat', 'light'); i += 1
    while spent + C('Recruit', 'bat', 'light') <= BUDGET:
        crew.append(recruit(i, side, 'bat', 'light')); spent += C('Recruit', 'bat', 'light'); i += 1
    return _p(_fill(crew, side, spent))


def mixed(side):
    crew, spent = [], 0
    if REQUIRE_BOSS:
        crew.append(boss(side, 'rifle')); spent += BC('rifle')
    if spent + C('Specialist', 'rifle') + 2 * C('Recruit', 'bat') <= BUDGET:
        crew.append(specialist(0, side, 'rifle')); spent += C('Specialist', 'rifle')
    i = 0
    while spent + C('Fighter', 'crowbar') <= BUDGET:
        crew.append(fighter(i, side, 'crowbar')); spent += C('Fighter', 'crowbar'); i += 1
    return _p(_fill(crew, side, spent))


CREWS = {'Swarm': swarm, 'Line': line, 'Elite': elite, 'Gunline': gunline,
         'Rooftop': rooftop, 'Armoured': armoured, 'Mixed': mixed}
names = list(CREWS)


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


def versus(a, b, GameCls, kw, n, seed=20260806):
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


def measure(label, header, quiet=False):
    sizes, spends = {}, {}
    for n in names:
        c = CREWS[n](0)
        sizes[n] = len(c)
        spends[n] = sum(u.cost for u in c)
    if not quiet:
        print(f"\n{'-' * 112}")
        print(f"[{label}]  {header}")
        print("  crews: " + "  ".join(f"{n} {sizes[n]}mdl/{spends[n]}cr" for n in names))
        illegal = [n for n in names if sizes[n] < 3]
        if illegal:
            print(f"  !! BELOW the 3-model minimum (illegal list): {', '.join(illegal)}")
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
    floor = min(means.values()) * 100
    if not quiet:
        print(f"  {'crew':<10}" + "".join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
        for n in names:
            print(f"  {n:<10}" + "".join(f"{per_sc[s][n] * 100:12.0f} " for s in SCENARIOS)
                  + f"{means[n] * 100:7.0f}")
        print(f"  >>> SPREAD {spread:.0f}   FLOOR {floor:.0f}% ({min(means, key=means.get)})"
              f"   MIN MDL {min(sizes.values())}"
              f"   (best {max(means, key=means.get)})")
    return dict(means=means, spread=spread, floor=floor, sizes=sizes, spends=spends)


def summary(results, axis):
    print(f"\n{'=' * 112}")
    print(f"SUMMARY — mean win % by crew; SPREAD, FLOOR and smallest crew at each {axis}")
    print(f"  {axis:<14}" + "".join(f"{n[:8]:>9}" for n in names)
          + f"{'SPREAD':>8}{'FLOOR':>7}{'MINMDL':>8}")
    for label, r in results.items():
        print(f"  {label:<14}" + "".join(f"{r['means'][n] * 100:8.0f} " for n in names)
              + f"{r['spread']:7.0f}{r['floor']:6.0f}%{min(r['sizes'].values()):7d}")
    print(f"\n  crew sizes by {axis}:")
    for label, r in results.items():
        print(f"  {label:<14}" + "  ".join(f"{n} {r['sizes'][n]}" for n in names))
    best = min(results.items(), key=lambda kv: kv[1]['spread'])
    print(f"\n  TIGHTEST SPREAD: {best[0]} at {best[1]['spread']:.0f} points "
          f"(floor {best[1]['floor']:.0f}%)")


print("=" * 112)
print(f"CAMPAIGN START @ {BUDGET} — FIX SEARCH [{MODE}]   "
      f"({N} games/pairing, sides swapped, 7 archetypes x 4 scenarios, 2.5D engine)")
print("=" * 112)
print(f"  armour CORRECTED to the adopted 60/100 (ticks.py still carries 30/60)")
print(f"  weapons from points/: " + "  ".join(f"{k} {BASE_WEAPON_COST[k]}" for k in BUILDS))
print(f"  games per configuration = {N * len(SCENARIOS) * (len(names) * (len(names) - 1) // 2):,}")

t0 = time.time()
results = {}
apply_ladder(DOC_LADDER)

if MODE == 'baseline':
    results['500 doc'] = measure('500 doc', "doc ladder R65/F75/S125/L170, armour 60/100")
    axis = 'config'

elif MODE == 'cap':
    for cap in (500, 560, 625, 750, 1000):
        BUDGET = cap
        results[f'{cap}cr'] = measure(f'{cap} CR', "doc ladder, armour 60/100")
    axis = 'cap'

elif MODE == 'founder':
    # A green crew's boss should not be the most expensive model in the game.
    # Sweep a cheaper command model on two axes: what it costs, and what it IS
    # (Orders and stat points). 'L170/9pt/2ord' is the doc's Leader = control.
    variants = [
        ('L170/9pt/2ord', 170, 2, dict(dex=4, nrv=3, str=2), dict(str=4, nrv=3, agi=2)),
        ('F140/9pt/1ord', 140, 1, dict(dex=4, nrv=3, str=2), dict(str=4, nrv=3, agi=2)),
        ('F120/7pt/1ord', 120, 1, dict(dex=4, nrv=2, str=1), dict(str=4, nrv=2, agi=1)),
        ('F100/7pt/1ord', 100, 1, dict(dex=4, nrv=2, str=1), dict(str=4, nrv=2, agi=1)),
        ('F95/5pt/1ord',   95, 1, dict(dex=2, nrv=2, agi=1), dict(str=2, nrv=2, agi=1)),
        ('F80/5pt/1ord',   80, 1, dict(dex=2, nrv=2, agi=1), dict(str=2, nrv=2, agi=1)),
    ]
    for label, cost, orders, st, mst in variants:
        data.RANKS['Founder'] = dict(stat_pts=sum(st.values()), skills=1,
                                     orders=orders, cost=cost)
        BOSS.update(rank='Founder', stats=st, melee_stats=mst)
        pct = cost * 100 // BUDGET
        results[label] = measure(label, f"boss = {cost}cr, {orders} Order(s), "
                                        f"{sum(st.values())} stat pts "
                                        f"— body alone is {pct}% of the crew")
    axis = 'founder'

elif MODE == 'noleader':
    for label, req in (('leader req', True), ('no leader', False)):
        REQUIRE_BOSS = req
        results[label] = measure(label, f"mandatory Leader = {req}, doc ladder @ 500")
    axis = 'rule'

elif MODE == 'freegear':
    # A founding crew scavenged what it could find. Extending the existing free
    # Light Melee to a wider class costs the crew nothing in Rating, which moves
    # the body:gear ratio without touching the cap.
    for label, free in (
        ('none (RAW)', set()),
        ('+sidearm', {'pistol'}),
        ('+melee', {'crowbar', 'sledge'}),
        ('+sidearm+melee', {'pistol', 'crowbar', 'sledge'}),
        ('+all incl rifle', {'pistol', 'crowbar', 'sledge', 'rifle', 'molotov'}),
    ):
        set_free_classes(free)
        results[label] = measure(label, f"free at Campaign Start: {sorted(free) or 'nothing'}")
    set_free_classes(set())
    axis = 'free kit'

elif MODE == 'rifle':
    # CLASS_CREDITS is marked "legacy x10" in ticks.py — the rifle's 100 is
    # inherited from the old 10-point Standard Ranged and has never been measured,
    # unlike the characteristics bolted onto it. At 1000 it is 10% of a crew; at
    # 500 it is 20%. Sweep it at a fixed 500 cap, scaling the sidearm with it.
    for rifle in (100, 85, 70, 55, 40):
        data.WEAPONS['rifle']['cost'] = rifle
        data.WEAPONS['pistol']['cost'] = int(round(rifle * 0.4 / 5) * 5)
        results[f'rifle {rifle}'] = measure(
            f'rifle {rifle}',
            f"rifle {rifle} · pistol {data.WEAPONS['pistol']['cost']}  >> boss+rifle = "
            f"{170 + rifle} ({(170 + rifle) * 100 // BUDGET}% of the crew)")
    data.WEAPONS['rifle']['cost'] = BASE_WEAPON_COST['rifle']
    data.WEAPONS['pistol']['cost'] = BASE_WEAPON_COST['pistol']
    axis = 'rifle'

elif MODE == 'combo':
    # Stack the levers that worked, then check the stack does not break the
    # 1000-Credit Match Play game it has to coexist with.
    def founder(cost, orders, st, mst):
        data.RANKS['Founder'] = dict(stat_pts=sum(st.values()), skills=1,
                                     orders=orders, cost=cost)
        BOSS.update(rank='Founder', stats=st, melee_stats=mst)

    ST, MST = dict(dex=4, nrv=2, str=1), dict(str=4, nrv=2, agi=1)

    results['A doc @500'] = measure('A doc @500', "control: Leader 170, no free kit")

    founder(120, 1, ST, MST)
    results['B founder120'] = measure('B founder120', "Founder 120 (7pt, 1 Order)")

    set_free_classes({'pistol', 'crowbar', 'sledge'})
    results['C B+freekit'] = measure('C B+freekit', "Founder 120 + free sidearm/melee")

    data.WEAPONS['rifle']['cost'] = 70
    results['D C+rifle70'] = measure('D C+rifle70', "Founder 120 + free kit + rifle 70")

    # does the same package hold at Match Play's 1000, with a real Leader back?
    BUDGET = 1000
    BOSS.update(rank='Leader', stats=dict(dex=4, nrv=3, str=2),
                melee_stats=dict(str=4, nrv=3, agi=2))
    apply_ladder(dict(Recruit=65, Fighter=95, Specialist=165, Leader=245))
    set_free_classes(set())
    data.WEAPONS['rifle']['cost'] = 70
    results['E 1000 rifle70'] = measure('E 1000 rifle70',
                                        "Match Play @1000, Leader 245, rifle 70, no free kit")
    data.WEAPONS['rifle']['cost'] = BASE_WEAPON_COST['rifle']
    results['F 1000 RAW'] = measure('F 1000 RAW', "Match Play @1000 unchanged (rifle 100)")
    axis = 'package'

elif MODE == 'capfine':
    # The 500->560 jump in `cap` was a cliff, not a curve. Find the exact step.
    # Arithmetic says it should be where a THIRD body fits for the worst list:
    #   Gunline  boss+rifle 270 + Fighter+rifle 175 + Recruit 65 = 510
    #   Armoured boss+sledge+light 330 + Fighter+bat+light 135 + Recruit 65 = 530
    for cap in (500, 510, 520, 530, 540, 550, 575, 600):
        BUDGET = cap
        results[f'{cap}cr'] = measure(f'{cap} CR', "doc ladder, armour 60/100, rifle 100")
    axis = 'cap'

elif MODE == 'combo2':
    # `combo` showed the levers are NOT additive: free kit poisoned every stack it
    # touched (spread 44 -> 53). This retests the survivors ONLY, and checks each
    # against the 1000-Credit Match Play game it has to coexist with.
    def founder(cost, orders, st, mst):
        data.RANKS['Founder'] = dict(stat_pts=sum(st.values()), skills=1,
                                     orders=orders, cost=cost)
        BOSS.update(rank='Founder', stats=st, melee_stats=mst)

    def leader_back():
        BOSS.update(rank='Leader', stats=dict(dex=4, nrv=3, str=2),
                    melee_stats=dict(str=4, nrv=3, agi=2))

    ST, MST = dict(dex=4, nrv=2, str=1), dict(str=4, nrv=2, agi=1)

    results['A 500 RAW'] = measure('A 500 RAW', "control: rifle 100, Leader 170, cap 500")

    data.WEAPONS['rifle']['cost'] = 85
    results['B r85 @500'] = measure('B r85 @500', "rifle 85 only")
    data.WEAPONS['rifle']['cost'] = 70
    results['C r70 @500'] = measure('C r70 @500', "rifle 70 only")

    BUDGET = 550
    results['D r70 @550'] = measure('D r70 @550', "rifle 70 + cap 550 (Armoured reaches 3)")
    BUDGET = 500

    founder(120, 1, ST, MST)
    results['E r70+fnd120'] = measure('E r70+fnd120', "rifle 70 + Founder 120, cap 500")
    leader_back()

    # --- the coexistence check: does a cheaper rifle break Match Play at 1000? ---
    BUDGET = 1000
    apply_ladder(dict(Recruit=65, Fighter=95, Specialist=165, Leader=245))
    data.WEAPONS['rifle']['cost'] = BASE_WEAPON_COST['rifle']
    results['F 1000 r100'] = measure('F 1000 r100', "Match Play @1000 unchanged")
    data.WEAPONS['rifle']['cost'] = 85
    results['G 1000 r85'] = measure('G 1000 r85', "Match Play @1000, rifle 85")
    data.WEAPONS['rifle']['cost'] = 70
    results['H 1000 r70'] = measure('H 1000 r70', "Match Play @1000, rifle 70")
    axis = 'package'

elif MODE == 'grid':
    # WHY THIS EXISTS. Single configurations disagree violently: rifle 70 scores a
    # 9 spread at cap 500 and a 26 at cap 550. Both cannot be "the balance of the
    # system". Crews are built by greedy fill, so the spread depends on exactly how
    # each archetype's per-model cost divides into the cap — a QUANTIZATION effect,
    # not sampling noise (24,000 games per archetype mean; noise is ~1 point).
    #
    # So sweep the surface, not points, and report the robust REGION. A fix that
    # only works at one (cap, price) pair is a coincidence, not a fix.
    grid = {}
    for rifle in (100, 85, 70):
        data.WEAPONS['rifle']['cost'] = rifle
        data.WEAPONS['pistol']['cost'] = int(round(rifle * 0.4 / 5) * 5)
        for cap in (500, 510, 525, 550, 575, 600):
            BUDGET = cap
            r = measure(f'r{rifle}@{cap}', f"rifle {rifle}, cap {cap}", quiet=True)
            grid[(rifle, cap)] = r
            print(f"  rifle {rifle:>3} cap {cap:>4}  spread {r['spread']:5.0f}"
                  f"  floor {r['floor']:3.0f}%  min mdl {min(r['sizes'].values())}"
                  f"  sizes " + "/".join(str(r['sizes'][n]) for n in names))
    data.WEAPONS['rifle']['cost'] = BASE_WEAPON_COST['rifle']
    data.WEAPONS['pistol']['cost'] = BASE_WEAPON_COST['pistol']

    print(f"\n{'=' * 112}")
    print("SPREAD SURFACE (lower is better) — rows: rifle price, cols: cap")
    print(f"  {'rifle':<8}" + "".join(f"{c:>8}" for c in (500, 510, 525, 550, 575, 600))
          + f"{'mean':>8}{'worst':>8}")
    for rifle in (100, 85, 70):
        row = [grid[(rifle, c)]['spread'] for c in (500, 510, 525, 550, 575, 600)]
        print(f"  {rifle:<8}" + "".join(f"{v:8.0f}" for v in row)
              + f"{sum(row) / len(row):8.1f}{max(row):8.0f}")
    print("\nFLOOR SURFACE (higher is better) — the worst archetype's win %")
    print(f"  {'rifle':<8}" + "".join(f"{c:>8}" for c in (500, 510, 525, 550, 575, 600))
          + f"{'mean':>8}{'worst':>8}")
    for rifle in (100, 85, 70):
        row = [grid[(rifle, c)]['floor'] for c in (500, 510, 525, 550, 575, 600)]
        print(f"  {rifle:<8}" + "".join(f"{v:8.0f}" for v in row)
              + f"{sum(row) / len(row):8.1f}{min(row):8.0f}")
    print("\n  Judge a row by its MEAN and WORST, not its best cell. A price that is")
    print("  good across the whole cap range is a real fix; a single good cell is not.")
    raise SystemExit(0)

else:
    raise SystemExit(f"unknown mode {MODE!r}")

summary(results, axis)
print(f"\n  elapsed {time.time() - t0:.0f}s")
print("=" * 112)

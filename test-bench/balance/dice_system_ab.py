"""Settlements - dice system A/B: current 1d10 two-roll vs proposed 1d20 one-roll.

THE QUESTION THIS ANSWERS, AND THE ONE IT DOES NOT.

Per-shot probabilities need no simulation - the chain is analytically closed and
was enumerated exactly before this harness was written. What arithmetic cannot
answer is what a SUSTAINED EXCHANGE looks like: how long a firefight runs, and
whether models leave the table by WOUND or by NERVE. Those are emergent over
rounds, because Stress accumulates, Shaken feeds back into the attack roll, and
the Break margin table is non-linear. That feedback loop is the whole subject.

    Measured here : rounds to resolution, removals split wound-vs-BugOut, mean
                    Stress carried, share of rounds spent Shaken.
    NOT measured  : whether the d20 game is BALANCED. Every price in the
                    catalogue was measured under 1d10/7+. Running d10-priced
                    rosters under d20 rules is a valid CONTROLLED comparison -
                    it isolates the dice chain and holds everything else - but
                    it says nothing about what those rosters should cost after
                    the change. That is a separate re-measurement and the two
                    questions must not be conflated.

WHAT IS MODELLED. A fixed-geometry firefight: two symmetric sides, every living
fighter shoots once per round at a random living enemy, then an End Phase runs
Break tests and Stress shedding. Rules applied verbatim from `Full Rules System
v1` SS9/11: Shaken is a flat -1 at 1+ Stress and does NOT double-apply to the
Break test; Break is `1d10 + NRV - (Stress-1)` vs 7+ at 2+ Stress; the fail
margin table is 2 -> Bolt, 3 -> Broken, 4+ -> BugOut; a unit at exactly 1 Stress
sheds it in the End Phase only on a round it gained none.

WHAT IS DELIBERATELY NOT MODELLED, so the delta stays attributable to the dice:
movement, cover changes, terrain, Attack Dice, payloads, reactions, Stabilize
and bleed-out. A Down model is simply removed. Absolute numbers here are NOT
game predictions - only the A/B delta between systems is meaningful.

THREE ASSUMPTIONS THAT ARE DESIGN DECISIONS, NOT CONVERSIONS. Each is flagged
because getting one wrong would silently invalidate the comparison:

  1. On d20 a natural 20 auto-succeeds at whichever test is being made, and a
     natural 1 auto-fails - the direct analogue of nat 1/nat 10.
  2. The Break test converts with the die. Leaving it on d10 would put two dice
     types in the game, which SS0 forbids.
  3. THE BREAK MARGIN TABLE DOES NOT CONVERT CLEANLY. On d10 vs 7+ a fail margin
     runs 1-6; on d20 vs 12+ it runs 1-11, so keeping 2/3/4+ would make BugOut
     dramatically more common for reasons that have nothing to do with morale
     design. The table is scaled x2 (4/6/8+) as the default, and the unscaled
     table is reported as a sensitivity so the size of that decision is visible.
     This is Ross's ruling to make, not the harness's.

Fail-by-1 has no listed result in SS11's table, which starts at margin 2. Modelled
as no additional effect, and noted as a genuine gap in the written rule.
"""

import json
import random
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

random.seed(20260708)
N_FIGHTS = 20000
MAX_ROUNDS = 30


# --------------------------------------------------------------------------
# the three resolution chains
# --------------------------------------------------------------------------

def resolve_d10_two(dex, cover, dmg, armour, shaken):
    """Current: 1d10+DEX+mods vs 7+, then a separate 1d10+DMG-ARM vs 7+."""
    d = random.randint(1, 10)
    if d == 1:
        return "miss"
    if d != 10 and d + dex - cover - shaken < 7:
        return "miss"
    e = random.randint(1, 10)
    if e == 1:
        return "pin"
    if e == 10 or e + dmg - armour >= 7:
        return "wound"
    return "pin"


def resolve_d20_dmg_in(dex, cover, dmg, armour, shaken):
    """Proposed A: 1d20 + DEX + DMG - cover - ARM.  12+ hits, 17+ wounds."""
    d = random.randint(1, 20)
    if d == 1:
        return "miss"
    total = d + dex + dmg - cover - armour - shaken
    if d == 20 or total >= 17:
        return "wound"
    if total >= 12:
        return "pin"
    return "miss"


def resolve_d20_dmg_bar(dex, cover, dmg, armour, shaken):
    """Proposed B: 1d20 + DEX - cover vs 12+ to hit; Damage lowers the wound bar.

    Keeps Damage off the accuracy roll - a machine gun no longer makes you a
    better shot - at the cost of a wound bar that moves per matchup.
    """
    d = random.randint(1, 20)
    if d == 1:
        return "miss"
    total = d + dex - cover - shaken
    if d == 20:
        return "wound"
    if total < 12:
        return "miss"
    return "wound" if total >= 17 - dmg + armour else "pin"


# (resolver, die sides, target number, is_d20)
# The margin-table scaling below applies ONLY to the d20 systems. d10 keeps its
# native 2/3/4+ table in every run - scaling the baseline as well would have
# silently zeroed the current system's morale removals and made the whole
# comparison meaningless.

def resolve_d20_split(dex, cover, dmg, armour, shaken):
    """Proposed C: one roll read at TWO points - McCullough's actual shape.

    Cover modifies the roll that decides whether you are HIT. Armour is applied
    only when that same total is re-read to decide whether you are HURT. This is
    the structure Frostgrave/Stargrave/RoSD actually use (cover is a Shooting
    Modifier on the target's side; Armour is subtracted from the winner's total
    afterwards), and it is what SS2 of the Settlements rules already requires:
    "Cover protects against being hit; armor protects against being hurt."

    The cost, relative to folding Damage into the roll: the Pin band is no longer
    a flat 25%. Its width is (5 - Damage + Armour) faces, so it varies from 35%
    (unarmed vs heavy armour) down to 0% (a +5 Heavy Ranged against an unarmoured
    target, where every hit wounds). Whether that matters is what this measures.
    """
    d = random.randint(1, 20)
    if d == 1:
        return "miss"
    if d == 20:
        return "wound"
    total = d + dex - cover - shaken
    if total < 12:
        return "miss"
    return "wound" if total + dmg - armour >= 17 else "pin"


SYSTEMS = {
    "d10 two-roll (current)": (resolve_d10_two, 10, 7, False),
    "d20 one-roll, DMG in roll": (resolve_d20_dmg_in, 20, 12, True),
    "d20 one-roll, DMG on bar": (resolve_d20_dmg_bar, 20, 12, True),
    "d20 split: cover=hit arm=wound": (resolve_d20_split, 20, 12, True),
}


# --------------------------------------------------------------------------
# morale
# --------------------------------------------------------------------------

def break_test(nrv, stress, sides, target, margin_scale):
    """SS11: 1d10 + NRV - (Stress-1) vs 7+. Shaken does not double-apply here."""
    d = random.randint(1, sides)
    if d == sides:
        return None
    total = d + nrv - (stress - 1)
    if d != 1 and total >= target:
        return None
    margin = target - total
    if margin >= 4 * margin_scale:
        return "bugout"
    if margin >= 3 * margin_scale:
        return "broken"
    if margin >= 2 * margin_scale:
        return "bolt"
    return None


class Fighter:
    __slots__ = ("dex", "nrv", "dmg", "armour", "stress", "alive", "suppressed", "gained")

    def __init__(self, dex, nrv, dmg, armour):
        self.dex, self.nrv, self.dmg, self.armour = dex, nrv, dmg, armour
        self.stress = 0
        self.alive = True
        self.suppressed = False
        self.gained = False


def run_fight(resolve, sides, target, margin_scale, profile, cover, squad):
    dex, nrv, dmg, armour = profile
    sides_ = [[Fighter(dex, nrv, dmg, armour) for _ in range(squad)] for _ in range(2)]
    downs = bugouts = 0

    for rnd in range(1, MAX_ROUNDS + 1):
        for f in sides_[0] + sides_[1]:
            f.gained = False

        for s in (0, 1):
            foes = [f for f in sides_[1 - s] if f.alive]
            if not foes:
                break
            for f in sides_[s]:
                if not f.alive or f.suppressed:
                    continue
                foes = [x for x in sides_[1 - s] if x.alive]
                if not foes:
                    break
                tgt = random.choice(foes)
                shaken = 1 if f.stress >= 1 else 0
                r = resolve(f.dex, cover, f.dmg, tgt.armour, shaken)
                if r == "wound":
                    tgt.alive = False
                    downs += 1
                elif r == "pin":
                    tgt.stress += 1
                    tgt.gained = True

        # End Phase
        for f in sides_[0] + sides_[1]:
            f.suppressed = False
            if not f.alive:
                continue
            if f.stress >= 2:
                res = break_test(f.nrv, f.stress, sides, target, margin_scale)
                if res == "bugout":
                    f.alive = False
                    bugouts += 1
                elif res in ("bolt", "broken"):
                    f.suppressed = True
            elif f.stress == 1 and not f.gained:
                f.stress = 0

        live = [sum(1 for f in s if f.alive) for s in sides_]
        if 0 in live:
            return rnd, downs, bugouts, sides_

    return MAX_ROUNDS, downs, bugouts, sides_


def sweep(profile, cover, squad, margin_scale, label):
    print(f"\n  {label}   DEX+{profile[0]} NRV+{profile[1]} DMG+{profile[2]} "
          f"ARM-{profile[3]} | cover -{cover} | {squad}v{squad}")
    print(f"    {'system':<28}{'rounds':>8}{'by wound':>10}{'by nerve':>10}"
          f"{'nerve %':>9}{'unresolved':>12}")
    out = {}
    for name, (fn, sides, target, is_d20) in SYSTEMS.items():
        scale = margin_scale if is_d20 else 1
        tot_r = tot_d = tot_b = stuck = 0
        for _ in range(N_FIGHTS):
            r, d, b, _ = run_fight(fn, sides, target, scale, profile, cover, squad)
            tot_r += r
            tot_d += d
            tot_b += b
            if r == MAX_ROUNDS:
                stuck += 1
        rem = tot_d + tot_b
        nerve = tot_b / rem if rem else 0.0
        print(f"    {name:<28}{tot_r/N_FIGHTS:>8.1f}{tot_d/N_FIGHTS:>10.2f}"
              f"{tot_b/N_FIGHTS:>10.2f}{nerve:>8.0%}{stuck/N_FIGHTS:>12.1%}")
        out[name] = {
            "mean_rounds": tot_r / N_FIGHTS,
            "removals_by_wound": tot_d / N_FIGHTS,
            "removals_by_bugout": tot_b / N_FIGHTS,
            "nerve_share": nerve,
            "unresolved_share": stuck / N_FIGHTS,
        }
    return out


def main():
    print(__doc__.split("\n")[0])
    print(f"N = {N_FIGHTS:,} fights per cell, seed 20260708, max {MAX_ROUNDS} rounds\n")
    print("=" * 78)
    print("BREAK MARGIN TABLE SCALED x2 ON d20 (4 / 6 / 8+) - the default")
    print("=" * 78)

    results = {"margin_scaled": {}, "margin_unscaled": {}}
    cells = [
        ((2, 2, 3, 1), 1, 4, "line fighters, light cover"),
        ((2, 2, 3, 2), 2, 4, "line fighters, heavy cover + heavy armour"),
        ((1, 1, 1, 2), 2, 4, "green crew, pistols, dug-in target"),
        ((4, 3, 4, 1), 2, 4, "veterans, heavy cover"),
        ((6, 3, 3, 2), 2, 3, "marksmen, heavy cover + heavy armour"),
    ]
    for profile, cover, squad, label in cells:
        results["margin_scaled"][label] = sweep(profile, cover, squad, 2, label)

    print()
    print("=" * 78)
    print("SENSITIVITY: margin table left UNSCALED on d20 (2 / 3 / 4+)")
    print("  the size of the ruling Ross owes on the Break margin table")
    print("=" * 78)
    for profile, cover, squad, label in cells[:3]:
        results["margin_unscaled"][label] = sweep(profile, cover, squad, 1, label)

    path = Path(__file__).resolve().parent / "results" / "dice-system-ab.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

"""The GEAR anchor, in one place, with its provenance attached.

Four measurement scripts each hardcoded `ANCHOR = 1.150`. That is the drift
pattern this rebuild exists to stop: a constant copied into several files goes
stale in some of them and nobody can tell which number a given result used. It
lives here now, and every script imports it.

HISTORY, kept because the movement is the point:

  1.1183   realistic.py, 1D board, asymmetric, no side swap. The original.
  1.12     hardcoded in packet_battle.py as DMG_ANCHOR, attributed to
           conditions2d.py, which does not actually produce it.
  0.90385  primitives2d, same engine, different lists.
  1.150    paired mirror, N=4000 x 6 cells, 2026-08-11. Admitted 1.12 and
           1.1183, rejected 0.90385. Measured under a policy defect.
  1.332    paired mirror, N=4000 x 6 cells, 2026-08-12, after the BalancedPolicy
           advance fix. Rejected all three earlier candidates - but priced across
           hold AND annihilate, and so superseded in turn.
  0.786    paired mirror, N=4000 x 9 cells, 2026-08-12, objective-only pricing,
           hold and hold_claim weighted 50/50. Superseded: the 50/50 was never
           chosen, and half of it was a scenario the ruleset does not contain.
  0.3432   hold_claim ONLY, 2026-08-13. `hold` dropped as modelling no shipped
           scenario. CI [0.234, 0.453]. HONEST, NOT CORRECT - see below.

The 1.150 run and an incidental 1.162 run agreed with each other and with 1.12,
and all of them were wrong for the same reason: BalancedPolicy shot instead of
advancing, so weapon range was negatively correlated with objective play and no
ranged crew ever reached an objective. Two independent confirmations of a number
that was wrong for a cause neither run could see.

1.332 then failed for a SECOND, unrelated reason: it averaged Annihilate into a
price, and the ruleset wins on objectives and never on kills. Dropping the kill
scenario cuts the anchor by 41% and RAISES every Credits price by 1.694x, because
the anchor is a denominator. Both defects were invisible from inside the number.

THE 5x SPREAD IS GONE, AND WHERE IT WENT IS THE POINT. Under the 50/50 blend the
per-cell values ran 0.292 to 1.471 - a 5.0x spread that had widened twice and was
the main evidence that a flat scalar might be the wrong SHAPE for this constant.

Priced on hold_claim alone the spread is 0.292 to 0.396: 1.35x. The 5x was almost
entirely the hold-vs-hold_claim gap, and that gap was never dispersion - it was
THE COST OF THE CLAIM STEP. An Action spent claiming is an Action not spent
attacking, so a damage buff has fewer chances to land. Two different games were
being averaged, and the average looked like a curve.

So the flat-vs-curve case is now much WEAKER than it appeared, on this evidence.
The question stays open pending the terrain-density sweep (a measured 66-point
win-rate lever, Full Rules System v1 §187), but the 5x that was driving it was an
artefact of the scenario mix, not a property of the atom.

The 15 Credits it is pegged to remains a CHOICE, not a measurement.
"""

from __future__ import annotations

# win-points per model buffed, +1 on the injury roll.
# hold_claim ONLY - the single faithful model of a shipped scenario.
VALUE = 0.3432
CI95 = (0.2337, 0.4527)
CELL_SPREAD = (0.292, 0.396)

# The scale choice. Pegging +1 Damage at this many Credits fixes the whole
# Credits scale; nothing measured it.
DAMAGE_CREDITS = 15

MEASURED = "gear-anchor-objective-n4000, 2026-08-12, objective-only pricing"

# THE HEAVIEST PROVISIONAL MARKING IN THE PROJECT, AND IT TRAVELS WITH THE NUMBER.
#
# 0.786 is the THIRD value in a row to reject its predecessors, and each preceding
# error was invisible from inside the number the one before it produced:
#
#   1.150 -> rejected by 1.332   cause: BalancedPolicy shot instead of advancing
#   1.332 -> rejected by 0.786   cause: Annihilate averaged into a price
#
# Neither cause was detectable from the measurement that carried it. Both runs
# were internally clean: paired estimator, tight CI, sane per-cell spread. 1.150
# even had two independent confirmations, and all of them were wrong together.
#
# This is NOT a reason to doubt 0.786 specifically - it is the best-founded anchor
# this project has had, and it is the first one measured on the scenarios the
# ruleset actually wins on. It is a reason it must not be treated as SETTLED
# merely because two prior errors were found. The base rate for "this anchor is
# final" is currently 0 for 3, and nothing about the third run changes what the
# first two demonstrated: a clean internal result cannot see the assumption it
# was built on.
#
# Cite it with this caveat everywhere, exactly as 1.332 and 1.150 should have been.
PROVISIONAL = (
    "COVERAGE-LIMITED, NOT A WORKING ANCHOR - rests on 1 of 5 shipped scenarios, "
    "and the most static one. Overvalues range/damage/armour, undervalues "
    "mobility/tempo/stealth. Fourth value in a row to reject its predecessors."
)

# 0.3432 IS HONEST. IT IS NOT CORRECT. DO NOT TREAT IT AS THE WORKING ANCHOR.
#
# Dropping `hold` removed a scenario that does not exist in the ruleset, which
# makes this number honest about WHAT IT MEASURED. It does not make it right,
# because what it measured is one fifth of the game:
#
#   Take a Hold    Control, VP accrual        MODELLED (this number)
#   Escort         Mobile, asymmetric         absent
#   Raid           Retrieve, enemy half       absent
#   Sabotage       Timer, sudden death        absent
#   Power Supply   Network, sudden death      absent
#
# Take a Hold is the most STATIC of the five. Pricing the whole game against it
# systematically overvalues defensive and static atoms - range, damage, armour -
# and undervalues mobility, tempo, stealth and objective-running, which is what
# the four missing scenarios reward. That is the DEX-ladder failure one level up:
# internally clean, structurally biased by the thing it was measured on.
#
# THE BLOCKER IS NO LONGER "WHICH ANCHOR VALUE". IT IS SCENARIO COVERAGE.
# Every atom priced from here inherits single-scenario bias until the harness
# covers something structurally different from control play. Sabotage and Raid
# are the two furthest from what hold_claim already measures - sudden-death
# timing and scoring in the enemy's half - so they expose the bias fastest.
#
# Expect this number to move again when they land. Do not spend a durable stamp
# on it, and do not write Credits into any shipped table against it.

# Every price taken at the 50/50 blend is low by this factor.
RESCALE_FROM_0786 = 2.2900

# Every price taken at 1.332 is low by this factor. Kept as a constant because
# several stored results carry valid objective-only NUMERATORS and only a wrong
# conversion - those can be re-priced by arithmetic instead of re-run.
RESCALE_FROM_1332 = 1.6941


def credits_per_winpoint() -> float:
    return DAMAGE_CREDITS / VALUE


def to_credits(wp: float) -> float:
    """Convert win-points per model into Credits at the current scale choice."""
    return wp * credits_per_winpoint()


def describe() -> str:
    """Every script prints this. The caveat is IN it so it cannot be dropped by a
    caller who only wanted the number."""
    lo, hi = CI95
    slo, shi = CELL_SPREAD
    return (f"anchor {VALUE:.3f} wp/model = {DAMAGE_CREDITS} Cr "
            f"(CI [{lo:.3f}, {hi:.3f}], per-cell {slo:.3f}..{shi:.3f}) "
            f"-> {credits_per_winpoint():.2f} Cr per win-point\n"
            f"  {PROVISIONAL}")

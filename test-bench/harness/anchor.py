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
  0.786    paired mirror, N=4000 x 9 cells, 2026-08-12, OBJECTIVE-ONLY pricing.
           REJECTS ALL FOUR PREDECESSORS, 1.332 included. CI [0.679, 0.894].

The 1.150 run and an incidental 1.162 run agreed with each other and with 1.12,
and all of them were wrong for the same reason: BalancedPolicy shot instead of
advancing, so weapon range was negatively correlated with objective play and no
ranged crew ever reached an objective. Two independent confirmations of a number
that was wrong for a cause neither run could see.

1.332 then failed for a SECOND, unrelated reason: it averaged Annihilate into a
price, and the ruleset wins on objectives and never on kills. Dropping the kill
scenario cuts the anchor by 41% and RAISES every Credits price by 1.694x, because
the anchor is a denominator. Both defects were invisible from inside the number.

THE SPREAD IS PART OF THE NUMBER, AND IT HAS NOW WIDENED TWICE. Objective-cell
values run 0.292 to 1.471 - a 5.0x spread, up from ~2x under mixed pricing. The
structure is not noise: hold_claim reads 0.29-0.40 in EVERY list while hold reads
0.90-1.47 in every list, consistently, 3/3. So the pricing set itself contains a
systematic scenario gap, and the headline averages across it. Whether that
average is the right shape is OPEN (see POINTS-REBUILD-TRACKING §4.2) and is
deliberately NOT ruled on here: terrain density is a 66-point win-rate lever in
the ruleset (Full Rules System v1 §187), larger than any atom yet measured, and
it is expected to move this spread. Do not let the headline figure travel alone.

The 15 Credits it is pegged to remains a CHOICE, not a measurement.
"""

from __future__ import annotations

# win-points per model buffed, +1 on the injury roll. OBJECTIVE-ONLY.
VALUE = 0.786
CI95 = (0.679, 0.894)
CELL_SPREAD = (0.292, 1.471)

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
    "PROVISIONAL - third anchor in a row to reject its predecessors; each prior "
    "error was invisible from inside the number before it. Best-founded to date, "
    "not settled."
)

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

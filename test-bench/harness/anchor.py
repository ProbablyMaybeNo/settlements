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
           scenario. CI [0.234, 0.453]. Superseded within the day: it was
           measured under an AI that never Sprinted and never took an objective
           Interact while it had a target.
  0.606    hold_claim only, 2026-08-13, AFTER the Sprint + objective-first policy
           fix. CI [0.436, 0.776]. REJECTS 0.3432 - outside its own successor's
           interval - and all four before it.

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

Priced on hold_claim alone the spread is tight and has STAYED tight across the
policy fix: 1.35x before it (0.292-0.396), 1.46x after (0.517-0.756). The 5x was almost
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
# Post Sprint + objective-first policy fix.
VALUE = 0.606
CI95 = (0.436, 0.776)
CELL_SPREAD = (0.517, 0.756)

# The scale choice. Pegging +1 Damage at this many Credits fixes the whole
# Credits scale; nothing measured it.
DAMAGE_CREDITS = 15

MEASURED = "gear-anchor-objective-n4000, 2026-08-13, post sprint + objective-first fix"

# THE HEAVIEST PROVISIONAL MARKING IN THE PROJECT, AND IT TRAVELS WITH THE NUMBER.
#
# 0.606 is the FIFTH value in a row to reject its predecessor, and every preceding
# error was invisible from inside the number the one before it produced:
#
#   1.150  -> rejected by 1.332   BalancedPolicy shot instead of advancing
#   1.332  -> rejected by 0.786   Annihilate averaged into a price
#   0.786  -> rejected by 0.3432  half its weight was `hold`, not a shipped scenario
#   0.3432 -> rejected by 0.606   the AI never Sprinted and never took an
#                                 objective Interact while it had a target
#
# Not one of those causes was detectable from the measurement that carried it.
# Every run was internally clean - paired estimator, tight CI, sane spread - and
# 1.150 even had two independent confirmations that were wrong together.
#
# THE BASE RATE FOR "THIS ANCHOR IS FINAL" IS 0 FOR 4. That is not a reason to
# doubt 0.606 specifically: it is the best-founded anchor this project has had,
# measured on the one scenario the ruleset actually contains, under an AI that
# now reaches the actions the rules assume. It is a reason it must never read as
# SETTLED because the previous four errors were found. Finding four does not
# imply finding all.
#
# THE SECOND DERIVATION EXISTS NOW, AND IT DOES NOT SETTLE THIS.
#
# two_route.py: rosters 0.606 vs probe chassis 0.712, gap 0.106 +- 0.164, AGREE
# (N=5000, both on hold_claim). Different crews, different chassis, same answer.
# That is the first real corroboration this project has produced and it is worth
# having.
#
# But the two routes share an ENGINE, a POLICY and SINGLE-SCENARIO COVERAGE. So
# it rules out derivation error in one path - a bad roster, a mis-specified
# probe, an estimator slip on one side. It does NOT touch the failure class that
# has actually bitten this project 4 times out of 4: a policy missing a legal
# action, or a scenario sample that does not represent the game. Both of those
# move both routes together, and the agreement would be exactly this tight if
# both were wrong. 1.150 had two independent confirmations for the same reason.
#
# INDEPENDENT-WITHIN-THE-SAME-INSTRUMENT IS NOT INDEPENDENT. The cross-check
# raises confidence in the arithmetic, not in the premises.
#
# Cite it with this caveat everywhere.
PROVISIONAL = (
    "COVERAGE-LIMITED - rests on 1 of 5 shipped scenarios, and the most static "
    "one. FIFTH value in a row to reject its predecessor; every one was "
    "internally clean. Mobility atoms may additionally read low (sprint "
    "overcorrection). Best-founded to date, not settled."
)

# WHAT IS STILL WRONG WITH 0.606, KNOWN AND UNFIXED.
#
# COVERAGE. It rests on 1 of 5 shipped scenarios, and the most static one:
#
#   Take a Hold    Control, VP accrual        MODELLED (this number)
#   Escort         Mobile, asymmetric         absent - blocked, nobody defends
#   Raid           Retrieve, enemy half       BUILT, passes verification
#   Sabotage       Timer, sudden death        BUILT, passes on 2 of 3 crews
#   Power Supply   Network, sudden death      absent
#
# Pricing the whole game against control play overvalues defensive and static
# atoms - range, damage, armour - and undervalues mobility, tempo, stealth and
# objective-running. Raid and Sabotage now work and can start correcting that.
#
# THE SPRINT OVERCORRECTION. The policy sprints across open ground where a
# slower advance would shoot, costing ~40-46% head-to-head in 3 of 9 cells.
# Accepted deliberately rather than fixed with an expected-value model. It is
# symmetric, so it skews no mirror - but MOBILITY-ADJACENT ATOMS MAY READ LOW.
#
# Expect this number to move again as coverage lands. Do not write Credits into
# any shipped table against it.

# Every price taken at an earlier anchor is low by these factors.
RESCALE_FROM_0786 = 1.2970    # the 50/50 blend
RESCALE_FROM_03432 = 1.7657   # hold_claim-only, but pre-policy-fix

RESCALE_FROM_1332 = 2.1980    # the mixed-scenario original


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

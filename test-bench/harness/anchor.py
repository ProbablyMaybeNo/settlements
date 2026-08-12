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
           advance fix. REJECTS ALL THREE historical candidates including the
           1.12 that the 1.150 run had endorsed.

The 1.150 run and an incidental 1.162 run agreed with each other and with 1.12,
and all of them were wrong for the same reason: BalancedPolicy shot instead of
advancing, so weapon range was negatively correlated with objective play and no
ranged crew ever reached an objective. Two independent confirmations of a number
that was wrong for a cause neither run could see.

THE SPREAD IS PART OF THE NUMBER. Per-cell values run 0.898 to 1.879 - roughly
2x from Fireteam/Hold to Armoured/Annihilate. That survived the policy fix and
widened slightly, so it is a real property of the game and not an artefact. A
flat scalar may be the wrong shape for this constant in the same way a flat
15/stat-point was the wrong shape for the stat ladder. Do not let the headline
figure travel without it.

The 15 Credits it is pegged to remains a CHOICE, not a measurement.
"""

from __future__ import annotations

# win-points per model buffed, +1 on the injury roll
VALUE = 1.332
CI95 = (1.202, 1.462)
CELL_SPREAD = (0.898, 1.879)

# The scale choice. Pegging +1 Damage at this many Credits fixes the whole
# Credits scale; nothing measured it.
DAMAGE_CREDITS = 15

MEASURED = "gear-anchor-paired-n4000, 2026-08-12, post-policy-fix"


def credits_per_winpoint() -> float:
    return DAMAGE_CREDITS / VALUE


def to_credits(wp: float) -> float:
    """Convert win-points per model into Credits at the current scale choice."""
    return wp * credits_per_winpoint()


def describe() -> str:
    lo, hi = CI95
    slo, shi = CELL_SPREAD
    return (f"anchor {VALUE:.3f} wp/model = {DAMAGE_CREDITS} Cr "
            f"(CI [{lo:.3f}, {hi:.3f}], per-cell {slo:.3f}..{shi:.3f}) "
            f"-> {credits_per_winpoint():.2f} Cr per win-point")

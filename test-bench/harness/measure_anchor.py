"""Settle the GEAR anchor: what is +1 Damage worth, in win-points per model?

WHY THIS RUN EXISTS
-------------------
Every Credits figure in this project is `win-points x CREDITS_PER_WINPOINT`, and
that constant is `15 / DMG_ANCHOR`. `DMG_ANCHOR = 1.12` is hardcoded at
balance/packet_battle.py:35 and attributed to "the anchor conditions2d.py
established on this engine" - but re-running conditions2d.py at N=1200 on the
merged engine returns **0.893**, and primitives2d's own figure is 0.90385.

If the anchor is 0.893 rather than 1.12, then CREDITS_PER_WINPOINT is 16.80 and
not 13.39, and every derived price rises 25% - T10's stat range moves from
16-34 Cr to 19.5-42 Cr, i.e. much further from the 15 currently charged.

conditions2d's mirror is unpaired, so at N=1200 its SE is ~0.10 wp/model and the
two candidates sit only ~2.3 SE apart. This run uses the paired estimator
(both arms on one seed, differenced per game), which removes the shared board
variance instead of summing it, and reports an explicit CI.

    py -3.13 measure_anchor.py [N]
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000

from crews import ARMOURED6, FIRETEAM6, SQUAD8  # noqa: E402

LISTS = {'Fireteam (6)': FIRETEAM6, 'Squad (8)': SQUAD8, 'Armoured (6)': ARMOURED6}
SCEN = ('hold', 'annihilate')

print("=" * 100)
print(f"GEAR ANCHOR — +1 Damage, paired mirror, N={N}/cell, sides swapped")
print("=" * 100)
print("Candidates on the table:  1.12 (packet_battle.py:35, hardcoded)")
print("                          1.1183 (ticks.py:18, 1D realistic.py)")
print("                          0.90385 (primitives2d, per anchor2d.py:167)")
print("                          0.893 (conditions2d.py re-run, N=1200, merged engine)")
print()
print(f"  {'list':<16}{'scenario':<13}{'delta':>10}{'SE':>7}{'/model':>9}{'95% CI':>18}{'sig':>5}")

rows = []
for lname, spec in LISTS.items():
    for scen in SCEN:
        r = M.measure(spec, E.damage_anchor(), scen, n=N)
        lo = r.per_applied - 1.96 * r.per_applied_se
        hi = r.per_applied + 1.96 * r.per_applied_se
        rows.append((lname, scen, r, lo, hi))
        print(f"  {lname:<16}{scen:<13}{r.delta:>+9.2f}{r.se:>7.2f}"
              f"{r.per_applied:>9.3f}   [{lo:+.3f}, {hi:+.3f}]"
              f"{'  yes' if r.significant else '   no':>5}")

per = [r.per_applied for _, _, r, _, _ in rows]
ses = [r.per_applied_se for _, _, r, _, _ in rows]
mean = statistics.fmean(per)
# Cells are independent runs, so the mean's SE is the pooled SE over cells.
pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled

print()
print(f"  ANCHOR  = {mean:.3f} win-points per model buffed   95% CI [{lo:.3f}, {hi:.3f}]")
print(f"  spread across cells: {min(per):.3f} .. {max(per):.3f}")
print()
print("  Consequences for the scale constant, if 15 Credits stays the GEAR peg:")
for cand, label in ((mean, "this run"), (1.12, "packet_battle.py"), (0.90385, "primitives2d")):
    print(f"    anchor {cand:.3f} ({label:<17}) -> CREDITS_PER_WINPOINT = {15/cand:5.2f}")
print()
for cand, label in ((1.12, "1.12  (packet_battle.py)"), (1.1183, "1.1183 (ticks.py 1D)"),
                    (0.90385, "0.90385 (primitives2d)")):
    verdict = "INSIDE the 95% CI" if lo <= cand <= hi else "OUTSIDE the 95% CI - rejected"
    print(f"    {label:<26} {verdict}")

env = P.Envelope(
    name=f"gear-anchor-paired-n{N}",
    question="What is +1 Damage worth in win-points per model? Adjudicates the 1.12 vs 0.90 "
            "scale-constant dispute that multiplies every Credits figure in the project.",
    values={"anchor_wp_per_model": round(mean, 4),
            "ci95_lo": round(lo, 4), "ci95_hi": round(hi, 4),
            "pooled_se": round(pooled, 4),
            "cells": {f"{l}/{s}": round(r.per_applied, 4) for l, s, r, _, _ in rows}},
    raw_cells=[{"list": l, "scenario": s, "delta": round(r.delta, 3),
                "se": round(r.se, 3), "per_applied": round(r.per_applied, 4),
                "n_applied": r.n_applied, "n_present": r.n_present,
                "significant": r.significant} for l, s, r, _, _ in rows],
    params={"N_per_cell": N, "method": "paired mirror, differenced per game on a shared seed",
            "lists": list(LISTS), "scenarios": list(SCEN)},
    caveats=[
        "Applies to melee AND ranged: injure() is reached from both fight() and shoot(), "
        "so unlike the payload traits this measurement carries no melee/ranged bias.",
        "Hold and Annihilate are reported per cell and then averaged for the headline; "
        "the per-cell spread is printed because averaging scenarios hides trait-by-scenario "
        "divergence (see T6).",
        "This fixes the win-points side only. The 15 Credits it is pegged to remains a "
        "CHOICE, not a measurement.",
    ],
)
out = env.write()
print(f"\n[stamped] {out.name}")

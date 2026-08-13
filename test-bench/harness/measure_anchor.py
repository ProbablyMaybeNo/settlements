"""Settle the GEAR anchor: what is +1 Damage worth, in win-points per model?

WHY THIS RUN EXISTS
-------------------
Every Credits figure in this project is `win-points x CREDITS_PER_WINPOINT`, and
that constant is `15 / DMG_ANCHOR`. So the anchor multiplies everything, and it
has now been wrong twice for two different reasons.

  1.12 / 1.1183 / 0.90385   pre-policy-fix candidates. All measured while
                            BalancedPolicy shot instead of advancing, so no
                            ranged crew ever reached an objective.
  1.332                     post-policy-fix, but priced across hold AND
                            annihilate. Superseded by THIS run, for the reason
                            below.

WHY THE 1.332 RUN IS SUPERSEDED
-------------------------------
Pricing moved to objective scenarios only (measure.PRICING_SCENARIOS): the
ruleset wins on objectives and never on kills, so Annihilate is a diagnostic
rather than a playable scenario, and a price averaged across it prices a game
nobody plays. That policy landed AFTER 1.332 was measured, and 1.332 is a
mixed-scenario figure.

That is not a cosmetic inconsistency. The anchor is the DENOMINATOR for every
atom now priced from objective cells only. Leaving it mixed means numerator and
denominator are drawn from different games, and the ratio between them describes
neither. The payload table already halved when its numerators moved to objective
pricing; some of that movement is real and some is the denominator failing to
move with it, and the two cannot be separated until this run lands.

Annihilate is still measured and still reported per cell. It never enters the
price.

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

from rosters import ARMOURED6, FIRETEAM6, SQUAD8  # noqa: E402

# PROVENANCE IS CAPTURED HERE, BEFORE THE MEASUREMENT RUNS, NOT AT THE END.
# Envelope's default_factory fields evaluate when the Envelope is CONSTRUCTED,
# which in every measure_* script is after the games have finished. An edit
# landing mid-run would therefore stamp a result with the fingerprint of code
# that never executed - the exact failure provenance.py was written to prevent,
# reintroduced by the order of operations. run_stamped.py already fingerprints up
# front; this script now does too. The remaining measure_* scripts do not yet.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

LISTS = {'Fireteam (6)': FIRETEAM6, 'Squad (8)': SQUAD8, 'Armoured (6)': ARMOURED6}

print("=" * 104)
print(f"GEAR ANCHOR — +1 Damage, paired mirror, N={N}/cell, sides swapped")
print("=" * 104)
print(f"Pricing scenarios: {', '.join(M.PRICING_SCENARIOS)}.  "
      f"{', '.join(M.DIAGNOSTIC_SCENARIOS)} is reported but never priced.")
print()
print("Superseded candidates:  1.332   (this harness, priced across hold+annihilate)")
print("                        1.12    (packet_battle.py:35, hardcoded, pre-policy-fix)")
print("                        1.1183  (ticks.py:18, 1D realistic.py)")
print("                        0.90385 (primitives2d, per anchor2d.py:167)")
print()
print(f"  {'list':<16}{'hold':>10}{'hold_claim':>12}{'annihilate':>12}"
      f"{'PRICE (obj)':>14}{'SE':>8}{'sig':>5}  dropped")

rows = []
for lname, spec in LISTS.items():
    res = M.price_atom(spec, E.damage_anchor(), n=N)

    def cell(s):
        c = res["cells"].get(s)
        return None if (c is None or c["degenerate"]) else c["wp"]

    def f(v):
        return f"{v:+.3f}" if v is not None else "   degen"

    dropped = ",".join(res["dropped_degenerate"]) or "-"
    price = res["price_wp"]
    print(f"  {lname:<16}{f(cell('hold')):>10}{f(cell('hold_claim')):>12}"
          f"{f(cell('annihilate')):>12}{f(price):>14}"
          f"{res.get('price_se', float('nan')):>8.3f}"
          f"{'  yes' if res['price_significant'] else '   no':>5}  {dropped}")
    rows.append((lname, res))

# The headline pools the per-list objective prices. A list whose objective cells
# were BOTH degenerate contributes nothing rather than contributing a zero.
priced = [(l, r) for l, r in rows if r["price_wp"] is not None]
if not priced:
    print("\n  NO LIST PRODUCED A PRICE — every objective cell degenerate. "
          "No anchor from this run.")
    sys.exit(1)

per = [r["price_wp"] for _, r in priced]
ses = [r["price_se"] for _, r in priced]
mean = statistics.fmean(per)
pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled

# The spread that decision #2 (flat scalar vs curve) turns on. Objective cells
# only, because those are the ones a price is now built from.
obj_cells = []
for lname, r in rows:
    for s in M.PRICING_SCENARIOS:
        c = r["cells"].get(s)
        if c and not c["degenerate"]:
            obj_cells.append((f"{lname}/{s}", c["wp"]))
spread_lo = min(v for _, v in obj_cells)
spread_hi = max(v for _, v in obj_cells)

# A MULTIPLICATIVE spread only means anything if every cell is above zero and on
# the same side of it. If any objective cell sits at or below zero, the atom does
# nothing (or hurts) in that cell, and "Nx spread" describes that badly - it
# reports a large ratio, or divides by zero, when the real finding is a cell where
# the anchor has no effect at all. That is a sharper input to the flat-vs-curve
# question than any ratio, so it is reported as its own line rather than folded in.
if spread_lo > 0:
    spread_note = f"{spread_hi / spread_lo:.2f}x across {len(obj_cells)} cells"
else:
    dead = [n for n, v in obj_cells if v <= 0]
    spread_note = (f"ratio undefined - {len(dead)} of {len(obj_cells)} objective cells "
                   f"at or below zero ({', '.join(dead)})")

print()
print(f"  ANCHOR  = {mean:.3f} win-points per model buffed   95% CI [{lo:.3f}, {hi:.3f}]")
print(f"  objective-cell spread: {spread_lo:.3f} .. {spread_hi:.3f}  ({spread_note})")
print(f"  CREDITS_PER_WINPOINT = {15 / mean:.2f}   (15 Cr peg unchanged, still a CHOICE)")
print()
print("  Effect on every price already taken at 1.332:")
print(f"    scale factor {1.332 / mean:.4f}x  "
      f"(a price of 19 Cr at 1.332 becomes {19 * 1.332 / mean:.1f} Cr here)")
print()
for cand, label in ((1.332, "1.332 (mixed-scenario)"), (1.12, "1.12  (packet_battle.py)"),
                    (1.1183, "1.1183 (ticks.py 1D)"), (0.90385, "0.90385 (primitives2d)")):
    verdict = "INSIDE the 95% CI" if lo <= cand <= hi else "OUTSIDE the 95% CI - rejected"
    print(f"    {label:<26} {verdict}")

env = P.Envelope(
    name=f"gear-anchor-objective-n{N}",
    question="What is +1 Damage worth in win-points per model, priced from OBJECTIVE "
            "scenarios only? Re-derives the denominator of every Credits figure in the "
            "project so it comes from the same game its numerators now do.",
    values={"anchor_wp_per_model": round(mean, 4),
            "ci95_lo": round(lo, 4), "ci95_hi": round(hi, 4),
            "pooled_se": round(pooled, 4),
            "credits_per_winpoint": round(15 / mean, 4),
            "objective_cell_spread": [round(spread_lo, 4), round(spread_hi, 4)],
            "objective_cell_spread_note": spread_note,
            "objective_cells": {n: round(v, 4) for n, v in obj_cells},
            "supersedes": {"value": 1.332, "why": "priced across hold+annihilate"},
            "rescale_factor_from_1332": round(1.332 / mean, 4),
            "cells": {f"{l}/{s}": (None if not c or c["degenerate"] else c["wp"])
                      for l, r in rows for s, c in r["cells"].items()}},
    raw_cells=[{"list": l, **r} for l, r in rows],
    params={"N_per_cell": N, "method": "paired mirror, differenced per game on a shared seed",
            "lists": list(LISTS),
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS)},
    caveats=[
        "Applies to melee AND ranged: injure() is reached from both fight() and shoot(), "
        "so unlike the payload traits this measurement carries no melee/ranged bias.",
        "Annihilate is measured and reported per cell but NEVER priced. The ruleset wins "
        "on objectives and never on kills, so a price averaged across it prices a game "
        "nobody plays.",
        "This fixes the win-points side only. The 15 Credits it is pegged to remains a "
        "CHOICE, not a measurement.",
        "The objective-cell spread is printed because a flat scalar may be the wrong SHAPE "
        "for this constant, exactly as a flat 15/stat-point was wrong for the stat ladder. "
        "That ruling is deliberately NOT taken on this evidence: terrain density is a "
        "66-point lever in the ruleset, larger than any atom measured so far, and it is "
        "expected to move this spread. Ruling on scenario-spread alone would fix one "
        "variable while a bigger untested one sits open. Held until the density sweep.",
        "policies.py still carries fixed action priorities beyond the advance fix - no "
        "kiting, no focusing a slowed target, unconditional Pinned-clearing. This is the "
        "best estimate under a LESS WRONG AI, not a provably right one.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")
print(f"[provenance] fingerprinted BEFORE the run: engine {ENGINE_AT_START['combined']}")

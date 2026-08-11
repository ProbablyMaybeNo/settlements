"""What is Pinned worth? The missing baseline under every ranged payload price.

THE PROBLEM THIS SOLVES
-----------------------
Rules §10: a payload lands IN PLACE OF the normal non-wound result, never in
addition. On a ranged hit that normal result is **Pinned**. So a ranged payload's
true worth is not what the condition does — it is:

        value(condition)  -  value(Pinned)

Every measured payload price in this project is that difference, and nobody has
ever measured the subtrahend. Which means "Concussive measures at zero" has two
completely different readings that no existing number can tell apart:

  (a) Off-Balance is a feeble condition worth nothing        -> a pricing problem
  (b) Off-Balance is worth about what Pinned is worth, and   -> a DESIGN problem:
      replaces it, so the swap is a wash                        the trait is
                                                                redundant, not weak

(a) says reprice. (b) says the trait should not exist in its current form, at any
price — and no amount of repricing fixes it. The distinction decides what happens
to Concussive and Crippling regardless of what number comes out.

METHOD. A `null_payload` trait suppresses the ordinary ranged result and applies
nothing in its place (engine.apply_payload, 'none' branch). Mirroring a crew
carrying it against the identical crew without it measures the loss of Pinned
directly:

        delta(null_payload)  =  -value(Pinned)

Melee carriers are excluded from the divisor: a melee non-wound is Shaken, not
Pinned, so there is no Pinned there to remove.

    py -3.13 measure_pinned.py [N]
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from crews import ARMOURED6, FIRETEAM6, SQUAD8  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
ANCHOR = 1.150  # win-points per model, measure_anchor.py, CI [1.022, 1.278]

LISTS = {"Fireteam (6)": FIRETEAM6, "Squad (8)": SQUAD8, "Armoured (6)": ARMOURED6}
SCEN = ("hold", "annihilate")

print("=" * 100)
print(f"VALUE OF PINNED — via a null payload that suppresses it, N={N}/cell")
print("=" * 100)
print("A ranged payload REPLACES Pinned, so every payload price on record is")
print("value(condition) - value(Pinned), and the subtrahend has never been measured.")
print()
print(f"  {'list':<16}{'scenario':<13}{'delta':>9}{'SE':>7}{'/applied':>10}{'95% CI':>18}{'sig':>5}")

# ranged-only: a melee non-wound is Shaken, so there is no Pinned to suppress
eff = E.Effect(kind="weapon_trait", trait="null_payload", require_ranged=True,
               name="null payload (suppresses Pinned)")

rows = []
for lname, spec in LISTS.items():
    for scen in SCEN:
        r = M.measure(spec, eff, scen, n=N)
        lo = r.per_applied - 1.96 * r.per_applied_se
        hi = r.per_applied + 1.96 * r.per_applied_se
        rows.append((lname, scen, r, lo, hi))
        print(f"  {lname:<16}{scen:<13}{r.delta:>+8.2f}{r.se:>7.2f}{r.per_applied:>10.3f}"
              f"   [{lo:+.3f}, {hi:+.3f}]{'  yes' if r.significant else '   no':>5}")

per = [r.per_applied for _, _, r, _, _ in rows]
ses = [r.per_applied_se for _, _, r, _, _ in rows]
mean = statistics.fmean(per)
pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled

pinned_wp = -mean
pinned_lo, pinned_hi = -hi, -lo

print()
print(f"  removing Pinned is worth {mean:+.3f} wp/model  ->  value(Pinned) = {pinned_wp:+.3f}")
print(f"  95% CI on value(Pinned): [{pinned_lo:+.3f}, {pinned_hi:+.3f}] wp/model")
print(f"  at the GEAR anchor ({ANCHOR:.3f} wp = 15 Cr): "
      f"Pinned ~ {pinned_wp / ANCHOR * 15:.1f} Cr "
      f"[{pinned_lo / ANCHOR * 15:.1f}, {pinned_hi / ANCHOR * 15:.1f}]")
print()

significant = abs(mean) > 1.96 * pooled
if not significant:
    print("  READING: value(Pinned) is INDISTINGUISHABLE FROM ZERO.")
    print("  Then the replaces-Pinned rule costs a ranged payload almost nothing, the")
    print("  measured payload prices are close to the conditions' own worth, and")
    print("  Concussive/Crippling really are feeble — reading (a), a pricing problem.")
else:
    print("  READING: Pinned carries real value, so every measured ranged payload price")
    print("  is NET of it. A payload measuring ~0 is worth ABOUT WHAT PINNED IS WORTH —")
    print("  reading (b): those traits are REDUNDANT, not weak. Repricing cannot fix a")
    print("  trait whose whole effect is to swap one result for an equal one.")
    print(f"  On that reading, Concussive/Crippling's gross worth is ~{pinned_wp:.3f} wp/model")
    print(f"  (~{pinned_wp / ANCHOR * 15:.0f} Cr) and their NET worth is the ~0 already measured.")

env = P.Envelope(
    name=f"value-of-pinned-n{N}",
    question="What is Pinned worth? It is the baseline every ranged payload price is "
            "quoted against, and it decides whether Concussive/Crippling are underpriced "
            "or redundant with the free default result.",
    values={"pinned_wp_per_model": round(pinned_wp, 4),
            "ci95_lo": round(pinned_lo, 4), "ci95_hi": round(pinned_hi, 4),
            "significant": significant,
            "anchor_used": ANCHOR,
            "cells": {f"{l}/{s}": round(-r.per_applied, 4) for l, s, r, _, _ in rows}},
    raw_cells=[{"list": l, "scenario": s, "delta": round(r.delta, 3), "se": round(r.se, 3),
                "per_applied": round(r.per_applied, 4), "n_applied": r.n_applied,
                "n_present": r.n_present, "significant": r.significant}
               for l, s, r, _, _ in rows],
    params={"N_per_cell": N, "method": "paired mirror vs a null-payload variant",
            "divisor": "ranged carriers only - a melee non-wound is Shaken, not Pinned"},
    caveats=[
        "Measured on this engine's AI, which never spends a Move to clear Pinned "
        "(clear_movement_condition is called by no policy). Pinned IS cleared by "
        "clear_pin() in every policy, so unlike Hobbled this is not a permanent-condition "
        "artefact - but the AI clears it immediately and unconditionally, which is a "
        "lower bound on a player who would sometimes shoot from where they stand.",
        "Suppressive is excluded: it modifies what clearing Pinned costs, so it is a "
        "second-order effect on this same baseline and must be measured after it.",
    ],
)
out = env.write()
print(f"\n[stamped] {out.name}")

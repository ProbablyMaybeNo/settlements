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

# IMPORT GUARD. This file is a SCRIPT: it runs its whole measurement at module
# level. `import measure_x` therefore executes a full sweep as a side effect -
# which happened TWICE in one session, once silently writing an artefact from a
# known-broken board ladder that then passed every provenance check.
#
# Deliberately a loud raise rather than the usual `if __name__ == "__main__":`
# wrapper. The wrapper makes an accidental import a silent no-op; this says why
# nothing happened. The failure being guarded is a silent one, so the guard is
# not silent.
if __name__ != "__main__":
    raise RuntimeError(
        f"{__name__} is a script, not a module - importing it would run its entire "
        "measurement as a side effect. Run it with `py -3.13 <file>.py` instead, or "
        "move the helper you wanted into a module."
    )

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6, SQUAD8  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
import anchor as A  # noqa: E402
ANCHOR = A.VALUE

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

LISTS = {"Fireteam (6)": FIRETEAM6, "Squad (8)": SQUAD8, "Armoured (6)": ARMOURED6}

print("=" * 108)
print(f"VALUE OF PINNED — via a null payload that suppresses it, N={N}/cell")
print("=" * 108)
print("A ranged payload REPLACES Pinned, so every payload price on record is")
print("value(condition) - value(Pinned), and the subtrahend has never been measured.")
print(A.describe())
print()
print(f"  {'list':<16}{'hold':>10}{'hold_claim':>12}{'annihilate':>12}"
      f"{'PRICE (obj)':>14}{'SE':>8}{'sig':>5}  dropped")

# ranged-only: a melee non-wound is Shaken, so there is no Pinned to suppress
eff = E.Effect(kind="weapon_trait", trait="null_payload", require_ranged=True,
               name="null payload (suppresses Pinned)")

rows = []
for lname, spec in LISTS.items():
    res = M.price_atom(spec, eff, n=N)

    def cell(s):
        c = res["cells"].get(s)
        return None if (c is None or c["degenerate"]) else c["wp"]

    def f(v):
        return f"{v:+.3f}" if v is not None else "   degen"

    rows.append((lname, res))
    print(f"  {lname:<16}{f(cell('hold')):>10}{f(cell('hold_claim')):>12}"
          f"{f(cell('annihilate')):>12}{f(res['price_wp']):>14}"
          f"{res.get('price_se', float('nan')):>8.3f}"
          f"{'  yes' if res['price_significant'] else '   no':>5}  "
          f"{','.join(res['dropped_degenerate']) or '-'}")

priced = [r for _, r in rows if r["price_wp"] is not None]
if not priced:
    print("\n  NO LIST PRODUCED A PRICE — every objective cell degenerate.")
    sys.exit(1)
per = [r["price_wp"] for r in priced]
ses = [r["price_se"] for r in priced]
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
    print("  reading (b): such a trait is REDUNDANT, not weak. Repricing cannot fix a")
    print("  trait whose whole effect is to swap one result for an equal one.")
    print(f"  Gross worth of a net-zero trait is therefore ~{pinned_wp:.3f} wp/model "
          f"(~{pinned_wp / ANCHOR * 15:.0f} Cr).")
    # NAMED TRAITS DELIBERATELY REMOVED FROM THIS PARAGRAPH, 2026-08-13.
    # It used to end "...Concussive/Crippling's NET worth is the ~0 already
    # measured", which was true when written and stopped being true the moment
    # the payload table was re-run: post-policy-fix they read -0.592 and -0.613,
    # SIGNIFICANTLY NEGATIVE, not ~0. A hardcoded narrative naming another
    # script's numbers cannot go stale visibly - it prints with full confidence
    # from a run that never measured the thing it is describing. The general
    # relation (net = gross - value(Pinned)) belongs here; which traits currently
    # sit at zero belongs to the payload table, and is read from there.
    print("  WHICH traits currently sit at ~0 is the payload table's question, not")
    print("  this one's — read it from payload-table-objective, not from here.")

env = P.Envelope(
    name=f"value-of-pinned-n{N}",
    question="What is Pinned worth? It is the baseline every ranged payload price is "
            "quoted against, and it decides whether Concussive/Crippling are underpriced "
            "or redundant with the free default result.",
    values={"pinned_wp_per_model": round(pinned_wp, 4),
            "ci95_lo": round(pinned_lo, 4), "ci95_hi": round(pinned_hi, 4),
            "significant": significant,
            "anchor_used": ANCHOR,
            "anchor_provisional": A.PROVISIONAL,
            # Sign flipped: the effect SUPPRESSES Pinned, so value(Pinned) is the
            # negative of what removing it is worth.
            "cells": {f"{lname}/{s}": (None if not c or c["degenerate"] else round(-c["wp"], 4))
                      for lname, res in rows for s, c in res["cells"].items()}},
    raw_cells=[{"list": lname, **res} for lname, res in rows],
    params={"N_per_cell": N, "method": "paired mirror vs a null-payload variant",
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            "divisor": "ranged carriers only - a melee non-wound is Shaken, not Pinned"},
    caveats=[
        "Priced from OBJECTIVE scenarios only. Supersedes value-of-pinned-n4000, which "
        "averaged Annihilate in - and Pinned is the atom whose sign-split ACROSS that "
        "boundary is what forced the objective-only policy in the first place.",
        "Measured on this engine's AI, which never spends a Move to clear Pinned "
        "(clear_movement_condition is called by no policy). Pinned IS cleared by "
        "clear_pin() in every policy, so unlike Hobbled this is not a permanent-condition "
        "artefact - but the AI clears it immediately and unconditionally, which is a "
        "lower bound on a player who would sometimes shoot from where they stand.",
        "Suppressive is excluded: it modifies what clearing Pinned costs, so it is a "
        "second-order effect on this same baseline and must be measured after it.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

"""Is a stat point one price, or does the rung decide? Measure every rung.

THE PROBLEM
-----------
The whole BODY scale is `20 + stat_points x 15 + orders`, a flat 15 per point.
The only evidence on the shape says flat is wrong: on one fighter, the same DEX
buff measured 0.46 / 3.24 / 4.24 win-points for +1 / +2 / +4
(results/packet_battle-n2000.txt:23-25) — a 6x spread across rungs of the SAME
stat on the SAME model. Three separate "the stat point is worth X" values exist
in project history (15, 25, 16-34) and they are not three estimates of one
quantity; they are estimates of different rungs on different carriers.

So this does not measure "a stat point". It measures rung r -> r+1, separately,
on a crew built so every model sits exactly on that rung.

TWO STATS, DELIBERATELY, BECAUSE THEY ARE DIFFERENT OBJECTS
  DEX is ONE-SIDED: it modifies only the shooter's own hit roll, and cover
      subtracts from it directly, so its ladder is truncated by the 10-90% floor
      and ceiling of the core test.
  STR is OPPOSED ON ITSELF: `opposed(att.str, dfn.str)` reads the same stat on
      both sides (engine.py fight), so one point buys an attack step AND a
      defence step. It never saturates the way a one-sided modifier does.
That structural difference is the likely reason STR measured ~2x DEX, and it is
a reason they cannot share a price, let alone a flat one.

    py -3.13 measure_stat_ladder.py [N]
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

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
import anchor as _anchor  # noqa: E402
ANCHOR = _anchor.VALUE

# Fingerprinted BEFORE the games run. Envelope's default_factory fields evaluate
# at CONSTRUCTION, which is after the run, so an edit landing mid-run would stamp
# a result with code that never executed.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()
RUNGS = (0, 1, 2, 3, 4, 5)   # measuring r -> r+1, so 0->1 .. 5->6


from rosters import uniform as uniform_crew  # noqa: E402


CASES = [
    ("DEX (one-sided, rifle)", "dex", "rifle"),
    ("STR (opposed, sledge)", "str", "sledge"),
]

print("=" * 104)
print(f"STAT LADDER — every rung measured separately, N={N}/cell, paired mirror")
print("=" * 104)
print(f"anchor {ANCHOR:.3f} wp/model = 15 Cr   |   charged today: a flat 15 per point, every rung")
print()

all_rows = []
for label, stat, weapon in CASES:
    print(f"  {label}")
    print(f"    {'rung':<10}{'hold_clm':>10}{'(hold)':>9}{'(annih)':>9}{'PRICE':>9}{'SE':>7}"
          f"{'95% CI':>18}{'Cr':>6}{'vs 15':>8}  sig")
    for r in RUNGS:
        spec = uniform_crew(stat, r, weapon)
        eff = E.stat_rung(stat, 1)
        # PRICED THROUGH price_atom LIKE EVERY OTHER SCRIPT — fixed 2026-08-13.
        #
        # This loop used to read `for scen in ("hold", "annihilate")` and average
        # the two, which is BOTH rulings this project has already made, still live
        # in one file: `annihilate` is a kill scenario and the ruleset wins on
        # objectives (the objective-only cut, 09c4462), and `hold` scores
        # positionally and models no shipped scenario (dropped, 6a54c6b). Neither
        # ruling reached here, because this script never routed through
        # price_atom() and so inherited nothing when PRICING_SCENARIOS moved.
        #
        # The stored artefact was correctly marked VOID on both counts — and that
        # was not enough, because RE-RUNNING IT REPRODUCED THE VOID BASIS. A
        # policy that lives in a constant only protects the callers that read the
        # constant. Both scenarios are kept as DIAGNOSTICS so the sign-split
        # detector still sees them; they no longer enter the price.
        res = M.price_atom(spec, eff, n=N)
        wp = res["price_wp"]

        def _c(s, _r=res):
            c = _r["cells"].get(s)
            return "    degen" if (c is None or c["degenerate"]) else f"{c['wp']:+.3f}"

        if wp is None:
            print(f"    {f'{r}->{r+1}':<10}  ALL OBJECTIVE CELLS DEGENERATE - no price")
            all_rows.append({"stat": stat, "weapon": weapon, "rung": f"{r}->{r+1}",
                             "wp": None, "significant": False,
                             "per_scenario": {s: c["wp"] for s, c in res["cells"].items()},
                             "scenarios_used": [],
                             "scenarios_excluded_degenerate": res["dropped_degenerate"]})
            continue
        se = res["price_se"]
        lo, hi = res["price_ci"]
        cr = wp / ANCHOR * 15
        sig = res["price_significant"]
        all_rows.append({"stat": stat, "weapon": weapon, "rung": f"{r}->{r+1}",
                         "per_scenario": {s: c["wp"] for s, c in res["cells"].items()},
                         "wp": wp, "se": se, "ci": [lo, hi],
                         "credits": round(cr, 1), "significant": sig,
                         "sign_split": res["sign_split"],
                         "scenarios_used": res["priced_from"],
                         "scenarios_excluded_degenerate": res["dropped_degenerate"]})
        print(f"    {f'{r}->{r+1}':<10}{_c('hold_claim'):>10}{_c('hold'):>9}{_c('annihilate'):>9}"
              f"{wp:>+9.3f}{se:>7.3f}"
              f"  [{lo:+.3f}, {hi:+.3f}]{cr:>6.0f}{cr - 15:>+8.0f}  {'yes' if sig else ' no'}"
              f"{'   SIGN-SPLIT' if res['sign_split'] else ''}")
    print()

print("  A flat price is only correct if these rows are flat. Read the spread, not the mean.")
for stat in ("dex", "str"):
    rows = [r for r in all_rows if r["stat"] == stat and r["significant"]]
    if len(rows) >= 2:
        lo = min(rows, key=lambda r: r["wp"])
        hi = max(rows, key=lambda r: r["wp"])
        ratio = hi["wp"] / lo["wp"] if lo["wp"] else float("inf")
        print(f"    {stat.upper()}: cheapest significant rung {lo['rung']} at {lo['credits']:.0f} Cr, "
              f"dearest {hi['rung']} at {hi['credits']:.0f} Cr  ->  {ratio:.1f}x spread")

env = P.Envelope(
    name=f"stat-ladder-n{N}",
    question="Is a stat point one price, or does the rung decide? Measures r->r+1 for "
            "every rung 0..6 on a crew built entirely on that rung, for a one-sided stat "
            "(DEX) and an opposed one (STR).",
    values={f"{r['stat']}:{r['rung']}": r["wp"] for r in all_rows},
    raw_cells=all_rows,
    params={"N_per_cell": N, "anchor_wp_per_model": ANCHOR, "rungs": list(RUNGS),
            "crew": "6 uniform models, ranks Leader/Specialist/Fighter x2/Recruit x2",
            "method": "paired mirror, differenced per game on a shared seed"},
    caveats=[
        "AGI is deliberately absent: it is read only inside the Dodge reaction and "
        "DODGE_ON defaults False, so an AGI rung measures exactly zero by construction. "
        "Measuring it requires DODGE_ON=True, which changes every other number too.",
        "INT is absent for the same class of reason: it is read by the claim test, so its "
        "value is zero in any scenario without a claim step and must be booked against the "
        "SCENARIO MIX rather than against the fighter.",
        "A uniform crew is not a real crew. It isolates the rung, which is the point, but "
        "a real fighter's rungs interact with its own other stats and its weapon.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

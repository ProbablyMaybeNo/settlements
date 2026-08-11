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
ANCHOR = 1.150
RUNGS = (0, 1, 2, 3, 4, 5)   # measuring r -> r+1, so 0->1 .. 5->6


from crews import uniform as uniform_crew  # noqa: E402


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
    print(f"    {'rung':<10}{'hold':>9}{'annih':>9}{'mean wp':>10}{'SE':>7}"
          f"{'95% CI':>18}{'Cr':>6}{'vs 15':>8}  sig")
    for r in RUNGS:
        spec = uniform_crew(stat, r, weapon)
        eff = E.stat_rung(stat, 1)
        cells = []
        for scen in ("hold", "annihilate"):
            cells.append(M.measure(spec, eff, scen, n=N))
        # Exclude any scenario that cannot resolve for this crew. A uniform rifle
        # crew draws 100% of Hold games, so including it halves the result.
        live = [c for c in cells if not c.degenerate]
        dead = [c for c in cells if c.degenerate]
        if not live:
            print(f"    {f'{r}->{r+1}':<10}  ALL SCENARIOS DEGENERATE - no measurement possible")
            continue
        per = [c.per_applied for c in live]
        ses = [c.per_applied_se for c in live]
        mean = statistics.fmean(per)
        pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
        lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled
        cr = mean / ANCHOR * 15
        sig = abs(mean) > 1.96 * pooled
        # Key by the cell's own scenario name. Indexing per[] positionally would
        # mislabel the moment a degenerate scenario is dropped from the list.
        by_scen = {c.scenario: (None if c.degenerate else round(c.per_applied, 4))
                   for c in cells}
        all_rows.append({"stat": stat, "weapon": weapon, "rung": f"{r}->{r+1}",
                         "per_scenario": by_scen,
                         "wp": round(mean, 4), "se": round(pooled, 4),
                         "ci": [round(lo, 4), round(hi, 4)],
                         "credits": round(cr, 1), "significant": sig,
                         "scenarios_used": [c.scenario for c in live],
                         "scenarios_excluded_degenerate": [c.scenario for c in dead],
                         "draw_rates": {c.scenario: round(c.draw_rate, 3) for c in cells}})
        h = f"{cells[0].per_applied:+.3f}" if not cells[0].degenerate else "  drawn"
        a = f"{cells[1].per_applied:+.3f}" if not cells[1].degenerate else "  drawn"
        print(f"    {f'{r}->{r+1}':<10}{h:>9}{a:>9}{mean:>+10.3f}{pooled:>7.3f}"
              f"  [{lo:+.3f}, {hi:+.3f}]{cr:>6.0f}{cr - 15:>+8.0f}  {'yes' if sig else ' no'}"
              f"{'   (' + str(len(dead)) + ' scenario excluded)' if dead else ''}")
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
)
out = env.write()
print(f"\n[stamped] {out.name}")

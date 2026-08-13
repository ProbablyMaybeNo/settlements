"""AUDIT: what was concluded from "all-ranged crews cannot score on hold_claim"?

WHY THIS RUNS BEFORE COVERAGE RESUMES
-------------------------------------
That behaviour was treated as a PROPERTY OF THE GAME. A guard was built to
exclude those cells as legitimately degenerate, rosters were designed around it,
and at least one measurement was priced from a single scenario because of it.

It was never a property. It was two missed legal actions - the AI never sprinted,
and it never took an objective Interact while it had a target - and with both
fixed a uniform rifle crew on hold_claim goes from 99.3% draws at 0.00 VP to
30.3% draws at 1.24 VP.

"We treated a bug as a property of the game" is the most expensive error class in
this rebuild, so every conclusion that rested on it is re-examined here rather
than rediscovered later.

WHAT THIS CHECKS
  1. Which stored artefacts actually dropped cells as degenerate.
  2. Whether each of those configurations still degenerates post-fix.
  3. The guard's own stated MECHANISM, which is a separate error from the
     threshold: the comment attributes the draws to crews sitting on their own
     objectives unable to displace each other. That is not what was happening.

    py -3.13 audit_degeneracy.py [N]
"""

from __future__ import annotations

# IMPORT GUARD - see the note in any measure_*.py.
if __name__ != "__main__":
    raise RuntimeError(f"{__name__} is a script, not a module.")

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6, MIXED6, SQUAD8, uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

print("=" * 112)
print(f"DEGENERACY AUDIT — what rested on 'all-ranged crews cannot score'? N={N}/cell")
print("=" * 112)
print()

# --- 1. which stored artefacts dropped cells? -------------------------------
print("  1. STORED ARTEFACTS THAT DROPPED CELLS AS DEGENERATE")
hits = []
for p in sorted(P.RESULTS.glob("*.json")):
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        continue
    found = []

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("dropped_degenerate", "scenarios_degenerate",
                         "scenarios_excluded_degenerate") and v:
                    found.append((path or "root", list(v) if isinstance(v, list) else v))
                elif k == "degenerate" and v is True:
                    found.append((path or "root", "degenerate=True"))
                else:
                    walk(v, f"{path}.{k}" if path else k)
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, f"{path}[{i}]")

    walk(d)
    if found:
        hits.append((p.name, found))
        print(f"     {p.name[:70]}")
        for where, what in found[:4]:
            print(f"        {where[:56]:<58}{what}")
        if len(found) > 4:
            print(f"        ... and {len(found) - 4} more")
print(f"     -> {len(hits)} artefact(s) carry dropped/degenerate cells")

# --- 2. do those configurations still degenerate? ---------------------------
print()
print("  2. DO THOSE CONFIGURATIONS STILL DEGENERATE? (post sprint + objective-first)")
print(f"     {'crew':<24}{'scenario':<12}{'draw':>8}{'degenerate?':>13}{'wp':>9}  was")

# The configurations that were excluded, reconstructed. The uniform ranged crews
# are the ones the guard's comment named explicitly.
CONFIGS = [
    ("uniform rifle (6)", uniform("dex", 2, "rifle", 6), "hold_claim", "DROPPED"),
    ("uniform rifle (6)", uniform("dex", 2, "rifle", 6), "hold", "DROPPED"),
    ("uniform pistol (6)", uniform("dex", 2, "pistol", 6), "hold_claim", "DROPPED"),
    ("probe chassis d1 (6)", uniform("dex", 2, "rifle", 6), "hold_claim", "DROPPED"),
    ("Fireteam (6)", FIRETEAM6, "hold_claim", "kept"),
    ("Squad (8)", SQUAD8, "hold_claim", "kept"),
    ("Armoured (6)", ARMOURED6, "hold_claim", "kept"),
    ("Mixed (6)", MIXED6, "hold_claim", "kept"),
]
rows = []
for label, spec, scen, was in CONFIGS:
    r = M.measure(spec, E.damage_anchor(), scen, n=N)
    rows.append({"crew": label, "scenario": scen, "was": was,
                 "draw_rate": r.draw_rate, "degenerate": r.degenerate,
                 "wp": r.per_applied, "significant": r.significant})
    flag = "STILL DEGEN" if r.degenerate else "resolves"
    print(f"     {label:<24}{scen:<12}{r.draw_rate:>7.1%}{flag:>13}"
          f"{r.per_applied:>+9.3f}  {was}")

recovered = [r for r in rows if r["was"] == "DROPPED" and not r["degenerate"]]
still = [r for r in rows if r["was"] == "DROPPED" and r["degenerate"]]

print()
print(f"     RECOVERED (were dropped, now resolve): {len(recovered)}")
for r in recovered:
    print(f"        {r['crew']:<24}{r['scenario']:<12}"
          f"{r['wp']:+.3f} wp  ({'significant' if r['significant'] else 'n.s.'})")
print(f"     STILL DEGENERATE: {len(still)}")
for r in still:
    print(f"        {r['crew']:<24}{r['scenario']:<12}{r['draw_rate']:.1%} draws")

# --- 3. the guard's stated mechanism ----------------------------------------
print()
print("  3. THE GUARD'S STATED MECHANISM IS A SEPARATE ERROR FROM ITS THRESHOLD")
print("     measure.py's guard comment reads: 'a uniform RIFLE crew mirror draws 100%")
print("     of Hold games - both sides sit on their own objectives and neither can")
print("     displace the other'.")
print()
print("     That mechanism is WRONG. The crews were not sitting on their own objectives")
print("     unable to displace each other - they were never REACHING an objective and")
print("     never CLAIMING one. Measured directly at the time: mean distance from goal at")
print("     game end rose monotonically with weapon range (melee 2.49\", rifle 7.37\",")
print("     24\" gun 9.30\") against a 3\" radius, and the claim count was 0.00.")
print()
print("     The THRESHOLD (draw_rate >= 0.95) is behaviourally fine and stays - it fires")
print("     on any cell that cannot resolve, whatever the cause. What was wrong was the")
print("     EXPLANATION, and the explanation is what licensed treating those cells as a")
print("     property of the game rather than a symptom to investigate.")

env = P.Envelope(
    name=f"degeneracy-audit-n{N}",
    question="What was concluded from 'all-ranged crews cannot score on hold_claim', and "
            "does any of it survive the sprint + objective-first fixes? The behaviour was "
            "treated as a property of the game and used to exclude cells, design rosters "
            "and price an atom from a single scenario.",
    values={"artefacts_with_dropped_cells": [h[0] for h in hits],
            "recovered": [{k: r[k] for k in ("crew", "scenario", "wp", "significant")}
                          for r in recovered],
            "still_degenerate": [{k: r[k] for k in ("crew", "scenario", "draw_rate")}
                                 for r in still]},
    raw_cells=rows,
    params={"N_per_cell": N, "guard_threshold": "draw_rate >= 0.95",
            "fixes_applied": ["sprint when goal beyond mov+IN_POSITION",
                              "objective Interact before shooting"]},
    caveats=[
        "The guard THRESHOLD is not the defect and is unchanged. The defect was its stated "
        "MECHANISM, and the conclusions that mechanism licensed.",
        "Recovered cells are NOT retro-fitted into old results. Every pre-fix measurement is "
        "void on its own terms; this audit says which CONCLUSIONS need re-examining, not "
        "which numbers can be salvaged.",
        "Measured under the sprint overcorrection (accepted residual): mobility-adjacent "
        "atoms may read low on Raid specifically.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

"""WHY don't Sabotage and Raid arrive? Quantify only - no policy is changed.

HYPOTHESIS. BalancedPolicy moves a gunner `u.mov` toward its goal but moves a
MELEE model `2 * u.mov` (policies.py, reposition branch). So gunners never
sprint. On Take-a-Hold the goal is ~15" away and a 6"/round crawl arrives inside
6 rounds; Sabotage and Raid put the goal in the ENEMY'S half, ~24" away and
behind the enemy crew, and the crawl does not.

If the hypothesis holds, a PURE MELEE crew - which takes the sprinting branch -
should arrive markedly closer on exactly the same boards and scenarios.

This is the same defect SHAPE as the advance/shoot bug: a capability the policy
has, applied in one branch and not another, which silently makes a whole class of
scenario unplayable. Per batch instruction it is measured and reported, NOT fixed.

    py -3.13 diag_arrival.py [N]
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

import random
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import dist, take_a_hold  # noqa: E402
from rosters import uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 400

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

# bat = melee (rng 0) -> takes the 2*mov sprint branch.
# rifle/pistol = ranged -> take the 1*mov branch.
CREWS = {
    "melee (bat)": uniform("str", 2, "bat", 6),
    "ranged (rifle)": uniform("dex", 2, "rifle", 6),
    "ranged (pistol)": uniform("dex", 2, "pistol", 6),
}
SCENS = ("hold_claim", "sabotage", "raid")


def run(scen, spec, n, seed=20260813):
    GameCls, kw = M.SCENARIOS[scen]
    random.seed(seed)
    dists, inters, wins = [], [], Counter()
    start = []
    for _ in range(n):
        ca, _ = M.build(spec, 0)
        cb, _ = M.build(spec, 1)
        g = GameCls(ca, cb, take_a_hold(), **kw)
        g._spawn()
        # how far the goal is at deployment, before anyone moves
        start += [dist(u.pos, u.goal) for u in g.units if getattr(u, "goal", None)]
        r = g.play()
        wins[r["winner"]] += 1
        for side in (0, 1):
            for u in g._standing(side):
                if getattr(u, "goal", None):
                    dists.append(dist(u.pos, u.goal))
        if scen == "sabotage":
            inters.append(sum(1 for s in (0, 1) if g.charge[s] is not None))
        elif scen == "raid":
            inters.append(len(g.looted[0]) + len(g.looted[1]))
        else:
            inters.append(sum(1 for v in g.claims.values() if v is not None))
    return {
        "start_dist": statistics.fmean(start) if start else None,
        "end_dist": statistics.fmean(dists) if dists else None,
        "closed": (statistics.fmean(start) - statistics.fmean(dists)) if dists and start else None,
        "interactions": statistics.fmean(inters),
        "draw_rate": wins["draw"] / float(n),
    }


print("=" * 108)
print(f"ARRIVAL DIAGNOSTIC — does the sprint branch explain non-arrival? N={N}/cell")
print("=" * 108)
print("BalancedPolicy moves gunners u.mov and melee 2*u.mov toward the goal.")
print("Quantify only. No policy change in this batch.")
print()
print(f"  {'scenario':<12}{'crew':<18}{'goal @start':>12}{'@end':>8}{'closed':>9}"
      f"{'inter':>8}{'draw':>8}")

rows = []
for scen in SCENS:
    for cname, spec in CREWS.items():
        r = run(scen, spec, N)
        r["scenario"], r["crew"] = scen, cname
        rows.append(r)
        print(f"  {scen:<12}{cname:<18}{r['start_dist']:>12.2f}{r['end_dist']:>8.2f}"
              f"{r['closed']:>9.2f}{r['interactions']:>8.2f}{r['draw_rate']:>8.1%}")
    print()

print("=" * 108)
print("READING")
print("=" * 108)
for scen in SCENS:
    rs = {r["crew"]: r for r in rows if r["scenario"] == scen}
    m, g = rs.get("melee (bat)"), rs.get("ranged (rifle)")
    if m and g:
        print(f"  {scen:<12} melee closes {m['closed']:.2f}\" and ends {m['end_dist']:.2f}\" out"
              f"  |  rifle closes {g['closed']:.2f}\" and ends {g['end_dist']:.2f}\" out")
        if m["end_dist"] < g["end_dist"] - 1.0:
            print(f"  {'':<12} -> melee arrives closer: consistent with the sprint hypothesis")
        else:
            print(f"  {'':<12} -> no melee advantage: sprint is NOT the whole story here")

env = P.Envelope(
    name=f"arrival-diagnostic-n{N}",
    question="Why do Sabotage and Raid fail the arrival check? Specifically, does "
            "BalancedPolicy's sprint-only-in-the-melee-branch behaviour account for it? "
            "Diagnostic only - no policy is changed and no atom is priced.",
    values={f"{r['scenario']}/{r['crew']}": {"start": r["start_dist"], "end": r["end_dist"],
                                             "closed": r["closed"],
                                             "interactions": r["interactions"]}
            for r in rows},
    raw_cells=rows,
    params={"N_per_cell": N, "scenarios": list(SCENS), "crews": list(CREWS),
            "hold_radius": 3.0,
            "method": "symmetric mirror, no effect; distance to goal at deploy vs at game end"},
    caveats=[
        "DIAGNOSTIC, NOT A PRICE. Nothing here converts to Credits.",
        "Melee and ranged crews differ in more than sprint - they also differ in whether "
        "they can damage at range, which changes how much they are slowed by combat. So a "
        "melee advantage is CONSISTENT with the sprint hypothesis rather than proof of it.",
        "The policy is deliberately NOT changed in this batch. This is the same defect "
        "shape as the advance/shoot bug, and that one was fixed only after being measured.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

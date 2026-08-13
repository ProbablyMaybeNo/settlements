"""Do Sabotage and Raid actually WORK, by the standards the existing scenarios
are held to? Build-and-verify only: no atom is priced here.

WHAT "WORK" MEANS, and why each check exists rather than being a formality:

  RESOLVES          Take-a-Hold with pure ranged crews drew 100% of games at 0.00
                    VP because nobody ever reached an objective. A scenario that
                    cannot produce a winner is not a hard scenario, it is a
                    broken one, and every number measured on it is a measurement
                    of the deadlock.

  ARRIVES           The non-arrival failure was invisible in the win rate - the
                    draws looked like balance. So distance-to-goal at game end is
                    measured DIRECTLY against the 3" interaction radius, which is
                    how that defect was eventually caught.

  INTERACTS         A scenario can resolve for the wrong reason. If no charge is
                    ever armed and no cache ever looted, Sabotage and Raid are
                    just Annihilate wearing a hat. Interaction counts are the
                    check that the NEW mechanic is the thing doing the work.

  GUARD BAND        A mirror sitting outside 20-80% has no room for a buff to
                    move the number; every delta compresses toward zero and the
                    scenario silently stops being able to measure anything.
                    Symmetric crews should sit near 50%.

  SIZE MONOTONIC    More models should not be worse. Take-a-Hold failed this and
                    the failure was read as evidence about crew size when it was
                    actually reading which sizes deadlock.

    py -3.13 verify_scenarios.py [N]
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
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import dist, take_a_hold  # noqa: E402
from rosters import FIRETEAM6, MIXED6, uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

CHECKED = ("hold_claim", "sabotage", "raid")
CREWS = {"Fireteam (6)": FIRETEAM6, "Mixed (6)": MIXED6,
         "Rifle (6)": uniform("dex", 2, "rifle", 6)}


def goal_distance(g):
    """Mean distance from each standing model to its goal at game end. The direct
    read that exposed non-arrival when the win rate could not."""
    ds = []
    for side in (0, 1):
        for u in g._standing(side):
            if getattr(u, "goal", None):
                ds.append(dist(u.pos, u.goal))
    return statistics.fmean(ds) if ds else None


def interactions(g, scen):
    if scen == "sabotage":
        return sum(1 for s in (0, 1) if g.charge[s] is not None)
    if scen == "raid":
        return len(g.looted[0]) + len(g.looted[1])
    if scen == "hold_claim":
        return sum(1 for v in g.claims.values() if v is not None)
    return 0


def run(scen, spec, n, seed=20260813):
    import random
    GameCls, kw = M.SCENARIOS[scen]
    random.seed(seed)
    wins = Counter()
    vps, rounds_used, dists, inters = [], [], [], []
    for _ in range(n):
        board = take_a_hold()
        ca, _ = M.build(spec, 0)
        cb, _ = M.build(spec, 1)
        g = GameCls(ca, cb, board, **kw)
        r = g.play()
        wins[r["winner"]] += 1
        vps.append(r["vp"])
        rounds_used.append(len(g.timeline))
        d = goal_distance(g)
        if d is not None:
            dists.append(d)
        inters.append(interactions(g, scen))
    n_f = float(n)
    return {
        "scenario": scen,
        "draw_rate": wins["draw"] / n_f,
        "a_rate": wins["A"] / n_f,
        "b_rate": wins["B"] / n_f,
        # Symmetric mirror: A's win share counting draws as half. 0.50 = fair.
        "a_share": (wins["A"] + 0.5 * wins["draw"]) / n_f,
        "mean_vp_a": statistics.fmean(v[0] for v in vps),
        "mean_vp_b": statistics.fmean(v[1] for v in vps),
        "zero_vp_games": sum(1 for v in vps if v[0] == 0 and v[1] == 0) / n_f,
        "mean_rounds": statistics.fmean(rounds_used),
        "mean_goal_dist": statistics.fmean(dists) if dists else None,
        "mean_interactions": statistics.fmean(inters),
        "no_interaction_games": sum(1 for i in inters if i == 0) / n_f,
    }


print("=" * 118)
print(f"SCENARIO VERIFICATION — Sabotage and Raid against hold_claim. N={N}/cell")
print("=" * 118)
print("Build-and-verify. No atom is priced here.")
print()
print(f"  {'scenario':<12}{'crew':<14}{'draw':>7}{'A share':>9}{'VP a/b':>13}"
      f"{'0-VP':>7}{'rounds':>8}{'goal d':>8}{'inter':>7}{'0-int':>7}")

rows = []
for scen in CHECKED:
    for cname, spec in CREWS.items():
        r = run(scen, spec, N)
        r["crew"] = cname
        rows.append(r)
        gd = f"{r['mean_goal_dist']:.2f}" if r["mean_goal_dist"] is not None else "  -"
        print(f"  {scen:<12}{cname:<14}{r['draw_rate']:>7.1%}{r['a_share']:>9.1%}"
              f"{r['mean_vp_a']:>6.2f}/{r['mean_vp_b']:<6.2f}"
              f"{r['zero_vp_games']:>7.1%}{r['mean_rounds']:>8.2f}"
              f"{gd:>8}{r['mean_interactions']:>7.2f}{r['no_interaction_games']:>7.1%}")

# --- crew-size monotonicity -------------------------------------------------
print()
print("  CREW SIZE — symmetric mirrors at 4/6/8. Draw rate must not pin at 100%,")
print("  and the scenario must keep resolving as the crew grows.")
print(f"  {'scenario':<12}{'size':>6}{'draw':>9}{'A share':>10}{'VP a':>8}{'0-VP':>8}")
size_rows = []
for scen in CHECKED:
    for size in (4, 6, 8):
        spec = uniform("dex", 2, "rifle", size)
        r = run(scen, spec, max(200, N // 3))
        r["crew"] = f"rifle{size}"
        r["size"] = size
        size_rows.append(r)
        print(f"  {scen:<12}{size:>6}{r['draw_rate']:>9.1%}{r['a_share']:>10.1%}"
              f"{r['mean_vp_a']:>8.2f}{r['zero_vp_games']:>8.1%}")

# --- verdicts ---------------------------------------------------------------
print()
print("=" * 118)
print("VERDICTS")
print("=" * 118)
verdicts = {}
for scen in CHECKED:
    rs = [r for r in rows if r["scenario"] == scen]
    ss = [r for r in size_rows if r["scenario"] == scen]
    fails = []
    if any(r["draw_rate"] >= 0.99 for r in rs + ss):
        fails.append("DEGENERATE: a cell draws >=99%")
    if any(r["zero_vp_games"] >= 0.99 for r in rs):
        fails.append("DEGENERATE: a cell scores nothing in >=99% of games")
    if any(not (0.20 <= r["a_share"] <= 0.80) for r in rs + ss):
        fails.append("OUTSIDE GUARD BAND: a symmetric mirror is not within 20-80%")
    if any(r["no_interaction_games"] >= 0.50 for r in rs):
        fails.append("MECHANIC UNUSED: >=50% of games saw no interaction at all")
    if any(r["mean_rounds"] > 6.001 for r in rs + ss):
        fails.append("OVERRUNS the 6-round limit")
    verdicts[scen] = fails or ["PASS"]
    print(f"  {scen:<12}{'; '.join(verdicts[scen])}")

print()
print("  Non-arrival check — mean distance to goal at game end, against a 3\" radius.")
for scen in CHECKED:
    rs = [r for r in rows if r["scenario"] == scen and r["mean_goal_dist"] is not None]
    if rs:
        worst = max(rs, key=lambda r: r["mean_goal_dist"])
        flag = "  <-- ARRIVES" if worst["mean_goal_dist"] <= 3.0 else "  <-- NON-ARRIVAL RISK"
        print(f"    {scen:<12}worst crew {worst['crew']:<14}"
              f"{worst['mean_goal_dist']:.2f}\"{flag}")

env = P.Envelope(
    name=f"scenario-verification-n{N}",
    question="Do Sabotage and Raid resolve, arrive, use their own mechanics, sit inside the "
            "20-80% guard band, and stay inside 6 rounds - by the same standards the "
            "existing scenarios are held to? Build-and-verify; nothing is priced.",
    values={"verdicts": verdicts},
    raw_cells={"by_crew": rows, "by_size": size_rows},
    params={"N_per_cell": N, "scenarios": list(CHECKED), "crews": list(CREWS),
            "board": "take_a_hold terrain, unchanged - so scoring semantics are the "
                     "ONLY difference between these scenarios",
            "method": "symmetric mirror, both sides identical, no effect applied"},
    caveats=[
        "SABOTAGE MODELS ONE BUILDING PER SIDE. sec 12.7 says each side 'nominates' a "
        "target building, which implies a choice among candidates; the ruleset gives no "
        "selection rule, so modelling the choice would mean inventing one. One symmetric "
        "building per side makes nomination trivial and invents nothing.",
        "RAID CACHE VALUES: the Jackpot is stated as 2 VP; the other two are NOT given a "
        "value in sec 12.7 and are modelled at 1 VP each. If that is wrong the RANKING of "
        "raid outcomes is unaffected but the VP scale is.",
        "RAID JACKPOT IS NOT RANDOMISED. 'Secretly' is hidden information between PLAYERS; "
        "this AI has no belief model, so randomising which cache is the jackpot would add "
        "variance without adding a decision. Symmetric placement keeps the mirror exact.",
        "Interactions use a 3\" radius because the engine's existing try_claim does. The "
        "rules say objectives are Interacts at BASE CONTACT while holding is within 3\". "
        "That conflation is inherited from the engine, not introduced here.",
        "The AI is BYTE-IDENTICAL across all scenarios - both new scenarios hook the "
        "existing g.try_claim slot in BalancedPolicy rather than changing the policy. Any "
        "difference between scenarios is therefore the scenario.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

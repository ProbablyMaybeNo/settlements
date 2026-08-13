"""Sabotage/Raid don't arrive. WHICH of the three levers is wrong?

THE CONTRADICTION
-----------------
Objectives sit ~26" from deployment; crews close 17-19" in six rounds (~3"/round
net). The ruleset's own scoring clock says Sabotage's "earliest arm ~Round 2-3
(cross + reach)" and sizes Escort at "~30-36" to cross at 6-12"/round". Design
and simulation disagree by a factor of two to four, and the disagreement would
show at a physical table as "nobody ever reached the objective".

THE THREE LEVERS, and what the rules actually permit:

  DEPLOYMENT DISTANCE  Deployment zones sit 24" apart (Full Rules sec 558, where
                       it is called load-bearing: range caps at 24" precisely so
                       a gun cannot fire from its own deployment zone turn one).
  MOVEMENT RATES       MOV is FIXED at 6" (sec 448) and raised only by the Fleet
                       skill, to 8". Sprint = BOTH SLOTS for 2xMOV = 12" and
                       "nothing else - no Shoot, no Ready" (sec 115).
  ROUND COUNT          6.

A FOURTH CANDIDATE THIS SCRIPT ALSO TESTS, because assuming it away would repeat
the exact error this project keeps catching: the AI's ACTION ALLOCATION.
BalancedPolicy moves a gunner 6" and spends the Action shooting. It never
Sprints. A human with a charge to plant would. If sprinting alone fixes arrival,
the geometry is sound and this is a harness limitation, NOT a ruleset defect -
and that distinction decides whether a rule changes.

NOTE THE SLOT CONSTRAINT, which is what makes this non-trivial: Sprint consumes
both slots, so a model CANNOT sprint and arm in the same activation. The approach
can run at 12"/round but the arriving turn must be a 6" move plus the Interact.

    py -3.13 investigate_arrival.py [N]
"""

from __future__ import annotations

# IMPORT GUARD - see the note in any measure_*.py.
if __name__ != "__main__":
    raise RuntimeError(f"{__name__} is a script, not a module.")

import random
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import dist, take_a_hold  # noqa: E402
from policies import BALANCED, BalancedPolicy, IN_POSITION  # noqa: E402
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

MOV = 6.0
DEPLOY_GAP = 24.0
ROUNDS = 6
REACH = 3.0     # the engine's interaction radius


class SprintingPolicy(BalancedPolicy):
    """BalancedPolicy that SPRINTS while its objective is far, exactly as the
    rules allow: both slots, 2xMOV, no Shoot.

    The one legal subtlety is preserved deliberately - it stops sprinting once
    within a single move of the goal, because Sprint consumes the Action slot and
    a model that sprints onto an objective cannot Interact with it that turn.
    Sprinting all the way in would arrive faster and never arm, which is a
    different bug wearing the same face.

    Measurement variant only. policies.py is untouched.
    """

    name = 'balanced+sprint'
    # Beyond this range from the goal, running beats shooting.
    SPRINT_BEYOND = MOV + IN_POSITION

    def act(self, g, u):
        far = u.goal is not None and dist(u.pos, u.goal) > self.SPRINT_BEYOND
        if far and u.standing() and not u.pinned and not g.engaged(u):
            g.move_to(u, u.goal, 2 * u.mov)     # Sprint: both slots, no shot
            return
        return super().act(g, u)


SPRINTER = SprintingPolicy()


def run(scen, spec, policy, n, rounds=ROUNDS, seed=20260813):
    GameCls, kw = M.SCENARIOS[scen]
    random.seed(seed)
    wins, dists, inters, arrived = Counter(), [], [], []
    for _ in range(n):
        ca, _ = M.build(spec, 0)
        cb, _ = M.build(spec, 1)
        for u in ca + cb:
            u.policy = policy
        g = GameCls(ca, cb, take_a_hold(), rounds=rounds, **kw)
        r = g.play()
        wins[r["winner"]] += 1
        near = 0
        tot = 0
        for side in (0, 1):
            for u in g._standing(side):
                if getattr(u, "goal", None):
                    d = dist(u.pos, u.goal)
                    dists.append(d)
                    tot += 1
                    near += 1 if d <= REACH else 0
        arrived.append(near / tot if tot else 0.0)
        if scen == "sabotage":
            inters.append(sum(1 for s in (0, 1) if g.charge[s] is not None)
                          + sum(g.best_countdown.values()))
        elif scen == "raid":
            inters.append(len(g.looted[0]) + len(g.looted[1]))
        else:
            inters.append(sum(1 for v in g.claims.values() if v is not None))
    return {"draw": wins["draw"] / float(n),
            "end_dist": statistics.fmean(dists) if dists else None,
            "frac_arrived": statistics.fmean(arrived),
            "interactions": statistics.fmean(inters)}


print("=" * 112)
print(f"ARRIVAL INVESTIGATION — which lever is wrong? N={N}/cell")
print("=" * 112)
print("Quantify only. No rule is changed and no lever is chosen.")
print()

# --- 1. what the rules permit, arithmetically -------------------------------
print("  1. WHAT THE RULES PERMIT (arithmetic, no simulation)")
print(f"     MOV {MOV:.0f}\" fixed (Fleet -> 8\" is the only raise). Sprint = both slots, 2xMOV.")
print(f"     Deployment zones {DEPLOY_GAP:.0f}\" apart. {ROUNDS} rounds. Interact reach {REACH:.0f}\".")
print()
print(f"     {'approach mode':<28}{'per round':>11}{'rounds to cross 24\"':>22}{'+1 to Interact':>16}")
for label, rate in (("Move only (6\"), Action free", MOV),
                    ("Sprint (12\"), no Action", 2 * MOV),
                    ("Fleet Move (8\")", 8.0),
                    ("Fleet Sprint (16\")", 16.0)):
    need = (DEPLOY_GAP - REACH) / rate
    import math
    print(f"     {label:<28}{rate:>10.0f}\"{math.ceil(need):>22}{math.ceil(need) + 1:>16}")
print()
print("     The ruleset's own clock: Sabotage 'earliest arm ~Round 2-3 (cross + reach)'.")
print("     Only the SPRINT rows reach that. Move-only cannot, at any deployment distance")
print("     the 24\" range cap implies.")

# --- 2. does sprinting alone fix it? ----------------------------------------
print()
print("  2. DOES SPRINTING ALONE FIX IT? (the fourth candidate: AI action allocation)")
print(f"     {'scenario':<11}{'crew':<14}{'policy':<10}{'end dist':>10}"
      f"{'% arrived':>11}{'inter':>8}{'draw':>8}")
CREWS = {"Fireteam (6)": FIRETEAM6, "Mixed (6)": MIXED6}
rows = []
for scen in ("sabotage", "raid"):
    for cname, spec in CREWS.items():
        for pname, pol in (("balanced", BALANCED), ("sprint", SPRINTER)):
            r = run(scen, spec, pol, N)
            r.update(scenario=scen, crew=cname, policy=pname)
            rows.append(r)
            print(f"     {scen:<11}{cname:<14}{pname:<10}{r['end_dist']:>9.2f}\""
                  f"{r['frac_arrived']:>10.1%}{r['interactions']:>8.2f}{r['draw']:>8.1%}")
    print()

# --- 3. how many rounds would the current AI need? --------------------------
print("  3. LEVER: ROUND COUNT — how many rounds until the current AI arrives?")
print(f"     {'scenario':<11}{'rounds':>8}{'end dist':>10}{'% arrived':>11}{'inter':>8}")
round_rows = []
for scen in ("sabotage", "raid"):
    for rnds in (6, 8, 10, 12):
        r = run(scen, MIXED6, BALANCED, max(200, N // 2), rounds=rnds)
        r.update(scenario=scen, rounds=rnds)
        round_rows.append(r)
        print(f"     {scen:<11}{rnds:>8}{r['end_dist']:>9.2f}\"{r['frac_arrived']:>10.1%}"
              f"{r['interactions']:>8.2f}")
    print()

print("=" * 112)
print("  Read section 2 first. If sprinting alone restores arrival, the geometry and the")
print("  clock are sound and this is a HARNESS limitation, not a ruleset defect - and no")
print("  rule needs to change. If it does not, the levers in 1 and 3 bound what would.")

env = P.Envelope(
    name=f"arrival-investigation-n{N}",
    question="Sabotage/Raid objectives sit ~26\" out and crews close ~3\"/round, against a "
            "ruleset clock that assumes 6-12\"/round and an arm by Round 2-3. Which is "
            "wrong: deployment distance, movement rates, round count - or the AI's action "
            "allocation? Quantified; no lever is chosen.",
    values={"by_policy": {f"{r['scenario']}/{r['crew']}/{r['policy']}":
                          {"end_dist": r["end_dist"], "frac_arrived": r["frac_arrived"],
                           "interactions": r["interactions"]} for r in rows},
            "by_rounds": {f"{r['scenario']}@{r['rounds']}":
                          {"end_dist": r["end_dist"], "frac_arrived": r["frac_arrived"],
                           "interactions": r["interactions"]} for r in round_rows}},
    raw_cells={"policy": rows, "rounds": round_rows},
    params={"N_per_cell": N, "MOV": MOV, "deploy_gap": DEPLOY_GAP,
            "rounds_default": ROUNDS, "interact_reach": REACH,
            "sprint_rule": "both slots, 2xMOV, no Shoot/Ready (Full Rules sec 115)",
            "variant": "SprintingPolicy - sprints while goal is beyond MOV+reach, then "
                       "reverts so the arriving activation can spend its Action on the Interact"},
    caveats=[
        "QUANTIFY ONLY. No rule is changed, no lever is chosen, policies.py is untouched.",
        "The sprint variant deliberately STOPS sprinting within one move of the goal. Sprint "
        "consumes the Action slot, so a model that sprints onto an objective cannot Interact "
        "with it that turn - sprinting all the way in arrives faster and never arms.",
        "Deployment distance is NOT freely tunable: the 24\" gap is load-bearing in the "
        "opposite direction. Full Rules sec 558 caps weapon range at 24\" BECAUSE the zones "
        "are 24\" apart, so a longer gap would silently un-cap long-range weapons and a "
        "shorter one would let a 24\" gun fire from its own deployment on turn one - which "
        "the sim already found beating every other list by 13-30 points.",
        "Round count is not free either: every scenario's clock is sized to 6 rounds, and "
        "Take a Hold's 15-VP ceiling is 3 objectives x 5 scoring rounds.",
        "MOV is the most constrained of the three: fixed at 6\" by sec 448 with Fleet (8\") "
        "named as the ONLY way to raise it, so a general MOV change rewrites a stat the "
        "whole skill list is balanced against.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

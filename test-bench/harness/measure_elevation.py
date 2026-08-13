"""Height has been an OBSTACLE in every measurement and never a TACTIC. Does that matter?

THE DEFECT SHAPE
----------------
`BalancedPolicy` never calls `g.ascend`. The engine models elevation fully - 2.5D
LOS, roofs at `Piece.height`, falls, cover computed in 3D - and every measurement
to date has had that machinery working AGAINST the models (blocking LOS) and
never FOR them. That is the same shape as the advance/shoot defect: a capability
the engine has, that the AI never exercises, silently biasing every number.

WHY NOT JUST COMPARE AGAINST RoofPolicy
---------------------------------------
`RoofPolicy` exists and does climb. But it also predates the advance/shoot fix and
shoots without the in-position gate, so BALANCED-vs-ROOF would conflate elevation
use with a policy generation. This defines a MINIMAL variant instead: identical to
BalancedPolicy in every respect except that a gunner standing on a building
footprint takes its roof. `policies.py` is NOT modified - the variant lives here,
is used only by this measurement, and nothing else can pick it up.

TWO QUESTIONS, and the second is the one that matters for the rebuild:

  1. Is elevation an EDGE?  Asymmetric: one side climbs, one does not.
  2. Do ATOM VALUES MOVE when both sides climb? If yes, every measurement taken
     without elevation carries a bias, exactly as every pre-5bdeafd number did.

Per batch instruction: QUANTIFY ONLY. The policy is not fixed here even if it matters.

    py -3.13 measure_elevation.py [N]
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

import anchor as A  # noqa: E402
import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import take_a_hold  # noqa: E402
from policies import BALANCED, BalancedPolicy  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6, MIXED6  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()


class BalancedRoof(BalancedPolicy):
    """BalancedPolicy, plus: a gunner standing on a building takes its roof.

    Deliberately the SMALLEST possible delta. It does not change movement,
    targeting, order issuing or the in-position gate - it only converts terrain
    the model is already standing on from cover into a firing position. Anything
    larger would measure a different AI rather than the value of elevation.
    """

    name = 'balanced+roof'

    def act(self, g, u):
        if (u.has_gun() and u.z == 0 and not u.pinned and u.standing()
                and not g.engaged(u)):
            b = g.building_at(u.pos)
            if b is not None and getattr(b, "height", 0) > 0:
                g.ascend(u, b)
        return super().act(g, u)


ROOFY = BalancedRoof()


def build_with(spec, side, policy, effect=None):
    crew, applied = M.build(spec, side, effect)
    for u in crew:
        u.policy = policy
    return crew, applied


def duel(spec, pa, pb, n, seed=20260813):
    """Side A on policy pa, side B on pb, sides swapped every other game so
    deployment and activation order cancel exactly."""
    GameCls, kw = M.SCENARIOS["hold_claim"]
    random.seed(seed)
    wins = Counter()
    roof_frac = []
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            ca, _ = build_with(spec, 0, pa)
            cb, _ = build_with(spec, 1, pb)
            g = GameCls(ca, cb, board, **kw)
            r = g.play()
            wins["test"] += 1 if r["winner"] == "A" else 0
            wins["ctrl"] += 1 if r["winner"] == "B" else 0
            probe = ca
        else:
            ca, _ = build_with(spec, 0, pb)
            cb, _ = build_with(spec, 1, pa)
            g = GameCls(ca, cb, board, **kw)
            r = g.play()
            wins["test"] += 1 if r["winner"] == "B" else 0
            wins["ctrl"] += 1 if r["winner"] == "A" else 0
            probe = cb
        wins["draw"] += 1 if r["winner"] == "draw" else 0
        up = sum(1 for u in probe if u.z > 0)
        roof_frac.append(up / float(len(probe)))
    share = (wins["test"] + 0.5 * wins["draw"]) / float(n)
    return {"test_share": share, "draw_rate": wins["draw"] / float(n),
            "mean_on_roof": statistics.fmean(roof_frac)}


print("=" * 112)
print(f"ELEVATION AS A TACTIC — quantify only, policies.py untouched. N={N}/cell")
print("=" * 112)
print(A.describe())
print("hold_claim. BalancedRoof = BalancedPolicy + 'take the roof you are standing on'.")
print()

# --- 1. is elevation an edge? -----------------------------------------------
print("  1. IS IT AN EDGE? one side climbs, the other does not. 50% = no edge.")
print(f"    {'crew':<16}{'climber share':>15}{'draw':>8}{'on roof':>10}  reading")
LISTS = {"Fireteam (6)": FIRETEAM6, "Mixed (6)": MIXED6, "Armoured (6)": ARMOURED6}
edge_rows = []
for cname, spec in LISTS.items():
    r = duel(spec, ROOFY, BALANCED, N)
    se = (0.25 / N) ** 0.5              # SE of a proportion at p~0.5
    edge = abs(r["test_share"] - 0.5) > 1.96 * se
    reading = "EDGE" if edge else "no significant edge"
    edge_rows.append({"crew": cname, **r, "se": se, "significant": edge})
    print(f"    {cname:<16}{r['test_share']:>14.1%}{r['draw_rate']:>8.1%}"
          f"{r['mean_on_roof']:>10.1%}  {reading}")

# --- 2. do atom values move? ------------------------------------------------
# THE ONE THAT MATTERS. If an atom prices differently when both sides use
# elevation, every number measured without it inherits that bias.
print()
print("  2. DO ATOM VALUES MOVE? both sides on the same policy, atom re-priced.")
print(f"    {'atom':<22}{'no roof':>10}{'roof':>10}{'delta':>9}{'SE':>8}  moves?")

ATOMS = {"+1 Damage (anchor)": E.damage_anchor(),
         "armour:light": E.Effect(kind="armour", armour="light", name="armour:light")}


def price_under(spec, eff, policy, n):
    """price_atom, with every unit on `policy`. Patches M.build for the call."""
    real = M.build

    def patched(s, side, effect=None, weapons=None):
        crew, applied = real(s, side, effect, weapons)
        for u in crew:
            u.policy = policy
        return crew, applied
    M.build = patched
    try:
        return M.price_atom(spec, eff, n=n)
    finally:
        M.build = real


atom_rows = []
for aname, eff in ATOMS.items():
    base_v, roof_v, base_s, roof_s = [], [], [], []
    for spec in LISTS.values():
        rb = price_under(spec, eff, BALANCED, N)
        rr = price_under(spec, eff, ROOFY, N)
        if rb["price_wp"] is not None and rr["price_wp"] is not None:
            base_v.append(rb["price_wp"]); base_s.append(rb["price_se"])
            roof_v.append(rr["price_wp"]); roof_s.append(rr["price_se"])
    if not base_v:
        print(f"    {aname:<22}  ALL CELLS DEGENERATE")
        continue
    b = statistics.fmean(base_v)
    r_ = statistics.fmean(roof_v)
    bse = (sum(s * s for s in base_s) ** 0.5) / len(base_s)
    rse = (sum(s * s for s in roof_s) ** 0.5) / len(roof_s)
    d = r_ - b
    dse = (bse ** 2 + rse ** 2) ** 0.5
    moves = abs(d) > 1.96 * dse
    atom_rows.append({"atom": aname, "no_roof": b, "roof": r_, "delta": d,
                      "delta_se": dse, "moves": moves})
    print(f"    {aname:<22}{b:>+10.3f}{r_:>+10.3f}{d:>+9.3f}{dse:>8.3f}  "
          f"{'MOVES' if moves else 'stable within noise'}")

print()
print("=" * 112)
any_move = any(r["moves"] for r in atom_rows)
any_edge = any(r["significant"] for r in edge_rows)
print(f"  Elevation is an edge:        {'YES' if any_edge else 'not detectably'}")
print(f"  Atom values move with it:    {'YES - existing numbers carry a bias' if any_move else 'not detectably'}")
print("  NOT FIXED in this batch, by instruction. Same shape as advance/shoot, and that")
print("  one was fixed only after it was measured.")

env = P.Envelope(
    name=f"elevation-tactic-n{N}",
    question="BalancedPolicy never calls ascend, so height has been an obstacle in every "
            "measurement and never a tactic. Is elevation an edge, and - the question that "
            "matters - do atom values move when both sides use it?",
    values={"edge": {r["crew"]: r["test_share"] for r in edge_rows},
            "atom_shift": {r["atom"]: {"no_roof": r["no_roof"], "roof": r["roof"],
                                       "delta": r["delta"], "moves": r["moves"]}
                           for r in atom_rows}},
    raw_cells={"edge": edge_rows, "atoms": atom_rows},
    params={"N_per_cell": N, "scenario": "hold_claim",
            "variant": "BalancedPolicy + take the roof you are standing on",
            "anchor_wp_per_model": A.VALUE, "anchor_provisional": A.PROVISIONAL,
            "lists": list(LISTS)},
    caveats=[
        "QUANTIFY ONLY. policies.py is NOT modified; BalancedRoof lives in this script and "
        "nothing else can pick it up.",
        "The variant is the SMALLEST possible delta - it only converts a building the model "
        "is already standing on from cover into a firing position. It does not change "
        "movement, targeting or the in-position gate. A larger variant would measure a "
        "different AI rather than the value of elevation.",
        "Deliberately NOT compared against the existing RoofPolicy: that one predates the "
        "advance/shoot fix and shoots without the in-position gate, so the comparison would "
        "conflate elevation with a policy generation.",
        "Measured on hold_claim only, so it inherits the single-scenario coverage limit "
        "like everything else in the rebuild.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

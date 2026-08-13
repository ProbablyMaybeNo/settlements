"""Did the Sprint fix overcorrect? And does the harness still behave?

WHY THIS EXISTS SEPARATELY FROM THE ARRIVAL NUMBERS
---------------------------------------------------
The arrival numbers only show the fix WORKS. They cannot show it doesn't work too
hard, and a policy that sprints too eagerly fails in a much quieter way than one
that never sprints: instead of 99% draws and a screaming zero-interaction count,
you get a crew that arrives promptly and then loses because it walked into the
open without shooting. Every measurement would still "resolve", and the bias
would sit inside every number.

So the fix is checked against the failure it could plausibly introduce, not only
against the one it was built to remove:

  A  HEAD-TO-HEAD      the fixed policy must not LOSE to the old one anywhere,
                       especially on hold_claim where the existing numbers live
                       and where objectives are close enough that sprinting is
                       mostly unnecessary.
  B  SPRINT RATE       what fraction of activations actually sprint? Near 100%
                       would mean the threshold is doing nothing.
  C  SHOOTING INTACT   a crew that stops shooting has traded one pathology for
                       another. Shots per game must survive.
  D  SMOKE INVARIANTS  policy-independent properties that must hold no matter
                       what any AI does. If these break, the harness is wrong
                       rather than the policy.

    py -3.13 verify_sprint_fix.py [N]
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

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import dist, take_a_hold  # noqa: E402
from policies import BALANCED, BalancedPolicy, IN_POSITION  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6, MIXED6, uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 800

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()


class LegacyNoSprint(BalancedPolicy):
    """The PRE-FIX policy, reconstructed for comparison: never sprints.

    Subclasses the fixed policy and forces the threshold out of reach, so the two
    differ in exactly one behaviour and nothing else. Rebuilding the old class by
    hand would have risked differing in some second way and attributing the gap
    to sprinting.
    """

    name = 'balanced-nosprint'

    def act(self, g, u):
        import policies as _p
        real = _p.sprint_threshold
        try:
            _p.sprint_threshold = lambda unit: float("inf")
            return super().act(g, u)
        finally:
            _p.sprint_threshold = real


LEGACY = LegacyNoSprint()

SCENS = ("hold_claim", "sabotage", "raid")
CREWS = {"Fireteam (6)": FIRETEAM6, "Mixed (6)": MIXED6, "Armoured (6)": ARMOURED6}


def duel(scen, spec, pa, pb, n, seed=20260813):
    """pa vs pb, sides swapped every other game."""
    GameCls, kw = M.SCENARIOS[scen]
    random.seed(seed)
    w = Counter()
    for i in range(n):
        ca, _ = M.build(spec, 0)
        cb, _ = M.build(spec, 1)
        first, second = (pa, pb) if i % 2 == 0 else (pb, pa)
        for u in ca:
            u.policy = first
        for u in cb:
            u.policy = second
        r = GameCls(ca, cb, take_a_hold(), **kw).play()
        a_is_test = (i % 2 == 0)
        if r["winner"] == "draw":
            w["draw"] += 1
        elif (r["winner"] == "A") == a_is_test:
            w["test"] += 1
        else:
            w["ctrl"] += 1
    return (w["test"] + 0.5 * w["draw"]) / float(n), w["draw"] / float(n)


print("=" * 108)
print(f"SPRINT FIX — did it overcorrect? N={N}/cell")
print("=" * 108)
print("Fixed policy vs the same policy with sprinting disabled. One behaviour differs.")
print()

# --- A. head to head --------------------------------------------------------
print("  A. HEAD-TO-HEAD — fixed vs no-sprint. <50% anywhere means it overcorrected.")
print(f"     {'scenario':<12}{'crew':<15}{'fixed share':>13}{'draw':>8}  reading")
duels = []
for scen in SCENS:
    for cname, spec in CREWS.items():
        share, draw = duel(scen, spec, BALANCED, LEGACY, N)
        se = (0.25 / N) ** 0.5
        if share < 0.5 - 1.96 * se:
            reading = "WORSE — overcorrected"
        elif share > 0.5 + 1.96 * se:
            reading = "better"
        else:
            reading = "no significant difference"
        duels.append({"scenario": scen, "crew": cname, "share": share,
                      "draw": draw, "reading": reading})
        print(f"     {scen:<12}{cname:<15}{share:>12.1%}{draw:>8.1%}  {reading}")
    print()

# --- B/C. sprint rate and shooting ------------------------------------------
print("  B/C. SPRINT RATE and SHOOTING — is the threshold doing any work, and do")
print("       models still shoot? Instrumented by counting engine calls.")
print(f"     {'scenario':<12}{'sprint/activation':>19}{'shots/game':>12}{'moves/game':>12}")


def instrument(scen, spec, n, seed=20260813):
    """Count sprints (a move_to with max_dist > mov) and shots."""
    GameCls, kw = M.SCENARIOS[scen]
    import engine as _e
    real_move, real_shoot = _e.Game.move_to, _e.Game.shoot
    stats = Counter()

    def move_to(self, u, point, max_dist):
        stats["moves"] += 1
        if max_dist > u.mov + 1e-9:
            stats["sprints"] += 1
        return real_move(self, u, point, max_dist)

    def shoot(self, u, t, *a, **k):
        stats["shots"] += 1
        return real_shoot(self, u, t, *a, **k)

    _e.Game.move_to, _e.Game.shoot = move_to, shoot
    try:
        random.seed(seed)
        acts = 0
        for _ in range(n):
            ca, _x = M.build(spec, 0)
            cb, _x = M.build(spec, 1)
            g = GameCls(ca, cb, take_a_hold(), **kw)
            g.play()
            acts += sum(len(t) for t in [g.timeline]) * len(g.units)
    finally:
        _e.Game.move_to, _e.Game.shoot = real_move, real_shoot
    return {"sprints": stats["sprints"], "moves": stats["moves"],
            "shots": stats["shots"], "activations": max(acts, 1), "n": n}


instr = []
for scen in SCENS:
    r = instrument(scen, MIXED6, max(150, N // 4))
    rate = r["sprints"] / r["activations"]
    instr.append({"scenario": scen, "sprint_per_activation": rate,
                  "shots_per_game": r["shots"] / r["n"],
                  "moves_per_game": r["moves"] / r["n"]})
    print(f"     {scen:<12}{rate:>18.1%}{r['shots'] / r['n']:>12.2f}"
          f"{r['moves'] / r['n']:>12.2f}")

# --- D. smoke invariants ----------------------------------------------------
print()
print("  D. SMOKE — properties that hold whatever the AI does. A break here means")
print("     the HARNESS is wrong, not the policy.")
checks = []


def check(label, ok, detail):
    checks.append({"check": label, "pass": bool(ok), "detail": detail})
    print(f"     {'PASS' if ok else 'FAIL':<6}{label:<44}{detail}")


# D1 - a symmetric mirror must sit at 50%
share, _ = duel("hold_claim", MIXED6, BALANCED, BALANCED, N)
se = (0.25 / N) ** 0.5
check("symmetric mirror sits at 50%", abs(share - 0.5) <= 1.96 * se,
      f"{share:.3%} (+-{1.96 * se:.3%})")

# SMOKE_N is fixed and generous rather than derived from N. An underpowered smoke
# check is worse than none: the first version ran the anchor at N//2=400, where
# its SE is wide enough that a perfectly healthy +0.5625 failed the significance
# leg and reported "harness suspect". A check that fails when nothing is wrong
# trains you to ignore it.
SMOKE_N = 2000

# D2 - a null effect must price at ~0
res = M.price_atom(MIXED6, None, n=SMOKE_N)
nullwp = res["price_wp"]
check("null effect prices at ~0", not res["price_significant"],
      f"{nullwp:+.4f}, significant={res['price_significant']}")

# D3 - the anchor must still be positive and significant. Its VALUE is expected
# to move (the fix voids pre-fix numbers); what must survive is the SIGN.
res = M.price_atom(MIXED6, E.damage_anchor(), n=SMOKE_N)
check("+1 Damage still positive & significant",
      res["price_wp"] is not None and res["price_wp"] > 0 and res["price_significant"],
      f"{res['price_wp']:+.4f} (n={SMOKE_N})")

# D4 - sprinting must never happen while engaged (illegal: you are in melee)
# and never while pinned (Pinned cannot Sprint, sec 272).
import engine as _e  # noqa: E402
real_move = _e.Game.move_to
violations = Counter()


def guarded(self, u, point, max_dist):
    if max_dist > u.mov + 1e-9:
        if self.engaged(u):
            violations["engaged"] += 1
        if u.pinned:
            violations["pinned"] += 1
    return real_move(self, u, point, max_dist)


_e.Game.move_to = guarded
try:
    random.seed(20260813)
    for _ in range(max(150, N // 4)):
        ca, _x = M.build(MIXED6, 0)
        cb, _x = M.build(MIXED6, 1)
        M.SCENARIOS["sabotage"][0](ca, cb, take_a_hold()).play()
finally:
    _e.Game.move_to = real_move
check("never sprints while engaged", violations["engaged"] == 0,
      f"{violations['engaged']} violations")
check("never sprints while pinned", violations["pinned"] == 0,
      f"{violations['pinned']} violations")

worst = min((d["share"] for d in duels), default=1.0)
overcorrected = any(d["reading"].startswith("WORSE") for d in duels)
all_smoke = all(c["pass"] for c in checks)

print()
print("=" * 108)
print(f"  overcorrected anywhere: {'YES' if overcorrected else 'no'}"
      f"   (worst cell {worst:.1%})")
print(f"  smoke invariants:       {'ALL PASS' if all_smoke else 'FAILURE - harness suspect'}")
print()
print("  EVERY MEASUREMENT TAKEN BEFORE THIS FIX IS VOID, on the same terms as the")
print("  advance/shoot fix: the AI now reaches an action it never took, so any number")
print("  measured under the old behaviour describes a different game.")

env = P.Envelope(
    name=f"sprint-fix-verification-n{N}",
    question="Did teaching BalancedPolicy to Sprint overcorrect? Checked against the failure "
            "the fix could plausibly INTRODUCE - sprinting when it shouldn't - rather than "
            "only the one it removes, plus policy-independent harness invariants.",
    values={"head_to_head": {f"{d['scenario']}/{d['crew']}": d["share"] for d in duels},
            "instrumentation": {r["scenario"]: r for r in instr},
            "smoke": {c["check"]: c["pass"] for c in checks},
            "overcorrected": overcorrected, "smoke_all_pass": all_smoke},
    raw_cells={"duels": duels, "instrumentation": instr, "smoke": checks},
    params={"N_per_cell": N, "scenarios": list(SCENS), "crews": list(CREWS),
            "threshold": "u.mov + IN_POSITION (9\" at baseline MOV 6\")",
            "sprint_rule": "both slots, 2xMOV, no Shoot/Ready (Full Rules sec 115)"},
    caveats=[
        "The control is the FIXED class with its threshold forced to infinity, not a "
        "hand-rebuilt old policy - so the two differ in exactly one behaviour and the gap "
        "cannot be attributed to some second accidental difference.",
        "A sprinting model still issues Orders. Orders are a rank resource granting a free "
        "Action to a friendly, not the sprinter's own Action slot, so this reads as legal "
        "under sec 115's 'nothing else' - but it IS an interpretation and is flagged.",
        "Every pre-fix measurement is void. The anchor smoke check asserts only that +1 "
        "Damage stays POSITIVE and significant; its value is expected to move.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

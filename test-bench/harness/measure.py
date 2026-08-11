"""Measure what an Effect is worth, in win-points per model. No Credits here.

METHOD — paired mirror, which is the method this project already established as
the trustworthy one (POINTS-TABLE.md 5.4): identical crews, one side buffed, so
the baseline is exactly 50% by symmetry. The asymmetric alternative was discarded
because its Hold baselines sat at 8% and 92%, where a buff has no room to move
the number and every delta compresses toward zero.

TWO THINGS THIS ADDS THAT NO EXISTING HARNESS HAS
-------------------------------------------------
1. A STANDARD ERROR. No harness in the project reports one and no document
   quotes a confidence interval, which is why four published prices (the
   single-fighter stat row at 6 Cr, extra-activation at -35, Concussive at 1,
   Crippling at -2) are all statistically indistinguishable from zero and were
   nonetheless written down as numbers. Here every measurement carries its SE and
   a `significant` flag, and the flag is computed, not asserted.

2. PAIRED VARIANCE REDUCTION. Both arms run the same seed over the same board
   sequence, so game i in the test arm and game i in the control arm are the same
   scenario. Differencing per game removes the shared board/deployment variance
   instead of adding the two arms' variance together. Typically 2-4x tighter for
   the same compute, and it is free.

The divisor question is not resolved here, it is REPORTED: every result carries
per_model (models present) and per_applied (models the effect actually reached).
They differ by ~20% on this project's own standard lists, and every published
price to date used the first.
"""

from __future__ import annotations

import math
import random
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / "engine2d"
if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))

import engine as _engine  # noqa: E402
from engine import Game, Unit  # noqa: E402
from board import take_a_hold  # noqa: E402
from policies import BALANCED  # noqa: E402
from data import WEAPONS  # noqa: E402


class Annihilate(Game):
    """VP = enemy models removed. The pure-kill read."""

    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {
    "hold": (Game, {}),
    "hold_claim": (Game, {"claim": True}),
    "annihilate": (Annihilate, {}),
}


@dataclass
class Result:
    effect: str
    scenario: str
    n: int
    n_present: int
    n_applied: int
    delta: float = 0.0
    se: float = 0.0
    per_model: float = 0.0
    per_applied: float = 0.0
    per_applied_se: float = 0.0
    significant: bool = False
    buffed_winrate: float = 0.0
    draw_rate: float = 0.0
    degenerate: bool = False
    notes: list = field(default_factory=list)

    def line(self) -> str:
        sig = "  " if self.significant else " ~"
        app = f"{self.per_applied:+6.3f}+-{self.per_applied_se:.3f}"
        return (f"{sig}{self.effect:<28} {self.scenario:<11} "
                f"d {self.delta:+7.2f}+-{self.se:4.2f}  "
                f"/model {self.per_model:+6.3f}  /applied {app}  "
                f"(n_applied {self.n_applied}/{self.n_present})")


def build(spec, side, effect=None, weapons=None):
    """spec: list of (name, rank, weapon, armour, stats-dict)."""
    weapons = WEAPONS if weapons is None else weapons
    crew = []
    for (nm, rank, wpn, arm, st) in spec:
        u = Unit(nm, side, rank, wpn, arm, **dict(st))
        u.policy = BALANCED
        crew.append(u)
    applied = effect.apply(crew, weapons) if effect else 0
    return crew, applied


def mirror(spec, effect, scenario="hold", n=2000, seed=20260811):
    """Identical crews, one side buffed. Returns per-game outcomes for the buffed
    side (1.0 win / 0.5 draw / 0.0 loss), and how many models the effect reached.

    The buffed side alternates so deployment and activation order cancel exactly.
    """
    GameCls, kw = SCENARIOS[scenario]
    random.seed(seed)
    outcomes = []
    applied = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            ca, applied = build(spec, 0, effect)
            cb, _ = build(spec, 1)
            r = GameCls(ca, cb, board, **kw).play()
            win, lose = r["winner"] == "A", r["winner"] == "B"
        else:
            ca, _ = build(spec, 0)
            cb, applied = build(spec, 1, effect)
            r = GameCls(ca, cb, board, **kw).play()
            win, lose = r["winner"] == "B", r["winner"] == "A"
        outcomes.append(1.0 if win else (0.0 if lose else 0.5))
    return outcomes, applied


def measure(spec, effect, scenario="hold", n=2000, seed=20260811, alpha=1.96):
    """Paired mirror against a null-effect control on the identical seed.

    Both arms see the same board sequence, so differencing per game removes the
    shared variance rather than summing it.
    """
    test, applied = mirror(spec, effect, scenario, n, seed)
    ctrl, _ = mirror(spec, None, scenario, n, seed)

    diffs = [(t - c) * 100.0 for t, c in zip(test, ctrl)]
    delta = statistics.fmean(diffs)
    se = (statistics.stdev(diffs) / math.sqrt(n)) if n > 1 else float("nan")

    present = len(spec)
    denom = applied if applied else present
    r = Result(
        effect=effect.label() if effect else "none",
        scenario=scenario,
        n=n,
        n_present=present,
        n_applied=applied,
        delta=delta,
        se=se,
        per_model=delta / present,
        per_applied=delta / denom,
        per_applied_se=se / denom,
        significant=abs(delta) > alpha * se,
        buffed_winrate=statistics.fmean(test),
        draw_rate=sum(1 for t in test if t == 0.5) / n,
    )

    # DEGENERATE CELL GUARD. A scenario that cannot resolve for this crew returns
    # a delta of exactly zero no matter how large the effect, and averaging that
    # structural zero with a real number halves it silently. Measured live: a
    # uniform RIFLE crew mirror draws 100% of Hold games - both sides sit on their
    # own objectives and neither can displace the other - while a uniform SLEDGE
    # crew draws 5.5% of the same scenario. Without this flag the DEX ladder came
    # out at exactly half its true value and looked entirely plausible.
    if r.draw_rate >= 0.95:
        r.degenerate = True
        r.significant = False
        r.notes.append(
            f"DEGENERATE: {r.draw_rate:.1%} of games drew, so this scenario cannot "
            "resolve for this crew. The delta is structurally zero and carries no "
            "information. Exclude it - do NOT average it with a live scenario."
        )

    if applied == 0:
        r.notes.append("effect reached NO model - divisor fell back to models present")
    elif applied < present:
        r.notes.append(
            f"reached {applied} of {present} models; dividing by models present "
            f"would understate this by {present / applied:.2f}x"
        )
    if not r.significant:
        r.notes.append(
            f"NOT significant at 95%: |{delta:.2f}| <= 1.96 x {se:.2f}. "
            "Report as indistinguishable from zero, never as a price."
        )
    return r


def across(spec, effect, scenarios=("hold", "annihilate"), n=2000, seed=20260811):
    """Per scenario, reported SEPARATELY. Averaging Hold and Annihilate is how a
    trait that is strong in one and useless in the other acquires a middling
    price that describes neither - see T6, where INT is competitive on Hold
    (47-49%) and collapses on Annihilate (14%)."""
    return [measure(spec, effect, s, n, seed) for s in scenarios]


def set_dials(**kw):
    """Set engine module dials, returning the previous values for restoration.

    NOTE: setattr on a module silently succeeds even when the attribute does not
    exist, which is how a packet harness run against an engine lacking the flag
    produces plausible numbers with every dial a no-op and no error. So this
    REFUSES unknown dials rather than creating them.
    """
    old = {}
    for k, v in kw.items():
        if not hasattr(_engine, k):
            raise AttributeError(
                f"engine has no dial {k!r} - refusing to create it. "
                "A silently-created dial is a no-op that looks like a measurement."
            )
        old[k] = getattr(_engine, k)
        setattr(_engine, k, v)
    return old

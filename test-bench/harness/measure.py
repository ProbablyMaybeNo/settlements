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

# PRICING RUNS ON OBJECTIVE SCENARIOS ONLY.
#
# The ruleset is explicit that you win on objectives and never on kills (sec 1,
# sec 12.7), so Annihilate is not a playable scenario - it is a diagnostic. A
# price averaged across it is a price for a game nobody plays.
#
# This is not a stylistic preference, it is load-bearing, because several atoms
# have OPPOSITE SIGNS in the two scenario families and the average hides it.
# Pinned is the worked case: all three Hold cells negative, all three Annihilate
# cells positive, 6/6 consistent, mean indistinguishable from zero. "Worth
# nothing" and "worth something on objectives and negative on kills" are
# different findings with different design consequences, and only the second
# survives contact with the per-cell data.
#
# Annihilate stays measurable and stays REPORTED per cell - it is useful for
# diagnosing what an atom does - but it never contributes to a price.
PRICING_SCENARIOS = ("hold", "hold_claim")
DIAGNOSTIC_SCENARIOS = ("annihilate",)


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
    saturated: bool = False
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

    # SATURATION GUARD. A mirror starts at 50%, so a crew-level delta of +35 sits
    # at 85% with only 15 points of headroom left, and further improvement has
    # nowhere to go. Differences between strong variants then compress toward each
    # other and can even invert. Measured live: a range sweep upgrading all six
    # models ran 83-87.5% and reported 8" as better than 24" - which was the
    # ceiling, not the game. conditions2d.py's own notes warn about exactly this
    # for its asymmetric pass; the mirror is not immune, it just starts centred.
    # Fix is to shrink the effect (upgrade one model, not the whole crew), never
    # to reinterpret the compressed numbers.
    if r.buffed_winrate >= 0.80 or r.buffed_winrate <= 0.20:
        r.saturated = True
        r.notes.append(
            f"SATURATED: buffed side at {r.buffed_winrate:.1%}, only "
            f"{min(abs(1 - r.buffed_winrate), abs(r.buffed_winrate)) * 100:.0f} points of "
            "headroom. Deltas here are compressed and orderings between strong "
            "variants are unreliable. Shrink the effect (e.g. only_first) and re-run."
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


def price_atom(spec, effect, n=2500, seed=20260811,
               pricing=PRICING_SCENARIOS, diagnostic=DIAGNOSTIC_SCENARIOS):
    """Measure an atom across every scenario, but price it from objective play only.

    Returns a dict carrying the per-cell values UNAVERAGED, because averaging is
    what hid the Pinned sign-split. `price_wp` is the objective-only figure and is
    the only number that should ever become a Credits price.
    """
    cells = {}
    for s in tuple(pricing) + tuple(diagnostic):
        r = measure(spec, effect, s, n=n, seed=seed)
        cells[s] = r

    live = [cells[s] for s in pricing if not cells[s].degenerate]
    out = {
        "effect": effect.label() if effect else "none",
        "cells": {s: {"wp": round(r.per_applied, 4), "se": round(r.per_applied_se, 4),
                      "winrate": round(r.buffed_winrate, 4),
                      "significant": r.significant, "degenerate": r.degenerate,
                      "saturated": r.saturated, "n_applied": r.n_applied}
                  for s, r in cells.items()},
        "priced_from": [s for s in pricing if not cells[s].degenerate],
        "dropped_degenerate": [s for s in pricing if cells[s].degenerate],
        "any_saturated": any(r.saturated for r in cells.values()),
    }
    if live:
        wp = statistics.fmean([r.per_applied for r in live])
        se = (sum(r.per_applied_se ** 2 for r in live) ** 0.5) / len(live)
        out["price_wp"] = round(wp, 4)
        out["price_se"] = round(se, 4)
        out["price_ci"] = [round(wp - 1.96 * se, 4), round(wp + 1.96 * se, 4)]
        out["price_significant"] = abs(wp) > 1.96 * se
    else:
        out["price_wp"] = None
        out["price_significant"] = False

    # SIGN-SPLIT DETECTOR. If an atom points one way on objectives and the other
    # on kills, an average across them is meaningless even when it looks tidy.
    # A sign difference only MEANS anything if both sides are distinguishable from
    # zero. Testing sign alone cries wolf: Concussive reads -0.021 on Hold and
    # +0.225 on Annihilate, which is technically opposite and actually just noise
    # against nothing. Require significance on BOTH sides, and require the pricing
    # side to agree with itself - Crippling's two objective cells had opposite
    # signs from each other, which is noise, not structure.
    def _signed(r):
        return (1 if r.per_applied > 0 else -1) if r.significant else 0

    signs = {s: _signed(r) for s, r in cells.items() if not r.degenerate}
    pricing_signs = {signs[s] for s in pricing if s in signs} - {0}
    diag_signs = {signs[s] for s in diagnostic if s in signs} - {0}
    if (len(pricing_signs) == 1 and len(diag_signs) == 1
            and pricing_signs.isdisjoint(diag_signs)):
        out["sign_split"] = True
        out["sign_split_note"] = (
            "objective and kill scenarios disagree in SIGN. The atom does opposite "
            "things in the two families; any average across them describes neither. "
            "Priced from objective cells only, which is the ruleset's own criterion."
        )
    else:
        out["sign_split"] = False
    return out

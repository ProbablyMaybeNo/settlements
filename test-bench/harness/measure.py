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
from board import take_a_hold, dist  # noqa: E402
from policies import BALANCED  # noqa: E402
from data import WEAPONS  # noqa: E402


class Annihilate(Game):
    """VP = enemy models removed. The pure-kill read."""

    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


# ===========================================================================
# SABOTAGE and RAID — the two scenarios furthest from control play.
#
# WHY THEY EXIST. Every price in this project was measured on Take-a-Hold, which
# is one of five shipped scenarios and the most STATIC one. Pricing the game
# against it overvalues defensive/static atoms (range, damage, armour) and
# undervalues mobility, tempo and objective-running - the DEX-ladder failure one
# level up. Sabotage resolves by TIMER and sudden death; Raid scores in the
# ENEMY'S HALF. Those are the two structural axes control play cannot express.
#
# HOW THEY HOOK IN WITHOUT TOUCHING THE AI. BalancedPolicy already has an
# "interact with the objective" slot at exactly the right priority - after
# shoot-once-in-position, before reposition - and it calls g.try_claim(u), which
# is a no-op outside claim mode. Both scenarios override try_claim. So the AI is
# BYTE-IDENTICAL across all four scenarios, and any difference measured between
# them is the scenario rather than a policy change. Changing policies.py would
# have made the comparison worthless.
#
# INTERACTION RADIUS. The rules say objectives are Interacts at BASE CONTACT,
# while holding is "within 3"". The engine already conflates the two - try_claim
# uses 3.0 - so these use 3.0 for consistency. That is a PRE-EXISTING engine
# simplification being inherited, not a new one being introduced.
# ===========================================================================

CHARGE_FUSE = 3          # End Phases a charge must survive armed, per sec 12.7
JACKPOT_VP = 2           # "one secretly a 2-VP Jackpot"
CACHE_VP = 1             # the other two. Not stated in sec 12.7 - see caveat.


class Sabotage(Game):
    """Timer, sudden death. Each side has one building; you win by arming a
    charge on the ENEMY'S and having it survive 3 End Phases.

    sec 12.7: "each side nominates a target building; the enemy arms a charge
    (INT 7+) that detonates after surviving 3 End Phases armed unless defused
    (DEX 7+, nat 1 = it goes off now). Detonating the enemy's building wins
    immediately."

    MODELLING NOTE - ONE BUILDING PER SIDE. "Nominates" implies a choice among
    candidates. Modelling the choice would require a selection rule the ruleset
    does not give, so each side gets exactly ONE building, symmetrically placed,
    which makes nomination trivial and invents nothing. Flagged in the log.
    """

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        # A's building sits in A's half, B's in B's, mirror-symmetric about y=18
        # so neither side has a shorter walk. Same terrain as take_a_hold, so the
        # ONLY difference from hold_claim is what scoring means.
        self.buildings = {0: (18.0, 9.0), 1: (18.0, 27.0)}
        self.charge = {0: None, 1: None}     # side -> End Phases armed on THAT side's building
        self.best_countdown = {0: 0, 1: 0}   # side -> furthest its charge ever got (tiebreak)
        self.detonated = None

    def _spawn(self):
        super()._spawn()
        # Goal is the ENEMY'S building. The base _spawn assigns the nearest
        # objective, which here would be a model's OWN building - i.e. everyone
        # would defend and nobody would ever attack, manufacturing a 100% draw.
        for side, crew in enumerate(self.sides):
            for u in crew:
                u.goal = self.buildings[1 - side]

    def try_claim(self, u):
        """Arm the enemy's charge, or defuse one on your own building."""
        mine, theirs = self.buildings[u.side], self.buildings[1 - u.side]
        # Defusing your own building takes priority: it is about to kill you.
        if self.charge[u.side] is not None and dist(u.pos, mine) <= 3.0:
            ok, die = _engine.core_d(u.stats['dex'] - u.penalty())
            if die == 1:
                self.charge[u.side] = CHARGE_FUSE      # nat 1: it goes off NOW
                self.note(f"  {u.tag} FUMBLES the defuse - it goes off now")
            elif ok:
                self.charge[u.side] = None
                self.note(f"  {u.tag} defuses the charge")
            return True
        # Otherwise arm a charge on theirs, if it is not already armed.
        if self.charge[1 - u.side] is None and dist(u.pos, theirs) <= 3.0:
            if _engine.core(u.stats['int'] - u.penalty()):
                self.charge[1 - u.side] = 0
                self.note(f"  {u.tag} arms a charge on the enemy building")
            return True
        return False

    def score_objectives(self, rnd):
        # A charge survives an End Phase armed, then detonates on the third.
        blown = []
        for side in (0, 1):
            if self.charge[side] is not None:
                self.charge[side] += 1
                self.best_countdown[1 - side] = max(self.best_countdown[1 - side],
                                                    self.charge[side])
                if self.charge[side] >= CHARGE_FUSE:
                    blown.append(side)
        # SIMULTANEOUS DETONATION IS A DRAW, and getting this wrong was measurable.
        # The first version resolved sides in list order and took the first
        # detonation, so when both fuses completed on the same End Phase - which
        # is the NORMAL case in a symmetric mirror, both crews doing the same
        # thing at the same pace - side 0's building always blew first and side 1
        # always won. It showed up as a 32.7% A-share in a mirror that is
        # symmetric by construction, which is impossible on the merits.
        #
        # sec 12.7 covers "neither detonates by Round 6" but is silent on both
        # detonating at once. A draw is the reading that does not invent a winner;
        # resolving by list order invents one and hides it in the iteration order.
        if blown and self.detonated is None:
            self.over = True
            if len(blown) == 2:
                self.vp[0] = self.vp[1] = CHARGE_FUSE + 1
                self.note("  both buildings detonate simultaneously - draw")
            else:
                side = blown[0]
                self.detonated = 1 - side          # the ARMING side wins
                self.vp[1 - side] = CHARGE_FUSE + 1
                self.note(f"  building {side} detonates - side {1 - side} wins")
        # THE ROUND-6 TIEBREAK, from Scenarios.md sec 4: "If neither detonates by
        # the end of Round 6, the side whose charge reached the MOST COUNTDOWN
        # wins; equal = draw." Without it a Sabotage game that fails to detonate
        # is a flat draw, which discards the entire difference between a side
        # that armed and nearly blew the building and a side that never crossed
        # the table. Partial progress decides the game, and the first version of
        # this class dropped that rule and drew 99.8% of games as a result.
        if not self.over and rnd >= self.rounds:
            for s in (0, 1):
                self.vp[s] = max(self.vp[s], self.best_countdown[s])
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


class Raid(Game):
    """Retrieve, scored in the ENEMY'S half. Each side hides 3 caches in its own
    half, one secretly a 2-VP Jackpot; you score by looting the enemy's.

    sec 12.7: "each side hides 3 loot caches in their own half (one secretly a
    2-VP Jackpot); score by looting the *enemy's*, not defending your own. Most
    enemy loot value by Round 6 wins."
    """

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        # Three caches per half, mirror-symmetric. The Jackpot is index 1 for
        # BOTH sides: "secretly" is hidden information between PLAYERS, and this
        # AI has no belief model to hide anything from, so randomising which one
        # is the jackpot would add variance without adding a decision. Symmetric
        # placement keeps the mirror exact.
        self.caches = {
            0: [(8.0, 8.0), (18.0, 10.0), (28.0, 8.0)],
            1: [(8.0, 28.0), (18.0, 26.0), (28.0, 28.0)],
        }
        self.jackpot = {0: 1, 1: 1}
        self.looted = {0: set(), 1: set()}    # which of side S's caches are gone

    def _spawn(self):
        super()._spawn()
        for side, crew in enumerate(self.sides):
            for u in crew:
                u.goal = min(self.caches[1 - side], key=lambda c: dist(u.pos, c))

    def try_claim(self, u):
        """Loot an unlooted enemy cache in reach. INT test, per 'Loot/search -> INT'."""
        foe = 1 - u.side
        for i, c in enumerate(self.caches[foe]):
            if i in self.looted[foe] or dist(u.pos, c) > 3.0:
                continue
            if _engine.core(u.stats['int'] - u.penalty()):
                self.looted[foe].add(i)
                self.vp[u.side] += JACKPOT_VP if i == self.jackpot[foe] else CACHE_VP
                self.note(f"  {u.tag} loots enemy cache {i}")
            return True
        # Nothing here to loot - retarget onto the nearest cache still standing.
        left = [c for j, c in enumerate(self.caches[foe]) if j not in self.looted[foe]]
        if left:
            u.goal = min(left, key=lambda c: dist(u.pos, c))
        return False

    def score_objectives(self, rnd):
        # VP accrue at the moment of looting, not per End Phase - the loot is
        # banked, not held. Nothing to do here but record the timeline.
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {
    "hold": (Game, {}),
    "hold_claim": (Game, {"claim": True}),
    "annihilate": (Annihilate, {}),
    "sabotage": (Sabotage, {}),
    "raid": (Raid, {}),
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
#
# ---------------------------------------------------------------------------
# 2026-08-13: `hold` DROPPED FROM PRICING. It is not a scenario in this game.
#
# Every objective in the ruleset is an Interact: "base contact, costs the Action,
# resolves as 1d10+Stat vs 7+. Claim/activate/connect -> INT" (Full Rules System
# v1 sec 12.7). `hold` is claim_mode=False, which scores POSITIONALLY -
# bodies-in-area, no stat test, no Action spent (engine.py score_objectives).
# There is no proximity-only scoring anywhere in the five shipped scenarios.
#
# So `hold` is not a variant of Take a Hold. It is a different game, in which
# objectives are taken by standing near them rather than by spending an Action.
# It was carrying HALF the anchor's weight, denominated in nothing - the same
# defect class as the "legacy x10" weapon scale, armour's 30/60 citing a file
# that never existed, and the unchosen 50/50 weighting itself.
#
# This also EXPLAINS the systematic hold-vs-hold_claim gap (0.90-1.47 against
# 0.29-0.40, consistent 3/3 across every list, replicated at 3.7-6.9x on the
# range probes). The gap was never dispersion. It was measuring THE COST OF THE
# CLAIM STEP: an Action spent claiming is an Action not spent attacking, so a
# damage buff has fewer opportunities to land. Flag resolved.
#
# WHAT THIS DOES NOT FIX - READ BEFORE TRUSTING ANY PRICE FROM HERE.
# hold_claim is a faithful model of ONE of five shipped scenarios, and it is the
# most STATIC one. Escort (mobile, asymmetric), Raid (scoring in the enemy half),
# Sabotage (sudden death) and Power Supply (network, sudden death) are all
# unrepresented. Pricing the whole game against control play will systematically
# OVERVALUE defensive and static atoms - range, damage, armour - and UNDERVALUE
# mobility, tempo, stealth and objective-running, which is exactly what the four
# missing scenarios reward. Internally clean, structurally biased by what it was
# measured on: the DEX-ladder failure one level up.
# ---------------------------------------------------------------------------
PRICING_SCENARIOS = ("hold_claim",)
DIAGNOSTIC_SCENARIOS = ("annihilate", "hold")


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
    # structural zero with a real number halves it silently. Without this flag the
    # DEX ladder came out at exactly half its true value and looked plausible.
    #
    # ---------------------------------------------------------------------
    # THE THRESHOLD IS SOUND. ITS ORIGINAL EXPLANATION WAS NOT. Read this before
    # concluding anything from a cell this guard excludes.
    #
    # This comment used to say a uniform rifle mirror drew 100% of Hold games
    # because "both sides sit on their own objectives and neither can displace
    # the other". That is a statement about the GAME, and it was wrong. The crews
    # were not sitting on objectives - they were never REACHING one and never
    # CLAIMING one. Two missed legal actions (the AI never Sprinted, and never
    # took an objective Interact while it had a target), both fixed 2026-08-13.
    # Post-fix the same mirror draws ~34% and prices +1 Damage at +0.951 wp,
    # significant.
    #
    # The cost of the wrong explanation was not the guard - it was everything
    # reasoned downstream of it. Cells were excluded as legitimately unplayable,
    # rosters were built to avoid them, and the weapon-class damage ladder was
    # priced from a single scenario because the other one "could not resolve".
    # See docs: degeneracy-audit.
    #
    # SO: this flag means "this cell did not resolve", NEVER "this cell cannot
    # resolve". It is a symptom to investigate, not a property to design around.
    # If a cell degenerates, ask what legal action the AI failed to take before
    # concluding anything about the ruleset.
    # ---------------------------------------------------------------------
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

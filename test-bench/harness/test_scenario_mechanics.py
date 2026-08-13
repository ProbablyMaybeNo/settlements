"""Do the Sabotage and Raid MECHANICS work, with the AI taken out of the picture?

This exists to separate two failures that look identical from the outside:

  (a) the mechanic is broken    - charges never arm, caches never loot
  (b) the mechanic is fine but the AI never reaches it

Both produce 100% draws and zero interactions. Only (b) is a policy problem, and
the project has already been burned once by reading an AI limitation as a rules
finding (BALANCED_GOALS, and before that the advance/shoot defect). So the
mechanics are driven DIRECTLY here, with models placed in contact by hand.

    py -3.13 -m pytest test_scenario_mechanics.py -q
"""

from __future__ import annotations

import random
import sys

import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import measure as M  # noqa: E402
from board import take_a_hold  # noqa: E402


def _game(cls, kw=None, n=3):
    spec = [(f"U{i}", "Fighter", "rifle", "none", dict(int=4, dex=4, str=2))
            for i in range(n)]
    ca, _ = M.build(spec, 0)
    cb, _ = M.build(spec, 1)
    g = cls(ca, cb, take_a_hold(), **(kw or {}))
    g._spawn()
    return g


def test_sabotage_arms_when_in_contact():
    """A model standing on the enemy building arms a charge."""
    random.seed(1)
    g = _game(M.Sabotage)
    u = g.sides[0][0]
    u.pos = g.buildings[1]                      # stand on the enemy building
    armed = any(g.try_claim(u) or g.charge[1] is not None for _ in range(40))
    assert armed, "no charge ever armed from base contact over 40 attempts"
    assert g.charge[1] is not None


def test_sabotage_detonates_on_the_third_end_phase():
    """Armed and undefused, it goes off after CHARGE_FUSE End Phases, and the
    ARMING side wins."""
    g = _game(M.Sabotage)
    g.charge[1] = 0                              # a charge on side 1's building
    for rnd in range(1, M.CHARGE_FUSE + 1):
        g.score_objectives(rnd)
    assert g.over, "sudden death never triggered"
    assert g.detonated == 0, "the arming side (0) should win"
    # A detonation must outscore any possible tiebreak total, since the tiebreak
    # awards up to CHARGE_FUSE and sudden death has to beat it outright.
    assert g.vp[0] > M.CHARGE_FUSE and g.vp[1] == 0


def test_sabotage_round6_tiebreak_rewards_partial_countdown():
    """Scenarios.md sec 4: if neither detonates, the side whose charge reached the
    most countdown wins. Without this a failed-detonation game is a flat draw and
    throws away the whole difference between nearly winning and never crossing."""
    g = _game(M.Sabotage)
    g.rounds = 6
    g.charge[1] = 0                    # side 0 armed on side 1's building
    g.score_objectives(1)              # countdown 1
    g.charge[1] = None                 # defused before it could go off
    for rnd in range(2, 7):
        g.score_objectives(rnd)
    assert not g.over, "nothing should have detonated"
    assert g.vp[0] > g.vp[1], f"partial countdown should win: {g.vp}"


def test_sabotage_defuse_clears_the_charge():
    random.seed(3)
    g = _game(M.Sabotage)
    u = g.sides[1][0]
    u.stats["dex"] = 9                           # make the DEX test near-certain
    u.pos = g.buildings[1]                       # own building
    cleared = False
    for _ in range(40):
        g.charge[1] = 0
        g.try_claim(u)
        if g.charge[1] is None:
            cleared = True
            break
    assert cleared, "a high-DEX model never defused in 40 attempts"


def test_sabotage_nat1_detonates_immediately():
    """nat 1 on the defuse sets the fuse to full rather than clearing it."""
    g = _game(M.Sabotage)
    u = g.sides[1][0]
    u.pos = g.buildings[1]
    import engine as _e
    real = _e.d10
    try:
        _e.d10 = lambda: 1                        # force a natural 1
        g.charge[1] = 0
        g.try_claim(u)
        assert g.charge[1] == M.CHARGE_FUSE, "nat 1 did not arm it to full fuse"
    finally:
        _e.d10 = real


def test_sabotage_sudden_death_ends_the_game_early():
    """The `over` hook actually stops play(), rather than running to the round limit.

    try_claim is disabled for the duration. Without that, this test failed for a
    reason worth recording: side 1's models walk past their OWN building on the
    way out and DEFUSE the charge, so the game correctly drew. That is the
    mechanic working, not failing - but it means a live game cannot isolate the
    detonation path, so the interaction is stubbed out here.
    """
    g = _game(M.Sabotage)
    # Fuse set to complete on round 1. A full 3-round fuse raced the crews'
    # lethality - 3v3 riflemen wipe by round 2, so play() exited on the
    # standing-models check and the hook was never reached. That is a property of
    # the test crew, not of the hook, so the hook is tested directly.
    g.charge[1] = M.CHARGE_FUSE - 1
    real = M.Sabotage.try_claim
    try:
        M.Sabotage.try_claim = lambda self, u: False
        r = g.play()
    finally:
        M.Sabotage.try_claim = real
    assert len(g.timeline) == 1, f"sudden death did not stop round 1: {g.timeline}"
    assert g.over and g.detonated == 0
    assert r["winner"] == "A", f"arming side should win, got {r['winner']}"


@pytest.mark.xfail(reason=(
    "KNOWN GAP, not a regression: the AI has no DEFENSIVE assignment. Every model's "
    "goal is the enemy's building, so once the Sprint fix landed (2026-08-13) crews "
    "leave their own building behind at 12\"/round and never come back to defuse. "
    "Before the fix they defused incidentally, by walking past slowly - which is what "
    "this test was accidentally asserting. Sabotage says each crew nominates a "
    "building it must DEFEND, so a crew that sends everyone to attack is playing the "
    "scenario badly. Fixing it means splitting the crew between attack and defence, "
    "which is a policy DESIGN decision (how many defend?), not a missed legal action - "
    "so it is recorded here rather than guessed at. The defuse MECHANIC itself is "
    "still covered directly by test_sabotage_defuse_clears_the_charge."))
def test_sabotage_defenders_defuse_in_a_live_game():
    random.seed(13)
    defused = 0
    for _ in range(20):
        g = _game(M.Sabotage)
        g.charge[1] = 0
        g.play()
        if g.charge[1] is None:
            defused += 1
    assert defused > 0, "defenders never defused across 20 live games"


def test_raid_loots_enemy_cache_only():
    """Looting scores for the looter, and only the ENEMY's caches are lootable."""
    random.seed(5)
    g = _game(M.Raid)
    u = g.sides[0][0]
    u.pos = g.caches[1][0]                       # stand on an enemy cache
    for _ in range(40):
        g.try_claim(u)
        if g.looted[1]:
            break
    assert g.looted[1], "never looted an enemy cache in 40 attempts"
    assert g.vp[0] > 0, "looting scored nothing"
    assert not g.looted[0], "looted its own side's cache"


def test_raid_jackpot_is_worth_more():
    random.seed(7)
    g = _game(M.Raid)
    u = g.sides[0][0]
    u.stats["int"] = 9
    u.pos = g.caches[1][g.jackpot[1]]
    for _ in range(40):
        g.try_claim(u)
        if g.looted[1]:
            break
    assert g.vp[0] == M.JACKPOT_VP, f"jackpot scored {g.vp[0]}, expected {M.JACKPOT_VP}"


def test_raid_cache_cannot_be_looted_twice():
    random.seed(11)
    g = _game(M.Raid)
    u = g.sides[0][0]
    u.stats["int"] = 9
    u.pos = g.caches[1][0]
    for _ in range(40):
        g.try_claim(u)
        if g.looted[1]:
            break
    first = g.vp[0]
    for _ in range(20):
        g.try_claim(u)
    assert g.vp[0] == first, "the same cache scored more than once"


def test_goals_point_at_the_enemy_half():
    """The failure this guards: base _spawn assigns the NEAREST objective, which
    for these scenarios is a model's own building/cache - so every model would
    defend, nobody would attack, and the scenario would draw 100% by construction
    while looking like a balance result."""
    for cls, key in ((M.Sabotage, "buildings"), (M.Raid, "caches")):
        g = _game(cls)
        for side in (0, 1):
            own_y = 9.0 if side == 0 else 27.0
            for u in g.sides[side]:
                assert u.goal is not None
                # the enemy half is the far side of the centreline from own_y
                assert (u.goal[1] > 18.0) == (own_y < 18.0), \
                    f"{cls.__name__} side {side} goal {u.goal} is in its OWN half"

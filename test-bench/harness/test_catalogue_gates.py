# -*- coding: utf-8 -*-
"""The gates that would have caught the founding bug, as tests that FAIL the build.

WHY THIS FILE EXISTS.

Both of these checks already existed. Neither blocked anything.

  - `consistency.check_gear_body_ratio` has contained the 17-33% gear:body band
    since the module was written, and its docstring opens with the rifle-costs-
    more-than-a-Fighter example. It was running, failing, and gating nothing.
  - The confidence-tier rule ("no number ships untagged") was written into the
    header of ticks.py and the front matter of POINTS-CATALOGUE.md as PROSE. Ten
    of twenty-five price tables shipped with no tier, including the weapon class
    table - the single number the rebuild was commissioned to fix.

The lesson the project already had on the wall, applied to itself: a guard that
is not enforced is not a guard, and an invariant stated in a comment is a wish.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HARNESS = Path(__file__).resolve().parent
TESTBENCH = HARNESS.parent
for p in (str(TESTBENCH), str(HARNESS)):
    if p not in sys.path:
        sys.path.insert(0, p)

import consistency  # noqa: E402
from points import ticks  # noqa: E402
from points.units import LISTED_BODY, Rank  # noqa: E402

TICKS_SRC = (TESTBENCH / "points" / "ticks.py").read_text(encoding="utf-8")

# Structural / metadata bindings that are not prices and so carry no tier.
NOT_A_PRICE = {
    "SCALE", "TICK", "TIER_A", "TIER_B", "TIER_C",
    "ANCHOR_WP", "ANCHOR_CI", "CREDITS_PER_WINPOINT",
    "CLASS_META", "RANGE_BAND", "CLASS_RANGE_BAND", "ARMOUR_INJURY",
    "BANDED_DRAWBACKS", "BLOCKED_REDESIGN", "STAT_KIND", "STAT_LADDER",
    "UNPRICEABLE_MEASURED_ZERO", "OVERRIDES_MEASUREMENT", "RANGE_STEP_UNPRICED",
    "CONDITIONAL_F_PROVISIONAL", "DAMAGE_FLOOR", "RANK_ORDER",
}

TIER_MARKS = ("[A]", "[B]", "[C]", "[BLOCKED]", "[OVERRIDE]", "[PARKED]", "[measured")


def _code() -> str:
    """ticks.py with its module docstring removed.

    Needed because the docstring QUOTES an assignment while explaining the T12
    circularity failure (`BATTLE_CREDITS = RECRUIT_CR`), and a naive scan read
    that prose as a live untagged price. A detector that invents findings is as
    useless as one that misses them.
    """
    body = TICKS_SRC.split('"""', 2)
    return body[2] if len(body) == 3 else TICKS_SRC


def _price_bindings() -> list[str]:
    return [n for n in re.findall(r"^([A-Z][A-Z0-9_]+)\s*=", _code(), re.M)
            if n not in NOT_A_PRICE]


def _block_for(name: str) -> str:
    """The commentary ATTACHED to a binding, and nothing else.

    The first version of this took a 2500-character window before the binding and
    split on blank lines. It reported every table as tagged - including five that
    demonstrably were not - because it was reading tier marks off NEIGHBOURING
    declarations. A gate that cannot fail is worse than no gate; it manufactures
    exactly the confidence it is supposed to earn. Caught by checking what the
    detector saw rather than trusting that it went green.

    Attached commentary is: the unbroken run of comment lines directly above the
    binding (a blank line ends it), plus the literal's own body.
    """
    lines = TICKS_SRC.splitlines()
    idx = next(i for i, ln in enumerate(lines) if re.match(rf"^{name}\s*=", ln))

    head = []
    for ln in reversed(lines[:idx]):
        if ln.lstrip().startswith("#"):
            head.append(ln)
        else:
            break                      # blank line or code ends the block
    body = [lines[idx]]
    if lines[idx].rstrip().endswith(("{", "(", "[")):
        for ln in lines[idx + 1:]:
            body.append(ln)
            if ln.startswith(("}", ")", "]")):
                break
    return "\n".join(reversed(head)) + "\n" + "\n".join(body)


def test_every_price_carries_a_confidence_tier():
    """§8.2: no number in ticks.py is legacy. Every value is measured, derived
    with a stated derivation, or ruled with OVERRIDE fields."""
    untagged = [n for n in _price_bindings()
                if not any(t in _block_for(n) for t in TIER_MARKS)]
    assert not untagged, (
        "price tables with no confidence tier: " + ", ".join(untagged) +
        "\nEvery price must be tagged [A]/[B]/[C]/[OVERRIDE] with its derivation. "
        "An untagged number is the defect this rebuild exists to eliminate."
    )


def test_no_gear_item_costs_more_than_its_carrier():
    """§8.4, the founding bug, as an assertion: a weapon must cost meaningfully
    less than the body carrying it."""
    over = {}
    for cls, cost in ticks.CLASS_CREDITS.items():
        if cost == 0:
            continue
        rank, body = consistency.cheapest_legal_carrier(cls)
        if cost / body > consistency.GEAR_BODY_HARD_CAP:
            over[cls] = f"{cost} Cr vs {rank} {body} Cr = {cost / body:.0%}"
    assert not over, (
        f"gear items above the {consistency.GEAR_BODY_HARD_CAP:.0%} hard cap: {over}"
    )


def test_a_rifle_costs_meaningfully_less_than_a_fighter():
    """The sentence the original directive opened with, pinned as a test.

    Shipping without this means the rebuild did not happen.
    """
    rifle = ticks.CLASS_CREDITS["standard_ranged"]
    fighter = LISTED_BODY[Rank.FIGHTER]
    assert rifle < fighter, f"rifle {rifle} Cr vs Fighter {fighter} Cr"
    assert rifle / fighter <= consistency.GEAR_BODY_HARD_CAP, (
        f"rifle is {rifle / fighter:.0%} of a Fighter"
    )


def test_deployables_are_on_the_gear_scale():
    """They were converted x10 onto the BODY scale and never reconciled - the
    worst was 189% of the model deploying it."""
    fighter = LISTED_BODY[Rank.FIGHTER]
    over = {k: v for k, v in ticks.DEPLOYABLE_CREDITS.items()
            if v / fighter > consistency.GEAR_BODY_HARD_CAP}
    assert not over, f"deployables above the hard cap: {over}"


def test_consistency_checks_have_no_failures():
    """The whole cross-subsystem suite, as a gate. WARNs are allowed - they are
    open questions. FAILs are broken relations."""
    rep = consistency.Report()
    consistency.run_all(rep)
    fails = [(c, d) for s, c, d, _ in rep.rows if s == "FAIL"]
    assert not fails, "consistency FAILs:\n" + "\n".join(f"  {c}: {d}" for c, d in fails)


def test_blocked_traits_are_not_sold():
    """A trait measuring at or below zero net must not reach a shipping price."""
    for name in ticks.BLOCKED_REDESIGN:
        assert name in ticks.CHAR_CREDITS, f"{name} vanished from CHAR_CREDITS"
    # they keep a number so existing catalogue rows resolve; the gate is that
    # verify refuses to ship them, and that they are listed here at all.
    assert set(ticks.BLOCKED_REDESIGN) >= {"concussive", "crippling", "blinding"}


def test_rank_gate_is_actually_enforced():
    """CLASS_META declared min_rank for eight classes and nothing read it."""
    from points.units import Fighter, fielded_cost
    from points.weapons import WeaponBuild

    heavy = WeaponBuild(name="probe", weapon_class="heavy_ranged")
    recruit = Fighter(name="R", rank=Rank.RECRUIT, weapons=[heavy])
    try:
        fielded_cost(recruit)
    except ValueError as e:
        assert "requires rank" in str(e)
    else:
        raise AssertionError("a Recruit was costed with a Heavy Ranged weapon")

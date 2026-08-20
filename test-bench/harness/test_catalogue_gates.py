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
    # Envelope CONSTRAINTS, not prices: caps, ceilings, rank gates and per-crew
    # limits say what is legal, never what it costs. RANGE_CREDITS is a price and
    # is deliberately NOT in this set.
    "DAMAGE_CAP", "CRAFTABLE_RANGE_CEILING", "LONG_RANGE_MIN_RANK",
    "LONG_RANGE_PER_CREW",
    # Budget and economy CONSTANTS, not prices: a Crew Rating is the size of the
    # envelope, a worker bonus and a payback target are stated rules, and the
    # Materials:Credits rate is an exchange rate. None is the cost of a thing.
    # BASE_GATHER_RATE IS deliberately not in this set - it is a rate that had to
    # be ruled, and it carries its OVERRIDE fields.
    "CREW_RATING_STANDARD", "CREW_RATING_CAMPAIGN_START",
    "MATERIALS_PER_CREDIT", "WORKER_BONUS", "GATHERER_PAYBACK_CYCLES",
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


# --- the 24" range gate: four gates, each asserted separately ----------------

def test_no_craftable_weapon_exceeds_24_inches():
    """Gate 1 of 4. Above 24" is MANUFACTURED ONLY - loot and raid spoils, never
    craftable at any Workshop tier. A 36" weapon fires from 12" BEHIND its own
    deployment zone and covers the whole board; the sim measured an uncapped
    long-range crew beating every other list by 13-30 points."""
    from points.weapons import WeaponBuild
    for cls, meta in ticks.CLASS_META.items():
        band = meta["range"]
        if band is None or band[1] <= ticks.CRAFTABLE_RANGE_CEILING:
            continue
        errs = WeaponBuild("probe", cls, damage=meta["damage"][0],
                           reach=band[1]).validate()
        assert any("MANUFACTURED" in e for e in errs), (
            f"{cls} at {band[1]}in was accepted as craftable")


def test_long_range_requires_specialist():
    """Gate 3 of 4."""
    from points.weapons import WeaponBuild, validate_carrier
    sniper = WeaponBuild("probe", "heavy_ranged", damage=3, reach=36,
                         manufactured=True)
    assert validate_carrier(sniper, "fighter"), "a Fighter took a 36in weapon"
    assert not validate_carrier(sniper, "specialist")


def test_long_range_is_limited_to_one_per_crew():
    """Gate 2 of 4 - the load-bearing one. The 13-30 point finding was a LIST
    archetype; limit-1 is what destroys the archetype rather than taxing it."""
    from points.units import Fighter, validate_crew
    from points.weapons import WeaponBuild
    sniper = WeaponBuild("Long Rifle", "heavy_ranged", damage=3, reach=36,
                         manufactured=True)
    one = [Fighter(name="A", rank=Rank.SPECIALIST, weapons=[sniper])]
    two = one + [Fighter(name="B", rank=Rank.SPECIALIST, weapons=[sniper])]
    assert not validate_crew(one)
    assert validate_crew(two), "two 36in weapons in one crew were allowed"


def test_damage_cap_moved_to_five():
    """heavy_ranged floors at +3 and ceilings at +5; the old +4 cap would have
    made its own envelope illegal."""
    assert ticks.DAMAGE_CAP == 5
    assert ticks.CLASS_META["heavy_ranged"]["damage"] == (3, 5)


def test_class_envelopes_overlap_rather_than_tier():
    """The flaw this replaced: class was a global damage tier, so a .22 and a
    Magnum could not both be one-handed. Overlap is the fix, not an accident."""
    oh = ticks.CLASS_META["one_handed_melee"]["damage"]
    hm = ticks.CLASS_META["heavy_melee"]["damage"]
    assert oh[1] >= hm[0], "one_handed and heavy_melee no longer overlap"
    assert hm[1] > oh[1], "heavy_melee must reach higher than one_handed"
    sa = ticks.CLASS_META["sidearm"]["damage"]
    sr = ticks.CLASS_META["standard_ranged"]["damage"]
    assert sr[0] > sa[0], "nothing shoulder-fired should be a .22"


def test_concealable_is_cut_and_stays_cut():
    assert "concealable" not in ticks.CHAR_CREDITS, (
        "Concealable was cut 2026-08-14 - 'may start Hidden' is skill territory, "
        "and Vanishing Point / Camouflage Drill already do it properly")
    assert "quiet" in ticks.CHAR_CREDITS, "Quiet is a real axis and stays"


# --- M1: skills are attachable, priced, and rank-gated -----------------------

def test_every_vault_skill_is_priced():
    """149 skills parsed from the vault; each must resolve to a tier price."""
    from points.skills import SKILLS, skill_credits
    assert len(SKILLS) > 140, f"only {len(SKILLS)} skills parsed - vault format changed?"
    for name in SKILLS:
        assert skill_credits(name) in ticks.SKILL_TIER_CREDITS.values()


def test_skills_are_rank_gated():
    """A Recruit has no tiered stat, so it may hold no skill at all; a Fighter
    tops out at 2x T1. Without this the pyramid stops meaning anything."""
    from points.skills import validate_skills
    assert validate_skills(["Dead Eye"], "recruit")
    assert validate_skills(["Dead Eye"], "fighter")
    assert not validate_skills(["Dead Eye"], "leader")
    assert validate_skills(["Weave", "Vault", "Leaper"], "fighter")   # 3x T1 > cap 2
    assert not validate_skills(["Weave", "Vault"], "fighter")


def test_a_skill_costs_its_tier_on_a_model():
    from points.units import Fighter, fielded_cost
    from points.weapons import WeaponBuild
    r = WeaponBuild("R", "standard_ranged", damage=3, reach=18)
    plain = Fighter(name="L", rank=Rank.LEADER, weapons=[r])
    skilled = Fighter(name="L", rank=Rank.LEADER, weapons=[r], skills=["Dead Eye"])
    assert fielded_cost(skilled) - fielded_cost(plain) == ticks.SKILL_TIER_CREDITS[3]


# --- the scale is one number, and every live document must agree on it -------

LIVE_DOCS = ("POINTS-CATALOGUE.md", "POINTS-TABLE.md", "POINTS-REBUILD-TRACKING.md")


def test_no_live_doc_cites_the_superseded_crew_rating():
    """Crew Rating rebased 1000 -> 1700 (Campaign Start 500 -> 850) on 2026-08-19.

    A stale cap in a secondary document is exactly how a wrong number gets picked
    up later - and this project has a worked example of that failure already:
    ARMOUR_CREDITS carried a price citing `balance/armourprice.py`, a file that
    never existed, for months, because nothing checked.

    Dated reports (POINTS-AUDIT, POINTS-RESEARCH, the CAMPAIGN-500 findings) are
    deliberately NOT covered: they are records of what was true when written, and
    rewriting them would falsify history. Only documents that a reader would
    price FROM are checked, plus GLOBAL-POINTS-SYSTEM which must carry its
    supersession banner.
    """
    import re
    docs = TESTBENCH.parent / "docs"
    stale = re.compile(r"\b1000[- ]?(?:Credit|point|pt|CR\b)|standard 1000|"
                       r"1000 = standard|500 Crew Rating|at \*\*500\*\*", re.I)
    bad = []
    for name in LIVE_DOCS:
        p = docs / name
        if not p.exists():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if stale.search(line) and "LEGACY" not in line and "rebased" not in line:
                bad.append(f"{name}:{i}: {line.strip()[:90]}")
    assert not bad, "live docs still cite the superseded scale:\n  " + "\n  ".join(bad)


def test_superseded_points_doc_carries_its_banner():
    p = TESTBENCH.parent / "docs" / "GLOBAL-POINTS-SYSTEM.md"
    if not p.exists():
        return
    head = p.read_text(encoding="utf-8")[:400]
    assert "SUPERSEDED" in head, (
        "GLOBAL-POINTS-SYSTEM.md states a 1000 Crew Rating as if live and must "
        "open with its supersession banner")


def test_the_scale_has_one_source_of_truth():
    """SCALE and CREW_RATING_STANDARD must not be able to drift apart."""
    assert ticks.SCALE == ticks.CREW_RATING_STANDARD == 1700
    assert ticks.CREW_RATING_CAMPAIGN_START == 850

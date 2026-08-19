"""Rank body Credits, Advances, and fielded crew rating."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .ticks import BODY_BASE, ORDER_PREMIUM, SKILL_TIER_CREDITS, TICK_STAT
from .weapons import WeaponBuild, weapon_cost


class Rank(str, Enum):
    RECRUIT = "recruit"
    FIGHTER = "fighter"
    SPECIALIST = "specialist"
    LEADER = "leader"


RANK_STAT_POINTS = {
    Rank.RECRUIT: 3,
    Rank.FIGHTER: 5,
    Rank.SPECIALIST: 7,
    Rank.LEADER: 9,
}

RANK_ORDERS = {
    Rank.RECRUIT: 0,
    Rank.FIGHTER: 0,
    Rank.SPECIALIST: 1,
    Rank.LEADER: 2,
}


# The max-value stat build each rank can legally reach (POINTS-TABLE sec 3).
# A rank's stat POINTS are spread across stats, and the measured ladder prices a
# RUNG, so the shape of the spread decides the cost. These are the shapes the
# rank table itself names.
RANK_STAT_SHAPE = {
    Rank.RECRUIT: (1, 1, 1),
    Rank.FIGHTER: (2, 2, 1),
    Rank.SPECIALIST: (4, 2, 1),
    Rank.LEADER: (6, 2, 1),
}


def _ladder_total(to_rung: int) -> int:
    """Running cost of taking one stat from 0 to `to_rung` on the MEASURED
    one-sided ladder (37/26/27/18/15/10)."""
    from .ticks import STAT_LADDER
    rungs = STAT_LADDER["one_sided"]
    return sum(rungs[r] for r in range(1, to_rung + 1))


def body_cost(rank: Rank) -> int:
    """RE-DERIVED FROM THE MEASURED STAT LADDER - 2026-08-19.

    This was `BODY_BASE + stat_points * TICK_STAT + orders`, i.e. a FLAT 15 per
    stat point. The flat 15 is measurably wrong in both directions: the measured
    one-sided ladder runs 37 at the first rung down to 10 at the sixth, a 3.6x
    spread, because a stat tested against a fixed TN saturates.

    TWO INDEPENDENT LINES OF EVIDENCE FORCED THIS, and they agree:

      1. The gear:body ratio check. Against legacy bodies, 12 of 19 catalogue
         weapons cost more than 40% of the cheapest body able to carry them -
         a rifle was 63% of a Fighter. Against measured bodies, ZERO exceed it.
      2. The catalogue validation (`catalogue-validation-n1500`). At equal Crew
         Rating a 7-model Horde beat a 4-model Elite 69-31, Armoured 65-35 and
         Assault 70-30. More cheap bodies beat fewer good ones.

    Both say the same thing from opposite directions: BODIES WERE TOO CHEAP.
    That is also the D21 model-count question re-run honestly for the first time
    - the tracking doc records the original as contaminated, because it compared
    crew sizes on a scenario that could not score.
    """
    from .ticks import BODY_BASE, ORDER_PREMIUM
    return (
        BODY_BASE
        + sum(_ladder_total(r) for r in RANK_STAT_SHAPE[rank])
        + ORDER_PREMIUM[RANK_ORDERS[rank]]
    )


# The listed ladder IS the derived one as of 2026-08-19. It used to be a
# hand-written table that happened to match the flat-15 formula; keeping a
# separate literal now would just be a second place for the ladder to go stale.
LISTED_BODY = {rank: body_cost(rank) for rank in Rank}


def listed_body_cost(rank: Rank) -> int:
    return LISTED_BODY[rank]


def advance_stat() -> int:
    """points added when an Advance grants +1 to a path-stat."""
    return TICK_STAT


def advance_skill(tier: int) -> int:
    if tier not in SKILL_TIER_CREDITS:
        raise ValueError(f"skill tier must be 1–3, got {tier}")
    return SKILL_TIER_CREDITS[tier]


def promotion_cost(from_rank: Rank, to_rank: Rank) -> int:
    return listed_body_cost(to_rank) - listed_body_cost(from_rank)


@dataclass
class Fighter:
    name: str
    rank: Rank
    advance_points: int = 0  # sum of Advance Δpoints over campaign
    weapons: list[WeaponBuild] = field(default_factory=list)
    armour: str = "thick_clothing"
    equipment: list[str] = field(default_factory=list)  # keys in tick tables
    skills: list[str] = field(default_factory=list)     # names in points.skills
    equipped: bool = True  # False = stashed body? (normally fighters are owned)


def armour_points(armour: str) -> int:
    from .ticks import ARMOUR_CREDITS

    if armour not in ARMOUR_CREDITS:
        raise ValueError(f"unknown armour {armour!r}")
    return ARMOUR_CREDITS[armour]


def equipment_points(item: str) -> int:
    from .ticks import EQUIPMENT_CREDITS, HACK_GEAR_CREDITS

    if item in EQUIPMENT_CREDITS:
        return EQUIPMENT_CREDITS[item]
    if item in HACK_GEAR_CREDITS:
        return HACK_GEAR_CREDITS[item]
    raise ValueError(f"unknown equipment {item!r}")


def fielded_cost(fighter: Fighter) -> int:
    """points rating contribution when this fighter is listed for battle.

    The rank gate is enforced HERE and not in WeaponBuild, because a weapon build
    is a catalogue entry and has no carrier until it is put on one. Costing a
    fighter is the first moment the pair exists.
    """
    from .skills import skill_credits, validate_skills
    from .weapons import validate_carrier

    gate = [e for w in fighter.weapons for e in validate_carrier(w, fighter.rank.value)]
    # Skills are rank-gated the same way weapons are: a rank may only hold the
    # tiers its stat line unlocks. Without this a Recruit could carry a T3 and
    # the pyramid stops meaning anything.
    gate += validate_skills(fighter.skills, fighter.rank.value)
    if gate:
        raise ValueError("; ".join(gate))
    total = listed_body_cost(fighter.rank) + fighter.advance_points
    total += armour_points(fighter.armour)
    for w in fighter.weapons:
        total += weapon_cost(w)
    for e in fighter.equipment:
        total += equipment_points(e)
    for sk in fighter.skills:
        total += skill_credits(sk)
    return total


def validate_crew(fighters: list[Fighter]) -> list[str]:
    """Crew-level legality. Gate 2 of 4 on the 24" line lives here, because
    "limit 1 per crew" is the only one of the four that cannot be checked on a
    single weapon or a single fighter."""
    from .ticks import LONG_RANGE_PER_CREW, is_long_range

    errs = []
    long_guns = [(f.name, w.name) for f in fighters for w in f.weapons
                 if is_long_range(w.picked_reach())]
    if len(long_guns) > LONG_RANGE_PER_CREW:
        errs.append(
            f"{len(long_guns)} weapons over 24\" - limit is {LONG_RANGE_PER_CREW} "
            f"per crew: " + ", ".join(f"{w} ({f})" for f, w in long_guns))
    return errs


def crew_rating(fighters: list[Fighter]) -> int:
    return sum(fielded_cost(f) for f in fighters)

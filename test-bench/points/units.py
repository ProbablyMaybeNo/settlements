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


def body_cost(rank: Rank) -> int:
    return (
        BODY_BASE
        + RANK_STAT_POINTS[rank] * TICK_STAT
        + ORDER_PREMIUM[RANK_ORDERS[rank]]
    )


# v0 listed ladder (may diverge from pure derived later)
LISTED_BODY = {
    Rank.RECRUIT: 65,
    Rank.FIGHTER: 95,
    Rank.SPECIALIST: 165,
    Rank.LEADER: 245,
}


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
    from .weapons import validate_carrier

    gate = [e for w in fighter.weapons for e in validate_carrier(w, fighter.rank.value)]
    if gate:
        raise ValueError("; ".join(gate))
    total = listed_body_cost(fighter.rank) + fighter.advance_points
    total += armour_points(fighter.armour)
    for w in fighter.weapons:
        total += weapon_cost(w)
    for e in fighter.equipment:
        total += equipment_points(e)
    return total


def crew_rating(fighters: list[Fighter]) -> int:
    return sum(fielded_cost(f) for f in fighters)

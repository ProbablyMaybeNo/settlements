"""Rank body Goods, Advances, and fielded crew rating."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .ticks import BODY_BASE, ORDER_PREMIUM, SKILL_TIER_GOODS, TICK_STAT
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
    """Goods added when an Advance grants +1 to a path-stat."""
    return TICK_STAT


def advance_skill(tier: int) -> int:
    if tier not in SKILL_TIER_GOODS:
        raise ValueError(f"skill tier must be 1–3, got {tier}")
    return SKILL_TIER_GOODS[tier]


def promotion_cost(from_rank: Rank, to_rank: Rank) -> int:
    return listed_body_cost(to_rank) - listed_body_cost(from_rank)


@dataclass
class Fighter:
    name: str
    rank: Rank
    advance_goods: int = 0  # sum of Advance Δgoods over campaign
    weapons: list[WeaponBuild] = field(default_factory=list)
    armour: str = "thick_clothing"
    equipment: list[str] = field(default_factory=list)  # keys in tick tables
    equipped: bool = True  # False = stashed body? (normally fighters are owned)


def armour_goods(armour: str) -> int:
    from .ticks import ARMOUR_GOODS

    if armour not in ARMOUR_GOODS:
        raise ValueError(f"unknown armour {armour!r}")
    return ARMOUR_GOODS[armour]


def equipment_goods(item: str) -> int:
    from .ticks import EQUIPMENT_GOODS, HACK_GEAR_GOODS

    if item in EQUIPMENT_GOODS:
        return EQUIPMENT_GOODS[item]
    if item in HACK_GEAR_GOODS:
        return HACK_GEAR_GOODS[item]
    raise ValueError(f"unknown equipment {item!r}")


def fielded_cost(fighter: Fighter) -> int:
    """Goods rating contribution when this fighter is listed for battle."""
    total = listed_body_cost(fighter.rank) + fighter.advance_goods
    total += armour_goods(fighter.armour)
    for w in fighter.weapons:
        total += weapon_cost(w)
    for e in fighter.equipment:
        total += equipment_goods(e)
    return total


def crew_rating(fighters: list[Fighter]) -> int:
    return sum(fielded_cost(f) for f in fighters)

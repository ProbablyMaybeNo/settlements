"""Settlements global Credits engine — designer/sim only (1000-Credit scale)."""

from .ticks import TICK, SCALE
from .weapons import weapon_cost, WeaponBuild
from .credits import crew_rating, headroom, legal
from .units import body_cost, fielded_cost, Rank, advance_stat, advance_skill
from .structures import materials_cost, StructureSpec

__all__ = [
    "TICK",
    "SCALE",
    "weapon_cost",
    "WeaponBuild",
    "body_cost",
    "fielded_cost",
    "Rank",
    "advance_stat",
    "advance_skill",
    "crew_rating",
    "headroom",
    "legal",
    "materials_cost",
    "StructureSpec",
]

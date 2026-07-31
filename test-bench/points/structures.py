"""Structure Materials cost derivation (not battle Goods)."""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil

from .ticks import (
    FOOTPRINT_BAND,
    GROUNDWORKS_MAT,
    POWER_MAT,
    ROLE_BAND,
    UPGRADE_MULT,
)


@dataclass(frozen=True)
class StructureSpec:
    name: str
    footprint: str  # station | plant | building | large | line | yard
    role: str  # sustain | gatherer | convert | operate | recover | defend
    tier: int = 1  # 1–3 → Power draw
    starter: bool = False

    @property
    def power_draw(self) -> int:
        if self.name.lower() == "generator":
            return 0
        return self.tier  # D9: T1=1, T2=2, T3=3


def materials_cost(spec: StructureSpec) -> int:
    if spec.footprint not in FOOTPRINT_BAND:
        raise ValueError(f"unknown footprint {spec.footprint!r}")
    if spec.role not in ROLE_BAND:
        raise ValueError(f"unknown role {spec.role!r}")
    if spec.tier not in (1, 2, 3):
        raise ValueError(f"tier must be 1–3, got {spec.tier}")

    base = FOOTPRINT_BAND[spec.footprint] + ROLE_BAND[spec.role]
    base += spec.power_draw * POWER_MAT

    # Tier 2/3 are priced as cumulative Materials to reach that tier from nothing
    if spec.tier == 1:
        return base
    t2 = ceil(base * UPGRADE_MULT[2])
    if spec.tier == 2:
        return t2
    return ceil(t2 * UPGRADE_MULT[3])


def groundworks_cost(level: int) -> int:
    if level not in GROUNDWORKS_MAT:
        raise ValueError("groundworks level must be 1 or 2")
    return GROUNDWORKS_MAT[level]


def materials_breakdown(spec: StructureSpec) -> dict:
    cost = materials_cost(spec)
    return {
        "name": spec.name,
        "footprint": spec.footprint,
        "role": spec.role,
        "tier": spec.tier,
        "power_draw": spec.power_draw,
        "materials": cost,
        "starter": spec.starter,
    }

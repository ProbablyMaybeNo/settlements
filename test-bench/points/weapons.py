"""Weapon Credits cost = class + characteristics + drawbacks."""

from __future__ import annotations

from dataclasses import dataclass

from .ticks import (
    BANDED_DRAWBACKS,
    CHAR_CREDITS,
    CLASS_CREDITS,
    CLASS_META,
    DRAWBACK_CREDITS,
    SHORT_RANGE_REFUND,
)


def drawback_points(drawback: str, weapon_class: str) -> int:
    """Refund for one drawback on one class. Short Range is banded (M3)."""
    if drawback in BANDED_DRAWBACKS:
        if weapon_class not in SHORT_RANGE_REFUND:
            raise ValueError(
                f"{drawback!r} has no band for class {weapon_class!r} - a melee "
                "weapon has no range to halve"
            )
        return SHORT_RANGE_REFUND[weapon_class]
    return DRAWBACK_CREDITS[drawback]


@dataclass(frozen=True)
class WeaponBuild:
    name: str
    weapon_class: str
    characteristics: tuple[str, ...] = ()
    drawbacks: tuple[str, ...] = ()

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.weapon_class not in CLASS_CREDITS:
            errs.append(f"unknown class {self.weapon_class!r}")
            return errs
        meta = CLASS_META[self.weapon_class]
        if len(self.characteristics) > meta["slots"]:
            errs.append(
                f"{self.name}: {len(self.characteristics)} chars > {meta['slots']} slots"
            )
        if len(self.drawbacks) > 2:
            errs.append(f"{self.name}: max 2 drawbacks")
        for c in self.characteristics:
            if c not in CHAR_CREDITS:
                errs.append(f"{self.name}: unknown characteristic {c!r}")
        for d in self.drawbacks:
            if d not in DRAWBACK_CREDITS and d not in BANDED_DRAWBACKS:
                errs.append(f"{self.name}: unknown drawback {d!r}")
            elif d in BANDED_DRAWBACKS and self.weapon_class not in SHORT_RANGE_REFUND:
                errs.append(
                    f"{self.name}: {d} on {self.weapon_class} - no range to halve"
                )
        dmg = meta["damage"] + (1 if "brutal" in self.characteristics else 0)
        if dmg > 4:
            errs.append(f"{self.name}: damage {dmg} exceeds +4 cap")
        if "brutal" in self.characteristics and self.weapon_class in {
            "sidearm",
            "standard_ranged",
            "heavy_ranged",
            "thrown",
        }:
            if "short_range" not in self.drawbacks:
                errs.append(f"{self.name}: Brutal on ranged requires Short Range")
        return errs


RANK_ORDER = ("recruit", "fighter", "specialist", "leader")


def can_carry(weapon_class: str, rank: str) -> bool:
    """Is `rank` allowed this class? CLASS_META has declared a min_rank for all
    eight classes since the table was written and NOTHING HAS EVER READ IT.

    That is not cosmetic. Every gear:body ratio in the catalogue is measured
    against "the cheapest body legally able to carry this", so an unenforced gate
    means the denominator in the founding-bug check was itself unverified — a
    Recruit could be costed with a Heavy Ranged and nothing objected.
    """
    meta = CLASS_META.get(weapon_class)
    if meta is None:
        raise ValueError(f"unknown class {weapon_class!r}")
    min_rank = meta.get("min_rank", "recruit")
    if rank not in RANK_ORDER:
        raise ValueError(f"unknown rank {rank!r}")
    return RANK_ORDER.index(rank) >= RANK_ORDER.index(min_rank)


def validate_carrier(build: "WeaponBuild", rank: str) -> list[str]:
    """Errors from putting this weapon on a fighter of `rank`."""
    if not can_carry(build.weapon_class, rank):
        need = CLASS_META[build.weapon_class]["min_rank"]
        return [f"{build.name}: {build.weapon_class} requires rank {need}, "
                f"carrier is {rank}"]
    return []


def weapon_cost(build: WeaponBuild) -> int:
    errs = build.validate()
    if errs:
        raise ValueError("; ".join(errs))
    total = CLASS_CREDITS[build.weapon_class]
    total += sum(CHAR_CREDITS[c] for c in build.characteristics)
    total += sum(drawback_points(d, build.weapon_class) for d in build.drawbacks)
    return total


def weapon_cost_breakdown(build: WeaponBuild) -> dict:
    from .ticks import CLASS_RANGE_BAND, RANGE_BAND

    cost = weapon_cost(build)
    band = CLASS_RANGE_BAND[build.weapon_class]
    return {
        "name": build.name,
        "class": build.weapon_class,
        "class_points": CLASS_CREDITS[build.weapon_class],
        "range_band": band,
        "range_inches": RANGE_BAND[band],
        "characteristics": {c: CHAR_CREDITS[c] for c in build.characteristics},
        "drawbacks": {
            d: drawback_points(d, build.weapon_class) for d in build.drawbacks
        },
        "total": cost,
    }

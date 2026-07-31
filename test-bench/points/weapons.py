"""Weapon Goods cost = class + characteristics + drawbacks."""

from __future__ import annotations

from dataclasses import dataclass

from .ticks import CHAR_GOODS, CLASS_GOODS, CLASS_META, DRAWBACK_GOODS


@dataclass(frozen=True)
class WeaponBuild:
    name: str
    weapon_class: str
    characteristics: tuple[str, ...] = ()
    drawbacks: tuple[str, ...] = ()

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.weapon_class not in CLASS_GOODS:
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
            if c not in CHAR_GOODS:
                errs.append(f"{self.name}: unknown characteristic {c!r}")
        for d in self.drawbacks:
            if d not in DRAWBACK_GOODS:
                errs.append(f"{self.name}: unknown drawback {d!r}")
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


def weapon_cost(build: WeaponBuild) -> int:
    errs = build.validate()
    if errs:
        raise ValueError("; ".join(errs))
    total = CLASS_GOODS[build.weapon_class]
    total += sum(CHAR_GOODS[c] for c in build.characteristics)
    total += sum(DRAWBACK_GOODS[d] for d in build.drawbacks)
    return total


def weapon_cost_breakdown(build: WeaponBuild) -> dict:
    cost = weapon_cost(build)
    return {
        "name": build.name,
        "class": build.weapon_class,
        "class_goods": CLASS_GOODS[build.weapon_class],
        "characteristics": {c: CHAR_GOODS[c] for c in build.characteristics},
        "drawbacks": {d: DRAWBACK_GOODS[d] for d in build.drawbacks},
        "total": cost,
    }

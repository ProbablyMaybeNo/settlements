"""Weapon Credits cost = class + characteristics + drawbacks."""

from __future__ import annotations

from dataclasses import dataclass

from .ticks import (
    BANDED_DRAWBACKS,
    CHAR_CREDITS,
    CLASS_CREDITS,
    CLASS_META,
    DAMAGE_CAP,
    DRAWBACK_CREDITS,
    LONG_RANGE_MIN_RANK,
    SHORT_RANGE_REFUND,
    class_base,
    damage_credits,
    is_long_range,
    range_credits,
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
    """A specific weapon, not a class.

    `damage` and `reach` are PICKS inside the class envelope. Leaving them None
    takes the class floor, which is what every pre-envelope build did implicitly.
    """
    name: str
    weapon_class: str
    characteristics: tuple[str, ...] = ()
    drawbacks: tuple[str, ...] = ()
    damage: int | None = None
    reach: int | None = None          # inches; None = melee or class floor
    manufactured: bool = False        # loot/raid spoils, not craftable

    def _meta(self) -> dict:
        return CLASS_META[self.weapon_class]

    def picked_damage(self) -> int:
        return self._meta()["damage"][0] if self.damage is None else self.damage

    def picked_reach(self):
        band = self._meta()["range"]
        if band is None:
            return None
        return band[0] if self.reach is None else self.reach

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.weapon_class not in CLASS_CREDITS:
            errs.append(f"unknown class {self.weapon_class!r}")
            return errs
        meta = CLASS_META[self.weapon_class]

        # --- the envelope: damage and reach must sit inside the class band ---
        lo, hi = meta["damage"]
        d = self.picked_damage()
        if not (lo <= d <= hi):
            errs.append(f"{self.name}: damage +{d} outside {self.weapon_class} "
                        f"envelope +{lo}..+{hi}")
        band = meta["range"]
        r = self.picked_reach()
        if band is None:
            if self.reach:
                errs.append(f"{self.name}: {self.weapon_class} is melee, no reach")
        else:
            rlo, rhi = band
            if r is None or not (rlo <= r <= rhi):
                errs.append(f"{self.name}: reach {r}\" outside {self.weapon_class} "
                            f"envelope {rlo}\"-{rhi}\"")

        # --- the 24" gate. Manufactured-only is enforced here; limit-1-per-crew
        # and the Specialist rank gate are enforced where a crew and a carrier
        # exist (units.crew_rating / validate_carrier), because a catalogue entry
        # has neither. ---
        if is_long_range(r) and not self.manufactured:
            errs.append(
                f"{self.name}: {r}\" exceeds the craftable ceiling - "
                "weapons past 24\" are MANUFACTURED only (loot and raid spoils), "
                "never craftable at any Workshop tier"
            )

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
        dmg = self.picked_damage() + (1 if "brutal" in self.characteristics else 0)
        if dmg > DAMAGE_CAP:
            errs.append(f"{self.name}: damage {dmg} exceeds +{DAMAGE_CAP} cap")
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
    errs = []
    if not can_carry(build.weapon_class, rank):
        need = CLASS_META[build.weapon_class]["min_rank"]
        errs.append(f"{build.name}: {build.weapon_class} requires rank {need}, "
                    f"carrier is {rank}")
    # Gate 3 of 4 on the 24" line: rank. A weapon that covers the board from
    # behind its own deployment zone is a Specialist's tool, not standard kit.
    if is_long_range(build.picked_reach()):
        if RANK_ORDER.index(rank) < RANK_ORDER.index(LONG_RANGE_MIN_RANK):
            errs.append(
                f"{build.name}: {build.picked_reach()}\" exceeds 24\" and requires "
                f"rank {LONG_RANGE_MIN_RANK}, carrier is {rank}")
    return errs


def weapon_cost(build: WeaponBuild) -> int:
    errs = build.validate()
    if errs:
        raise ValueError("; ".join(errs))
    meta = CLASS_META[build.weapon_class]
    total = class_base(meta["slots"])
    total += damage_credits(build.picked_damage())
    total += range_credits(build.picked_reach())
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

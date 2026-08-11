"""An Effect is a declarative mutation of a crew. Sweeps come free from that.

WHY DECLARATIVE
---------------
T5, T6, T10, T13 and T14 were each a bespoke script answering one question, and
they disagree with each other in ways nobody could see because the difference was
buried in Python rather than stated as data. T13's published table has no harness
in any branch at all.

An Effect names WHAT it changes and by HOW MUCH, so two measurements are
comparable by inspection and a sweep is a list comprehension.

THE DIVISOR
-----------
Every published price in this project is win-points divided by MODELS PRESENT.
That is wrong whenever the effect cannot reach every model: `+1 DEX` on the
packet's DEX6 crew is divided by 6 though only 5 carry a gun, and a ranged-only
trait applied to a crew with bat-carriers is divided by all of them. So an Effect
reports `n_applied` — models it actually changed — and the measurement records
BOTH divisors. They differ by ~20% on the project's own standard lists.
"""

from __future__ import annotations

from dataclasses import dataclass, field


STATS = ("str", "dex", "agi", "int", "nrv")


@dataclass
class Effect:
    """One declarative mutation. `kind` decides which fields matter."""
    kind: str
    name: str = ""
    stat: str | None = None
    amount: int = 0
    trait: str | None = None
    weapon: str | None = None
    armour: str | None = None
    skill: str | None = None
    wnd: int | None = None
    orders: int | None = None
    dials: dict = field(default_factory=dict)
    only_first: bool = False
    require_ranged: bool = False
    require_melee: bool = False
    require_gun: bool = False

    def label(self) -> str:
        if self.name:
            return self.name
        if self.kind == "stat":
            return f"{self.stat.upper()}{self.amount:+d}"
        if self.kind == "weapon_trait":
            return f"trait:{self.trait}"
        if self.kind == "armour":
            return f"armour:{self.armour}"
        if self.kind == "skill":
            return f"skill:{self.skill}"
        if self.kind == "wnd":
            return f"WND{self.wnd:+d}"
        if self.kind == "orders":
            return f"orders={self.orders}"
        return self.kind

    def eligible(self, unit, weapons) -> bool:
        spec = weapons.get(unit.weapon, {})
        rng = spec.get("rng", 0)
        if self.require_gun and rng <= 0:
            return False
        if self.require_ranged and rng <= 0:
            return False
        if self.require_melee and rng > 0:
            return False
        return True

    def apply(self, crew, weapons) -> int:
        """Mutate the crew in place. Returns the number of models actually changed.

        A model that cannot benefit is NOT counted — that count is the honest
        divisor, and it is the one this project has never used.
        """
        n = 0
        for i, u in enumerate(crew):
            if self.only_first and i != 0:
                continue
            if not self.eligible(u, weapons):
                continue
            if self.kind == "stat":
                u.stats[self.stat] = u.stats.get(self.stat, 0) + self.amount
            elif self.kind == "weapon_trait":
                variant = register_trait_variant(weapons, u.weapon, self.trait)
                if variant is None:
                    continue
                u.weapon = variant
            elif self.kind == "weapon_damage":
                variant = register_damage_variant(weapons, u.weapon, self.amount)
                if variant is None:
                    continue
                u.weapon = variant
            elif self.kind == "weapon_swap":
                if self.weapon not in weapons:
                    continue
                u.weapon = self.weapon
            elif self.kind == "armour":
                u.armour = self.armour
            elif self.kind == "skill":
                u.skills = tuple(u.skills) + (self.skill,)
            elif self.kind == "wnd":
                u.w = u.w + self.wnd
                u.wnd_max = getattr(u, "wnd_max", u.w)
            elif self.kind == "orders":
                u.orders = self.orders
            else:
                raise ValueError(f"unknown effect kind {self.kind!r}")
            n += 1
        return n


def register_trait_variant(weapons, base: str, trait: str) -> str | None:
    """Add `trait` to a copy of `base`, keeping every other field identical.

    Cost is copied unchanged on purpose: this measures VALUE. Paying for it is a
    separate question, and conflating the two is how a harness ends up asserting
    the price it was meant to test.
    """
    if base not in weapons:
        return None
    key = f"{base}+{trait}"
    if key not in weapons:
        spec = dict(weapons[base])
        if trait in spec.get("traits", ()):
            return base
        spec["traits"] = tuple(spec["traits"]) + (trait,)
        weapons[key] = spec
    return key


def register_damage_variant(weapons, base: str, delta: int) -> str | None:
    if base not in weapons:
        return None
    key = f"{base}+dmg{delta}"
    if key not in weapons:
        spec = dict(weapons[base])
        spec["dmg"] = spec["dmg"] + delta
        weapons[key] = spec
    return key


# --- the anchors, named once so no harness re-spells them -------------------

def damage_anchor(only_first: bool = False) -> Effect:
    """+1 on the Injury roll. The GEAR scale's anchor.

    Applies to melee and ranged alike — `injure()` is reached from both `fight()`
    and `shoot()` — so unlike the payload traits this one is NOT biased by the
    melee/ranged asymmetry.
    """
    return Effect(kind="weapon_damage", amount=1, name="+1 Damage (GEAR anchor)",
                  only_first=only_first)


def stat_rung(stat: str, amount: int = 1, only_first: bool = False,
              require_gun: bool = False) -> Effect:
    """A stat bump. NOT 'a stat point' — the ladder is non-linear (0.46 / 3.24 /
    4.24 win-points for +1 / +2 / +4 on one fighter, packet_battle-n2000.txt:23-25),
    so the rung matters as much as the stat and both belong in the label."""
    return Effect(kind="stat", stat=stat, amount=amount, only_first=only_first,
                  require_gun=require_gun,
                  name=f"{stat.upper()}{amount:+d}" + (" (one fighter)" if only_first else ""))


def payload(trait: str, ranged_only: bool = False) -> Effect:
    return Effect(kind="weapon_trait", trait=trait, name=f"payload:{trait}",
                  require_ranged=ranged_only)

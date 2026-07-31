"""Seed catalogue — sample armoury (legacy ×10) + starter/key structures."""

from __future__ import annotations

from .structures import StructureSpec
from .weapons import WeaponBuild

# Legacy 100-scale sample armoury ×10 — must reconcile exactly via weapon_cost
SAMPLE_ARMOURY: list[tuple[WeaponBuild, int]] = [
    (WeaponBuild("Baseball Bat", "light_melee"), 0),
    (
        WeaponBuild(
            "Kitchen Knife",
            "light_melee",
            ("balanced", "concealable"),
        ),
        40,
    ),
    (
        WeaponBuild("Crowbar", "one_handed_melee", ("breaching",)),
        70,
    ),
    (WeaponBuild("Great Axe", "heavy_melee"), 80),
    (
        WeaponBuild(
            "Sledgehammer",
            "heavy_melee",
            ("heavy_impact", "breaching"),
        ),
        140,
    ),
    (
        WeaponBuild("Fire Axe", "heavy_melee", ("brutal", "bleeding")),
        160,
    ),
    (
        WeaponBuild("Reaping Hook", "heavy_melee", ("cleaving", "defensive")),
        160,
    ),
    (WeaponBuild("Pistol", "sidearm"), 40),
    (
        WeaponBuild(
            "Pipe Shotgun",
            "standard_ranged",
            ("brutal", "spread"),
            ("short_range", "unstable"),
        ),
        120,
    ),
    (
        WeaponBuild("Assault Rifle", "standard_ranged", ("accurate",)),
        130,
    ),
    (
        WeaponBuild("Nailgun", "standard_ranged", ("bleeding",)),
        140,
    ),
    (
        WeaponBuild(
            "Grandpa's Hunting Rifle",
            "standard_ranged",
            ("accurate", "long_range"),
        ),
        190,
    ),
    (
        WeaponBuild(
            "Squad Machine Gun",
            "heavy_ranged",
            ("suppressive", "armour_piercing"),
        ),
        220,
    ),
    (
        WeaponBuild(
            "Makeshift Flamethrower",
            "heavy_ranged",
            ("incendiary", "blast"),
            ("short_range", "limited"),
        ),
        150,
    ),
    (
        WeaponBuild("Molotov", "thrown", ("incendiary", "blast")),
        90,
    ),
    (WeaponBuild("Smoke Grenade", "thrown", ("smoke",)), 50),
]

# Worked examples from the design brief (user's rifle / machete shape)
DESIGN_EXAMPLES: list[WeaponBuild] = [
    WeaponBuild(
        "Auto Rifle +Fire",
        "standard_ranged",
        ("incendiary",),  # +Fire; +DMG would need Brutal+Short Range
    ),
    WeaponBuild(
        "Machete +Shock",
        "one_handed_melee",
        ("shocking",),
    ),
    WeaponBuild(
        "Brutal Machete +Shock",
        "one_handed_melee",
        ("brutal", "shocking"),
    ),
]

STARTER_STRUCTURES: list[StructureSpec] = [
    StructureSpec("HQ", "building", "operate", tier=1, starter=True),
    StructureSpec("Generator", "plant", "sustain", tier=1, starter=True),
    StructureSpec("Processor", "plant", "gatherer", tier=1, starter=True),
    StructureSpec("Salvage Yard", "yard", "gatherer", tier=1, starter=True),
    # Water structures cut (D19)
]

KEY_STRUCTURES: list[StructureSpec] = [
    StructureSpec("Bunkhouse", "large", "sustain", tier=1),
    StructureSpec("Storehouse", "building", "sustain", tier=1),
    StructureSpec("Equipment Shed", "station", "sustain", tier=1),
    StructureSpec("Armory", "building", "sustain", tier=2),
    StructureSpec("Workbench", "station", "convert", tier=1),
    StructureSpec("Workshop", "building", "convert", tier=2),
    StructureSpec("Trader's Kiosk", "station", "convert", tier=1),
    StructureSpec("Trade House", "building", "convert", tier=2),
    StructureSpec("Fabricator", "building", "convert", tier=1),
    StructureSpec("Med-bay", "building", "recover", tier=1),
    StructureSpec("Holding Cells", "building", "recover", tier=1),
    StructureSpec("Scout Post", "plant", "operate", tier=1),
    StructureSpec("Comms Mast", "plant", "operate", tier=1),
    StructureSpec("Perimeter Wall (6\" seg)", "line", "defend", tier=1),
    StructureSpec("Gatehouse", "building", "defend", tier=1),
    StructureSpec("Watchtower", "plant", "defend", tier=1),
    StructureSpec("Turret Mount", "plant", "defend", tier=2),
    StructureSpec("EW Mast", "plant", "defend", tier=2),
    StructureSpec("Drone Bay", "large", "operate", tier=2),
    StructureSpec("Server Core", "building", "operate", tier=2),
    StructureSpec("Vault", "plant", "operate", tier=1),
]

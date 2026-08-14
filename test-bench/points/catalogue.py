"""Seed catalogue — sample armoury (legacy ×10) + starter/key structures."""

from __future__ import annotations

from .structures import StructureSpec
from .weapons import WeaponBuild

# Legacy 100-scale sample armoury ×10 — must reconcile exactly via weapon_cost
SAMPLE_ARMOURY: list[tuple[WeaponBuild, int]] = [
    # REGENERATED 2026-08-14 from class envelopes. Every entry now names its
    # damage and reach PICK; before this the class dictated both, so a Pistol and
    # a Magnum were the same weapon and a rifle, a great axe and a machine gun
    # all sat at +3. Second number is the legacy x10 price, kept for the drift
    # report. "Kitchen Knife" lost Concealable (cut) and is rebuilt without it.
    (WeaponBuild("Baseball Bat", "light_melee", damage=1), 0),
    (WeaponBuild("Kitchen Knife", "light_melee", ("balanced",), damage=1), 40),
    (WeaponBuild("Machete", "one_handed_melee", damage=2), 40),
    (WeaponBuild("Crowbar", "one_handed_melee", ("breaching",), damage=2), 70),
    (WeaponBuild("Magnum", "sidearm", ("brutal",), ("short_range",),
                 damage=3, reach=6), 90),
    (WeaponBuild("Great Axe", "heavy_melee", damage=3), 80),
    (WeaponBuild("Sledgehammer", "heavy_melee", ("heavy_impact", "breaching"),
                 damage=4), 140),
    (WeaponBuild("Fire Axe", "heavy_melee", ("brutal", "bleeding"), damage=3), 160),
    (WeaponBuild("Reaping Hook", "heavy_melee", ("cleaving", "defensive"),
                 damage=2), 160),
    (WeaponBuild("Pistol", "sidearm", damage=2, reach=8), 40),
    (WeaponBuild("Snub Revolver", "sidearm", damage=2, reach=6), 40),
    (WeaponBuild("Pipe Shotgun", "standard_ranged", ("brutal", "spread"),
                 ("short_range", "unstable"), damage=3, reach=12), 120),
    (WeaponBuild("Assault Rifle", "standard_ranged", ("accurate",),
                 damage=3, reach=18), 130),
    (WeaponBuild("Nailgun", "standard_ranged", ("bleeding",), damage=2, reach=12), 140),
    (WeaponBuild("Grandpa's Hunting Rifle", "standard_ranged", ("accurate",),
                 damage=3, reach=24), 190),
    (WeaponBuild("Squad Machine Gun", "heavy_ranged",
                 ("suppressive", "armour_piercing"), damage=3, reach=24), 220),
    (WeaponBuild("Makeshift Flamethrower", "standard_ranged", ("incendiary",),
                 ("short_range",), damage=2, reach=12), 150),
    (WeaponBuild("Molotov", "thrown", ("incendiary",), ("single_use",),
                 damage=1, reach=8), 90),
    (WeaponBuild("Smoke Grenade", "thrown", ("smoke",), ("single_use",),
                 damage=1, reach=8), 50),
    # THE GATED TOP END, as a worked example. 36" reaches the whole board from
    # 12" behind its own deployment zone. Manufactured only (never craftable),
    # limit 1 per crew, Specialist+, and the price crosses the 24" threshold at
    # an accelerating rate. All four gates are enforced in code, not just noted.
    (WeaponBuild("Ranger's Long Rifle", "heavy_ranged", ("accurate",),
                 damage=3, reach=36, manufactured=True), 0),
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

# -*- coding: utf-8 -*-
"""Fail loudly when the written rules and the costing engine disagree.

WHY THIS EXISTS. On 2026-08-27 an audit found the rules text and the shipping
catalogue were a full generation apart: the vault printed an Assault Rifle at 130
Credits while the engine priced it at 35, an Autoturret at 120 against 10, an HQ
at 130 Materials against 70. Nothing was wrong with either number — they simply
stopped being the same number, silently, because every price was hand-copied into
six notes and the engine moved underneath them.

Hand-copying them again guarantees the same drift. This script is the guard: it
does NOT rewrite the notes (each table keeps exactly one home — the same
architecture `build_catalogue.py` assumes), it just reports when a note has fallen
behind the engine, or still carries a value that was explicitly retired.

    py -3.13 scripts/check_rules_consistency.py          # report
    py -3.13 scripts/check_rules_consistency.py --repo   # check the repo mirror

Exit code 1 on any failure, so it can gate a commit.
"""
import argparse
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault",
                     "Settlements", "Rules System")
MIRROR = os.path.normpath(os.path.join(HERE, "..", "rules-vault", "Rules System"))

# --------------------------------------------------------------------------
# Values the engine owns. Pulled live so this file never becomes a second
# hand-maintained copy of the thing it is policing.
# --------------------------------------------------------------------------
def engine_values():
    sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "test-bench")))
    from points import ticks as t          # noqa: E402
    return {
        "rifle": t.CLASS_CREDITS["standard_ranged"],
        "heavy_ranged": t.CLASS_CREDITS["heavy_ranged"],
        "sidearm": t.CLASS_CREDITS["sidearm"],
        "heavy_melee": t.CLASS_CREDITS["heavy_melee"],
        "armour_light": t.ARMOUR_CREDITS["light"],
        "armour_heavy": t.ARMOUR_CREDITS["heavy"],
        "breach_kit": t.HACK_GEAR_CREDITS["breach_kit"],
        "exploit_suite": t.HACK_GEAR_CREDITS["exploit_suite"],
        "med_kit": t.EQUIPMENT_CREDITS["med_kit"],
        "autoturret": t.DEPLOYABLE_CREDITS["autoturret"],
        "sniper_turret": t.DEPLOYABLE_CREDITS["sniper_turret"],
        "skill_t1": t.SKILL_TIER_CREDITS[1],
        "skill_t2": t.SKILL_TIER_CREDITS[2],
        "skill_t3": t.SKILL_TIER_CREDITS[3],
        "wnd": t.WND_CREDITS,
        "damage_cap": t.DAMAGE_CAP,
    }

# --------------------------------------------------------------------------
# RETIRED VALUES. Any of these appearing in a rules note is drift, full stop.
# (note, pattern, what it should be now)
# --------------------------------------------------------------------------
FORBIDDEN = [
    # --- the Crew Rating fight, settled at 850 / 425 ---
    ("Full Rules System v1.md", r"standard 1000, raid 750", "Crew Rating is 850/640/1275/425"),
    ("Full Rules System v1.md", r"Standard cap: 1000 Credits", "Crew Rating is 850"),
    ("List Building.md",        r"\|\s*\*\*1000\*\*\s*\|", "Crew Rating is 850"),
    ("Downtime.md",             r"standard 1000", "Crew Rating is 850"),
    # --- retired rank ladders ---
    ("Unit Design.md",          r"\|\s*245\s*\|", "Leader is 185"),
    ("Unit Design.md",          r"65 / 75 / 125 / 170", "one ladder: 70/100/145/185"),
    # --- retired weapon/armour prices ---
    ("Weapons.md",              r"multiply by 10", "the x10 scale is retired"),
    # Anchored to the armour row, not a bare number — "**100**" is also a
    # legitimate Fighter body cost two tables up.
    ("List Building.md",        r"\|\s*Light\s*\|\s*−1\s*\|\s*\*\*60\*\*", "light armour is 10"),
    ("List Building.md",        r"\|\s*Heavy\s*\|\s*−2\s*\|\s*\*\*100\*\*", "heavy armour is 20"),
    # --- retired damage/range ceilings (superseded by the 2026-08-14 bands) ---
    ("Full Rules System v1.md", r"Damage stops at \*\*\+4\*\*", "the ceiling is +5"),
    ("Deployables.md",          r"\+4 Damage ceiling", "the ceiling is +5"),
    # --- rulings the master made that satellites used to contradict ---
    ("Initiative & Activation.md", r"move up to \*\*full MOV", "Dodge moves half MOV"),
    ("Territory.md",            r"One dose of a basic \*\*Chem\*\*", "loot 7 is +15 Credits"),
    ("Progression.md",          r"\+1 \*\*Secondary\*\* stat", "levels 1/4/8 float to any stat"),
    ("Damage.md",               r"Armor carries drawbacks", "armour carries none"),
    ("Deployables.md",          r"\|\s*\*\*Seeker\*\*\s*\|\s*\*\*80\*\*", "the Seeker chassis is parked"),
    # --- retired structure Materials ---
    ("Structures.md",           r"\*\*130\*\*\|Campaign actions", "the HQ is 70 Materials"),
    ("Full Rules System v1.md", r"250 Materials \+ 150 Credits", "founding is 125 + 75"),
]

# --------------------------------------------------------------------------
# PRESENCE CHECKS. The live engine value must actually appear in the note that
# owns that table. Keyed to the engine so it updates itself.
# --------------------------------------------------------------------------
def presence_checks(v):
    return [
        ("Weapons.md",              f"**{v['armour_light']}**",   "light armour price"),
        ("Weapons.md",              f"**{v['armour_heavy']}**",   "heavy armour price"),
        ("Weapons.md",              f"**{v['breach_kit']}**",     "breach kit price"),
        ("List Building.md",        f"**{v['med_kit']}**",        "med-kit price"),
        ("Deployables.md",          f"**{v['autoturret']}**",     "autoturret price"),
        ("Deployables.md",          f"**{v['sniper_turret']}**",  "sniper turret price"),
        ("Progression.md",          f"**{v['skill_t1']}**",       "T1 skill price"),
        ("Progression.md",          f"**{v['skill_t3']}**",       "T3 skill price"),
        ("Progression.md",          f"**{v['wnd']}**",            "+1 WND price"),
        ("Full Rules System v1.md", "850",                        "Crew Rating"),
        ("Full Rules System v1.md", "425",                        "Campaign Start cap"),
        ("Full Rules System v1.md", f"+{v['damage_cap']}",        "damage ceiling"),
    ]

# --------------------------------------------------------------------------
def read(root, name):
    path = os.path.join(root, name)
    if not os.path.exists(path):
        return None
    with io.open(path, encoding="utf-8") as f:
        return f.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", action="store_true",
                    help="check the repo mirror instead of the live vault")
    args = ap.parse_args()
    root = MIRROR if args.repo else VAULT
    label = "repo mirror" if args.repo else "Obsidian vault"

    if not os.path.isdir(root):
        print(f"FATAL: {label} not found at {root}")
        return 2

    v = engine_values()
    print(f"Checking {label}\n  {root}")
    print(f"Engine: rifle {v['rifle']} · armour {v['armour_light']}/{v['armour_heavy']} "
          f"· skills {v['skill_t1']}/{v['skill_t2']}/{v['skill_t3']} "
          f"· WND {v['wnd']} · damage cap +{v['damage_cap']}\n")

    fails = []
    cache = {}

    print("RETIRED VALUES (must not appear)")
    for name, pattern, should_be in FORBIDDEN:
        if name not in cache:
            cache[name] = read(root, name)
        text = cache[name]
        if text is None:
            fails.append(f"{name}: FILE MISSING")
            print(f"  ??  {name}  (missing)")
            continue
        if re.search(pattern, text):
            fails.append(f"{name}: still carries a retired value — {should_be}")
            print(f"  !!  {name:32s} {should_be}")
    if not fails:
        print("  clean")

    print("\nLIVE ENGINE VALUES (must appear)")
    missing = []
    for name, needle, what in presence_checks(v):
        if name not in cache:
            cache[name] = read(root, name)
        text = cache[name]
        if text is None or needle not in text:
            missing.append(f"{name}: {what} ({needle}) not found")
            print(f"  !!  {name:32s} {what} — expected {needle}")
    if not missing:
        print("  clean")
    fails += missing

    print()
    if fails:
        print(f"FAIL — {len(fails)} inconsistencies")
        print("The rules and the engine disagree. Either propagate the engine into")
        print("the note, or change the engine — but do not leave them apart.")
        return 1
    print("PASS — the written rules and the costing engine agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

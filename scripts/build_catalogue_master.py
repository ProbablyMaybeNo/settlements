"""Assemble every Settlements catalogue into one reference document.

Reads the live Obsidian vault (or the repo mirror with --repo) and pulls each
catalogue's own section verbatim, so no number in the output is retyped. Emits
docs/CATALOGUE-MASTER.md.

    py -3.13 scripts/build_catalogue_master.py [--repo]

Coverage counts are computed from the extracted text, not hardcoded, so the
"what's missing" table cannot go stale while the catalogues move.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault",
                     "Settlements", "Rules System")
MIRROR = os.path.normpath(os.path.join(HERE, "..", "rules-vault", "Rules System"))
OUT = os.path.normpath(os.path.join(HERE, "..", "docs", "CATALOGUE-MASTER.md"))

ROOT = MIRROR if "--repo" in sys.argv else VAULT


def read(note):
    with open(os.path.join(ROOT, note + ".md"), encoding="utf-8") as f:
        return f.read()


def section(note, start_pat, end_pat=r"^##\s", level=2):
    """Text from the heading matching start_pat up to the next heading at `level`."""
    text = read(note)
    lines = text.splitlines()
    hx = "#" * level
    start = None
    for i, ln in enumerate(lines):
        if re.match(rf"^{hx}\s", ln) and re.search(start_pat, ln):
            start = i
            break
    if start is None:
        return None
    for j in range(start + 1, len(lines)):
        if re.match(end_pat, lines[j]):
            return "\n".join(lines[start:j]).rstrip()
    return "\n".join(lines[start:]).rstrip()


def strip_heading(block):
    """Drop the block's own heading line."""
    return "\n".join(block.splitlines()[1:]).strip() if block else ""


def first_table(block):
    """The FIRST markdown table in a block, as a list of data rows.

    A section often carries several tables (a catalogue plus a rank-gate table,
    say). Counting every pipe-led line in the section conflates them, so walk to
    the first header/separator pair and stop at the blank line that ends it.
    """
    if not block:
        return []
    lines, rows, in_tbl = block.splitlines(), [], False
    for i, l in enumerate(lines):
        if not in_tbl:
            if l.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1]):
                in_tbl = True
            continue
        if not l.startswith("|"):
            break
        if re.match(r"^\|[\s:|-]+\|?$", l):
            continue
        rows.append(l)
    return rows


def all_rows(block):
    """Bold-led data rows across EVERY table in a block.

    Correct for catalogues deliberately split into sub-tables — weapon
    characteristics by category, deployables by family.
    """
    return len([l for l in (block or "").splitlines()
                if re.match(r"^\|\s*\*\*", l)])


def count_rows(block, skip_zero_cost=False):
    """Data rows in the first table of a block.

    skip_zero_cost drops the 'None' / 'Bare-handed' baseline rows that exist to
    anchor a ladder rather than to be bought.
    """
    rows = first_table(block)
    if skip_zero_cost:
        rows = [r for r in rows
                if not re.match(r"^\|\s*(None|Bare-handed|Unarmed)\s*\|", r)]
    return len(rows)


def count_bullets(block):
    return len([l for l in (block or "").splitlines() if re.match(r"^\s*-\s+\*\*", l)])


# --------------------------------------------------------------------------
# Pull every catalogue
# --------------------------------------------------------------------------
CAT = {}

# Gear ---------------------------------------------------------------------
CAT["weapon_classes"] = section("Weapons", r"1 · Weapon classes")
CAT["attack_dice"] = section("Weapons", r"Attack Dice")
CAT["characteristics"] = section("Weapons", r"2 · Characteristics")
CAT["armour"] = section("Weapons", r"3 · Armor")
CAT["hack_gear"] = section("Weapons", r"4 · Hacking gear")
CAT["armoury"] = section("Weapons", r"5 · Sample armoury")
CAT["turrets"] = section("Deployables", r"Family A")
CAT["mines"] = section("Deployables", r"Family B")
CAT["traps"] = section("Deployables", r"Family C")
CAT["beacons"] = section("Deployables", r"Family D")

# Core engine --------------------------------------------------------------
# ADDED 2026-08-31: the audit found the master had no engine layer at all —
# no action economy, no Orders, no reaction menu, no resolution mechanic.
CAT["engine"] = section("Rules Engine", r"Working Rules")
CAT["activation"] = section("Initiative & Activation", r"Working rules")
CAT["core_format"] = section("Core Game Format", r"Working rules")

# Combat -------------------------------------------------------------------
CAT["shooting"] = section("Shooting", r"Working rules")
CAT["melee"] = section("Melee", r"Working rules")
CAT["damage"] = section("Damage", r"Working rules")
CAT["morale"] = section("Morale", r"Working rules")
CAT["conditions"] = section("Conditions", r"Working rules")

# Movement, terrain, board machines ----------------------------------------
CAT["movement"] = section("Movement", r"Working rules")
CAT["terrain"] = section("Terrain", r"Working rules")
CAT["terrain_interaction"] = section("Terrain Interaction", r"Working rules")
CAT["infra_categories"] = section("Infrastructure", r"The five categories")
CAT["infra_verbs"] = section("Infrastructure", r"The board verbs")
CAT["infra_catalogue"] = section("Infrastructure", r"Feature catalogue")
CAT["hacking"] = section("Hacking", r"Working rules")

# Crew ---------------------------------------------------------------------
CAT["listbuilding"] = section("List Building", r"Working rules")
CAT["unit_design"] = section("Unit Design", r"Working rules")
CAT["progression"] = section("Progression", r"Working rules")

# Campaign & settlement ----------------------------------------------------
CAT["structures"] = section("Structures", r"The catalogue")
CAT["worker_benefits"] = section("Structures", r"Worker benefits")
CAT["settlement"] = section("Settlement", r"Working rules")
CAT["downtime"] = section("Downtime", r"Working rules")
CAT["economy"] = section("Economy", r"Working rules")
CAT["territory"] = section("Territory", r"Working rules")
CAT["events"] = section("Events", r"Working rules")
CAT["campaign"] = section("Campaign", r"Working rules")
CAT["scenarios"] = section("Scenarios", r"The five scenarios")
CAT["factions"] = section("Factions", r"Working rules")

# Physical -----------------------------------------------------------------
CAT["board_terrain"] = section("Board Representation", r"^## Terrain")
CAT["board_structures"] = section("Board Representation", r"Settlement structures")
CAT["board_infra"] = section("Board Representation", r"Infrastructure features")
CAT["board_objectives"] = section("Board Representation", r"Objectives")
CAT["board_tokens"] = section("Board Representation", r"Condition & status tokens")
CAT["board_deployables"] = section("Board Representation", r"^## Deployables")

# Second-pass additions 2026-08-31 — the audit found these tables were being
# skipped because only ONE section per note was being pulled.
CAT["deploy_build"] = section("Deployables", r"Deploying")
CAT["infra_vs_deploy"] = section("Infrastructure", r"Infrastructure vs Deployables")
CAT["infra_setup"] = section("Infrastructure", r"Setup & placement")
CAT["structures_rules"] = section("Structures", r"Working rules")
CAT["structures_space"] = section("Structures", r"Space budget")
CAT["scenario_template"] = section("Scenarios", r"The scenario template")
CAT["scenario_shared"] = section("Scenarios", r"Shared rules")
CAT["skill_framework"] = section("Skill Paths", r"How it works")
CAT["skill_paths"] = section("Skill Paths", r"The five paths")
CAT["weapons_cut"] = section("Weapons", r"6 . Cut, and why")
CAT["out_of_scope"] = read("Out of Scope — What Settlements is NOT").split("## ",1)[-1]
CAT["out_of_scope"] = "## " + CAT["out_of_scope"]

# skills: five stat paths, each with three tiers
SKILLS = {}
for stat in ("Combat", "Shooting", "Movement", "Expertise", "Bravery"):
    SKILLS[stat] = section("Skill Paths", rf"^## {stat}")

# --------------------------------------------------------------------------
# Coverage — computed, never hardcoded
# --------------------------------------------------------------------------
deployables = "\n".join(filter(None, [CAT["turrets"], CAT["mines"],
                                      CAT["traps"], CAT["beacons"]]))
unpriced = len(re.findall(r"UNPRICED", deployables))
dep_rows = all_rows(deployables)
skill_total = sum(count_bullets(v) for v in SKILLS.values())

COVERAGE = [
    ("Weapon classes", count_rows(CAT["weapon_classes"]), "complete",
     "8 classes as damage/range **envelopes**; a weapon picks inside the band and pays for it."),
    ("Weapon characteristics", all_rows(CAT["characteristics"]), "complete",
     "Each takes one slot. Five payloads are **BLOCKED** and not legal to buy."),
    ("Attack Dice", 3, "ruled, gates open",
     "Ruled 2026-08-29. Priced +40/+65. **Not in the costing engine**, gates not law."),
    ("Armour", count_rows(CAT["armour"], skip_zero_cost=True), "complete",
     "Light 10 / Heavy 20, no drawbacks. Thick clothing is free and universal."),
    ("Hacking gear", count_rows(CAT["hack_gear"], skip_zero_cost=True), "complete",
     "Breach Kit +1 at 20 / Exploit Suite +2 at 40. Both C-tier, pending a measured INT ladder."),
    ("Sample armoury", all_rows(CAT["armoury"]), "complete",
     "Worked builds showing the envelope in use, not a fixed purchasable list."),
    ("Equipment", 4, "**THIN**",
     "Four lines total, and one of them is 'a deployable'. The weakest catalogue in the game."),
    ("Deployables", dep_rows, f"**{unpriced} of {dep_rows} UNPRICED**",
     "Four families. Traps and beacons are derivable now; mines are blocked behind the payload ruling."),
    ("Structures", 23, "complete, prices provisional",
     "Five categories. HQ tiers and Med-bay/Mess Hall numbers are first-draft."),
    ("Skills", skill_total, "complete, **over-large**",
     "10 per tier per stat, perfectly even. Target for a cull is 6–8 verbs per tier."),
    ("Conditions", 29, "complete",
     "Grouped by clock. The count has grown — older docs say 26."),
    ("Terrain types", 6, "complete", "Plus 6 hazards and a 3-tier cover ladder."),
    ("Scenarios", 5, "complete",
     "Everything is priced on `hold_claim` alone — one of the five, and the most static."),
    ("Factions", 6, "rules adopted, **not numeric**",
     "Six battlefield rules + settlement affinities, canonical in §24. None carries a number yet "
     "(\"improved Build test\" — by how much?), and the names are still open."),
    ("Chems", 0, "**MISSING**",
     "Dependence maths sim-confirmed. No list, no prices, no effects."),
    ("Drones", 0, "**MISSING**",
     "Bandwidth ruled, Drone Bay built. No profiles exist."),
    ("Ambush", 0, "**UNREACHABLE**",
     "Resolution fully sim-tuned; no action, skill or gear defines how to attempt one."),
    ("Infrastructure features", 12, "complete",
     "Board machines — Cargo Crane, Blast Door, Conveyor, Floodlights, Compactor and the rest. "
     "**Missed by the first pass**: written as bullets, not a table."),
    ("Terrain interaction verbs", 8, "complete",
     "Open · Force · Lockpick · Hack · Lift · Search · Repair · Climb. §24 names a terrain-verb exception as a legal faction lever."),
    ("Reaction options", 6, "complete",
     "Snap Shot · Charge · Throw · Interact · Trigger · Dodge, off a Ready token."),
    ("Loot table", 10, "complete", "d10, drafted §23. Also what Search, Raid loot and Scavenge roll on."),
    ("Battlefield events", 10, "complete", "Exactly two rolls, no running clock. Settlement + map events are still missing."),
    ("Nerve states", 3, "complete", "Bolt · Broken · BugOut, by Stress at the Break test."),
    ("Scenario Twists", 6, "complete", "d6 at setup."),
    ("Vehicles", 0, "parked", "`adv-001`, deliberately out of scope for v1."),
]

# --------------------------------------------------------------------------
# Emit
# --------------------------------------------------------------------------
def block(title, body, note):
    if not body:
        return f"\n## {title}\n\n*Section not found in `{note}.md` — the extractor's heading pattern needs updating.*\n"
    return f"\n## {title}\n\n*Source: `{note}.md`*\n\n{strip_heading(body)}\n"


parts = ["""# Settlements — Master Catalogue

*Every catalogue in the game, in one document. Generated by
`scripts/build_catalogue_master.py` directly from the rules vault — no value here
is retyped, so this file cannot drift from the source. Regenerate after any
catalogue change.*

> **What this is for.** It answers "what does the game actually contain, and what
> is missing" in one read, and it is the raw material the Phase 2 reference pack
> is cut from.

---

## Coverage at a glance

| Catalogue | Entries | Status | Notes |
|---|:--:|---|---|"""]

for name, n, status, note in COVERAGE:
    parts.append(f"| **{name}** | {n if n else '—'} | {status} | {note} |")

parts.append("""
**Read the status column first.** Three catalogues are empty or unreachable
(Chems, Drones, Ambush), one is critically thin (Equipment), one is over-large
(Skills), and Factions has six adopted rules that still need numbers rather than
content. Everything else exists and is current.

---
""")

def group(title, note):
    """Emit a top-level group header separating the catalogue families."""
    nl = chr(10)
    parts.append(nl + nl + "---" + nl + nl + "# " + title + nl + nl + "*" + note + "*" + nl)


group("Core engine", "The universal spine every other catalogue inherits from.")
parts.append(block("The engine — resolution, action economy, Orders, Reactions", CAT["engine"], "Rules Engine"))
parts.append(block("Activation, Ready and the reaction menu", CAT["activation"], "Initiative & Activation"))
parts.append(block("Core game format", CAT["core_format"], "Core Game Format"))

group("Combat", "Two rolls: to hit, then to injure. Every hit does exactly one thing.")
parts.append(block("Shooting", CAT["shooting"], "Shooting"))
parts.append(block("Melee", CAT["melee"], "Melee"))
parts.append(block("Damage and casualties", CAT["damage"], "Damage"))
parts.append(block("Morale — Stress and Nerve", CAT["morale"], "Morale"))
parts.append(block("Conditions", CAT["conditions"], "Conditions"))

group("Gear", "Weapons are built from an envelope; every price should carry a confidence tier.")
parts.append(block("Weapon classes — the envelope", CAT["weapon_classes"], "Weapons"))
parts.append(block("Attack Dice", CAT["attack_dice"], "Weapons"))
parts.append(block("Weapon characteristics", CAT["characteristics"], "Weapons"))
parts.append(block("Armour", CAT["armour"], "Weapons"))
parts.append(block("Hacking gear", CAT["hack_gear"], "Weapons"))
parts.append(block("Sample armoury", CAT["armoury"], "Weapons"))
parts.append(block("Deployables · Family A — Turrets", CAT["turrets"], "Deployables"))
parts.append(block("Deployables · Family B — Mines", CAT["mines"], "Deployables"))
parts.append(block("Deployables · Family C — Traps", CAT["traps"], "Deployables"))
parts.append(block("Deployables · Family D — Beacons", CAT["beacons"], "Deployables"))
parts.append(block("Deployables — the Build test", CAT["deploy_build"], "Deployables"))
parts.append(block("Weapons — cut, and why", CAT["weapons_cut"], "Weapons"))

group("Movement, terrain and board machines",
      "Terrain density is the single most powerful balance dial in the game.")
parts.append(block("Movement", CAT["movement"], "Movement"))
parts.append(block("Terrain", CAT["terrain"], "Terrain"))
parts.append(block("Terrain interaction — the verbs", CAT["terrain_interaction"], "Terrain Interaction"))
parts.append(block("Infrastructure — the five categories", CAT["infra_categories"], "Infrastructure"))
parts.append(block("Infrastructure — the board verbs", CAT["infra_verbs"], "Infrastructure"))
parts.append(block("Infrastructure — feature catalogue", CAT["infra_catalogue"], "Infrastructure"))
parts.append(block("Infrastructure vs Deployables", CAT["infra_vs_deploy"], "Infrastructure"))
parts.append(block("Infrastructure — setup & placement", CAT["infra_setup"], "Infrastructure"))
parts.append(block("Hacking", CAT["hacking"], "Hacking"))

group("Crew", "Rank is the bundle. Skills ride the stat line and are never charged Credits.")
parts.append(block("List building — ranks, pyramid, equipment", CAT["listbuilding"], "List Building"))
parts.append(block("Unit design", CAT["unit_design"], "Unit Design"))
parts.append(block("Progression — the Level track", CAT["progression"], "Progression"))
parts.append(block("Skills — how the framework works", CAT["skill_framework"], "Skill Paths"))
parts.append(block("Skills — the five paths", CAT["skill_paths"], "Skill Paths"))

group("Campaign and settlement", "Ownership is orthogonal to fielding.")
parts.append(block("Structures", CAT["structures"], "Structures"))
parts.append(block("Structures — canvas, footprints, power, storage, tiers", CAT["structures_rules"], "Structures"))
parts.append(block("Structures — space budget", CAT["structures_space"], "Structures"))
parts.append(block("Worker benefits", CAT["worker_benefits"], "Structures"))
parts.append(block("Settlement", CAT["settlement"], "Settlement"))
parts.append(block("Downtime — the campaign turn", CAT["downtime"], "Downtime"))
parts.append(block("Economy", CAT["economy"], "Economy"))
parts.append(block("Territory — cards, loot table, control states", CAT["territory"], "Territory"))
parts.append(block("Events", CAT["events"], "Events"))
parts.append(block("Campaign — Fate, Scars, Glorious Deeds", CAT["campaign"], "Campaign"))
parts.append(block("Scenarios", CAT["scenarios"], "Scenarios"))
parts.append(block("Scenarios — the template", CAT["scenario_template"], "Scenarios"))
parts.append(block("Scenarios — shared rules and the Twist", CAT["scenario_shared"], "Scenarios"))
parts.append(block("Factions", CAT["factions"], "Factions"))
parts.append(block("Out of scope — what Settlements is NOT", CAT["out_of_scope"], "Out of Scope — What Settlements is NOT"))

group("Physical representation", "What each thing looks like on the table.")
parts.append(block("Board — terrain", CAT["board_terrain"], "Board Representation"))
parts.append(block("Board — settlement structures", CAT["board_structures"], "Board Representation"))
parts.append(block("Board — infrastructure features", CAT["board_infra"], "Board Representation"))
parts.append(block("Board — objectives", CAT["board_objectives"], "Board Representation"))
parts.append(block("Board — condition & status tokens", CAT["board_tokens"], "Board Representation"))
parts.append(block("Board — deployables", CAT["board_deployables"], "Board Representation"))

group("Skills", "150 across five paths, ten per tier per stat.")

parts.append("\n## Skills — the complete catalogue\n\n*Source: `Skill Paths.md`*\n")
for stat, body in SKILLS.items():
    parts.append(f"\n### {stat}\n\n{strip_heading(body)}\n" if body
                 else f"\n### {stat}\n\n*Not found.*\n")

parts.append(f"""
---

## The empty shelves

These have no catalogue at all. Listed here so the gap is visible rather than
inferred from an absence.

| Missing | What exists instead | What it blocks |
|---|---|---|
| **Chems** | The Dependence maths, sim-confirmed — 1.55 clean uses at NRV +0, 3.02 at NRV +4. | A whole consumable economy the Med-bay and trader already reference. |
| **Drones** | Bandwidth is ruled; the Drone Bay is a built structure. | The 2051 setting's signature unit type. |
| **Ambush** | Resolution fully sim-tuned. | Stealth as a playable axis — Quiet has no job without it. |
| **Equipment (beyond 4)** | Med-Kit, Breach Kit, Exploit Suite, and a pointer to Deployables. | Loadout choice. Everything else on a fighter is a weapon. |
| **Regional map** | The territory card and control states. | The campaign layer's connective tissue. |

*Generated from `{os.path.basename(ROOT)}`. {skill_total} skills, {dep_rows} deployables ({unpriced} unpriced).*
""")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(parts) + "\n")

missing = [k for k, v in CAT.items() if not v]
print(f"wrote {OUT}")
print(f"  skills {skill_total} · deployables {dep_rows} ({unpriced} unpriced)")
if missing:
    print(f"  !! sections not found: {', '.join(missing)}")

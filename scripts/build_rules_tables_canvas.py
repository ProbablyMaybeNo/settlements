"""Build `_Rules Tables.canvas` — every rules table in the system on one canvas.

Two passes:
  1. Inject a stable block ID (`^tbl-...`) after every table we want to show, in the
     REAL Obsidian vault. Idempotent — re-running never duplicates an ID.
  2. Emit a canvas whose nodes are block/heading embeds of those tables, so the canvas
     always renders the live text. Editing a rule updates the canvas; only *new* tables
     need this script re-run.

Usage:  py -3.13 scripts/build_rules_tables_canvas.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

VAULT = Path(r"C:\Users\Admin\Documents\Obsidian Vault")
RULES = VAULT / "Settlements" / "Rules System"
CANVAS = RULES / "_Rules Tables.canvas"
VAULT_PREFIX = "Settlements/Rules System"

# ---------------------------------------------------------------- layout config

CARD_MIN_W, CARD_MAX_W = 420, 1180
ROW_H = 30
TITLE_H = 46
GAP_Y = 26
GROUP_PAD = 60
COL_GAP = 90

# Ordered left-to-right. Each band is a labelled group column on the canvas.
# ("File.md", None)          -> every table in that file, in document order
# ("File.md", ["Heading"])   -> only tables whose nearest heading is in the list
SPEC: list[dict] = [
    {
        "label": "① CORE ENGINE — the one test everything reuses",
        "color": "5",
        "files": [("Rules Ledger/core-000 Core Test.md", None)],
        "sections": [],
    },
    {
        "label": "② UNIT DESIGN — what a fighter is",
        "color": "5",
        "files": [("Unit Design.md", None)],
        "sections": [],
    },
    {
        "label": "③ ACTIONS, MOVEMENT & REACTIONS",
        "color": "4",
        "files": [("Movement.md", None), ("Initiative & Activation.md", None)],
        "sections": [],
    },
    {
        "label": "④ MORALE & CONDITIONS — the component pool for status effects",
        "color": "4",
        "files": [("Morale.md", None)],
        "sections": [
            ("Conditions.md", "Working rules / decisions#Core combat conditions"),
            ("Conditions.md", "Working rules / decisions#Control conditions (from skills, weapons and terrain)"),
            ("Conditions.md", "Working rules / decisions#Persistent conditions (resolve in the End Phase)"),
            ("Conditions.md", "Working rules / decisions#Nerve states (from [[Morale]])"),
            ("Conditions.md", "Working rules / decisions#Morale modifiers (from skills)"),
            ("Conditions.md", "Working rules / decisions#Marker & device states (not conditions on units)"),
        ],
    },
    {
        "label": "⑤ TERRAIN & INTERACTION — the battlefield",
        "color": "4",
        "files": [("Terrain.md", None), ("Terrain Interaction.md", None)],
        "sections": [],
    },
    {
        "label": "⑥ HACKING & INFRASTRUCTURE — the digital / machine layer",
        "color": "6",
        "files": [("Hacking.md", None), ("Infrastructure.md", None)],
        "sections": [
            ("Infrastructure.md", "The board verbs"),
            ("Infrastructure.md", "Damage — two keywords"),
            ("Infrastructure.md", "Feature catalogue"),
        ],
    },
    {
        "label": "⑦ WEAPONS — build a weapon from these parts  ★ POINTS",
        "color": "1",
        "files": [("Weapons.md", None)],
        "sections": [],
    },
    {
        "label": "⑧ DEPLOYABLES — turrets · mines · traps · beacons  ★ POINTS",
        "color": "1",
        "files": [("Deployables.md", None)],
        "sections": [],
    },
    {
        "label": "⑨ LIST BUILDING — ranks, armour, equipment  ★ POINTS",
        "color": "1",
        "files": [("List Building.md", None)],
        "sections": [],
    },
    {
        "label": "⑩ SKILL PATHS — 150 skills, the biggest component pool",
        "color": "2",
        "files": [("Skill Paths.md", None)],
        "sections": [
            ("Skill Paths.md", "Combat / Muscle (STR)#Tier 1 — Good"),
            ("Skill Paths.md", "Combat / Muscle (STR)#Tier 2 — Great"),
            ("Skill Paths.md", "Combat / Muscle (STR)#Tier 3 — Amazing"),
            ("Skill Paths.md", "Shooting / Perception (DEX)#Tier 1 — Good"),
            ("Skill Paths.md", "Shooting / Perception (DEX)#Tier 2 — Great"),
            ("Skill Paths.md", "Shooting / Perception (DEX)#Tier 3 — Amazing"),
            ("Skill Paths.md", "Movement / Acrobatics (AGI)#Tier 1 — Good"),
            ("Skill Paths.md", "Movement / Acrobatics (AGI)#Tier 2 — Great"),
            ("Skill Paths.md", "Movement / Acrobatics (AGI)#Tier 3 — Amazing"),
            ("Skill Paths.md", "Expertise / Knowledge (INT)#Tier 1 — Good"),
            ("Skill Paths.md", "Expertise / Knowledge (INT)#Tier 2 — Great"),
            ("Skill Paths.md", "Expertise / Knowledge (INT)#Tier 3 — Amazing"),
            ("Skill Paths.md", "Bravery / Morale (NRV)#Tier 1 — Good"),
            ("Skill Paths.md", "Bravery / Morale (NRV)#Tier 2 — Great"),
            ("Skill Paths.md", "Bravery / Morale (NRV)#Tier 3 — Amazing"),
        ],
    },
    {
        "label": "⑪ SCENARIOS & CAMPAIGN — what you fight over, and after",
        "color": "3",
        "files": [("Scenarios.md", None), ("Campaign.md", None)],
        "sections": [],
    },
    {
        "label": "⑫ STRUCTURES — the 25-entry settlement catalogue",
        "color": "3",
        "files": [("Structures.md", None)],
        "sections": [],
    },
    {
        "label": "⑬ TABLE & COMPONENT REFERENCE",
        "color": "6",
        "files": [("Board Representation.md", None)],
        "sections": [],
    },
    {
        "label": "⑭ DESIGN GUARDS — what was cut, and why (check before inventing)",
        "color": "2",
        "files": [("Out of Scope — What Settlements is NOT.md", None)],
        "sections": [],
    },
    {
        "label": "⑮ EVIDENCE — simulation findings behind the numbers",
        "color": "6",
        "files": [
            ("Crew Sim — Findings.md", None),
            ("Dice Mechanic — Sim Findings.md", None),
            ("Skill Sim — Findings.md", None),
            ("Deployables Sim — Findings.md", None),
            ("Terrain Hacking Cover — Sim Findings.md", None),
        ],
        "sections": [],
    },
]

# Notes that are tooling / project management, never rules content.
EXCLUDE_FILES = {
    "Obsidian Guide — Building Settlements.md",
    "Quick Reference — Writing Rules.md",
    "Rules System — Master Roadmap.md",
    "Interviews — Completing the Rules System.md",
}

BANNER = """# 🧮 Rules Tables — the whole system on one wall

Every table in the Settlements rules, live-embedded from its source note. **Edit the rule, not the card** — change a value in `Weapons.md` and it changes here.

**Costs shown are the printed vault prices** (100-point crew budget). The repo's `docs/POINTS-TABLE.md` v0.2 holds a rebuilt **1000-point** derivation that has *not* been propagated into these notes yet — the two scales disagree until it is.

Re-run `scripts/build_rules_tables_canvas.py` after adding a new table."""


# ---------------------------------------------------------------- table parsing

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", text)
    text = re.sub(r"[*_`#]", "", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")[:44] or "table"


def find_tables(path: Path) -> list[dict]:
    """Return every markdown table in a note with its heading breadcrumb."""
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[dict] = []
    heads: list[str] = []
    i, n = 0, len(lines)
    in_fm = bool(lines) and lines[0].strip() == "---"
    while i < n:
        line = lines[i]
        if in_fm:
            if i > 0 and line.strip() == "---":
                in_fm = False
            i += 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            lvl = len(h.group(1))
            heads = heads[: lvl - 1] + [h.group(2).strip()]
            i += 1
            continue
        if re.match(r"^\s*\|.*\|\s*$", line):
            j = i
            while j < n and re.match(r"^\s*\|.*\|\s*$", lines[j]):
                j += 1
            body = lines[i:j]
            if len(body) >= 2 and re.match(r"^\s*\|[\s:\-|]+\|\s*$", body[1]):
                out.append(
                    {
                        "file": path,
                        "heading": heads[-1] if heads else path.stem,
                        "crumb": list(heads),
                        "start": i,
                        "end": j,
                        "body": body,
                        "existing_id": _existing_id(lines, j),
                    }
                )
            i = j
            continue
        i += 1
    return out


def _existing_id(lines: list[str], j: int) -> str | None:
    """Obsidian wants a table's block ID on its own line, blank line either side."""
    k = j
    while k < len(lines) and not lines[k].strip():
        k += 1
    if k < len(lines):
        m = re.match(r"^\^([A-Za-z0-9\-]+)$", lines[k].strip())
        if m:
            return m.group(1)
    return None


def inject_ids(tables: list[dict], dry: bool) -> None:
    """Write `^tbl-slug` under each table, blank-line separated. Idempotent."""
    by_file: dict[Path, list[dict]] = {}
    for t in tables:
        by_file.setdefault(t["file"], []).append(t)

    for path, group in by_file.items():
        lines = path.read_text(encoding="utf-8").split("\n")
        used: set[str] = set(re.findall(r"^\^([A-Za-z0-9\-]+)$", "\n".join(lines), re.M))
        inserts: list[tuple[int, list[str]]] = []
        for t in group:
            if t["existing_id"]:
                t["block_id"] = t["existing_id"]
                continue
            base = f"tbl-{slugify(t['heading'])}"
            bid, k = base, 2
            while bid in used:
                bid, k = f"{base}-{k}", k + 1
            used.add(bid)
            t["block_id"] = bid
            # table │ blank │ ^id │ blank │ whatever followed
            block = ["", f"^{bid}"]
            if t["end"] < len(lines) and lines[t["end"]].strip():
                block.append("")
            inserts.append((t["end"], block))
        if not inserts:
            continue
        for at, block in sorted(inserts, key=lambda p: p[0], reverse=True):
            lines[at:at] = block
        print(f"  + {len(inserts):2d} block id(s) -> {path.name}")
        if not dry:
            path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------- sizing

def size_table(body: list[str]) -> tuple[int, int]:
    widest = max(len(re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", r)) for r in body)
    w = max(CARD_MIN_W, min(CARD_MAX_W, int(widest * 8.2) + 40))
    wrap_factor = max(1.0, (widest * 8.2 + 40) / w)
    rows = len(body) - 1  # separator row renders as the header rule
    h = int(60 + rows * ROW_H * wrap_factor)
    return w, max(h, 130)


def size_section(path: Path, subpath: str) -> tuple[int, int, str]:
    """Estimate a heading-embed card, and return its display title.

    `subpath` is Obsidian's nested form, e.g. `Parent Heading#Child Heading`.
    """
    text = path.read_text(encoding="utf-8")
    parts = [p for p in subpath.split("#") if p]
    title = parts[-1]

    def heading_at(name: str, after: int) -> re.Match | None:
        pat = re.compile(r"^#{1,6}[ \t]+" + re.escape(name) + r"[ \t]*$", re.M)
        return pat.search(text, after)

    cursor = 0
    match = None
    for name in parts:
        match = heading_at(name, cursor)
        if not match:
            print(f"  ! heading not found: {path.name}#{name}")
            return 760, 400, title
        cursor = match.end()

    nxt = re.search(r"^#{1,6}[ \t]+", text[match.end() :], re.M)
    chunk = text[match.end() : match.end() + (nxt.start() if nxt else 4000)]
    w = 760
    chars_per_line = w / 7.4
    est_lines = sum(max(1, int(len(ln) / chars_per_line) + 1) for ln in chunk.split("\n") if ln.strip())
    return w, max(180, int(60 + est_lines * 26)), title


# ---------------------------------------------------------------- canvas build

def build() -> dict:
    dry = "--dry-run" in sys.argv
    nodes: list[dict] = []
    nid = [0]

    def new_id(tag: str) -> str:
        nid[0] += 1
        return f"{tag}{nid[0]:04d}"

    # collect every table we intend to show, per band
    all_tables: list[dict] = []
    band_items: list[list[dict]] = []
    for band in SPEC:
        items: list[dict] = []
        for fname, only in band["files"]:
            path = RULES / fname
            if fname in EXCLUDE_FILES or not path.exists():
                print(f"  ! missing {fname}")
                continue
            for t in find_tables(path):
                if only and t["heading"] not in only:
                    continue
                items.append({"kind": "table", "t": t, "fname": fname})
                all_tables.append(t)
        for fname, subpath in band["sections"]:
            items.append({"kind": "section", "fname": fname, "subpath": subpath})
        band_items.append(items)

    print(f"Tables found: {len(all_tables)}")
    headings_mode = "--headings" in sys.argv
    if headings_mode:
        print("  (heading-embed mode — cards show the whole section, not just the table)")
    else:
        inject_ids(all_tables, dry)

    # lay out: one group column per band, wrapping into sub-columns when tall
    MAX_COL_H = 5200
    x = 0
    for band, items in zip(SPEC, band_items):
        placed: list[dict] = []
        col_x, col_y, col_w = 0, 0, 0
        for it in items:
            if it["kind"] == "table":
                t = it["t"]
                w, h = size_table(t["body"])
                title = t["heading"]
                if headings_mode:
                    subpath = "#" + "#".join(t["crumb"][1:] or t["crumb"])
                    h += 160  # the section carries prose around the table
                else:
                    subpath = f"#^{t['block_id']}"
                fname = it["fname"]
            else:
                w, h, title = size_section(RULES / it["fname"], it["subpath"])
                subpath = "#" + it["subpath"]
                fname = it["fname"]
            block_h = TITLE_H + 8 + h
            if col_y and col_y + block_h > MAX_COL_H:
                col_x += col_w + COL_GAP
                col_y, col_w = 0, 0
            note = Path(fname).stem
            placed.append(
                {
                    "id": new_id("t"),
                    "type": "text",
                    "text": f"**{note} · {title}**",
                    "x": col_x,
                    "y": col_y,
                    "width": w,
                    "height": TITLE_H,
                    "color": band["color"],
                }
            )
            placed.append(
                {
                    "id": new_id("f"),
                    "type": "file",
                    "file": f"{VAULT_PREFIX}/{fname}",
                    "subpath": subpath,
                    "x": col_x,
                    "y": col_y + TITLE_H + 8,
                    "width": w,
                    "height": h,
                }
            )
            col_y += block_h + GAP_Y
            col_w = max(col_w, w)
        if not placed:
            continue
        min_x = min(n["x"] for n in placed)
        max_x = max(n["x"] + n["width"] for n in placed)
        max_y = max(n["y"] + n["height"] for n in placed)
        dx = x - min_x + GROUP_PAD
        for n in placed:
            n["x"] += dx
        nodes.append(
            {
                "id": new_id("g"),
                "type": "group",
                "label": band["label"],
                "x": x,
                "y": -GROUP_PAD,
                "width": (max_x - min_x) + GROUP_PAD * 2,
                "height": max_y + GROUP_PAD * 2,
                "color": band["color"],
            }
        )
        nodes.extend(placed)
        x += (max_x - min_x) + GROUP_PAD * 2 + 160

    nodes.insert(
        0,
        {
            "id": "banner",
            "type": "text",
            "text": BANNER,
            "x": 0,
            "y": -620,
            "width": 1500,
            "height": 440,
            "color": "5",
        },
    )
    return {"nodes": nodes, "edges": []}


if __name__ == "__main__":
    canvas = build()
    if "--dry-run" in sys.argv:
        print(f"[dry-run] {len(canvas['nodes'])} nodes; canvas not written")
    else:
        CANVAS.write_text(json.dumps(canvas, indent="\t", ensure_ascii=False), encoding="utf-8")
        print(f"Wrote {CANVAS} — {len(canvas['nodes'])} nodes")

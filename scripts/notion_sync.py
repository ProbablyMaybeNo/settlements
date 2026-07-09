"""
notion_sync.py — Bidirectional sync between local Settlements files and Notion.

Local files are source of truth. Notion is the visualisation/steering layer.
Pushes CSV rows to Notion databases; pulls mutable fields (status) back to
local CSVs.

SETUP (one-time):
  1. Create an internal integration at https://www.notion.so/my-integrations
     - Name: Settlements Sync
     - Capabilities: Read, Update, Insert content
  2. Copy the secret token (starts with "secret_" or "ntn_")
  3. Set env var: NOTION_API_KEY=<token>
     Or create .env in project root with: NOTION_API_KEY=<token>
  4. In Notion, open the Settlements parent page > "..." > "Add connections"
     > select your "Settlements Sync" integration. This grants access to all
     child pages and databases.
  5. Run: py -3.13 scripts/notion_sync.py sync-all

USAGE:
  py -3.13 scripts/notion_sync.py <command> [--dry-run] [--verbose]

COMMANDS:
  sync-factions      Push TRACKERS/factions.csv     -> Factions DB
  sync-units         Push TRACKERS/units.csv        -> Units DB
  sync-weapons       Push TRACKERS/weapons.csv      -> Weapons DB
  sync-equipment     Push TRACKERS/equipment.csv    -> Equipment DB
  sync-scenarios     Push TRACKERS/scenarios.csv    -> Scenarios DB
  sync-locations     Push TRACKERS/locations.csv    -> Locations DB
  sync-characters    Push TRACKERS/characters.csv   -> Characters DB
  sync-playtests     Push TRACKERS/playtests.csv    -> Playtests DB
  sync-art           Push TRACKERS/art-assets.csv   -> Art Assets DB
  sync-3d            Push TRACKERS/3d-models.csv    -> 3D Models DB
  sync-ideas         Push TRACKERS/ideas.csv        -> Ideas Inbox DB
  sync-rules         Push TRACKERS/rules.csv        -> Rules DB
  sync-all           Run every sync command
  pull-status        Pull Status changes from Notion back into local CSVs
  reconcile          Populate page_ids from existing Notion rows
  status             Show sync state summary
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
IDS_FILE = ROOT / ".notion-ids.json"
STATE_FILE = ROOT / ".notion-sync-state.json"
ENV_FILE = ROOT / ".env"
NOTION_VERSION = "2022-06-28"
API_BASE = "https://api.notion.com/v1"


# ---------- Setup ----------

def load_env() -> None:
    """Read .env if present. Project-local .env overrides shell env vars."""
    if not ENV_FILE.exists():
        return
    for raw in ENV_FILE.read_text(encoding="utf-8-sig").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ[key.strip()] = value.strip().strip('"').strip("'")


def load_ids() -> dict:
    if not IDS_FILE.exists():
        raise SystemExit(f"Missing {IDS_FILE}. Run initial Notion build first.")
    return json.loads(IDS_FILE.read_text(encoding="utf-8"))


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"last_sync": None, "row_hashes": {}, "page_ids": {}}


def save_state(state: dict) -> None:
    state["last_sync"] = datetime.now(timezone.utc).isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def row_hash(row: dict) -> str:
    return hashlib.sha256(
        json.dumps(row, sort_keys=True, default=str).encode()
    ).hexdigest()[:16]


# ---------- Notion client ----------

class Notion:
    def __init__(self, token: str, verbose: bool = False, dry_run: bool = False):
        self.token = token
        self.verbose = verbose
        self.dry_run = dry_run

    def _request(self, method: str, path: str, body: dict | None = None) -> dict:
        url = f"{API_BASE}{path}"
        if self.dry_run and method in ("POST", "PATCH", "DELETE"):
            if self.verbose:
                print(f"  [dry-run] {method} {path}")
            return {}
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Notion-Version", NOTION_VERSION)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as exc:
            body_text = exc.read().decode(errors="replace")
            raise SystemExit(f"Notion API {exc.code}: {body_text}") from exc

    def query_database(self, database_id: str, filter_: dict | None = None) -> list[dict]:
        results: list[dict] = []
        cursor: str | None = None
        while True:
            body: dict = {"page_size": 100}
            if filter_:
                body["filter"] = filter_
            if cursor:
                body["start_cursor"] = cursor
            response = self._request("POST", f"/databases/{database_id}/query", body)
            results.extend(response.get("results", []))
            if not response.get("has_more"):
                break
            cursor = response.get("next_cursor")
        return results

    def create_page(self, database_id: str, properties: dict) -> dict:
        return self._request("POST", "/pages", {
            "parent": {"database_id": database_id},
            "properties": properties,
        })

    def update_page(self, page_id: str, properties: dict) -> dict:
        return self._request("PATCH", f"/pages/{page_id}", {"properties": properties})


# ---------- Property builders ----------

def title(text: str) -> dict:
    return {"title": [{"text": {"content": text or ""}}]}


def rich_text(text: str) -> dict:
    return {"rich_text": [{"text": {"content": text}}]} if text else {"rich_text": []}


def select(value: str) -> dict:
    return {"select": {"name": value}} if value else {"select": None}


def multi_select(values: list[str]) -> dict:
    return {"multi_select": [{"name": v} for v in values if v]}


def number(value: str | int | float | None) -> dict:
    if value in (None, ""):
        return {"number": None}
    try:
        return {"number": float(value)}
    except (TypeError, ValueError):
        return {"number": None}


def date(value: str | None) -> dict:
    if not value:
        return {"date": None}
    return {"date": {"start": value}}


def checkbox(value: Any) -> dict:
    truthy = {True, "true", "True", "yes", "Yes", "1", 1}
    return {"checkbox": value in truthy}


def url_prop(value: str) -> dict:
    return {"url": value or None}


# ---------- Generic row sync ----------

def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        # csv.DictReader puts overflow fields under a None key when a row has
        # more values than columns (e.g. an unescaped comma in a notes field).
        # Drop it so json.dumps(sort_keys=True) doesn't choke comparing None to str.
        rows = []
        for row in csv.DictReader(handle):
            rows.append({k: v for k, v in row.items() if k is not None})
        return rows


def upsert_rows(
    notion: Notion,
    state: dict,
    tracker_key: str,
    database_id: str,
    rows: list[dict],
    id_col: str,
    build_properties: Callable[[dict], dict],
    title_col: str | None = None,
) -> tuple[int, int, int]:
    """Upsert rows. Returns (created, updated, skipped)."""
    hashes = state["row_hashes"].setdefault(tracker_key, {})
    page_ids = state["page_ids"].setdefault(tracker_key, {})
    created = updated = skipped = 0

    for row in rows:
        local_id = row.get(id_col) or (row.get(title_col) if title_col else None)
        if not local_id:
            continue
        # Skip rows where the title-equivalent is empty (typical scaffold rows)
        if title_col and not row.get(title_col):
            continue
        new_hash = row_hash(row)
        if hashes.get(local_id) == new_hash and local_id in page_ids:
            skipped += 1
            continue
        properties = build_properties(row)
        if local_id in page_ids:
            notion.update_page(page_ids[local_id], properties)
            updated += 1
        else:
            result = notion.create_page(database_id, properties)
            page_id = result.get("id") if not notion.dry_run else f"dry-{local_id}"
            page_ids[local_id] = page_id
            created += 1
        hashes[local_id] = new_hash

    return created, updated, skipped


# ---------- Per-tracker property builders ----------

def factions_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Faction ID": rich_text(row.get("faction_id", "")),
        "Strongest In": rich_text(row.get("strongest_in", "")),
        "Weakness": rich_text(row.get("weakness", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("family"):
        props["Family"] = select(row["family"])
    if row.get("ideology_code"):
        props["Ideology"] = select(row["ideology_code"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def units_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Unit ID": rich_text(row.get("unit_id", "")),
        "Faction ID": rich_text(row.get("faction_id", "")),
        "Equipment": rich_text(row.get("equipment", "")),
        "Special Rules": rich_text(row.get("special_rules", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("role"):
        props["Role"] = select(row["role"])
    for csv_col, notion_col in (
        ("move", "Move"), ("shoot", "Shoot"), ("fight", "Fight"),
        ("resolve", "Resolve"), ("hp", "HP"), ("armor", "Armor"),
        ("cost", "Cost"),
    ):
        if row.get(csv_col):
            props[notion_col] = number(row[csv_col])
    return props


def weapons_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Weapon ID": rich_text(row.get("weapon_id", "")),
        "Range": rich_text(row.get("range", "")),
        "Traits": rich_text(row.get("traits", "")),
        "Faction Availability": rich_text(row.get("faction_availability", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("type"):
        props["Type"] = select(row["type"])
    for csv_col, notion_col in (("damage", "Damage"), ("attacks", "Attacks")):
        if row.get(csv_col):
            props[notion_col] = number(row[csv_col])
    return props


def equipment_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Equipment ID": rich_text(row.get("equipment_id", "")),
        "Effect": rich_text(row.get("effect", "")),
        "Faction Availability": rich_text(row.get("faction_availability", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("type"):
        props["Type"] = select(row["type"])
    if row.get("cost"):
        props["Cost"] = number(row["cost"])
    return props


def scenarios_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Scenario ID": rich_text(row.get("scenario_id", "")),
        "Attacker": rich_text(row.get("attacker", "")),
        "Defender": rich_text(row.get("defender", "")),
        "Objectives": rich_text(row.get("objectives", "")),
        "Victory Conditions": rich_text(row.get("victory_conditions", "")),
        "Rules Version": rich_text(row.get("rules_version", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("type"):
        props["Type"] = select(row["type"])
    if row.get("region_archetype"):
        props["Region"] = select(row["region_archetype"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def locations_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Location ID": rich_text(row.get("location_id", "")),
        "Tactical Value": rich_text(row.get("tactical_value", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("region_archetype"):
        props["Region"] = select(row["region_archetype"])
    if row.get("controller"):
        props["Controller"] = select(row["controller"])
    if row.get("terrain"):
        props["Terrain"] = select(row["terrain"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def characters_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Character ID": rich_text(row.get("character_id", "")),
        "Faction ID": rich_text(row.get("faction_id", "")),
        "Role": rich_text(row.get("role", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def playtests_properties(row: dict) -> dict:
    label = f"Playtest {row.get('date', '')} {row.get('scenario_id', '')}"
    props = {
        "Session": title(label.strip()),
        "Playtest ID": rich_text(row.get("playtest_id", "")),
        "Scenario ID": rich_text(row.get("scenario_id", "")),
        "Rules Version": rich_text(row.get("rules_version", "")),
        "Outcome": rich_text(row.get("outcome", "")),
        "Question": rich_text(row.get("question", "")),
        "Findings": rich_text(row.get("findings", "")),
        "Follow Up": rich_text(row.get("follow_up", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("date"):
        props["Date"] = date(row["date"])
    if row.get("duration_minutes"):
        props["Duration (min)"] = number(row["duration_minutes"])
    return props


def art_assets_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Asset ID": rich_text(row.get("asset_id", "")),
        "Subject": rich_text(row.get("subject", "")),
        "File Path": rich_text(row.get("file_path", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("type"):
        props["Type"] = select(row["type"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def models_3d_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Model ID": rich_text(row.get("model_id", "")),
        "Subject": rich_text(row.get("subject", "")),
        "Source Path": rich_text(row.get("source_path", "")),
        "STL Path": rich_text(row.get("stl_path", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("scale"):
        props["Scale"] = select(row["scale"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


def ideas_properties(row: dict) -> dict:
    props = {
        "Title": title(row.get("title", "")),
        "Idea ID": rich_text(row.get("idea_id", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("tag"):
        props["Tag"] = select(row["tag"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    if row.get("date_added"):
        props["Date Added"] = date(row["date_added"])
    return props


def rules_properties(row: dict) -> dict:
    props = {
        "Name": title(row.get("name", "")),
        "Rule ID": rich_text(row.get("rule_id", "")),
        "Version": rich_text(row.get("version", "")),
        "Text": rich_text(row.get("text", "")),
        "Notes": rich_text(row.get("notes", "")),
    }
    if row.get("category"):
        props["Category"] = select(row["category"])
    if row.get("status"):
        props["Status"] = select(row["status"])
    return props


# ---------- Tracker registry ----------

# tracker key -> (notion DB key, csv path, id column, builder, title-fallback column)
TRACKERS: dict[str, tuple[str, str, str, Callable[[dict], dict], str]] = {
    "factions":   ("factions",   "TRACKERS/factions.csv",   "faction_id",   factions_properties,   "name"),
    "units":      ("units",      "TRACKERS/units.csv",      "unit_id",      units_properties,      "name"),
    "weapons":    ("weapons",    "TRACKERS/weapons.csv",    "weapon_id",    weapons_properties,    "name"),
    "equipment":  ("equipment",  "TRACKERS/equipment.csv",  "equipment_id", equipment_properties,  "name"),
    "scenarios":  ("scenarios",  "TRACKERS/scenarios.csv",  "scenario_id",  scenarios_properties,  "name"),
    "locations":  ("locations",  "TRACKERS/locations.csv",  "location_id",  locations_properties,  "name"),
    "characters": ("characters", "TRACKERS/characters.csv", "character_id", characters_properties, "name"),
    "playtests":  ("playtests",  "TRACKERS/playtests.csv",  "playtest_id",  playtests_properties,  "date"),
    "art":        ("art_assets", "TRACKERS/art-assets.csv", "asset_id",     art_assets_properties, "name"),
    "3d":         ("models_3d",  "TRACKERS/3d-models.csv",  "model_id",     models_3d_properties,  "name"),
    "ideas":      ("ideas",      "TRACKERS/ideas.csv",      "idea_id",      ideas_properties,      "title"),
    "rules":      ("rules",      "TRACKERS/rules.csv",      "rule_id",      rules_properties,      "name"),
}

# (notion column name, kind) used to find existing rows during reconcile
RECONCILE_ID_PROPS: dict[str, tuple[str, str]] = {
    "factions":   ("Faction ID",    "rich_text"),
    "units":      ("Unit ID",       "rich_text"),
    "weapons":    ("Weapon ID",     "rich_text"),
    "equipment":  ("Equipment ID",  "rich_text"),
    "scenarios":  ("Scenario ID",   "rich_text"),
    "locations":  ("Location ID",   "rich_text"),
    "characters": ("Character ID",  "rich_text"),
    "playtests":  ("Playtest ID",   "rich_text"),
    "art":        ("Asset ID",      "rich_text"),
    "3d":         ("Model ID",      "rich_text"),
    "ideas":      ("Idea ID",       "rich_text"),
    "rules":      ("Rule ID",       "rich_text"),
}


def _plain(prop: dict | None, kind: str) -> str:
    if not prop:
        return ""
    parts = prop.get(kind, []) or []
    return "".join(p.get("plain_text", "") for p in parts)


def _title_text(page: dict) -> str:
    """Pull the title-property plain text from a Notion page, whichever the
    title column is named (Name / Title / Session / ...)."""
    for prop in page.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(p.get("plain_text", "") for p in prop.get("title", []))
    return ""


def reconcile(notion: Notion, ids: dict, state: dict) -> None:
    """Populate page_ids from existing Notion rows so future syncs are idempotent.

    For each tracker, match Notion rows to local CSV rows. Prefer the ID column;
    fall back to title if the local row has no ID (seed rows often leave the ID
    blank — title is the next-best stable identifier)."""
    for tracker, (notion_col, kind) in RECONCILE_ID_PROPS.items():
        db_key, csv_rel, id_col, _builder, fallback_id = TRACKERS[tracker]
        if db_key not in ids.get("databases", {}):
            continue
        database_id = ids["databases"][db_key]["database_id"]
        pages = notion.query_database(database_id)

        # Build two lookups from Notion: by ID, and by title.
        by_id: dict[str, str] = {}
        by_title: dict[str, str] = {}
        for page in pages:
            ident = _plain(page.get("properties", {}).get(notion_col), kind).strip()
            if ident:
                by_id[ident] = page["id"]
            title_text = _title_text(page).strip()
            if title_text:
                by_title[title_text] = page["id"]

        # Walk local CSV rows in the same order sync uses, and match.
        mapping = state["page_ids"].setdefault(tracker, {})
        hashes = state["row_hashes"].setdefault(tracker, {})
        rows = read_csv(ROOT / csv_rel)
        matched = 0
        for row in rows:
            local_id = row.get(id_col) or (row.get(fallback_id) if fallback_id else None)
            if not local_id:
                continue
            page_id = by_id.get(local_id) or by_title.get(local_id)
            if page_id:
                mapping[local_id] = page_id
                hashes[local_id] = row_hash(row)
                matched += 1
        print(f"  {tracker}: reconciled {matched} of {len(rows)} local row(s)")


def run_tracker_sync(tracker: str, notion: Notion, ids: dict, state: dict) -> None:
    db_key, csv_rel, id_col, builder, fallback_id = TRACKERS[tracker]
    if db_key not in ids.get("databases", {}):
        print(f"  {tracker}: skipped (no DB id in .notion-ids.json)")
        return
    database_id = ids["databases"][db_key]["database_id"]
    csv_path = ROOT / csv_rel
    rows = read_csv(csv_path)
    effective_id = id_col or fallback_id
    if not rows:
        print(f"  {tracker}: no rows in {csv_rel}")
        return
    created, updated, skipped = upsert_rows(
        notion, state, tracker, database_id, rows, effective_id, builder, fallback_id
    )
    print(f"  {tracker}: {created} created · {updated} updated · {skipped} unchanged")


# ---------- Pull from Notion ----------

PULLABLE = {
    "playtests":  ("Playtest ID",  "TRACKERS/playtests.csv",  "playtest_id"),
    "ideas":      ("Idea ID",      "TRACKERS/ideas.csv",      "idea_id"),
    "rules":      ("Rule ID",      "TRACKERS/rules.csv",      "rule_id"),
}


def pull_status(notion: Notion, ids: dict) -> None:
    """Pull Status changes from Notion back to local CSVs (idempotent)."""
    for tracker, (notion_id_col, csv_rel, csv_id_col) in PULLABLE.items():
        db_key = TRACKERS[tracker][0]
        if db_key not in ids.get("databases", {}):
            continue
        database_id = ids["databases"][db_key]["database_id"]
        pages = notion.query_database(database_id)
        status_by_id: dict[str, str] = {}
        for page in pages:
            props = page.get("properties", {})
            local_id = _plain(props.get(notion_id_col), "rich_text").strip()
            status = (props.get("Status", {}).get("select") or {}).get("name", "")
            if local_id and status:
                status_by_id[local_id] = status

        csv_path = ROOT / csv_rel
        if not csv_path.exists():
            continue
        with csv_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fieldnames = reader.fieldnames or []
            local_rows = list(reader)
        updated = 0
        for row in local_rows:
            cid = row.get(csv_id_col, "")
            if cid in status_by_id and row.get("status") != status_by_id[cid]:
                row["status"] = status_by_id[cid]
                updated += 1
        if updated:
            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(local_rows)
            print(f"  {tracker}: pulled {updated} status change(s)")
        else:
            print(f"  {tracker}: no status changes")


# ---------- CLI ----------

def main(argv: list[str] | None = None) -> int:
    load_env()
    token = os.environ.get("NOTION_API_KEY")
    sync_choices = [f"sync-{k}" for k in TRACKERS] + ["sync-all"]
    parser = argparse.ArgumentParser(description="Notion sync for the Settlements project.")
    parser.add_argument("command", choices=[*sync_choices, "pull-status", "reconcile", "status"])
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    if args.command == "status":
        state = load_state()
        print(f"Last sync: {state.get('last_sync') or 'never'}")
        for tracker, hashes in state.get("row_hashes", {}).items():
            print(f"  {tracker}: {len(hashes)} tracked rows")
        return 0

    if not token:
        print(
            "ERROR: NOTION_API_KEY not set.\n"
            "  1. Create an integration at https://www.notion.so/my-integrations\n"
            "  2. Add it to the Settlements parent page (Notion UI > ... > Add connections)\n"
            "  3. Set env: NOTION_API_KEY=<secret> (or add to .env)",
            file=sys.stderr,
        )
        return 1

    ids = load_ids()
    state = load_state()
    notion = Notion(token, verbose=args.verbose, dry_run=args.dry_run)

    print(f"notion_sync · command={args.command} · dry_run={args.dry_run}")

    try:
        if args.command == "reconcile":
            reconcile(notion, ids, state)
        elif args.command == "pull-status":
            pull_status(notion, ids)
        elif args.command == "sync-all":
            for tracker in TRACKERS:
                try:
                    run_tracker_sync(tracker, notion, ids, state)
                except SystemExit as exc:
                    # Transient Notion error on one tracker shouldn't lose
                    # the state from the trackers that already succeeded.
                    print(f"  {tracker}: FAILED ({exc}) — continuing")
                finally:
                    save_state(state)
            pull_status(notion, ids)
        else:
            tracker = args.command.removeprefix("sync-")
            run_tracker_sync(tracker, notion, ids, state)
    finally:
        save_state(state)
    print(f"done · state written to {STATE_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

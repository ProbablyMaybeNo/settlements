"""Build `settlements-sims.db` - one queryable store for every sim result.

    py -3.13 test-bench/explorer/build_db.py

WHAT THIS IS FOR
----------------
Answering "what is the percentage chance to injure a unit while firing weapon X
with stat line Y" without opening a script. Two kinds of thing live here and
they are NOT the same kind of thing, so they are kept in separate tables:

  DERIVED   `shot_matrix`, `weapon_shot`. Exact closed-form probabilities over
            the locked core engine, recomputed from scratch every build. No
            sampling error, no provenance needed - if the engine changes, these
            change with it on the next build. This is the table to search.

  MEASURED  `sim_runs`, `sim_values`. The stamped Monte-Carlo envelopes in
            balance/results/. These CANNOT be recomputed and they carry
            fingerprints, so every row keeps its engine / cost-table / harness
            hash and a `stale` flag against what those hashes are today.

Mixing the two would be the project's own false-freshness failure in a new
place: a derived number is current by construction, a measured one is current
only if nothing it depended on has moved since. The `provenance` column says
which kind every row is, so a query can never quietly average them together.

COSTS are read live from points/ticks.py at build time, never hardcoded.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
BENCH = HERE.parent
REPO = BENCH.parent
sys.path.insert(0, str(BENCH))

from points import skills as SK                            # noqa: E402
from points import ticks as T                              # noqa: E402
from points import units as U                              # noqa: E402
from points.catalogue import SAMPLE_ARMOURY                # noqa: E402
from points.weapons import WeaponBuild, weapon_cost        # noqa: E402

sys.path.insert(0, str(BENCH / "harness"))
import provenance as P                                     # noqa: E402

DB = HERE / "settlements-sims.db"
RESULTS = BENCH / "balance" / "results"

COVERS = [("open", 0), ("light", -1), ("heavy", -2), ("hidden", -3)]
ARMOURS = [("unarmoured", 0), ("light", -1), ("heavy", -2)]
MOD_CAP = 3


# ==========================================================================
# The engine. Identical to sim_report.py / attack_dice_sim.py.
# ==========================================================================
def core_exact(mod: int, target: int = 7) -> float:
    """P(1d10 + mod >= target). Nat 1 always fails, nat 10 always succeeds."""
    w = 0
    for d in range(1, 11):
        if d == 1:
            continue
        if d == 10:
            w += 1
            continue
        if d + mod >= target:
            w += 1
    return w / 10


def chain(stat: int, cover_mod: int, extra_hit: int, damage: int, armour_mod: int,
          dice: int) -> dict:
    """One Action's worth of the full Shooting -> Injury chain, exactly."""
    to_hit_mod = cover_mod + extra_hit
    capped = max(-MOD_CAP, min(MOD_CAP, to_hit_mod))
    p_hit = core_exact(stat + capped)
    p_inj = core_exact(damage + armour_mod)
    w = p_hit * p_inj                 # wound
    s = p_hit * (1 - p_inj)           # Pinned: hit, failed to wound
    miss = 1 - p_hit

    p_down = 1 - (1 - w) ** dice
    live = sum((1 - w) ** i for i in range(dice))   # dice that actually resolve

    # P(>= 2 Pins) under stop_on_down - the Break-test trigger (Morale: 2+).
    # Terminal sequences only: end on a wound at position i, or run all n dry.
    from itertools import product
    p2 = 0.0
    for i in range(1, dice + 1):
        for pre in product("pm", repeat=i - 1):
            pr, pins = w, 0
            for ch in pre:
                pr *= s if ch == "p" else miss
                pins += 1 if ch == "p" else 0
            if pins >= 2:
                p2 += pr
    for seq in product("pm", repeat=dice):
        pr, pins = 1.0, 0
        for ch in seq:
            pr *= s if ch == "p" else miss
            pins += 1 if ch == "p" else 0
        if pins >= 2:
            p2 += pr

    return {
        "to_hit_mod_raw": to_hit_mod,
        "to_hit_mod_applied": capped,
        "over_mod_cap": int(to_hit_mod != capped),
        "to_hit": round(p_hit, 4),
        "injure_given_hit": round(p_inj, 4),
        "wound_per_die": round(w, 4),
        "stress_per_die": round(s, 4),
        "p_wound_action": round(p_down, 4),
        "e_wounds_resolve_all": round(dice * w, 4),
        "e_wounds_stop_on_down": round(p_down, 4),
        "e_stress_resolve_all": round(dice * s, 4),
        "e_stress_stop_on_down": round(s * live, 4),
        "p_break_test": round(p2, 4),
        "actions_to_down": round(1 / p_down, 3) if p_down else None,
    }


# ==========================================================================
def build_schema(cx: sqlite3.Connection) -> None:
    cx.executescript("""
    DROP TABLE IF EXISTS shot_matrix;
    CREATE TABLE shot_matrix (
      id INTEGER PRIMARY KEY,
      provenance TEXT DEFAULT 'derived-exact',
      stat INTEGER, stat_label TEXT,
      cover TEXT, cover_mod INTEGER,
      extra_to_hit INTEGER,
      to_hit_mod_raw INTEGER, to_hit_mod_applied INTEGER, over_mod_cap INTEGER,
      armour TEXT, armour_mod INTEGER,
      damage INTEGER, damage_label TEXT,
      attack_dice INTEGER,
      to_hit REAL, injure_given_hit REAL,
      wound_per_die REAL, stress_per_die REAL,
      p_wound_action REAL,
      e_wounds_resolve_all REAL, e_wounds_stop_on_down REAL,
      e_stress_resolve_all REAL, e_stress_stop_on_down REAL,
      p_break_test REAL, actions_to_down REAL
    );

    DROP TABLE IF EXISTS weapons;
    CREATE TABLE weapons (
      name TEXT PRIMARY KEY, class TEXT, damage INTEGER, reach INTEGER,
      characteristics TEXT, drawbacks TEXT, credits INTEGER,
      min_rank TEXT, slots INTEGER, manufactured INTEGER,
      damage_band TEXT, range_band TEXT, provenance TEXT DEFAULT 'points-engine'
    );

    DROP TABLE IF EXISTS weapon_shot;
    CREATE TABLE weapon_shot (
      id INTEGER PRIMARY KEY, provenance TEXT DEFAULT 'derived-exact',
      weapon TEXT, class TEXT, damage INTEGER, weapon_credits INTEGER,
      stat INTEGER, cover TEXT, armour TEXT, attack_dice INTEGER,
      to_hit REAL, injure_given_hit REAL, p_wound_action REAL,
      e_wounds_stop_on_down REAL, e_stress_stop_on_down REAL,
      actions_to_down REAL,
      carrier_rank TEXT, fielded_credits INTEGER,
      wounds_per_action_per_100cr REAL
    );

    DROP TABLE IF EXISTS bodies;
    CREATE TABLE bodies (rank TEXT PRIMARY KEY, credits INTEGER,
                         stat_points INTEGER, orders INTEGER,
                         provenance TEXT DEFAULT 'points-engine');

    DROP TABLE IF EXISTS armour_costs;
    CREATE TABLE armour_costs (name TEXT PRIMARY KEY, injury_mod INTEGER,
                               credits INTEGER, provenance TEXT DEFAULT 'points-engine');

    DROP TABLE IF EXISTS characteristics;
    CREATE TABLE characteristics (name TEXT PRIMARY KEY, credits INTEGER,
                                  provenance TEXT DEFAULT 'points-engine');

    DROP TABLE IF EXISTS skills;
    CREATE TABLE skills (name TEXT PRIMARY KEY, tier INTEGER, path TEXT,
                         stat TEXT, credits INTEGER, unlocks_at TEXT,
                         provenance TEXT DEFAULT 'points-engine');

    DROP TABLE IF EXISTS sim_runs;
    CREATE TABLE sim_runs (
      name TEXT, file TEXT PRIMARY KEY, question TEXT, script TEXT,
      created TEXT, n_per_cell INTEGER,
      engine TEXT, cost_table TEXT, harness TEXT,
      git_commit TEXT, git_branch TEXT, git_dirty INTEGER,
      stale INTEGER, stale_reason TEXT, caveats TEXT,
      provenance TEXT DEFAULT 'measured-monte-carlo'
    );

    DROP TABLE IF EXISTS sim_values;
    CREATE TABLE sim_values (
      id INTEGER PRIMARY KEY, run_name TEXT, run_file TEXT,
      path TEXT, leaf TEXT, value_num REAL, value_text TEXT,
      created TEXT, stale INTEGER
    );

    CREATE INDEX idx_sm_lookup ON shot_matrix(stat, cover, armour, damage, attack_dice);
    CREATE INDEX idx_ws_weapon ON weapon_shot(weapon, stat, cover, armour);
    CREATE INDEX idx_sv_run ON sim_values(run_name);
    CREATE INDEX idx_sv_leaf ON sim_values(leaf);
    """)


def fill_reference(cx: sqlite3.Connection) -> None:
    for rank in ("recruit", "fighter", "specialist", "leader"):
        cx.execute("INSERT INTO bodies(rank,credits,stat_points,orders) VALUES(?,?,?,?)",
                   (rank, U.body_cost(rank), U.RANK_STAT_POINTS[rank],
                    U.RANK_ORDERS[rank]))
    for name, mod in (("none", 0), ("light", -1), ("heavy", -2)):
        cx.execute("INSERT INTO armour_costs(name,injury_mod,credits) VALUES(?,?,?)",
                   (name, mod, U.armour_points(name)))
    for name, cr in T.CHAR_CREDITS.items():
        cx.execute("INSERT INTO characteristics(name,credits) VALUES(?,?)", (name, cr))
    for name, (tier, path, stat) in SK.SKILLS.items():
        cx.execute("INSERT OR REPLACE INTO skills"
                   "(name,tier,path,stat,credits,unlocks_at) VALUES(?,?,?,?,?,?)",
                   (name, tier, path, stat, SK.SKILL_TIER_CREDITS[tier],
                    f"{stat} +{tier * 2}"))


def fill_weapons(cx: sqlite3.Connection) -> list[WeaponBuild]:
    builds = [b for b, _ in SAMPLE_ARMOURY]
    for b in builds:
        meta = T.CLASS_META[b.weapon_class]
        lo, hi = meta["damage"]
        band = meta["range"]
        cx.execute(
            "INSERT OR REPLACE INTO weapons(name,class,damage,reach,characteristics,"
            "drawbacks,credits,min_rank,slots,manufactured,damage_band,range_band)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (b.name, b.weapon_class, b.picked_damage(), b.picked_reach(),
             ", ".join(b.characteristics), ", ".join(b.drawbacks),
             weapon_cost(b), meta.get("min_rank", "recruit"), meta["slots"],
             int(b.manufactured), f"+{lo}..+{hi}",
             "melee" if band is None else f'{band[0]}"-{band[1]}"'))
    return builds


def fill_shot_matrix(cx: sqlite3.Connection) -> int:
    rows = 0
    dmg_label = {0: "+0", 1: "light +1", 2: "medium +2", 3: "heavy +3",
                 4: "+4", 5: "+5 (cap)"}
    for stat in range(-1, 7):
        for cover, cmod in COVERS:
            for extra in range(-3, 4):
                for armour, amod in ARMOURS:
                    for damage in range(0, 6):
                        for dice in (1, 2, 3):
                            r = chain(stat, cmod, extra, damage, amod, dice)
                            cx.execute(
                                "INSERT INTO shot_matrix(stat,stat_label,cover,"
                                "cover_mod,extra_to_hit,to_hit_mod_raw,"
                                "to_hit_mod_applied,over_mod_cap,armour,armour_mod,"
                                "damage,damage_label,attack_dice,to_hit,"
                                "injure_given_hit,wound_per_die,stress_per_die,"
                                "p_wound_action,e_wounds_resolve_all,"
                                "e_wounds_stop_on_down,e_stress_resolve_all,"
                                "e_stress_stop_on_down,p_break_test,actions_to_down)"
                                " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                (stat, f"{stat:+d}", cover, cmod, extra,
                                 r["to_hit_mod_raw"], r["to_hit_mod_applied"],
                                 r["over_mod_cap"], armour, amod, damage,
                                 dmg_label[damage], dice, r["to_hit"],
                                 r["injure_given_hit"], r["wound_per_die"],
                                 r["stress_per_die"], r["p_wound_action"],
                                 r["e_wounds_resolve_all"], r["e_wounds_stop_on_down"],
                                 r["e_stress_resolve_all"], r["e_stress_stop_on_down"],
                                 r["p_break_test"], r["actions_to_down"]))
                            rows += 1
    return rows


def fill_weapon_shot(cx: sqlite3.Connection, builds: list[WeaponBuild]) -> int:
    rows = 0
    for b in builds:
        meta = T.CLASS_META[b.weapon_class]
        rank = meta.get("min_rank", "recruit")
        body = U.body_cost(rank)
        wcr = weapon_cost(b)
        fielded = body + wcr
        for stat in range(-1, 7):
            for cover, cmod in COVERS:
                for armour, amod in ARMOURS:
                    for dice in (1, 2, 3):
                        r = chain(stat, cmod, 0, b.picked_damage(), amod, dice)
                        per100 = (r["e_wounds_stop_on_down"] / fielded * 100
                                  if fielded else None)
                        cx.execute(
                            "INSERT INTO weapon_shot(weapon,class,damage,"
                            "weapon_credits,stat,cover,armour,attack_dice,to_hit,"
                            "injure_given_hit,p_wound_action,e_wounds_stop_on_down,"
                            "e_stress_stop_on_down,actions_to_down,carrier_rank,"
                            "fielded_credits,wounds_per_action_per_100cr)"
                            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (b.name, b.weapon_class, b.picked_damage(), wcr, stat,
                             cover, armour, dice, r["to_hit"], r["injure_given_hit"],
                             r["p_wound_action"], r["e_wounds_stop_on_down"],
                             r["e_stress_stop_on_down"], r["actions_to_down"],
                             rank, fielded, round(per100, 4) if per100 else None))
                        rows += 1
    return rows


def _flatten(obj, prefix=""):
    """Walk an envelope's nested values into (path, leaf, value) triples."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _flatten(v, f"{prefix}.{k}" if prefix else str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            label = None
            if isinstance(v, dict):
                for key in ("variant", "package", "name", "atom", "label", "cell",
                            "band", "purchase", "cover", "rule"):
                    if key in v:
                        label = str(v[key])
                        break
            yield from _flatten(v, f"{prefix}[{label or i}]")
    else:
        leaf = prefix.split(".")[-1] if prefix else ""
        yield prefix, leaf, obj


def fill_sim_runs(cx: sqlite3.Connection) -> tuple[int, int]:
    """Ingest every stamped envelope, flagging any whose fingerprints have moved."""
    now_engine = P.engine_fingerprint()["combined"]
    now_cost = P.cost_table_fingerprint()["combined"]
    now_harness = P.harness_fingerprint()["combined"]

    runs = vals = 0
    for f in sorted(RESULTS.glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  ! unreadable, skipped: {f.name} ({e})")
            continue
        if not isinstance(d, dict):
            continue

        eng = (d.get("engine") or {}).get("combined")
        cost = (d.get("cost_table") or {}).get("combined")
        harn = (d.get("harness") or {}).get("combined")
        git = d.get("git") or {}

        reasons = []
        if eng and eng != now_engine:
            reasons.append("engine moved")
        if cost and cost != now_cost:
            reasons.append("cost table moved")
        if harn and harn != now_harness:
            reasons.append("harness moved")
        if "SUPERSEDED" in f.name or "CONTAMINATED" in f.name:
            reasons.append(f"filename flag: {f.name.split('.')[-2]}")
        stale = int(bool(reasons))

        name = d.get("name") or f.stem
        params = d.get("params") or {}
        cx.execute(
            "INSERT OR REPLACE INTO sim_runs(name,file,question,script,created,"
            "n_per_cell,engine,cost_table,harness,git_commit,git_branch,git_dirty,"
            "stale,stale_reason,caveats) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (name, f.name, d.get("question", ""),
             (d.get("script") or {}).get("name", ""), d.get("created", ""),
             params.get("N_per_cell") or params.get("n") or None,
             eng, cost, harn, git.get("commit"), git.get("branch"),
             int(bool(git.get("dirty"))), stale, "; ".join(reasons),
             json.dumps(d.get("caveats", []))))
        runs += 1

        # Flatten every section that is NOT provenance bookkeeping.
        #
        # This was a whitelist of known section names, and that was wrong in the
        # project's own characteristic way: a new harness with new section names
        # was ingested as a run with ZERO values and looked identical to a run
        # that genuinely measured nothing. Silent under-ingestion, no error. So
        # the rule is inverted - name the metadata, take everything else.
        META_KEYS = {"name", "question", "params", "caveats", "engine",
                     "cost_table", "harness", "script", "git", "created",
                     "python", "schema"}
        for section in d:
            if section in META_KEYS or not isinstance(d[section], (dict, list)):
                continue
            for path, leaf, v in _flatten(d[section], section):
                num = v if isinstance(v, (int, float)) and not isinstance(v, bool) else None
                txt = None if num is not None else (
                    json.dumps(v) if isinstance(v, (list, dict)) else str(v))
                cx.execute(
                    "INSERT INTO sim_values(run_name,run_file,path,leaf,value_num,"
                    "value_text,created,stale) VALUES(?,?,?,?,?,?,?,?)",
                    (name, f.name, path, leaf, num, txt, d.get("created", ""), stale))
                vals += 1
    return runs, vals


def build_fts(cx: sqlite3.Connection) -> None:
    """One search box over every measured finding and every weapon."""
    cx.executescript("""
    DROP TABLE IF EXISTS search;
    CREATE VIRTUAL TABLE search USING fts5(kind, name, detail, value, source);
    """)
    cx.execute("""
      INSERT INTO search(kind,name,detail,value,source)
      SELECT 'finding', run_name, path, COALESCE(CAST(value_num AS TEXT), value_text),
             run_file FROM sim_values
    """)
    cx.execute("""
      INSERT INTO search(kind,name,detail,value,source)
      SELECT 'weapon', name, class || ' | ' || characteristics || ' | ' || drawbacks,
             CAST(credits AS TEXT) || ' Cr', 'points-engine' FROM weapons
    """)
    cx.execute("""
      INSERT INTO search(kind,name,detail,value,source)
      SELECT 'skill', name, path || ' | T' || tier || ' | ' || stat,
             CAST(credits AS TEXT) || ' Cr', 'points-engine' FROM skills
    """)
    cx.execute("""
      INSERT INTO search(kind,name,detail,value,source)
      SELECT 'run', name, question, created, file FROM sim_runs
    """)


def drop_everything(cx: sqlite3.Connection) -> None:
    """Clear the file IN PLACE rather than deleting and recreating it.

    Deleting was the obvious implementation and it is wrong here. Two long-lived
    readers hold this file open for their whole lifetime - a Datasette server,
    and the `settlements-sims` MCP connector that Claude Code spawns at session
    start. On Windows an open handle makes unlink fail outright, so a rebuild
    would work exactly until the connector that makes the database useful was
    registered, and never again after.

    Dropping objects through a connection is what SQLite is for. Everything is
    enumerated from sqlite_master rather than named, so a table removed from
    this script in future does not linger in the file as a stale relic.

    ORDER IS LOAD-BEARING. An FTS5 table owns shadow tables (search_data,
    search_idx, ...) which appear in sqlite_master as ordinary tables. Drop a
    shadow first and the virtual table can no longer be dropped at all - its
    constructor fails on the next open with "vtable constructor failed", and the
    file is left in a state no amount of re-running fixes. So virtual tables go
    first, taking their shadows with them, and only then is the schema re-read.
    """
    def sweep():
        for kind in ("trigger", "view", "index", "table"):
            for (name,) in cx.execute(
                "SELECT name FROM sqlite_master WHERE type=? "
                "AND name NOT LIKE 'sqlite_%'", (kind,)).fetchall():
                try:
                    cx.execute(f'DROP {kind.upper()} IF EXISTS "{name}"')
                except sqlite3.OperationalError:
                    pass      # already gone with its parent

    # 1. virtual tables first - each takes its own shadow tables with it
    for (name,) in cx.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "AND sql LIKE '%VIRTUAL TABLE%'").fetchall():
        try:
            cx.execute(f'DROP TABLE IF EXISTS "{name}"')
        except sqlite3.OperationalError:
            # A previous half-drop can leave an unconstructible vtable. Remove
            # its schema row directly, then bin the orphaned shadows by name.
            cx.execute("PRAGMA writable_schema = ON")
            cx.execute("DELETE FROM sqlite_master WHERE name = ?", (name,))
            cx.execute("PRAGMA writable_schema = OFF")
            cx.commit()
            for (shadow,) in cx.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE ?",
                (f"{name}\\_%", )).fetchall():
                cx.execute(f'DROP TABLE IF EXISTS "{shadow}"')
    cx.commit()

    # 2. everything that remains
    sweep()
    cx.commit()


def main() -> int:
    # Drop on one connection, then REOPEN before building. A connection that has
    # dropped a virtual table (or touched sqlite_master directly) keeps a stale
    # schema cache, and re-creating a vtable of the same name on it fails with
    # "vtable constructor failed" against a file that is perfectly healthy - the
    # error names the table, so it reads like corruption rather than caching.
    cx = sqlite3.connect(DB)
    drop_everything(cx)
    cx.close()

    cx = sqlite3.connect(DB)
    print(f"building {DB.name}")
    build_schema(cx)

    fill_reference(cx)
    print("  reference   bodies / armour / characteristics / skills")

    builds = fill_weapons(cx)
    print(f"  weapons     {len(builds)} catalogue entries, priced live")

    n = fill_shot_matrix(cx)
    print(f"  shot_matrix {n:,} exact rows "
          "(stat x cover x extra-mod x armour x damage x attack dice)")

    n = fill_weapon_shot(cx, builds)
    print(f"  weapon_shot {n:,} exact rows (catalogue weapon x stat x cover x armour)")

    runs, vals = fill_sim_runs(cx)
    print(f"  sim_runs    {runs} stamped envelopes -> {vals:,} searchable values")

    build_fts(cx)
    cx.commit()

    stale = cx.execute("SELECT COUNT(*) FROM sim_runs WHERE stale=1").fetchone()[0]
    print(f"\n  {stale} of {runs} stored runs are STALE against today's fingerprints.")
    print("  (expected and healthy - the harness prefers false-stale to false-fresh)")
    try:
        cx.execute("VACUUM")     # reclaims the dropped tables' pages
    except sqlite3.OperationalError as e:
        print(f"  (VACUUM skipped: {e} - file is larger than it needs to be, "
              "not incorrect)")
    cx.close()
    print(f"\ndone: {DB}  ({DB.stat().st_size/1024/1024:.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

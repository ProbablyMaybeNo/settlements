"""Provenance: bind every measurement to the code and prices that produced it.

WHY THIS EXISTS
---------------
`docs/PACKET-TEST-RESULTS.md` was written to be re-derivable, and its
`results/README.md` says so in as many words: "committed so every number in that
document can be re-derived rather than trusted." 84 of its 85 raw output lines
reproduce byte-for-byte two rules-generations later. One does not — the
`extra activation` row records -2.63 where both the branch engine and today's
merged engine produce +1.95, because the .txt was generated before the
implementation beside it was fixed, and the two were committed together.

Persisting raw output was necessary and was not sufficient. Nothing tied the
numbers to the code version that made them, so a stale artefact sat next to the
code that superseded it and looked exactly like a good one.

So every result this harness emits carries three fingerprints:

  engine      SHA-256 over the 2.5D engine's source text. Behaviour IS the text;
              a comment change is a behaviour change as far as reproduction goes,
              and false staleness is cheap while false freshness is not.
  cost_table  SHA-256 over the RESOLVED VALUES in points/ticks.py, not its text.
              Reworded provenance comments must not invalidate a measurement;
              a moved number must. That is the whole distinction, so the two
              fingerprints are deliberately computed different ways.
  git         commit, branch, and whether the tree was dirty when it ran.

`staleness()` then answers the question nobody could previously ask without
remembering to: which stored results were taken against something that has
since moved?
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path


try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO / "test-bench" / "engine2d"
HARNESS_DIR = Path(__file__).resolve().parent
TICKS = REPO / "test-bench" / "points" / "ticks.py"
RESULTS = REPO / "test-bench" / "balance" / "results"

# Engine files whose text can change what a game does. viz.py and run.py are CLI
# and rendering; they are excluded so a plotting tweak does not invalidate every
# stored measurement. If a file here is ever imported by engine.py, add it.
ENGINE_SOURCES = ("engine.py", "board.py", "policies.py", "data.py", "crews.py")

# Harness files that decide what a number MEANS, as opposed to what the game does.
#
# WHY THIS SET EXISTS AT ALL. The objective-only pricing cut (2026-08-12) voided
# the anchor, the stat ladder, the weapon classes and value(Pinned) - and
# staleness() went on reporting every one of them CURRENT, because the engine and
# the cost table had not moved. The policy that voided them lived HERE. So the
# module written to catch stale artefacts could not catch itself, which is the
# same false-freshness failure one layer up.
#
#   measure.py   PRICING_SCENARIOS, the estimator, the degeneracy and saturation
#                guards, price_atom's sign-split detector.
#   effects.py   the divisor. n_applied vs models-present is a ~20% swing on the
#                project's own standard lists.
#   anchor.py    VALUE. Every Credits figure is win-points x 15/VALUE.
#
# TEXT-hashed, not value-hashed, deliberately - the opposite choice from the cost
# table above. ticks.py is mostly provenance commentary, so rewording it must not
# invalidate a measurement. These are mostly LOGIC, and an estimator can change
# completely while its constants stay put. False-stale is noise here;
# false-fresh is what this whole module exists to prevent.
#
# 2026-08-13: THE MEASUREMENT SCRIPTS WERE ADDED, and the reason is worth keeping.
# The set was previously the three shared modules only. A density run executed
# against a BROKEN board ladder wrote an artefact whose engine and harness
# fingerprints were IDENTICAL to the fixed code, so staleness() reported it
# CURRENT and it was indistinguishable from a good result. The board ladder, the
# roster choice, the atom list and the scenario selection all live in the
# individual measure_*.py scripts, and every one of them changes what a number
# MEANS. None was covered by anything.
#
# That was the THIRD appearance of the same false-freshness class at a new layer:
# first the engine, then the pricing policy in measure.py, now the scripts. What
# happened to catch it was supersession-by-name grouping landing in the same
# batch - luck, not a control. Had the broken run been the newest, nothing would
# have flagged it.
#
# ACCEPTED CONSEQUENCE: editing ANY measurement script now marks EVERY stored
# result stale, including results from unrelated scripts. That is deliberate and
# consistent with the standing trade - false-stale is noise, false-fresh is
# dangerous - and `script` below exists so a reader can tell the two apart.
_MEASUREMENT_SCRIPTS = tuple(sorted(
    p.name for p in Path(__file__).resolve().parent.glob("*.py")
    if p.name.startswith(("measure_", "verify_", "diag_"))
))
# provenance.py is deliberately NOT in this set. It decides how a result is
# STAMPED, not what the number MEANS, so a bookkeeping edit here should not
# invalidate every measurement in the project. rosters.py IS in it - crew
# definitions change what was measured.
HARNESS_SOURCES = ("measure.py", "effects.py", "anchor.py",
                   "rosters.py") + _MEASUREMENT_SCRIPTS


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def engine_fingerprint() -> dict:
    """Hash the engine's source text, per file and combined."""
    per_file = {}
    for name in ENGINE_SOURCES:
        p = ENGINE_DIR / name
        per_file[name] = _sha(p.read_text(encoding="utf-8")) if p.exists() else None
    combined = _sha(json.dumps(per_file, sort_keys=True))
    return {"combined": combined[:16], "files": {k: (v[:16] if v else None)
                                                 for k, v in per_file.items()}}


def harness_fingerprint() -> dict:
    """Hash the harness logic that decides what a measurement MEANS."""
    per_file = {}
    for name in HARNESS_SOURCES:
        p = HARNESS_DIR / name
        per_file[name] = _sha(p.read_text(encoding="utf-8")) if p.exists() else None
    combined = _sha(json.dumps(per_file, sort_keys=True))
    return {"combined": combined[:16], "files": {k: (v[:16] if v else None)
                                                 for k, v in per_file.items()}}


def producing_script() -> dict:
    """The specific script that produced this result, and its own hash.

    HARNESS_SOURCES is deliberately broad, so editing any measurement script
    marks every result stale. That is the safe direction, but it makes staleness
    noisy: a reader cannot tell "the script that made this number changed" from
    "some unrelated script changed". This records the producing script by name
    and hash so the two are distinguishable after the fact.
    """
    main = sys.modules.get("__main__")
    path = getattr(main, "__file__", None)
    if not path:
        return {"name": None, "sha": None}
    p = Path(path).resolve()
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return {"name": p.name, "sha": None}
    return {"name": p.name, "sha": _sha(text)[:16]}


def _canonical(obj):
    """Deterministic, JSON-safe form. Sets and frozensets are order-independent,
    so they sort; tuples become lists because JSON has no tuple."""
    if isinstance(obj, dict):
        return {str(k): _canonical(v) for k, v in sorted(obj.items(), key=lambda kv: str(kv[0]))}
    if isinstance(obj, (set, frozenset)):
        return sorted(_canonical(v) for v in obj)
    if isinstance(obj, (list, tuple)):
        return [_canonical(v) for v in obj]
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    return repr(obj)


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cost_table_values() -> dict:
    """Every public constant in points/ticks.py, resolved to values.

    Deliberately value-based, not text-based: ticks.py is mostly provenance
    commentary, and rewording an explanation must not mark a measurement stale.
    """
    mod = _load_module(TICKS, "_ticks_fingerprint")
    out = {}
    for key in dir(mod):
        if key.startswith("_") or not key[0].isupper():
            continue
        val = getattr(mod, key)
        if callable(val) or isinstance(val, type):
            continue
        out[key] = _canonical(val)
    return out


def cost_table_fingerprint() -> dict:
    vals = cost_table_values()
    return {"combined": _sha(json.dumps(vals, sort_keys=True))[:16],
            "n_constants": len(vals)}


def git_state() -> dict:
    def run(*args):
        try:
            return subprocess.run(("git",) + args, cwd=REPO, capture_output=True,
                                  text=True, timeout=30).stdout.strip()
        except Exception:
            return ""
    dirty = run("status", "--porcelain")
    paths = [l[3:].strip().strip('"') for l in dirty.splitlines()]
    # "dirty" alone is too blunt to act on: uncommitted notes elsewhere in the
    # repo say nothing about whether THIS result is attributable. What matters is
    # whether anything feeding the two fingerprints was uncommitted at run time.
    # harness/ is included because it now PRODUCES results, not just wraps them:
    # measure.py's estimator and effects.py's divisor both change what a number
    # means, so an uncommitted harness makes a result as unattributable as an
    # uncommitted engine does.
    watched = ("test-bench/engine2d/", "test-bench/points/", "test-bench/balance/",
               "test-bench/harness/")
    relevant = [p for p in paths if any(p.startswith(w) for w in watched)
                and not p.startswith("test-bench/balance/results/")]
    return {
        "commit": run("rev-parse", "HEAD")[:12],
        "branch": run("rev-parse", "--abbrev-ref", "HEAD"),
        "dirty": bool(dirty),
        "dirty_relevant": relevant,
        "dirty_paths": paths[:20],
    }


@dataclass
class Envelope:
    """One measurement, plus everything needed to know whether to still believe it.

    `values` is raw win-points per model. There is no Credits figure anywhere in
    this class, on purpose: the Credits-per-win-point constant is a scale CHOICE
    that the rebuild is re-making, and a harness that stores Credits has silently
    pre-decided it. Convert downstream, where the choice is visible.
    """
    name: str
    question: str
    values: dict = field(default_factory=dict)
    raw_cells: list = field(default_factory=list)
    params: dict = field(default_factory=dict)
    caveats: list = field(default_factory=list)
    engine: dict = field(default_factory=engine_fingerprint)
    cost_table: dict = field(default_factory=cost_table_fingerprint)
    harness: dict = field(default_factory=harness_fingerprint)
    script: dict = field(default_factory=producing_script)
    git: dict = field(default_factory=git_state)
    created: str = field(default_factory=lambda: datetime.now().strftime("%Y%m%d-%H%M%S"))
    python: str = field(default_factory=lambda: f"{platform.python_version()}")
    schema: int = 2

    def write(self, stdout_text: str | None = None) -> Path:
        """Write to a filename that CANNOT collide with a prior artefact.

        WHY THE NAME CARRIES ALL OF THIS. The old stem was `name-engine8`, which
        is content-independent: re-running a script with the SAME name, N and
        engine silently overwrote the previous result. That is not a theoretical
        risk - it destroyed the sign-split artefact on 2026-08-12, and only a
        commit 26 minutes earlier made it recoverable. `git show` is not a
        durability guarantee for an uncommitted run.

        This is the second artefact-naming defect in two milestones, and both had
        the same root: the filename carried no uniqueness guarantee. So the fix is
        the class, not the instance - the timestamp makes collision impossible
        even for a byte-identical re-run, and the exists() check below refuses
        rather than clobbers if it somehow happens anyway. No CI check can catch a
        silent overwrite after the fact, because the evidence is what got deleted.
        """
        RESULTS.mkdir(parents=True, exist_ok=True)
        stem = (f"{self.name}"
                f"-e{self.engine['combined'][:8]}"
                f"-h{self.harness['combined'][:8]}"
                f"-{self.created}")
        out = RESULTS / f"{stem}.json"
        if out.exists():
            raise FileExistsError(
                f"refusing to overwrite an existing result: {out.name}. "
                "Filenames are timestamped, so this means two runs finished in "
                "the same second - re-run rather than losing the earlier one."
            )
        out.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")
        if stdout_text is not None:
            (RESULTS / f"{stem}.txt").write_text(stdout_text, encoding="utf-8")
        return out


def staleness(verbose: bool = True) -> list[dict]:
    """Which stored results were taken against something that has since moved?

    This is the check that did not exist when the extra-activation row went stale.
    It compares three fingerprints. `harness` was added after the objective-only
    pricing cut voided four measurements while this function reported all four
    CURRENT - the engine and cost table had not moved, and the policy that voided
    them was not covered by anything.

    It also answers the question timestamped filenames create: with collision made
    impossible, a name now has MANY artefacts and only one is live. Superseded
    ones are labelled rather than left for a reader to date by eye - the milestone-1
    finding was precisely that a result is only findable under the question it
    appears to answer, and "which of these six is current" is the same defect.
    """
    eng_now = engine_fingerprint()["combined"]
    cost_now = cost_table_fingerprint()["combined"]
    harness_now = harness_fingerprint()["combined"]
    rows = []
    for p in sorted(RESULTS.glob("*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            rows.append({"file": p.name, "status": "UNREADABLE", "detail": str(e)})
            continue
        if d.get("schema") is None:
            rows.append({"file": p.name, "status": "UNSTAMPED",
                         "detail": "predates the provenance envelope"})
            continue
        moved = []
        if d.get("engine", {}).get("combined") != eng_now:
            moved.append("engine")
        # COST TABLE IS DOWNSTREAM, AND IT IS THE ONLY ONE THAT IS.
        #
        # Nothing in a measurement reads points/ticks.py. The engine costs crews
        # from engine2d/data.py; the harness measures WIN-POINTS and never touches
        # Credits. ticks.py is where a measurement's answer eventually gets
        # WRITTEN, not an input to taking it.
        #
        # So writing measured prices back into ticks.py - the entire point of the
        # exercise - marks every artefact that produced them stale, and re-running
        # reproduces them exactly, because the changed file was never read. Found
        # the moment the first real write-back landed (2026-08-13): eight current
        # artefacts went stale at once and not one of their numbers could move.
        #
        # A guard that fires when nothing is wrong is worse than no guard - it
        # trains you to ignore it - so this is reported SEPARATELY rather than
        # folded into `moved`. It still appears, because "which price table was
        # live when this was taken" is real provenance and worth knowing. It just
        # is not a reason to distrust the number.
        cost_moved = d.get("cost_table", {}).get("combined") != cost_now
        # A pre-schema-2 result has no harness fingerprint at all. That is not
        # "unchanged", it is unknown - and unknown must read as stale, because the
        # objective-only cut is exactly the change these files cannot describe.
        if d.get("harness", {}).get("combined") != harness_now:
            moved.append("harness" if d.get("harness") else "harness(unstamped)")
        # Did the script that ACTUALLY PRODUCED this result change, as opposed to
        # some unrelated script sharing the broad harness fingerprint? That
        # distinction is the difference between "re-run this" and "ignore".
        sc = d.get("script") or {}
        own_moved = False
        if sc.get("name") and sc.get("sha"):
            here = HARNESS_DIR / sc["name"]
            if here.exists():
                own_moved = _sha(here.read_text(encoding="utf-8"))[:16] != sc["sha"]
        rows.append({
            "file": p.name,
            "name": d.get("name", p.stem),
            "created": d.get("created", ""),
            "script": sc.get("name"),
            "own_script_moved": own_moved,
            "status": "STALE" if moved else "CURRENT",
            "detail": ", ".join(moved) if moved else "",
            # Downstream-only: recorded, never a reason to distrust the number.
            "cost_table_moved": cost_moved,
            "was_dirty": bool(d.get("git", {}).get("dirty_relevant", [])),
        })

    # Supersession is per measurement NAME, newest wins. Sorting by `created`
    # falls back to filename for pre-schema-2 files, which embedded no timestamp -
    # so those sort by engine hash and their relative order is not meaningful.
    # Flagged rather than guessed at.
    by_name: dict[str, list] = {}
    for r in rows:
        if "name" in r:
            by_name.setdefault(r["name"], []).append(r)
    for name, group in by_name.items():
        group.sort(key=lambda r: (r.get("created") or "", r["file"]))
        for r in group[:-1]:
            r["superseded_by"] = group[-1]["file"]
        group[-1]["latest_of_name"] = True

    if verbose:
        _print_staleness(rows, eng_now, cost_now, harness_now)
    return rows


def latest(name: str) -> Path | None:
    """The live artefact for a measurement name. Use this instead of globbing.

    Timestamped filenames mean a name maps to many files; reading 'the' result by
    hand-picking a filename is how a superseded number gets quoted as current.
    """
    rows = [r for r in staleness(verbose=False)
            if r.get("name") == name and r.get("latest_of_name")]
    return RESULTS / rows[0]["file"] if rows else None


def _print_staleness(rows, eng_now, cost_now, harness_now) -> None:
    print(f"engine     {eng_now}")
    print(f"cost_table {cost_now}")
    print(f"harness    {harness_now}")
    unstamped = [p.name for p in sorted(RESULTS.glob("*.txt"))
                 if not (RESULTS / f"{p.stem}.json").exists()]
    print()
    if not rows:
        print("no stamped results yet")
    for r in rows:
        mark = {"CURRENT": "  ok  ", "STALE": " STALE", "UNSTAMPED": " UNSTMP",
                "UNREADABLE": " ERROR"}.get(r["status"], "  ?   ")
        live = "" if r.get("superseded_by") else ("  <- LIVE" if r.get("latest_of_name") else "")
        print(f"{mark}  {r['file']:<64} {r['detail']}{live}")
        if r.get("own_script_moved"):
            print(f"          {'':<64} ** its OWN script ({r['script']}) changed — re-run **")
        if r.get("cost_table_moved"):
            print(f"          {'':<64} price table has moved since (DOWNSTREAM — "
                  f"no measurement reads it; not a reason to re-run)")
        if r.get("superseded_by"):
            print(f"          {'':<64} superseded by {r['superseded_by']}")
        if r.get("was_dirty"):
            print(f"          {'':<64} (uncommitted engine/points changes at run time)")
    if unstamped:
        print()
        print("UNSTAMPED raw outputs — no envelope, so staleness cannot be checked:")
        for n in unstamped:
            print(f"    {n}")
        print("  These predate this harness. packet_battle-n2000.txt is known to")
        print("  contain one superseded row (extra activation) and is kept as-is,")
        print("  deliberately, as the worked example of why this module exists.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "values":
        print(json.dumps(cost_table_values(), indent=2))
    else:
        staleness()

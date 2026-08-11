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
from pathlib import Path


try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO / "test-bench" / "engine2d"
TICKS = REPO / "test-bench" / "points" / "ticks.py"
RESULTS = REPO / "test-bench" / "balance" / "results"

# Engine files whose text can change what a game does. viz.py and run.py are CLI
# and rendering; they are excluded so a plotting tweak does not invalidate every
# stored measurement. If a file here is ever imported by engine.py, add it.
ENGINE_SOURCES = ("engine.py", "board.py", "policies.py", "data.py", "crews.py")


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
    git: dict = field(default_factory=git_state)
    python: str = field(default_factory=lambda: f"{platform.python_version()}")
    schema: int = 1

    def write(self, stdout_text: str | None = None) -> Path:
        RESULTS.mkdir(parents=True, exist_ok=True)
        stem = f"{self.name}-{self.engine['combined'][:8]}"
        out = RESULTS / f"{stem}.json"
        out.write_text(json.dumps(asdict(self), indent=2), encoding="utf-8")
        if stdout_text is not None:
            (RESULTS / f"{stem}.txt").write_text(stdout_text, encoding="utf-8")
        return out


def staleness(verbose: bool = True) -> list[dict]:
    """Which stored results were taken against an engine or cost table that moved?

    This is the check that did not exist when the extra-activation row went stale.
    """
    eng_now = engine_fingerprint()["combined"]
    cost_now = cost_table_fingerprint()["combined"]
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
        if d.get("cost_table", {}).get("combined") != cost_now:
            moved.append("cost_table")
        rows.append({
            "file": p.name,
            "status": "STALE" if moved else "CURRENT",
            "detail": ", ".join(moved) if moved else "",
            "was_dirty": bool(d.get("git", {}).get("dirty_relevant", [])),
        })
    if verbose:
        _print_staleness(rows, eng_now, cost_now)
    return rows


def _print_staleness(rows, eng_now, cost_now) -> None:
    print(f"engine     {eng_now}")
    print(f"cost_table {cost_now}")
    unstamped = [p.name for p in sorted(RESULTS.glob("*.txt"))
                 if not (RESULTS / f"{p.stem}.json").exists()]
    print()
    if not rows:
        print("no stamped results yet")
    for r in rows:
        mark = {"CURRENT": "  ok  ", "STALE": " STALE", "UNSTAMPED": " UNSTMP",
                "UNREADABLE": " ERROR"}.get(r["status"], "  ?   ")
        print(f"{mark}  {r['file']:<52} {r['detail']}")
        if r.get("was_dirty"):
            print(f"          {'':<52} (uncommitted engine/points changes at run time)")
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

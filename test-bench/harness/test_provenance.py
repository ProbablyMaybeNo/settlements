"""The two fingerprints must have DIFFERENT semantics. Prove it, don't claim it.

  cost_table  is value-based: rewording a provenance comment must NOT invalidate
              a stored measurement, but moving a number must.
  engine      is text-based: behaviour is the text, and false staleness is cheap
              while false freshness is what let a superseded row sit in
              results/ looking exactly like a good one.

Run: py -3.13 -m pytest test_provenance.py -q   (from test-bench/harness/)
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

import provenance as P


def _fingerprint_ticks_at(path: Path) -> str:
    original = P.TICKS
    try:
        P.TICKS = path
        return P.cost_table_fingerprint()["combined"]
    finally:
        P.TICKS = original


def test_cost_fingerprint_ignores_comment_edits():
    src = P.TICKS.read_text(encoding="utf-8")
    base = _fingerprint_ticks_at(P.TICKS)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "ticks.py"
        edited = src.replace(
            '"""Atomic tick table — 1000-Credit scale. Players never see these atoms."""',
            '"""Atomic tick table. REWORDED PROVENANCE COMMENTARY, no value moved."""',
        )
        assert edited != src, "the docstring anchor moved; update this test"
        edited += "\n# a trailing explanatory comment added during a doc pass\n"
        p.write_text(edited, encoding="utf-8")
        assert _fingerprint_ticks_at(p) == base


def test_cost_fingerprint_catches_a_moved_number():
    src = P.TICKS.read_text(encoding="utf-8")
    base = _fingerprint_ticks_at(P.TICKS)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "ticks.py"
        edited = src.replace("TICK_STAT = 15", "TICK_STAT = 25")
        assert edited != src, "TICK_STAT anchor moved; update this test"
        p.write_text(edited, encoding="utf-8")
        assert _fingerprint_ticks_at(p) != base


def test_cost_fingerprint_catches_a_nested_dict_value():
    src = P.TICKS.read_text(encoding="utf-8")
    base = _fingerprint_ticks_at(P.TICKS)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "ticks.py"
        edited = src.replace('"bleeding": 46,', '"bleeding": 47,')
        assert edited != src, "bleeding anchor moved; update this test"
        p.write_text(edited, encoding="utf-8")
        assert _fingerprint_ticks_at(p) != base


def test_engine_fingerprint_is_text_based():
    """A comment-only edit to the engine SHOULD invalidate. Opposite of ticks.py,
    and that asymmetry is the point."""
    original = P.ENGINE_DIR
    base = P.engine_fingerprint()["combined"]
    with tempfile.TemporaryDirectory() as td:
        dst = Path(td) / "engine2d"
        dst.mkdir()
        for name in P.ENGINE_SOURCES:
            shutil.copy(original / name, dst / name)
        (dst / "engine.py").write_text(
            (dst / "engine.py").read_text(encoding="utf-8") + "\n# harmless comment\n",
            encoding="utf-8",
        )
        try:
            P.ENGINE_DIR = dst
            assert P.engine_fingerprint()["combined"] != base
        finally:
            P.ENGINE_DIR = original


def test_envelope_stores_no_credits():
    """A Credits figure in a stored result would silently pre-decide the scale
    constant the rebuild exists to re-choose."""
    env = P.Envelope(name="x", question="q", values={"wp_per_model": 1.95})
    blob = str(P.asdict(env)).lower()
    for banned in ("credit", "cr_per", "price"):
        assert banned not in blob

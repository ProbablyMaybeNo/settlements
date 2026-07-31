"""Verify armoury math and print v0 catalogue residuals."""

from __future__ import annotations

import json
from pathlib import Path

from .catalogue import (
    DESIGN_EXAMPLES,
    KEY_STRUCTURES,
    SAMPLE_ARMOURY,
    STARTER_STRUCTURES,
)
from .structures import groundworks_cost, materials_breakdown, materials_cost
from .ticks import SCALE
from .units import Rank, body_cost, listed_body_cost
from .weapons import weapon_cost, weapon_cost_breakdown


def verify_armoury() -> list[str]:
    """Hard failures only: a build that cannot be costed at all.

    Divergence from the legacy ×10 price is NOT a failure — Milestone 1 repriced
    the atoms from measurement, so the legacy column is a superseded baseline.
    It is reported by legacy_drift() instead.
    """
    failures: list[str] = []
    for build, _expected in SAMPLE_ARMOURY:
        try:
            weapon_cost(build)
        except ValueError as e:
            failures.append(str(e))
    return failures


def legacy_drift() -> list[dict]:
    """Per-weapon before/after against the legacy ×10 baseline."""
    rows = []
    for build, expected in SAMPLE_ARMOURY:
        try:
            got = weapon_cost(build)
        except ValueError:
            continue
        rows.append(
            {
                "name": build.name,
                "legacy": expected,
                "derived": got,
                "delta": got - expected,
            }
        )
    return rows


def verify_structural() -> list[str]:
    """Invariants the costing system claims about itself, checked not asserted."""
    from .ticks import (
        CHAR_GOODS,
        CLASS_GOODS,
        CLASS_META,
        CLASS_RANGE_BAND,
        DRAWBACK_GOODS,
        RANGE_BAND,
        SHORT_RANGE_REFUND,
    )

    errs: list[str] = []

    # The 24" threshold, derived twice independently (POINTS-TABLE §4).
    lhs = CLASS_GOODS["heavy_ranged"]
    rhs = (
        CLASS_GOODS["standard_ranged"]
        + CHAR_GOODS["long_range"]
        + DRAWBACK_GOODS["cumbersome"]
    )
    if lhs != rhs:
        errs.append(
            f"24\" threshold broken: heavy_ranged {lhs} != standard "
            f"{CLASS_GOODS['standard_ranged']} + long_range "
            f"{CHAR_GOODS['long_range']} + cumbersome "
            f"{DRAWBACK_GOODS['cumbersome']} = {rhs}"
        )

    # Every class must sit in a range band, and the band must match CLASS_META.
    for cls, meta in CLASS_META.items():
        band = CLASS_RANGE_BAND.get(cls)
        if band is None:
            errs.append(f"class {cls} has no range band")
        elif RANGE_BAND[band] != meta["range"]:
            errs.append(
                f"class {cls}: band {band} is {RANGE_BAND[band]}\" but "
                f"CLASS_META says {meta['range']}\""
            )

    # A refund must refund, and must never exceed the class it refunds against.
    for cls, refund in SHORT_RANGE_REFUND.items():
        if refund >= 0:
            errs.append(f"short_range refund for {cls} is not negative: {refund}")
        if -refund > CLASS_GOODS[cls]:
            errs.append(
                f"short_range on {cls} refunds {-refund} > class cost "
                f"{CLASS_GOODS[cls]}"
            )

    # The refund must be monotonic in what is actually lost: a longer-ranged
    # class must never get back less than a shorter-ranged one.
    ordered = sorted(SHORT_RANGE_REFUND, key=lambda c: RANGE_BAND[CLASS_RANGE_BAND[c]])
    for a, b in zip(ordered, ordered[1:]):
        if SHORT_RANGE_REFUND[b] > SHORT_RANGE_REFUND[a]:
            errs.append(
                f"short_range refund not monotonic: {b} "
                f"({SHORT_RANGE_REFUND[b]}) refunds less than {a} "
                f"({SHORT_RANGE_REFUND[a]}) despite longer range"
            )

    # No catalogue weapon may cost less than nothing.
    for build, _ in SAMPLE_ARMOURY:
        try:
            c = weapon_cost(build)
        except ValueError:
            continue
        if c < 0:
            errs.append(f"{build.name}: negative cost {c}")
    return errs


def rank_table() -> list[dict]:
    rows = []
    for rank in Rank:
        rows.append(
            {
                "rank": rank.value,
                "derived": body_cost(rank),
                "listed": listed_body_cost(rank),
                "delta": listed_body_cost(rank) - body_cost(rank),
            }
        )
    return rows


def structure_table() -> list[dict]:
    rows = []
    for spec in STARTER_STRUCTURES + KEY_STRUCTURES:
        rows.append(materials_breakdown(spec))
    return rows


def export_catalogue(path: Path) -> dict:
    payload = {
        "version": "0.1",
        "scale": SCALE,
        "ranks": rank_table(),
        "armoury": [
            {
                **weapon_cost_breakdown(b),
                "legacy_expected": exp,
                "legacy_delta": weapon_cost(b) - exp,
            }
            for b, exp in SAMPLE_ARMOURY
        ],
        "design_examples": [weapon_cost_breakdown(b) for b in DESIGN_EXAMPLES],
        "structures": structure_table(),
        "groundworks": {"I": groundworks_cost(1), "II": groundworks_cost(2)},
        "settlement_dials": {
            "housing_base": 12,
            "bunkhouse_slots": 6,
            "equipment_slots_base": 30,
            "equipment_slots_per_shed": 30,
            "generator_power": 5,
            "power_draw_by_tier": {1: 1, 2: 2, 3: 3},
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def run_report() -> int:
    print(f"=== Settlements Points Engine v0  (scale {SCALE}) ===\n")
    rc = 0

    fails = verify_armoury() + verify_structural()
    if fails:
        print("VERIFY FAILED:")
        for f in fails:
            print(f"  FAIL {f}")
        rc = 1
    else:
        print(
            f"Armoury: {len(SAMPLE_ARMOURY)}/{len(SAMPLE_ARMOURY)} cost cleanly; "
            "structural invariants hold\n"
        )

    drift = legacy_drift()
    moved = [r for r in drift if r["delta"]]
    print("Legacy x10 baseline vs measured atoms  (M1 repriced the injury/to-hit side):")
    for r in drift:
        mark = "" if not r["delta"] else "  <-- moved"
        print(
            f"  {r['name']:26} legacy {r['legacy']:4}  ->  now {r['derived']:4}  "
            f"({r['delta']:+d}){mark}"
        )
    tl, td = sum(r["legacy"] for r in drift), sum(r["derived"] for r in drift)
    print(
        f"  {'TOTAL':26} legacy {tl:4}  ->  now {td:4}  ({td - tl:+d})   "
        f"{len(moved)}/{len(drift)} weapons moved\n"
    )

    print("Ranks (derived vs listed):")
    for row in rank_table():
        print(
            f"  {row['rank']:12} derived={row['derived']:4}  "
            f"listed={row['listed']:4}  d={row['delta']:+d}"
        )

    print("\nDesign examples (your construction shape):")
    for b in DESIGN_EXAMPLES:
        print(f"  {b.name:28} {weapon_cost(b):4} Goods")

    print("\nStarter structures (Materials):")
    power_budget = 5
    draw = 0
    for spec in STARTER_STRUCTURES:
        m = materials_cost(spec)
        d = spec.power_draw
        draw += d
        tag = "*" if spec.starter else " "
        print(f"  {tag} {spec.name:16} Mat {m:4}  Pwr -{d}")
    print(f"  Power check: draw {draw} / Generator +{power_budget}")

    print("\nKey structures (Materials sample):")
    for spec in KEY_STRUCTURES[:8]:
        print(f"    {spec.name:24} Mat {materials_cost(spec):4}  Pwr -{spec.power_draw}")

    out = Path(__file__).resolve().parents[2] / "costs" / "catalogue_v0.json"
    export_catalogue(out)
    print(f"\nWrote {out}")
    return rc

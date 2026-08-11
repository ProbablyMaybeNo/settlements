"""Standing cross-subsystem checks. Run whenever a cost table changes.

WHY THIS EXISTS
---------------
Every defect this rebuild was called in to fix is a RELATION between two
subsystems that were each internally consistent:

  - a Standard Ranged rifle costs 100 while the cheapest body that may carry one
    costs 95, against reference data where a trooper's common weapon runs 17-33%
    of the trooper;
  - Deployables were converted x10 onto the BODY scale from an older list;
  - eleven Payloads were priced identically while measuring 46:1 apart;
  - a free T1 skill grants what a 40-Credit item sells.

None of those is visible from inside the subsystem that contains it. Each was
found by a human reading two tables side by side, months later. These checks read
the tables side by side on demand.

A check here does NOT assert a correct price. It asserts a RELATION that must
hold whatever the prices are, and prints the evidence when one breaks. Every
finding names the two sources it compared, because "which of these two is wrong"
is a design question and this file does not get a vote.

    py -3.13 consistency.py            all checks
    py -3.13 consistency.py --strict   exit 1 on any FAIL (for a pre-commit hook)
"""

from __future__ import annotations

import sys
from pathlib import Path

HARNESS = Path(__file__).resolve().parent
POINTS = HARNESS.parent / "points"
for p in (str(POINTS.parent), str(HARNESS)):
    if p not in sys.path:
        sys.path.insert(0, p)

from points import ticks  # noqa: E402
from points.units import LISTED_BODY, Rank  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


# The reference band from the Trench Crusade pull: a basic trooper's common
# weapon ran roughly 17-33% of the trooper's own cost. Held as a BAND, not a
# target - a class outside it is a question, not automatically an error.
GEAR_BODY_BAND = (0.17, 0.33)

RANK_ORDER = ["recruit", "fighter", "specialist", "leader"]


class Report:
    def __init__(self):
        self.rows = []

    def add(self, status, check, detail, sources):
        self.rows.append((status, check, detail, sources))

    def ok(self, check, detail, sources=""):
        self.add("ok", check, detail, sources)

    def warn(self, check, detail, sources=""):
        self.add("WARN", check, detail, sources)

    def fail(self, check, detail, sources=""):
        self.add("FAIL", check, detail, sources)

    def print(self):
        width = max((len(r[1]) for r in self.rows), default=10)
        n_fail = n_warn = 0
        for status, check, detail, sources in self.rows:
            mark = {"ok": "  ok  ", "WARN": " WARN ", "FAIL": " FAIL "}[status]
            print(f"{mark} {check:<{width}}  {detail}")
            if sources:
                print(f"       {'':<{width}}  ^ {sources}")
            n_fail += status == "FAIL"
            n_warn += status == "WARN"
        print()
        print(f"{len(self.rows)} checks - {n_fail} FAIL, {n_warn} WARN")
        return n_fail


def cheapest_legal_carrier(weapon_class: str) -> tuple[str, int]:
    meta = ticks.CLASS_META.get(weapon_class, {})
    min_rank = meta.get("min_rank", "recruit")
    idx = RANK_ORDER.index(min_rank) if min_rank in RANK_ORDER else 0
    best = None
    for name in RANK_ORDER[idx:]:
        cost = LISTED_BODY[Rank(name)]
        if best is None or cost < best[1]:
            best = (name, cost)
    return best


def check_gear_body_ratio(rep: Report) -> None:
    """The headline relation. A weapon must be cheap relative to the cheapest
    body legally able to hold it."""
    for cls, cost in sorted(ticks.CLASS_CREDITS.items(), key=lambda kv: -kv[1]):
        if cost == 0:
            continue
        rank, body = cheapest_legal_carrier(cls)
        ratio = cost / body
        detail = (f"{cls} {cost} Cr vs cheapest legal carrier {rank} {body} Cr "
                  f"= {ratio:.0%} of the body")
        src = "ticks.CLASS_CREDITS + ticks.CLASS_META[min_rank] vs units.LISTED_BODY"
        if ratio > GEAR_BODY_BAND[1]:
            rep.fail("gear:body ratio", detail + f"  (band {GEAR_BODY_BAND[0]:.0%}-{GEAR_BODY_BAND[1]:.0%})", src)
        elif ratio < GEAR_BODY_BAND[0]:
            rep.warn("gear:body ratio", detail + "  (below band - possibly underpriced)", src)
        else:
            rep.ok("gear:body ratio", detail)


def check_rank_gate_enforced(rep: Report) -> None:
    """CLASS_META carries a min_rank. If nothing reads it, the gate is decorative
    and every ratio check above is comparing against a carrier that is not
    actually enforced."""
    src_text = (POINTS / "weapons.py").read_text(encoding="utf-8")
    reads = "min_rank" in src_text
    if reads:
        rep.ok("rank gate enforced", "weapons.py reads CLASS_META['min_rank']")
    else:
        rep.fail(
            "rank gate enforced",
            "CLASS_META declares min_rank for all 8 classes and weapons.py never reads it - "
            "a Recruit can be costed with a Heavy Ranged and nothing objects",
            "ticks.CLASS_META vs points/weapons.py validate()",
        )


def check_zero_measured_still_priced(rep: Report) -> None:
    for name in getattr(ticks, "UNPRICEABLE_MEASURED_ZERO", ()):
        price = ticks.CHAR_CREDITS.get(name)
        rep.warn(
            "measured-zero priced",
            f"{name} is flagged as measuring inside the noise floor yet is sold at {price} Cr "
            "- a rules defect held open deliberately, not a price to trust",
            "ticks.UNPRICEABLE_MEASURED_ZERO vs ticks.CHAR_CREDITS",
        )


def check_equal_price_unequal_effect(rep: Report) -> None:
    """Failure mode B, mechanised: two things at one price is only fair if they
    are worth the same. Groups characteristics by price and flags any group whose
    members are known to differ."""
    by_price = {}
    for name, cost in ticks.CHAR_CREDITS.items():
        by_price.setdefault(cost, []).append(name)
    zeros = set(getattr(ticks, "UNPRICEABLE_MEASURED_ZERO", ()))
    for cost, names in sorted(by_price.items()):
        if len(names) < 2:
            continue
        names_s = sorted(names)
        legacy = [n for n in names_s if n in LEGACY_UNDERIVED]
        zero = [n for n in names_s if n in zeros]
        measured = [n for n in names_s if n not in LEGACY_UNDERIVED and n not in zeros]

        if zero and measured:
            rep.fail(
                "equal price, unequal evidence",
                f"{cost} Cr shared by {', '.join(names_s)} - but {', '.join(zero)} "
                f"measured inside the noise floor while {', '.join(measured)} did not. "
                "One price, two verdicts",
                "ticks.CHAR_CREDITS vs ticks.UNPRICEABLE_MEASURED_ZERO",
            )
        elif zero and legacy:
            rep.fail(
                "equal price, unequal evidence",
                f"{cost} Cr shared by {', '.join(names_s)} - {', '.join(zero)} measured at "
                f"~zero, {', '.join(legacy)} never measured at all. The shared price is a "
                "grouping that survived its own disproof",
                "ticks.CHAR_CREDITS vs ticks.UNPRICEABLE_MEASURED_ZERO",
            )
        elif len(legacy) == len(names_s):
            rep.warn(
                "equal price, no evidence",
                f"{cost} Cr shared by {', '.join(names_s)} - all still legacy x10, "
                "so the shared price reflects a grouping, not a measurement",
                "ticks.CHAR_CREDITS",
            )
        elif legacy and measured:
            rep.warn(
                "equal price, mixed evidence",
                f"{cost} Cr shared by {', '.join(names_s)} - {', '.join(measured)} measured, "
                f"{', '.join(legacy)} inherited. Agreement here is coincidence until the "
                "inherited ones are measured",
                "ticks.CHAR_CREDITS",
            )
        else:
            rep.ok("equal price", f"{cost} Cr: {', '.join(names_s)} (all measured)")


LEGACY_UNDERIVED = {
    "hook", "smoke", "long_range", "balanced", "defensive", "cleaving",
    "breaching", "concealable", "quiet", "compact",
}


def check_armour_linearity(rep: Report) -> None:
    per_point = {}
    for name, cost in ticks.ARMOUR_CREDITS.items():
        inj = ticks.ARMOUR_INJURY.get(name, 0)
        if inj:
            per_point[name] = cost / abs(inj)
    vals = set(per_point.values())
    if len(vals) <= 1:
        rep.ok("armour linear", f"{per_point} Cr per point of injury reduction")
    else:
        rep.fail(
            "armour linear",
            f"Cr per armour point differs: {per_point}. Each point is a flat -10% on the "
            "injury roll, so -2 must cost exactly twice -1 unless a diminishing-returns "
            "judgment is being encoded deliberately",
            "ticks.ARMOUR_CREDITS vs ticks.ARMOUR_INJURY",
        )


def check_derivation_is_not_tautology(rep: Report) -> None:
    """`heavy_ranged == standard_ranged + long_range` is presented as derived
    twice independently. It is one identity rearranged: both inputs are legacy,
    so the check confirms arithmetic, never a price."""
    lhs = ticks.CLASS_CREDITS["heavy_ranged"]
    rhs = ticks.CLASS_CREDITS["standard_ranged"] + ticks.CHAR_CREDITS["long_range"]
    if lhs == rhs:
        rep.warn(
            "range identity",
            f"heavy_ranged {lhs} == standard_ranged {ticks.CLASS_CREDITS['standard_ranged']} "
            f"+ long_range {ticks.CHAR_CREDITS['long_range']} holds - but both inputs are "
            "legacy x10 and unmeasured, so this verifies arithmetic, not a price",
            "ticks.CLASS_CREDITS + ticks.CHAR_CREDITS",
        )
    else:
        rep.fail("range identity", f"heavy_ranged {lhs} != {rhs}", "ticks.CLASS_CREDITS")


def check_body_formula_reproduces_ladder(rep: Report) -> None:
    """If the printed ladder is reproduced exactly by `base + pts*stat + orders`,
    then the ladder contains ZERO skill value - which makes any derivation that
    SUBTRACTS skill Credits from it arithmetically invalid."""
    pts = {"recruit": 3, "fighter": 5, "specialist": 7, "leader": 9}
    orders = {"recruit": 0, "fighter": 0, "specialist": 1, "leader": 2}
    bad = []
    for name, p in pts.items():
        derived = ticks.BODY_BASE + p * ticks.TICK_STAT + ticks.ORDER_PREMIUM[orders[name]]
        listed = LISTED_BODY[Rank(name)]
        if derived != listed:
            bad.append(f"{name} derived {derived} != listed {listed}")
    if bad:
        rep.warn("body formula", "; ".join(bad), "ticks + units.LISTED_BODY")
    else:
        rep.ok(
            "body formula",
            "base + pts*TICK_STAT + orders reproduces all four ranks exactly, so the "
            "ladder carries NO skill value - any Campaign-Start derivation that subtracts "
            "skill Credits from it is subtracting something that was never added",
        )


def check_deployables_scale(rep: Report) -> None:
    """Deployables live in the rules text, not in ticks.py. Held as declared
    constants so the check runs; the point is the RELATION, not the source."""
    deployables = {
        "Autoturret": 120, "Sniper Turret": 150, "Burst Turret": 180,
        "Blast Turret": 140, "Reinforced Turret": 150,
        "Proximity mine + Explosion": 90, "Trip Wire": 30,
        "Munitions Beacon": 80, "Revive Beacon": 120,
    }
    fighter = LISTED_BODY[Rank.FIGHTER]
    over = {k: v for k, v in deployables.items() if v / fighter > GEAR_BODY_BAND[1]}
    if over:
        worst = max(over.items(), key=lambda kv: kv[1])
        rep.fail(
            "deployables on gear scale",
            f"{len(over)} of {len(deployables)} deployables exceed {GEAR_BODY_BAND[1]:.0%} of a "
            f"Fighter body ({fighter} Cr); worst is {worst[0]} at {worst[1]} Cr "
            f"= {worst[1]/fighter:.0%} of the body carrying it",
            "Full Rules System v1 sec 12.6 (x10 conversion) vs units.LISTED_BODY",
        )
    else:
        rep.ok("deployables on gear scale", "all within band")


def check_equipment_vs_measured_primitive(rep: Report) -> None:
    """Equipment sells modifiers. A modifier has a measured price. They should be
    in the same neighbourhood."""
    to_hit = ticks.CREDITS_TO_HIT
    for item, cost, plus in (("breach_kit", ticks.HACK_GEAR_CREDITS["breach_kit"], 1),
                             ("exploit_suite", ticks.HACK_GEAR_CREDITS["exploit_suite"], 2)):
        implied = cost / plus
        if implied > to_hit * 1.5:
            rep.warn(
                "equipment vs primitive",
                f"{item} sells +{plus} for {cost} Cr = {implied:.0f} Cr per +1, against a "
                f"MEASURED +1 to-hit of {to_hit} Cr ({implied/to_hit:.1f}x) - and it modifies "
                "a test that is worth nothing in scenarios without a claim step",
                "ticks.HACK_GEAR_CREDITS vs ticks.CREDITS_TO_HIT",
            )
        else:
            rep.ok("equipment vs primitive", f"{item} {implied:.0f} Cr per +1 vs measured {to_hit}")


def main(strict: bool = False) -> int:
    rep = Report()
    print("=" * 100)
    print("CROSS-SUBSYSTEM CONSISTENCY - relations that must hold whatever the prices are")
    print("=" * 100)
    print()
    check_body_formula_reproduces_ladder(rep)
    check_gear_body_ratio(rep)
    check_deployables_scale(rep)
    check_rank_gate_enforced(rep)
    check_armour_linearity(rep)
    check_zero_measured_still_priced(rep)
    check_equal_price_unequal_effect(rep)
    check_derivation_is_not_tautology(rep)
    check_equipment_vs_measured_primitive(rep)
    n_fail = rep.print()
    return 1 if (strict and n_fail) else 0


if __name__ == "__main__":
    raise SystemExit(main(strict="--strict" in sys.argv))

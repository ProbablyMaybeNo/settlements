"""Every atom with a plausible SECOND derivation, computed both ways and compared.

WHY THIS EXISTS
---------------
All four guard classes this rebuild has added were found by exactly one pattern,
by hand, late:

  the anchor        1.332 looked clean until the probe chassis disagreed
  the payload table two files disagreed 44 vs 19 vs 33
  Pinned            flipped sign when the scenario basis changed
  armour linearity  the measured ratio and the ruled ratio were indistinguishable

In each case ONE derivation looked internally perfect - tight CI, sane spread,
paired estimator - and the defect was only visible from a SECOND route to the
same quantity. A confidence interval bounds sampling noise; it cannot see a wrong
denominator, a wrong scenario basis, or a stale artefact. A second derivation can.

So this does automatically, on demand, what was previously done by a human
noticing. It reads the LIVE artefact for each measurement (never a hand-picked
filename) and compares quantities that must agree.

IT DOES NOT ADJUDICATE. When two routes disagree it names both sources and stops.
Which one is wrong is a design question and this file does not get a vote - the
same rule consistency.py already follows.

    py -3.13 two_route.py            report
    py -3.13 two_route.py --strict   exit 1 on any DISAGREE (for a hook)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import provenance as P  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def load(name):
    """The LIVE artefact for a measurement name, or None."""
    p = P.latest(name)
    if p is None or not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def newest(prefix):
    """Live artefact whose name starts with `prefix` - tolerates the N in the name."""
    rows = [r for r in P.staleness(verbose=False)
            if r.get("latest_of_name") and str(r.get("name", "")).startswith(prefix)]
    if not rows:
        return None, None
    rows.sort(key=lambda r: r.get("created") or "")
    r = rows[-1]
    return json.loads((P.RESULTS / r["file"]).read_text(encoding="utf-8")), r["file"]


class Route:
    """One derivation of a quantity: a value, its SE, where it came from, and the
    BASIS it was measured on. Two routes on different bases are not comparable,
    and calling that a disagreement is the cry-wolf failure the sign-split
    detector already had once."""

    def __init__(self, value, se, source, note="", basis="hold_claim"):
        self.value, self.se, self.source, self.note = value, se, source, note
        self.basis = basis

    def __repr__(self):
        return f"{self.value:+.4f}+-{self.se:.4f} ({self.source}, basis={self.basis})"


def compare(label, a, b, rep, tol_note="", resolve=None):
    """Two routes to one quantity. Disagreement = the gap exceeds combined noise.

    `resolve` is the smallest difference this check MUST be able to detect for a
    pass to mean anything. Supply it whenever route B is a RIVAL HYPOTHESIS rather
    than a second measurement — see the armour row.
    """
    if a is None or b is None:
        missing = "route A" if a is None else "route B"
        rep.append({"quantity": label, "status": "UNAVAILABLE",
                    "detail": f"{missing} could not be derived"})
        print(f"  {'UNAVAIL':<10}{label:<38} {missing} could not be derived")
        return
    gap = b.value - a.value
    gse = (a.se ** 2 + b.se ** 2) ** 0.5
    # A gap inside combined noise is AGREEMENT ONLY IF the noise is small enough
    # to have detected a real gap. Two useless measurements always "agree".
    #
    # THE DEFAULT TEST IS RELATIVE, AND THAT IS WRONG FOR HYPOTHESIS ROWS.
    # 2026-08-13: this module issued a false pass on exactly the failure it exists
    # to prevent. The armour row compares the measured heavy/light ratio against
    # the arithmetic 2.0, with the ruled 1.667 as the live rival — the two are
    # 0.333 apart. At ratio 1.745 the relative rule set the bar at 0.35 x 1.745 =
    # 0.611, nearly TWICE the whole distance between the hypotheses, so gse 0.416
    # passed as AGREE while `measure_armour.py`, reading the same numbers, printed
    # CANNOT DISCRIMINATE. Two files, one dataset, opposite verdicts.
    #
    # The relative rule is a fine generic proxy for "is this measurement worth
    # anything at all". It is the wrong question when the check is asked to
    # separate two named candidates: there the bar is set by the DISTANCE BETWEEN
    # THEM, not by the size of the quantity. Pass `resolve` and the bar follows the
    # question being asked.
    if resolve:
        informative = gse < resolve / 1.96
    elif a.value:
        informative = gse < max(0.35 * abs(a.value), 0.05)
    else:
        informative = gse < 0.05
    disagree = abs(gap) > 1.96 * gse
    if a.basis != b.basis:
        # NOT a contradiction. The two routes measured different games, so the
        # gap is uninterpretable in either direction - it is not evidence that
        # one is wrong, and it is not evidence that they agree.
        status = "BASIS-MISMATCH"
    else:
        status = "DISAGREE" if disagree else ("AGREE" if informative else "INCONCLUSIVE")
    rep.append({"quantity": label, "status": status, "gap": round(gap, 4),
                "gap_se": round(gse, 4), "a": repr(a), "b": repr(b),
                "a_source": a.source, "b_source": b.source})
    mark = {"DISAGREE": "DISAGREE", "AGREE": "  ok  ", "INCONCLUSIVE": "INCONCL",
            "BASIS-MISMATCH": "BASIS!!"}[status]
    print(f"  {mark:<10}{label:<38} {a.value:+.3f} vs {b.value:+.3f}"
          f"   gap {gap:+.3f}+-{gse:.3f}")
    print(f"  {'':<10}{'':<38} A: {a.source}")
    print(f"  {'':<10}{'':<38} B: {b.source}")
    if a.note or b.note:
        print(f"  {'':<10}{'':<38} {a.note or b.note}")


# ---------------------------------------------------------------------------
# ROUTE BUILDERS. Each returns a Route or None; None means "not derivable from
# the current artefacts", which is reported as UNAVAILABLE rather than skipped.
# ---------------------------------------------------------------------------

def anchor_direct():
    d, f = newest("gear-anchor-objective")
    if not d:
        return None
    vals, ses = [], []
    for r in d.get("raw_cells", []):
        c = (r.get("cells") or {}).get("hold_claim")
        if c and not c.get("degenerate"):
            vals.append(c["wp"]); ses.append(c["se"])
    if not vals:
        return None
    m = sum(vals) / len(vals)
    se = (sum(s * s for s in ses) ** 0.5) / len(ses)
    return Route(m, se, f"{f} (hold_claim cells, standard rosters)")


def anchor_from_probe():
    """+1 Damage read off the weapon-class damage ladder: probe_d1->d2 IS +1."""
    d, f = newest("weapon-class-atoms-objective")
    if not d:
        return None
    rows = (d.get("raw_cells") or {}).get("damage") or []
    r = next((x for x in rows if x.get("variant") == "probe_d2"), None)
    if not r or r.get("wp") is None:
        return None
    hc = r.get("hold_claim")
    if hc is None:
        return Route(r["wp"], r["se"], f"{f} (probe_d2)", basis="hold",
                     note="probe_d2's hold_claim cell was DEGENERATE, so this route is "
                          "hold-only and is NOT basis-comparable to route A")
    return Route(hc, r["se"], f"{f} (probe_d2, hold_claim cell)")


def damage_ladder_steps():
    """Internal check: consecutive damage probes must each differ by one anchor."""
    d, f = newest("weapon-class-atoms-objective")
    if not d:
        return None, None
    rows = {x["variant"]: x for x in ((d.get("raw_cells") or {}).get("damage") or [])
            if x.get("wp") is not None}
    if not {"probe_d2", "probe_d3"} <= set(rows):
        return None, None
    a, b = rows["probe_d2"], rows["probe_d3"]
    step = b["wp"] - a["wp"]
    se = (a["se"] ** 2 + b["se"] ** 2) ** 0.5
    basis = "hold_claim" if a.get("hold_claim") is not None else "hold"
    return Route(step, se, f"{f} (probe_d3 - probe_d2 step)", basis=basis), f


def melee_to_ranged_direct():
    """The melee -> 18" step, measured in one hop."""
    d, f = newest("weapon-class-atoms-objective")
    if not d:
        return None
    rows = {x["variant"]: x for x in ((d.get("raw_cells") or {}).get("melee") or [])
            if x.get("wp") is not None}
    r = rows.get("probe_r18")
    if not r:
        return None
    return Route(r["wp"], r["se"], f"{f} (melee -> probe_r18, direct)")


def melee_to_ranged_composed():
    """The same step, composed: melee -> 6" plus 6" -> 18".

    READ THE VERDICT CAREFULLY - THIS CROSSES CHASSIS, AND THAT IS THE POINT.

    The two hops are measured on DIFFERENT baseline crews. `melee -> r6` upgrades
    one model in an all-MELEE crew; `r6 -> r18` upgrades one model in an all-r6
    crew. So composing them is valid only if a weapon's value is INDEPENDENT of
    what the rest of the crew carries.

    A disagreement here therefore does NOT mean "reach is non-additive within one
    chassis". It means the value of a weapon DEPENDS ON THE CREW AROUND IT - and
    that is the assumption a flat per-weapon catalogue price is built on. If this
    route disagrees, the size of the gap is the size of the error in pricing any
    weapon independently of its list.

    Measured 2026-08-13 at N=5000: direct +10.930 vs composed +7.870, a 3.060
    gap at 2.10 SE. Giving one model an 18" gun is worth ~39% MORE in a crew that
    has no other guns than the decomposition through a gun-carrying crew predicts.
    """
    d, f = newest("weapon-class-atoms-objective")
    if not d:
        return None
    cells = d.get("raw_cells") or {}
    mel = {x["variant"]: x for x in (cells.get("melee") or []) if x.get("wp") is not None}
    rng = {x["variant"]: x for x in (cells.get("range") or []) if x.get("wp") is not None}
    a, b = mel.get("probe_r6"), rng.get("probe_r18")
    if not a or not b:
        return None
    v = a["wp"] + b["wp"]
    se = (a["se"] ** 2 + b["se"] ** 2) ** 0.5
    return Route(v, se, f"{f} (melee->r6 plus r6->r18, composed)")


def payload_route(which, trait):
    name = {"table": "payload-table-objective", "signsplit": "payload-signsplit"}[which]
    d, f = newest(name)
    if not d:
        return None
    if which == "table":
        r = next((x for x in d.get("raw_cells", []) if x.get("trait") == trait), None)
        if not r or r.get("price_wp") is None:
            return None
        return Route(r["price_wp"], r.get("price_se") or 0.0, f"{f}")
    r = next((x for x in d.get("raw_cells", []) if x.get("trait") == trait), None)
    if not r or r.get("price_wp") is None:
        return None
    # signsplit stores no per-trait SE; borrow the table's as an order of
    # magnitude and SAY SO rather than silently treating it as exact.
    t = payload_route("table", trait)
    return Route(r["price_wp"], (t.se if t else 0.1), f"{f}",
                 note="signsplit stores no per-trait SE; the table's SE is used as a "
                      "proxy, so this comparison is indicative rather than exact")


def armour_ratio_routes():
    d, f = newest("armour-level")
    if not d:
        return None, None
    rows = (d.get("raw_cells") or {}).get("value") or []
    lo = next((x for x in rows if x.get("variant") == "light" and x.get("wp")), None)
    hi = next((x for x in rows if x.get("variant") == "heavy" and x.get("wp")), None)
    if not lo or not hi:
        return None, None
    ratio = hi["wp"] / lo["wp"]
    rse = abs(ratio) * ((hi["se"] / hi["wp"]) ** 2 + (lo["se"] / lo["wp"]) ** 2) ** 0.5
    measured = Route(ratio, rse, f"{f} (heavy/light)")
    # The arithmetic route: armour is a flat -1 per level on the injury roll, so
    # IF win-point value were linear in injury probability the ratio would be 2.0.
    # That premise is now in doubt - linear in probability does not imply linear
    # in win-points - so this is reported as a COMPARISON, not a requirement.
    arithmetic = Route(2.0, 0.0, "injury-roll arithmetic (-1 vs -2), zero SE by construction",
                       basis=measured.basis,
                       note="the 2.0 premise is DISPUTED: linear in injury probability does "
                            "not imply linear in win-points")
    return measured, arithmetic


def main(strict=False):
    print("=" * 100)
    print("TWO-ROUTE CONSISTENCY — every quantity with a second derivation")
    print("=" * 100)
    print("Reads the LIVE artefact per measurement. Names both sources on disagreement")
    print("and does NOT adjudicate: which route is wrong is a design question.")
    print()

    rep = []

    print("ANCHOR (+1 Damage)")
    compare("anchor: rosters vs probe chassis",
            anchor_direct(), anchor_from_probe(), rep)

    print()
    print("DAMAGE LADDER (internal)")
    step, _ = damage_ladder_steps()
    compare("damage step d2->d3 vs anchor", anchor_direct(), step, rep)

    print()
    print("RANGE ADDITIVITY (one hop vs two)")
    compare("melee->18\" direct vs composed",
            melee_to_ranged_direct(), melee_to_ranged_composed(), rep)

    print()
    print("PAYLOAD TABLE (canonical vs diagnostic)")
    for trait in ("bleeding", "blast", "suppressive", "shocking", "armour_piercing"):
        a = payload_route("table", trait)
        b = payload_route("signsplit", trait)
        compare(f"payload:{trait}", a, b, rep)

    print()
    print("ARMOUR LADDER")
    m, arith = armour_ratio_routes()
    # resolve = |2.0 - 1.667|, the gap between the arithmetic prediction and the
    # ruled Light 60 / Heavy 100. A pass here is only meaningful if the data could
    # have told those two apart; anything coarser is a coin toss reported as a tick.
    compare("armour heavy/light ratio", m, arith, rep, resolve=abs(2.0 - 5.0 / 3.0))

    print()
    print("=" * 100)
    bad = [r for r in rep if r["status"] == "DISAGREE"]
    mism = [r for r in rep if r["status"] == "BASIS-MISMATCH"]
    unk = [r for r in rep if r["status"] in ("UNAVAILABLE", "INCONCLUSIVE")]
    print(f"  DISAGREE: {len(bad)}   BASIS-MISMATCH: {len(mism)}   "
          f"INCONCLUSIVE/UNAVAILABLE: {len(unk)}   "
          f"AGREE: {len(rep) - len(bad) - len(unk) - len(mism)}")
    for r in mism:
        print(f"    BASIS-MISMATCH  {r['quantity']}")
        print(f"                    the two routes measured DIFFERENT GAMES, so the gap")
        print(f"                    is uninterpretable - not a contradiction, and not a pass")
    for r in bad:
        print(f"    DISAGREE  {r['quantity']}")
        print(f"              A: {r['a_source']}")
        print(f"              B: {r['b_source']}")
    print()
    print("  INCONCLUSIVE means the two routes are consistent but too NOISY to have")
    print("  detected a real gap. It is not agreement - two useless measurements always")
    print("  agree, and reporting that as a pass is how a false all-clear gets issued.")
    return 1 if (strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main("--strict" in sys.argv))

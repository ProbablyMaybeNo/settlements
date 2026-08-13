"""Re-derive the weapon classes from measured atoms, replacing the legacy x10.

WHAT IS BEING REPLACED
----------------------
points/ticks.py introduces its class table with the comment "Weapon classes -
legacy x10": the eight class prices were carried across from an older, much
smaller point scale by multiplying by ten, and not one of them has ever been
measured. Standard Ranged at 100 Credits is the load-bearing case, because the
cheapest body that may legally carry one is a 95-Credit Fighter - a weapon at
105% of its own carrier, against reference data where a basic trooper's common
weapon runs 17-33% of the trooper.

A class is not an atom. It is a BUNDLE, and the bundle has to come apart before
anything can be priced:

    class price  =  damage value  +  range band  +  hands/slots
                    +  rank gate  +  always-on traits

DAMAGE is already anchored: see anchor.py, which holds the value, its CI, its
per-cell spread and the full history of the four candidates it replaced.

RANGE is the one this file exists to measure. ticks.py prices exactly one range
step - effective 18" to deployment 24" at 60 Credits - and that figure is
long_range's own legacy value restated, so the "derived twice independently"
claim in POINTS-TABLE is one identity rearranged. The three lower steps are
recorded as RANGE_STEP_UNPRICED, correctly, because they cannot be read off the
class table: the table says melee->6" is worth 40 (thrown minus light melee) and
melee->8" is worth 0 (sidearm minus one-handed melee). Same axis, two answers.

METHOD. Probe weapons, not catalogue weapons. Each probe fixes every field but
one, so a mirror between two probes isolates a single axis. Costs are irrelevant
and set to zero: this measures VALUE. A catalogue weapon cannot do this job
because it varies damage, range and traits simultaneously.

  probe_r{R}   dmg 1, range R, no traits    -> isolates the range band
  probe_d{D}   dmg D, range 18, no traits   -> isolates damage at fixed range
  probe_melee  dmg 1, range 0, no traits    -> the melee floor

WHAT CANNOT BE MEASURED HERE, and must stay a flagged judgment call:
  hands / slots     Unit takes exactly one weapon string; 'two_handed' is a dead
                    string in data.py. Needs a loadout model.
  rank gate         CLASS_META declares min_rank for all eight classes and
                    weapons.py never reads it. The gate is enforced by nothing in
                    code, so it currently has no measurable value at all.
  Loud / Quiet      no alarm or noise system exists.
  fire-while-Engaged the Sidearm's defining privilege - take_action() forces melee
                    for every engaged unit with no trait check.

    py -3.13 measure_weapon_classes.py [N]
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from measure import WEAPONS  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
import anchor as A  # noqa: E402
ANCHOR = A.VALUE

# Fingerprinted BEFORE the games run, so an edit landing mid-run cannot stamp this
# result with code that never executed.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

# --- probes -----------------------------------------------------------------
# 12" is included deliberately. The whole banding story rests on 12" being the
# turn-one firing threshold (deploy zones 24" apart, MOV 6", so 24-6=18 fires on
# turn one and 8" cannot), and no experiment has ever tested that claim.
RANGES = (6, 8, 12, 18, 24)
for r in RANGES:
    WEAPONS[f"probe_r{r}"] = dict(rng=r, dmg=1, kind="ranged", cost=0, traits=())
WEAPONS["probe_melee"] = dict(rng=0, dmg=1, kind="melee", cost=0, traits=())
for d in (0, 1, 2, 3, 4):
    WEAPONS[f"probe_d{d}"] = dict(rng=18, dmg=d, kind="ranged", cost=0, traits=())


def uniform(weapon, n=6):
    ranks = ["Leader", "Specialist", "Fighter", "Fighter", "Recruit", "Recruit"][:n]
    return [(f"U{i}", ranks[i], weapon, "none", dict(dex=2, str=2)) for i in range(n)]


def sweep(base_weapon, variants, label, note, only_first=False):
    """Mirror a crew carrying `base_weapon` against itself, upgrading one side to
    each variant. Priced from OBJECTIVE cells only; Annihilate reported, never priced.

    The previous version of this function averaged hold and annihilate together,
    which is why its results were void: a weapon's value on a kill scenario is not
    a component of its price in a ruleset that wins on objectives.
    """
    print(f"\n  {label}")
    print(f"    {'variant':<16}{'hold':>9}{'hold_clm':>10}{'annih':>9}"
          f"{'PRICE':>9}{'SE':>7}{'Cr':>7}  sig  dropped")
    rows = []
    spec = uniform(base_weapon)
    for v in variants:
        eff = E.Effect(kind="weapon_swap", weapon=v, name=v, only_first=only_first)
        res = M.price_atom(spec, eff, n=N)

        def cell(s):
            c = res["cells"].get(s)
            return None if (c is None or c["degenerate"]) else c["wp"]

        def f(x):
            return f"{x:+.3f}" if x is not None else "   degen"

        if res["price_wp"] is None:
            print(f"    {v:<16}{'ALL OBJECTIVE CELLS DEGENERATE - no price':>50}")
            rows.append({"variant": v, "wp": None, "se": None,
                         "degenerate": res["dropped_degenerate"]})
            continue
        wp, se = res["price_wp"], res["price_se"]
        lo, hi = res["price_ci"]
        print(f"    {v:<16}{f(cell('hold')):>9}{f(cell('hold_claim')):>10}"
              f"{f(cell('annihilate')):>9}{wp:>+9.3f}{se:>7.3f}"
              f"{A.to_credits(wp):>7.0f}"
              f"{'  yes' if res['price_significant'] else '   no'}  "
              f"{','.join(res['dropped_degenerate']) or '-'}")
        rows.append({"variant": v, "wp": round(wp, 4), "se": round(se, 4),
                     "ci": [round(lo, 4), round(hi, 4)],
                     "credits": round(A.to_credits(wp), 1),
                     "hold": cell("hold"), "hold_claim": cell("hold_claim"),
                     "annihilate": cell("annihilate"),
                     "priced_from": res["priced_from"],
                     "scenarios_degenerate": res["dropped_degenerate"],
                     "significant": res["price_significant"],
                     "sign_split": res["sign_split"],
                     "saturated": res["any_saturated"]})
    print(f"    {note}")
    return rows


print("=" * 104)
print(f"WEAPON CLASS ATOMS — probes, not catalogue weapons. N={N}/cell, paired mirror")
print("=" * 104)
print(A.describe())
print("replacing prices whose own source comment reads 'Weapon classes - legacy x10'")
print("and which nothing has ever measured")
print(f"Pricing: {', '.join(M.PRICING_SCENARIOS)}.  "
      f"{', '.join(M.DIAGNOSTIC_SCENARIOS)} reported, never priced.")

range_rows = sweep(
    "probe_r6", [f"probe_r{r}" for r in RANGES if r != 6],
    "RANGE BAND — ONE model upgraded; only reach changes (baseline 6\")",
    "one model, not six: upgrading the whole crew ran the mirror to 83-87% where "
    "the ceiling compresses every difference",
    only_first=True,
)

dmg_rows = sweep(
    "probe_d1", [f"probe_d{d}" for d in (0, 2, 3, 4)],
    "DAMAGE — every model at 18\"; only the injury modifier changes (baseline +1)",
    "confirms the GEAR anchor transfers to a probe chassis; +2 should read ~1x anchor",
)

melee_rows = sweep(
    "probe_melee", ["probe_r6", "probe_r18"],
    "MELEE vs RANGED — ONE model upgraded, baseline a dmg-1 melee weapon",
    "the melee-to-ranged step, which the class table prices inconsistently (40 or 0)",
    only_first=True,
)

print("\n" + "=" * 104)
print("WHAT THIS DOES AND DOES NOT SETTLE")
print("=" * 104)
print("  Settled: the range curve and the damage curve, on one chassis, with CIs.")
print("  NOT settled, and unmeasurable on this engine as built:")
print("    hands/slots        Unit carries one weapon string; 'two_handed' is inert")
print("    rank gate          CLASS_META.min_rank is read by nothing in weapons.py")
print("    Loud / Quiet       no noise or alarm system exists")
print("    fire-while-Engaged take_action() forces melee for any engaged unit")
print("  A class price built from this file is therefore damage + range only, and")
print("  the remainder is a flagged judgment call rather than a measurement.")

env = P.Envelope(
    name=f"weapon-class-atoms-objective-n{N}",
    question="What are the weapon classes actually worth, decomposed into damage and "
            "range on a fixed probe chassis and priced from OBJECTIVE play only, "
            "replacing the legacy x10 figures?",
    values={"range": {r["variant"]: r["wp"] for r in range_rows},
            "damage": {r["variant"]: r["wp"] for r in dmg_rows},
            "melee_to_ranged": {r["variant"]: r["wp"] for r in melee_rows}},
    raw_cells={"range": range_rows, "damage": dmg_rows, "melee": melee_rows},
    params={"N_per_cell": N, "anchor_wp_per_model": ANCHOR,
            "anchor_provisional": A.PROVISIONAL,
            "credits_per_winpoint": round(A.credits_per_winpoint(), 4),
            "ranges": list(RANGES),
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            "method": "paired mirror between probe weapons differing in ONE field"},
    caveats=[
        "Probes carry no traits and cost zero: this measures VALUE, not price. "
        "Conflating the two is how a harness ends up asserting the number it was "
        "built to test.",
        "SUPERSEDES weapon-class-atoms-n2500 and -n3000, which averaged hold with "
        "annihilate and so priced a game the ruleset says nobody wins. The earlier "
        "caveat that 'most rows rest on Annihilate' described the pre-policy-fix "
        "engine; Hold now resolves and carries its own weight.",
        "The anchor is PROVISIONAL - third in a row to reject its predecessors. Every "
        "Credits column moves if it moves; the win-point column does not.",
        "hands/slots, the rank gate, Loud/Quiet and fire-while-Engaged are all "
        "unmeasurable on this engine, so a class price from this file covers damage "
        "and range only.",
        "12\" is measured explicitly because the entire banding argument rests on it "
        "being the turn-one firing threshold, and that has never been tested.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

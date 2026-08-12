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

DAMAGE is already anchored: +1 on the injury roll = 1.150 wp/model
(measure_anchor.py, CI [1.022, 1.278]).

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
import anchor as _anchor  # noqa: E402
ANCHOR = _anchor.VALUE

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


def sweep(base_weapon, variants, label, note):
    """Mirror a crew carrying `base_weapon` against itself, upgrading one side to
    each variant. Returns rows of (variant, wp, se, live scenarios)."""
    print(f"\n  {label}")
    print(f"    {'variant':<16}{'wp/model':>10}{'SE':>7}{'95% CI':>18}"
          f"{'Cr':>7}{'scenarios':>22}")
    rows = []
    spec = uniform(base_weapon)
    for v in variants:
        eff = E.Effect(kind="weapon_swap", weapon=v, name=v)
        cells = [M.measure(spec, eff, s, n=N) for s in ("hold", "annihilate")]
        live = [c for c in cells if not c.degenerate]
        dead = [c.scenario for c in cells if c.degenerate]
        if not live:
            print(f"    {v:<16}{'ALL SCENARIOS DEGENERATE - unmeasurable on this crew':>60}")
            rows.append({"variant": v, "wp": None, "se": None,
                         "degenerate": [c.scenario for c in cells]})
            continue
        wp = statistics.fmean([c.per_applied for c in live])
        se = (sum(c.per_applied_se ** 2 for c in live) ** 0.5) / len(live)
        lo, hi = wp - 1.96 * se, wp + 1.96 * se
        used = ",".join(c.scenario for c in live) + (f" (-{','.join(dead)})" if dead else "")
        print(f"    {v:<16}{wp:>+10.3f}{se:>7.3f}  [{lo:+.3f}, {hi:+.3f}]"
              f"{wp / ANCHOR * 15:>7.0f}{used:>22}")
        rows.append({"variant": v, "wp": round(wp, 4), "se": round(se, 4),
                     "ci": [round(lo, 4), round(hi, 4)],
                     "credits": round(wp / ANCHOR * 15, 1),
                     "scenarios_used": [c.scenario for c in live],
                     "scenarios_degenerate": dead,
                     "significant": abs(wp) > 1.96 * se})
    print(f"    {note}")
    return rows


print("=" * 104)
print(f"WEAPON CLASS ATOMS — probes, not catalogue weapons. N={N}/cell, paired mirror")
print("=" * 104)
print(f"anchor {ANCHOR:.3f} wp/model = 15 Cr   |   replacing prices whose own source comment")
print("reads 'Weapon classes - legacy x10' and which nothing has ever measured")

range_rows = sweep(
    "probe_r6", [f"probe_r{r}" for r in RANGES if r != 6],
    "RANGE BAND — every model carries dmg 1; only reach changes (baseline 6\")",
    "each row is value(R) - value(6\"), so the steps are differences between rows",
)

dmg_rows = sweep(
    "probe_d1", [f"probe_d{d}" for d in (0, 2, 3, 4)],
    "DAMAGE — every model at 18\"; only the injury modifier changes (baseline +1)",
    "confirms the GEAR anchor transfers to a probe chassis; +2 should read ~1x anchor",
)

melee_rows = sweep(
    "probe_melee", ["probe_r6", "probe_r18"],
    "MELEE vs RANGED — baseline is a dmg-1 melee weapon",
    "the melee-to-ranged step, which the class table prices inconsistently (40 or 0)",
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
    name=f"weapon-class-atoms-n{N}",
    question="What are the weapon classes actually worth, decomposed into damage and "
            "range on a fixed probe chassis, replacing the legacy x10 figures?",
    values={"range": {r["variant"]: r["wp"] for r in range_rows},
            "damage": {r["variant"]: r["wp"] for r in dmg_rows},
            "melee_to_ranged": {r["variant"]: r["wp"] for r in melee_rows}},
    raw_cells={"range": range_rows, "damage": dmg_rows, "melee": melee_rows},
    params={"N_per_cell": N, "anchor_wp_per_model": ANCHOR, "ranges": list(RANGES),
            "method": "paired mirror between probe weapons differing in ONE field"},
    caveats=[
        "Probes carry no traits and cost zero: this measures VALUE, not price. "
        "Conflating the two is how a harness ends up asserting the number it was "
        "built to test.",
        "Hold is degenerate for symmetric pure-ranged crews (100% draws, 0.00 VP "
        "against a 15-VP ceiling), so most rows here rest on Annihilate - the one "
        "scenario the ruleset says you do not win by. Same structural limit as the "
        "DEX ladder. Blocked on the Take-a-Hold scoring fix.",
        "hands/slots, the rank gate, Loud/Quiet and fire-while-Engaged are all "
        "unmeasurable on this engine, so a class price from this file covers damage "
        "and range only.",
        "12\" is measured explicitly because the entire banding argument rests on it "
        "being the turn-one firing threshold, and that has never been tested.",
    ],
)
out = env.write()
print(f"\n[stamped] {out.name}")

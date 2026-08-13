"""Re-price every payload from objective play only. THE CANONICAL PAYLOAD TABLE.

WHY THIS SCRIPT IS THE ONE TO READ
----------------------------------
For a while the best payload numbers in the project lived in
`measure_signsplit.py`'s output, because that script happened to be the first one
moved onto `price_atom()` and therefore the only one pricing from objective play.
Its filename advertises a narrow diagnostic - "are these three traits sign-split?"
- so the whole 12-trait table sat under a name no reader would look under. The
numbers were right and the index was wrong, which no confidence interval and no
provenance fingerprint can catch.

So: THIS script is canonical. `measure_signsplit.py` stays, answering only the
question its name asks. Both must go through `price_atom()` and agree; if they
ever disagree, one of them has drifted and the disagreement is the finding.

WHAT CHANGED SINCE THE LAST TABLE
---------------------------------
1. Melee delivers payloads (engine.fight -> payload_of). Every price on record
   before 2026-08-12 was a RANGED-ONLY measurement divided by melee carriers too
   - a DIFFERENTIAL bias that distorted the ranking between traits, not just the
   level. Hook (pull 1", melee only) could never fire at all.
2. The divisor counts models that can actually deliver the trait (n_applied).
3. PRICING IS OBJECTIVE-ONLY. Annihilate is measured and reported per cell and
   never enters a price: the ruleset wins on objectives and never on kills.
4. The anchor is 0.786, not 1.332. The earlier "payload table halves" reading was
   objective numerators over a mixed denominator - an artefact of the mismatch,
   not a finding. Bleeding moves 44 -> 33 Cr, not 44 -> 19.

    py -3.13 measure_payloads.py [N]
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anchor as A  # noqa: E402
import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500

# Fingerprinted BEFORE the games run, so an edit landing mid-run cannot stamp this
# result with code that never executed.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

# Melee-capable payloads now that fight() delivers them. Blast and Suppressive
# stay ranged-only because the rules gate them that way (Thrown/Heavy Ranged, and
# a Pin that only a ranged hit creates).
TRAITS = [
    ("bleeding", False), ("incendiary_fire", False), ("toxic", False),
    ("blinding", False), ("shocking", False), ("concussive", False),
    ("crippling", False), ("heavy_impact", False), ("hook", "melee"),
    ("suppressive", True), ("blast", True), ("armour_piercing", False),
]

# engine trait names differ from the rules names in one place
TRAIT_KEY = {"incendiary_fire": "fire"}

LISTS = {"Fireteam (6)": FIRETEAM6, "Armoured (6)": ARMOURED6}

# what ticks.py charges today, for the drift column
CURRENT = {"bleeding": 46, "incendiary_fire": 22, "toxic": 9, "blinding": 4,
           "shocking": 16, "concussive": 30, "crippling": 30, "heavy_impact": 15,
           "hook": 20, "suppressive": 17, "blast": 43, "armour_piercing": 9}

print("=" * 116)
print(f"PAYLOAD TABLE — canonical, objective-only pricing. N={N}/cell, paired mirror")
print("=" * 116)
print(A.describe())
print()
print(f"  {'trait':<18}{'hold':>9}{'hold_clm':>10}{'annih':>9}"
      f"{'PRICE':>9}{'SE':>7}{'xDmg':>7}{'Cr':>6}{'ticks':>7}{'drift':>8}  sig")

rows = []
for name, gate in TRAITS:
    key = TRAIT_KEY.get(name, name)
    kw = {}
    if gate is True:
        kw["require_ranged"] = True
    elif gate == "melee":
        kw["require_melee"] = True
    eff = E.Effect(kind="weapon_trait", trait=key, name=name, **kw)

    per_list = [M.price_atom(spec, eff, n=N) for spec in LISTS.values()]

    def cell(s):
        vals = []
        for r in per_list:
            c = r["cells"].get(s)
            if c and not c["degenerate"]:
                vals.append(c["wp"])
        return statistics.fmean(vals) if vals else None

    prices = [r["price_wp"] for r in per_list if r["price_wp"] is not None]
    if not prices:
        print(f"  {name:<18}  ALL OBJECTIVE CELLS DEGENERATE — no price")
        rows.append({"trait": name, "price_wp": None, "degenerate": True})
        continue

    mean = statistics.fmean(prices)
    ses = [r["price_se"] for r in per_list if r["price_wp"] is not None]
    pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
    lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled
    rel = mean / A.VALUE
    cr = A.to_credits(mean)
    cur = CURRENT.get(name, 0)
    sig = abs(mean) > 1.96 * pooled
    split = any(r["sign_split"] for r in per_list)

    def f(v):
        return f"{v:+.3f}" if v is not None else "  degen"

    rows.append({"trait": name, "hold": cell("hold"), "hold_claim": cell("hold_claim"),
                 "annihilate": cell("annihilate"), "price_wp": round(mean, 4),
                 "price_se": round(pooled, 4), "price_ci": [round(lo, 4), round(hi, 4)],
                 "rel_to_damage": round(rel, 3), "credits": round(cr, 1),
                 "ticks_now": cur, "significant": sig, "sign_split": split,
                 "per_list": per_list})
    print(f"  {name:<18}{f(cell('hold')):>9}{f(cell('hold_claim')):>10}"
          f"{f(cell('annihilate')):>9}{mean:>+9.3f}{pooled:>7.3f}"
          f"{rel:>6.2f}x{cr:>6.0f}{cur:>7}{cr - cur:>+8.0f}  "
          f"{'yes' if sig else ' no'}{'  SPLIT' if split else ''}")

print()
priced = [r for r in rows if r.get("price_wp") is not None]
zeros = [r["trait"] for r in priced if not r["significant"]]
splits = [r["trait"] for r in priced if r["sign_split"]]
print(f"  indistinguishable from zero at 95%: {', '.join(zeros) if zeros else 'none'}")
print("  A trait in that list has no price. It has a rules problem, and repricing it")
print("  to a small number sells the player something that does nothing.")
print(f"  sign-split (average across families meaningless): {', '.join(splits) or 'none'}")

env = P.Envelope(
    name=f"payload-table-objective-n{N}",
    question="What is every payload worth, priced from OBJECTIVE play only, with melee "
            "delivering its payload and the divisor counting only models that can "
            "actually deliver it? This is the canonical payload table.",
    values={r["trait"]: r.get("price_wp") for r in rows},
    raw_cells=rows,
    params={"N_per_cell": N, "anchor_wp_per_model": A.VALUE,
            "anchor_provisional": A.PROVISIONAL,
            "credits_per_winpoint": round(A.credits_per_winpoint(), 4),
            "lists": list(LISTS),
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            "method": "paired mirror, differenced per game on a shared seed"},
    caveats=[
        "CANONICAL. Supersedes both payload-table-meleefixed (mixed scenarios) and the "
        "payload values carried in payload-signsplit (objective numerators over a mixed "
        "1.332 anchor). measure_signsplit.py remains, answering only its own question.",
        "Supersedes the conditions2d.py M4 table: that one measured ranged-only "
        "delivery while dividing by melee carriers too, a DIFFERENTIAL bias that "
        "distorted the ranking rather than the level.",
        "Annihilate is reported per cell and NEVER priced. The ruleset wins on "
        "objectives and never on kills.",
        "The anchor is PROVISIONAL - third in a row to reject its predecessors, each "
        "prior error invisible from inside the number before it. Every Credits column "
        "here moves if it moves; the win-point column does not.",
        "AI-limited downward for any trait whose value depends on the target REACTING "
        "to it: no policy calls clear_movement_condition, so Off-Balance and Hobbled are "
        "permanent AND unexploited, and the AI never kites or focuses a slowed target.",
        "Payload value rises with target armour (a payload only lands on a hit that "
        "fails to wound), which is why an armoured list is one of the two here. The "
        "armour LEVEL is still unresolved, so these prices move if it moves.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

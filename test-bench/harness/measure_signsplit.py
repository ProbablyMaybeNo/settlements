"""Are the "statistically zero" payloads actually zero, or averaged wrong?

THE QUESTION
------------
Concussive, Crippling and Hook all measure indistinguishable from zero, and the
standing ruling was that they need a mechanical buff or a cut, because no price
fixes a trait that does nothing.

But Pinned measured indistinguishable from zero too, and it was not flat. Its
three Hold cells were all negative and its three Annihilate cells all positive -
six of six consistent - so the mean sat on zero while the atom was doing two
opposite things in the two scenario families. "Worth nothing" and "worth
something on objectives, negative on kills" are different findings, and only the
second survives the per-cell data.

So before any of the three gets redesigned, check whether it is flat or split.
If split, the fix is the same one Pinned needs - price it from objective cells
only - and the effect may not be weak at all.

Every payload is checked, not just the three, because if the pattern is general
then the whole table has been priced across a boundary it should not cross.

    py -3.13 measure_signsplit.py [N]
"""

from __future__ import annotations

# IMPORT GUARD. This file is a SCRIPT: it runs its whole measurement at module
# level. `import measure_x` therefore executes a full sweep as a side effect -
# which happened TWICE in one session, once silently writing an artefact from a
# known-broken board ladder that then passed every provenance check.
#
# Deliberately a loud raise rather than the usual `if __name__ == "__main__":`
# wrapper. The wrapper makes an accidental import a silent no-op; this says why
# nothing happened. The failure being guarded is a silent one, so the guard is
# not silent.
if __name__ != "__main__":
    raise RuntimeError(
        f"{__name__} is a script, not a module - importing it would run its entire "
        "measurement as a side effect. Run it with `py -3.13 <file>.py` instead, or "
        "move the helper you wanted into a module."
    )

import json
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

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

# Fingerprinted BEFORE the games run: Envelope's default_factory fields
# evaluate at construction, which is after the run.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

TRAITS = [
    ("concussive", {}), ("crippling", {}), ("hook", {"require_melee": True}),
    ("bleeding", {}), ("fire", {}), ("toxic", {}), ("blinding", {}),
    ("shocking", {}), ("heavy_impact", {}),
    ("suppressive", {"require_ranged": True}), ("blast", {"require_ranged": True}),
    ("armour_piercing", {}),
]

print("=" * 112)
print(f"SIGN-SPLIT CHECK — per-cell, unaveraged. N={N}/cell")
print("=" * 112)
print("Pricing scenarios: hold, hold_claim.  Annihilate is reported but never priced.")
print(A.describe())
print()
print(f"  {'trait':<16}{'hold':>10}{'hold_claim':>12}{'annihilate':>12}"
      f"{'PRICE (obj only)':>18}{'Cr':>6}  verdict")

rows = []
for name, kw in TRAITS:
    eff = E.Effect(kind="weapon_trait", trait=name, name=name, **kw)
    # Fireteam carries the mixed loadout; Armoured is where payloads land most,
    # since a payload only arrives on a hit that fails to wound.
    per_list = [M.price_atom(spec, eff, n=N) for spec in (FIRETEAM6, ARMOURED6)]

    def cell(res, s):
        c = res["cells"].get(s)
        return None if (c is None or c["degenerate"]) else c["wp"]

    def avg(s):
        vals = [cell(r, s) for r in per_list]
        vals = [v for v in vals if v is not None]
        return sum(vals) / len(vals) if vals else None

    h, hc, an = avg("hold"), avg("hold_claim"), avg("annihilate")
    prices = [r["price_wp"] for r in per_list if r["price_wp"] is not None]
    price = sum(prices) / len(prices) if prices else None
    sig = any(r["price_significant"] for r in per_list)
    split = any(r["sign_split"] for r in per_list)

    # The detector lives in measure.price_atom and NOWHERE ELSE. There was a
    # second one here that tested raw SIGN with no significance requirement, then
    # OR'd itself with the real one - so it could only ever add false positives,
    # never remove them, and it silently defeated the tightening in price_atom.
    # It called Concussive split on hold -0.021 vs annihilate +0.225: opposite in
    # sign, both indistinguishable from zero, i.e. noise against nothing. A
    # detector that fires on noise is worse than no detector, because it
    # manufactures exactly the false structure this rebuild exists to remove.
    if split:
        verdict = "SIGN-SPLIT - not flat"
    elif sig:
        verdict = "real on objectives"
    else:
        verdict = "flat - genuinely ~0"

    def f(v):
        return f"{v:+.3f}" if v is not None else "  degen"

    print(f"  {name:<16}{f(h):>10}{f(hc):>12}{f(an):>12}"
          f"{f(price):>18}{A.to_credits(price) if price is not None else 0:>6.0f}  {verdict}")
    rows.append({"trait": name, "hold": h, "hold_claim": hc, "annihilate": an,
                 "price_wp": price,
                 "credits": round(A.to_credits(price), 1) if price is not None else None,
                 "price_significant": sig, "sign_split": split,
                 "verdict": verdict, "per_list": per_list})

print()
split_rows = [r for r in rows if r["sign_split"]]
flat_rows = [r for r in rows if not r["sign_split"] and not r["price_significant"]]
print(f"  SIGN-SPLIT (average is meaningless): {', '.join(r['trait'] for r in split_rows) or 'none'}")
print(f"  GENUINELY FLAT (buff or cut):        {', '.join(r['trait'] for r in flat_rows) or 'none'}")
print()
print("  A sign-split trait does NOT need a mechanical buff. It needs pricing from")
print("  objective cells only - the same fix Pinned needs, for the same reason.")

env = P.Envelope(
    name=f"payload-signsplit-n{N}",
    question="Are Concussive/Crippling/Hook genuinely flat, or sign-split across scenario "
            "families the way Pinned turned out to be? Checked for every payload, since a "
            "general pattern would mean the whole table was priced across a boundary.",
    values={r["trait"]: {"hold": r["hold"], "hold_claim": r["hold_claim"],
                         "annihilate": r["annihilate"], "price_wp": r["price_wp"],
                         "sign_split": r["sign_split"], "verdict": r["verdict"]}
            for r in rows},
    raw_cells=[{k: v for k, v in r.items() if k != "per_list"} for r in rows],
    params={"N_per_cell": N, "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            "anchor_wp_per_model": A.VALUE, "credits_per_winpoint": A.credits_per_winpoint()},
    caveats=[
        "Prices come from objective scenarios ONLY. The ruleset wins on objectives and "
        "never on kills, so an average including Annihilate prices a game nobody plays.",
        "Annihilate is reported per cell because it diagnoses what an atom does; it is "
        "never summed into a price.",
        "A sign-split verdict means the average was hiding opposite behaviour, not that "
        "the effect is strong. The objective-only figure still has to clear significance "
        "on its own before it becomes a price.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

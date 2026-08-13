"""What is a point of armour worth, and what does it cost? Two different questions.

WHY THIS WAS BLOCKED UNTIL NOW
------------------------------
The shape of the armour ladder was never in dispute. Injury is `1d10 + Damage -
Armour vs 7+`, and `engine2d/data.py` gives none/light/heavy as injury 0/-1/-2,
so each point is a flat 10% off the chance of being wounded and -2 is EXACTLY
twice -1. Linearity is arithmetic here, not a stylistic choice.

What was blocked is the LEVEL. Two methods disagreed by 4x:

  value method       armour ~= 1x damage per point -> ~15 Cr at the old peg
  rebuild-to-pay     broke even nearer 60 Cr per point

Rebuild-to-pay is the one a catalogue actually wants, because a price is "how
much of a fixed budget should this consume", not "how much win rate does this
deliver in isolation". But it measures armour in units of WHATEVER YOU GAVE UP -
and what you give up is a weapon, whose class prices were `legacy x10` and had
never been measured. So it returned "armour costs about as much as a rifle",
which is true and useless, denominated in a currency of unknown value.

Weapon classes are now measured (weapon-class-atoms-objective-n2500), so the
currency is real and rebuild-to-pay means something for the first time.

PROVENANCE WARNING ON THE PRIOR: THERE IS NO PRIOR.
`points/ticks.py` carries Light 30 / Heavy 60 tagged `[measured]`, citing
`balance/armourprice.py`. That file does not exist in the working tree and no
commit on any branch has ever touched a file by that name. The ruled price in the
master rules note is Light 60 / Heavy 100, which is not a clean doubling and so
encodes an unmeasured diminishing-return judgment that the arithmetic above
contradicts. Measure from zero. Do not anchor on either pair.

    py -3.13 measure_armour.py [N]
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

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anchor as A  # noqa: E402
import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from rosters import uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()


class Pair:
    """Two effects applied together, so a BUY and its PAYMENT land on one crew.

    Duck-typed to the Effect interface (`label`, `apply`) because that is all
    `measure.build` requires. The divisor is the larger of the two counts: a model
    that got the armour but not the downgrade was still reached by the package.
    """

    def __init__(self, buy, pay, name):
        self.buy, self.pay, self.name = buy, pay, name

    def label(self):
        return self.name

    def apply(self, crew, weapons):
        nb = self.buy.apply(crew, weapons)
        np_ = self.pay.apply(crew, weapons)
        return max(nb, np_)


def armour(level):
    return E.Effect(kind="armour", armour=level, name=f"armour:{level}")


def downgrade(to):
    # require_ranged so the payment only reaches models that actually carry reach.
    # Without it, a weapon_swap to pistol UPGRADES the melee models and the
    # "payment" is partly a buy - which would bias the trade toward looking fair.
    return E.Effect(kind="weapon_swap", weapon=to, name=f"->{to}",
                    require_ranged=True)


# BASELINE: 4 rifles + 2 bats, NOT a uniform rifle crew.
#
# A pure-ranged mirror draws ~100% of claim games and the scenario reports
# degenerate - the same structural failure that hit the damage probes in
# weapon-class-atoms. Since hold_claim is the ONLY faithful model of a shipped
# scenario (tracking doc 4.5), a baseline that kills it would leave armour
# measurable only on a scenario that models nothing in the ruleset.
#
# Two melee models restore a resolving claim game while leaving four rifles to
# pay with. The armour buy reaches all six; the weapon payment reaches the four.
BASE6 = ([(f"R{i}", rk, "rifle", "none", dict(dex=2, str=2))
          for i, rk in enumerate(["Leader", "Specialist", "Fighter", "Fighter"])]
         + [(f"M{i}", "Recruit", "bat", "none", dict(dex=2, str=2)) for i in range(2)])

print("=" * 112)
print(f"ARMOUR — value, linearity, and rebuild-to-pay. N={N}/cell, paired mirror")
print("=" * 112)
print(A.describe())
print("PRIOR: none. ticks.py's 30/60 cites balance/armourprice.py, a file that has")
print("never existed in any commit on any branch. Measuring from zero.")
print()

# --- 1. VALUE ---------------------------------------------------------------
print("  1. VALUE — what a point of armour delivers, in isolation")
print(f"    {'variant':<22}{'hold':>9}{'hold_clm':>10}{'annih':>9}"
      f"{'PRICE':>9}{'SE':>7}{'xDmg':>7}{'Cr':>7}  sig")

value_rows = []
for level in ("light", "heavy"):
    res = M.price_atom(BASE6,armour(level), n=N)

    def cell(s, r=res):
        c = r["cells"].get(s)
        return None if (c is None or c["degenerate"]) else c["wp"]

    def f(v):
        return f"{v:+.3f}" if v is not None else "   degen"

    wp = res["price_wp"]
    if wp is None:
        print(f"    {'armour:' + level:<22}  ALL OBJECTIVE CELLS DEGENERATE")
        value_rows.append({"variant": level, "wp": None})
        continue
    print(f"    {'armour:' + level:<22}{f(cell('hold')):>9}{f(cell('hold_claim')):>10}"
          f"{f(cell('annihilate')):>9}{wp:>+9.3f}{res['price_se']:>7.3f}"
          f"{wp / A.VALUE:>6.2f}x{A.to_credits(wp):>7.1f}"
          f"{'  yes' if res['price_significant'] else '   no'}")
    value_rows.append({"variant": level, "wp": wp, "se": res["price_se"],
                       "ci": res["price_ci"], "per_point": wp / (1 if level == "light" else 2),
                       "credits": round(A.to_credits(wp), 1),
                       "rel_to_damage": round(wp / A.VALUE, 3),
                       "significant": res["price_significant"],
                       "sign_split": res["sign_split"],
                       "hold": cell("hold"), "hold_claim": cell("hold_claim"),
                       "annihilate": cell("annihilate")})

# --- 2. LINEARITY -----------------------------------------------------------
lin = None
lo_r = next((r for r in value_rows if r["variant"] == "light" and r["wp"]), None)
hi_r = next((r for r in value_rows if r["variant"] == "heavy" and r["wp"]), None)
print()
print("  2. LINEARITY — is heavy 2x light, the ruled 1.667, or neither?")
print("     THE '2x IS ARITHMETIC' PREMISE IS WITHDRAWN (2026-08-13). It argued from the")
print("     flat -10%/point on the injury roll, which is the WRONG QUANTITY: linear in")
print("     injury PROBABILITY does not imply linear in WIN-POINTS, because the second")
print("     armour point buys survival on a model already surviving more often. Neither")
print("     2.0 nor 1.667 is privileged here; both are rivals to be discriminated.")
if lo_r and hi_r and lo_r["significant"] and hi_r["significant"]:
    ratio = hi_r["wp"] / lo_r["wp"]
    # SE of a ratio, delta method.
    rse = abs(ratio) * ((hi_r["se"] / hi_r["wp"]) ** 2 + (lo_r["se"] / lo_r["wp"]) ** 2) ** 0.5
    rlo, rhi = ratio - 1.96 * rse, ratio + 1.96 * rse
    # "2.0 is inside the CI" is WORTHLESS on its own - a CI of [-15, +10] contains
    # 2.0 and also contains everything else. A confidence interval bounds sampling
    # noise; it says nothing about whether the estimate is informative. So the
    # interval must be tight enough to RULE THINGS OUT before its agreement counts
    # as agreement. 1.67 is the ruled Light 60 / Heavy 100 ratio and is the
    # specific rival this test exists to discriminate against.
    informative = (rhi - rlo) < 1.0
    has2 = rlo <= 2.0 <= rhi
    has167 = rlo <= 1.667 <= rhi
    # Naming a verdict "LINEAR (2.0)" while the interval ALSO contains the rival
    # is how a non-result gets read as a confirmation. If both candidates are
    # inside, the only honest verdict is that the run did not discriminate.
    if has2 and has167:
        verdict = "CANNOT DISCRIMINATE — both 2.0 and 1.667 inside the CI"
    elif has2:
        verdict = "consistent with 2.0; 1.667 EXCLUDED"
    elif has167:
        verdict = "consistent with the ruled 1.667; 2.0 EXCLUDED"
    else:
        verdict = "EXCLUDES BOTH — the ratio is neither candidate"
    lin = {"ratio": round(ratio, 3), "se": round(rse, 3),
           "ci": [round(rlo, 3), round(rhi, 3)],
           "informative": informative,
           "contains_2": has2, "contains_167": has167,
           "verdict": verdict}
    print(f"     heavy/light = {ratio:.3f} +- {rse:.3f}   95% CI [{rlo:.3f}, {rhi:.3f}]")
    print(f"     VERDICT: {verdict}")
    if not informative:
        print(f"     (CI spans {rhi - rlo:.2f} — wide enough that agreement with any value")
        print("      would be uninformative on its own.)")
else:
    print("     VERDICT: not testable — at least one armour level did not measure")
    print("     significantly different from zero, so their ratio is noise over noise.")
    lin = {"verdict": "not testable", "informative": False}

# --- 3. REBUILD-TO-PAY ------------------------------------------------------
# The question a catalogue asks: buy armour, pay for it by giving something up,
# and find the payment that returns the crew to parity. A package measuring ~0 is
# a fair trade, and armour is then worth exactly what was surrendered.
print()
print("  3. REBUILD-TO-PAY — buy armour, pay in weapon downgrade, find the fair trade")
print(f"    {'package':<30}{'PRICE':>9}{'SE':>7}{'95% CI':>18}  reading")

pay_rows = []
PACKAGES = [
    (Pair(armour("light"), downgrade("pistol"), "light armour, rifle->pistol"),
     "light armour vs 10\" of reach and -1 dmg"),
    (Pair(armour("heavy"), downgrade("pistol"), "heavy armour, rifle->pistol"),
     "heavy armour vs the same payment"),
    (Pair(armour("heavy"), downgrade("bat"), "heavy armour, rifle->bat"),
     "heavy armour vs surrendering ranged entirely"),
]
for pkg, note in PACKAGES:
    res = M.price_atom(BASE6,pkg, n=N)
    wp = res["price_wp"]
    if wp is None:
        print(f"    {pkg.label():<30}  ALL OBJECTIVE CELLS DEGENERATE")
        continue
    lo, hi = res["price_ci"]
    if not res["price_significant"]:
        reading = "FAIR TRADE — indistinguishable from parity"
    elif wp > 0:
        reading = "armour WORTH MORE than the payment"
    else:
        reading = "armour WORTH LESS than the payment"
    print(f"    {pkg.label():<30}{wp:>+9.3f}{res['price_se']:>7.3f}"
          f"  [{lo:+.3f}, {hi:+.3f}]  {reading}")
    pay_rows.append({"package": pkg.label(), "wp": wp, "se": res["price_se"],
                     "ci": res["price_ci"], "significant": res["price_significant"],
                     "reading": reading, "note": note})

print()
print("  HOW TO READ 3: a package at ~0 means the two sides of the trade are equal, so")
print("  armour's price IS the measured value of what was given up. The weapon-class")
print("  atoms supply that value in win-points, so the conversion no longer routes")
print("  through a 'legacy x10' number. THAT is what unblocked this measurement.")

env = P.Envelope(
    name=f"armour-level-n{N}",
    question="What is a point of armour worth (value), is the ladder linear (it must be, "
            "arithmetically), and what does it cost when a crew has to pay for it by "
            "giving something up (rebuild-to-pay)? Measured with ZERO prior - the 30/60 in "
            "ticks.py cites a file that has never existed.",
    values={"value": {r["variant"]: r["wp"] for r in value_rows},
            "linearity": lin,
            "rebuild_to_pay": {r["package"]: r["wp"] for r in pay_rows}},
    raw_cells={"value": value_rows, "linearity": lin, "rebuild_to_pay": pay_rows},
    params={"N_per_cell": N, "anchor_wp_per_model": A.VALUE,
            "anchor_provisional": A.PROVISIONAL,
            "credits_per_winpoint": round(A.credits_per_winpoint(), 4),
            "baseline_crew": "6 uniform DEX2 riflemen, no armour",
            "armour_table": "none 0 / light -1 / heavy -2 on the injury roll",
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            "method": "paired mirror; rebuild-to-pay via a composite buy+payment effect"},
    caveats=[
        "ZERO PRIOR by design. ticks.py's Light 30 / Heavy 60 is tagged [measured] citing "
        "balance/armourprice.py, which has never existed in any commit on any branch. The "
        "master note's ruled Light 60 / Heavy 100 implies a 1.67 ratio, which contradicts "
        "the flat -10%-per-point arithmetic. Neither pair is used as a starting guess.",
        "Armour and payloads are JOINTLY DETERMINED: a payload only lands on a hit that "
        "fails to wound, so more armour on the table makes every payload more valuable, and "
        "AP is worth a full damage step against armour and nothing against a bare target. "
        "The payload table must be re-run after this lands, and AP after that.",
        "Rebuild-to-pay prices armour in units of the weapon surrendered. That is only "
        "meaningful because the weapon classes are now measured; before that it returned "
        "'about as much as a rifle' denominated in a legacy x10 figure.",
        "The armour penalties in the rules (Improvised -1 AGI; Heavy -1 MOV / -1 AGI / Loud) "
        "are NOT modelled here: AGI is read only inside Dodge and DODGE_ON is False, and "
        "there is no noise system. So this OVERSTATES armour by pricing its drawbacks at "
        "zero - a known upward bias, not a neutral omission.",
        "Every Credits column is provisional on the anchor AND on the scenario-mix ruling "
        "(tracking doc 4.5). The win-point column is not.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")

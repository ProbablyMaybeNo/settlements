"""Re-price every payload, now that melee weapons actually deliver one.

WHAT CHANGED SINCE THE LAST TABLE
---------------------------------
`fight()` called `injure()` with no payload argument for the entire life of the
project, and `_resolve_hit()` — the only reader of PAYLOAD_TRAITS — is reached
solely from `shoot()`. So every payload price on record is a RANGED-ONLY
measurement. Meanwhile `conditions2d.py`'s `upgrade()` swapped melee carriers to
the payload variant and counted them in its divisor, so those prices were divided
by models that could not possibly deliver the trait.

The bias is DIFFERENTIAL, not a flat scale error: it depends on how many melee
carriers each list holds, so it distorts the RANKING between traits, not just the
level. Hook (pull 1", melee only) could never fire under any circumstances.

Two corrections here, then:
  1. melee now delivers its payload (engine.fight -> payload_of)
  2. the divisor counts models that can actually deliver the trait, via
     Effect.eligible / n_applied — not models present

And one thing now known that was not before: value(Pinned) is ~0
(-0.109 wp/model, CI [-0.267, +0.049], value-of-pinned-n4000). A ranged payload
REPLACES Pinned, so with the subtrahend at zero these measured values are close
to each condition's gross worth rather than a difference against an unknown.

    py -3.13 measure_payloads.py [N]
"""

from __future__ import annotations

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from crews import ARMOURED6, FIRETEAM6  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
ANCHOR = 1.150

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
SCEN = ("hold", "annihilate")

# what ticks.py charges today, for the drift column
CURRENT = {"bleeding": 46, "incendiary_fire": 22, "toxic": 9, "blinding": 4,
           "shocking": 16, "concussive": 30, "crippling": 30, "heavy_impact": 15,
           "hook": 20, "suppressive": 17, "blast": 43, "armour_piercing": 9}

print("=" * 108)
print(f"PAYLOAD TABLE — re-measured with melee delivery FIXED, N={N}/cell, paired mirror")
print("=" * 108)
print(f"anchor {ANCHOR:.3f} wp/model = 15 Cr   |   value(Pinned) ~ 0, so these are close to gross worth")
print()
print(f"  {'trait':<18}{'wp/model':>10}{'SE':>7}{'95% CI':>18}{'x Damage':>10}{'Cr':>6}"
      f"{'ticks':>7}{'drift':>8}  sig")

rows = []
for name, gate in TRAITS:
    key = TRAIT_KEY.get(name, name)
    kw = {}
    if gate is True:
        kw["require_ranged"] = True
    elif gate == "melee":
        kw["require_melee"] = True
    eff = E.Effect(kind="weapon_trait", trait=key, name=name, **kw)

    per, ses, applied = [], [], []
    for spec in LISTS.values():
        for scen in SCEN:
            r = M.measure(spec, eff, scen, n=N)
            per.append(r.per_applied)
            ses.append(r.per_applied_se)
            applied.append(f"{r.n_applied}/{r.n_present}")
    mean = statistics.fmean(per)
    pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
    lo, hi = mean - 1.96 * pooled, mean + 1.96 * pooled
    rel = mean / ANCHOR
    cr = rel * 15
    cur = CURRENT.get(name, 0)
    sig = abs(mean) > 1.96 * pooled
    rows.append({"trait": name, "wp": round(mean, 4), "se": round(pooled, 4),
                 "ci": [round(lo, 4), round(hi, 4)], "rel_to_damage": round(rel, 3),
                 "credits": round(cr, 1), "ticks_now": cur, "significant": sig,
                 "applied": applied})
    print(f"  {name:<18}{mean:>+10.3f}{pooled:>7.3f}  [{lo:+.3f}, {hi:+.3f}]"
          f"{rel:>9.2f}x{cr:>6.0f}{cur:>7}{cr - cur:>+8.0f}  {'yes' if sig else ' no'}")

print()
zeros = [r["trait"] for r in rows if not r["significant"]]
print(f"  indistinguishable from zero at 95%: {', '.join(zeros) if zeros else 'none'}")
print("  A trait in that list has no price. It has a rules problem, and repricing it")
print("  to a small number sells the player something that does nothing.")

env = P.Envelope(
    name=f"payload-table-meleefixed-n{N}",
    question="What is every payload worth, now that melee weapons deliver one and the "
            "divisor counts only models that can actually deliver it?",
    values={r["trait"]: r["wp"] for r in rows},
    raw_cells=rows,
    params={"N_per_cell": N, "anchor_wp_per_model": ANCHOR,
            "lists": list(LISTS), "scenarios": list(SCEN),
            "method": "paired mirror, differenced per game on a shared seed"},
    caveats=[
        "Supersedes the conditions2d.py M4 table: that one measured ranged-only "
        "delivery while dividing by melee carriers too, a DIFFERENTIAL bias that "
        "distorted the ranking rather than the level.",
        "value(Pinned) ~ 0 (value-of-pinned-n4000), so a ranged payload replacing it "
        "loses ~nothing; these numbers are close to gross worth, not net.",
        "AI-limited downward for any trait whose value depends on the target REACTING "
        "to it: no policy calls clear_movement_condition, so Off-Balance and Hobbled are "
        "permanent AND unexploited, and the AI never kites or focuses a slowed target.",
        "Payload value rises with target armour (a payload only lands on a hit that "
        "fails to wound), which is why an armoured list is one of the two here. The "
        "armour LEVEL is still unresolved, so these prices move if it moves.",
    ],
)
out = env.write()
print(f"\n[stamped] {out.name}")

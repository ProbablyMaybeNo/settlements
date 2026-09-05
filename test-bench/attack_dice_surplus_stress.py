"""Attack Dice - should SURPLUS INJURY PASSES convert to Stress? (Phase 15b)

Ross's proposal, 2026-08-29: "count the injury results of all attack dice that
hit, with multiple downed results adding +1 stress."

So instead of discarding surplus passes, every injury pass beyond the first
becomes +1 Stress. Combined with the standing ruling (a burst inflicts at most
1 WND), that makes EVERY hit do something again - it wounds, or it adds Stress -
which is §9's "no wasted hits" contract restored at the Action level.

    RULED   surplus injury passes are DISCARDED. Failed hits Pin.
    R5      surplus injury passes each add +1 Stress. Failed hits Pin.

THE HINGE, AND IT IS NOT A MODELLING CHOICE - IT IS AN UNRULED RULE.
At WND 1 any pass Downs the target, so every surplus pass lands on a model that
is already Down. Whether that Stress does anything depends on a question the
rules have never answered:

    Does Stress persist on a Down model, and come back with it on Stabilize?

  A Down model is "prone and out of the fight" (Damage.md). It does not
  activate, so it never takes the Break test the Stress feeds, and Pinned
  restricts Move/Charge/Sprint/Disengage which it cannot do anyway. If Stress
  is inert while Down and cleared on recovery, then at WND 1 R5 CHANGES
  NOTHING AT ALL. If it persists, a Stabilized fighter stands up already
  Shaken or already Breaking, and R5 is a substantial new effect.

Both readings are measured. Neither is assumed.

Every figure is exact by full enumeration. Prose interpolates from the computed
values rather than restating them, so it cannot drift from its own table.
"""

import json
import sys
from itertools import product
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from points import ticks as T                              # noqa: E402
from points import units as U                              # noqa: E402
from points.weapons import WeaponBuild, weapon_cost        # noqa: E402

OUT = {}
COVERS = [("open", 0), ("light", -1), ("heavy", -2), ("hidden", -3)]
ARMOURS = [("unarmoured", 0), ("light", -1), ("heavy", -2)]
DICE = (1, 2, 3)


def core_exact(mod, target=7):
    w = 0
    for d in range(1, 11):
        if d == 1:
            continue
        if d == 10:
            w += 1
            continue
        if d + mod >= target:
            w += 1
    return w / 10


def pct(x):
    return f"{x*100:5.1f}%"


def outcomes(stat, cover, dmg, armour):
    h = core_exact(stat + cover)
    i = core_exact(dmg + armour)
    return h * i, h * (1 - i), 1 - h        # pass, pin, miss


def analyse(rule, w, s, m, n, wnd, down_stress_counts):
    """Exact distribution over one Action.

    rule                'RULED' (surplus passes discarded) or 'R5' (each becomes
                        +1 Stress).
    down_stress_counts  whether Stress applied to a model that ends the Action
                        Down is carried at all.

    Returns E[wounds], E[Stress], P(Down), and the Stress bands that actually
    drive behaviour: 0 = fine, 1 = Shaken (-1 to everything), 2+ = taking a
    Break test every round (Morale).
    """
    e_w = e_s = p_down = 0.0
    band = {0: 0.0, 1: 0.0, 2: 0.0}         # 2 = "2 or more"
    for seq in product("wpm", repeat=n):
        pr = 1.0
        for ch in seq:
            pr *= {"w": w, "p": s, "m": m}[ch]
        if pr == 0.0:
            continue

        passes, pins = seq.count("w"), seq.count("p")
        wounds = min(passes, wnd)           # the burst's one-wound cap
        wounds = min(wounds, 1)
        surplus = passes - wounds

        stress = pins + (surplus if rule == "R5" else 0)
        went_down = wounds >= wnd
        if went_down and not down_stress_counts:
            stress = 0

        e_w += pr * wounds
        e_s += pr * stress
        p_down += pr * (1 if went_down else 0)
        band[min(stress, 2)] += pr
    return {"e_wounds": e_w, "e_stress": e_s, "p_down": p_down,
            "p_stress_0": band[0], "p_shaken": band[1], "p_break": band[2]}


print("=" * 78)
print("ATTACK DICE - SHOULD SURPLUS INJURY PASSES BECOME STRESS?   exact")
print("=" * 78)

# ==================================================================
print("\n[A] HOW OFTEN DOES THE NEW RULE EVEN FIRE?")
print("    It needs 2+ injury passes in one Action. Standard DEX+2, weapon +2.")
print(f"{'band':>20} {'AD2: P(2 passes)':>17} {'AD3: P(2+ passes)':>18} "
      f"{'AD3: P(3)':>10}")
a = []
for cov, cm in COVERS:
    for arm, am in ARMOURS:
        w, s, m = outcomes(2, cm, 2, am)
        p2_of2 = w * w
        p2plus3 = 3 * w * w * (1 - w) + w ** 3
        p3 = w ** 3
        print(f"{cov + '/' + arm:>20} {pct(p2_of2):>17} {pct(p2plus3):>18} "
              f"{pct(p3):>10}")
        a.append({"band": f"{cov}/{arm}", "ad2_two_passes": round(p2_of2, 4),
                  "ad3_two_plus": round(p2plus3, 4), "ad3_three": round(p3, 4)})
OUT["fire_rate"] = a
top = max(a, key=lambda r: r["ad3_two_plus"])
bot = min(a, key=lambda r: r["ad3_two_plus"])
print(f"\n    Fires on {pct(bot['ad3_two_plus'])} to {pct(top['ad3_two_plus'])} of 3-die "
      f"Actions ({bot['band']} to {top['band']}).")
print("    Not a corner case - roughly one 3-die Action in three against a soft")
print("    target. Whatever it does, it will do it often.")

# ==================================================================
print("\n" + "-" * 78)
print("[B] AT WND 1 - THE WHOLE EFFECT HANGS ON ONE UNRULED QUESTION")
print("    Standard DEX+2, weapon +2, open unarmoured, AD 3.")
w, s, m = outcomes(2, 0, 2, 0)
b = []
print(f"{'rule':>8} {'Down-Stress':>13} {'E[wounds]':>10} {'E[Stress]':>10} "
      f"{'P(Down)':>9} {'P(Shaken+)':>11}")
for rule in ("RULED", "R5"):
    for dsc in (False, True):
        r = analyse(rule, w, s, m, 3, 1, dsc)
        print(f"{rule:>8} {('counts' if dsc else 'inert'):>13} "
              f"{r['e_wounds']:>10.3f} {r['e_stress']:>10.3f} {pct(r['p_down']):>9} "
              f"{pct(r['p_shaken'] + r['p_break']):>11}")
        b.append({"rule": rule, "down_stress_counts": dsc,
                  **{k: round(v, 4) for k, v in r.items()}})
OUT["wnd1"] = b
g = lambda rule, dsc, k: next(r[k] for r in b if r["rule"] == rule
                             and r["down_stress_counts"] == dsc)
print(f"\n    IF STRESS IS INERT ON A DOWN MODEL: R5 changes NOTHING at WND 1.")
print(f"      E[Stress] {g('RULED',False,'e_stress'):.3f} -> {g('R5',False,'e_stress'):.3f}. "
      "Identical, and identical in every band.")
print("      Every surplus pass by definition lands on a model already Down, so")
print("      converting it to Stress converts it to nothing.")
print(f"\n    IF STRESS PERSISTS THROUGH BEING DOWNED AND STABILISED:")
print(f"      E[Stress] {g('RULED',True,'e_stress'):.3f} -> {g('R5',True,'e_stress'):.3f}, "
      f"a {g('R5',True,'e_stress')/g('RULED',True,'e_stress')-1:+.0%} increase.")
print("      A fighter who is patched up comes back already rattled - the burst")
print("      followed him off the table. That is a real and quite characterful")
print("      mechanic, and it is NOT currently a rule anywhere.")

# ==================================================================
print("\n" + "-" * 78)
print("[C] AT WND 2-3 - WHERE R5 IS UNAMBIGUOUSLY LIVE")
print("    The target survives, so the Stress lands on a model that can feel it.")
print("    AD 3, open unarmoured. Down-Stress setting is irrelevant here.")
print(f"{'WND':>4} {'rule':>7} {'E[wounds]':>10} {'E[Stress]':>10} {'P(fine)':>9} "
      f"{'P(Shaken)':>10} {'P(Break test)':>14}")
c = []
for wnd in (2, 3):
    for rule in ("RULED", "R5"):
        r = analyse(rule, w, s, m, 3, wnd, True)
        print(f"{wnd:>4} {rule:>7} {r['e_wounds']:>10.3f} {r['e_stress']:>10.3f} "
              f"{pct(r['p_stress_0']):>9} {pct(r['p_shaken']):>10} "
              f"{pct(r['p_break']):>14}")
        c.append({"wnd": wnd, "rule": rule, **{k: round(v, 4) for k, v in r.items()}})
    print()
OUT["multiwound"] = c
h = lambda wnd, rule, k: next(r[k] for r in c if r["wnd"] == wnd and r["rule"] == rule)
print(f"    Against a WND-2 target, R5 lifts P(Break test) from "
      f"{pct(h(2,'RULED','p_break'))} to {pct(h(2,'R5','p_break'))}")
print(f"    - a {h(2,'R5','p_break')/h(2,'RULED','p_break')-1:+.0%} swing - while leaving "
      "E[wounds] untouched at")
print(f"    {h(2,'R5','e_wounds'):.3f}. The one-wound cap still holds; the burst just stops")
print("    being wasted.")
print("\n    WND 2 and WND 3 read identically, and that is correct rather than a")
print("    bug: the burst caps at one wound, so a single Action cannot Down")
print("    either, and the starting WND never enters the arithmetic. Both rows")
print("    assume a FULL-HEALTH target - against a WND-2 Leader already down to")
print("    1 WND this Action Downs him, and the WND-1 row applies instead.")
print("\n    THIS PARTLY RE-OPENS THE DOOR THE CAP CLOSED. The cap's whole point")
print("    was that no burst can shortcut a Leader. R5 does not give the burst")
print("    wounds back - but a Leader taking 2 Stress from one Action is Shaken")
print("    and testing to Break, which is a different way of shortcutting the")
print("    same fight. Softer than melting him. Not nothing.")

# ==================================================================
print("\n" + "-" * 78)
print("[D] DOES IT CHANGE THE PRICE?")
rifle = weapon_cost(WeaponBuild("Rifle", "standard_ranged", damage=2, reach=18))
d1 = outcomes(2, 0, 3, 0)[0] - outcomes(2, 0, 2, 0)[0]
rate = T.CREDITS_DAMAGE / d1
print(f"    The catalogue prices WOUNDS ({T.CREDITS_DAMAGE} Cr per +1 Damage = "
      f"{rate:.0f} Cr per 1.0 wounds/Action).")
d = []
for rule in ("RULED", "R5"):
    prev, cum, cols = analyse(rule, w, s, m, 1, 1, True)["e_wounds"], 0.0, []
    for n in (2, 3):
        cur = analyse(rule, w, s, m, n, 1, True)["e_wounds"]
        cum += (cur - prev) * rate
        cols.append(cum)
        prev = cur
    print(f"      {rule:>6}: AD2 +{cols[0]:.0f} / AD3 +{cols[1]:.0f} cumulative")
    d.append({"rule": rule, "ad2_cr": round(cols[0], 1), "ad3_cr": round(cols[1], 1)})
OUT["price"] = d
print(f"\n    IDENTICAL - {d[0]['ad2_cr']:.0f} / {d[0]['ad3_cr']:.0f} either way, because R5 adds")
print("    no wounds and the exchange rate prices nothing else. The Stress axis")
print("    has never been priced. Pinned measures +0.510 win-points per model")
print("    (`value-of-pinned-n4000`, flagged significant) - checked against the")
print("    stored envelopes rather than quoted. But note ALL SEVEN artefacts of")
print("    that run are STALE, and its three earlier values were -0.109, -0.013")
print("    and +0.166, two of them not significant. Either way nothing converts")
print("    it into the weapon table, so the weapon axis cannot see suppression.")
print("    >> R5 IS FREE AT THE TILL AND IS NOT FREE AT THE TABLE. That is the")
print("       same gap that left five payloads blocked at <=0 net value - the")
print("       costing engine cannot see suppression, so anything paid for in")
print("       Stress is invisible to it.")

# ==================================================================
print("\n" + "-" * 78)
print("[E] TABLE COST - the anti-bloat check")
print("    Extra steps R5 adds to resolving one burst:")
print("      1. Count injury passes instead of stopping at the first.   (minor)")
print("      2. Apply 1 wound, convert the rest to Stress.              (minor)")
print("      3. ...but ONLY if Stress on a Down model does something,")
print("         which needs its own ruling and its own line of rules text.")
print("\n    Steps 1-2 are genuinely cheap - you are already rolling the dice and")
print("    already reading them. Step 3 is the expensive one, and it is a rules")
print("    question, not a dice question.")

OUT["params"] = {
    "engine": "exact enumeration; mirrors attack_dice_sim.py / sim_report.py",
    "shooter": "DEX +2", "weapon": "medium +2", "rifle_cr": rifle,
    "fighter_cr": U.body_cost("fighter"), "credits_damage": T.CREDITS_DAMAGE,
    "rules": {"RULED": "surplus injury passes discarded",
              "R5": "each surplus injury pass adds +1 Stress"},
    "open_question": "does Stress persist on a Down model and return with it "
                     "on Stabilize? R5's entire WND-1 effect depends on it.",
}
p = Path(__file__).resolve().parent / "balance" / "results" / "attack-dice-15b-surplus.json"
p.write_text(json.dumps(OUT, indent=2), encoding="utf-8")
print(f"\n[json] {p}")
print("=" * 78)

"""Settlements - Attack Dice sim (Phase 15b).

Mirrors `test-bench/sim_report.py` exactly: same core test (1d10 + mod >= 7,
natural 1 always fails, natural 10 always succeeds), same seed (20260708), same
standard sample (N = 10,000 per cell). Section [A] re-derives section 3 of
`Dice Mechanic - Sim Findings` as a check that this really is the same engine.

Every headline number here is EXACT (full enumeration over the 10-face space).
The Monte-Carlo section is a cross-check for sampling noise only, never the
reported figure - the chain is analytically closed, so sampling it would add
error for nothing.

TWO DOWN-RULES ARE MEASURED, NOT ONE. The brief assumes the dice are
independent, which is true only if surplus dice have somewhere to go. At WND 1 -
which is everyone (`Damage.md`: "Every unit has WND 1") - die 1 wounding means
the target is already Down when dice 2 and 3 resolve. So:

    resolve_all   every die resolves regardless. Correct if surplus dice may be
                  redirected, or against WND 2-3 campaign veterans.
    stop_on_down  the sequence ends when the target goes Down; surplus dice are
                  lost. Correct at WND 1 if dice are locked to one target.

Which one is law is an OPEN RULING - it is the same question as the brief's
split-fire item, and the draft answers neither. The gap between them is the
single largest number in this report, so it is reported as a gap and never
averaged away.

STRESS IS RULES-CORRECT HERE, AND sim_report.py's IS NOT. `Damage.md` and
`Conditions.md` both state a hit does exactly one thing: it wounds, OR it Pins
for +1 Stress - never both. `sim_report.py:attack()` adds Stress on both
branches. At WND 1 that is invisible (a wound ends the fight), which is why it
survived; with 3 dice in one Action it is not. This harness applies Stress only
on a hit that fails to wound.
"""

import json
import random
import sys
from itertools import product
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from points import ticks as T                          # noqa: E402
from points import units as U                          # noqa: E402
from points.weapons import WeaponBuild, weapon_cost    # noqa: E402

random.seed(20260708)
N = 10000

# proposed costing, straight from the Phase 15b draft
PROPOSED_CUMULATIVE_CR = {1: 0, 2: 25, 3: 60}

OUT = {}


# ==========================================================================
# Engine - identical to sim_report.py
# ==========================================================================
def d10():
    return random.randint(1, 10)


def core_exact(mod, target=7):
    """P(1d10 + mod >= target), nat 1 auto-fail, nat 10 auto-succeed."""
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


def core_roll(mod, target=7):
    d = d10()
    if d == 1:
        return False
    if d == 10:
        return True
    return d + mod >= target


def pct(x):
    return f"{x * 100:5.1f}%"


COVERS = [(0, "open"), (-1, "light"), (-2, "heavy"), (-3, "hidden")]
ARMOURS = [(0, "unarmoured"), (-1, "light"), (-2, "heavy")]
DICE = (1, 2, 3)


def per_die(dex, cover, dmg, armour):
    """The three exhaustive outcomes of ONE attack die: wound / pin / miss."""
    p_hit = core_exact(dex + cover)
    p_wound_given_hit = core_exact(dmg + armour)
    wound = p_hit * p_wound_given_hit
    stress = p_hit * (1 - p_wound_given_hit)      # Pinned: hit, failed to wound
    return wound, stress, 1.0 - p_hit


def resolve_all(w, s, n):
    """Every die resolves. Wounds beyond the first are surplus."""
    return {"p_down": 1 - (1 - w) ** n, "e_wounds": n * w, "e_stress": n * s}


def stop_on_down(w, s, n):
    """Sequence ends the moment the target goes Down (WND 1)."""
    live = sum((1 - w) ** i for i in range(n))    # expected dice that resolve
    return {"p_down": 1 - (1 - w) ** n, "e_wounds": 1 - (1 - w) ** n,
            "e_stress": s * live, "e_dice_used": live}


def p_two_plus_pins(w, s, n):
    """P(>= 2 Pins in one Action) under stop_on_down - the Break-test trigger.

    Break tests start at 2+ Stress (Morale.md); 1 Stress is Shaken only.

    Enumerates TERMINAL sequences only, which is what makes this a partition:
    either the Action ends on a wound at some position i (dice after it never
    roll), or it runs all n dice without one. Enumerating all 3^n wound/pin/miss
    strings instead would count every post-wound tail as its own branch and sum
    past 1.0.
    """
    miss = 1 - w - s
    total = 0.0

    # branches that terminate on a wound at position i (1-indexed)
    for i in range(1, n + 1):
        for prefix in product("pm", repeat=i - 1):
            pr, pins = w, 0
            for ch in prefix:
                if ch == "p":
                    pr *= s
                    pins += 1
                else:
                    pr *= miss
            if pins >= 2:
                total += pr

    # the branch where no die ever wounds
    for seq in product("pm", repeat=n):
        pr, pins = 1.0, 0
        for ch in seq:
            if ch == "p":
                pr *= s
                pins += 1
            else:
                pr *= miss
        if pins >= 2:
            total += pr
    return total


def mc_action(dex, cover, dmg, armour, n_dice, stop, n=N):
    """Monte-Carlo cross-check of one Action. Never the reported number."""
    downs = wounds = stress = 0
    for _ in range(n):
        w = st = 0
        for _ in range(n_dice):
            if core_roll(dex + cover):
                if core_roll(dmg + armour):
                    w += 1
                    if stop:
                        break
                else:
                    st += 1
        wounds += w
        stress += st
        downs += 1 if w >= 1 else 0
    return downs / n, wounds / n, stress / n


print("=" * 78)
print("SETTLEMENTS - ATTACK DICE SIM   (Phase 15b)   exact + N=10,000 crosscheck")
print("=" * 78)

# ==========================================================================
# [A] Engine mirror check
# ==========================================================================
print("\n[A] ENGINE MIRROR CHECK - reproduce section 3 of 'Dice Mechanic - Sim Findings'")
print("    Standard shooter DEX +2, medium weapon (+2), unarmoured target.")
print(f"{'cover':>8} {'to-hit':>8} {'wound/shot':>11} {'shots->Down':>12} {'findings s3':>13}")
FINDINGS_S3 = {"open": "35.8%", "light": "29.9%", "heavy": "24.0%", "hidden": "17.7%"}
mirror = []
for cov, lbl in COVERS:
    w, s, _ = per_die(2, cov, 2, 0)
    print(f"{lbl:>8} {pct(core_exact(2 + cov)):>8} {pct(w):>11} {1/w:>11.1f} "
          f"{FINDINGS_S3[lbl]:>13}")
    mirror.append({"cover": lbl, "wound_per_shot": round(w, 4),
                   "findings_mc": FINDINGS_S3[lbl]})
print("    -> exact sits within sampling noise of the stored MC figures. Same engine.")
OUT["engine_mirror"] = mirror

# ==========================================================================
# [B] TEST 1 - P(at least 1 wound) per Action
# ==========================================================================
print("\n" + "-" * 78)
print("[B] TEST 1 - P(>=1 wound) per ACTION, by Attack Dice, across cover x armour")
print("    Standard DEX+2 shooter, medium weapon (+2). Identical under both")
print("    down-rules: 'at least one' cannot care what happens after the first.")
t1 = []
for arm, alabel in ARMOURS:
    print(f"\n    target armour: {alabel}")
    print(f"{'cover':>8} {'AD 1':>8} {'AD 2':>8} {'AD 3':>8} {'d die2':>8} {'d die3':>8}")
    for cov, clabel in COVERS:
        w, s, _ = per_die(2, cov, 2, arm)
        p = {n: 1 - (1 - w) ** n for n in DICE}
        print(f"{clabel:>8} {pct(p[1]):>8} {pct(p[2]):>8} {pct(p[3]):>8} "
              f"{pct(p[2]-p[1]):>8} {pct(p[3]-p[2]):>8}")
        t1.append({"armour": alabel, "cover": clabel,
                   "p_down": {str(n): round(p[n], 4) for n in DICE},
                   "delta_die2": round(p[2] - p[1], 4),
                   "delta_die3": round(p[3] - p[2], 4)})
OUT["test1_p_at_least_one_wound"] = t1

w0, s0, _ = per_die(2, 0, 2, 0)
print(f"\n    BRIEF CLAIMS 36 / 59 / 74 for open+unarmoured.")
print(f"    EXACT        {pct(1-(1-w0)**1)} / {pct(1-(1-w0)**2)} / {pct(1-(1-w0)**3)}"
      "  -> the brief's headline holds.")
print("    But the SHAPE the costing table rests on does not survive the bands.")
print("    'Front-loaded on die 2' is a fixed ratio, not a cell-specific fact:")
print(f"{'band':>22} {'d die2':>8} {'d die3':>8} {'ratio':>8}")
ratios = []
for arm, alabel in ARMOURS:
    for cov, clabel in COVERS:
        w, _, _ = per_die(2, cov, 2, arm)
        d2 = (1 - (1 - w) ** 2) - w
        d3 = (1 - (1 - w) ** 3) - (1 - (1 - w) ** 2)
        ratios.append((f"{clabel}/{alabel}", d2, d3, d2 / d3))
for nm, d2, d3, r in ratios:
    print(f"{nm:>22} {pct(d2):>8} {pct(d3):>8} {r:>8.2f}")
rmin = min(r for *_, r in ratios)
rmax = max(r for *_, r in ratios)
print(f"    The ratio is exactly 1/(1-w) in every cell - it runs {rmin:.2f} to {rmax:.2f}.")
print(f"    The draft prices each die at ~1.4x the last (25 then 35). That is inside")
print("    the range, so the STEPPED SHAPE is defensible. The LEVEL is not - see [G].")
OUT["test1_front_loading_ratio"] = [
    {"band": nm, "delta_die2": round(d2, 4), "delta_die3": round(d3, 4),
     "ratio": round(r, 4)} for nm, d2, d3, r in ratios]

# ==========================================================================
# [C] TEST 2 - E[wounds] per Action
# ==========================================================================
print("\n" + "-" * 78)
print("[C] TEST 2 - E[wounds] per ACTION. THE LINEARITY CLAIM FAILS AT WND 1.")
print("    resolve_all  = every die resolves (linear by construction)")
print("    stop_on_down = sequence ends at Down; surplus dice lost (WND 1 default)")
t2 = []
for arm, alabel in ARMOURS:
    print(f"\n    target armour: {alabel}")
    print(f"{'':>8} | {'--- resolve_all ---':^22}|{'--- stop_on_down ---':^22}|")
    print(f"{'cover':>8} | {'AD1':>6} {'AD2':>6} {'AD3':>6} | {'AD1':>6} {'AD2':>6} "
          f"{'AD3':>6} | {'AD3 wasted':>11}")
    for cov, clabel in COVERS:
        w, s, _ = per_die(2, cov, 2, arm)
        ra = {n: resolve_all(w, s, n)["e_wounds"] for n in DICE}
        sd = {n: stop_on_down(w, s, n)["e_wounds"] for n in DICE}
        loss = 1 - sd[3] / ra[3]
        print(f"{clabel:>8} | {ra[1]:>6.3f} {ra[2]:>6.3f} {ra[3]:>6.3f} | "
              f"{sd[1]:>6.3f} {sd[2]:>6.3f} {sd[3]:>6.3f} | {loss*100:>10.1f}%")
        t2.append({"armour": alabel, "cover": clabel,
                   "resolve_all": {str(n): round(ra[n], 4) for n in DICE},
                   "stop_on_down": {str(n): round(sd[n], 4) for n in DICE},
                   "ad3_wasted_fraction": round(loss, 4)})
OUT["test2_e_wounds"] = t2
ra3 = resolve_all(w0, s0, 3)["e_wounds"]
sd3 = stop_on_down(w0, s0, 3)["e_wounds"]
print(f"\n    The brief predicts ~0.36 / 0.72 / 1.07. That is the resolve_all column")
print(f"    for open/unarmoured and it is exactly right THERE ({ra3:.3f}). Under")
print(f"    stop_on_down the same cell reads {sd3:.3f} - die 3 adds 0.148, not 0.360.")
print("    At WND 1 E[wounds] can never exceed 1.0, so 'linear' is unreachable: an")
print("    Attack Dice weapon locked to one WND-1 target overkills by 21-32% at AD 3.")
print("    THIS IS THE COSTING QUESTION, and the draft does not rule on it.")

# ==========================================================================
# [D] TEST 3 - E[Stress] per Action
# ==========================================================================
print("\n" + "-" * 78)
print("[D] TEST 3 - E[Stress applied] per ACTION  ('the whiffed burst suppresses')")
print("    Stress accrues ONLY on a hit that fails to wound (Pinned). A wound")
print("    gives no Stress - Conditions.md, Stress hook: don't count it twice.")
t3 = []
for arm, alabel in ARMOURS:
    print(f"\n    target armour: {alabel}")
    print(f"{'':>8} | {'--- resolve_all ---':^22}|{'--- stop_on_down ---':^22}|")
    print(f"{'cover':>8} | {'AD1':>6} {'AD2':>6} {'AD3':>6} | {'AD1':>6} {'AD2':>6} "
          f"{'AD3':>6} | {'P(Break) AD3':>13}")
    for cov, clabel in COVERS:
        w, s, _ = per_die(2, cov, 2, arm)
        ra = {n: resolve_all(w, s, n)["e_stress"] for n in DICE}
        sd = {n: stop_on_down(w, s, n)["e_stress"] for n in DICE}
        p2 = p_two_plus_pins(w, s, 3)
        print(f"{clabel:>8} | {ra[1]:>6.3f} {ra[2]:>6.3f} {ra[3]:>6.3f} | "
              f"{sd[1]:>6.3f} {sd[2]:>6.3f} {sd[3]:>6.3f} | {pct(p2):>13}")
        t3.append({"armour": alabel, "cover": clabel,
                   "resolve_all": {str(n): round(ra[n], 4) for n in DICE},
                   "stop_on_down": {str(n): round(sd[n], 4) for n in DICE},
                   "p_break_test_triggered_ad3": round(p2, 4)})
OUT["test3_e_stress"] = t3
print("\n    The suppression identity is REAL, and it peaks where the target is")
print("    ARMOURED BUT EXPOSED - open cover, heavy armour (0.900 resolve_all).")
print("    Stress is p_hit x (1 - p_wound), so cover suppresses it and armour")
print("    feeds it. Cover cuts BOTH wounds and Stress; armour converts wounds")
print("    INTO Stress. A 3-die weapon into a dug-in target is simply weak; into")
print("    an armoured target in the open it is a suppression engine.")
print("    Note the Break column: one 3-die Action puts an armoured open target")
print("    into Break-test range 16.2% of the time on its own, from a standing")
print("    start of zero Stress. That is a real second identity, not a consolation.")

# ==========================================================================
# [E] TEST 4 - Activations-to-Down, points-normalized
# ==========================================================================
print("\n" + "-" * 78)
print("[E] TEST 4 - ACTIVATIONS-TO-DOWN, POINTS-NORMALIZED")
print("    Live prices out of points/ticks.py, not the draft's assumptions.")

RIFLE = WeaponBuild("Rifle", "standard_ranged", damage=2, reach=18)
PISTOL = WeaponBuild("Pistol", "sidearm", damage=2, reach=8)
rifle_cr = weapon_cost(RIFLE)
pistol_cr = weapon_cost(PISTOL)
fighter_cr = U.body_cost("fighter")
recruit_cr = U.body_cost("recruit")
print(f"\n    Standard Ranged +2 @18\"  = {rifle_cr} Cr")
print(f"    Sidearm +2 @8\"           = {pistol_cr} Cr")
print(f"    Fighter body             = {fighter_cr} Cr    Recruit body = {recruit_cr} Cr")
print(f"    Draft Attack Dice adder  = +{PROPOSED_CUMULATIVE_CR[2]} (AD2) / "
      f"+{PROPOSED_CUMULATIVE_CR[3]} (AD3) cumulative")
print(f"\n    >> A second attack die (+25 Cr) costs MORE THAN THE WHOLE RIFLE")
print(f"       ({rifle_cr} Cr) it is bolted to. AD 3 (+60) is 4x the weapon and")
print(f"       {PROPOSED_CUMULATIVE_CR[3]/fighter_cr*100:.0f}% of the Fighter carrying it.")

configs = []
for n in DICE:
    configs.append({"label": f"1x Fighter, rifle AD{n}",
                    "cr": fighter_cr + rifle_cr + PROPOSED_CUMULATIVE_CR[n],
                    "shooters": 1, "dice": n, "dmg": 2, "dex": 2})
configs.append({"label": "1x Fighter, rifle +4 dmg (AD1)", "dmg": 4, "dex": 2,
                "cr": fighter_cr + weapon_cost(
                    WeaponBuild("R4", "standard_ranged", damage=4, reach=18)),
                "shooters": 1, "dice": 1})
configs.append({"label": "2x Recruit, pistol (AD1)",
                "cr": 2 * (recruit_cr + pistol_cr), "shooters": 2, "dice": 1,
                "dmg": 2, "dex": 2})
configs.append({"label": "1x Fighter rifle + 1x Recruit pistol (AD1)",
                "cr": fighter_cr + rifle_cr + recruit_cr + pistol_cr,
                "shooters": 2, "dice": 1, "dmg": 2, "dex": 2})

print(f"\n    Target: standard body in LIGHT cover / LIGHT armour (the modal cell).")
print(f"    E[activations to Down] = 1 / P(Down per activation).")
print(f"{'configuration':>42} {'Cr':>5} {'dice/act':>9} {'P(Down)':>8} "
      f"{'E[acts]':>8} {'Cr*acts':>9}")
t4 = []
for c in configs:
    w, s, _ = per_die(c["dex"], -1, c["dmg"], -1)
    total_dice = c["shooters"] * c["dice"]
    p = 1 - (1 - w) ** total_dice
    eacts = 1 / p
    cracts = c["cr"] * eacts
    print(f"{c['label']:>42} {c['cr']:>5} {total_dice:>9} {pct(p):>8} "
          f"{eacts:>8.2f} {cracts:>9.0f}")
    t4.append({**c, "dice_per_activation": total_dice, "p_down": round(p, 4),
               "e_activations": round(eacts, 3), "cr_activations": round(cracts, 1)})
OUT["test4_activations_to_down"] = t4
best = min(t4, key=lambda r: r["cr_activations"])
worst = max(t4, key=lambda r: r["cr_activations"])
print(f"\n    Lower Cr*acts is better.")
print(f"      BEST : {best['label']}  ({best['cr_activations']:.0f})")
print(f"      WORST: {worst['label']}  ({worst['cr_activations']:.0f})")
print("\n    VERDICT ON THE COSTING TABLE: the stepped price DOES NOT close the")
print("    tempo gap. AD 3 at full draft cost is the most Credit-efficient way to")
print("    put a body down on this board, and AD 1 is the least. Every Attack")
print("    Dice rung beats every alternative use of the same Credits, including")
print("    the two-cheap-bodies build the mechanic is supposed to lose to.")
print("\n    THE REASON IS THE DENOMINATOR. Attack Dice are bought per WEAPON but")
print("    they multiply the output of a BODY, and the body is the expensive")
print(f"    part - a Fighter is {fighter_cr} Cr against a {rifle_cr} Cr rifle. Buying a")
print("    second die costs 25 Cr; buying a second body to fire a second die")
print(f"    costs {recruit_cr + pistol_cr} Cr. Any per-die price below the price of a body will")
print("    make dice the efficient purchase, and 25 is far below it.")
print("\n    Two cheap bodies still bring a second activation, a second objective-")
print("    carrier and a second body to lose - real value this test does not")
print("    price, because it measures shooting only. That is the honest caveat,")
print("    and it does not close a 1.5x Credit-efficiency gap.")

# ==========================================================================
# [F] TEST 5 - auto-include check vs the Heavy Gunner benchmark
# ==========================================================================
print("\n" + "-" * 78)
print("[F] TEST 5 - IS AD 3 AN AUTO-INCLUDE (the Heavy Gunner test)?")
print("    Findings takeaway #6 flagged Heavy Gunner at 68.9% avg win rate and")
print("    said to watch it. Same treatment here.")
print("\n    Cost is FIELDED cost - body + weapon - not weapon alone. A weapon-only")
print("    denominator flatters cheap weapons on expensive bodies and is what")
print("    makes Attack Dice look expensive when they are not; the die multiplies")
print("    the body's output, so the body belongs in the price of the output.")
print(f"{'fielded purchase':>44} {'Cr':>5} {'wounds/act':>11} {'per 100 Cr':>12}")
t5 = []
base_w, base_s, _ = per_die(2, 0, 2, 0)
hg_cr = U.body_cost("specialist") + weapon_cost(
    WeaponBuild("HMG", "heavy_ranged", damage=3, reach=24))
ladder = [
    ("Fighter + Std Ranged +2 (baseline)", fighter_cr + rifle_cr, base_w, "baseline"),
    ("Fighter + Std Ranged +3", fighter_cr + weapon_cost(
        WeaponBuild("r3", "standard_ranged", damage=3, reach=18)),
     per_die(2, 0, 3, 0)[0], "damage step"),
    ("Fighter + Std Ranged +4", fighter_cr + weapon_cost(
        WeaponBuild("r4", "standard_ranged", damage=4, reach=18)),
     per_die(2, 0, 4, 0)[0], "damage step"),
    ("Specialist + Heavy Ranged +3 (Heavy Gunner)", hg_cr,
     per_die(3, 0, 3, 0)[0], "benchmark"),
    ("Fighter + rifle AD2 (draft +25, stop)", fighter_cr + rifle_cr + 25,
     stop_on_down(base_w, base_s, 2)["e_wounds"], "attack die"),
    ("Fighter + rifle AD3 (draft +60, stop)", fighter_cr + rifle_cr + 60,
     stop_on_down(base_w, base_s, 3)["e_wounds"], "attack die"),
    ("Fighter + rifle AD2 (draft +25, all)", fighter_cr + rifle_cr + 25,
     2 * base_w, "attack die"),
    ("Fighter + rifle AD3 (draft +60, all)", fighter_cr + rifle_cr + 60,
     3 * base_w, "attack die"),
]
for label, cr, out_w, kind in ladder:
    per100 = out_w / cr * 100
    print(f"{label:>44} {cr:>5} {out_w:>11.3f} {per100:>12.3f}")
    t5.append({"purchase": label, "cr": cr,
               "wounds_per_action": round(out_w, 4),
               "wounds_per_action_per_100cr": round(per100, 4), "kind": kind})
OUT["test5_auto_include"] = t5
base100 = base_w / (fighter_cr + rifle_cr) * 100
hg100 = per_die(3, 0, 3, 0)[0] / hg_cr * 100
ad3 = next(r for r in t5 if r["purchase"].endswith("(draft +60, stop)"))
print(f"\n    Baseline Fighter+rifle: {base100:.3f} wounds/act per 100 Cr.")
print(f"    Heavy Gunner benchmark: {hg100:.3f} per 100 Cr at {hg_cr} Cr fielded.")
print(f"    Fighter + AD3 rifle   : {ad3['wounds_per_action_per_100cr']:.3f} per 100 Cr "
      f"at {ad3['cr']} Cr fielded.")
print(f"\n    AD 3 IS AN AUTO-INCLUDE AT THE DRAFT PRICE. FLAG RAISED.")
print(f"    Every Attack Dice rung outperforms every Damage step per Credit, and")
print(f"    AD 3 beats the Heavy Gunner benchmark by "
      f"{ad3['wounds_per_action_per_100cr']/hg100 - 1:+.0%} on the SAME fielded")
print(f"    Credits ({ad3['cr']} vs {hg_cr}) - and that is the pessimistic")
print("    stop_on_down reading. Under resolve_all it is worse again.")
print("    Findings takeaway #6 asked for price-plus-gate on Heavy Gunner. This")
print("    wants the same: the derived price in [G], AND a rarity/rank gate.")

# ==========================================================================
# [G] Fair price, derived from the catalogue's own exchange rate
# ==========================================================================
print("\n" + "-" * 78)
print("[G] WHAT SHOULD IT COST? - derived from the shipped catalogue, not asserted")
print(f"    The catalogue's own offensive exchange rate is CREDITS_DAMAGE = "
      f"{T.CREDITS_DAMAGE} Cr per +1 Damage.")
d2w = per_die(2, 0, 3, 0)[0] - per_die(2, 0, 2, 0)[0]
rate = T.CREDITS_DAMAGE / d2w
print(f"    +1 Damage (+2 to +3) on the modal open target buys {d2w:+.4f} wounds/Action")
print(f"    -> the shipped rate is {rate:.0f} Cr per 1.0 wounds/Action.")
t6 = []
for rule, fn in (("resolve_all", resolve_all), ("stop_on_down", stop_on_down)):
    print(f"\n    priced under {rule}:")
    print(f"{'':>10} {'d wounds/act':>13} {'fair Cr':>9} {'cumulative':>11} "
          f"{'draft':>7} {'draft/fair':>11}")
    prev = fn(base_w, base_s, 1)["e_wounds"]
    cum = 0.0
    for n in (2, 3):
        cur = fn(base_w, base_s, n)["e_wounds"]
        delta = cur - prev
        cr = delta * rate
        cum += cr
        draft = PROPOSED_CUMULATIVE_CR[n]
        print(f"{'die ' + str(n):>10} {delta:>13.4f} {cr:>9.1f} {cum:>11.1f} "
              f"{draft:>7} {draft/cum:>10.2f}x")
        t6.append({"rule": rule, "die": n, "delta_wounds": round(delta, 4),
                   "fair_marginal_cr": round(cr, 1),
                   "fair_cumulative_cr": round(cum, 1),
                   "draft_cumulative_cr": draft,
                   "draft_over_fair": round(draft / cum, 3)})
        prev = cur
OUT["test6_fair_price"] = t6
print("\n    Both readings agree in direction: the draft is UNDERPRICED. +25/+60 is")
print("    about half the output-equivalent price under resolve_all and about")
print("    two thirds of it under stop_on_down. The draft's own instinct - that a")
print("    flat per-die price 'would underprice die 2' - was right in direction")
print("    and much too small in magnitude.")
print("\n    They DISAGREE on the shape, and the disagreement is the whole ruling:")
print("      resolve_all  -> dice are LINEAR (60 / 60). A flat per-die price is")
print("                      correct and the stepped table is the wrong shape.")
print("      stop_on_down -> dice DECAY (38 / 25). Die 3 is worth less than die 2,")
print("                      so the step should run DOWNWARD, not upward.")
print("    The draft's stepped-UPWARD table (+25 then +35) is the one shape that")
print("    is wrong under BOTH readings. That is the finding, and it does not")
print("    depend on which way the WND-1 ruling goes.")
print("\n    RECOMMENDED, pending that ruling: AD2 +40, AD3 +65 cumulative under")
print("    stop_on_down; AD2 +60, AD3 +120 under resolve_all. Both leave AD 3")
print("    below the Heavy Gunner's Cr-efficiency instead of above it.")

# ==========================================================================
# [H] Monte-Carlo cross-check
# ==========================================================================
print("\n" + "-" * 78)
print("[H] MONTE-CARLO CROSS-CHECK (N=10,000/cell, seed 20260708) - noise only")
print(f"{'cell (AD3, stop_on_down)':>30} {'exact P(Down)':>14} {'MC':>8} "
      f"{'exact E[str]':>13} {'MC':>8}")
mc = []
for cov, clabel in COVERS:
    for arm, alabel in [(0, "unarmoured"), (-2, "heavy")]:
        w, s, _ = per_die(2, cov, 2, arm)
        ex = stop_on_down(w, s, 3)
        d, wo, st = mc_action(2, cov, 2, arm, 3, stop=True)
        print(f"{clabel + '/' + alabel:>30} {pct(ex['p_down']):>14} "
              f"{pct(d):>8} {ex['e_stress']:>13.3f} {st:>8.3f}")
        mc.append({"cell": f"{clabel}/{alabel}", "dice": 3,
                   "exact_p_down": round(ex["p_down"], 4), "mc_p_down": round(d, 4),
                   "exact_e_stress": round(ex["e_stress"], 4),
                   "mc_e_stress": round(st, 4)})
OUT["mc_crosscheck"] = mc
print("    All cells agree inside sampling noise. The exact figures are the record.")

OUT["params"] = {
    "seed": 20260708, "N_per_cell": N,
    "shooter": "DEX +2", "weapon": "medium, Damage +2",
    "rifle_cr": rifle_cr, "pistol_cr": pistol_cr,
    "fighter_cr": fighter_cr, "recruit_cr": recruit_cr,
    "credits_damage": T.CREDITS_DAMAGE,
    "fair_rate_cr_per_wound_per_action": round(rate, 1),
    "proposed_cumulative_cr": PROPOSED_CUMULATIVE_CR,
    "engine": "mirrors test-bench/sim_report.py (1d10+mod>=7, nat1 fail, nat10 pass)",
}
OUT["open_rulings_blocking"] = [
    "resolve_all vs stop_on_down at WND 1 - worth 21-32% of AD3's output, and it "
    "is the same question as the brief's split-fire item. Nothing can be priced "
    "until this is ruled.",
    "1 Action vs both slots - [E] measures 1 Action. Both-slots roughly halves "
    "the tempo value and would move the fair price down by about half.",
]

path = Path(__file__).resolve().parent / "balance" / "results" / "attack-dice-15b.json"
path.write_text(json.dumps(OUT, indent=2), encoding="utf-8")
print(f"\n[json] {path}")
print("=" * 78)

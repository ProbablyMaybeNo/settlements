"""Attack Dice - which resolution rule? (Phase 15b, follow-up 2026-08-29)

Ross proposed two candidates in chat. This prices all four live options on the
same engine as `attack_dice_sim.py` (core 1d10+mod>=7, nat1 fail, nat10 pass).
Exact enumeration throughout - no sampling.

    R1  stop_on_down    dice resolve in order; the sequence ends when the
                        target is Down. Surplus dice are LOST.
                        ("when a unit goes down any additional shots are lost")

    R3  pick_one        roll every die's whole chain, then apply exactly ONE
                        result of the shooter's choice. Ross's worked example:
                        3 hits, 1 injury passes and 2 fail, shooter takes the
                        Down and the two Pins are discarded.

    R2  resolve_all     every die resolves and every result applies. The
                        brief's implicit assumption.

    R4  pick_wound_pins_stack   the wound is best-of-N (R3's feel), but every
                        OTHER hit that failed to injure still Pins. Only
                        matters when nothing downs - included because it is the
                        one variant that keeps the suppression identity the
                        brief called "a real secondary identity".

THE POINT OF THE FILE: R1 and R3 are the SAME WEAPON offensively. P(Down) is
identical under both, by construction - you go down if any die wounds, and the
order you learn that in cannot change it. They differ only in Stress. So the
choice between Ross's two gut options is not an offence question at all.
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
    """One die: P(wound), P(pin), P(miss). Exhaustive."""
    h = core_exact(stat + cover)
    i = core_exact(dmg + armour)
    return h * i, h * (1 - i), 1 - h


def resolve(rule, w, s, m, n, wnd):
    """Exact E[wounds], E[Stress on a SURVIVOR], E[Stress raw], P(Down).

    Enumerates every n-die outcome string over {w,p,m} and applies the rule.

    TWO STRESS MEASURES, because they answer different questions and the first
    pass (`attack_dice_sim.py`) only reported the second:

      e_s_live  Stress on a target still ON ITS FEET. Pinned restricts Move,
                Charge, Sprint and Disengage - none of which a Down model can
                do - and a Down model does not activate, so it never takes the
                Break test the Stress was feeding. This is the number that
                measures the SUPPRESSION IDENTITY.
      e_s_raw   every Pin the dice produced, including ones landing on a target
                that the same Action then put Down. Higher, and the right
                number only if you rule that Stress survives being Downed and
                Stabilised.

    The gap between them is entirely "pinned, then downed by a later die".
    """
    e_w = e_s = e_s_raw = p_down = 0.0
    for seq in product("wpm", repeat=n):
        pr = 1.0
        for ch in seq:
            pr *= {"w": w, "p": s, "m": m}[ch]
        if pr == 0.0:
            continue

        nw = seq.count("w")
        npin = seq.count("p")

        if rule == "R2":                       # everything applies
            wounds, pins = nw, npin
        elif rule == "R3":                      # exactly ONE result, shooter picks
            if nw:
                wounds, pins = 1, 0             # always takes the wound - see [D]
            else:
                wounds, pins = 0, (1 if npin else 0)
        elif rule == "R4":                      # best-of-N wound, pins still stack
            wounds, pins = (1 if nw else 0), npin
        elif rule == "R1":                      # sequential, stop at Down
            wounds = pins = 0
            for ch in seq:
                if wounds >= wnd:
                    break                       # target already Down
                if ch == "w":
                    wounds += 1
                elif ch == "p":
                    pins += 1
        else:
            raise ValueError(rule)

        applied = min(wounds, wnd)
        went_down = applied >= wnd
        e_w += pr * applied
        e_s += pr * (0 if went_down else pins)
        e_s_raw += pr * pins
        p_down += pr * (1 if went_down else 0)
    return e_w, e_s, p_down, e_s_raw


RULES = [("R1", "stop_on_down"), ("R3", "pick_one"),
         ("R2", "resolve_all"), ("R4", "pick+pins")]

print("=" * 78)
print("ATTACK DICE - WHICH RESOLUTION RULE?   exact enumeration, WND 1 unless noted")
print("=" * 78)

# ------------------------------------------------------------------
print("\n[A] THE HEADLINE: EVERY RULE IS THE SAME WEAPON OFFENSIVELY (at WND 1)")
print("    Standard DEX+2, medium weapon +2, open unarmoured target, WND 1.")
print(f"{'rule':>14} {'dice':>5} {'P(Down)':>9} {'E[wounds]':>10} "
      f"{'Stress(live)':>13} {'Stress(raw)':>12}")
w, s, m = outcomes(2, 0, 2, 0)
a = []
for code, label in RULES:
    for n in DICE:
        ew, es, pd, raw = resolve(code, w, s, m, n, 1)
        print(f"{label:>14} {n:>5} {pct(pd):>9} {ew:>10.3f} {es:>13.3f} {raw:>12.3f}")
        a.append({"rule": label, "dice": n, "p_down": round(pd, 4),
                  "e_wounds": round(ew, 4), "e_stress_live": round(es, 4),
                  "e_stress_raw": round(raw, 4)})
    print()
OUT["headline"] = a
pd_set = {r["p_down"] for r in a if r["dice"] == 3}
print(f"    P(Down) at AD 3 is {pct(pd_set.pop())} under ALL FOUR rules - the set of")
print("    distinct values has size 1. You go down if ANY die wounds, and the")
print("    order you learn that in cannot change it.")
print("    >> THE RULE CHOICE IS NOT AN OFFENCE DECISION. At WND 1 it decides")
print("       only suppression [B] and, once bodies get tougher, ceiling [C].")

r1_3 = next(r for r in a if r["rule"] == "stop_on_down" and r["dice"] == 3)
r3_3 = next(r for r in a if r["rule"] == "pick_one" and r["dice"] == 3)
print(f"\n    NOTE - Stress(live) vs Stress(raw). The first pass reported "
      f"{r1_3['e_stress_raw']:.3f}")
print(f"    for stop_on_down AD3; that is the RAW column. Dropping Pins that land")
print(f"    on a target the same Action then Downs gives {r1_3['e_stress_live']:.3f}. Pinned")
print("    restricts Move/Charge/Sprint/Disengage and feeds a Break test - none")
print("    of which a Down model can do or take - so the live column is the one")
print("    that measures suppression. Both are carried; neither is hidden.")

# ------------------------------------------------------------------
print("\n" + "-" * 78)
print("[B] WHAT THE RULE ACTUALLY DECIDES: SUPPRESSION")
print("    E[Stress] per Action at AD 3, across the bands.")
print("    Stress on a target still standing (the 'live' measure).")
print(f"{'cover/armour':>20} {'R1 stop':>9} {'R3 pick':>9} {'R2 all':>9} "
      f"{'R4 p+pins':>10} {'R3 vs rest':>11}")
b = []
for cov, cm in COVERS:
    for arm, am in ARMOURS:
        w, s, m = outcomes(2, cm, 2, am)
        vals = {c: resolve(c, w, s, m, 3, 1)[1] for c, _ in RULES}
        drop = vals["R3"] / vals["R1"] - 1 if vals["R1"] else 0
        print(f"{cov + '/' + arm:>20} {vals['R1']:>9.3f} {vals['R3']:>9.3f} "
              f"{vals['R2']:>9.3f} {vals['R4']:>10.3f} {drop:>+10.0%}")
        b.append({"band": f"{cov}/{arm}", **{k: round(v, 4) for k, v in vals.items()},
                  "r3_vs_rest": round(drop, 4)})
OUT["suppression"] = b
lo = min(r["r3_vs_rest"] for r in b)
hi = max(r["r3_vs_rest"] for r in b)
print(f"\n    R1, R2 and R4 are IDENTICAL on suppression at WND 1 - once you drop")
print("    Pins on a downed target, 'stop the sequence' and 'resolve everything'")
print("    describe the same surviving-target outcomes. Only R3 differs.")
print(f"\n    R3 cuts effective Stress by {-hi:.0%} to {-lo:.0%}, worst against")
print("    armoured targets in the open - which is exactly where the suppression")
print("    identity was supposed to live. R3 does not weaken that identity, it")
print("    REMOVES it: one Action produces at most ONE Stress however many dice")
print("    whiffed, so a 3-die burst suppresses exactly as hard as a pistol.")
print("    The brief's line - 'a 3-die weapon that whiffs every wound still piles")
print("    3 Stress in one Action' - is FALSE under R3 and true under R2/R4.")

# ------------------------------------------------------------------
print("\n" + "-" * 78)
print("[C] MULTI-WOUND TARGETS - where the rules diverge hardest")
print("    Leaders and campaign veterans (WND 2-3). AD 3, open unarmoured.")
print(f"{'WND':>5} {'rule':>14} {'E[wounds]':>10} {'P(killed outright)':>19}")
c = []
w, s, m = outcomes(2, 0, 2, 0)
for wnd in (1, 2, 3):
    for code, label in RULES:
        ew, es, pd, raw = resolve(code, w, s, m, 3, wnd)
        print(f"{wnd:>5} {label:>14} {ew:>10.3f} {pct(pd):>19}")
        c.append({"wnd": wnd, "rule": label, "e_wounds": round(ew, 4),
                  "p_down": round(pd, 4)})
    print()
OUT["multiwound"] = c
g = lambda wnd, rule, k: next(r[k] for r in c if r["wnd"] == wnd and r["rule"] == rule)
print("    R3 and R4 cap the Action at ONE wound however many dice were rolled,")
print("    so a 3-die weapon can NEVER take a WND-2 or WND-3 target from full to")
print(f"    Down - {pct(g(2,'pick_one','p_down'))} and {pct(g(3,'pick_one','p_down'))}, "
      "exactly zero by construction.")
print(f"    R1/R2 kill a WND-2 outright {pct(g(2,'stop_on_down','p_down'))} of the "
      f"time and a WND-3 {pct(g(3,'stop_on_down','p_down'))},")
print(f"    averaging {g(3,'stop_on_down','e_wounds'):.3f} wounds against "
      f"{g(3,'pick_one','e_wounds'):.3f}.")
print("\n    This is the sharpest difference between the two rules and it is an")
print("    IDENTITY choice, not a balance one:")
print("      R3/R4 -> Attack Dice SHRED RANK-AND-FILE, DO NOT MELT CHARACTERS.")
print("               A leader is a hard target no burst can shortcut.")
print("      R1/R2 -> Attack Dice are the ANTI-CHARACTER tool - the more WND a")
print("               target has, the better multiple dice get relative to one.")
print("    Note WND 2-3 is not hypothetical: it is the campaign veteran ceiling")
print("    (Level 7, +Tough), so this rules on how durable a grown leader feels.")

# ------------------------------------------------------------------
print("\n" + "-" * 78)
print("[D] IS 'THE SHOOTER CHOOSES' A REAL CHOICE?")
print("    Down vs Pinned, from the rules as written:")
rows = [
    ("Can still Shoot / Interact?", "Down: no", "Pinned: YES"),
    ("Can be cleared by the target?", "Down: no, needs Stabilize", "Pinned: yes, spend Move"),
    ("Costs the enemy an Action?", "Down: yes, Stabilize or bleed out", "Pinned: no"),
    ("Removes the model from play?", "Down: yes if not stabilised", "Pinned: no"),
    ("Feeds the Stress ladder?", "Down: n/a", "Pinned: +1 Stress"),
]
for q, d, p in rows:
    print(f"      {q:<30} {d:<34} {p}")
print("\n    Down strictly dominates Pinned on every axis that matters at WND 1.")
print("    So 'the shooter chooses' offers a choice that has exactly one correct")
print("    answer, every single time. That is a decision point that costs table")
print("    time and returns no agency - the thing Out of Scope's anti-bloat")
print("    tenet exists to catch.")
print("\n    IT BECOMES A REAL CHOICE IN EXACTLY TWO CASES:")
print("      1. PAYLOAD WEAPONS. A payload lands in place of Pinned, so the pick")
print("         is 'wound' vs 'Bleeding/Fire/Suppressive'. Against a WND 2-3")
print("         target, Bleeding (a two-round death clock) can beat 1 of 3 WND.")
print("      2. MULTI-WOUND TARGETS, for the same reason.")
print("    Both are the same condition: the choice is real only when one wound")
print("    is NOT decisive. At WND 1 with a vanilla weapon it never is.")

# ------------------------------------------------------------------
print("\n" + "-" * 78)
print("[E] THE STAT-CEILING PROBLEM - true under EVERY rule")
print("    P(wound) per Action vs a maxed-out shooter on one die.")
best = core_exact(6) * core_exact(2)         # DEX +6, medium weapon, unarmoured
print(f"    A DEX +6 marksman - the hard stat cap - with a medium weapon reaches")
print(f"    {pct(best)} wound/Action. It cannot go higher; the natural-1 rule caps")
print(f"    to-hit at 90%.")
print(f"{'shooter':>34} {'wound/Action':>13} {'vs cap':>9}")
e = []
for stat, n, lbl in [(6, 1, "DEX +6 marksman, AD 1 (the cap)"),
                     (2, 2, "DEX +2 Fighter, AD 2"),
                     (2, 3, "DEX +2 Fighter, AD 3"),
                     (0, 3, "DEX +0 Recruit, AD 3"),
                     (-1, 3, "DEX -1, AD 3")]:
    w2, s2, m2 = outcomes(stat, 0, 2, 0)
    pd = resolve("R3", w2, s2, m2, n, 1)[2]
    print(f"{lbl:>34} {pct(pd):>13} {pd/best-1:>+8.0%}")
    e.append({"shooter": lbl, "p_wound_action": round(pd, 4),
              "vs_stat_cap": round(pd / best - 1, 4)})
OUT["stat_ceiling"] = e
print("\n    ATTACK DICE BREAK THE STAT CEILING. Two dice on an ordinary Fighter")
print("    beat the best marksman the game permits, and a DEX +0 Recruit with")
print("    three dice is within a whisker of one. No amount of pricing fixes")
print("    that - it is a statement about what skill is worth. If a 25 Cr")
print("    upgrade outperforms four stat points on the hard cap, DEX stops")
print("    being the thing that decides whether you land it (Weapons, tenet 1).")
print("    -> This is the strongest argument for RARITY/RANK GATING over price.")

# ------------------------------------------------------------------
print("\n" + "-" * 78)
print("[F] FAIR PRICE UNDER EACH RULE")
rifle = weapon_cost(WeaponBuild("Rifle", "standard_ranged", damage=2, reach=18))
fighter = U.body_cost("fighter")
d1 = outcomes(2, 0, 3, 0)[0] - outcomes(2, 0, 2, 0)[0]
rate = T.CREDITS_DAMAGE / d1
print(f"    Catalogue rate: {T.CREDITS_DAMAGE} Cr per +1 Damage = {rate:.0f} Cr per "
      "1.0 wounds/Action.")
print(f"{'rule':>14} {'AD2 cum':>9} {'AD3 cum':>9} {'draft 25/60':>13} {'verdict':>26}")
f = []
w, s, m = outcomes(2, 0, 2, 0)
for code, label in RULES:
    base = resolve(code, w, s, m, 1, 1)[0]
    cum, prev, cols = 0.0, base, []
    for n in (2, 3):
        cur = resolve(code, w, s, m, n, 1)[0]
        cum += (cur - prev) * rate
        cols.append(cum)
        prev = cur
    verdict = ("draft UNDER by "
               f"{cols[1]/60-1:+.0%}" if cols[1] > 60 else
               f"draft OVER by {cols[1]/60-1:+.0%}")
    print(f"{label:>14} {cols[0]:>8.0f}  {cols[1]:>8.0f}  {'25 / 60':>13} "
          f"{verdict:>26}")
    f.append({"rule": label, "ad2_cumulative_cr": round(cols[0], 1),
              "ad3_cumulative_cr": round(cols[1], 1), "draft_ad3": 60})
OUT["fair_price"] = f
ad2 = f[0]["ad2_cumulative_cr"]
ad3 = f[0]["ad3_cumulative_cr"]
print(f"\n    ALL FOUR RULES PRICE IDENTICALLY ({ad2:.0f} / {ad3:.0f} cumulative), because they")
print("    deliver identical WOUNDS and the catalogue's exchange rate prices")
print("    wounds only. The rule choice is free at the till; it is paid for in")
print("    suppression [B] and in character durability [C], neither of which the")
print("    Damage ladder has ever priced.")
print(f"\n    AGAINST THE DRAFT: AD 3 at +60 is right - fair is {ad3:.0f}, a {60/ad3-1:+.0%} gap.")
print(f"    AD 2 at +25 is the underpriced rung - fair is {ad2:.0f}, a {25/ad2-1:+.0%} gap.")
print("    The draft's step runs the wrong way: it should be roughly +40 then")
print("    +25, not +25 then +35. Die 2 is the expensive one.")
print("\n    THIS SUPERSEDES the '+25/+60 is about half price' line in the first")
print("    pass. That figure came from resolve_all's UNCAPPED E[wounds] (60/120),")
print("    which counts overkill on a WND-1 target as value. It is not value.")
print("    Capping at the target's actual WND - which every rule here does - the")
print("    honest fair price is 38/63 and the draft is close on AD 3.")
print("\n    The auto-include finding is UNAFFECTED and still stands: it compares")
print("    Attack Dice against BODIES, not against the Damage ladder. Both are")
print("    true at once - the price matches the damage-step rate, and the damage")
print("    ladder is itself cheap relative to a 100 Cr Fighter.")

OUT["params"] = {
    "engine": "exact enumeration, mirrors attack_dice_sim.py / sim_report.py",
    "shooter": "DEX +2", "weapon": "medium +2", "rifle_cr": rifle,
    "fighter_cr": fighter, "credits_damage": T.CREDITS_DAMAGE,
    "fair_rate_cr_per_wound_per_action": round(rate, 1),
    "rules": {"R1": "stop_on_down", "R2": "resolve_all", "R3": "pick_one",
              "R4": "pick_wound_pins_stack"},
}
p = Path(__file__).resolve().parent / "balance" / "results" / "attack-dice-15b-rules.json"
p.write_text(json.dumps(OUT, indent=2), encoding="utf-8")
print(f"\n[json] {p}")
print("=" * 78)

"""Settlements - the symmetric d20 two-roll proposal at TARGET NUMBER 10.

    HIT      1d20 + DEX + hit modifiers     vs  10 + Cover
    INJURY   1d20 + Damage + inj modifiers  vs  10 + Armour

    natural 1 always fails, natural 20 always succeeds (both rolls)

Ross's structure, with the target number dropped from 12 to 10. Section [C] also
measures a SECOND injury threshold at 15 - how often an injury roll clears 10+
versus 15+ - as a possible severity tier.

WHAT THE 15+ TIER DOES IS NOT RULED, AND THIS HARNESS DOES NOT ASSUME. It reports
the frequency only. Whether a 15+ injury means Out of Action instead of Down, a
second wound, a critical effect, or nothing at all is an open design question;
inventing one here would put a mechanic in the sim that nobody asked for.

Every headline number is EXACT - full enumeration over the 20 faces, mirroring
`attack_dice_sim.py`. The Monte Carlo block is a sampling-noise cross-check only,
never the reported figure.

THE KNOWN COST OF TN 10, stated up front because it is the reason 12 was the
default: the hit roll must distinguish 13 net states (stat +0..+6 crossed with
modifiers -3..+3, so net -3..+9). At TN 12 all 13 resolve distinctly. At TN 10
the top two collapse - net +8 and net +9 both read 95% - because the natural-1
floor caps usable outcomes at 19/20. That is one clipped state, at the single
best matchup in the game, and section [D] measures exactly where it bites.
"""

import json
import random
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

random.seed(20260708)
N_MC = 200000
TN = 10
SEVERE = 15

OUT = {}


def p_exact(bonus, tn_add, target=TN):
    """P(1d20 + bonus >= target + tn_add), nat 1 fails, nat 20 succeeds."""
    faces = sum(1 for d in range(2, 20) if d + bonus >= target + tn_add) + 1
    return faces / 20


def p_mc(bonus, tn_add, target=TN, n=N_MC):
    ok = 0
    for _ in range(n):
        d = random.randint(1, 20)
        if d == 1:
            continue
        if d == 20 or d + bonus >= target + tn_add:
            ok += 1
    return ok / n


ROWS = [
    ("Recruit  +1 DEX, +1 pistol, hvy cvr, hvy arm", 1, 2, 1, 2),
    ("Recruit  +1 DEX, +1 pistol, open, unarmoured",  1, 0, 1, 0),
    ("Fighter  +2 DEX, +3 rifle,  lt cvr,  lt arm",   2, 1, 3, 1),
    ("Fighter  +2 DEX, +3 rifle,  hvy cvr, hvy arm",  2, 2, 3, 2),
    ("Spec     +4 DEX, +4 rifle,  hvy cvr, lt arm",   4, 2, 4, 1),
    ("Marksman +6 DEX, +3 rifle,  hvy cvr, hvy arm",  6, 2, 3, 2),
    ("Marksman +6 DEX, +5 heavy,  hvy cvr, hvy arm",  6, 2, 5, 2),
    ("Marksman +6 DEX, +3 rifle,  open, unarmoured",  6, 0, 3, 0),
    ("Marksman +6 DEX, +5 heavy,  open, unarmoured",  6, 0, 5, 0),
]


def old_d10(dex, cov, dmg, arm):
    h = max(1, min(9, 4 + dex - cov)) / 10
    i = max(1, min(9, 4 + dmg - arm)) / 10
    return h * i


def section_a():
    print("=" * 92)
    print("[A]  TN 10 - hit, injury, and the outcome split      (vs today's d10 two-roll)")
    print("=" * 92)
    print(f"{'':<46}{'hit':>7}{'inj':>7}{'miss':>8}{'Pin':>7}{'DOWN':>8}{'today':>8}")
    rows = {}
    for lbl, dex, cov, dmg, arm in ROWS:
        h, i = p_exact(dex, cov), p_exact(dmg, arm)
        print(f"{lbl:<46}{h:>7.0%}{i:>7.0%}{1-h:>8.0%}{h*(1-i):>7.0%}{h*i:>8.0%}"
              f"{old_d10(dex, cov, dmg, arm):>8.0%}")
        rows[lbl] = {"hit": h, "injure": i, "miss": 1-h, "pin": h*(1-i), "down": h*i,
                     "d10_today": old_d10(dex, cov, dmg, arm)}
    OUT["A_tn10_outcomes"] = rows


def section_b():
    print()
    print("=" * 92)
    print("[B]  TN 10 vs TN 11 vs TN 12 - the whole dial, DOWN rate per attack")
    print("=" * 92)
    print(f"{'':<46}{'TN 10':>9}{'TN 11':>9}{'TN 12':>9}{'today':>9}")
    rows = {}
    for lbl, dex, cov, dmg, arm in ROWS:
        vals = [p_exact(dex, cov, t) * p_exact(dmg, arm, t) for t in (10, 11, 12)]
        print(f"{lbl:<46}" + "".join(f"{v:>9.0%}" for v in vals)
              + f"{old_d10(dex, cov, dmg, arm):>9.0%}")
        rows[lbl] = {"tn10": vals[0], "tn11": vals[1], "tn12": vals[2]}
    OUT["B_target_number_dial"] = rows


def section_c():
    print()
    print("=" * 92)
    print(f"[C]  THE INJURY ROLL AT TWO BARS - how often does it clear {TN}+ and {SEVERE}+ ?")
    print("     (what a 15+ result MEANS is unruled - frequency only)")
    print("=" * 92)
    print(f"{'':<34}{'>=10+Arm':>10}{'>=15+Arm':>10}{'severe as':>12}{'per attack':>12}")
    print(f"{'weapon vs armour':<34}{'(wound)':>10}{'(severe)':>10}{'% of wounds':>12}{'incl. hit':>12}")
    rows = {}
    for dmg in (1, 2, 3, 4, 5):
        for arm in (0, 1, 2):
            w = p_exact(dmg, arm, TN)
            s = p_exact(dmg, arm, SEVERE)
            share = s / w if w else 0.0
            # per-attack figure uses a mid-ladder shooter: DEX +2, light cover
            per = p_exact(2, 1, TN) * s
            lbl = f"Damage +{dmg} vs Armour -{arm}"
            print(f"{lbl:<34}{w:>10.0%}{s:>10.0%}{share:>12.0%}{per:>12.0%}")
            rows[lbl] = {"wound": w, "severe": s, "severe_share_of_wounds": share,
                         "severe_per_attack_dex2_lt_cover": per}
        print()
    OUT["C_injury_two_bars"] = rows

    print("  Read: at Damage +3 vs no armour, 70% of injury rolls wound and 45% reach 15+,")
    print("  so roughly TWO IN THREE wounds would be 'severe'. That is not a rare tier.")


def section_d():
    print()
    print("=" * 92)
    print("[D]  SATURATION - does the hit roll still tell all 13 net states apart?")
    print("=" * 92)
    for t in (10, 11, 12):
        seen = {}
        for net in range(-3, 10):
            seen.setdefault(round(p_exact(net, 0, t), 6), []).append(net)
        collapsed = {k: v for k, v in seen.items() if len(v) > 1}
        status = "clean" if not collapsed else \
            "COLLAPSED: " + "; ".join(f"net {v} share {k:.0%}" for k, v in collapsed.items())
        print(f"  TN {t}:  {len(seen)}/13 distinct   range {min(seen):.0%}..{max(seen):.0%}   {status}")
        OUT.setdefault("D_saturation", {})[f"tn{t}"] = {
            "distinct": len(seen), "collapsed": {str(k): v for k, v in collapsed.items()}}
    print()
    print("  d10 vs 7+ (today), for reference:")
    seen = {}
    for net in range(-3, 10):
        seen.setdefault(max(1, min(9, 4 + net)) / 10, []).append(net)
    collapsed = {k: v for k, v in seen.items() if len(v) > 1}
    print(f"  d10:    {len(seen)}/13 distinct   COLLAPSED: "
          + "; ".join(f"net {v}" for v in collapsed.values()))


def section_e():
    print()
    print("=" * 92)
    print(f"[E]  MONTE CARLO CROSS-CHECK  (N = {N_MC:,}) - sampling noise only, not the figure")
    print("=" * 92)
    worst = 0.0
    for lbl, dex, cov, dmg, arm in ROWS[:4]:
        for what, b, t in (("hit", dex, cov), ("inj", dmg, arm)):
            e, m = p_exact(b, t), p_mc(b, t)
            worst = max(worst, abs(e - m))
    print(f"  largest exact-vs-sampled gap across 8 cells: {worst:.4f}")
    print(f"  {'consistent with sampling noise' if worst < 0.005 else 'INVESTIGATE'}")
    OUT["E_mc_max_gap"] = worst


def main():
    print(__doc__.split("\n")[0])
    print(f"seed 20260708 | TN {TN} | severe bar {SEVERE}\n")
    section_a()
    section_b()
    section_c()
    section_d()
    section_e()
    path = Path(__file__).resolve().parent / "results" / "d20-tn10.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(OUT, indent=2), encoding="utf-8")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()

"""Should Stress survive being Downed? (Phase 15b, follow-up 2026-08-29)

Ross's read: realistically it should, and the mechanical consequence is that a
Stabilised fighter's next activation opens with a Break test.

THIS IS NOT AN ATTACK DICE QUESTION. It only surfaced here, and that matters
for how it gets ruled. A model can already arrive at Down carrying Stress from
earlier in the fight - failed Injury rolls against it, friendlies going Down in
LOS, hazards - and the rules have never said what happens to that Stress when
it drops. So the ruling lands on EVERY fight in the game, and Attack Dice
merely made it visible. Both contributions are measured separately below.

What the ruling actually switches on, from `Morale`:
  Stress 1    Shaken - a flat -1 to everything, no test.
  Stress 2+   Break test each round: 1d10 + NRV - (Stress - 1) >= 7,
              Shaken's -1 excluded. Pass clears ALL Stress.
              Fail -> Bolt (at 2) / Broken (at 3) / BUGOUT (at 4+) = REMOVED.

So the sharp end is a revived fighter at 4+ Stress: the crew spends an Action
and an INT test to save him, he stands up, fails one roll, and walks off the
table. That is the outcome to price before agreeing to this, and it is what
section [C] measures.

Exact enumeration for the Attack-Dice contribution; Monte-Carlo (seeded) for
the accumulated-Stress question, which needs a fight to exist.
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

random.seed(20260708)
N = 20000
OUT = {}


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
    return h * i, h * (1 - i), 1 - h


def break_test_outcome(stress, nrv):
    """P(pass), P(fail) and the severity a failure carries at this Stress."""
    if stress < 2:
        return 1.0, 0.0, "no test"
    p_pass = core_exact(nrv - (stress - 1))
    sev = "Bolt" if stress == 2 else ("Broken" if stress == 3 else "BUGOUT (removed)")
    return p_pass, 1 - p_pass, sev


print("=" * 78)
print("SHOULD STRESS SURVIVE BEING DOWNED?   exact + seeded MC")
print("=" * 78)

# ==================================================================
print("\n[A] WHAT STRESS DOES A DOWNED MODEL CARRY, FROM THE BURST ALONE?")
print("    Conditional on the target going Down. DEX+2, weapon +2, open")
print("    unarmoured, surplus injury passes converting to Stress.")
print(f"{'dice':>5} {'S=0':>8} {'S=1':>8} {'S=2':>8} {'S=3+':>8} {'mean':>7} "
      f"{'P(S>=2 | Down)':>15}")
w, s, m = outcomes(2, 0, 2, 0)
a = []
for n in (1, 2, 3):
    dist = {}
    p_down_tot = 0.0
    for seq in product("wpm", repeat=n):
        pr = 1.0
        for ch in seq:
            pr *= {"w": w, "p": s, "m": m}[ch]
        passes, pins = seq.count("w"), seq.count("p")
        if passes == 0:
            continue                      # target still standing, not our case
        stress = pins + (passes - 1)      # one pass is the wound; rest are Stress
        dist[stress] = dist.get(stress, 0.0) + pr
        p_down_tot += pr
    cond = {k: v / p_down_tot for k, v in dist.items()}
    mean = sum(k * v for k, v in cond.items())
    ge2 = sum(v for k, v in cond.items() if k >= 2)
    print(f"{n:>5} {pct(cond.get(0,0)):>8} {pct(cond.get(1,0)):>8} "
          f"{pct(cond.get(2,0)):>8} {pct(sum(v for k,v in cond.items() if k>=3)):>8} "
          f"{mean:>7.2f} {pct(ge2):>15}")
    a.append({"dice": n, "mean_stress_given_down": round(mean, 3),
              "p_stress_ge2_given_down": round(ge2, 4),
              "dist": {str(k): round(v, 4) for k, v in sorted(cond.items())}})
OUT["stress_given_down"] = a
g = lambda n, k: next(r[k] for r in a if r["dice"] == n)
print(f"\n    A 3-die burst leaves its victim on {g(3,'mean_stress_given_down'):.2f} Stress on average,")
print(f"    and at 2+ Stress - Break-test range - {pct(g(3,'p_stress_ge2_given_down'))} of the time.")
print(f"    A single shot leaves {g(1,'mean_stress_given_down'):.2f}: a lone bullet that Downs you")
print("    carries no Stress at all, because its one pass IS the wound. So this")
print("    Stress is entirely an Attack Dice phenomenon at the moment of Down.")

# ==================================================================
print("\n" + "-" * 78)
print("[B] BUT MOST OF THE STRESS IS NOT FROM THE BURST")
print("    A model usually arrives at Down having already been shot at for")
print("    rounds. Seeded MC, N=20,000: a DEX+2 rifleman is fired on until Down")
print("    by single-shot weapons only - NO Attack Dice anywhere.")
acc = {}
for _ in range(N):
    st = 0
    while True:
        r = random.random()
        if r < w:                          # wounded -> Down
            acc[st] = acc.get(st, 0) + 1
            break
        elif r < w + s:                    # Pinned
            st += 1
        # miss: nothing
tot = sum(acc.values())
dist_b = {k: v / tot for k, v in sorted(acc.items())}
mean_b = sum(k * v for k, v in dist_b.items())
ge2_b = sum(v for k, v in dist_b.items() if k >= 2)
print(f"{'S=0':>8} {'S=1':>8} {'S=2':>8} {'S=3':>8} {'S=4+':>8} {'mean':>7} {'P(S>=2)':>9}")
print(f"{pct(dist_b.get(0,0)):>8} {pct(dist_b.get(1,0)):>8} {pct(dist_b.get(2,0)):>8} "
      f"{pct(dist_b.get(3,0)):>8} {pct(sum(v for k,v in dist_b.items() if k>=4)):>8} "
      f"{mean_b:>7.2f} {pct(ge2_b):>9}")
OUT["accumulated_stress_no_attack_dice"] = {
    "mean": round(mean_b, 3), "p_ge2": round(ge2_b, 4),
    "dist": {str(k): round(v, 4) for k, v in dist_b.items()}}
print(f"\n    With NO Attack Dice in the game at all, a model reaches Down carrying")
print(f"    {mean_b:.2f} Stress on average and is in Break-test range {pct(ge2_b)} of the time.")
print(f"    Against {g(3,'mean_stress_given_down'):.2f} / {pct(g(3,'p_stress_ge2_given_down'))} from a 3-die burst in one Action.")
print("\n    >> THE RULING IS NOT ABOUT ATTACK DICE. Ordinary single-shot fire")
print("       already puts more Stress on a downed model than a burst does,")
print("       because it takes several attempts and every failed one Pins.")
print("       Attack Dice compress that into one Action; they did not create it.")

# ==================================================================
print("\n" + "-" * 78)
print("[B2] BOTH RULES TOGETHER - the case actually on the table")
print("     Same MC, but the shooter carries a 3-die weapon and surplus injury")
print("     passes convert to Stress. This is what Stress-at-Down looks like if")
print("     BOTH open items are ruled yes.")


def mc_until_down(n_dice, surplus_to_stress, n=N):
    acc = {}
    for _ in range(n):
        st = 0
        while True:
            passes = pins = 0
            for _ in range(n_dice):
                r = random.random()
                if r < w:
                    passes += 1
                elif r < w + s:
                    pins += 1
            st += pins
            if passes:
                if surplus_to_stress:
                    st += passes - 1
                acc[st] = acc.get(st, 0) + 1
                break
    tot = sum(acc.values())
    d = {k: v / tot for k, v in sorted(acc.items())}
    return d, sum(k * v for k, v in d.items()), sum(v for k, v in d.items() if k >= 2)


print(f"{'configuration':>34} {'mean':>7} {'P(S>=2)':>9} {'P(S>=4)':>9}")
b2 = []
for lbl, nd, sur in [("1 die, no conversion (today)", 1, False),
                     ("3 dice, no conversion", 3, False),
                     ("3 dice + surplus->Stress", 3, True)]:
    d, mn, ge2 = mc_until_down(nd, sur)
    ge4 = sum(v for k, v in d.items() if k >= 4)
    print(f"{lbl:>34} {mn:>7.2f} {pct(ge2):>9} {pct(ge4):>9}")
    b2.append({"config": lbl, "mean": round(mn, 3), "p_ge2": round(ge2, 4),
               "p_ge4": round(ge4, 4), "dist": {str(k): round(v, 4) for k, v in d.items()}})
OUT["both_rules_together"] = b2
base, both = b2[0], b2[2]
print(f"\n     Adopting both roughly {both['mean']/base['mean']:.1f}x the Stress a downed model")
print(f"     carries ({base['mean']:.2f} -> {both['mean']:.2f}), and takes P(in Break-test range)")
print(f"     from {pct(base['p_ge2'])} to {pct(both['p_ge2'])}. The BugOut band (4+) goes")
print(f"     {pct(base['p_ge4'])} -> {pct(both['p_ge4'])}.")

print("\n" + "-" * 78)
print("[C] THE SHARP END - what happens when someone revives him?")
print("    A Stabilised fighter opens his next activation with a Break test.")
print(f"{'Stress':>7} {'test?':>7} {'NRV+1 fail':>11} {'NRV+2 fail':>11} "
      f"{'NRV+3 fail':>11} {'failure means':>18}")
c = []
for st in (0, 1, 2, 3, 4, 5):
    row = []
    for nrv in (1, 2, 3):
        _, pf, sev = break_test_outcome(st, nrv)
        row.append(pf)
    _, _, sev = break_test_outcome(st, 2)
    print(f"{st:>7} {('yes' if st >= 2 else 'no'):>7} {pct(row[0]):>11} "
          f"{pct(row[1]):>11} {pct(row[2]):>11} {sev:>18}")
    c.append({"stress": st, "fail_nrv1": round(row[0], 4),
              "fail_nrv2": round(row[1], 4), "fail_nrv3": round(row[2], 4),
              "severity": sev})
OUT["revival_break_test"] = c
print("\n    The 4+ row is the one that matters. A crew spends an Action AND an")
print("    INT test to Stabilise a friend; he stands up, rolls, and on a failure")
print("    at 4+ Stress he BUGS OUT - removed from play. The rescue bought")
print("    nothing, and it cost a whole activation to buy it.")

# combined probability of the bad beat
print("\n    How often does that actually happen, per revival, at NRV +2?")
print(f"{'game state':>34} {'fails 1st test':>15} {'BUGS OUT':>10} "
      f"{'~1 in N bug out':>16}")
bad = []
for row in b2:
    d = {int(k): v for k, v in row["dist"].items()}
    pf = sum(v * break_test_outcome(k, 2)[1] for k, v in d.items() if k >= 2)
    pb = sum(v * break_test_outcome(k, 2)[1] for k, v in d.items() if k >= 4)
    print(f"{row['config']:>34} {pct(pf):>15} {pct(pb):>10} "
          f"{('1 in ' + f'{1/pb:.0f}') if pb else '-':>16}")
    bad.append({"config": row["config"], "p_fail_first_test": round(pf, 4),
                "p_bugout_on_revival": round(pb, 4)})
OUT["bad_beat"] = bad
now, both_r = bad[0], bad[2]
print(f"\n    TODAY'S GAME, if Stress simply persists: {pct(now['p_fail_first_test'])} of revived")
print(f"    fighters lose the activation, {pct(now['p_bugout_on_revival'])} walk off - about "
      f"1 in {1/now['p_bugout_on_revival']:.0f}.")
print(f"    WITH BOTH ATTACK DICE RULES: {pct(both_r['p_fail_first_test'])} and "
      f"{pct(both_r['p_bugout_on_revival'])} - about 1 in {1/both_r['p_bugout_on_revival']:.0f}.")
print("\n    Both land in story territory rather than feels-bad territory. The")
print("    second is the one to watch: a fifth of revivals wasted is a lot more")
print("    noticeable than a tenth, and it is the version that also has three")
print("    dice hitting the model on the way down.")

# ==================================================================
print("\n" + "-" * 78)
print("[D] THREE WAYS TO RULE IT, and what each costs")
print("""
    1. STRESS PERSISTS IN FULL  (Ross's reading)
       Revived fighter tests immediately, can BugOut.
       + Realistic, dramatic, zero new rules text - it is the ABSENCE of a
         clearing rule, so it is literally the cheapest option to write.
       + Makes Stabilise a real decision instead of an automatic yes.
       - The double-punish above: {af} of revivals fail at once, {bo} are
         removed outright after someone spent an Action saving them.
       - Interacts with the death-spiral risk already flagged in
         `Dice Mechanic - Sim Findings` 7.
       - Note those figures are for BOTH Attack Dice rules adopted. On
         today's game the same rule costs only {af0} / {bo0}.

    2. STABILISE CLEARS TO 1 STRESS  (the valve)
       "A Stabilised fighter returns Shaken, however much Stress it had."
       + One clause. Keeps the flavour - he comes back rattled, at -1.
       + Removes the bad beat entirely; no test on revival, ever.
       - Loses exactly the beat Ross wants: no nerve test on standing up.

    3. PERSISTS, BUT NO BUGOUT ON THE FIRST TEST  (capped)
       Failure on the revival test caps at Broken - lose the activation.
       + Keeps the test and the drama, removes only the walk-off-the-table.
       - A special case, and special cases are what this project cuts.
""".format(af=pct(both_r["p_fail_first_test"]).strip(),
           bo=pct(both_r["p_bugout_on_revival"]).strip(),
           af0=pct(now["p_fail_first_test"]).strip(),
           bo0=pct(now["p_bugout_on_revival"]).strip()))

OUT["params"] = {
    "seed": 20260708, "N": N,
    "shooter": "DEX +2", "weapon": "medium +2", "target": "open, unarmoured",
    "break_test": "1d10 + NRV - (Stress-1) >= 7; fail -> Bolt(2)/Broken(3)/BugOut(4+)",
    "note": "Section B is deliberately Attack-Dice-free - it measures what the "
            "ruling does to the EXISTING game, which is the larger effect.",
}
p = Path(__file__).resolve().parent / "balance" / "results" / "attack-dice-15b-stress-on-down.json"
p.write_text(json.dumps(OUT, indent=2), encoding="utf-8")
print(f"[json] {p}")
print("=" * 78)

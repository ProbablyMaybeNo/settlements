"""BLKOUT-import test battery — measures the two new reaction mechanics against
the locked engine, A/B (toggles off = pre-import behaviour):

  DODGE      a Ready target may Dodge a shot (opposed AGI vs DEX; win = miss +
             reposition out of LOS + Pinned). Ignores cover, so it's the
             "caught in the open" tool. Policy: dodge only when cover < Heavy.
  DIST_GATE  movement overwatch only fires on a Move > half MOV (creeping is safe).

Run:  py -3.13 blkout_test.py            # full battery (default N)
      py -3.13 blkout_test.py 1000       # smaller/faster
"""
import random
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

import engine
from engine import Game
from board import take_a_hold
from crews import redline

SEED = 20260717


def run_series(n, pa, pb, dodge, gate, seed=SEED):
    engine.DODGE_ON = dodge
    engine.DIST_GATE = gate
    random.seed(seed)
    w = {'a': 0, 'b': 0, 'draw': 0}
    vp = [0, 0]
    al = [0, 0]
    st = {'snap': 0, 'dodge_try': 0, 'dodge_save': 0}
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            g = Game(redline(0, pa), redline(1, pb), board)
            r = g.play()
            asd, bsd = 0, 1
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            g = Game(redline(0, pb), redline(1, pa), board)
            r = g.play()
            asd, bsd = 1, 0
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        w['a' if aw else 'b' if bw else 'draw'] += 1
        vp[0] += r['vp'][asd]; vp[1] += r['vp'][bsd]
        al[0] += r['alive'][asd]; al[1] += r['alive'][bsd]
        for k in st:
            st[k] += g.stat[k]
    return dict(w=w, vp=[vp[0] / n, vp[1] / n], al=[al[0] / n, al[1] / n],
                st={k: st[k] / n for k in st}, n=n)


def winpct(s):
    return (s['w']['a'] + 0.5 * s['w']['draw']) / s['n']


def surv(s):
    return (s['al'][0] + s['al'][1]) / 2.0     # avg survivors per side (mirror -> lethality proxy)


# --- isolated dodge micro-sim (no board / AI, just the resolution maths) ------
def _core(mod, target=7):
    d = random.randint(1, 10)
    if d == 1:
        return False
    if d == 10:
        return True
    return d + mod >= target


def _opp(a, b):        # ties -> b (the defender / dodger)
    return random.randint(1, 10) + a > random.randint(1, 10) + b


def p_survive_normal(dex, cover, dmg, armor=0, trials=200000):
    s = 0
    for _ in range(trials):
        if _core(dex - cover) and _core(dmg - armor):     # hit AND wound -> Down (WND 1)
            continue
        s += 1
    return s / trials


def p_survive_dodge(dex, agi, dmg, armor=0, trials=200000):
    s = 0
    for _ in range(trials):
        if _opp(dex, agi):                                # attacker wins -> auto-hit
            if _core(dmg - armor):
                continue
            s += 1
        else:                                             # dodge beats the shot
            s += 1
    return s / trials


def bar(p):
    return '#' * round(p * 30)


def hdr(t):
    print("\n" + "=" * 66)
    print(t)
    print("=" * 66)


def main(n):
    print("SETTLEMENTS — BLKOUT-import test battery")
    print(f"(balanced Redline mirror, {n} games/series, sides swapped; micro-sim 200k trials)")

    # 1) SYMMETRY — the new mechanics must not introduce a side bias.
    hdr("[1] SYMMETRY — balanced mirror with BOTH changes ON (must be ~50/50)")
    s = run_series(n, 'balanced', 'balanced', dodge=True, gate=True)
    print(f"    side-A win {winpct(s):5.1%}   (draws {s['w']['draw']/s['n']:4.1%})")
    print("    -> a gap here would mean the import broke combat symmetry.")

    # 2) ISOLATE each change — survivors (lethality) + trigger frequency.
    hdr("[2] LETHALITY & TRIGGERS — balanced mirror, each toggle isolated")
    print(f"    {'config':<22}{'win%':>7}{'surv/side':>11}{'VP/side':>9}"
          f"{'snap/g':>8}{'dodge try/save':>16}")
    for label, d, gt in [("baseline (pre-import)", False, False),
                         ("dist-gate only", False, True),
                         ("dodge only", True, False),
                         ("both (full import)", True, True)]:
        s = run_series(n, 'balanced', 'balanced', dodge=d, gate=gt)
        print(f"    {label:<22}{winpct(s):6.1%}{surv(s):11.2f}{s['vp'][0]:9.1f}"
              f"{s['st']['snap']:8.2f}{s['st']['dodge_try']:9.2f}/{s['st']['dodge_save']:.2f}")
    print("    surv/side rising = combat less lethal; watch it doesn't gut the 'super-deadly' pillar.")

    # 3) OBJECTIVE-PRIMACY — does balanced still beat runner/hunter with changes ON?
    hdr("[3] OBJECTIVE-PRIMACY holds? — balanced vs runner/hunter, BOTH changes ON")
    for foe, base in [('runner', '100'), ('hunter', '60')]:
        s = run_series(n, 'balanced', foe, dodge=True, gate=True)
        print(f"    balanced vs {foe:<7} {winpct(s):6.1%}   (pre-import baseline was ~{base}%)")
    print("    balanced must still crush runner and beat hunter, or the import broke the vision.")

    # 4) DODGE micro-sim — the isolated protective value + does AGI now matter?
    hdr("[4] DODGE micro-sim — P(target survives one shot) vs a DEX+2 rifle (dmg3, no armour)")
    print("    'normal' = eat the shot behind cover · 'dodge' = evade (ignores cover), by AGI")
    print(f"    {'cover':<10}{'normal':>9}   {'dodge AGI0':>11}{'dodge AGI2':>12}{'dodge AGI4':>12}")
    dm = 3
    for cov, cname in [(0, 'open'), (1, 'light'), (2, 'heavy')]:
        pn = p_survive_normal(2, cov, dm)
        pd = [p_survive_dodge(2, a, dm) for a in (0, 2, 4)]
        print(f"    {cname:<10}{pn:9.1%}   {pd[0]:11.1%}{pd[1]:12.1%}{pd[2]:12.1%}")
    print("    Reads: dodge beats standing in the OPEN (esp. high AGI) but is WORSE than Heavy")
    print("    cover -> the 'dodge only when exposed' policy is correct, and AGI now buys defence.")


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 2500
    main(n)

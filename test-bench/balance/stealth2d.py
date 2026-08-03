# -*- coding: utf-8 -*-
"""PACKET TESTS T1-T4 — the stealth / Ambush layer (Packet-Design-Review §2.6).

  T1  the stealth skill list has never been measured at all
  T2  Vanishing Point + Ghost Step + Return to the Shadows may make one fighter
      "effectively un-targetable for an entire game"
  T3  a failed Ambush must draw a free Attack Back or Hidden is strictly dominant
  T4  Ambush-on-AGI is meant to give AGI a COMBAT identity, not just a mobility one

METHOD — paired mirror. For every crew we measure BOTH:
    control : crew        vs crew        (no stealth anywhere)   -> the harness baseline
    test    : crew + kit  vs crew        (only side A stealthy)  -> the mechanic
and report the DIFFERENCE. Reporting the difference rather than the distance from
50% removes any residual side/activation bias in the harness itself.

Both sides always run the SAME policy (AmbushPolicy) so the delta is the value of
the MECHANIC, never of a playstyle.

TWO CARRIERS ARE TESTED ON PURPOSE. Ambush resolves on AGI, so handing the kit to
a DEX crew makes its fighters attack on their worst stat. Measuring only that
would report "stealth is terrible" when what was measured is a trap build. The
AGI crew is the intended carrier; the DEX crew is the control for mis-building.

Nothing in the packet fixes these numbers, so every dial is swept.
"""
import sys, os, random

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

import engine
from engine import Game, Unit
from board import take_a_hold
from policies import AMBUSH

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
DMG_ANCHOR = 1.12       # win-points per model for +1 Damage (conditions2d.py mirror pass)


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


# ============================== CREWS =======================================
DEX6 = [('Boss', 'Leader', 'rifle', 'none', dict(dex=4, str=2)),
        ('Marks', 'Specialist', 'rifle', 'none', dict(dex=4)),
        ('Gun1', 'Fighter', 'pistol', 'none', dict(dex=2)),
        ('Gun2', 'Fighter', 'pistol', 'none', dict(dex=2)),
        ('R1', 'Recruit', 'pistol', 'none', dict(dex=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(str=1))]

STR6 = [('Boss', 'Leader', 'sledge', 'none', dict(str=4, nrv=2)),
        ('B1', 'Specialist', 'crowbar', 'none', dict(str=4)),
        ('B2', 'Fighter', 'crowbar', 'none', dict(str=2)),
        ('B3', 'Fighter', 'bat', 'none', dict(str=2)),
        ('R1', 'Recruit', 'bat', 'none', dict(str=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(str=1))]

AGI6 = [('Boss', 'Leader', 'sledge', 'none', dict(agi=4, nrv=2)),
        ('A1', 'Specialist', 'crowbar', 'none', dict(agi=4)),
        ('A2', 'Fighter', 'crowbar', 'none', dict(agi=2)),
        ('A3', 'Fighter', 'bat', 'none', dict(agi=2)),
        ('R1', 'Recruit', 'bat', 'none', dict(agi=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(agi=1))]

KIT = ('stealth', 'ghost_step')
COMBO = ('stealth', 'ghost_step', 'vanishing_point', 'return_to_shadows')


def crew(spec, extra=(), combo_first=False):
    def build(side):
        out = []
        for i, (nm, rank, wpn, arm, st) in enumerate(spec):
            sk = COMBO if (combo_first and i == 0) else tuple(extra)
            u = Unit(nm, side, rank, wpn, arm, skills=sk, **st)
            u.policy = AMBUSH
            out.append(u)
        return out
    return build


# ============================== HARNESS =====================================
def versus(mkA, mkB, GameCls, n, seed=20260802, collect=None):
    random.seed(seed)
    a = dr = 0
    acc = {}
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            ca, cb = mkA(0), mkB(1)
            r = GameCls(ca, cb, board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            cb, ca = mkB(0), mkA(1)
            r = GameCls(cb, ca, board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
        if collect:
            for k, fn in collect.items():
                acc[k] = acc.get(k, 0.0) + fn(ca)
    out = (a + 0.5 * dr) / n
    return (out, {k: v / n for k, v in acc.items()}) if collect else out


def paired(spec, kit=KIT, combo_first=False, collect=None, foe=None):
    """(test - control) across both scoring shapes. Returns mean delta in points.

    `foe` defaults to the same spec (a true mirror). It MUST be overridden with a
    shooting crew for the T2 'is it ever shot at?' metric — against an all-melee
    mirror, 'never targeted' is true by construction and measures nothing."""
    foe = foe or spec
    res = {}
    for name, G in (('Hold', Game), ('Annih', Annihilate)):
        ctrl = versus(crew(spec), crew(foe), G, N)
        if collect:
            test, st = versus(crew(spec, kit, combo_first), crew(foe), G, N, collect=collect)
        else:
            test, st = versus(crew(spec, kit, combo_first), crew(foe), G, N), {}
        res[name] = (ctrl, test, st)
    dh = (res['Hold'][1] - res['Hold'][0]) * 100
    da = (res['Annih'][1] - res['Annih'][0]) * 100
    stats = {}
    for k in (collect or {}):
        stats[k] = (res['Hold'][2].get(k, 0) + res['Annih'][2].get(k, 0)) / 2
    return (dh + da) / 2, dh, da, res, stats


def dials(**kw):
    for k, v in kw.items():
        setattr(engine, k, v)


def banner(t):
    print("\n" + "=" * 104)
    print(t)
    print("=" * 104)


# ============================ CONTROLS ======================================
banner(f"HARNESS CONTROLS — identical crews, no stealth. Any drift from 50% is measured")
print("and subtracted from every result below, so the harness bias cannot leak in.\n")
dials(STEALTH_ON=False)
for label, spec in (('DEX6', DEX6), ('STR6', STR6), ('AGI6', AGI6)):
    h = versus(crew(spec), crew(spec), Game, N)
    a = versus(crew(spec), crew(spec), Annihilate, N)
    print(f"  {label:<8} mirror control    Hold {h*100:5.1f}%   Annih {a*100:5.1f}%")

# ============================= T1 + T4 ======================================
banner(f"T1 / T4 - WHAT IS STEALTH WORTH, AND TO WHOM?   ({N} games/cell, paired mirror)")
print("Delta = (stealthy crew vs plain crew) minus (plain vs plain). Positive = the")
print("kit is worth something. Per-model is comparable with conditions2d.py, where")
print("+1 Damage = 1.12 win-points/model and is priced at 15 Credits.\n")
print(f"  {'carrier':<8}{'hidden mode':<14}{'holds':>7}{'payoff':>8}"
      f"{'d Hold':>9}{'d Annih':>9}{'d mean':>9}{'per model':>11}{'~Credits':>10}{'ambush/gm':>11}")

for cname, spec in (('DEX6', DEX6), ('AGI6', AGI6)):
    for hmode in ('modifier', 'untargetable'):
        for holds in (True, False):
            for payoff in (0, 2):
                dials(STEALTH_ON=True, HIDDEN_MODE=hmode, HIDDEN_HOLDS=holds,
                      AMBUSH_PAYOFF=payoff, ATTACK_BACK=True)
                m, dh, da, _, st = paired(spec, collect={
                    'amb': lambda c: sum(u.ambushes for u in c)})
                pm = m / 6
                print(f"  {cname:<8}{hmode:<14}{str(holds):>7}{payoff:>8}"
                      f"{dh:>+8.1f} {da:>+8.1f} {m:>+8.1f} {pm:>10.2f}"
                      f"{pm / DMG_ANCHOR * 15:>10.0f}{st['amb']:>11.2f}")

# ============================= T3 ===========================================
banner(f"T3 - DOES THE FREE ATTACK BACK ACTUALLY BITE?   ({N} games/cell, AGI6 carrier)")
print("The review: without a real punishment for a failed sneak attack, Hidden is")
print("strictly dominant and Ambush is a free roll for upside.\n")
print(f"  {'hidden mode':<14}{'attack back':>13}{'d mean':>9}{'ambushes/gm':>13}"
      f"{'miss rate':>11}{'ambush kills':>14}")

for hmode in ('modifier', 'untargetable'):
    for ab in (True, False):
        dials(STEALTH_ON=True, HIDDEN_MODE=hmode, HIDDEN_HOLDS=True,
              AMBUSH_PAYOFF=1, ATTACK_BACK=ab)
        m, dh, da, _, st = paired(AGI6, collect={
            'amb': lambda c: sum(u.ambushes for u in c),
            'fail': lambda c: sum(u.ambush_fails for u in c),
            'ak': lambda c: sum(u.ambush_kills for u in c)})
        fr = st['fail'] / st['amb'] * 100 if st['amb'] else 0.0
        print(f"  {hmode:<14}{str(ab):>13}{m:>+8.1f} {st['amb']:>13.2f}"
              f"{fr:>10.1f}%{st['ak']:>14.2f}")

# ============================= T2 ===========================================
banner(f"T2 - THE 'UN-TARGETABLE FIGHTER' COMBO   ({N} games/cell, AGI6 vs the DEX6 gunline)")
print("Vanishing Point + Ghost Step + Return to the Shadows stacked on ONE fighter.")
print("If the review is right, that fighter finishes ~6/6 rounds Hidden and is never")
print("shot at. Figures are for fighter 0 of the buffed crew.")
print("The opponent is the SHOOTING crew on purpose: against an all-melee mirror,")
print("'never shot at' is true by construction and would measure nothing.\n")
print(f"  {'hidden mode':<14}{'build':<20}{'d mean':>9}{'rnds hidden':>13}"
      f"{'times shot at':>15}{'kills':>8}{'survived':>10}")

COLLECT = {'hid': lambda c: c[0].rounds_hidden,
           'shot': lambda c: c[0].times_targeted,
           'k': lambda c: c[0].kills,
           'alive': lambda c: 1.0 if c[0].standing() else 0.0}

for hmode in ('modifier', 'untargetable'):
    dials(STEALTH_ON=True, HIDDEN_MODE=hmode, HIDDEN_HOLDS=True,
          AMBUSH_PAYOFF=1, ATTACK_BACK=True)
    for label, cf in (('plain stealth kit', False), ('COMBO on fighter 0', True)):
        m, dh, da, _, st = paired(AGI6, combo_first=cf, collect=COLLECT, foe=DEX6)
        print(f"  {hmode:<14}{label:<20}{m:>+8.1f} {st['hid']:>13.2f}"
              f"{st['shot']:>15.2f}{st['k']:>8.2f}{st['alive']*100:>9.1f}%")

dials(STEALTH_ON=False)
print("\n" + "=" * 104)
print("Every row is a measurement on the 2.5D engine. Dials swept, never asserted.")
print("=" * 104)

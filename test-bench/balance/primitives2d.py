# -*- coding: utf-8 -*-
"""Primitive exchange rates, measured on the 2.5D engine.

WHY THIS EXISTS
---------------
The atoms folded into points/ticks.py by Milestone 1 (+1 to-hit 22 / +1 Damage 15
/ +1 Stress 7) come from balance/realistic.py, which runs on crew_sim.py — a
board that documents itself as 1D, with no side swapping. The completion plan
records that a 1D armour result was later shown to be an artefact in 2.5D. That
makes the 1D provenance of the anchor a live risk.

This harness re-asks the same question of engine2d/ so the two can be compared.

METHOD (identical to realistic.py, so the numbers are comparable)
  - one side is given a free +1 of a single primitive, every model
  - win-rate delta vs that side's own baseline, divided by models buffed
  - sides swapped every game, so deployment and activation order cancel
  - two scenarios: Hold (presence-scored, the dominant balance lever) and
    Annihilate (pure kill, the closest analogue to what the 1D sim measures)

It does NOT modify the engine. Game.injure is wrapped for the duration of the
run so buffs can be applied; nothing in engine2d/ is edited.
"""
import sys, os, random, copy

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

from engine import Game, Unit, core
from board import take_a_hold, dist
from policies import BALANCED
from data import WEAPONS, ARMOUR

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000

BUFF = {'dmg': 0, 'arm': 0, 'stress': 0}


# --- patched injure: honours dmg / arm / stress buffs ------------------------
# Mirrors engine.Game.injure exactly, plus the buff terms.
def injure(self, att, dfn, ranged, payload=None):
    sk = att.shaken()
    mod = WEAPONS[att.weapon]['dmg'] + ARMOUR[dfn.armour]['injury'] - sk
    if getattr(att, 'buffed', False):
        mod += BUFF['dmg']
    if getattr(dfn, 'buffed', False):
        mod -= BUFF['arm']
    if core(mod):
        dfn.w -= 1
        if dfn.w <= 0:
            self.go_down(dfn, ranged)
        else:
            self.add_stress(dfn, 1)
        return True
    if payload == 'fire':
        dfn.fire = True
    elif ranged:
        dfn.pinned = True
    self.add_stress(dfn, 1)
    if BUFF['stress'] and getattr(att, 'buffed', False):
        self.add_stress(dfn, BUFF['stress'])
    return False


Game.injure = injure


class Annihilate(Game):
    """Straight kill. VP = enemy models removed from play."""
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


def _pol(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


# --- realistic lists: everyone who can hold a gun, holds one -----------------
# Mirrors balance/realistic.py. engine2d has no shotgun profile, so the
# Fireteam's Specialist carries a rifle instead.
def GUNLINE4(side):        # 96 — long-range elite, light armour
    return _pol([
        Unit('Boss',  side, 'Leader',     'rifle', 'light', dex=4, str=2),
        Unit('Marks', side, 'Specialist', 'rifle', 'light', dex=4),
        Unit('Gun1',  side, 'Fighter',    'pistol', dex=2),
        Unit('Gun2',  side, 'Fighter',    'pistol', dex=2)])


def FIRETEAM6(side):       # 98 — mixed, all armed
    return _pol([
        Unit('Boss',  side, 'Leader',     'rifle',  dex=4, str=2),
        Unit('Marks', side, 'Specialist', 'rifle',  dex=4),
        Unit('Gun1',  side, 'Fighter',    'pistol', dex=2),
        Unit('Gun2',  side, 'Fighter',    'pistol', dex=2),
        Unit('R1',    side, 'Recruit',    'pistol', dex=1),
        Unit('R2',    side, 'Recruit',    'bat',    str=1)])


def SQUAD8(side):          # 98 — max models with almost everyone armed
    return _pol([
        Unit('Boss', side, 'Leader',  'rifle',  dex=2, str=2, nrv=2),
        Unit('F1',   side, 'Fighter', 'pistol', dex=2),
        Unit('F2',   side, 'Fighter', 'pistol', dex=2),
        Unit('F3',   side, 'Fighter', 'pistol', dex=2),
        Unit('R1',   side, 'Recruit', 'pistol', dex=1),
        Unit('R2',   side, 'Recruit', 'pistol', dex=1),
        Unit('R3',   side, 'Recruit', 'bat'),
        Unit('R4',   side, 'Recruit', 'bat')])


# --- the M2 pair: armour bought with bodies ---------------------------------
def MOB11(side):           # 97 — bare melee horde
    c = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2, skills=('knockback',)) for i in range(5)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _pol(c)


def ARMOURED7(side):       # 95 — same melee, everyone in scrap plate
    c = [Unit('Boss', side, 'Leader', 'sledge', 'improvised', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', 'improvised', str=2, skills=('knockback',)) for i in range(4)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat', 'improvised') for i in range(2)]
    return _pol(c)


def tag(crew, hit):
    for u in crew:
        u.buffed = True
        u.stats['dex'] += hit
        u.stats['str'] += hit
    return crew


def versus(mkA, mkB, GameCls, n, hit=0, seed=20260730):
    """Win rate for A, sides swapped every game. A carries the buff."""
    random.seed(seed)
    a = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = GameCls(tag(mkA(0), hit), mkB(1), board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(mkB(0), tag(mkA(1), hit), board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
    return (a + 0.5 * dr) / n


PRIMS = [
    ('+1 to-hit', dict(hit=1, dmg=0, arm=0, stress=0)),
    ('+1 Damage', dict(hit=0, dmg=1, arm=0, stress=0)),
    ('+1 Armour', dict(hit=0, dmg=0, arm=1, stress=0)),
    ('+1 Stress', dict(hit=0, dmg=0, arm=0, stress=1)),
]

LISTS = {'Gunline (4)': (GUNLINE4, 4), 'Fireteam (6)': (FIRETEAM6, 6),
         'Squad (8)': (SQUAD8, 8)}
SCEN = {'Hold': Game, 'Annihilate': Annihilate}

print("=" * 100)
print(f"PRIMITIVE EXCHANGE RATES ON THE 2.5D ENGINE   ({N} games/cell, sides swapped)")
print("Compare against balance/realistic.py, which measured the same thing in 1D.")
print("=" * 100)

per_model = {}      # (scenario, primitive) -> [per-model deltas]

for scen, GameCls in SCEN.items():
    print(f"\n  [{scen.upper()}]   total delta, and (per model buffed)")
    print(f"    {'primitive':<14}" + "".join(f"{n:>24}" for n in LISTS))
    base = {}
    for lname, (mk, models) in LISTS.items():
        BUFF.update(dmg=0, arm=0, stress=0)
        foe = SQUAD8 if lname != 'Squad (8)' else GUNLINE4
        base[lname] = versus(mk, foe, GameCls, N)
    print(f"    {'baseline':<14}" + "".join(f"{base[n]*100:23.1f} " for n in LISTS))
    for label, cfg in PRIMS:
        BUFF.update({k: v for k, v in cfg.items() if k != 'hit'})
        cells, pm = [], []
        for lname, (mk, models) in LISTS.items():
            foe = SQUAD8 if lname != 'Squad (8)' else GUNLINE4
            wr = versus(mk, foe, GameCls, N, hit=cfg['hit'])
            d = (wr - base[lname]) * 100
            pm.append(d / models)
            cells.append(f"{d:+13.1f} ({d/models:+5.2f})")
        per_model[(scen, label)] = pm
        print(f"    {label:<14}" + "".join(cells))

print("\n" + "=" * 100)
print("EXCHANGE RATE — mean per-model delta, and the ratio to +1 Damage")
print("=" * 100)
print(f"    {'primitive':<14}{'Hold':>10}{'Annihilate':>13}{'mean':>10}"
      f"{'rel to Dmg':>13}{'at 15-anchor':>15}")
means = {}
for label, _ in PRIMS:
    h = sum(per_model[('Hold', label)]) / 3
    a = sum(per_model[('Annihilate', label)]) / 3
    means[label] = (h + a) / 2
dmg = means['+1 Damage']
for label, _ in PRIMS:
    m = means[label]
    h = sum(per_model[('Hold', label)]) / 3
    a = sum(per_model[('Annihilate', label)]) / 3
    rel = m / dmg if dmg else float('nan')
    print(f"    {label:<14}{h:>10.4f}{a:>13.4f}{m:>10.4f}{rel:>12.4f}x{rel*15:>14.2f}")

print("\n" + "=" * 100)
print("THE M2 QUESTION — armour bought with bodies, head to head")
print("Armoured 7 (95 pts, everyone in scrap) vs Mob 11 (97 pts, bare)")
print("1D (balance/melee_armour.py) said the armoured build wins 37.9%.")
print("=" * 100)
BUFF.update(dmg=0, arm=0, stress=0)
for scen, GameCls in SCEN.items():
    wr = versus(ARMOURED7, MOB11, GameCls, N)
    print(f"    {scen:<14} Armoured 7 wins {wr*100:5.1f}%   (50% = the armour paid for itself)")
print("=" * 100)

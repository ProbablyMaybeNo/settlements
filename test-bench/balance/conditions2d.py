# -*- coding: utf-8 -*-
"""Milestone 4 — price every payload / characteristic INDIVIDUALLY.

WHY THIS EXISTS
---------------
`points/ticks.py` flat-prices six payloads at 30 by grouping them
(Concussive / Crippling / Blinding / Shocking / Toxic / Incendiary), Bleeding at
40, and several handling traits at 20-40. None of those numbers is derived from
anything. Bleed at WND 1 is a two-round death clock; Blind is a one-round -2 on
sight rolls. They cannot share a price.

METHOD — identical to balance/primitives2d.py so the numbers are comparable:
  - one side gets the characteristic free on every weapon it can carry
  - win-rate delta vs that side's own baseline, divided by models buffed
  - sides swapped every game, so deployment and activation order cancel
  - two scenarios: Hold (presence-scored) and Annihilate (pure kill)

The price falls out of the same anchor Milestone 1 used:
    +1 Damage = 15 Goods, measured at 1.1183 win-points per model in 1D.
Here the anchor is re-measured on THIS engine in the same run, so the payload
prices are internally consistent even if the absolute scale moves.

Nothing in engine2d/ is modified by this file. It registers extra WEAPONS rows
(a base profile plus one characteristic) and swaps a unit's weapon string.
"""
import sys, os, random

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED
from data import WEAPONS

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500


class Annihilate(Game):
    """Straight kill. VP = enemy models removed from play."""
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


# --- variant weapons: base profile + exactly one characteristic --------------
# Cost is copied from the base: we are measuring VALUE, not paying for it.
CHARS = [
    ('Incendiary',      'fire'),
    ('Bleeding',        'bleeding'),
    ('Toxic',           'toxic'),
    ('Blinding',        'blinding'),
    ('Shocking',        'shocking'),
    ('Concussive',      'concussive'),
    ('Crippling',       'crippling'),
    ('Heavy Impact',    'heavy_impact'),
    ('Suppressive',     'suppressive'),
    ('Armour Piercing', 'armour_piercing'),
    ('Blast',           'blast'),
]
MELEE_ONLY = {'hook'}
RANGED_ONLY = {'suppressive', 'blast'}

BASE = ('rifle', 'pistol', 'bat', 'sledge', 'crowbar', 'fists')
for _, trait in CHARS:
    for w in BASE:
        spec = dict(WEAPONS[w])
        spec['traits'] = tuple(spec['traits']) + (trait,)
        WEAPONS[f'{w}+{trait}'] = spec

# +1 Damage variants — the anchor, re-measured on this engine in the same run.
for w in BASE:
    spec = dict(WEAPONS[w])
    spec['dmg'] = spec['dmg'] + 1
    WEAPONS[f'{w}+dmg1'] = spec


def _pol(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


# Same realistic lists primitives2d.py uses, so results sit on the same footing.
def GUNLINE4(side):
    return _pol([
        Unit('Boss',  side, 'Leader',     'rifle', 'light', dex=4, str=2),
        Unit('Marks', side, 'Specialist', 'rifle', 'light', dex=4),
        Unit('Gun1',  side, 'Fighter',    'pistol', dex=2),
        Unit('Gun2',  side, 'Fighter',    'pistol', dex=2)])


def FIRETEAM6(side):
    return _pol([
        Unit('Boss',  side, 'Leader',     'rifle',  dex=4, str=2),
        Unit('Marks', side, 'Specialist', 'rifle',  dex=4),
        Unit('Gun1',  side, 'Fighter',    'pistol', dex=2),
        Unit('Gun2',  side, 'Fighter',    'pistol', dex=2),
        Unit('R1',    side, 'Recruit',    'pistol', dex=1),
        Unit('R2',    side, 'Recruit',    'bat',    str=1)])


def SQUAD8(side):
    return _pol([
        Unit('Boss', side, 'Leader',  'rifle',  dex=2, str=2, nrv=2),
        Unit('F1',   side, 'Fighter', 'pistol', dex=2),
        Unit('F2',   side, 'Fighter', 'pistol', dex=2),
        Unit('F3',   side, 'Fighter', 'pistol', dex=2),
        Unit('R1',   side, 'Recruit', 'pistol', dex=1),
        Unit('R2',   side, 'Recruit', 'pistol', dex=1),
        Unit('R3',   side, 'Recruit', 'bat'),
        Unit('R4',   side, 'Recruit', 'bat')])


def ARMOURED6(side):
    """A list in armour — the only way Armour Piercing can be measured at all.
    Against the bare lists above AP is worth exactly nothing, by definition."""
    return _pol([
        Unit('Boss',  side, 'Leader',     'rifle',  'heavy', dex=4, str=2),
        Unit('Marks', side, 'Specialist', 'rifle',  'heavy', dex=4),
        Unit('Gun1',  side, 'Fighter',    'pistol', 'light', dex=2),
        Unit('Gun2',  side, 'Fighter',    'pistol', 'light', dex=2),
        Unit('R1',    side, 'Recruit',    'pistol', 'light', dex=1),
        Unit('R2',    side, 'Recruit',    'bat',    'light', str=1)])


LISTS = {'Gunline (4)': (GUNLINE4, 4), 'Fireteam (6)': (FIRETEAM6, 6), 'Squad (8)': (SQUAD8, 8)}
SCEN = {'Hold': Game, 'Annihilate': Annihilate}


def upgrade(crew, trait):
    """Swap each eligible weapon for its variant. Returns models actually buffed —
    a ranged-only trait on a bat-carrier buys nothing, and must not be counted."""
    n = 0
    for u in crew:
        rng = WEAPONS[u.weapon]['rng']
        if trait in RANGED_ONLY and rng == 0:
            continue
        if trait in MELEE_ONLY and rng > 0:
            continue
        variant = f'{u.weapon}+{trait}'
        if variant in WEAPONS:
            u.weapon = variant
            n += 1
    return n


def versus(mkA, mkB, GameCls, n, trait=None, seed=20260801):
    random.seed(seed)
    a = dr = 0
    buffed = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            ca = mkA(0)
            if trait:
                buffed = upgrade(ca, trait)
            r = GameCls(ca, mkB(1), board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            ca = mkA(1)
            if trait:
                buffed = upgrade(ca, trait)
            r = GameCls(mkB(0), ca, board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
    return (a + 0.5 * dr) / n, buffed


def foe_of(lname):
    return SQUAD8 if lname != 'Squad (8)' else GUNLINE4


print("=" * 104)
print(f"CHARACTERISTIC EXCHANGE RATES — each priced on its own  ({N} games/cell, sides swapped)")
print("Anchor: +1 Damage = 15 Goods, re-measured on this engine in this run.")
print("=" * 104)

rows = [('+1 Damage (anchor)', 'dmg1')] + [(n, t) for n, t in CHARS]
per_model = {}

for scen, GameCls in SCEN.items():
    print(f"\n  [{scen.upper()}]   win-rate delta, and (per model buffed)")
    print(f"    {'characteristic':<20}" + "".join(f"{n:>25}" for n in LISTS))
    base = {}
    for lname, (mk, _) in LISTS.items():
        base[lname], _ = versus(mk, foe_of(lname), GameCls, N)
    print(f"    {'baseline':<20}" + "".join(f"{base[n]*100:24.1f} " for n in LISTS))
    for label, trait in rows:
        cells, pm = [], []
        for lname, (mk, _) in LISTS.items():
            wr, nb = versus(mk, foe_of(lname), GameCls, N, trait=trait)
            d = (wr - base[lname]) * 100
            if nb:
                pm.append(d / nb)
                cells.append(f"{d:+13.1f} ({d/nb:+5.2f}/{nb})")
            else:
                cells.append(f"{'n/a':>24} ")
        per_model[(scen, label)] = pm
        print(f"    {label:<20}" + "".join(cells))

print("\n" + "=" * 104)
print("PRICE — mean per-model delta, ratio to +1 Damage, and the Goods price at the 15-anchor")
print("=" * 104)
print(f"    {'characteristic':<20}{'Hold':>9}{'Annih':>9}{'mean':>9}{'rel to Dmg':>13}"
      f"{'measured':>11}{'in ticks.py':>13}")

CURRENT = {
    '+1 Damage (anchor)': 15, 'Incendiary': 30, 'Bleeding': 40, 'Toxic': 30,
    'Blinding': 30, 'Shocking': 30, 'Concussive': 30, 'Crippling': 30,
    'Heavy Impact': 30, 'Suppressive': 40, 'Armour Piercing': 15, 'Blast': 40,
}

means = {}
for label, _ in rows:
    vals = []
    for scen in SCEN:
        p = per_model[(scen, label)]
        if p:
            vals.append(sum(p) / len(p))
    means[label] = sum(vals) / len(vals) if vals else 0.0

anchor = means['+1 Damage (anchor)']
out = {}
for label, _ in rows:
    m = means[label]
    h = per_model[('Hold', label)]
    a = per_model[('Annihilate', label)]
    hm = sum(h) / len(h) if h else 0.0
    am = sum(a) / len(a) if a else 0.0
    rel = m / anchor if anchor else float('nan')
    price = rel * 15
    out[label] = price
    print(f"    {label:<20}{hm:>9.3f}{am:>9.3f}{m:>9.3f}{rel:>12.3f}x"
          f"{price:>11.0f}{CURRENT.get(label, 0):>13}")

print("\n  Anchor check: +1 Damage measured at "
      f"{anchor:.3f} win-points per model on this engine.")
print("  A negative or near-zero measurement means the characteristic is not doing")
print("  measurable work in this simulator — report it, do not price it.")

# ---------------------------------------------------------------------------
# MIRROR PASS — the same question without the floor/ceiling problem.
#
# Above, Gunline's Hold baseline is ~8% and Squad's ~92%. A buff applied at
# either end has almost no room to move the number, so every delta is
# compressed toward zero and the prices come out low across the board.
# A mirror match is 50% by construction: maximum sensitivity, no clipping,
# and deployment/activation asymmetries cancel exactly.
# ---------------------------------------------------------------------------
print("\n\n" + "=" * 104)
print(f"MIRROR PASS — identical crews, one side buffed  ({N} games/cell)")
print("Baseline is exactly 50% by symmetry, so nothing is clipped at the ends.")
print("=" * 104)

MIRRORS = {'Fireteam (6)': (FIRETEAM6, 6), 'Squad (8)': (SQUAD8, 8), 'Armoured (6)': (ARMOURED6, 6)}


def mirror(mk, GameCls, n, trait, seed=20260801):
    """A vs an identical A. Only side A is upgraded. Returns win% for the buffed side."""
    random.seed(seed)
    a = dr = 0
    buffed = 0
    for i in range(n):
        board = take_a_hold()
        ca, cb = mk(0), mk(1)
        if i % 2 == 0:
            buffed = upgrade(ca, trait)
            r = GameCls(ca, cb, board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            buffed = upgrade(cb, trait)
            r = GameCls(ca, cb, board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
    return (a + 0.5 * dr) / n, buffed


mirror_pm = {}
for scen, GameCls in SCEN.items():
    print(f"\n  [{scen.upper()}]   win% for the buffed side (50 = worth nothing), and (per model)")
    print(f"    {'characteristic':<20}" + "".join(f"{n:>25}" for n in MIRRORS))
    for label, trait in rows:
        cells, pm = [], []
        for lname, (mk, _) in MIRRORS.items():
            wr, nb = mirror(mk, GameCls, N, trait)
            d = (wr - 0.5) * 100
            if nb:
                pm.append(d / nb)
                cells.append(f"{wr*100:12.1f}% ({d/nb:+5.2f}/{nb})")
            else:
                cells.append(f"{'n/a':>24} ")
        mirror_pm[(scen, label)] = pm
        print(f"    {label:<20}" + "".join(cells))

print("\n" + "=" * 104)
print("MIRROR PRICE — the number to trust")
print("=" * 104)
print(f"    {'characteristic':<20}{'Hold':>9}{'Annih':>9}{'mean':>9}{'rel to Dmg':>13}"
      f"{'MIRROR':>9}{'asym':>8}{'ticks.py':>10}")

mmeans = {}
for label, _ in rows:
    vals = []
    for scen in SCEN:
        p = mirror_pm[(scen, label)]
        if p:
            vals.append(sum(p) / len(p))
    mmeans[label] = sum(vals) / len(vals) if vals else 0.0

manchor = mmeans['+1 Damage (anchor)']
for label, _ in rows:
    m = mmeans[label]
    h = mirror_pm[('Hold', label)]
    a = mirror_pm[('Annihilate', label)]
    hm = sum(h) / len(h) if h else 0.0
    am = sum(a) / len(a) if a else 0.0
    rel = m / manchor if manchor else float('nan')
    print(f"    {label:<20}{hm:>9.3f}{am:>9.3f}{m:>9.3f}{rel:>12.3f}x"
          f"{rel*15:>9.0f}{out[label]:>8.0f}{CURRENT.get(label, 0):>10}")

print(f"\n  Mirror anchor: +1 Damage = {manchor:.3f} win-points per model "
      f"(asymmetric pass said {anchor:.3f}).")
print("  'Armoured (6)' is the only column where Armour Piercing can do anything;")
print("  read AP from the mirror mean, never from the bare-list columns.")

# -*- coding: utf-8 -*-
"""What is one Goods actually worth in win probability? (2.5D)

WHY THIS EXISTS
---------------
primitives.py, realistic.py and primitives2d.py all measure the SAME thing: the
value of primitives *relative to each other*. None of them sets the absolute
level. The completion plan closes that by fiat — "Anchoring on +1 Damage = 15
Goods" — and 15 is the value of TICK_STAT in ticks.py, not a measurement.

That matters for the M2 armour gate. The "4x gap" between measured armour
(~15/point) and charged armour (Light 60) is a comparison between a RELATIVE
measurement and an ABSOLUTE legacy table. Before moving armour, it is worth
knowing whether the anchor itself is right.

METHOD
------
Take a fixed crew and remove known quantities of Goods from it (drop a model,
downgrade a weapon). Measure the win-rate cost of each removal against a fixed
foe, sides swapped. Regress win-points lost on Goods removed. The slope is
win-points per Goods; its inverse is Goods per win-point.

Then any primitive measured in win-points/model converts straight to Goods.

This is the same method balance/rof_cost.py used to price Rate of Fire 2 — pay
for the thing in dropped kit — generalised and run on the 2.5D engine.

engine2d costs are at the 100-scale; ticks.py is at the 1000-scale. Goods = 10x.
"""
import sys, os, random

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


def _pol(crew):
    for u in crew:
        u.policy = BALANCED
    return crew


def SQUAD8(side):          # the fixed opponent, 98 pts
    return _pol([
        Unit('Boss', side, 'Leader',  'rifle',  dex=2, str=2, nrv=2),
        Unit('F1',   side, 'Fighter', 'pistol', dex=2),
        Unit('F2',   side, 'Fighter', 'pistol', dex=2),
        Unit('F3',   side, 'Fighter', 'pistol', dex=2),
        Unit('R1',   side, 'Recruit', 'pistol', dex=1),
        Unit('R2',   side, 'Recruit', 'pistol', dex=1),
        Unit('R3',   side, 'Recruit', 'bat'),
        Unit('R4',   side, 'Recruit', 'bat')])


# --- the test crew, and progressively cheaper versions of it ----------------
# Each variant removes a KNOWN number of points. Nothing else changes.
def make_fireteam(drop=(), downgrade=()):
    def build(side):
        c = []
        spec = [
            ('Boss',  'Leader',     'rifle',  dict(dex=4, str=2)),
            ('Marks', 'Specialist', 'rifle',  dict(dex=4)),
            ('Gun1',  'Fighter',    'pistol', dict(dex=2)),
            ('Gun2',  'Fighter',    'pistol', dict(dex=2)),
            ('R1',    'Recruit',    'pistol', dict(dex=1)),
            ('R2',    'Recruit',    'bat',    dict(str=1)),
        ]
        for name, rank, wpn, st in spec:
            if name in drop:
                continue
            if name in downgrade:
                wpn = downgrade[name] if isinstance(downgrade, dict) else 'bat'
            c.append(Unit(name, side, rank, wpn, **st))
        return _pol(c)
    return build


BASE = make_fireteam()

VARIANTS = [
    ('baseline',                    BASE,                                       0),
    ('R2 bat -> fists',             make_fireteam(downgrade={'R2': 'fists'}),   0),
    ('Gun2 pistol -> bat',          make_fireteam(downgrade={'Gun2': 'bat'}),   4),
    ('Marks rifle -> pistol',       make_fireteam(downgrade={'Marks': 'pistol'}), 6),
    ('drop R2 (Recruit, bat)',      make_fireteam(drop=('R2',)),                5),
    ('drop R1 (Recruit, pistol)',   make_fireteam(drop=('R1',)),                9),
    ('drop Gun2 (Fighter, pistol)', make_fireteam(drop=('Gun2',)),             12),
    ('drop R1 + R2',                make_fireteam(drop=('R1', 'R2')),          14),
    ('drop R1 + R2 + Gun2',         make_fireteam(drop=('R1', 'R2', 'Gun2')),  26),
]


def versus(mkA, mkB, GameCls, n, seed=20260730):
    random.seed(seed)
    a = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = GameCls(mkA(0), mkB(1), board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(mkB(0), mkA(1), board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
    return (a + 0.5 * dr) / n


def ols(xs, ys):
    """Least squares through the origin: y = b*x. Returns b."""
    return sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)


SCEN = {'Hold': Game, 'Annihilate': Annihilate}

print("=" * 100)
print(f"WHAT IS ONE GOODS WORTH?   ({N} games/variant, sides swapped, 2.5D)")
print("Fireteam 6 (98 pts) vs a fixed Squad 8. Points are removed; the cost is measured.")
print("=" * 100)

slopes = {}
for scen, GameCls in SCEN.items():
    print(f"\n  [{scen.upper()}]")
    print(f"    {'variant':<30}{'models':>7}{'pts':>5}{'gave up':>9}{'win%':>8}{'delta':>8}")
    base = None
    xs, ys = [], []
    for label, build, given in VARIANTS:
        crew = build(0)
        wr = versus(build, SQUAD8, GameCls, N)
        if base is None:
            base = wr
            print(f"    {label:<30}{len(crew):>7}{sum(u.cost for u in crew):>5}"
                  f"{given:>9}{wr*100:>8.1f}{'—':>8}")
            continue
        d = (wr - base) * 100
        if given:
            xs.append(given * 10)     # 100-scale points -> Goods
            ys.append(-d)             # win-points LOST
        print(f"    {label:<30}{len(crew):>7}{sum(u.cost for u in crew):>5}"
              f"{given:>9}{wr*100:>8.1f}{d:>+8.1f}")
    b = ols(xs, ys)                   # win-points lost per Goods removed
    slopes[scen] = b
    print(f"\n    slope: {b:.4f} win-points per Goods"
          f"   ->   1 win-point = {1/b:>6.1f} Goods")

print("\n" + "=" * 100)
print("CONVERTING THE MEASURED PRIMITIVES INTO ABSOLUTE GOODS")
print("=" * 100)
# per-model win-point values measured by primitives2d.py at N=2000, sides swapped
PRIM_2D = {
    '+1 to-hit': dict(Hold=1.2705, Annihilate=2.2014),
    '+1 Damage': dict(Hold=0.5764, Annihilate=1.2313),
    '+1 Armour': dict(Hold=0.4198, Annihilate=1.3438),
    '+1 Stress': dict(Hold=0.0795, Annihilate=1.1257),
}
print(f"    {'primitive':<14}{'Hold Goods':>13}{'Annih Goods':>14}{'mean':>10}"
      f"{'ticks.py':>12}")
TICKS = {'+1 to-hit': 22, '+1 Damage': 15, '+1 Armour': '60 (Light)', '+1 Stress': 7}
for name, vals in PRIM_2D.items():
    g = {s: vals[s] / slopes[s] for s in SCEN}
    mean = sum(g.values()) / len(g)
    print(f"    {name:<14}{g['Hold']:>13.1f}{g['Annihilate']:>14.1f}{mean:>10.1f}"
          f"{str(TICKS[name]):>12}")
print("\n    (Hold and Annihilate disagree hard — that IS the finding. A primitive's")
print("     absolute worth depends on how the scenario scores, so a single global")
print("     price is a weighted bet on the scenario mix, not a fact about the gun.)")
print("=" * 100)

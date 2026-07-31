# -*- coding: utf-8 -*-
"""BODY-COST SWEEP — at what price do bodies stop dominating?

At each price point every crew is REBUILT to the same budget, so the swarms
shrink while the elites barely move. Verdict metric = spread of win rates.
"""
import sys, os, random, itertools, time

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

import data
from engine import Game, Unit
from board import take_a_hold, dist
from policies import BALANCED

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
BUDGET = 100


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


class Breakthrough(Game):
    def score_objectives(self, rnd):
        if rnd >= 2:
            self.vp[0] += sum(1 for u in self._standing(0) if u.pos[1] > 18.0)
            self.vp[1] += sum(1 for u in self._standing(1) if u.pos[1] < 18.0)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


SCENARIOS = {
    'Hold':         (Game, dict()),
    'Hold+Claim':   (Game, dict(claim=True)),
    'Annihilate':   (Annihilate, dict()),
    'Breakthrough': (Breakthrough, dict()),
}

def C(rank, weapon='bat', armour='none', equip=(), dep=None):
    return data.unit_cost(rank, weapon, armour, equip, dep)

def _p(crew):
    for u in crew:
        u.policy = BALANCED
    return crew

# ---- crew GENERATORS: fill to budget at whatever the current prices are -----
def horde(side):
    """Max bodies, melee. Pyramid-legal: Recruits never exceed Fighters."""
    crew = [Unit('Boss', side, 'Leader', 'bat', str=2, nrv=2, skills=('knockback',))]
    spent = C('Leader', 'bat')
    nf = nr = 0
    while True:
        if nr < nf and spent + C('Recruit', 'bat') <= BUDGET:
            crew.append(Unit(f'R{nr}', side, 'Recruit', 'bat')); spent += C('Recruit', 'bat'); nr += 1
        elif spent + C('Fighter', 'bat') <= BUDGET:
            crew.append(Unit(f'F{nf}', side, 'Fighter', 'bat', str=2)); spent += C('Fighter', 'bat'); nf += 1
        else:
            break
    return _p(crew)

def mob(side):
    """Melee, Leader with a sledge, then bodies."""
    crew = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=('knockback',))]
    spent = C('Leader', 'sledge')
    nf = nr = 0
    while True:
        if nr < nf and spent + C('Recruit', 'bat') <= BUDGET:
            crew.append(Unit(f'R{nr}', side, 'Recruit', 'bat')); spent += C('Recruit', 'bat'); nr += 1
        elif spent + C('Fighter', 'bat') <= BUDGET:
            crew.append(Unit(f'F{nf}', side, 'Fighter', 'bat', str=2, skills=('knockback',)))
            spent += C('Fighter', 'bat'); nf += 1
        else:
            break
    return _p(crew)

def armoured(side):
    """Melee in scrap plate."""
    crew = [Unit('Boss', side, 'Leader', 'sledge', 'improvised', str=4, nrv=2, skills=('knockback',))]
    spent = C('Leader', 'sledge', 'improvised')
    nf = nr = 0
    while True:
        if nr < nf and spent + C('Recruit', 'bat', 'improvised') <= BUDGET:
            crew.append(Unit(f'R{nr}', side, 'Recruit', 'bat', 'improvised'))
            spent += C('Recruit', 'bat', 'improvised'); nr += 1
        elif spent + C('Fighter', 'bat', 'improvised') <= BUDGET:
            crew.append(Unit(f'F{nf}', side, 'Fighter', 'bat', 'improvised', str=2, skills=('knockback',)))
            spent += C('Fighter', 'bat', 'improvised'); nf += 1
        else:
            break
    return _p(crew)

def gunline(side):
    """Leader + Specialist with rifles and light armour, then armed Fighters."""
    crew = [Unit('Boss', side, 'Leader', 'rifle', 'light', dex=4, nrv=2, skills=('sharp_eyes',)),
            Unit('Marks', side, 'Specialist', 'rifle', 'light', dex=4, skills=('ready_to_react',))]
    spent = C('Leader', 'rifle', 'light') + C('Specialist', 'rifle', 'light')
    i = 0
    while spent + C('Fighter', 'pistol') <= BUDGET:
        crew.append(Unit(f'G{i}', side, 'Fighter', 'pistol', dex=2))
        spent += C('Fighter', 'pistol'); i += 1
    return _p(crew)

def elite(side):
    """Heavy armour, rifles, as few models as possible."""
    crew = [Unit('Boss', side, 'Leader', 'rifle', 'heavy', dex=4, nrv=2, skills=('sharp_eyes',)),
            Unit('Marks', side, 'Specialist', 'rifle', 'heavy', dex=4)]
    spent = C('Leader', 'rifle', 'heavy') + C('Specialist', 'rifle', 'heavy')
    i = 0
    while spent + C('Fighter', 'pistol', 'light') <= BUDGET:
        crew.append(Unit(f'E{i}', side, 'Fighter', 'pistol', 'light', dex=2))
        spent += C('Fighter', 'pistol', 'light'); i += 1
    return _p(crew)

def balanced(side):
    """The canonical mixed crew — Leader rifle, a brawler, a shooter, then filler."""
    crew = [Unit('Boss', side, 'Leader', 'rifle', dex=2, int=2, nrv=2, skills=('sharp_eyes', 'keep_moving')),
            Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=('knockback',)),
            Unit('Deadeye', side, 'Fighter', 'pistol', dex=2, skills=('ready_to_react',))]
    spent = C('Leader', 'rifle') + C('Fighter', 'crowbar') + C('Fighter', 'pistol')
    i = 0
    while spent + C('Fighter', 'bat') <= BUDGET:
        crew.append(Unit(f'B{i}', side, 'Fighter', 'bat', str=2 if i % 2 else 0, nrv=2 if i % 2 == 0 else 0))
        spent += C('Fighter', 'bat'); i += 1
    return _p(crew)

CREWS = {'Horde': horde, 'Mob': mob, 'Armoured': armoured,
         'Balanced': balanced, 'Gunline': gunline, 'Elite': elite}

PRICES = [(5, 8), (6, 10), (7, 12), (8, 14), (10, 16), (12, 20)]


def versus(a, b, GameCls, kw, n, seed=20260730):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = GameCls(a(0), b(1), board, **kw).play()
            x, y = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(b(0), a(1), board, **kw).play()
            x, y = r['winner'] == 'B', r['winner'] == 'A'
        wa += x; wb += y; dr += (not x and not y)
    return (wa + 0.5 * dr) / n


names = list(CREWS)
print("=" * 104)
print(f"BODY-COST SWEEP   ({N} games/pairing, sides swapped, crews rebuilt to {BUDGET} pts at each price)")
print("=" * 104)
t0 = time.time()
results = {}

for rec, fig in PRICES:
    data.RANKS['Recruit']['cost'] = rec
    data.RANKS['Fighter']['cost'] = fig
    sizes = {n: len(CREWS[n](0)) for n in names}
    label = f"R{rec}/F{fig}"
    print(f"\n{'=' * 104}")
    print(f"[{label}]  crew sizes: " + "  ".join(f"{n} {sizes[n]}" for n in names))
    wr = {n: {} for n in names}
    per_sc = {}
    for sc, (GameCls, kw) in SCENARIOS.items():
        w2 = {n: {} for n in names}
        for a, b in itertools.combinations(names, 2):
            v = versus(CREWS[a], CREWS[b], GameCls, kw, N)
            w2[a][b] = v; w2[b][a] = 1 - v
        ov = {n: sum(w2[n].values()) / (len(names) - 1) for n in names}
        per_sc[sc] = ov
    means = {n: sum(per_sc[s][n] for s in SCENARIOS) / len(SCENARIOS) for n in names}
    spread = (max(means.values()) - min(means.values())) * 100
    results[label] = (means, spread, sizes)
    print(f"  {'crew':<10}" + "".join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
    for n in names:
        print(f"  {n:<10}" + "".join(f"{per_sc[s][n]*100:12.0f} " for s in SCENARIOS)
              + f"{means[n]*100:7.0f}")
    print(f"  >>> SPREAD {spread:.0f} points   "
          f"(best {max(means, key=means.get)}, worst {min(means, key=means.get)})")

print(f"\n{'=' * 104}")
print("SWEEP SUMMARY — mean win % by crew, and the spread at each price")
print(f"  {'price':<10}" + "".join(f"{n[:9]:>10}" for n in names) + f"{'SPREAD':>9}")
for label, (means, spread, sizes) in results.items():
    print(f"  {label:<10}" + "".join(f"{means[n]*100:9.0f} " for n in names) + f"{spread:8.0f}")
print(f"\n  crew sizes by price:")
for label, (_, _, sizes) in results.items():
    print(f"  {label:<10}" + "  ".join(f"{n} {sizes[n]}" for n in names))
best = min(results.items(), key=lambda kv: kv[1][1])
print(f"\n  TIGHTEST SPREAD: {best[0]} at {best[1][1]:.0f} points")
print(f"  elapsed {time.time()-t0:.0f}s")
print("=" * 104)

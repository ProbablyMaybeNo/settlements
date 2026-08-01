# -*- coding: utf-8 -*-
"""What is a weapon class actually worth, measured against bodies?

The class costs (rifle 100, sidearm 40, ...) are the last legacy numbers in the
engine — inherited from the old hand-set table and never derived. Everything
else in the catalogue is priced relative to them, so if they are wrong the whole
table is skewed.

Method: the body-trade that worked for RoF and armour. Sweep the class price;
rebuild every crew to 100 pts at each point; find where the gun-heavy builds sit
at parity with the body-heavy ones.
"""
import sys, os, random, itertools, time

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

import data
from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 250
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


SCEN = {'Hold': (Game, dict()), 'Claim': (Game, dict(claim=True)),
        'Annihilate': (Annihilate, dict()), 'Breakthrough': (Breakthrough, dict())}


def C(rank, weapon='bat', armour='none'):
    return data.unit_cost(rank, weapon, armour)


def _p(c):
    for u in c:
        u.policy = BALANCED
    return c


def _fill_melee(side, crew, spent):
    nf = nr = 0
    while True:
        if nr < nf and spent + C('Recruit', 'bat') <= BUDGET:
            crew.append(Unit(f'R{nr}', side, 'Recruit', 'bat'))
            spent += C('Recruit', 'bat'); nr += 1
        elif spent + C('Fighter', 'bat') <= BUDGET:
            crew.append(Unit(f'F{nf}', side, 'Fighter', 'bat', str=2, skills=('knockback',)))
            spent += C('Fighter', 'bat'); nf += 1
        else:
            break
    return _p(crew)


def mob(side):
    """No guns at all — the control. Never changes with the rifle price."""
    c = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=('knockback',))]
    return _fill_melee(side, c, C('Leader', 'sledge'))


def gunline(side):
    """Every model that can hold a rifle, holds one."""
    c = [Unit('Boss', side, 'Leader', 'rifle', 'light', dex=4, nrv=2, skills=('sharp_eyes',))]
    spent = C('Leader', 'rifle', 'light')
    i = 0
    while spent + C('Fighter', 'rifle') <= BUDGET:
        c.append(Unit(f'G{i}', side, 'Fighter', 'rifle', dex=2, skills=('ready_to_react',)))
        spent += C('Fighter', 'rifle'); i += 1
    while spent + C('Recruit', 'pistol') <= BUDGET:
        c.append(Unit(f'P{i}', side, 'Recruit', 'pistol', dex=1))
        spent += C('Recruit', 'pistol'); i += 1
    return _p(c)


def mixed(side):
    """One rifle, then bodies — the middle of the road."""
    c = [Unit('Boss', side, 'Leader', 'rifle', dex=4, nrv=2, skills=('sharp_eyes',))]
    spent = C('Leader', 'rifle')
    nf = nr = 0
    while True:
        if nr < nf and spent + C('Recruit', 'bat') <= BUDGET:
            c.append(Unit(f'R{nr}', side, 'Recruit', 'bat'))
            spent += C('Recruit', 'bat'); nr += 1
        elif spent + C('Fighter', 'bat') <= BUDGET:
            c.append(Unit(f'F{nf}', side, 'Fighter', 'bat', str=2))
            spent += C('Fighter', 'bat'); nf += 1
        else:
            break
    return _p(c)


CREWS = {'Gunline': gunline, 'Mixed': mixed, 'Mob (control)': mob}
names = list(CREWS)


def versus(a, b, G, kw, n, seed=20260731):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = G(a(0), b(1), board, **kw).play()
            x, y = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = G(b(0), a(1), board, **kw).play()
            x, y = r['winner'] == 'B', r['winner'] == 'A'
        wa += x; wb += y; dr += (not x and not y)
    return (wa + 0.5 * dr) / n


print("=" * 98)
print(f"WEAPON CLASS PRICE — what is a rifle worth in bodies?   ({N} games/pairing)")
print("Rifle = 'standard_ranged'. Legacy price 10 at the 100-scale (100 at the 1000-scale).")
print("=" * 98)
t0 = time.time()

for rc in (6, 8, 10, 12, 15, 18):
    data.WEAPONS['rifle'] = dict(rng=18, dmg=3, kind='ranged', cost=rc,
                                 traits=('loud', 'two_handed'))
    sizes = {n: len(CREWS[n](0)) for n in names}
    per = {}
    for sc, (G, kw) in SCEN.items():
        w = {n: {} for n in names}
        for a, b in itertools.combinations(names, 2):
            v = versus(CREWS[a], CREWS[b], G, kw, N)
            w[a][b] = v
            w[b][a] = 1 - v
        per[sc] = {n: sum(w[n].values()) / (len(names) - 1) for n in names}
    means = {n: sum(per[s][n] for s in SCEN) / len(SCEN) for n in names}
    spread = (max(means.values()) - min(means.values())) * 100
    print(f"\n[rifle {rc} / {rc*10} at the 1000-scale]   sizes: "
          + "  ".join(f"{n.split()[0]} {sizes[n]}" for n in names))
    print("   " + "   ".join(f"{n} {means[n]*100:.0f}%" for n in names)
          + f"      spread {spread:.0f}")
    print("     per scenario  " + "  ".join(
        f"{s} [{'/'.join(f'{per[s][n]*100:.0f}' for n in names)}]" for s in SCEN))

print(f"\n  Parity = Gunline and Mob sitting on top of each other.")
print(f"  elapsed {time.time()-t0:.0f}s")
print("=" * 98)

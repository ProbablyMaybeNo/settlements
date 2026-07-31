# -*- coding: utf-8 -*-
"""Is KNOCKBACK the real culprit? Same crews, same prices, skill on vs off."""
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
KB = {'on': True}


def sk(*names):
    """Filter knockback out when the toggle is off."""
    return tuple(s for s in names if s != 'knockback' or KB['on'])


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

SCENARIOS = {'Hold': (Game, dict()), 'Hold+Claim': (Game, dict(claim=True)),
             'Annihilate': (Annihilate, dict()), 'Breakthrough': (Breakthrough, dict())}

def _p(c):
    for u in c: u.policy = BALANCED
    return c

def horde(side):
    c = [Unit('Boss', side, 'Leader', 'bat', str=2, nrv=2, skills=sk('knockback'))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2) for i in range(6)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _p(c)

def mob(side):
    c = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=sk('knockback'))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2, skills=sk('knockback')) for i in range(5)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _p(c)

def armoured(side):
    c = [Unit('Boss', side, 'Leader', 'sledge', 'improvised', str=4, nrv=2, skills=sk('knockback'))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', 'improvised', str=2, skills=sk('knockback')) for i in range(4)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat', 'improvised') for i in range(2)]
    return _p(c)

def balanced(side):
    return _p([
        Unit('Boss', side, 'Leader', 'rifle', dex=2, int=2, nrv=2, skills=('sharp_eyes', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=sk('knockback')),
        Unit('Deadeye', side, 'Fighter', 'pistol', dex=2, skills=('ready_to_react',)),
        Unit('Wire', side, 'Fighter', 'bat', int=2, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner', side, 'Fighter', 'molotov', agi=2),
        Unit('Nerves', side, 'Fighter', 'bat', nrv=2, skills=('stare_down',))])

def gunline(side):
    return _p([
        Unit('Boss', side, 'Leader', 'rifle', 'light', dex=4, nrv=2, skills=('sharp_eyes',)),
        Unit('Marks', side, 'Specialist', 'rifle', 'light', dex=4, skills=('ready_to_react',)),
        Unit('G0', side, 'Fighter', 'pistol', dex=2),
        Unit('G1', side, 'Fighter', 'pistol', dex=2)])

def elite(side):
    return _p([
        Unit('Boss', side, 'Leader', 'rifle', 'heavy', dex=4, nrv=2, skills=('sharp_eyes',)),
        Unit('Marks', side, 'Specialist', 'rifle', 'heavy', dex=4),
        Unit('E0', side, 'Fighter', 'pistol', dex=2)])

CREWS = {'Horde': horde, 'Mob': mob, 'Armoured': armoured,
         'Balanced': balanced, 'Gunline': gunline, 'Elite': elite}
names = list(CREWS)


def versus(a, b, G, kw, n, seed=20260730):
    random.seed(seed)
    wa = wb = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = G(a(0), b(1), board, **kw).play(); x, y = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = G(b(0), a(1), board, **kw).play(); x, y = r['winner'] == 'B', r['winner'] == 'A'
        wa += x; wb += y; dr += (not x and not y)
    return (wa + 0.5 * dr) / n


print("=" * 100)
print(f"KNOCKBACK TEST   ({N} games/pairing, sides swapped, prices unchanged at R5/F8)")
print("=" * 100)
t0 = time.time()
out = {}

for state in ('on', 'off'):
    KB['on'] = (state == 'on')
    per_sc = {}
    for sc, (G, kw) in SCENARIOS.items():
        w = {n: {} for n in names}
        for a, b in itertools.combinations(names, 2):
            v = versus(CREWS[a], CREWS[b], G, kw, N)
            w[a][b] = v; w[b][a] = 1 - v
        per_sc[sc] = {n: sum(w[n].values()) / (len(names) - 1) for n in names}
    means = {n: sum(per_sc[s][n] for s in SCENARIOS) / len(SCENARIOS) for n in names}
    spread = (max(means.values()) - min(means.values())) * 100
    out[state] = (means, spread, per_sc)
    print(f"\n[KNOCKBACK {state.upper()}]")
    print(f"  {'crew':<10}" + "".join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'MEAN':>8}")
    for n in names:
        print(f"  {n:<10}" + "".join(f"{per_sc[s][n]*100:12.0f} " for s in SCENARIOS)
              + f"{means[n]*100:7.0f}")
    print(f"  >>> SPREAD {spread:.0f}   (best {max(means, key=means.get)}, "
          f"worst {min(means, key=means.get)})")

print(f"\n{'=' * 100}")
print("EFFECT OF REMOVING KNOCKBACK")
print(f"  {'crew':<10}{'with':>8}{'without':>10}{'delta':>9}")
mo, so, _ = out['on']
mf, sf, _ = out['off']
for n in names:
    print(f"  {n:<10}{mo[n]*100:7.0f} {mf[n]*100:9.0f} {(mf[n]-mo[n])*100:+8.0f}")
print(f"\n  SPREAD  with {so:.0f}  ->  without {sf:.0f}   ({sf-so:+.0f})")
print(f"  elapsed {time.time()-t0:.0f}s")
print("=" * 100)

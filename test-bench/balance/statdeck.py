# -*- coding: utf-8 -*-
"""STAT-VARIED SCENARIO DECK — does keying each scenario to a different stat
flatten the spread without any cost changes or caps?

Every objective needs an ACTION + a test. The stat tested varies by scenario.
Two stats per scenario (best of) so no crew is hard-countered.
"""
import sys, os, random, itertools, time

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

from engine import Game, Unit, core
from board import take_a_hold, dist
from policies import BALANCED

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 250


class StatClaim(Game):
    """Objectives are claimed with an Action + a test on the scenario's stat(s)."""
    STATS = ('int',)
    def try_claim(self, u):
        if not self.claim_mode:
            return False
        for i, o in enumerate(self.objectives):
            if dist(u.pos, o) > 3.0 or self.claims[i] == u.side:
                continue
            best = max(u.stats[s] for s in self.STATS)
            bonus = 1 if ('hacker' in u.skills and 'int' in self.STATS) else 0
            bonus += 1 if ('breach_kit' in u.equip and 'int' in self.STATS) else 0
            if core(best + bonus - u.shaken()):
                self.claims[i] = u.side
            return True
        return False

def deck(*stats):
    return type('S_' + '_'.join(stats), (StatClaim,), {'STATS': stats})

class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))

class PositionalHold(Game):
    pass   # the current rules: presence only, no test

SCENARIOS = {
    'Hold (NRV/STR)':   (deck('nrv', 'str'), dict(claim=True)),
    'Power (INT)':      (deck('int'),        dict(claim=True)),
    'Sabotage (INT/DEX)': (deck('int', 'dex'), dict(claim=True)),
    'Raid (STR/DEX)':   (deck('str', 'dex'), dict(claim=True)),
    'Extract (AGI)':    (deck('agi'),        dict(claim=True)),
    'Annihilate':       (Annihilate,         dict()),
}

CONTROL = {'Hold (positional)': (PositionalHold, dict())}


def _p(c):
    for u in c: u.policy = BALANCED
    return c

def horde(side):
    c = [Unit('Boss', side, 'Leader', 'bat', str=2, nrv=2)]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2) for i in range(6)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _p(c)

def mob(side):
    c = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2, skills=('knockback',)) for i in range(5)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _p(c)

def armoured(side):
    c = [Unit('Boss', side, 'Leader', 'sledge', 'light', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', 'light', str=2, skills=('knockback',)) for i in range(4)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat', 'light') for i in range(2)]
    return _p(c)

def balanced(side):
    return _p([
        Unit('Boss', side, 'Leader', 'rifle', dex=2, int=2, nrv=2, skills=('sharp_eyes', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=('knockback',)),
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


def sweep(scen):
    out = {}
    for sc, (G, kw) in scen.items():
        w = {n: {} for n in names}
        for a, b in itertools.combinations(names, 2):
            v = versus(CREWS[a], CREWS[b], G, kw, N)
            w[a][b] = v; w[b][a] = 1 - v
        out[sc] = {n: sum(w[n].values()) / (len(names) - 1) for n in names}
    return out


t0 = time.time()
print("=" * 108)
print(f"STAT-VARIED SCENARIO DECK   ({N} games/pairing, sides swapped) — no cost changes, no caps")
print("=" * 108)

ctrl = sweep(CONTROL)
cv = ctrl['Hold (positional)']
print(f"\n[CONTROL] current rules — Hold scored by PRESENCE only")
print(f"  " + "  ".join(f"{n} {cv[n]*100:.0f}%" for n in names))
print(f"  SPREAD {(max(cv.values())-min(cv.values()))*100:.0f} points")

res = sweep(SCENARIOS)
print(f"\n{'=' * 108}")
print("[STAT-VARIED DECK] every objective = Action + a test; stat varies by scenario")
print(f"  {'crew':<10}" + "".join(f"{s.split(' (')[0][:9]:>11}" for s in SCENARIOS) + f"{'MEAN':>8}")
means = {}
for n in names:
    vals = [res[s][n] for s in SCENARIOS]
    means[n] = sum(vals) / len(vals)
    print(f"  {n:<10}" + "".join(f"{v*100:10.0f} " for v in vals) + f"{means[n]*100:7.0f}")

print(f"\n  per-scenario spread: " + "  ".join(
    f"{s.split(' (')[0]} {(max(res[s].values())-min(res[s].values()))*100:.0f}" for s in SCENARIOS))
sp = (max(means.values()) - min(means.values())) * 100
print(f"\n  >>> OVERALL SPREAD {sp:.0f} points  "
      f"(best {max(means, key=means.get)} {max(means.values())*100:.0f}%, "
      f"worst {min(means, key=means.get)} {min(means.values())*100:.0f}%)")

print(f"\n{'=' * 108}")
print("BEFORE / AFTER")
print(f"  {'crew':<10}{'positional Hold':>17}{'stat deck mean':>17}{'delta':>9}")
for n in names:
    print(f"  {n:<10}{cv[n]*100:16.0f} {means[n]*100:16.0f} {(means[n]-cv[n])*100:+8.0f}")
print(f"\n  spread: positional Hold {(max(cv.values())-min(cv.values()))*100:.0f}"
      f"  ->  stat deck {sp:.0f}")
print(f"  elapsed {time.time()-t0:.0f}s")
print("=" * 108)

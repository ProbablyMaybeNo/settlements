# -*- coding: utf-8 -*-
"""SETTLEMENTS — FULL BALANCE SUITE (2.5D engine)

8 crew archetypes x 5 scenario types, sides swapped every game.
Verdict metric = spread of overall win rates. Tight spread = balanced.
"""
import sys, os, random, itertools, time

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

from engine import Game, Unit
from board import take_a_hold, dist, Piece
from policies import POLICIES, BALANCED, RUNNER, HUNTER

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 200

# ============================ SCENARIOS =====================================
class Annihilate(Game):
    """Straight kill. VP = enemy models removed from play."""
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


class Loot(Game):
    """6 scattered caches. First crew to reach one banks it permanently."""
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.looted = {}
    def score_objectives(self, rnd):
        for i, o in enumerate(self.objectives):
            if i in self.looted:
                continue
            for side in (0, 1):
                if any(dist(u.pos, o) <= 2.0 for u in self._standing(side)):
                    self.looted[i] = side
                    self.vp[side] += 1
                    break
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


class Breakthrough(Game):
    """Push through. VP for each standing model in the enemy HALF (past the centreline)."""
    def score_objectives(self, rnd):
        if rnd >= 2:
            self.vp[0] += sum(1 for u in self._standing(0) if u.pos[1] > 18.0)
            self.vp[1] += sum(1 for u in self._standing(1) if u.pos[1] < 18.0)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


def loot_board():
    b = take_a_hold()
    b['objectives'] = [(6, 12), (18, 12), (30, 12), (6, 24), (18, 24), (30, 24)]
    return b


SCENARIOS = {
    'Hold':         (take_a_hold, Game,         dict()),
    'Hold+Claim':   (take_a_hold, Game,         dict(claim=True)),
    'Annihilate':   (take_a_hold, Annihilate,   dict()),
    'Loot':         (loot_board,  Loot,         dict()),
    'Breakthrough': (take_a_hold, Breakthrough, dict()),
}

# ============================== CREWS =======================================
def _pol(crew, policy=BALANCED):
    for u in crew:
        u.policy = policy
    return crew

def gunline4(side):        # 96 — long-range elite, light armour
    return _pol([
        Unit('Boss', side, 'Leader', 'rifle', 'light', dex=4, nrv=2, skills=('sharp_eyes',)),
        Unit('Marks', side, 'Specialist', 'rifle', 'light', dex=4, skills=('ready_to_react',)),
        Unit('Gun1', side, 'Fighter', 'pistol', dex=2),
        Unit('Gun2', side, 'Fighter', 'pistol', dex=2)])

def redline6(side):        # 98 — the canonical balanced mirror crew
    return _pol([
        Unit('Boss', side, 'Leader', 'rifle', dex=2, int=2, nrv=2, skills=('sharp_eyes', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol', dex=2, skills=('ready_to_react',)),
        Unit('Wire', side, 'Fighter', 'bat', int=2, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner', side, 'Fighter', 'molotov', agi=2),
        Unit('Nerves', side, 'Fighter', 'bat', nrv=2, skills=('stare_down',))])

def mob11(side):           # 97 — bare melee horde
    c = [Unit('Boss', side, 'Leader', 'sledge', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2, skills=('knockback',)) for i in range(5)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _pol(c)

def armoured7(side):       # 95 — melee, everyone in scrap plate
    c = [Unit('Boss', side, 'Leader', 'sledge', 'light', str=4, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', 'light', str=2, skills=('knockback',)) for i in range(4)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat', 'light') for i in range(2)]
    return _pol(c)

def turret5(side):         # 97 — static gunline with hardware
    return _pol([
        Unit('Boss', side, 'Leader', 'rifle', dex=4, nrv=2, skills=('sharp_eyes',)),
        Unit('Marks', side, 'Specialist', 'rifle', dex=2, int=2),
        Unit('Tech', side, 'Fighter', 'bat', int=2, deployable='autoturret'),
        Unit('Gun', side, 'Fighter', 'pistol', dex=2),
        Unit('Rec', side, 'Recruit', 'bat')])

def skirmish6(side):       # 94 — mobile, incendiary, mid-range
    return _pol([
        Unit('Boss', side, 'Leader', 'rifle', dex=2, agi=2, nrv=2, skills=('keep_moving',)),
        Unit('Fire1', side, 'Fighter', 'molotov', agi=2),
        Unit('Fire2', side, 'Fighter', 'molotov', agi=2),
        Unit('Gun', side, 'Fighter', 'pistol', dex=2),
        Unit('R1', side, 'Recruit', 'pistol'),
        Unit('R2', side, 'Recruit', 'bat')])

def elite3(side):          # 92 — three heavily armoured shooters
    return _pol([
        Unit('Boss', side, 'Leader', 'rifle', 'heavy', dex=4, nrv=2, skills=('sharp_eyes',)),
        Unit('Marks', side, 'Specialist', 'rifle', 'heavy', dex=4),
        Unit('Gun', side, 'Fighter', 'pistol', dex=2)])

def horde12(side):         # 97 — maximum bodies, legal pyramid
    c = [Unit('Boss', side, 'Leader', 'bat', str=2, nrv=2, skills=('knockback',))]
    c += [Unit(f'F{i}', side, 'Fighter', 'bat', str=2) for i in range(6)]
    c += [Unit(f'R{i}', side, 'Recruit', 'bat') for i in range(5)]
    return _pol(c)

CREWS = {'Gunline 4': gunline4, 'Redline 6': redline6, 'Mob 11': mob11,
         'Armoured 7': armoured7, 'Turret 5': turret5, 'Skirmish 6': skirmish6,
         'Elite 3': elite3, 'Horde 12': horde12}


def versus(buildA, buildB, board_fn, GameCls, kw, n, seed=20260730):
    random.seed(seed)
    a = b = dr = 0
    for i in range(n):
        board = board_fn()
        if i % 2 == 0:
            r = GameCls(buildA(0), buildB(1), board, **kw).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = GameCls(buildB(0), buildA(1), board, **kw).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw; b += bw; dr += (not aw and not bw)
    return (a + 0.5 * dr) / n


print("=" * 100)
print(f"SETTLEMENTS — FULL BALANCE SUITE   ({N} games/pairing, sides swapped, 2.5D engine)")
print("=" * 100)
print(f"\n  {'crew':<13}{'models':>7}{'pts':>6}   composition")
for name, mk in CREWS.items():
    c = mk(0)
    print(f"  {name:<13}{len(c):>7}{sum(u.cost for u in c):>6}   "
          + ", ".join(sorted({u.weapon for u in c})))

names = list(CREWS)
overall = {}
t0 = time.time()

for sc, (board_fn, GameCls, kw) in SCENARIOS.items():
    print(f"\n{'=' * 100}\n[{sc.upper()}]   row wins % vs column")
    print(f"  {'':<13}" + "".join(f"{n[:10]:>11}" for n in names))
    wr = {n: {} for n in names}
    for a, b in itertools.combinations(names, 2):
        v = versus(CREWS[a], CREWS[b], board_fn, GameCls, kw, N)
        wr[a][b] = v
        wr[b][a] = 1 - v
    for rn in names:
        cells = "".join("      —    " if cn == rn else f"{wr[rn][cn]*100:10.0f} "
                        for cn in names)
        print(f"  {rn:<13}{cells}")
    ov = {n: sum(wr[n].values()) / (len(names) - 1) for n in names}
    overall[sc] = ov
    lo, hi = min(ov.values()), max(ov.values())
    print(f"\n  overall: " + "  ".join(f"{n.split()[0]} {v*100:.0f}%"
                                       for n, v in sorted(ov.items(), key=lambda x: -x[1])))
    print(f"  SPREAD: {(hi-lo)*100:.0f} points   "
          f"(best {max(ov, key=ov.get)}, worst {min(ov, key=ov.get)})")

print(f"\n{'=' * 100}\nSUMMARY — overall win % by crew and scenario")
print(f"  {'crew':<13}" + "".join(f"{s[:11]:>13}" for s in SCENARIOS) + f"{'mean':>8}{'range':>8}")
for n in names:
    vals = [overall[s][n] for s in SCENARIOS]
    print(f"  {n:<13}" + "".join(f"{v*100:12.0f} " for v in vals)
          + f"{sum(vals)/len(vals)*100:7.0f} {(max(vals)-min(vals))*100:7.0f}")
print(f"\n  per-scenario spread: "
      + "  ".join(f"{s} {(max(overall[s].values())-min(overall[s].values()))*100:.0f}"
                  for s in SCENARIOS))
print(f"\n  elapsed {time.time()-t0:.0f}s")
print("=" * 100)

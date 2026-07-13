"""Settlements — crew-sim calibration sweep.

Two questions:
  1. At what terrain density does elite-vs-swarm sit at 50/50? (i.e. where does the
     '9 large features per 3x3' rule actually put the game?)
  2. Does The Mob doctrine's bunching rule ('ignore Stress from a friendly going Down
     while within 2" of two or more friendlies') rescue the swarm, and does it
     over-rescue it?
"""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

import crew_sim as CS

N = 3000

def make_terrain(blocked):
    """Interpolate the cover mix + witness rate with LOS density."""
    t = (blocked - 0.10) / 0.50                      # 0 at sparse, 1 at very dense
    t = max(0.0, min(1.0, t))
    open_w  = 0.55 - 0.45 * t
    light_w = 0.30
    heavy_w = 1.0 - open_w - light_w
    witness = 0.85 - 0.60 * t
    return dict(blocked=blocked, cover=(open_w, light_w, heavy_w), witness=witness)

def run(a_fn, b_fn, terrain, n=N):
    CS.TERRAIN['_sweep'] = terrain
    w = d = 0
    for _ in range(n):
        res, *_ = CS.battle(a_fn(), b_fn(), '_sweep')
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / n

# --- The Mob doctrine: patch the witness rule ---------------------------------
_orig_go_down = CS.go_down

def go_down_mob(u, ranged, allies, T):
    """Allies within 2" of 2+ friendlies take no Stress from a Down (The Mob)."""
    if ranged: u['down'] = True
    else: u['out'] = True
    for a in CS.eff(allies):
        if a is u: continue
        if a.get('_mob'):
            near = sum(1 for f in CS.eff(allies)
                       if f is not a and abs(f['pos'] - a['pos']) <= 2.0)
            if near >= 2: continue
        if random.random() < T['witness']:
            CS.add_stress(a, 1)

def MOB_DOCTRINE():
    c = CS.RABBLE_HORDE()
    for f in c: f['_mob'] = True
    return c

if __name__ == '__main__':
    random.seed(20260713)

    print("=" * 78)
    print("SETTLEMENTS — CREW SIM CALIBRATION   (N = %d battles/point)" % N)
    print("=" * 78)

    print("\n[1] TERRAIN SWEEP — where is the elite/swarm balance point?")
    print("    Cadre(4) win% vs each swarm, as LOS-blocking rises.")
    print("    A 3'x3' is nine 12\" squares; roughly, 1 big feature per square ~= 35-40% blocked.\n")
    hdr = f"    {'blocked':>8}{'witness':>9}"
    swarms = [('Recruit horde (9)', CS.RECRUIT_HORDE),
              ('Pyramid mob (11)', CS.PYRAMID_MOB),
              ('Rabble horde (14)', CS.RABBLE_HORDE)]
    print(hdr + "".join(f"{n:>20}" for n, _ in swarms))
    for blocked in (0.10, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60):
        T = make_terrain(blocked)
        row = [run(CS.CADRE, fn, T) for _, fn in swarms]
        print(f"    {blocked:>7.0%} {T['witness']:>8.0%}"
              + "".join(f"{w*100:>19.0f}%" for w in row))
    print("\n    (50% = the two lists are correctly costed against each other.)")

    print("\n[2] THE MOB DOCTRINE — does the bunching rule rescue the swarm?")
    print("    'Ignore Stress from a friendly going Down while within 2\" of 2+ friendlies'")
    print(f"\n    {'blocked':>8}{'Rabble horde':>16}{'+ Mob doctrine':>17}{'delta':>9}")
    for blocked in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60):
        T = make_terrain(blocked)
        base = 1 - run(CS.CADRE, CS.RABBLE_HORDE, T)
        CS.go_down = go_down_mob
        mob = 1 - run(CS.CADRE, MOB_DOCTRINE, T)
        CS.go_down = _orig_go_down
        print(f"    {blocked:>7.0%}{base*100:>15.0f}%{mob*100:>16.0f}%"
              f"{(mob-base)*100:>+8.0f}")
    print("\n    (horde win% vs the Cadre. Doctrine should lift the sparse-board floor")
    print("     without breaking the dense-board ceiling.)")

    print("\n[3] STAT ALLOCATION — what should a Recruit actually buy?")
    print("    9-model horde vs Cadre(4), by what the Recruits put their 2 points into.\n")
    def horde(**kw):
        def f():
            return [CS.fighter('Leader', 'shotgun', str=4, nrv=2)] + \
                   [CS.fighter('Recruit', 'bat', **kw) for _ in range(8)]
        return f
    builds = [('STR +2 (fight)', dict(str=2)),
              ('NRV +2 (nerve)', dict(nrv=2)),
              ('STR+1 / NRV+1', dict(str=1, nrv=1)),
              ('DEX +2 (guns)', dict(dex=2))]
    print(f"    {'recruit build':<18}{'sparse 10%':>12}{'mid 35%':>10}{'dense 55%':>12}")
    for lbl, kw in builds:
        row = [1 - run(CS.CADRE, horde(**kw), make_terrain(b))
               for b in (0.10, 0.35, 0.55)]
        print(f"    {lbl:<18}" + "".join(f"{w*100:>11.0f}%" for w in row))

    print("\n" + "=" * 78)

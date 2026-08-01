"""Settlements CREW-SCALE sim — validates the List Building point costs.

Mirrors the locked engine: core 1d10+stat>=7 (nat1 fail / nat10 pass), opposed melee
ties->defender, injury 1d10+Damage-Armor>=7, Shaken -1 at 1+ Stress (not on the Break
test), Break test at 2+: 1d10+NRV-(Stress-1)>=7 -> Bolt(2)/Broken(3)/BugOut(4+).
Ranged kill = Down; melee kill = Out of Action. Orders are issued only on the issuing
unit's own activation (ruling 2026-07-13). Ready persists across rounds.

Board is modelled in 1D: 36" long, deployment 6" from each edge (24" apart). Terrain is
probabilistic - a density setting drives P(LOS blocked) per shot, the cover distribution
for shots that do connect, and P(a friendly witnesses a Down).

NOT modelled (deliberate, first pass): objectives, skills, hacking, terrain interaction,
flanking, Hidden, stabilise/bleed-out (a Down fighter is simply out of the fight).
This sim prices the COMBAT FLOOR only - utility stats are priced by the board, per the
existing thesis in Dice Mechanic - Sim Findings s6.
"""
import random, sys
from collections import Counter
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

SEED = 20260713
N = 3000
BOARD = 36.0
DEPLOY = 6.0
ROUNDS = 6

def d10(): return random.randint(1, 10)

def core(mod, target=7):
    d = d10()
    if d == 1: return False
    if d == 10: return True
    return d + mod >= target

def opposed(mod_a, mod_b):          # ties -> defender
    return d10() + mod_a > d10() + mod_b

# --- terrain -----------------------------------------------------------------
# blocked = P(no LOS on a given shot); cover = weights for open/light/heavy;
# witness = P(a friendly sees a Down and takes the Stress.
TERRAIN = {
    'open':   dict(blocked=0.10, cover=(0.55, 0.30, 0.15), witness=0.85),
    'medium': dict(blocked=0.30, cover=(0.25, 0.40, 0.35), witness=0.55),
    'dense':  dict(blocked=0.55, cover=(0.10, 0.30, 0.60), witness=0.30),
}
COVER_MOD = (0, -1, -2)

WEAPONS = {
    'fists':     dict(rng=0,  dmg=0, cost=0),
    'bat':       dict(rng=0,  dmg=1, cost=0),
    'sledge':    dict(rng=0,  dmg=2, cost=4),
    'pistol':    dict(rng=8,  dmg=2, cost=4),
    'shotgun':   dict(rng=10, dmg=3, cost=8),
    'rifle':     dict(rng=18, dmg=3, cost=12),
}
ARMOUR = {'none': (0, 0), 'light': (-1, 3), 'heavy': (-2, 6)}
RANK   = {'Recruit': 5, 'Fighter': 8, 'Specialist': 16, 'Leader': 24}
ORDERS = {'Recruit': 0, 'Fighter': 0, 'Specialist': 1, 'Leader': 2}

def fighter(rank, weapon='bat', armour='none', **stats):
    f = dict(rank=rank, str=0, dex=0, agi=0, int=0, nrv=0, mov=6.0, wnd=1,
             weapon=weapon, armour=armour)
    f.update(stats)
    f['cost'] = RANK[rank] + WEAPONS[weapon]['cost'] + ARMOUR[armour][1]
    f['orders'] = ORDERS[rank]
    return f

def crew_cost(crew): return sum(f['cost'] for f in crew)

# --- battle state ------------------------------------------------------------
def spawn(crew, side):
    us = []
    for f in crew:
        u = dict(f)
        u.update(side=side, w=f['wnd'], stress=0, gained=0, pinned=False, down=False,
                 out=False, ready=False, skip=False, acted=False, ordered=False,
                 pos=(DEPLOY if side == 0 else BOARD - DEPLOY))
        us.append(u)
    return us

def live(us):   return [u for u in us if not u['out']]
def eff(us):    return [u for u in us if not u['out'] and not u['down']]
def shaken(u):  return 1 if u['stress'] >= 1 else 0

def add_stress(u, n=1):
    u['stress'] += n
    u['gained'] += n

def go_down(u, ranged, allies, T):
    if ranged:
        u['down'] = True
    else:
        u['out'] = True
    for a in eff(allies):
        if a is not u and random.random() < T['witness']:
            add_stress(a, 1)

def injure(att, dfn, ranged, dfn_allies, T):
    sk = shaken(att)
    if core(WEAPONS[att['weapon']]['dmg'] + ARMOUR[dfn['armour']][0] - sk):
        dfn['w'] -= 1
        if dfn['w'] <= 0:
            go_down(dfn, ranged, dfn_allies, T)
        else:
            add_stress(dfn, 1)
        return True
    # no wound: ranged -> Pinned; melee -> Shaken. Both are +1 Stress.
    if ranged: dfn['pinned'] = True
    add_stress(dfn, 1)
    return False

def cover_of(T):
    return COVER_MOD[random.choices((0, 1, 2), weights=T['cover'])[0]]

def can_see(T): return random.random() >= T['blocked']

def shoot(att, dfn, dfn_allies, T):
    rng = WEAPONS[att['weapon']]['rng']
    if rng == 0: return False
    if abs(att['pos'] - dfn['pos']) > rng: return False
    if not can_see(T): return False
    cov = cover_of(T)
    if dfn['down']: cov = min(cov, -2)          # Down = heavy cover vs ranged
    if core(att['dex'] + cov - shaken(att)):
        injure(att, dfn, True, dfn_allies, T)
    return True

def fight(att, dfn, dfn_allies, T, charge=0):
    if dfn['down']:                              # melee auto-hits a Down fighter
        injure(att, dfn, False, dfn_allies, T)
        return
    if opposed(att['str'] + charge - shaken(att), dfn['str'] - shaken(dfn)):
        injure(att, dfn, False, dfn_allies, T)
    else:
        add_stress(att, 1)                       # you lost the clash: Shaken

def nearest(u, foes):
    c = eff(foes) or live(foes)
    return min(c, key=lambda e: abs(e['pos'] - u['pos'])) if c else None

def engaged(u, foes):
    return [e for e in live(foes) if abs(e['pos'] - u['pos']) <= 1.0]

def has_gun(u): return WEAPONS[u['weapon']]['rng'] > 0

def reactions(mover, foes, mover_allies, T):
    """Every Readied enemy with LOS+range snap-shots a fighter that ends a Move."""
    for r in eff(foes):
        if not r['ready'] or mover['out'] or mover['down']: continue
        if not has_gun(r): continue
        if abs(r['pos'] - mover['pos']) > WEAPONS[r['weapon']]['rng']: continue
        r['ready'] = False
        shoot(r, mover, mover_allies, T)

def take_action(u, allies, foes, T):
    """One Action slot. Returns nothing; used both for normal actions and Orders."""
    eng = engaged(u, foes)
    if eng:
        fight(u, eng[0], foes, T)
        return
    tgt = nearest(u, foes)
    if tgt and has_gun(u) and shoot(u, tgt, foes, T):
        return
    if has_gun(u):
        u['ready'] = True                        # nothing to shoot -> bank overwatch

def activate(u, allies, foes, T):
    u['acted'] = True
    if u['out'] or u['down']: return
    if u['skip']:                                # Bolt / Broken
        u['skip'] = False
        return
    eng = engaged(u, foes)
    tgt = nearest(u, foes)
    if tgt is None: return
    dist = abs(u['pos'] - tgt['pos'])
    direction = 1 if tgt['pos'] > u['pos'] else -1

    if u['pinned']:                              # Move slot must clear the Pin
        u['pinned'] = False
        if eng: fight(u, eng[0], foes, T)
        elif has_gun(u) and not shoot(u, tgt, foes, T): u['ready'] = True
        _orders(u, allies, foes, T)
        return

    if eng:                                      # already in contact: just fight
        fight(u, eng[0], foes, T)
        _orders(u, allies, foes, T)
        return

    if has_gun(u):
        if dist <= WEAPONS[u['weapon']]['rng']:
            if not shoot(u, tgt, foes, T):
                u['ready'] = True                # no LOS this activation
        else:                                    # close to range, then reactions fire
            step = min(u['mov'], dist - WEAPONS[u['weapon']]['rng'])
            u['pos'] += direction * step
            reactions(u, foes, allies, T)
            if not (u['out'] or u['down']):
                if not shoot(u, tgt, foes, T): u['ready'] = True
        _orders(u, allies, foes, T)
        return

    # melee fighter: Charge if reachable, else Sprint
    if dist <= 2 * u['mov'] and can_see(T):
        u['pos'] = tgt['pos'] - direction * 0.9
        reactions(u, foes, allies, T)
        if not (u['out'] or u['down']):
            fight(u, tgt, foes, T, charge=1)
    else:
        u['pos'] += direction * min(2 * u['mov'], max(0.0, dist - 0.9))
        reactions(u, foes, allies, T)
    _orders(u, allies, foes, T)

def _orders(u, allies, foes, T):
    """Orders are issued during the issuing unit's own activation (locked ruling)."""
    for _ in range(u['orders']):
        pool = [a for a in eff(allies) if a is not u and not a['ordered']]
        # prefer a friendly who can actually shoot something right now
        shooters = [a for a in pool if has_gun(a) and not a['pinned']
                    and nearest(a, foes)
                    and abs(a['pos'] - nearest(a, foes)['pos']) <= WEAPONS[a['weapon']]['rng']]
        brawlers = [a for a in pool if engaged(a, foes)]
        pick = (shooters or brawlers or [None])[0]
        if pick is None: break
        pick['ordered'] = True
        take_action(pick, allies, foes, T)

def break_test(u):
    if u['out'] or u['down']: return
    if u['stress'] >= 2:
        d = d10()
        pen = u['stress'] - 1
        # Shaken's -1 is NOT applied here (already in the formula)
        if d == 10 or (d != 1 and d + u['nrv'] - pen >= 7):
            u['stress'] = 0
        else:
            if u['stress'] >= 4:
                u['out'] = True                  # BugOut: removed from play
            else:
                u['skip'] = True                 # Bolt / Broken: lose next activation
            u['stress'] = max(0, u['stress'] - 1)
    elif u['stress'] == 1 and u['gained'] == 0:
        u['stress'] = 0                          # sheds only on a clean round

def battle(crewA, crewB, density, max_rounds=ROUNDS):
    T = TERRAIN[density]
    A, B = spawn(crewA, 0), spawn(crewB, 1)
    for rnd in range(max_rounds):
        if not eff(A) or not eff(B): break
        for u in A + B:
            u['acted'] = False; u['ordered'] = False; u['gained'] = 0
        pa = d10() + (1 if len(live(A)) < len(live(B)) else 0)
        pb = d10() + (1 if len(live(B)) < len(live(A)) else 0)
        while pa == pb:
            pa, pb = d10(), d10()
        first = 0 if pa > pb else 1
        while True:
            qa = [u for u in eff(A) if not u['acted']]
            qb = [u for u in eff(B) if not u['acted']]
            if not qa and not qb: break
            order = (qa, qb) if first == 0 else (qb, qa)
            moved = False
            for q, (allies, foes) in zip(order,
                    [(A, B), (B, A)] if first == 0 else [(B, A), (A, B)]):
                if q:
                    u = q[0]
                    if not u['acted'] and not u['out'] and not u['down']:
                        activate(u, allies, foes, T)
                    u['acted'] = True
                    moved = True
                if not eff(A) or not eff(B): return _score(A, B, rnd + 1)
            if not moved: break
        for u in A + B: break_test(u)
        if not eff(A) or not eff(B): return _score(A, B, rnd + 1)
    return _score(A, B, max_rounds)

def _score(A, B, rnd):
    ea, eb = len(eff(A)), len(eff(B))
    if ea and not eb: res = 'A'
    elif eb and not ea: res = 'B'
    elif ea == eb == 0: res = 'draw'
    else:
        # 6 rounds elapsed: proxy the objective game by share of crew still standing
        fa, fb = ea / len(A), eb / len(B)
        res = 'A' if fa > fb + 0.05 else 'B' if fb > fa + 0.05 else 'draw'
    return res, rnd, ea, eb

# --- the candidate lists (all built to 100 pts under the proposed costs) -------
def CADRE():        # 4 models, all shooting. Pure DEX build.
    return [fighter('Leader', 'rifle', 'light', dex=4, str=2, nrv=0),
            fighter('Specialist', 'rifle', 'light', dex=4, nrv=0),
            fighter('Fighter', 'pistol', dex=2),
            fighter('Fighter', 'pistol', dex=2)]

def CADRE_MIXED():  # same 4 models, but stats split to survive a melee
    return [fighter('Leader', 'rifle', 'light', dex=4, str=2),
            fighter('Specialist', 'rifle', 'light', dex=2, str=2),
            fighter('Fighter', 'pistol', str=2),
            fighter('Fighter', 'pistol', str=2)]

def STANDARD():     # 6 models
    return [fighter('Leader', 'rifle', dex=4, str=2),
            fighter('Specialist', 'shotgun', dex=4),
            fighter('Fighter', 'pistol', str=2),
            fighter('Fighter', 'pistol', str=2),
            fighter('Fighter', 'bat', str=2),
            fighter('Fighter', 'bat', str=2)]

def RECRUIT_HORDE():   # 9 models, STR+2 brawlers. Legal without any doctrine.
    return [fighter('Leader', 'shotgun', str=4, nrv=2)] + \
           [fighter('Fighter', 'bat', str=2) for _ in range(8)]

def RECRUIT_HORDE_NRV():  # same, but the Fighters bought Nerve instead of Strength
    return [fighter('Leader', 'shotgun', str=4, nrv=2)] + \
           [fighter('Fighter', 'bat', nrv=2) for _ in range(8)]

def PYRAMID_MOB():  # 11 models, the legal no-doctrine maximum
    return [fighter('Leader', 'shotgun', str=4, nrv=2)] + \
           [fighter('Fighter', 'bat', str=2) for _ in range(5)] + \
           [fighter('Recruit', 'bat') for _ in range(5)]

def RABBLE_HORDE(): # 14 models, needs The Mob doctrine (Recruit w/o Fighters)
    return [fighter('Leader', 'shotgun', str=4, nrv=2)] + \
           [fighter('Recruit', 'bat') for _ in range(13)]

LISTS = {
    'Cadre (4, pure DEX)':   CADRE,
    'Cadre (4, DEX/STR)':    CADRE_MIXED,
    'Standard (6)':          STANDARD,
    'Fighter horde (9 STR)': RECRUIT_HORDE,
    'Fighter horde (9 NRV)': RECRUIT_HORDE_NRV,
    'Pyramid mob (11)':      PYRAMID_MOB,
    'Recruit horde (14)':     RABBLE_HORDE,
}

def pct(x): return f"{x*100:4.0f}%"

if __name__ == '__main__':
    random.seed(SEED)
    names = list(LISTS)

    print("=" * 78)
    print(f"SETTLEMENTS — CREW SIM   (N = {N} battles/matchup, {ROUNDS} rounds, seed {SEED})")
    print("=" * 78)
    print("\n[0] THE LISTS — all built to the proposed 100-pt costs")
    print(f"    {'list':<24}{'models':>7}{'points':>8}")
    for n in names:
        c = LISTS[n]()
        print(f"    {n:<24}{len(c):>7}{crew_cost(c):>8}")

    for density in ('open', 'medium', 'dense'):
        print(f"\n[{density.upper()}]  row wins % vs column   "
              f"(blocked LOS {TERRAIN[density]['blocked']:.0%}, "
              f"witness {TERRAIN[density]['witness']:.0%})")
        print(f"    {'':<24}" + "".join(f"{n.split(' (')[0][:9]:>10}" for n in names))
        overall = {}
        for rn in names:
            cells, tot, k = [], 0.0, 0
            for cn in names:
                if rn == cn:
                    cells.append("     —    "); continue
                w = d = 0
                for _ in range(N):
                    res, *_ = battle(LISTS[rn](), LISTS[cn](), density)
                    if res == 'A': w += 1
                    elif res == 'draw': d += 1
                wr = (w + 0.5 * d) / N
                cells.append(f"{wr*100:9.0f} ")
                tot += wr; k += 1
            overall[rn] = tot / k
            print(f"    {rn:<24}" + "".join(cells))
        print(f"\n    overall win rate:")
        for n, wr in sorted(overall.items(), key=lambda x: -x[1]):
            print(f"      {n:<24}{pct(wr)}")

    # --- diagnostics ----------------------------------------------------------
    print("\n" + "=" * 78)
    print("[D] DIAGNOSTICS — Cadre(4) vs Recruit horde(14), by terrain")
    print(f"    {'terrain':<9}{'Cadre win':>11}{'avg rounds':>12}"
          f"{'Cadre alive':>13}{'Horde alive':>13}")
    for density in ('open', 'medium', 'dense'):
        w = 0; rs = 0; sa = 0; sb = 0
        for _ in range(N):
            res, rnd, ea, eb = battle(CADRE(), RABBLE_HORDE(), density)
            if res == 'A': w += 1
            rs += rnd; sa += ea; sb += eb
        print(f"    {density:<9}{pct(w/N):>11}{rs/N:>12.1f}"
              f"{sa/N:>13.1f}{sb/N:>13.1f}")

    print("\n[E] STRESS CASCADE — how often does a crew break vs get shot?")
    print("    cause of removal, Recruit horde(14) vs Cadre(4):")
    for density in ('open', 'medium', 'dense'):
        causes = Counter()
        for _ in range(400):
            T = TERRAIN[density]
            A, B = spawn(RABBLE_HORDE(), 0), spawn(CADRE(), 1)
            for rnd in range(ROUNDS):
                if not eff(A) or not eff(B): break
                for u in A + B:
                    u['acted'] = False; u['ordered'] = False; u['gained'] = 0
                first = 0 if d10() >= 5 else 1
                while True:
                    qa = [u for u in eff(A) if not u['acted']]
                    qb = [u for u in eff(B) if not u['acted']]
                    if not qa and not qb: break
                    for q, (al, fo) in (zip((qa, qb), ((A, B), (B, A))) if first == 0
                                        else zip((qb, qa), ((B, A), (A, B)))):
                        if q:
                            u = q[0]
                            if not u['acted'] and not u['out'] and not u['down']:
                                activate(u, al, fo, T)
                            u['acted'] = True
                    if not eff(A) or not eff(B): break
                pre = {id(u): (u['out'], u['down']) for u in A}
                for u in A + B: break_test(u)
                for u in A:
                    was_out, was_down = pre[id(u)]
                    if u['out'] and not was_out and not was_down:
                        causes['BugOut (Stress)'] += 1
            for u in A:
                if u['down']: causes['Down (shot)'] += 1
                elif u['out']: causes.setdefault('BugOut (Stress)', 0)
        tot = sum(causes.values()) or 1
        line = "  ".join(f"{k}: {v/400:.1f}/battle" for k, v in causes.most_common())
        print(f"    {density:<9}{line}")
    print("\n" + "=" * 78)

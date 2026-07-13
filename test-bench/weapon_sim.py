"""Settlements WEAPON SYSTEM sim — validates the construction system in Weapons.md.

Adds to the crew sim: built weapons (class + characteristics), the Payload rule
(a condition lands IN PLACE OF Pinned/Shaken when a hit fails to wound), armour,
Armour Piercing, Accurate, Spread, Brutal, Blast, Suppressive, Defensive, Balanced,
Cleaving, and the full condition suite from Conditions.md (Fire, Bleed, Poison,
Shocked, Blind, Off-Balance, Hobbled, Pinned).

Engine unchanged: 1d10+stat>=7 (nat1/nat10), opposed melee ties->defender,
injury 1d10+Damage-Armor>=7, Shaken -1 at 1+ Stress, Break at 2+.
Modifier cap +/-3 on any roll, COVER COUNTED SEPARATELY (per Terrain sim T2).
"""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

SEED = 20260713
BOARD, DEPLOY, ROUNDS = 36.0, 6.0, 6

def d10(): return random.randint(1, 10)
def core(mod, target=7):
    d = d10()
    if d == 1: return False
    if d == 10: return True
    return d + mod >= target
def opposed(a, b): return d10() + a > d10() + b

# ---------------------------------------------------------------- weapons
CLASSES = {
    'unarmed':       dict(cost=0,  dmg=0, rng=0,  hands=0, tier=0, slots=0),
    'light_melee':   dict(cost=0,  dmg=1, rng=0,  hands=1, tier=0, slots=2),
    'onehand_melee': dict(cost=4,  dmg=2, rng=0,  hands=1, tier=1, slots=2),
    'heavy_melee':   dict(cost=8,  dmg=3, rng=0,  hands=2, tier=2, slots=3),
    'thrown':        dict(cost=2,  dmg=1, rng=6,  hands=1, tier=0, slots=2),
    'sidearm':       dict(cost=4,  dmg=2, rng=8,  hands=1, tier=0, slots=2),
    'std_ranged':    dict(cost=10, dmg=3, rng=18, hands=2, tier=1, slots=3),
    'heavy_ranged':  dict(cost=14, dmg=3, rng=24, hands=2, tier=2, slots=4),
}
RANK_TIER = {'Rabble': 0, 'Recruit': 1, 'Specialist': 2, 'Leader': 2}

CHARS = dict(brutal=4, ap=4, accurate=3, spread=3,
             concussive=3, crippling=3, blinding=3, shocking=3, toxic=3,
             incendiary=3, bleeding=4, heavy_impact=3, hook=2, suppressive=4,
             blast=4, smoke=3, long_range=6, balanced=2, defensive=3,
             cleaving=5, breaching=3, concealable=2, quiet=2, compact=2)
DRAWBACKS = dict(short_range=-3, slow=-3, unstable=-2,
                 cumbersome=-2, limited=-3)
# a drawback must ALWAYS bite, or it is free points (sim, 2026-07-13)
MELEE_ONLY_DRAW = {'slow'}
RANGED_ONLY_DRAW = {'short_range'}
PAYLOAD = dict(concussive='offbalance', crippling='hobbled', blinding='blind',
               shocking='shocked', toxic='poison', incendiary='fire',
               bleeding='bleed')

def W(name, cls, *traits):
    c = CLASSES[cls]
    t = set(traits)
    chars = t & set(CHARS)
    draws = t & set(DRAWBACKS)
    assert len(chars) <= c['slots'], f"{name}: {len(chars)} chars > {c['slots']} slots"
    assert len(draws) <= 2, f"{name}: too many drawbacks"
    dmg = c['dmg'] + (1 if 'brutal' in t else 0)
    assert dmg <= 4, f"{name}: damage {dmg} over the +4 ceiling"
    if 'brutal' in t and c['rng'] > 10:
        assert 'short_range' in t, f"{name}: Brutal on a long-ranged weapon needs Short Range"
    rng = c['rng'] + (6 if 'long_range' in t else 0)
    if 'short_range' in t: rng //= 2
    rng = min(rng, 24)          # hard cap: deployment zones are 24" apart
    for dbk in draws:
        if dbk in MELEE_ONLY_DRAW:
            assert c['rng'] == 0, f"{name}: {dbk} is melee-only (free points on a gun)"
        if dbk in RANGED_ONLY_DRAW:
            assert c['rng'] > 0, f"{name}: {dbk} is ranged-only (free points in melee)"
    cost = c['cost'] + sum(CHARS[x] for x in chars) + sum(DRAWBACKS[x] for x in draws)
    return dict(name=name, cls=cls, dmg=dmg, rng=rng, cost=cost, tier=c['tier'],
                t=t, melee=(c['rng'] == 0))

# --- the sample armoury (Weapons.md s5) --------------------------------------
BAT        = W('Baseball Bat',   'light_melee')
KNIFE      = W('Kitchen Knife',  'light_melee', 'balanced', 'concealable')
CROWBAR    = W('Crowbar',        'onehand_melee', 'breaching')
FIRE_AXE   = W('Fire Axe',       'heavy_melee', 'brutal', 'bleeding')
SLEDGE     = W('Sledgehammer',   'heavy_melee', 'heavy_impact', 'breaching')
CLEAVER    = W('Reaping Hook',   'heavy_melee', 'cleaving', 'defensive')
HEAVY_PLAIN= W('Great Axe',      'heavy_melee')
PISTOL     = W('Pistol',         'sidearm')
RIFLE      = W('Assault Rifle',  'std_ranged', 'accurate')
HUNTER     = W("Grandpa's Rifle",'std_ranged', 'accurate', 'long_range')
PIPE_GUN   = W('Pipe Shotgun',   'std_ranged', 'brutal', 'spread', 'short_range', 'unstable')
MG         = W('Squad MG',       'heavy_ranged', 'suppressive', 'ap')
FLAMER     = W('Flamethrower',   'heavy_ranged', 'incendiary', 'blast', 'short_range', 'limited')
MOLOTOV    = W('Molotov',        'thrown', 'incendiary', 'blast')
BLEEDGUN   = W('Nailgun',        'std_ranged', 'bleeding')
SUPPRESSOR = W('Suppressor Rifle','std_ranged', 'suppressive')

ARMOUR = {'none': (0, 0), 'improvised': (-1, 3), 'light': (-1, 6), 'heavy': (-2, 10)}
RANK = {'Rabble': 5, 'Recruit': 8, 'Specialist': 16, 'Leader': 24}
ORDERS = {'Rabble': 0, 'Recruit': 0, 'Specialist': 1, 'Leader': 2}

def F(rank, wpn=BAT, armour='none', **st):
    assert wpn['tier'] <= RANK_TIER[rank], f"{rank} may not carry {wpn['name']}"
    f = dict(rank=rank, str=0, dex=0, agi=0, int=0, nrv=0, mov=6.0, wnd=1,
             w=wpn, armour=armour, orders=ORDERS[rank])
    f.update(st)
    f['cost'] = RANK[rank] + wpn['cost'] + ARMOUR[armour][1]
    if armour == 'heavy': f['mov'] -= 1
    if 'cumbersome' in wpn['t']: f['mov'] -= 1
    return f

def cost(crew): return sum(f['cost'] for f in crew)

# ---------------------------------------------------------------- terrain
def terrain(blocked):
    t = max(0.0, min(1.0, (blocked - 0.10) / 0.50))
    o = 0.55 - 0.45 * t
    return dict(blocked=blocked, cover=(o, 0.30, 1 - o - 0.30), witness=0.85 - 0.60 * t)
COVER = (0, -1, -2)

# ---------------------------------------------------------------- conditions
def penalty(u, sight=False):
    """All non-cover negative modifiers on this unit's roll, capped at -3."""
    p = 0
    if u['stress'] >= 1: p += 1                 # Shaken
    if 'poison' in u['c']: p += 1
    if 'shocked' in u['c']: p += 2
    if sight and 'blind' in u['c']: p += 2
    return min(p, 3)

def add_stress(u, n=1):
    u['stress'] += n; u['gained'] += n

def apply_cond(u, cond):
    if cond in u['c']: return                   # no stacking; refresh only
    u['c'].add(cond)
    add_stress(u, 1)                            # a new negative condition = +1 Stress

# ---------------------------------------------------------------- battle
def spawn(crew, side):
    out = []
    for f in crew:
        u = dict(f); u.update(side=side, hp=f['wnd'], stress=0, gained=0, c=set(),
                              pinned=False, pinlock=False, down=False, out=False,
                              ready=False, skip=False, acted=False, ordered=False,
                              used=False, broken_wpn=False,
                              pos=(DEPLOY if side == 0 else BOARD - DEPLOY))
        out.append(u)
    return out

def live(us): return [u for u in us if not u['out']]
def eff(us):  return [u for u in us if not u['out'] and not u['down']]

def go_down(u, ranged, allies, T):
    if ranged: u['down'] = True
    else: u['out'] = True
    for a in eff(allies):
        if a is not u and random.random() < T['witness']: add_stress(a, 1)

def injure(att, dfn, ranged, dfn_allies, T):
    w = att['w']
    arm = ARMOUR[dfn['armour']][0] + (1 if 'ap' in w['t'] else 0)
    arm = min(arm, 0)
    if core(w['dmg'] + arm - penalty(att)):
        dfn['hp'] -= 1
        if dfn['hp'] <= 0:
            go_down(dfn, ranged, dfn_allies, T)
            if 'bleeding' in w['t']: dfn['c'].add('bleed')   # cannot be stabilised
        else:
            add_stress(dfn, 1)
        return
    # --- no wound: the PAYLOAD lands in place of Pinned / Shaken ---
    pay = [PAYLOAD[k] for k in w['t'] if k in PAYLOAD]
    if pay:
        apply_cond(dfn, pay[0])
    elif 'heavy_impact' in w['t']:
        d = 2.0 if dfn['pos'] > att['pos'] else -2.0
        dfn['pos'] = max(0.0, min(BOARD, dfn['pos'] + d)); add_stress(dfn, 1)
    elif 'hook' in w['t']:
        dfn['pos'] += (-1.0 if dfn['pos'] > att['pos'] else 1.0); add_stress(dfn, 1)
    elif ranged:
        dfn['pinned'] = True
        if 'suppressive' in w['t']: dfn['pinlock'] = True
        add_stress(dfn, 1)
    else:
        add_stress(dfn, 1)                       # melee non-wound = Shaken

def targets_in_blast(tgt, foes):
    return [f for f in live(foes) if abs(f['pos'] - tgt['pos']) <= 2.0]

def shoot(att, tgt, foes, T):
    w = att['w']
    if w['rng'] == 0 or att['broken_wpn']: return False
    if 'limited' in w['t'] and att['used']: return False
    dist = abs(att['pos'] - tgt['pos'])
    if dist > w['rng']: return False
    if random.random() < T['blocked']: return False           # no LOS this shot
    att['used'] = True
    mod = att['dex'] - penalty(att, sight=True)
    if 'accurate' in w['t'] and not att.get('_moved'): mod += 1
    if 'spread' in w['t']: mod += 1 if dist <= w['rng'] / 2 else -1
    cov = COVER[random.choices((0, 1, 2), weights=T['cover'])[0]]
    if tgt['down']: cov = min(cov, -2)
    d = d10()
    if d == 1:
        if 'unstable' in w['t']: att['broken_wpn'] = True
        return True
    hit = (d == 10) or (d + mod + cov >= 7)
    if not hit: return True
    victims = targets_in_blast(tgt, foes) if 'blast' in w['t'] else [tgt]
    for v in victims:
        injure(att, v, True, foes, T)
    return True

def fight(att, tgt, foes, T, charge=0):
    w = att['w']
    if tgt['down']:
        injure(att, tgt, False, foes, T); return
    astat = att['agi'] if ('balanced' in w['t'] and att['agi'] > att['str']) else att['str']
    dw = tgt['w']
    dbonus = 1 if ('defensive' in dw['t'] and not tgt.get('_moved')) else 0
    if opposed(astat + charge - penalty(att), tgt['str'] + dbonus - penalty(tgt)):
        if 'cleaving' in w['t']:
            for v in [f for f in eff(foes) if abs(f['pos'] - att['pos']) <= 1.0]:
                injure(att, v, False, foes, T)
        else:
            injure(att, tgt, False, foes, T)
    else:
        add_stress(att, 1)

def nearest(u, foes):
    c = eff(foes) or live(foes)
    return min(c, key=lambda e: abs(e['pos'] - u['pos'])) if c else None
def engaged(u, foes): return [e for e in live(foes) if abs(e['pos'] - u['pos']) <= 1.0]
def has_gun(u): return u['w']['rng'] > 0 and not u['broken_wpn']

def reactions(mover, foes, mover_allies, T):
    for r in eff(foes):
        if not r['ready'] or mover['out'] or mover['down']: continue
        if 'shocked' in r['c'] or 'suppressed' in r['c']: continue
        if not has_gun(r): continue
        if abs(r['pos'] - mover['pos']) > r['w']['rng']: continue
        r['ready'] = False
        shoot(r, mover, mover_allies, T)

def do_action(u, allies, foes, T):
    eng = engaged(u, foes)
    if eng: fight(u, eng[0], foes, T); return
    t = nearest(u, foes)
    if t and has_gun(u) and shoot(u, t, foes, T): return
    if has_gun(u): u['ready'] = True

def activate(u, allies, foes, T):
    u['acted'] = True; u['_moved'] = False
    if u['out'] or u['down']: return
    if u['skip']: u['skip'] = False; return
    if 'fire' in u['c']:                              # extinguishing is worth an Action
        u['c'].discard('fire'); _orders(u, allies, foes, T); return
    t = nearest(u, foes)
    if t is None: return
    mov = u['mov'] - (2 if 'hobbled' in u['c'] else 0)
    dist = abs(u['pos'] - t['pos']); dirn = 1 if t['pos'] > u['pos'] else -1
    eng = engaged(u, foes)

    if u['pinned']:
        u['pinned'] = False
        if u['pinlock']:                              # Suppressive: whole activation
            u['pinlock'] = False; _orders(u, allies, foes, T); return
        if eng: fight(u, eng[0], foes, T)
        elif has_gun(u) and not shoot(u, t, foes, T): u['ready'] = True
        _orders(u, allies, foes, T); return

    if eng:
        fight(u, eng[0], foes, T); _orders(u, allies, foes, T); return

    if has_gun(u):
        if dist <= u['w']['rng']:
            if not shoot(u, t, foes, T): u['ready'] = True
        elif 'awkward' not in u['w']['t']:
            u['pos'] += dirn * min(mov, dist - u['w']['rng']); u['_moved'] = True
            reactions(u, foes, allies, T)
            if not (u['out'] or u['down']):
                if not shoot(u, t, foes, T): u['ready'] = True
        else:
            u['pos'] += dirn * min(mov, dist - u['w']['rng']); u['_moved'] = True
            reactions(u, foes, allies, T)
        _orders(u, allies, foes, T); return

    # melee fighter
    no_charge = 'slow' in u['w']['t'] or 'offbalance' in u['c']
    if dist <= 2 * mov and not no_charge and random.random() >= T['blocked']:
        u['pos'] = t['pos'] - dirn * 0.9; u['_moved'] = True
        reactions(u, foes, allies, T)
        if not (u['out'] or u['down']): fight(u, t, foes, T, charge=1)
    else:
        u['pos'] += dirn * min(2 * mov, max(0.0, dist - 0.9)); u['_moved'] = True
        reactions(u, foes, allies, T)
        if not (u['out'] or u['down']) and engaged(u, foes):
            fight(u, engaged(u, foes)[0], foes, T)
    _orders(u, allies, foes, T)

def _orders(u, allies, foes, T):
    for _ in range(u['orders']):
        pool = [a for a in eff(allies) if a is not u and not a['ordered']
                and not a['pinned'] and 'shocked' not in a['c']]
        shooters = [a for a in pool if has_gun(a) and nearest(a, foes)
                    and abs(a['pos'] - nearest(a, foes)['pos']) <= a['w']['rng']]
        brawlers = [a for a in pool if engaged(a, foes)]
        pick = (shooters or brawlers or [None])[0]
        if pick is None: break
        pick['ordered'] = True
        do_action(pick, allies, foes, T)

def end_phase(u, allies, T):
    if u['out']: return
    if 'fire' in u['c']:                     # Injury at +1, ignoring armour
        if core(1):
            u['hp'] -= 1
            if u['hp'] <= 0 and not u['down']: go_down(u, True, allies, T)
            elif u['hp'] <= 0: u['out'] = True
    if 'bleed' in u['c']:
        u['hp'] -= 1
        if u['hp'] <= 0:
            if u['down']: u['out'] = True     # Down + Bleed = bleeds out
            else: go_down(u, True, allies, T)
    if 'poison' in u['c'] and core(u['str']): u['c'].discard('poison')
    u['c'] -= {'shocked', 'blind'}
    u['c'] -= {'offbalance', 'hobbled'}
    if u['out'] or u['down']: return
    if u['stress'] >= 2:
        d = d10(); pen = u['stress'] - 1
        if d == 10 or (d != 1 and d + u['nrv'] - pen >= 7):
            u['stress'] = 0
        else:
            if u['stress'] >= 4: u['out'] = True
            else: u['skip'] = True
            u['stress'] = max(0, u['stress'] - 1)
    elif u['stress'] == 1 and u['gained'] == 0:
        u['stress'] = 0

def battle(cA, cB, blocked):
    T = terrain(blocked)
    A, B = spawn(cA, 0), spawn(cB, 1)
    for _ in range(ROUNDS):
        if not eff(A) or not eff(B): break
        for u in A + B: u['acted'] = u['ordered'] = False; u['gained'] = 0
        pa = d10() + (1 if len(live(A)) < len(live(B)) else 0)
        pb = d10() + (1 if len(live(B)) < len(live(A)) else 0)
        first = 0 if pa >= pb else 1
        while True:
            qa = [u for u in eff(A) if not u['acted']]
            qb = [u for u in eff(B) if not u['acted']]
            if not qa and not qb: break
            seq = [(qa, A, B), (qb, B, A)] if first == 0 else [(qb, B, A), (qa, A, B)]
            for q, al, fo in seq:
                if q:
                    u = q[0]
                    if not u['acted'] and not u['out'] and not u['down']:
                        activate(u, al, fo, T)
                    u['acted'] = True
                if not eff(A) or not eff(B): return score(A, B)
        for u in A: end_phase(u, A, T)
        for u in B: end_phase(u, B, T)
        if not eff(A) or not eff(B): return score(A, B)
    return score(A, B)

def score(A, B):
    ea, eb = len(eff(A)), len(eff(B))
    if ea and not eb: return 'A'
    if eb and not ea: return 'B'
    if ea == eb == 0: return 'draw'
    fa, fb = ea / len(A), eb / len(B)
    return 'A' if fa > fb + 0.05 else 'B' if fb > fa + 0.05 else 'draw'

def wr(a_fn, b_fn, blocked, n):
    w = d = 0
    for _ in range(n):
        r = battle(a_fn(), b_fn(), blocked)
        if r == 'A': w += 1
        elif r == 'draw': d += 1
    return (w + 0.5 * d) / n

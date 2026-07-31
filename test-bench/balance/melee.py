# -*- coding: utf-8 -*-
"""What does a melee-only crew actually need to be viable?

Candidate supports, tested one at a time then combined:
  UNSTOPPABLE  clearing a Pin costs your Action, not your Move (you keep advancing)
  FLEET        +2" MOV
  REACH        Engage at 2" instead of 1"
  PLATE        +1 Armour on every model
"""
import sys, random
from collections import Counter

sys.path.insert(0, r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench")
import crew_sim as cs
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

OPT = {'unstoppable': 0, 'fleet': 0, 'reach': 0, 'plate': 0}
F = cs.fighter

# ---- patched engagement radius ---------------------------------------------
def engaged(u, foes):
    r = 1.0 + (OPT['reach'] if u.get('buffed') else 0)
    return [e for e in cs.live(foes) if abs(e['pos'] - u['pos']) <= r]
cs.engaged = engaged

# ---- patched injure for the armour option ----------------------------------
def injure(att, dfn, ranged, dfn_allies, T):
    sk = cs.shaken(att)
    arm = cs.ARMOUR[dfn['armour']][0] - (OPT['plate'] if dfn.get('buffed') else 0)
    if cs.core(cs.WEAPONS[att['weapon']]['dmg'] + arm - sk):
        dfn['w'] -= 1
        if dfn['w'] <= 0: cs.go_down(dfn, ranged, dfn_allies, T)
        else: cs.add_stress(dfn, 1)
        return True
    if ranged: dfn['pinned'] = True
    cs.add_stress(dfn, 1)
    return False
cs.injure = injure

# ---- patched activate: UNSTOPPABLE lets a Pinned model still advance -------
_orig_activate = cs.activate
def activate(u, allies, foes, T):
    if u['pinned'] and OPT['unstoppable'] and u.get('buffed') \
            and not (u['out'] or u['down']) and not u['skip']:
        u['pinned'] = False          # cleared by the Action instead
    _orig_activate(u, allies, foes, T)
cs.activate = activate


def MELEE11():          # pure melee, no guns at all — 97 pts
    return [F('Leader', 'sledge', str=4, nrv=2)] + \
           [F('Fighter', 'bat', str=2) for _ in range(5)] + \
           [F('Recruit', 'bat') for _ in range(5)]

def MOB11():            # the stock mob (Leader has a shotgun)
    return cs.PYRAMID_MOB()

def GUNLINE4():
    return cs.CADRE()

def FIRETEAM6():
    return [F('Leader', 'rifle', dex=4, str=2),
            F('Specialist', 'shotgun', dex=4),
            F('Fighter', 'pistol', dex=2),
            F('Fighter', 'pistol', dex=2),
            F('Recruit', 'pistol', dex=1),
            F('Recruit', 'bat', str=1)]


def tag(crew):
    for f in crew:
        f['buffed'] = True
        f['mov'] += OPT['fleet']
    return crew

def run(mk_a, mk_b, density, n=2500, seed=20260713):
    random.seed(seed)
    w = d = 0
    for _ in range(n):
        res, *_ = cs.battle(tag(mk_a()), mk_b(), density)
        if res == 'A': w += 1
        elif res == 'draw': d += 1
    return (w + 0.5 * d) / n


SUPPORTS = [
    ('none (baseline)',      dict(unstoppable=0, fleet=0, reach=0, plate=0)),
    ('UNSTOPPABLE',          dict(unstoppable=1, fleet=0, reach=0, plate=0)),
    ('FLEET (+2 MOV)',       dict(unstoppable=0, fleet=2, reach=0, plate=0)),
    ('REACH (2")',           dict(unstoppable=0, fleet=0, reach=1, plate=0)),
    ('PLATE (+1 Armour)',    dict(unstoppable=0, fleet=0, reach=0, plate=1)),
    ('UNSTOPPABLE + FLEET',  dict(unstoppable=1, fleet=2, reach=0, plate=0)),
    ('UNSTOPPABLE + PLATE',  dict(unstoppable=1, fleet=0, reach=0, plate=1)),
    ('all four',             dict(unstoppable=1, fleet=2, reach=1, plate=1)),
]

FOES = [('vs Gunline(4)', GUNLINE4), ('vs Fireteam(6)', FIRETEAM6)]

print("=" * 96)
print("MELEE VIABILITY — pure-melee 11-model crew, win% with each support")
print("target: get medium density out of the 20-35% hole without breaking dense")
print("=" * 96)

for lname, mk in (('MELEE11 (no guns)', MELEE11), ('MOB11 (stock)', MOB11)):
    print(f"\n  {lname}")
    print(f"    {'support':<22}" + "".join(
        f"{f'{fn} {d}':>20}" for fn, _ in FOES for d in ('med', 'dense')))
    base = {}
    for label, cfg in SUPPORTS:
        OPT.update(cfg)
        cells = []
        for fn, foe in FOES:
            for density in ('medium', 'dense'):
                wr = run(mk, foe, density)
                k = (fn, density)
                if label.startswith('none'):
                    base[k] = wr
                    cells.append(f"{wr*100:19.1f} ")
                else:
                    cells.append(f"{wr*100:12.1f}({(wr-base[k])*100:+5.1f})")
        print(f"    {label:<22}" + "".join(cells))

print("\n" + "=" * 96)

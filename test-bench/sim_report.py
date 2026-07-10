"""Settlements dice-mechanic sim — mirrors the Test Bench engine exactly.
Standard sample = 10,000 rolls per test. Seeded for reproducibility."""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')  # Windows console is cp1252 by default
except Exception: pass
random.seed(20260708)
N = 10000

def d10(): return random.randint(1, 10)

def core_exact(mod, target=7):
    w = 0
    for d in range(1, 11):
        if d == 1: continue
        if d == 10: w += 1; continue
        if d + mod >= target: w += 1
    return w / 10

def core_roll(mod, target=7):
    d = d10()
    if d == 1: return False
    if d == 10: return True
    return d + mod >= target

def opposed_exact(dmod, tieA=False):  # attacker advantage = dmod (modA-modB)
    w = 0
    for a in range(1, 11):
        for b in range(1, 11):
            if a + dmod > b: w += 1
            elif a + dmod == b and tieA: w += 1
    return w / 100

def opposed_roll(modA, modB, tieA=False):
    a, b = d10(), d10()
    if a + modA > b + modB: return True
    if a + modA == b + modB and tieA: return True
    return False

def pct(x): return f"{x*100:5.1f}%"

print("="*72)
print("SETTLEMENTS — DICE MECHANIC SIM REPORT   (N = 10,000 rolls / test)")
print("="*72)

# ---- A. Core test curve ----
print("\n[A] CORE TEST  1d10+mod >= 7   (exact vs simulated)")
print(f"{'mod':>4} {'exact':>7} {'sim':>7}")
for mod in range(-1, 7):
    hits = sum(core_roll(mod) for _ in range(N))
    print(f"{mod:>+4} {pct(core_exact(mod)):>7} {pct(hits/N):>7}")

# ---- B. Difficulty ladder ----
print("\n[B] STAT CHECK  success% by difficulty target (exact)")
print(f"{'mod':>4} {'7+':>7} {'9+':>7} {'11+':>7}")
for mod in range(0, 7):
    print(f"{mod:>+4} {pct(core_exact(mod,7)):>7} {pct(core_exact(mod,9)):>7} {pct(core_exact(mod,11)):>7}")

# ---- C. Shooting ----
def shoot(dex, cover, dmg, arm, n=N):
    hits = wounds = 0
    for _ in range(n):
        if core_roll(dex + cover):
            hits += 1
            if core_roll(dmg + arm): wounds += 1
    return hits/n, wounds/n

print("\n[C] SHOOTING — standard shooter DEX +2, medium weapon (+2), no armour target")
print("    vary COVER:")
print(f"{'cover':>7} {'hit':>7} {'wound/shot':>11} {'shots→down':>11}")
for cov, lbl in [(0,'open'),(-1,'light'),(-2,'heavy'),(-3,'hidden')]:
    h, w = shoot(2, cov, 2, 0)
    std = f"{1/w:.1f}" if w>0 else "inf"
    print(f"{lbl:>7} {pct(h):>7} {pct(w):>11} {std:>11}")

print("\n    DEX +2, open target — vary WEAPON vs ARMOUR (wound/shot):")
print(f"{'':>7} {'arm 0':>8} {'arm -1':>8} {'arm -2':>8}")
for dmg, dl in [(1,'light+1'),(2,'med+2'),(3,'heavy+3')]:
    row = []
    for arm in [0,-1,-2]:
        _, w = shoot(2, 0, dmg, arm)
        row.append(pct(w))
    print(f"{dl:>7} {row[0]:>8} {row[1]:>8} {row[2]:>8}")

# ---- D. Melee ----
def melee(str_a, str_d, dmg, arm, charge=0, n=N):
    awin = down = 0
    for _ in range(n):
        if opposed_roll(str_a+charge, str_d):
            awin += 1
            if core_roll(dmg+arm): down += 1
    return awin/n, down/n

print("\n[D] MELEE — opposed STR, ties→defender. Attacker light weapon (+1), no armour.")
print(f"{'STR Δ':>6} {'atk wins':>9} {'+charge':>9} {'atk downs/clash':>16}")
for da in range(-2, 3):
    aw, dn = melee(2+da, 2, 1, 0)
    awc, _ = melee(2+da, 2, 1, 0, charge=1)
    print(f"{da:>+6} {pct(aw):>9} {pct(awc):>9} {pct(dn):>16}")
print("    (STR Δ 0 = even fight; note the defender's tie edge.)")

# ---- E. Head to head ----
print("\n[E] HEAD-TO-HEAD — opposed, ties→defender/B. P(A wins) by A's advantage:")
print(f"{'A adv':>6} {'exact':>7} {'sim':>7}")
for d in range(-3, 4):
    w = sum(opposed_roll(d,0) for _ in range(N))
    print(f"{d:>+6} {pct(opposed_exact(d)):>7} {pct(w/N):>7}")

# ---- F. Duel matrix (archetypes) ----
ROSTER = {
 'Brawler':          dict(mode='melee', str=4,dex=1,agi=2,int=1,nrv=2,wnd=1,dmg=2,arm=-1,cov=0),
 'Gunner':           dict(mode='ranged',str=1,dex=4,agi=2,int=1,nrv=1,wnd=1,dmg=3,arm=0, cov=0),
 'Techie':           dict(mode='ranged',str=1,dex=2,agi=2,int=4,nrv=1,wnd=1,dmg=1,arm=0, cov=0),
 'Builder':          dict(mode='melee', str=3,dex=1,agi=1,int=3,nrv=2,wnd=1,dmg=2,arm=-1,cov=0),
 'Objective Grabber':dict(mode='melee', str=1,dex=2,agi=4,int=2,nrv=2,wnd=1,dmg=1,arm=0, cov=0),
 'Heavy Gunner':     dict(mode='ranged',str=3,dex=3,agi=1,int=1,nrv=2,wnd=1,dmg=3,arm=-1,cov=0),
 'Quick Muscle':     dict(mode='melee', str=3,dex=1,agi=3,int=1,nrv=2,wnd=1,dmg=2,arm=-1,cov=0),
 'Jack':             dict(mode='melee', str=2,dex=2,agi=2,int=2,nrv=2,wnd=1,dmg=2,arm=0, cov=0),
}
def attack(att, dfn, stress=True):
    sk = 1 if (stress and att['_st'] >= 1) else 0  # Shaken: -1 to this unit's rolls
    if att['mode'] == 'ranged':
        hit = core_roll(att['dex'] + dfn['cov'] - sk)
    else:
        dk = 1 if (stress and dfn['_st'] >= 1) else 0
        hit = opposed_roll(att['str'] - sk, dfn['str'] - dk)
    if not hit: return
    if core_roll(att['dmg'] + dfn['arm'] - sk): dfn['_w'] -= 1; dfn['_st'] += 1
    else: dfn['_st'] += 1
def nerve(u):
    if u['_st'] < 2: return  # 1 Stress = Shaken only, no test
    d = d10(); pen = u['_st'] - 1
    if d == 10 or (d != 1 and d + u['nrv'] - pen >= 7):
        u['_st'] = 0  # steady: clear all Stress
    else:
        if u['_st'] >= 4: u['_out'] = True   # BugOut → removed
        else: u['_skip'] = True              # Bolt/Broken → lose next activation
        u['_st'] = max(0, u['_st'] - 1)
def duel(A, B, stress=True):
    a = dict(A); a.update(_w=A['wnd'], _st=0, _skip=False, _out=False)
    b = dict(B); b.update(_w=B['wnd'], _st=0, _skip=False, _out=False)
    turn = 0 if random.random() < 0.5 else 1
    for _ in range(30):
        for _ in range(2):
            att, dfn = (a, b) if turn == 0 else (b, a)
            if att['_skip']: att['_skip'] = False
            else: attack(att, dfn, stress)
            if dfn['_w'] <= 0: return 'A' if att is a else 'B'
            turn = 1 - turn
        if stress:
            nerve(a); nerve(b)
            if a['_out']: return 'B'
            if b['_out']: return 'A'
    return 'draw'

names = list(ROSTER)
print("\n[F] DUEL MATRIX — row vs col, % row wins (10k fights, random first, Stress on)")
print("     WND all = 1 (pure attrition, NO terrain/cover). Draw% tiny, omitted.")
hdr = "".join(f"{n[:4]:>6}" for n in names)
print(f"{'':>18}{hdr}")
winrate = {n:0 for n in names}
fights = 0
for rn in names:
    cells = []
    for cn in names:
        if rn == cn: cells.append("  —  "); continue
        w = sum(1 for _ in range(N) if duel(ROSTER[rn], ROSTER[cn]) == 'A')
        cells.append(f"{w/N*100:4.0f} ")
        winrate[rn] += w/N; fights += 1
    print(f"{rn:>18}" + "".join(f"{c:>6}" for c in cells))

print("\n    OVERALL WIN RATE (avg vs the other 7):")
for n, wr in sorted(winrate.items(), key=lambda x:-x[1]):
    print(f"      {n:>18}  {wr/7*100:4.1f}%")

# ---- G. avg fight length + crack rate, sample matchup ----
def duel_stats(A,B,n=N):
    rounds=0; cracks=0
    def duel2(A,B):
        nonlocal cracks
        a=dict(A);a.update(_w=A['wnd'],_st=0,_skip=False,_out=False)
        b=dict(B);b.update(_w=B['wnd'],_st=0,_skip=False,_out=False)
        turn=0 if random.random()<.5 else 1
        for r in range(30):
            for _ in range(2):
                att,dfn=(a,b) if turn==0 else (b,a)
                if att['_skip']: att['_skip']=False
                else: attack(att,dfn)
                if dfn['_w']<=0: return r+1
                turn=1-turn
            for u in (a,b):
                if u['_st']>=2:  # Break test at 2+; 1 Stress = Shaken only
                    d=d10(); pen=u['_st']-1
                    if d==10 or (d!=1 and d+u['nrv']-pen>=7):
                        u['_st']=0
                    else:
                        cracks+=1
                        if u['_st']>=4: u['_out']=True
                        else: u['_skip']=True
                        u['_st']=max(0,u['_st']-1)
            if a['_out'] or b['_out']: return r+1
        return 30
    for _ in range(n): rounds+=duel2(A,B)
    return rounds/n, cracks/n
r_even,c_even = duel_stats(ROSTER['Jack'],ROSTER['Jack'])
r_gb,c_gb = duel_stats(ROSTER['Gunner'],ROSTER['Brawler'])
print(f"\n[G] FIGHT LENGTH / CRACK RATE (WND 1):")
print(f"      Jack vs Jack   : avg {r_even:.2f} rounds, cracks/fight {c_even:.3f}")
print(f"      Gunner vs Brawler: avg {r_gb:.2f} rounds, cracks/fight {c_gb:.3f}")

# ---- H. Multi-wound stress probe (WND 3) ----
def wnd3(A,B):
    a=dict(A); a['wnd']=3; b=dict(B); b['wnd']=3
    return duel_stats(a,b)
r3,c3 = wnd3(ROSTER['Jack'],ROSTER['Jack'])
print(f"      Jack vs Jack @ WND3: avg {r3:.2f} rounds, cracks/fight {c3:.3f}  (stress bites when fights last)")
print("\n" + "="*72)

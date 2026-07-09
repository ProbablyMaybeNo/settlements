import random
random.seed(20260709)
N=40000
def d10(): return random.randint(1,10)
def core(mod,t=7):
    d=d10()
    return True if d==10 else False if d==1 else d+mod>=t
def opp(a,b):
    return (d10()+a) > (d10()+b)  # ties to defender
def coreP(mod,t=7):
    w=0
    for d in range(1,11):
        if d==1: continue
        if d==10: w+=1; continue
        if d+mod>=t: w+=1
    return w/10

# 1) Shooter wound/shot at penalty 0/-1/-2 (DEX+2, med +2, open, no armour)
print("SHOOTER (DEX+2, med weapon, open target) — effect of a flat penalty:")
for pen in (0,1,2):
    w=sum(1 for _ in range(N) if core(2-pen) and core(2))/N
    print(f"  pen -{pen}:  wound/shot {w*100:4.1f}%   (shots→down {1/w:.1f})")

# 2) Even melee, attacker penalty (opposed both directions handled: pen on attacker roll)
print("\nMELEE, even STR (2 v 2) — attacker Shook (-pen to its roll):")
for pen in (0,1,2):
    win=sum(1 for _ in range(N) if opp(2-pen,2))/N
    print(f"  pen -{pen}:  attacker wins {win*100:4.1f}%")

# 3) Full duel: even fighters, one is Shook for the WHOLE fight (pen on all its rolls, both offence+defence)
ARCH=dict(mode='melee',s=2,dex=2,dmg=2,arm=0,cov=0,wnd=1)
def attack(att,dfn):
    if att['mode']=='ranged':
        hit=core(att['dex']-att['pen']+dfn['cov'])
    else:
        hit=opp(att['s']-att['pen'], dfn['s']-dfn['pen'])  # both sides' penalty apply
    if not hit: return
    if core(att['dmg']-att['pen']+dfn['arm']): dfn['_w']-=1
def duel(penA,penB,mode='melee'):
    a=dict(ARCH,pen=penA,mode=mode,_w=1); b=dict(ARCH,pen=penB,mode=mode,_w=1)
    turn=0 if random.random()<.5 else 1
    for _ in range(60):
        att,dfn=(a,b) if turn==0 else (b,a)
        attack(att,dfn)
        if dfn['_w']<=0: return 'A' if att is a else 'B'
        turn=1-turn
    return 'draw'
print("\nDUEL, even fighters, MELEE — one unit Shook whole fight:")
for pen in (0,1,2,3):
    aw=sum(1 for _ in range(N) if duel(pen,0)=='A')/N
    print(f"  Shook unit pen -{pen}:  win rate {aw*100:4.1f}%   (swing vs 50%: {(aw-0.5)*100:+4.1f})")
print("\nDUEL, even fighters, RANGED — one unit Shook whole fight:")
for pen in (0,1,2):
    aw=sum(1 for _ in range(N) if duel(pen,0,'ranged')=='A')/N
    print(f"  Shook unit pen -{pen}:  win rate {aw*100:4.1f}%")

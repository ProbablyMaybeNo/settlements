"""Settlements — Hacking two-roll model (Access then graded Breach). Exact math.
Access: 1d10+INT+range>=7 (or opposed INT, ties->defender).
Breach: 1d10 + Program - Firewall, total -> 7 ShutOut / 8 Surge / 9 TakeOver / 10 BrainHack.
nat1 = nothing, nat10 = BrainHack."""
import sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

def cx(mod, t=7):
    w = 0
    for d in range(1, 11):
        if d == 1: continue
        if d == 10: w += 1; continue
        if d + mod >= t: w += 1
    return w/10
def ox(dmod, tieA=False):
    w = 0
    for a in range(1,11):
        for b in range(1,11):
            if a+dmod > b: w += 1
            elif a+dmod == b and tieA: w += 1
    return w/100
def pc(x): return f"{x*100:4.0f}%"

TIERS = ['nothing','ShutOut','Surge','TakeOver','BrainHack']
def breach(net):                       # net = Program - Firewall
    o = {k:0.0 for k in TIERS}
    for d in range(1,11):
        if d == 1: o['nothing'] += .1; continue
        if d == 10: o['BrainHack'] += .1; continue
        tot = d + net
        if   tot >= 10: o['BrainHack'] += .1
        elif tot >= 9:  o['TakeOver']  += .1
        elif tot >= 8:  o['Surge']     += .1
        elif tot >= 7:  o['ShutOut']   += .1
        else:           o['nothing']   += .1
    return o

print("="*70)
print("SETTLEMENTS — HACKING (two-roll: Access -> graded Breach)")
print("="*70)

# H1 · Access roll (unchanged from combat to-hit) — confirm
print("\n[H1] ACCESS ROLL  1d10 + INT + range >= 7")
print(f"   {'INT':>4}{'Close':>8}{'Short':>8}{'Med':>8}{'Long':>8}")
for i in range(0,7):
    print(f"   {'+'+str(i):>4}{pc(cx(i)):>8}{pc(cx(i-1)):>8}{pc(cx(i-2)):>8}{pc(cx(i-3)):>8}")

# H2 · Breach tier distribution by net Program-Firewall
print("\n[H2] BREACH TIER SPREAD by (Program − Firewall)  [given you got in]")
print(f"   {'net':>5}{'nothing':>9}{'ShutOut':>9}{'Surge':>8}{'TakeOvr':>9}{'BrnHack':>9}{'≥ShutOut':>10}")
for net in [-2,-1,0,1,2,3]:
    o = breach(net); atleast = 1-o['nothing']
    print(f"   {('+'+str(net) if net>=0 else str(net)):>5}{pc(o['nothing']):>9}{pc(o['ShutOut']):>9}"
          f"{pc(o['Surge']):>8}{pc(o['TakeOver']):>9}{pc(o['BrainHack']):>9}{pc(atleast):>10}")

# H3 · Full hack (Access x Breach) — landed-effect rates
print("\n[H3] FULL HACK — P(access) × breach. 'real effect' = at least Shut Out.")
def full(intmod, prog, fw, rng=0):
    acc = cx(intmod+rng); o = breach(prog+fw)
    real = acc*(1-o['nothing'])
    takeover = acc*(o['TakeOver']+o['BrainHack'])
    brain = acc*o['BrainHack']
    return acc, real, takeover, brain
print(f"   {'hacker / target':<34}{'access':>8}{'≥ShutOut':>10}{'≥TakeOvr':>10}{'BrainHack':>11}")
rows = [
 ("Standard INT+2, Prog+2 · undefended", 2,2,0),
 ("Standard INT+2, Prog+2 · Firewall −2", 2,2,-2),
 ("Specialist INT+4, Prog+2 · undefended", 4,2,0),
 ("Specialist INT+4, Prog+2 · Firewall −2", 4,2,-2),
 ("Bare INT+2, Prog+0 · undefended", 2,0,0),
]
for lbl,i,p,f in rows:
    acc,real,to,br = full(i,p,f)
    print(f"   {lbl:<34}{pc(acc):>8}{pc(real):>10}{pc(to):>10}{pc(br):>11}")

# H4 · Head-to-head hacker duel (access = opposed INT, ties->defender)
print("\n[H4] HACKER DUEL — access = opposed INT (ties→def), then attacker breach vs Firewall")
print(f"   {'matchup':<34}{'win access':>11}{'≥ShutOut':>10}{'BrainHack(auto-hit)':>20}")
duels = [
 ("even INT+4, Prog+2 · Firewall 0", 0,2,0),
 ("even INT+4, Prog+2 · Firewall −2", 0,2,-2),
 ("attacker INT+2 edge, Prog+2 · FW 0", 2,2,0),
 ("attacker INT−2 behind, Prog+2 · FW 0", -2,2,0),
]
for lbl,dINT,p,f in duels:
    acc = ox(dINT)  # attacker wins access
    o = breach(p+f)
    real = acc*(1-o['nothing']); brain = acc*o['BrainHack']
    print(f"   {lbl:<34}{pc(acc):>11}{pc(real):>10}{pc(brain):>20}")

print("\n" + "="*70)
print("Old model (opposed→Effect→table): even-INT real effect ≈ 14%.")
print("="*70)

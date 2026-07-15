"""Settlements — Hacking v1 (simple). Exact math.
A hack is ONE core test: 1d10 + INT - range >= 7. Pass = activate one Linked feature.
Interrupt: an enemy at another live terminal declares before the roll; if the access PASSES it is
  jammed (no feature) and the interrupter's terminal is Overloaded till next turn; if the access FAILS
  the interrupt is not spent. No opposed roll. Each interrupter terminal eats exactly ONE successful
  hack per turn, so to land 1 feature past K interrupters you need (K+1) successful hacks on the network."""
import sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass
from math import comb

def cx(mod, t=7):                      # P(pass) for 1d10 + mod >= t, nat1 auto-fail, nat10 auto-pass
    w = 0
    for d in range(1, 11):
        if d == 1: continue
        if d == 10: w += 1; continue
        if d + mod >= t: w += 1
    return w/10
def pc(x): return f"{x*100:4.0f}%"

def atleast_k(n, p, k):                # P(>= k successes in n independent hacks at prob p)
    return sum(comb(n, j) * p**j * (1-p)**(n-j) for j in range(k, n+1))

RANGE = [("Close",0),("Short",-1),("Med",-2),("Long",-3)]

print("="*68)
print("SETTLEMENTS — HACKING v1 (one INT test · interrupt = single-shot jam)")
print("="*68)

# H1 · The whole solo mechanic: 1d10 + INT - range >= 7
print("\n[H1] HACK TEST  1d10 + INT - range >= 7   P(activate feature)")
print(f"   {'INT':>4}" + "".join(f"{r[0]:>8}" for r in RANGE))
for i in range(0,7):
    print(f"   {'+'+str(i):>4}" + "".join(f"{pc(cx(i+r[1])):>8}" for r in RANGE))
print("   Hardened terminal = a flat extra penalty (shift left one/two columns).")

# H2 · Interrupt is a hard counter — you need TWO successes to land ONE feature past it
print("\n[H2] PUSHING A FEATURE PAST 1 INTERRUPTER  (needs >= 2 successful hacks)")
print("   P(land >=1 feature) by number of attacking units, at per-hack pass rate p")
print(f"   {'p (per hack)':>13}{'1 unit':>9}{'2 units':>9}{'3 units':>9}{'4 units':>9}")
for p in [0.4,0.6,0.8]:
    row = "".join(f"{pc(atleast_k(n,p,2)):>9}" for n in [1,2,3,4])
    print(f"   {pc(p):>13}{row}")
print("   1 unit alone = 0% — a lone hacker can't beat an interrupter. Bring bodies.")

# H3 · No interrupter — pass rate IS the feature rate (baseline to compare against)
print("\n[H3] NO INTERRUPTER  P(>=1 feature from N units, each at p)")
print(f"   {'p (per hack)':>13}{'1 unit':>9}{'2 units':>9}{'3 units':>9}")
for p in [0.4,0.6,0.8]:
    row = "".join(f"{pc(atleast_k(n,p,1)):>9}" for n in [1,2,3])
    print(f"   {pc(p):>13}{row}")

print("\n" + "="*68)
print("v1: one roll to hack, one clean deny. Interrupt eats one successful hack")
print("per terminal per turn (Overloaded after) — so bodies beat a lone defender.")
print("="*68)

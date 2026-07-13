"""Settlements — Terrain / Hacking / Cover test battery (P1 from the test plan).
Engine mirrors the locked core (1d10+mod>=7, nat1 fail / nat10 pass; opposed ties->defender).
Exact where the math is closed-form; seeded Monte-Carlo (N=10,000) for multi-step chains."""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass
random.seed(20260713)
N = 10000

def d10(): return random.randint(1, 10)
def cx(mod, t=7):                      # exact P(core test success)
    w = 0
    for d in range(1, 11):
        if d == 1: continue
        if d == 10: w += 1; continue
        if d + mod >= t: w += 1
    return w / 10
def ox(dmod, tieA=False):              # exact P(attacker wins opposed), advantage=dmod
    w = 0
    for a in range(1, 11):
        for b in range(1, 11):
            if a + dmod > b: w += 1
            elif a + dmod == b and tieA: w += 1
    return w / 100
def cr(mod, t=7):
    d = d10()
    if d == 1: return False
    if d == 10: return True
    return d + mod >= t
def pc(x): return f"{x*100:4.0f}%"

print("="*72)
print("SETTLEMENTS — TERRAIN / HACKING / COVER TESTS   (N=10,000, seed 20260713)")
print("="*72)

# ---- T1 · Cover ladder (Hidden = -3) ----
print("\n[T1] COVER LADDER — shooter DEX+2, medium weapon (+2), target Armor 0")
print(f"   {'cover':<8}{'to-hit':>8}{'wound/shot':>12}{'shots→down':>12}")
for cov, lbl in [(0,'Open'),(-1,'Light'),(-2,'Heavy'),(-3,'Hidden')]:
    h = cx(2+cov); w = h*cx(2)
    print(f"   {lbl:<8}{pc(h):>8}{pc(w):>12}{(f'{1/w:.1f}' if w else '—'):>12}")

# ---- T2 · Cover × the ±3 cap (we ruled cover SEPARATE from the conditions cap) ----
print("\n[T2] COVER × ±3 CAP — Shaken shooter (−1) into cover. DEX+2 base.")
print("   Does cover share the conditions' −3 cap, or is it separate (our ruling)?")
print(f"   {'cover':<8}{'separate(ruled)':>16}{'shared-cap':>12}{'Shaken worth':>14}")
for cov, lbl in [(-2,'Heavy'),(-3,'Hidden')]:
    sep = cx(2 + cov + (-1))                    # cover and −1 both apply
    shr = cx(2 + max(-3, cov + (-1)))           # total negatives capped at −3
    print(f"   {lbl:<8}{pc(sep):>16}{pc(shr):>12}{('−'+str(round((shr-sep)*100))+'pts' ):>14}")
print("   → Under a shared cap, Shaken does NOTHING vs a Hidden target. Ruling = separate.")

# ---- T3 · Fall damage vs WND 1 ----
print("\n[T3] FALL DAMAGE — 1d10 + (1 per full 2\") ignoring Armor ≥ 7 → wound; lands Prone")
print(f"   {'fall':<8}{'+Dmg':>6}{'P(wound)':>10}{'note (WND1 = P down)':>24}")
for h in [2,3,4,6,8]:
    dmg = h//2; p = cx(dmg)
    note = 'coin-flip kill' if abs(p-0.5)<0.06 else ('lethal' if p>=0.7 else '')
    print(f"   {str(h)+chr(34):<8}{'+'+str(dmg):>6}{pc(p):>10}{note:>24}")
print("   (Voluntary 2–3\" drop may test AGI 7+ to avoid entirely; involuntary = full.)")

# ---- T4 · Height advantage ----
print("\n[T4] HEIGHT — attacker 2\"+ up ignores Light cover. Target in LIGHT cover.")
gh = cx(2-1); gw = gh*cx(2)          # ground shooter vs Light
eh = cx(2+0); ew = eh*cx(2)          # elevated ignores Light -> treats as Open
print(f"   {'shooter':<12}{'to-hit':>8}{'wound/shot':>12}{'shots→down':>12}")
print(f"   {'ground':<12}{pc(gh):>8}{pc(gw):>12}{1/gw:>11.1f}")
print(f"   {'elevated':<12}{pc(eh):>8}{pc(ew):>12}{1/ew:>11.1f}")
print(f"   → Height strips Light (≈ +{round((ew/gw-1)*100)}% lethality). Heavy cover still counts from above.")

# ---- T5 · Hacking success curve ----
print("\n[T5] HACKING — 1d10 + INT + range ≥ 7")
print(f"   {'INT':>4}{'Close(0)':>10}{'Short(−1)':>11}{'Med(−2)':>10}{'Long(−3)':>10}")
for i in range(0,7):
    print(f"   {'+'+str(i):>4}{pc(cx(i)):>10}{pc(cx(i-1)):>11}{pc(cx(i-2)):>10}{pc(cx(i-3)):>10}")

# ---- T6 · Hacker-vs-hacker shut-out (full chain) ----
print("\n[T6] SHUT-OUT — opposed INT (ties→def) → Effect 1d10≥7 → Shut-out table")
EFFECT = 0.4  # d10 in {7,8,9,10}
# table given a landed payload:
TBL = {'Glitch(nothing)':0.2,'Shutdown':0.3,'Destroyed':0.2,'TakeOver':0.2,'Overload':0.1}
print(f"   {'INT Δ':>6}{'P(win opp)':>11}{'P(payload)':>11}{'P(real effect)':>15}{'P(nothing)':>12}")
for d in [-2,0,2]:
    win = ox(d)                       # attacker advantage d, ties->defender
    payload = win*EFFECT
    real = payload*(1-TBL['Glitch(nothing)'])
    print(f"   {('+'+str(d) if d>=0 else str(d)):>6}{pc(win):>11}{pc(payload):>11}{pc(real):>15}{pc(1-real):>12}")
print("   Outcome mix WHEN a payload lands: "+" · ".join(f"{k} {int(v*100)}%" for k,v in TBL.items()))
print("   ⚠ Even-INT shut-out = ~14% to do anything real → very weak for a whole activation.")

# ---- T7 · Search EV ----
print("\n[T7] SEARCH — find table on a passed INT 7+ search (one attempt per piece)")
find = {'Hazard(1)':0.1,'Nothing(2-4)':0.3,'Resource(5-7)':0.3,'Gear(8-9)':0.2,'Jackpot(10)':0.1}
eRes = 0.3*1 + 0.1*1; eGear = 0.2*1 + 0.1*1
print(f"   per successful search:  E[Resource]={eRes:.2f}  E[gear]={eGear:.2f}  P(hazard/self-Pin)={pc(0.1)}")
for i,lbl in [(2,'INT+2'),(4,'INT+4')]:
    ps = cx(i)
    print(f"   {lbl}: search passes {pc(ps)} → per attempt {ps*eRes:.2f} Resource, {ps*eGear:.2f} gear, {pc(ps*0.1)} hazard")

# ---- T8 · Disengage cost (Monte-Carlo) ----
print("\n[T8] DISENGAGE — free swing at −2 from each engager (even STR, light wpn +1)")
def swing():   # one engager's free swing at -2 vs disengager; opposed then injure
    return cr_opp(-2) and cr(1)
def cr_opp(dmod):
    a,b = d10(),d10(); return a+dmod > b
for eng in [1,2]:
    downs = 0
    for _ in range(N):
        w = sum(1 for _ in range(eng) if swing())
        if w >= 1: downs += 1   # WND1: any wound = Down
    print(f"   leaving {eng} engager(s): {pc(downs/N)} chance to be Downed while fleeing (+ lose whole activation)")

# ---- T9 · AGI traversal + armour drag ----
print("\n[T9] TRAVERSAL — climb/jump/vault/swim = 1d10 + AGI ≥ 7 (fail = fall/Prone)")
print(f"   {'AGI':>4}{'unarmoured':>12}{'Heavy(−1 AGI)':>15}{'fail→fall (unarm)':>18}")
for a in range(0,7):
    print(f"   {'+'+str(a):>4}{pc(cx(a)):>12}{pc(cx(a-1)):>15}{pc(1-cx(a)):>18}")
print("   → Heavy armour drops every terrain test ~10%; heavies pay for cover on the board.")

# ---- T10 · Brutal shotgun (close) lethality ----
print("\n[T10] SHOTGUN CLOSE = +3 & Brutal(+1) = +4 injury  vs armour")
print(f"   {'weapon':<18}{'arm 0':>8}{'arm −1':>8}{'arm −2':>8}")
print(f"   {'Heavy +3 (rifle)':<18}{pc(cx(3)):>8}{pc(cx(2)):>8}{pc(cx(1)):>8}")
print(f"   {'Shotgun close +4':<18}{pc(cx(4)):>8}{pc(cx(3)):>8}{pc(cx(2)):>8}")
print("   ⚠ +4 = 80% wound at Armor 0 — top of the scale; gate it with close-range + Loud + Spread.")

# ---- T11 · Overload injury ----
print("\n[T11] OVERLOAD (shut-out 10) — defending hacker Injury 1d10 + 0 − Armor ≥ 7")
print(f"   arm 0 {pc(cx(0))} · arm −1 {pc(cx(-1))} · arm −2 {pc(cx(-2))}   (and only on the rare 10)")

print("\n"+"="*72)

"""Settlements SKILL sim — how much is each dice-testable skill actually worth?
Mirrors the locked engine (core 1d10+stat>=7, opposed melee ties->defender, injury
1d10+dmg-arm>=7, Shaken -1 at 1+ Stress, Break test at 2+: 1d10+NRV-(Stress-1)>=7).
Standard sample = 10,000. Seeded."""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass
random.seed(20260710)
N = 10000

def d10(): return random.randint(1, 11-1)
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
def opposed_exact(dmod, tieA=False):
    w = 0
    for a in range(1, 11):
        for b in range(1, 11):
            if a + dmod > b: w += 1
            elif a + dmod == b and tieA: w += 1
    return w / 100
def pct(x): return f"{x*100:5.1f}%"

print("="*74)
print("SETTLEMENTS — SKILL SIM   (N = 10,000 / test, seed 20260710)")
print("="*74)

# =====================================================================
# 1. FLAT COMBAT MODIFIERS — exact probability shift
# =====================================================================
print("\n[1] FLAT COMBAT MODIFIERS — the raw % a single skill buys (exact)")
print(f"    {'skill / effect':<38}{'base':>7}{'w/skill':>9}{'delta':>8}")
def line(lbl, base, skill): print(f"    {lbl:<38}{pct(base):>7}{pct(skill):>9}{'+'+str(round((skill-base)*100)):>7}%")
# shooter DEX+2 open, med weapon +2 vs arm0
line("Dead Eye (+1 hit, no-move/no-cover)", core_exact(2), core_exact(3))
line("The Muscle (+2 injury, 1st charge hit)", core_exact(2), core_exact(4))
line("Heavy Hands (+1 melee vs Pinned)", opposed_exact(0), opposed_exact(1))
line("Feint (+2 melee after hidden approach)", opposed_exact(0), opposed_exact(2))
line("Ghost Blade (AGI4 melee vs STR2 base)", opposed_exact(0), opposed_exact(2))
print("    (Each modifier = ~+10%/point, capped 90% by the nat-1 rule.)")

# =====================================================================
# 2. MULTI-ATTACK — expected WOUNDS per activation (2nd attack at -2)
# =====================================================================
print("\n[2] MULTI-ATTACK — expected wounds / activation (target WND=inf, no cap)")
def ew_ranged(dex, cov, dmg, arm, second=None):
    e = core_exact(dex+cov)*core_exact(dmg+arm)
    if second is not None: e += core_exact(dex+cov+second)*core_exact(dmg+arm)
    return e
def ew_melee(dstr, dmg, arm, second=None):
    e = opposed_exact(dstr)*core_exact(dmg+arm)
    if second is not None: e += opposed_exact(dstr+second)*core_exact(dmg+arm)
    return e
base_r = ew_ranged(2,0,2,0); qs = ew_ranged(2,0,2,0,second=-2)
base_m = ew_melee(0,1,0);    dw = ew_melee(0,1,0,second=-2)
print(f"    Single shot (DEX+2, med+2, open) : {base_r:.3f}")
print(f"    Quick Shot (2 shots, 2nd -2)     : {qs:.3f}   (+{(qs/base_r-1)*100:.0f}% output, no Reactions this round)")
print(f"    Single melee (even STR, +1 wpn)  : {base_m:.3f}")
print(f"    Dual Wield (2 swings, 2nd -2)    : {dw:.3f}   (+{(dw/base_m-1)*100:.0f}% output)")
print("    Gunslinger = 2 targets → 0 gain in a 1v1; only pays vs multiple foes.")

# =====================================================================
# 3. GRAPPLE CHAIN
# =====================================================================
print("\n[3] GRAPPLE CHAIN — opposed STR, ties->defender")
print(f"    Grapple lands (even STR)          : {pct(opposed_exact(0))}")
print(f"    Grapple lands (STR+2 grappler)    : {pct(opposed_exact(2))}")
print(f"    Victim escapes next activation    : {pct(opposed_exact(0))}  (even) / {pct(opposed_exact(-2))} (vs STR+2)")
print(f"    Squeeze auto-hit injures (unarmed +0 vs arm0): {pct(core_exact(0))}/use")
print(f"    Heavy Hands on the Grappled target: melee {pct(opposed_exact(0))} -> {pct(opposed_exact(1))}")

# =====================================================================
# 4. BRAVERY PATH — break-rate impact (the nerve skills)
# =====================================================================
print("\n[4] BRAVERY PATH — chance of BREAKING at a given Stress (NRV+2 fighter)")
def crack(nrv, st):  # 1 - pass, pass = nat10 or (not nat1 and d+nrv-(st-1)>=7)
    return 1 - core_exact(nrv-(st-1))
print(f"    {'':<34}{'St2':>7}{'St3':>7}{'St4':>7}")
def brow(lbl, f): print(f"    {lbl:<34}{pct(f(2)):>7}{pct(f(3)):>7}{pct(f(4)):>7}")
brow("Baseline NRV+2", lambda s: crack(2,s))
brow("Rattle-Proof (effective -1 Stress)", lambda s: crack(2,max(1,s-1)) if s>1 else 0.0)
brow("Cowed on you (-1 this test)", lambda s: 1-core_exact(2-(s-1)-1))
brow("Braced (+1 this test)", lambda s: 1-core_exact(2-(s-1)+1))
print("    Iron Will: negates one failed test/game outright (see [5]).")
print("    Steady/Count Breaths: don't change per-test odds — they cut how OFTEN you test")
print("    by shedding Stress before it reaches 2 (frequency, see [5]).")

# =====================================================================
# 5. MARQUEE DUEL — mirror match, side A has the skill. Baseline = 50%.
#    WND 3 so fights last long enough for stress/multi-round skills to bite.
# =====================================================================
def F(mode, **kw):
    d = dict(mode=mode, str=2, dex=2, agi=2, dmg=(1 if mode=='melee' else 2),
             arm=0, cov=0, wnd=3, nrv=2, skills=set())
    d.update(kw); return d

def add_stress(u, n):
    for _ in range(n):
        if 'rattle_proof' in u['skills'] and not u['_rp_used']:
            u['_rp_used'] = True; continue
        u['_st'] += 1

def do_injure(att, dfn, sk):
    injmod = att['dmg'] + dfn['arm'] - sk
    if 'the_muscle' in att['skills'] and not att['_muscle_used']:
        injmod += 2; att['_muscle_used'] = True
    if core_roll(injmod):
        dfn['_w'] -= 1; add_stress(dfn, 1); dfn['_pinned'] = False
    else:
        add_stress(dfn, 1); dfn['_pinned'] = True

def activation(att, dfn):
    # start-of-activation self effects
    if 'steady' in att['skills'] and att['_st'] > 0: att['_st'] -= 1
    melbonus = 0
    if att['mode'] == 'melee' and att['_w'] > 0:
        if 'red_mist' in att['skills']: add_stress(att, 3); melbonus = 2
        elif 'feed_anger' in att['skills']: add_stress(att, 1); melbonus = 1
    if att.get('_skip'):
        att['_skip'] = False; return
    sk = 1 if att['_st'] >= 1 else 0
    if att['mode'] == 'ranged':
        mod = att['dex'] + dfn['cov'] - sk
        if 'dead_eye' in att['skills'] and dfn['cov'] == 0: mod += 1
        shots = 2 if 'quick_shot' in att['skills'] else 1
        for i in range(shots):
            if dfn['_w'] <= 0: break
            if core_roll(mod - (2 if i else 0)): do_injure(att, dfn, sk)
    else:
        atkstat = att['agi'] if 'ghost_blade' in att['skills'] else att['str']
        amod = atkstat + melbonus - sk
        if 'feint' in att['skills']: amod += 2
        if 'heavy_hands' in att['skills'] and dfn.get('_pinned'): amod += 1
        dmod = dfn['str'] + (1 if 'dodge' in dfn['skills'] else 0) - (1 if dfn['_st'] >= 1 else 0)
        swings = 2 if 'dual_wield' in att['skills'] else 1
        for i in range(swings):
            if dfn['_w'] <= 0: break
            a, b = d10(), d10()
            if a + amod - (2 if i else 0) > b + dmod: do_injure(att, dfn, sk)

def break_test(u):
    if u['_st'] < 2: return
    d = d10(); pen = u['_st'] - 1
    if d == 10 or (d != 1 and d + u['nrv'] - pen >= 7):
        u['_st'] = 0; return
    # fail
    if 'iron_will' in u['skills'] and not u['_iw_used']:
        u['_iw_used'] = True; u['_st'] = 0; return  # auto-pass negates it
    if u['_st'] >= 4:
        u['_out'] = True; u['_st'] -= 1; return
    # Bolt/Broken
    if 'fanatic' in u['skills']:
        add_stress(u, 2); u['_st'] = max(0, u['_st']-1)  # Fight: keeps acting, no skip
    else:
        u['_skip'] = True; u['_st'] = max(0, u['_st']-1)

def duel(A, B):
    a = {**A, '_w': A['wnd'], '_st': 0, '_skip': False, '_out': False, '_pinned': False,
         '_muscle_used': False, '_iw_used': False, '_rp_used': False}
    b = {**B, '_w': B['wnd'], '_st': 0, '_skip': False, '_out': False, '_pinned': False,
         '_muscle_used': False, '_iw_used': False, '_rp_used': False}
    turn = 0 if random.random() < 0.5 else 1
    for _ in range(40):
        a['_rp_used'] = False; b['_rp_used'] = False
        for _ in range(2):
            att, dfn = (a, b) if turn == 0 else (b, a)
            activation(att, dfn)
            if dfn['_w'] <= 0: return 'A' if att is a else 'B'
            turn = 1 - turn
        break_test(a); break_test(b)
        if a['_out']: return 'B'
        if b['_out']: return 'A'
    return 'draw'

def winrate(mkA, mkB):
    aw = sum(1 for _ in range(N) if duel(mkA(), mkB()) == 'A')
    return aw / N

print("\n[5] MARQUEE DUEL — A has the skill, B is a plain mirror. WND 3. Baseline 50%.")
print(f"    {'skill (side A)':<34}{'A win%':>8}{'edge':>8}")
def duelrow(lbl, mode, skill):
    def mkA(): return F(mode, skills={skill}) if skill else F(mode)
    def mkB(): return F(mode)
    wr = winrate(mkA, mkB)
    print(f"    {lbl:<34}{pct(wr):>8}{('+'+str(round((wr-0.5)*100))):>7}%")

duelrow("(sanity: no skill)", 'melee', None)
# melee combat skills
duelrow("Tough (+1 WND)", 'melee', 'tough') if False else None
def duelrow_wnd(lbl, extra):  # for tough we bump A wnd
    def mkA(): a=F('melee'); a['wnd']=4; return a
    def mkB(): return F('melee')
    wr = winrate(mkA, mkB); print(f"    {lbl:<34}{pct(wr):>8}{('+'+str(round((wr-0.5)*100))):>7}%")
duelrow_wnd("Tough (WND 3->4)", None)
duelrow("Feint (+2 melee)", 'melee', 'feint')
duelrow("The Muscle (+2 injury, first hit)", 'melee', 'the_muscle')
duelrow("Dual Wield (2 swings, 2nd -2)", 'melee', 'dual_wield')
duelrow("Dodge (incoming melee -1)", 'melee', 'dodge')
def duelrow_ghost():
    def mkA(): a=F('melee'); a['agi']=4; a['skills']={'ghost_blade'}; return a
    def mkB(): return F('melee')
    wr = winrate(mkA, mkB); print(f"    {'Ghost Blade (AGI4 vs STR2)':<34}{pct(wr):>8}{('+'+str(round((wr-0.5)*100))):>7}%")
duelrow_ghost()
# NRV skills in a melee grind
duelrow("Red Mist (+3 St -> +2 melee)", 'melee', 'red_mist')
duelrow("Feed the Anger (+1 St -> +1 melee)", 'melee', 'feed_anger')
duelrow("Rattle-Proof (ignore 1 St/round)", 'melee', 'rattle_proof')
duelrow("Steady (-1 St/activation)", 'melee', 'steady')
duelrow("Iron Will (auto-pass 1 test)", 'melee', 'iron_will')
duelrow("Fanatic (Bolt/Broken -> Fight)", 'melee', 'fanatic')
# ranged skills
print(f"    {'--- ranged mirrors (DEX 2, med +2) ---':<34}")
duelrow("Dead Eye (+1 hit, open)", 'ranged', 'dead_eye')
duelrow("Quick Shot (2 shots, 2nd -2)", 'ranged', 'quick_shot')

print("\n" + "="*74)
print("Baselines should read ~50%; any deviation is Monte-Carlo noise (~<1%).")
print("="*74)

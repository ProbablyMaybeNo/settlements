"""Settlements — WEAPON SYSTEM test battery (Weapons.md v0.3).
Every list is built to a LEGAL <=100 pts under the List Building pyramid.
"""
import random, sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass
import weapon_sim as S
from weapon_sim import F, BAT, KNIFE, CROWBAR, FIRE_AXE, SLEDGE, CLEAVER, HEAVY_PLAIN, \
    PISTOL, RIFLE, HUNTER, PIPE_GUN, MG, FLAMER, MOLOTOV, BLEEDGUN, SUPPRESSOR, \
    cost, wr

random.seed(S.SEED)
N = 2500
BUDGET = 100

def core_x(mod, target=7):
    return sum(1 for d in range(1, 11)
               if d == 10 or (d != 1 and d + mod >= target)) / 10
def opp_x(dm):
    return sum(1 for a in range(1, 11) for b in range(1, 11) if a + dm > b) / 100

def legal(crew, name):
    """Enforce the List Building pyramid + budget."""
    n = lambda r: sum(1 for f in crew if f['rank'] == r)
    errs = []
    if n('Leader') != 1: errs.append("needs exactly 1 Leader")
    if n('Specialist') * 2 > n('Recruit') + n('Rabble'):
        errs.append("Specialists need 2 lower-rank each")
    if n('Rabble') > n('Recruit'): errs.append("each Rabble needs a Recruit or better")
    if len(crew) < 4: errs.append("min crew 4")
    if cost(crew) > BUDGET: errs.append(f"OVER BUDGET ({cost(crew)})")
    return errs

print("=" * 84)
print("SETTLEMENTS — WEAPON SYSTEM TESTS   (Weapons.md v0.3, all lists legal @ 100 pts)")
print("=" * 84)

# ============================================================ 1. armoury
ARMOURY = [BAT, KNIFE, CROWBAR, FIRE_AXE, SLEDGE, CLEAVER, HEAVY_PLAIN, PISTOL,
           RIFLE, HUNTER, PIPE_GUN, MG, FLAMER, MOLOTOV, BLEEDGUN, SUPPRESSOR]
print("\n[1] THE ARMOURY — every build passes class / slot / ceiling / drawback asserts")
print(f"    {'weapon':<22}{'dmg':>5}{'range':>7}{'cost':>6}   traits")
for w in ARMOURY:
    tr = " · ".join(sorted(t for t in w['t']))
    print(f"    {w['name']:<22}{'+'+str(w['dmg']):>5}"
          f"{(str(w['rng'])+chr(34)) if w['rng'] else 'melee':>7}{w['cost']:>6}   {tr}")

# ============================================================ 2. efficiency
print("\n[2] EFFICIENCY — expected wounds / activation, and per point of (Recruit + weapon)")
print("    Ranged: DEX+2.  Melee: STR+2 vs STR+2 (opposed, ties→def).  Target: no armour, open.")
print(f"\n    {'weapon':<22}{'open':>7}{'covered':>9}{'unit pts':>10}{'wounds/pt':>11}  payload")
rows = []
for w in ARMOURY:
    if w['rng']:
        bonus = (1 if 'accurate' in w['t'] else 0) + (1 if 'spread' in w['t'] else 0)
        hit_o, hit_c = core_x(2 + bonus), core_x(2 + bonus - 2)
    else:
        hit_o = hit_c = opp_x(0)
    ap = 1 if 'ap' in w['t'] else 0
    eo = hit_o * core_x(w['dmg'])
    ec = hit_c * core_x(w['dmg'] - 1 + ap)
    unit = 8 + w['cost']
    pay = next((k for k in w['t'] if k in S.PAYLOAD), '')
    for extra in ('suppressive', 'cleaving', 'blast', 'heavy_impact'):
        if extra in w['t']: pay = (pay + '+' + extra).strip('+')
    rows.append((w['name'], eo, ec, unit, eo / unit, pay))
for n_, eo, ec, unit, wpp, pay in sorted(rows, key=lambda r: -r[4]):
    print(f"    {n_:<22}{eo:>7.2f}{ec:>9.2f}{unit:>10}{wpp:>11.3f}  {pay}")

# ============================================================ 3. crew matrix
def CADRE():        # 4 · 96
    return [F('Leader', RIFLE, dex=4, str=2), F('Specialist', RIFLE, 'light', dex=4),
            F('Recruit', PISTOL, dex=2), F('Recruit', PISTOL, dex=2)]
def FIREBASE():     # 4 · 99
    return [F('Leader', RIFLE, dex=4, str=2), F('Specialist', MG, dex=4),
            F('Recruit', PISTOL, dex=2), F('Recruit', PISTOL, dex=2)]
def BLEEDERS():     # 4 · 98
    return [F('Leader', BLEEDGUN, 'light', dex=4), F('Specialist', BLEEDGUN, dex=4),
            F('Recruit', PISTOL, dex=2), F('Recruit', PISTOL, str=2)]
def SHOCKERS():     # 5 · 100 — anti-swarm melee elite w/ Cleaving
    return [F('Leader', CLEAVER, 'light', str=4), F('Specialist', RIFLE, dex=4),
            F('Recruit', PISTOL, str=2), F('Recruit', PISTOL, str=2),
            F('Rabble', BAT)]
def STANDARD():     # 6 · 96
    return [F('Leader', RIFLE, dex=4, str=2), F('Specialist', RIFLE, dex=4),
            F('Recruit', PISTOL, str=2), F('Recruit', BAT, str=2),
            F('Rabble', BAT), F('Rabble', BAT)]
def FIREBUGS():     # 5 · 99 — thrown / incendiary
    return [F('Leader', MOLOTOV, dex=4, str=2), F('Specialist', FLAMER, dex=4),
            F('Recruit', MOLOTOV, dex=2), F('Recruit', PISTOL, dex=2),
            F('Rabble', MOLOTOV)]
def HORDE():        # 9 · 100
    return [F('Leader', PIPE_GUN, str=4, nrv=2)] + \
           [F('Recruit', BAT, str=2) for _ in range(8)]
def PYRAMID():      # 11 · 93 — the no-doctrine legal maximum
    return [F('Leader', PISTOL, str=4, nrv=2)] + \
           [F('Recruit', BAT, str=2) for _ in range(5)] + \
           [F('Rabble', BAT) for _ in range(5)]
def MOB():          # 13 · 96 — needs The Mob doctrine
    return [F('Leader', PIPE_GUN, str=4, nrv=2)] + \
           [F('Rabble', BAT) for _ in range(12)]

LISTS = {'Cadre': CADRE, 'Firebase': FIREBASE, 'Bleeders': BLEEDERS,
         'Cleavers': SHOCKERS, 'Standard': STANDARD, 'Firebugs': FIREBUGS,
         'Horde': HORDE, 'Pyramid': PYRAMID, 'Mob': MOB}

print("\n[3] LEGALITY OF THE TEST LISTS")
print(f"    {'list':<12}{'models':>7}{'points':>8}   status")
for n_, fn in LISTS.items():
    c = fn(); e = legal(c, n_)
    mob = " (needs The Mob doctrine)" if n_ == 'Mob' else ""
    status = "✓ legal" + mob if not e or (n_ == 'Mob' and e == ["each Rabble needs a Recruit or better"]) \
             else "✗ " + "; ".join(e)
    print(f"    {n_:<12}{len(c):>7}{cost(c):>8}   {status}")

names = list(LISTS)
print("\n[4] CREW MATRIX — row win% vs column")
for blocked, lbl in ((0.20, 'sparse 20%  (illegal — under 9 features)'),
                     (0.42, 'LEGAL 42%   (9–12 features)'),
                     (0.60, 'crowded 60% (illegal — over 12)')):
    print(f"\n    [{lbl}]")
    print(f"    {'':<11}" + "".join(f"{n_[:8]:>9}" for n_ in names))
    ov = {}
    for rn in names:
        cells, tot = [], 0.0
        for cn in names:
            if rn == cn: cells.append("    —    "); continue
            v = wr(LISTS[rn], LISTS[cn], blocked, N)
            cells.append(f"{v*100:8.0f} "); tot += v
        ov[rn] = tot / (len(names) - 1)
        print(f"    {rn:<11}" + "".join(cells))
    srt = sorted(ov.items(), key=lambda x: -x[1])
    print("    overall: " + " · ".join(f"{n_} {v*100:.0f}%" for n_, v in srt))
    print(f"    spread: {(srt[0][1]-srt[-1][1])*100:.0f} points"
          f"  ({srt[0][0]} {srt[0][1]*100:.0f}% → {srt[-1][0]} {srt[-1][1]*100:.0f}%)")

# ============================================================ 5. probes
print("\n[5] CHARACTERISTIC PROBES — same 4-model chassis, ONE weapon swapped.")
print("    Leader + Specialist share the weapon; 2 Recruits w/ pistols. vs Mob & Standard @42%.\n")
def chassis(w, label, stat='dex'):
    def f():
        st = {stat: 4, 'str': 4} if stat == 'dex' else {'str': 4}
        return [F('Leader', w, 'light', **st), F('Specialist', w, 'light', **st),
                F('Recruit', PISTOL, str=2), F('Recruit', PISTOL, str=2)]
    return label, f
probes = [
    chassis(RIFLE,      'BASELINE — Assault Rifle'),
    chassis(SUPPRESSOR, 'Suppressive'),
    chassis(BLEEDGUN,   'Bleeding'),
    chassis(HUNTER,     'Long Range (24")'),
    chassis(PIPE_GUN,   'Brutal + Spread'),
    chassis(MG,         'Suppressive + AP (Heavy)'),
    chassis(FLAMER,     'Blast + Fire'),
    chassis(HEAVY_PLAIN,'BASELINE — plain Heavy Melee', 'str'),
    chassis(CLEAVER,    'Cleaving + Defensive', 'str'),
    chassis(FIRE_AXE,   'Brutal + Bleeding (melee)', 'str'),
    chassis(SLEDGE,     'Heavy Impact (melee)', 'str'),
]
print(f"    {'variant':<30}{'pts':>5}{'vs Mob':>9}{'vs Horde':>10}{'vs Standard':>13}{'avg':>7}")
for lbl, fn in probes:
    c = fn()
    a = wr(fn, MOB, 0.42, N); b = wr(fn, HORDE, 0.42, N); d = wr(fn, STANDARD, 0.42, N)
    mark = "  ←" if lbl.startswith('BASELINE') else ""
    print(f"    {lbl:<30}{cost(c):>5}{a*100:>8.0f}%{b*100:>9.0f}%{d*100:>12.0f}%"
          f"{(a+b+d)/3*100:>6.0f}%{mark}")
print("\n    A variant >15 pts of win rate above its baseline at similar cost is a problem.")

# ============================================================ 6. armour vs AP
print("\n[6] ARMOUR vs ARMOUR PIERCING — does 4 pts of AP beat 10 pts of plate?")
print(f"\n    {'attacker':<26}{'no armour':>11}{'light −1':>11}{'heavy −2':>11}   armour saves")
for w in (PISTOL, RIFLE, PIPE_GUN, MG, FIRE_AXE):
    vals = []
    for arm in (0, -1, -2):
        a = min(arm + (1 if 'ap' in w['t'] else 0), 0)
        vals.append(core_x(w['dmg'] + a))
    ap = ' (AP)' if 'ap' in w['t'] else ''
    saved = (vals[0] - vals[2]) * 100
    print(f"    {w['name']+ap:<26}" + "".join(f"{v*100:>10.0f}%" for v in vals)
          + f"   heavy: −{saved:.0f} pts")

# ============================================================ 7. DEX vs STR
print("\n[7] DEX vs STR — do ranged weapons compete now that they carry payloads?")
def GUNLINE():      # 4 · 99, pure DEX, zero STR
    return [F('Leader', RIFLE, dex=4), F('Specialist', MG, dex=4),
            F('Recruit', PISTOL, dex=2), F('Recruit', PISTOL, dex=2)]
def BRAWLERS():     # 6 · 99, pure STR
    return [F('Leader', HEAVY_PLAIN, 'light', str=4),
            F('Specialist', HEAVY_PLAIN, str=4),
            F('Recruit', CROWBAR, str=2), F('Recruit', CROWBAR, str=2),
            F('Rabble', BAT), F('Rabble', BAT)]
print(f"\n    Gunline {cost(GUNLINE())} pts / {len(GUNLINE())} models  vs  "
      f"Brawlers {cost(BRAWLERS())} pts / {len(BRAWLERS())} models")
print(f"\n    {'blocked':>9}{'gunline wins':>15}")
for b in (0.20, 0.30, 0.42, 0.50, 0.60):
    tag = "  ← legal board" if b == 0.42 else ""
    print(f"    {b:>8.0%}{wr(GUNLINE, BRAWLERS, b, N)*100:>14.0f}%{tag}")
print("\n" + "=" * 84)

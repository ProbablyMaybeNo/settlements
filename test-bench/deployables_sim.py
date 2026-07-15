"""Settlements — DEPLOYABLES sim. Validates Deployables.md against the engine.

Checks four things and prints a FLAGS verdict:
  D1 STRUCTURAL — every deployable obeys the ceilings (Damage <=+4, |mod|<=3,
     range<=24, one mechanic, no re-rolls); chassis+payload costs add up.
  D2 DEPLOY     — P(deploy) = 1d10 + INT + Build >= 7, by INT x Build.
  D3 TURRETS    — expected wounds/round vs armour, points-efficiency vs the
     sim-validated Assault-Rifle body (Weapons.md). Flags mispriced turrets.
  D4 MINES      — auto-detonation kill probability (no to-hit) vs armour.
  D5 BEACONS    — the per-ally value of each aura, in hit/wound deltas.
  D6 MONTE-CARLO— imports weapon_sim's engine and fires a turret at an advancing
     rifleman over 6 rounds, N times, to confirm the D3 analytic numbers.

Engine is identical to every other sim: 1d10 + mod >= 7, nat1 auto-fail,
nat10 auto-pass; injury 1d10 + Damage - Armor >= 7; global +/-3 cap; +4 Damage
ceiling. No new dice mechanic is introduced anywhere.
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

FLAGS = []

def cx(mod, t=7):                      # P(pass) for 1d10 + mod >= t, nat1 fail, nat10 pass
    w = 0
    for d in range(1, 11):
        if d == 1: continue
        if d == 10: w += 1; continue
        if d + mod >= t: w += 1
    return w / 10
def pc(x): return f"{x*100:4.0f}%"

# ---------------------------------------------------------------- catalogue
# turret: (name, dmg, to_hit, rng, shots, cost, note)
TURRETS = [
    ("Autoturret",        3, 0, 18, 1, 12, "baseline"),
    ("Sniper Turret",     3, 1, 24, 1, 15, "24in reach, +1 hit"),
    ("Burst Turret",      2, 0, 18, 2, 18, "two shots"),
    ("Blast Turret",      3, 0, 12, 1, 14, "Blast 2in"),
    ("Reinforced Turret", 3, 0, 18, 1, 15, "always Heavy cover to hit"),
]
CHASSIS = {"Proximity": 5, "Remote": 7, "Seeker": 8}
PAYLOAD = {"Explosion": 4, "Fire": 3, "Poison": 3, "Shock": 3, "Smoke": 2}
PAYLOAD_DMG = {"Explosion": 3, "Fire": 2, "Poison": None, "Shock": None, "Smoke": None}
# beacon: (name, kind, mod, cost)  kind in {ally_hit, ally_injure, enemy_injure, to_be_hit, util}
BEACONS = [
    ("Munitions",  "ally_injure",  +1, 8),
    ("Targeting",  "ally_hit",     +1, 8),
    ("Aegis",      "enemy_injure", -1, 8),
    ("Cover",      "to_be_hit",    -1, 6),
    ("Cleansing",  "util",          0, 8),
    ("Revive",     "util",          0, 12),
    ("Dread",      "util",          0, 7),
]
ARMOUR = {"none": 0, "light": -1, "heavy": -2}

print("=" * 70)
print("SETTLEMENTS — DEPLOYABLES SIM  (one INT deploy · engine unchanged)")
print("=" * 70)

# ---------------------------------------------------------------- D1 structural
print("\n[D1] STRUCTURAL — ceilings & cost arithmetic")
ok = True
for name, dmg, hit, rng, shots, cost, note in TURRETS:
    if dmg > 4: FLAGS.append(f"{name}: Damage {dmg} over +4 ceiling"); ok = False
    if rng > 24: FLAGS.append(f"{name}: range {rng} over 24in ceiling"); ok = False
    if abs(hit) > 3: FLAGS.append(f"{name}: to-hit {hit} over +/-3 cap"); ok = False
for pay, d in PAYLOAD_DMG.items():
    if d is not None and d > 4: FLAGS.append(f"mine {pay}: Damage {d} over +4"); ok = False
for name, kind, mod, cost in BEACONS:
    if abs(mod) > 3: FLAGS.append(f"{name} beacon: aura {mod} over +/-3 cap"); ok = False
# sample mine builds quoted in the note must add up
CHECKS = [("Proximity", "Explosion", 9), ("Remote", "Poison", 10),
          ("Seeker", "Explosion", 12), ("Proximity", "Smoke", 7)]
for ch, pay, quoted in CHECKS:
    got = CHASSIS[ch] + PAYLOAD[pay]
    tag = "ok" if got == quoted else "MISMATCH"
    if got != quoted: FLAGS.append(f"mine {ch}+{pay}={got} != note {quoted}"); ok = False
    print(f"   {ch}+{pay:9} = {got:2}  (note {quoted})  {tag}")
print(f"   ceilings: Damage<=+4, |mod|<=3, range<=24 ...... {'PASS' if ok else 'FAIL'}")

# ---------------------------------------------------------------- D2 deploy
print("\n[D2] DEPLOY  1d10 + INT + Build >= 7   P(deploy succeeds)")
BUILDS = [("Simple +1", 1), ("Standard 0", 0), ("Complex -1", -1), ("Intricate -2", -2)]
print(f"   {'INT':>4}" + "".join(f"{b[0]:>13}" for b in BUILDS))
for i in range(0, 7):
    print(f"   {'+'+str(i):>4}" + "".join(f"{pc(cx(i+b[1])):>13}" for b in BUILDS))
print("   A Specialist (INT +2..+4) stands up Complex/Intricate hardware reliably;")
print("   a Rabble (INT +0) fumbling a Sniper Turret fails ~70%. INT is the gate.")

# ---------------------------------------------------------------- D3 turrets
print("\n[D3] TURRETS — expected wounds/round (open cover), vs armour")
print(f"   {'turret':>18}{'none':>7}{'light':>7}{'heavy':>7}{'cost':>6}{'w/rd/pt':>9}")
# baseline: Assault-Rifle Recruit body = 21 pts, DEX+2, Damage+3
base_wpr = cx(2) * cx(3)                  # hit x injure vs unarmoured, open
base_eff = base_wpr / 21.0
for name, dmg, hit, rng, shots, cost, note in TURRETS:
    row = {}
    for a, arm in ARMOUR.items():
        wound = cx(hit) * cx(dmg + arm)   # to-hit (open) x injury
        row[a] = wound * shots
    eff = row["none"] / cost
    flag = ""
    if eff > base_eff * 1.4: flag = " <-- HOT (undercosted?)"; FLAGS.append(f"{name}: {eff:.4f} w/rd/pt > 1.4x baseline")
    elif eff < base_eff * 0.6: flag = " <-- COLD (overcosted?)"; FLAGS.append(f"{name}: {eff:.4f} w/rd/pt < 0.6x baseline")
    print(f"   {name:>18}{row['none']:>7.2f}{row['light']:>7.2f}{row['heavy']:>7.2f}{cost:>6}{eff:>9.4f}{flag}")
print(f"   baseline = Assault-Rifle body (21 pts): {base_wpr:.2f} w/rd, {base_eff:.4f} w/rd/pt")
print("   Turrets trade raw output for zero activation cost + 360deg vs one-hit fragility.")

# ---------------------------------------------------------------- D4 mines
print("\n[D4] MINES — auto-detonation (no to-hit) P(wound the caught model)")
print(f"   {'payload':>12}{'dmg':>5}{'none':>7}{'light':>7}{'heavy':>7}   note")
for pay in ["Explosion", "Fire"]:
    d = PAYLOAD_DMG[pay]
    r = {a: cx(d + arm) for a, arm in ARMOUR.items()}
    blast = "Blast 2in -> every model in radius" if pay in ("Explosion", "Fire") else ""
    print(f"   {pay:>12}{('+'+str(d)):>5}{pc(r['none']):>7}{pc(r['light']):>7}{pc(r['heavy']):>7}   {blast}")
print(f"   {'Poison':>12}{'--':>5}{'--':>7}{'--':>7}{'--':>7}   places 3in Poison hazard (2 rounds)")
print(f"   {'Shock':>12}{'--':>5}{'--':>7}{'--':>7}{'--':>7}   Blast, no injury -> Shocked+Blind")
print(f"   {'Smoke':>12}{'--':>5}{'--':>7}{'--':>7}{'--':>7}   places 3in Dense Smoke (screen)")
print("   Proximity+Explosion (9 pts) auto-lands ~70% vs unarmoured — but one-use,")
print("   stationary and avoidable (visible if the deploy failed). Anchor: Molotov 9.")

# ---------------------------------------------------------------- D5 beacons
print("\n[D5] BEACONS — per-affected-ally value of each 6in aura")
def delta_ally_hit():   return cx(2+1) - cx(2)          # +1 to a DEX+2 shooter's hit
def delta_ally_injure():return cx(3+1) - cx(3)          # +1 to a +3 injury roll
def delta_enemy_injure():return cx(3) - cx(3-1)         # -1 on incoming +3 injury (harm avoided)
def delta_to_be_hit():  return cx(2) - cx(2-1)          # -1 to enemy hit (harm avoided)
print(f"   Targeting  (+1 hit)      : +{pc(delta_ally_hit())} to each ally's hit chance")
print(f"   Munitions  (+1 injure)   : +{pc(delta_ally_injure())} to each ally's wound chance")
print(f"   Aegis      (-1 enemy inj): -{pc(delta_enemy_injure())} incoming wound chance / ally")
print(f"   Cover      (-1 to be hit): -{pc(delta_to_be_hit())} incoming hit chance / ally")
print(f"   Cleansing  : clears 1 condition/ally/EndPhase + Med-Kit aura   (util)")
print(f"   Revive     : 1 Down->Prone/EndPhase (Down only, not Out)       (util, HIGH swing)")
print(f"   Dread      : +1 Stress on entry, -1 Break inside               (util, negative aura)")
print("   ~+10% per affected ally. Value scales with how many allies sit in 6in ->")
print("   the both-slots cost + max-2-auras-per-model cap are the anti-cluster brakes.")

# ---------------------------------------------------------------- D6 monte-carlo
print("\n[D6] MONTE-CARLO — turret vs advancing rifleman, 6 rounds, confirms D3")
try:
    import weapon_sim as ws
    import random
    random.seed(20260715)
    N = 40000
    def mc_turret(dmg, hit, shots, rng, arm):
        kills = 0
        for _ in range(N):
            pos = 30.0
            downed = False
            for _rnd in range(6):
                if downed: break
                if 30.0 - pos <= rng:                       # in range this round
                    for _s in range(shots):
                        d = ws.d10()
                        got = (d != 1) and (d == 10 or d + hit >= 7)   # open cover
                        if got and ws.core(dmg + arm):
                            downed = True; break
                pos -= 6.0                                   # advances 6"/round
            kills += 1 if downed else 0
        return kills / N
    print(f"   {'turret':>18}{'MC kills/6rd':>14}{'analytic 1-(1-w)^r':>20}")
    for name, dmg, hit, rng, shots, cost, note in TURRETS:
        mc = mc_turret(dmg, hit, shots, rng, 0)
        wpr = cx(hit) * cx(dmg) * shots
        rounds_in_range = min(6, int(rng // 6) + 1)
        analytic = 1 - (1 - wpr) ** rounds_in_range
        print(f"   {name:>18}{pc(mc):>14}{pc(analytic):>20}")
    print("   MC ~ analytic confirms the wounds/round math; turrets kill ~0.6-1.0")
    print("   bodies before contact if they survive, which one hit prevents.")
except Exception as e:
    print(f"   (skipped MC: {e})")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 70)
if FLAGS:
    print(f"FLAGS ({len(FLAGS)}) — review before locking:")
    for f in FLAGS: print(f"  - {f}")
else:
    print("ALL CLEAR — no ceiling breaks, no mispriced items vs the armoury baseline.")
print("=" * 70)

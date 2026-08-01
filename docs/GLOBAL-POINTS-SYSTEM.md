# Settlements — Global Points System

**Version:** 0.1 · **Scale:** 1000 Credits = standard Crew Rating  
**Status:** provisional (tune with sim) · **Engine:** `test-bench/points/` · **Export:** `costs/catalogue_v0.json`  
**Decisions:** `docs/POINTS-DECISIONS.md`

Players never see the formulas below. They only see final **Credits** / **Materials** prices on catalogue entries.

---

## How Crew Rating works

1. Agree a rating cap (standard **1000**).
2. Each fielded fighter costs: **body Credits + equipped gear Credits**.
3. **Stashed / unequipped gear = 0** toward rating.
4. Hire and buy kit with **Credits**. That same Credits number is what counts when the item is on a fielded fighter.

```
crew_rating = sum(body + equipped_weapons + armour + equipment)  for each fielded fighter
crew_rating ≤ agreed_cap
```

---

## Resources (campaign layer)

| Resource | Use |
|---|---|
| **Credits** | Hire crew, buy equipment, primary currency. Fielded Credits = Crew Rating. |
| **Materials** | Build / upgrade structures. Convert to Credits at a **Trader** (rate TBD). |
| **Power** | Assigned each Settlement round. Generator **+5**. Structure draw: **T1=1 · T2=2 · T3=3**. Unpowered = no benefit this round (still on board). |

**Water is cut.** Population brake = housing slots only.

---

## Settlement dials

| Dial | Value |
|---|---|
| Standard Crew Rating | **1000** |
| HQ housing slots | **12** |
| Bunkhouse | **+6** slots |
| Equipment slots (start) | **30** |
| Per Equipment Shed / Armory tier | **+30** slots |
| Generator Power | **+5** |
| Founding budget | enough for **1–2** extra structures |
| Pyramid | **founding crew only**; always **1 Leader** max |
| Veterans | get more expensive as they Advance |
| Scars | rules penalties only — **no** price change |

---

## The tick (designer only)

```
1 TICK = 10 Credits
```

| Atom | Credits | Notes |
|---|:--:|---|
| Unconditional +1 on a test | 10 | Rare as flat gear |
| +1 injury (Brutal / Armour Piercing) | **40** | Legacy ×10 spine |
| Conditional +1 hit (Accurate-class) | **30** | Discounted |
| Standard payload (Fire, Shock, …) | **30** | |
| Bleed payload | **40** | Deadliest |
| Path-stat point inside a rank bundle | **15** | Not sold à la carte |
| Body base (WND 1 + MOV 6") | **20** | |
| 1 Order premium | **40** | |
| 2 Orders premium (Leader) | **90** | Super-linear |

**Weapon formula:** `class + characteristics − drawbacks`  
**Body formula:** `20 + (stat_points × 15) + order_premium`  
**Advance:** +1 stat = **+15**; new skill = **+20 / +35 / +55** (T1/T2/T3); promotion = difference in body cost

---

## Rank bodies (Credits)

| Rank | Stat pts | Orders | Credits |
|---|:--:|:--:|:--:|
| **Recruit** | 3 | 0 | **65** |
| **Fighter** | 5 | 0 | **95** |
| **Specialist** | 7 | 1 | **165** |
| **Leader** | 9 | 2 | **245** |

---

## Weapon classes (Credits)

| Class | Credits | Damage | Range | Slots | Min rank |
|---|:--:|:--:|:--:|:--:|---|
| Unarmed | 0 | +0 | melee | 0 | Any |
| Light Melee | 0 | +1 | melee | 2 | Recruit |
| One-Handed Melee | **40** | +2 | melee | 2 | Fighter |
| Heavy Melee | **80** | +3 | melee | 3 | Specialist |
| Thrown | **20** | +1 | 6" | 2 | Any |
| Sidearm | **40** | +2 | 8" | 2 | Recruit |
| Standard Ranged | **100** | +3 | 18" | 3 | Fighter |
| Heavy Ranged | **140** | +3 | 24" | 4 | Specialist |

Hard caps: damage ≤ **+4** · range ≤ **24"** · max **2** drawbacks.

---

## Characteristics (Credits)

| Characteristic | Credits | Effect |
|---|:--:|---|
| Brutal | 40 | +1 Damage (max +4) |
| Armour Piercing | 40 | Target armour −1 on Injury |
| Accurate | 30 | +1 hit if you did not Move/Sprint/Climb |
| Spread | 30 | +1 hit at ≤ half range; −1 beyond |
| Concussive | 30 | Payload: Off-Balance |
| Crippling | 30 | Payload: Hobbled |
| Blinding | 30 | Payload: Blind |
| Shocking | 30 | Payload: Shocked |
| Toxic | 30 | Payload: Poison |
| Incendiary | 30 | Payload: Fire |
| Bleeding | 40 | Payload: Bleed |
| Heavy Impact | 30 | Push 2" |
| Hook | 20 | Pull 1" (melee) |
| Suppressive | 40 | Cannot clear Pin with Move alone |
| Blast | 40 | Resolve vs every model within 2" |
| Smoke | 30 | Place 3" Dense Smoke |
| Long Range | 60 | +6" range (to 24" ceiling) |
| Balanced | 20 | Use AGI for melee |
| Defensive | 30 | +1 opposed melee when not attacker / didn't Move |
| Cleaving | 50 | Injury vs every Engaged enemy on melee win |
| Breaching | 30 | +2 STR vs Breachable |
| Concealable | 20 | May start Hidden / smuggle |
| Quiet | 20 | No reveal / no noise |
| Compact | 20 | Counts as one-handed (heavy classes) |

### Drawbacks (refund Credits)

| Drawback | Refund | Effect |
|---|:--:|---|
| Short Range | −30 | Halve max range |
| Slow | −30 | May not Charge (melee) |
| Unstable | −20 | Nat 1 to hit → weapon destroyed |
| Cumbersome | −20 | −1 MOV while carried |
| Limited | −30 | One use per battle |

---

## Armour & kit (Credits)

| Armour | Credits | Injury | Drawback |
|---|:--:|:--:|---|
| None / Thick clothing | 0 | 0 | — |
| Improvised | **30** | −1 | −1 AGI |
| Light | **60** | −1 | — |
| Heavy | **100** | −2 | −1 MOV, −1 AGI, Loud |

| Equipment | Credits |
|---|:--:|
| Med-Kit | 40 |
| Breach Kit | 40 |
| Exploit Suite | 80 |

---

## Sample armoury (Credits)

| Name | Build | Credits |
|---|---|:--:|
| Baseball Bat | Light Melee | **0** |
| Kitchen Knife | Light Melee · Balanced · Concealable | **40** |
| Crowbar | One-Handed Melee · Breaching | **70** |
| Great Axe | Heavy Melee | **80** |
| Sledgehammer | Heavy Melee · Heavy Impact · Breaching | **140** |
| Fire Axe | Heavy Melee · Brutal · Bleeding | **160** |
| Reaping Hook | Heavy Melee · Cleaving · Defensive | **160** |
| Pistol | Sidearm | **40** |
| Pipe Shotgun | Standard Ranged · Brutal · Spread · Short Range · Unstable | **120** |
| Assault Rifle | Standard Ranged · Accurate | **130** |
| Nailgun | Standard Ranged · Bleeding | **140** |
| Grandpa's Hunting Rifle | Standard Ranged · Accurate · Long Range | **190** |
| Squad Machine Gun | Heavy Ranged · Suppressive · Armour Piercing | **220** |
| Makeshift Flamethrower | Heavy Ranged · Incendiary · Blast · Short Range · Limited | **150** |
| Molotov | Thrown · Incendiary · Blast | **90** |
| Smoke Grenade | Thrown · Smoke | **50** |

### Construction examples

| Build | Math | Credits |
|---|---|:--:|
| Auto Rifle + Fire | Standard Ranged 100 + Incendiary 30 | **130** |
| Machete + Shock | One-Handed 40 + Shocking 30 | **70** |
| Brutal Machete + Shock | 40 + Brutal 40 + Shocking 30 | **110** |

---

## Structures (Materials)

Formula: `footprint_band + role_band + (power_draw × 15)`  
Tier 2 ≈ ×1.6 of T1 · Tier 3 ≈ ×1.75 of T2.

| Footprint | Band | Role | Band |
|---|:--:|---|:--:|
| Station / line | 25 | Sustain | +0 |
| Plant / yard | 40 | Gatherer | +25 |
| Building | 75 | Convert | +35 |
| Large | 100 | Operate | +40 |
| | | Recover | +30 |
| | | Defend | +45 |

### Catalogue (v0 derived)

| Structure | Tier | Power | Materials | Starter |
|---|:--:|:--:|:--:|:--:|
| HQ | 1 | −1 | **130** | yes |
| Generator | 1 | +5 out | **40** | yes |
| Processor | 1 | −1 | **80** | yes |
| Salvage Yard | 1 | −1 | **80** | yes |
| Bunkhouse | 1 | −1 | **115** | |
| Storehouse | 1 | −1 | **90** | |
| Equipment Shed | 1 | −1 | **40** | |
| Armory | 2 | −2 | **168** | |
| Workbench | 1 | −1 | **75** | |
| Workshop | 2 | −2 | **224** | |
| Trader's Kiosk | 1 | −1 | **75** | |
| Trade House | 2 | −2 | **224** | |
| Fabricator | 1 | −1 | **125** | |
| Med-bay | 1 | −1 | **120** | |
| Holding Cells | 1 | −1 | **120** | |
| Scout Post | 1 | −1 | **95** | |
| Comms Mast | 1 | −1 | **95** | |
| Vault | 1 | −1 | **95** | |
| Perimeter Wall (6" seg) | 1 | −1 | **85** | |
| Gatehouse | 1 | −1 | **135** | |
| Watchtower | 1 | −1 | **100** | |
| Turret Mount | 2 | −2 | **184** | |
| EW Mast | 2 | −2 | **184** | |
| Drone Bay | 2 | −2 | **272** | |
| Server Core | 2 | −2 | **232** | |
| Groundworks I | — | — | **120** | project |
| Groundworks II | — | — | **200** | project |

Starter Power check: draw **3** / Generator **+5**.

Water structures (Reclaimer / Cistern / Water Tower) are **cut** for now.

---

## Worked crew example

**Leader** (245) + Light armour (60) + Assault Rifle (130) + Med-Kit (40) = **475**  
**Fighter** (95) + Pistol (40) = **135**  
**Fighter** (95) + Crowbar (70) = **165**  
**Recruit** (65) + Bat (0) = **65**  
**Recruit** (65) + Bat (0) = **65**  

**Crew total = 905** of 1000 (95 left for more kit or another Recruit).

After one Advance that buys +1 DEX on the Leader: Leader body becomes 245+15 = **260** → crew **920**.

---

## Caps (costing preconditions)

- Damage ≤ +4 · Armour ≥ −2 · Modifier ±3 · Range ≤ 24"
- WND = 1 · MOV = 6" (except named skills)
- Legal board: **9–12** large features
- Extra attacks / multi-action: **rank/tier gated**, never sold as a flat Credits line
- Thresholds are gated, not priced

---

## Engine

```
cd test-bench
py -3.13 -m points
```

Regenerates `costs/catalogue_v0.json` and verifies sample armoury math.

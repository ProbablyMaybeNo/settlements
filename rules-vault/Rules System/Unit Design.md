---
type: rule-phase
phase: "06"
stage: S2 Core Combat
status: Drafted
build_order: 4
depends_on:
  - Rules Engine
feeds_into:
  - Movement
  - Shooting
  - Melee
  - List Building
  - Factions
tags:
  - settlements/phase
  - settlements/stage/s2
---
# 06 · Unit Design
> **S2 Core Combat** · status **Drafted** · build order **4**

**Depends on:** [[Rules Engine]]
**Feeds into:** [[Movement]], [[Shooting]], [[Melee]], [[List Building]], [[Factions]]
**Raw dependency (from Notion):** Rules Engine

## Focus
The stat line FIRST — every other system references it. Define the data card before anything else in combat.

The Rules column should nail down:
- Each stat and exactly what it governs: Wounds, Move, Strength, Agility, Dexterity, Intelligence, Nerve.
- Rank structure (Recruit / Fighter / Specialist / Leader) and how Fielding caps work — Role is emergent, not a separate unlock tree.
- The data-card layout: stats + skills/abilities + equipment + narrative/identity.
- How weapons & armour attach (separate profiles vs baked into the unit) — decide this here, it drives Shooting/Melee/Damage.
- Baseline human numbers to anchor the whole game; how champions/leaders/veterans scale above baseline.

## Inherits from the engine
> [!info] Recall — a stat is just the modifier a fighter brings to a [[Rules Engine#Universal Resolution Mechanic|core test]]. Design every number against this ±10%-per-point curve.

![[core-000 Core Test#Probability]]

The engine already spends these stats: **Dexterity** → ranged tests · **Strength** → melee · **Morale** → the Nerve/Morale system. Specialists and Leaders also carry the Command economy from [[Rules Engine#Universal Action Economy]].

## Working rules / decisions

### UNIT STATISTICS

**Wounds — WND**

How many serious hits a unit can suffer before it goes down. Most units have 1 Wound.

**Move — MOV**

The number of inches a unit may move when it takes a Move action. The standard human Move is 6".

**Strength — STR**

Used for physical force, including melee combat, breaching doors, smashing obstacles, dragging heavy objects, carrying wounded units, moving terrain, and constructing barricades or defenses.

**Agility — AGI**

Used for physical movement tests, including jumping, climbing, vaulting, balancing, swinging, crawling, dodging hazards, avoiding falls, and escaping dangerous positions.

**Dexterity — DEX**

Used for precise hand-eye actions, including ranged combat, throwing objects, lockpicking, setting traps, disarming traps, and using delicate equipment.

**Intelligence — INT**

Used for technical and knowledge-based actions, including hacking, crafting, repairing, medicine, searching, identifying terrain features, and using complex equipment.

**Nerve — NRV**

Used to test a unit’s mental state under pressure, including stress

### Stat Scale
Only the **five path-stats** (STR, AGI, DEX, INT, NRV) take stat points. **WND stays 1 and MOV stays 6"** — they rise only via a specific [[Skills|skill]], never from points. Each **+1 ≈ +10%** on a [[core-000 Core Test|core test]] (bounded 10–90%).

| Value | Meaning | Skill tier (none) |
|:---:|---|:---:|
| −1 | Impaired — injured, panicked, exhausted | — |
| 0 | Civilian baseline | — |
| +1 | Capable | — |
| +2 | Skilled | — |
| +3 | Trained | — |
| +4 | Veteran | — |
| +5 | Elite | — |
| +6 | Peak / master | — |

^tbl-stat-scale

**Max is +6**, which keeps the clean 2-point tier cadence. A flat test still tops out at 90% (the natural-1 floor), so +5 and +6 read the same on an *unmodified* roll — the extra point earns its keep against cover, armour, and opposed rolls.

### Rank vs Role
Two separate axes — don't conflate them:
- **Rank** = a unit's **command slot**, limited by [[List Building]]. It sets stat points, skill slots, Orders, and caps. Only **Rank** is restricted. Skill acquisition is pending.
- **Role** = what a unit is *good at* (Brawler, Shooter, Techie, Medic…). It **emerges** from stats, [[Skills|skills]], gear and scars — unlimited and narrative, and never restricts fielding.

### Ranks (build budget)
Units buy up from the civilian baseline with **stat points**, spent only on the five path-stats.

Skill acquisition and starting counts: **undecided**; see [[Skills#Acquisition]].

| Rank | Stat pts | Stat allocation caps (per stat line) | Skills* | Orders | Credits |
|---|:---:|---|:---:|:---:|:---:|
| **Recruit** | **3** | none — each stat at most +1 | **0** | 0 | **70** |
| **Fighter** | **5** | up to **2 stats reaching +2** | **Undecided** | 0 | **100** |
| **Specialist** | **7** | **Undecided** | **Undecided** | 1 | **145** |
| **Leader** | **9** | **Undecided** | **Undecided** | 2 | **185** |

^tbl-ranks-build-budget

Skill acquisition and starting counts: **undecided**; see [[Skills#Acquisition]].

Skill acquisition and starting counts: **undecided**; see [[Skills#Acquisition]].


- **The stat allocation caps are the ceiling** — they set how many stats a rank may push to each tier, so points *must* spread. A Fighter (5 pts, max 2 stats reaching +2) builds e.g. `STR+2 / INT+2 / AGI+1` — a brawler who can also hack. Only a **Leader** ever gets a — (a +6 elite stat) — its signature.
Skill acquisition and starting counts: **undecided**; see [[Skills#Acquisition]].

- **Rank is also a weapon gate** — a Recruit physically cannot hold a rifle ([[Weapons#Rank gates the class]]).
- A **Leader is a fighter with Orders** — never benched. Rank rises only by deliberate **promotion** into an open slot ([[Progression]]), never automatically.
- Fielding caps and costs live in [[List Building]].

> [!info] The rank price **is** the stat price
> Buying a rank buys its stat points and its skills. That's why [[List Building]] never charges you separately for stats — it would be double-counting. Rank is a *bundle*.

> [!check] Bodies are now **derived from the measured stat ladder** — 2026-08-19, rescaled 2026-08-20
> The flat 15-per-stat-point is gone. Bodies compute as `body base + stat ladder + Orders premium`, on the **850-Credit** scale, and the measured ladder is **non-flat and stat-dependent**: a one-sided stat (DEX/INT/NRV) is tested against a fixed TN and **saturates** (20/15/15/10/10/5 across the six rungs), while an opposed stat (STR/AGI) cannot saturate and measures **flat at 15**. The old flat rate was wrong in *both* directions.
>
> **Validated end-to-end**: at equal Crew Rating the win-rate spread across four archetypes tightened from **31–70%** to **41–61%** (`catalogue-validation-n1500`). Re-deriving bodies halved the spread.
>
> **The weakest number left here is the Orders premium** (0 / 20 / 45) — never measured as an Order on any engine, and with no measured neighbour close enough to derive from. Tolerable only because Orders are **rank-gated and never sold à la carte**, so a list-builder cannot arbitrage them.

- Role labels (Brawler, Techie, Medic…) are **emergent** — a role is what a unit is *good at*, never a rank.

## Rule ledger
- [[adv-001 Vehicles]]
- [[adv-002 Drones]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

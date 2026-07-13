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
- Rank structure (Recruit / Specialist / Leader) and how Fielding caps work — Role is emergent, not a separate unlock tree.
- The data-card layout: stats + skills/abilities + equipment + narrative/identity.
- How weapons & armour attach (separate profiles vs baked into the unit) — decide this here, it drives Shooting/Melee/Damage.
- Baseline human numbers to anchor the whole game; how champions/leaders/veterans scale above baseline.

## Inherits from the engine
> [!info] Recall — a stat is just the modifier a fighter brings to a [[Rules Engine#Universal Resolution Mechanic|core test]]. Design every number against this ±10%-per-point curve.

![[core-000 Core Test#Probability]]

The engine already spends these stats: **Dexterity** → ranged tests · **Strength** → melee · **Morale** → the Nerve/Morale system. Champions and Leaders also carry the Command economy from [[Rules Engine#Universal Action Economy]].

## Working rules / decisions

### UNIT STATISTICS

**Wounds — WND

How many serious hits a unit can suffer before it goes down. Most units have 1 Wound.

**Move — MOV

The number of inches a unit may move when it takes a Move action. The standard human Move is 6".

**Strength — STR

Used for physical force, including melee combat, breaching doors, smashing obstacles, dragging heavy objects, carrying wounded units, moving terrain, and constructing barricades or defenses.

**Agility — AGI

Used for physical movement tests, including jumping, climbing, vaulting, balancing, swinging, crawling, dodging hazards, avoiding falls, and escaping dangerous positions.

**Dexterity — DEX

Used for precise hand-eye actions, including ranged combat, throwing objects, lockpicking, setting traps, disarming traps, and using delicate equipment.

**Intelligence — INT

Used for technical and knowledge-based actions, including hacking, crafting, repairing, medicine, searching, identifying terrain features, and using complex equipment.

**Nerve — NRV

Used to test a unit’s mental state under pressure, including stress

### Stat Scale
Only the **five path-stats** (STR, AGI, DEX, INT, NRV) take stat points. **WND stays 1 and MOV stays 6"** — they rise only via a specific [[Skill Paths|skill]], never from points. Each **+1 ≈ +10%** on a [[core-000 Core Test|core test]] (bounded 10–90%).

| Value | Meaning | Path tier |
|:---:|---|:---:|
| −1 | Impaired — injured, panicked, exhausted | — |
| 0 | Civilian baseline | — |
| +1 | Capable | — |
| +2 | Skilled | **Tier 1** |
| +3 | Trained | — |
| +4 | Veteran | **Tier 2** |
| +5 | Elite | — |
| +6 | Peak / master | **Tier 3** |

**Max is +6**, which keeps the clean 2-point tier cadence. A flat test still tops out at 90% (the natural-1 floor), so +5 and +6 read the same on an *unmodified* roll — the extra point earns its keep against cover, armour, and opposed rolls.

### Rank vs Role
Two separate axes — don't conflate them:
- **Rank** = a unit's **command slot**, limited by [[List Building]]. It sets stat points, skill slots, Orders, and caps. Only **Rank** is restricted.
- **Role** = what a unit is *good at* (Brawler, Shooter, Techie, Medic…). It **emerges** from stats, [[Skill Paths|skills]], gear and scars — unlimited and narrative, and never restricts fielding.

### Ranks (build budget)
Units buy up from the civilian baseline with **stat points**, spent only on the five path-stats.

| Rank | Stat points | → Skills | Orders | Start cap | Cost |
|---|:---:|:---:|:---:|:---:|:---:|
| **Rabble** | **0** | **0** | 0 | — | 5 |
| **Recruit** | 2 | 1 | 0 | +2 | 8 |
| **Specialist** | 4 | 2 | 1 | +4 | 16 |
| **Leader** | 6 | 3 | 2 | +4 | 24 |

- **One currency:** every **+2** in a path-stat unlocks that path's next **tier** (T1/T2/T3 at +2/+4/+6), and every **2 stat points spent = 1 skill point** ([[Skill Paths]]). So skills = points ÷ 2.
- **Rabble** are the bottom of the ladder: a body, nothing more. **Zero stat points, zero skills** — flat civilian baseline, 40% at everything, NRV 0. They exist so a *swarm* can actually be fielded; without them the cheapest fighter in the game is a Recruit with 2 points, and the mob you can picture cannot legally be built. They are chaff, screens and objective-sitters — **not** a melee force ([[List Building]]).
- **Rank is also a weapon gate** — a Rabble physically cannot hold a rifle ([[Weapons#Rank gates the class]]).
- **Start caps** keep Tier 3 as something you *earn*; campaign growth lifts the cap to **+6** ([[Progression]]).
- A **Leader is a fighter with Orders** — never benched. Rank rises only by deliberate **promotion** into an open slot ([[Progression]]), never automatically.
- Fielding caps and costs live in [[List Building]].

> [!info] The rank price **is** the stat price
> Buying a rank buys its stat points and its skills. That's why [[List Building]] never charges you separately for stats — it would be double-counting. Rank is a *bundle*.
- Role labels (Fighter, Techie, Medic…) are **emergent** — a Recruit is a *rank*, not a role.

## Rule ledger
- [[adv-001 Vehicles]]
- [[adv-002 Drones]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

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

^tbl-stat-scale

**Max is +6**, which keeps the clean 2-point tier cadence. A flat test still tops out at 90% (the natural-1 floor), so +5 and +6 read the same on an *unmodified* roll — the extra point earns its keep against cover, armour, and opposed rolls.

### Rank vs Role
Two separate axes — don't conflate them:
- **Rank** = a unit's **command slot**, limited by [[List Building]]. It sets stat points, skill slots, Orders, and caps. Only **Rank** is restricted.
- **Role** = what a unit is *good at* (Brawler, Shooter, Techie, Medic…). It **emerges** from stats, [[Skill Paths|skills]], gear and scars — unlimited and narrative, and never restricts fielding.

### Ranks (build budget)
Units buy up from the civilian baseline with **stat points**, spent only on the five path-stats.

A rank grants **more stat points than a unit can spike into one stat** — **tier caps force the spread**, so a fighter is a real character, not a single +2 in a field of zeros.

| Rank | Stat pts | Tier caps (per stat line) | Skills* | Orders | Credits |
|---|:---:|---|:---:|:---:|:---:|
| **Recruit** | **3** | none — no tiered stats | **0** | 0 | 65 |
| **Fighter** | **5** | up to **2× T1** | ~2 | 0 | 95 |
| **Specialist** | **7** | **1× T2 · 2× T1** | ~3 | 1 | 165 |
| **Leader** | **9** | **1× T3 · 2× T2 · 4× T1** | ~4 | 2 | 245 |

^tbl-ranks-build-budget

<small>*Skills are derived from the stat line — see [[Skill Paths]]. **Counts are exact, not approximate: one skill per tier a stat reaches.** The table value is the maximum, reached only when every point lands in tiered stats — a fighter who spreads into +1 "dabbles" trades skills for breadth. Costs live in [[List Building]] · [[Full Rules System v1]] §16.</small>

> [!info] Starting skills depend on the **format**, not the rank alone
> The table above is **Match Play** — a crew built for one game with no campaign attached, so it gets the richer kit. A **Campaign Start** crew is meant to *grow* through the Level track ([[Progression]]) and begins with **exactly one skill each, at the rank's own tier**: Recruit none · Fighter 1× T1 · Specialist 1× T2 · Leader 1× T3, at **65 / 75 / 125 / 170** against a 500 Crew Rating cap. Stat points, tier caps and Orders are identical in both. Full tables in [[List Building#The four ranks — two starting tiers]].

- **Tiers:** a path-stat at **+2 = Tier 1**, **+4 = Tier 2**, **+6 = Tier 3**. **+1 is a "dabble"** — capable, but not a tier (no skill). Max stat **+6**.
- **The tier caps are the ceiling** — they set how many stats a rank may push to each tier, so points *must* spread. A Fighter (5 pts, max 2× T1) builds e.g. `STR+2 / INT+2 / AGI+1` — a brawler who can also hack. Only a **Leader** ever gets a **T3** (a +6 elite stat) — its signature.
- **Skills ride the stat line:** each stat grants **one skill at every tier it reaches**, from *that stat's* path. So a **+4** stat = its **T1 *and* T2** skill; a **+6** = T1 + T2 + T3 ([[Skill Paths]]). *(Replaces the old points ÷ 2 rule.)*
- **Recruits** are the bottom of the ladder: a body, nothing more. **No tiered stat, so no skills** — 3 points of +1 dabbles over a flat civilian baseline. They exist so a *swarm* can be fielded; chaff, screens and objective-sitters — **not** a melee force ([[List Building]]).
- **Rank is also a weapon gate** — a Recruit physically cannot hold a rifle ([[Weapons#Rank gates the class]]).
- A **Leader is a fighter with Orders** — never benched. Rank rises only by deliberate **promotion** into an open slot ([[Progression]]), never automatically.
- Fielding caps and costs live in [[List Building]].

> [!info] The rank price **is** the stat price
> Buying a rank buys its stat points and its skills. That's why [[List Building]] never charges you separately for stats — it would be double-counting. Rank is a *bundle*.

> [!warning] Costs are provisional — a re-cost is owed
> The ladder is on the **1000-Credit scale** as of 2026-08-05; the old **5 / 8 / 16 / 24** numbers are retired. The Credits figures are still inherited rather than measured — `TICK_STAT` (15/stat point) and the Order premium (0/0/40/90) in `test-bench/points/ticks.py` are hand-set legacy values, unlike the weapon and condition atoms beside them, which are measured. The [[Crew Sim — Findings|sim]] shows the richer stat lines run meaningfully stronger. Locked to *play-test the structure*, not the final numbers.

- Role labels (Brawler, Techie, Medic…) are **emergent** — a role is what a unit is *good at*, never a rank.

## Rule ledger
- [[adv-001 Vehicles]]
- [[adv-002 Drones]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

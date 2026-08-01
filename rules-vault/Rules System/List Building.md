---
type: rule-phase
phase: "05"
stage: S3 Battle Layer
status: Drafted
build_order: 15
depends_on: ["Unit Design", "Weapons"]
feeds_into: ["Factions", "Scenarios", "Balance"]
tags: [settlements/phase, settlements/stage/s3]
---
# 05 · List Building
> **S3 Battle Layer** · status **Drafted** · build order **15**

**Depends on:** [[Unit Design]], [[Weapons]]
**Feeds into:** [[Factions]], [[Scenarios]], [[Balance]]

## Focus
How players assemble a legal crew — roster rules, costs, and force composition.

## The core claim
> [!info] Points buy **bodies and guns**. Stats and skills are **free**.
> Rank already caps stats and skills — a Specialist *always* has 4 stat points and 2 skills — so pricing them again is double-counting. **Buying a rank IS buying its stats.** The only things worth pricing separately are the two whose value doesn't depend on the mission: **a body, and the weapon in its hands.**
>
> It is also the honest call. [[Dice Mechanic — Sim Findings]] proved you *cannot* price a stat fairly in a vacuum — the Objective Grabber wins 24% on bare ground and the Heavy Gunner 69%. **The board prices stats. Points price bodies and guns.**

## Working rules / decisions

### Budget
A crew is built to a **points budget** set by the scenario. **Standard = 100 points.** *(75 = raid · 150 = pitched.)*

### The four ranks
The rank price *is* the stat price — see [[Unit Design#Ranks (build budget)]].

| Rank | Stat pts | Tier caps | Skills | Orders | **Cost** |
|---|:--:|---|:--:|:--:|:--:|
| **Recruit** | 3 | no tiers | 0 | 0 | **5** |
| **Fighter** | 5 | 2× T1 | ~2 | 0 | **8** |
| **Specialist** | 7 | 1× T2 · 2× T1 | ~3 | 1 | **16** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 | 2 | **24** |

^tbl-the-four-ranks

More points than a unit can spike into one stat, capped by tier so it *spreads* — full rules in [[Unit Design#Ranks (build budget)]]. Skills come off the stat line (one per tier a stat reaches). A **Specialist costs exactly two Fighters** — the central trade of the system. *(Costs are provisional; the richer stat lines run stronger — a re-cost pass is owed.)*

### The pyramid — the only structural rule
> **Exactly one Leader. Every Specialist requires two fighters of lower rank. Every Recruit requires one Fighter or better. Minimum four fighters.**

**There is no unit cap on the crew you field.** The pyramid and the budget do it: at 100 points the legal maximum is **11 fighters** (Leader + 5 Fighters + 5 Recruits, with about 11 points of gear between them — a mob with bats).

> [!warning] Per-battle only — the roster IS capped
> "No unit cap" scopes to the **crew you field in one battle**. The **roster you own** is capped by housing: a base **10** body slots from the HQ, raised by building Bunkhouses ([[Structures#The catalogue — 23 structures|Structures]]). **Housing is the only population brake** — there is no per-head upkeep *(Water cut 2026-08-01)*. Ownership and fielding are orthogonal — **Goods/Materials buy what you own, points gate what you field.**

The old ⅓-of-budget **anti-hero cap is cut** — it is redundant. WND is fixed at 1 ([[Damage]]), so a 40-point Leader in plate dies to one lucky pistol shot from a Recruit with a knife. The engine already forbids heroes.

### Loadout
- **Free to every fighter:** fists, one **Light Melee** weapon, and thick clothing. A civilian with a bat and a jacket.
- **Carry limits:** one armour · two hands (a Two-Handed weapon takes both, otherwise two one-handers) · up to **two** pieces of equipment.
- **Weapons are built, not bought** — class + characteristics, rank-gated. Full system in **[[Weapons]]**. A Recruit physically cannot hold a rifle.

### Armour & equipment

| Armour | Injury | Cost |
|---|:--:|:--:|
| None / Thick clothing | 0 | **0** |
| Light | −1 | **3** |
| Heavy | −2 | **6** |

^tbl-armour-equipment

*Armour carries no drawbacks, and the ladder is linear — each point is a flat −10% on the Injury roll, so Heavy costs exactly twice Light. Improvised was cut once its penalty went; it was Light armour under a second name. Full note in [[Weapons#3 · Armor]].*

| Equipment | Effect | Cost |
|---|---|:--:|
| Med-Kit | Cancels the −2 on Stabilize / treating Bleed & Poison ([[Damage]]) | **4** |
| Breach Kit | **+1 to the hack test** ([[Hacking]]) | **4** |
| Deployable | Turret · mine · trap · beacon — full costed catalogue in [[Deployables]] | **4–14** |
| Exploit Suite | **+2 to the hack test** ([[Hacking]]) | **8** |

^tbl-armour-equipment-2

## Campaign rosters
You keep a persistent **roster** and field a **crew** to the scenario's budget each battle.

> **Each Advance a fighter carries adds +2 points to its cost. Each lasting scar subtracts 2.**

That one line is the anti-snowball valve: **veterans crowd out rookies.** The longer a campaign runs, the smaller your crew gets — the war grinds you down to a handful of hardened survivors who then can't hold enough ground. Every campaign list becomes a real question: *field my best, or field the most?* See [[Progression]] · [[Campaign]].

## Validation
Full detail in **[[Crew Sim — Findings]]**. Eight archetypes, all built to 100 points, 3,000 battles per pairing:

| Board | Spread across all 8 lists |
|---|---|
| Sparse (illegal — under 9 features) | 35 points — **shooters dominate** |
| **Legal (9–12 features)** | **11 points** — tightest spread |
| Crowded (illegal — over 12) | 34 points — **swarms dominate** |

^tbl-validation

**The system is balanced on a legal board, and only on a legal board.** That is not a flaw — it is the [[Game Vision|first tenet]] operating as a mechanic. The battlefield decides, and [[Terrain#Setup procedure|terrain density]] is the most powerful dial in the game.

## Open dials
- [x] Rank names locked: **Recruit** (5) / **Fighter** (8) / **Specialist** (16) / **Leader** (24) — replaces the old Rabble/Recruit working titles.
- [ ] Budget 100 and the 5/8/16/24 ladder — validated in sim, not yet at a table.
- [ ] NRV is close to a dead stat at Fighter level; it earns its keep only through Bravery *skills*.

## Rule ledger
_none yet — graduate a `core-00X List building` card after first playtest._

---
_See [[Rules System MOC]] · [[Unit Design]] · [[Weapons]] · [[Terrain]] · [[Crew Sim — Findings]]._

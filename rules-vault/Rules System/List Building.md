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
A crew is built to a **Crew Rating** cap in **Credits**, set by the scenario.

| Format | Cap |
|---|:--:|
| **Match Play** — a one-off game, no campaign attached | **1000** |
| Raid variant | 750 |
| Pitched variant | 1500 |
| **Campaign Start** — a fresh crew entering the settlement layer | **500** |

^tbl-budget

*The **100-point** budget and its 5/8/16/24 ladder are **retired**. Everything is on the 1000-Credit scale ([[Full Rules System v1]] §16). One number does both jobs: you buy with Credits, and the Credits you field are your Crew Rating.*

### The four ranks — two starting tiers
The rank price *is* the stat price — see [[Unit Design#Ranks (build budget)]].

**Match Play** gets the richer starting kit, because those fighters are built for one game and never get another chance to develop.

| Rank | Stat pts | Tier caps | Skills | Orders | **Credits** |
|---|:--:|---|:--:|:--:|:--:|
| **Recruit** | 3 | no tiers | 0 | 0 | **65** |
| **Fighter** | 5 | 2× T1 | ~2 | 0 | **95** |
| **Specialist** | 7 | 1× T2 · 2× T1 | ~3 | 1 | **165** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 | 2 | **245** |

^tbl-the-four-ranks

**Campaign Start** is a green crew *meant* to grow through the Level track ([[Progression]]), so it starts lean — **exactly one skill each, at the rank's own tier.**

| Rank | Stat pts | Tier caps | Starting skill | Orders | **Credits** |
|---|:--:|---|:--:|:--:|:--:|
| **Recruit** | 3 | no tiers | — | 0 | **65** |
| **Fighter** | 5 | 2× T1 | 1× T1 | 0 | **75** |
| **Specialist** | 7 | 1× T2 · 2× T1 | 1× T2 | 1 | **125** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | 1× T3 | 2 | **170** |

^tbl-the-four-ranks-campaign

More points than a unit can spike into one stat, capped by tier so it *spreads* — full rules in [[Unit Design#Ranks (build budget)]]. Skills come off the stat line (one per tier a stat reaches).

> [!warning] The Campaign Start column is a first draft and the sim disagrees with it
> Those prices were **backed out arithmetically** from the Match Play column by subtracting skill Credit values (T1 20 / T2 35 / T3 55) — never measured. `test-bench/balance/campaign500.py` (2026-08-05, 15,000 games/ladder) found that at a **500** cap a crew is only **2–4 models**, the mandatory Leader eats **34%** of the budget against Match Play's 24%, and a shooting list is unbuildable — the Gunline archetype won **18%**. No rank ladder tested closed that gap, because the binding constraint is the cap, not the prices. Treat the 500 column as provisional until that is settled.

### The pyramid — two versions
> **Match Play:** exactly one Leader. Every Specialist requires two fighters of lower rank. Every Recruit requires one Fighter or better. Minimum four fighters.

> **Campaign Start:** exactly one Leader, **minimum three models, no ratio requirement** — any mix inside the 500 cap. Deliberately looser: a green crew hasn't built a chain of command yet, it's just whoever the founding Leader could round up. **Untested** — dropping the ratio makes all-Specialist and all-Recruit lists legal for the first time.

**There is no unit cap on the crew you field.** The pyramid and the budget do it: at 1000 Credits the legal maximum is about **11 fighters** (Leader + 5 Fighters + 5 Recruits, with roughly 110 Credits of gear between them — a mob with bats).

> [!warning] Per-battle only — the roster IS capped
> "No unit cap" scopes to the **crew you field in one battle**. The **roster you own** is capped by housing: a base **10** body slots from the HQ, raised by building Bunkhouses ([[Structures#The catalogue — 23 structures|Structures]]). **Housing is the only population brake** — there is no per-head upkeep *(Water cut 2026-08-01)*. Ownership and fielding are orthogonal — **Credits/Materials buy what you own, points gate what you field.**

The old ⅓-of-budget **anti-hero cap is cut** — it is redundant. WND is fixed at 1 ([[Damage]]), so a 40-point Leader in plate dies to one lucky pistol shot from a Recruit with a knife. The engine already forbids heroes.

### Loadout
- **Free to every fighter:** fists, one **Light Melee** weapon, and thick clothing. A civilian with a bat and a jacket.
- **Carry limits:** one armour · two hands (a Two-Handed weapon takes both, otherwise two one-handers) · up to **two** pieces of equipment.
- **Weapons are built, not bought** — class + characteristics, rank-gated. Full system in **[[Weapons]]**. A Recruit physically cannot hold a rifle.

### Armour & equipment

| Armour | Injury | Credits |
|---|:--:|:--:|
| None / Thick clothing | 0 | **0** |
| Light | −1 | **60** |
| Heavy | −2 | **100** |

^tbl-armour-equipment

> [!bug] Armour has two prices and they disagree — unresolved
> [[Full Rules System v1]] §15 prints **60 / 100** (above). The costing engine `test-bench/points/ticks.py` carries **30 / 60**, marked *[measured]*. That is a **2× gap on every armoured fighter in the game**. The engine's provenance is also broken: `POINTS-COMPLETION-PLAN.md` M2 records that `balance/armourprice.py`, the file both `ticks.py` and `POINTS-TABLE.md` §7 cite as the source, **does not exist in the repo**. Neither number can currently be re-derived. Rebuild the sweep before locking either.

*Armour carries no drawbacks, and the ladder is linear — each point is a flat −10% on the Injury roll, so Heavy costs exactly twice Light. Improvised was cut once its penalty went; it was Light armour under a second name. Full note in [[Weapons#3 · Armor]].*

| Equipment | Effect | Credits |
|---|---|:--:|
| Med-Kit | Cancels the −2 on Stabilize / treating Bleed & Poison ([[Damage]]) | **40** |
| Breach Kit | **+1 to the hack test** ([[Hacking]]) | **40** |
| Deployable | Turret · mine · trap · beacon — full costed catalogue in [[Deployables]] | **30–180** |
| Exploit Suite | **+2 to the hack test** ([[Hacking]]) | **80** |

^tbl-armour-equipment-2

## Campaign rosters
You keep a persistent **roster** and field a **crew** to the scenario's budget each battle.

> **Each Level a fighter has gained adds its own printed Credit cost to that fighter. Scars cost nothing and refund nothing.**

Levels are a **fixed track**, not a freeform spend, and each rung has a price: 15 per stat point, 20/35/55 per T1/T2/T3 skill, 45 for the Level-7 wound. A fighter who runs the whole track carries **+245 Credits** over their rank body. Full table in [[Progression#Levels — the fixed advancement track]]. *(This replaces the old flat "+2 per Advance", which was written on the retired 100-point scale.)*

That first half is the anti-snowball valve: **veterans crowd out rookies.** The longer a campaign runs, the smaller your crew gets — the war grinds you down to a handful of hardened survivors who then can't hold enough ground. Every campaign list becomes a real question: *field my best, or field the most?* See [[Progression]] · [[Campaign]].

> [!success] Scars don't touch Crew Rating — ruled 2026-08-01
> A scar is a **pure nerf**. It carries rules penalties and **no change to the fighter's Credit cost**, exactly as a skill carries no separate cost of its own. The old **−2 per lasting scar** rebate is **cut**.
>
> It was working against the very valve it sat inside. A rebate makes a *scarred* veteran cheaper to field, which is backwards twice over: it softens the grind the valve exists to create, and it quietly rewards you for having fighters maimed. Removing it makes the ladder honest — Advances raise your cost, injuries just make you worse, and neither one pays for the other.
>
> The real question a scarred veteran now poses is the right one: *this fighter costs more than a rookie **and** is worse than they were — is what they can still do worth the Credits?* Sometimes the answer is to bench them, or spend a Med-bay visit ([[Structures]]). See `POINTS-DECISIONS.md` D14 · D27.

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
- [x] Rank names locked: **Recruit / Fighter / Specialist / Leader** — replaces the old Rabble/Recruit working titles.
- [x] Scale moved to **1000 Credits**; the old 5/8/16/24 ladder is retired *(2026-08-05, [[Full Rules System v1]] §16)*.
- [ ] Match Play **65/95/165/245 at 1000** — sim-validated on the old 100-point scale (an 11-point spread across 8 archetypes), not yet at a table.
- [ ] Campaign Start **65/75/125/170 at 500** — **not validated; the sim contradicts it.** See the warning above and `test-bench/balance/campaign500.py`.
- [ ] NRV is close to a dead stat at Fighter level; it earns its keep only through Bravery *skills*.

## Rule ledger
_none yet — graduate a `core-00X List building` card after first playtest._

---
_See [[Rules System MOC]] · [[Unit Design]] · [[Weapons]] · [[Terrain]] · [[Crew Sim — Findings]]._

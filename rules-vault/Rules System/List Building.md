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

> [!info] Superseded — [[Full Rules System v1]] is the ruling
> **§16 is canonical for costs and composition.** The old 5/8/16/24 ladder on the 100-point budget is deprecated; everything is on the 1000-Credit scale. Match Play skill counts are now *exact* (one per tier a stat reaches), and Campaign Start keeps the Specialist ratio.

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
| **Recruit** | 3 | no tiers | 0 | 0 | **70** |
| **Fighter** | 5 | 2× T1 | ~2 | 0 | **100** |
| **Specialist** | 7 | 1× T2 · 2× T1 | ~3 | 1 | **145** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 | 2 | **185** |

^tbl-the-four-ranks

**Campaign Start** is a green crew *meant* to grow through the Level track ([[Progression]]), so it starts lean — **exactly one skill each, at the rank's own tier.**

| Rank | Stat pts | Tier caps | Starting skill | Orders | **Credits** |
|---|:--:|---|:--:|:--:|:--:|
| **Recruit** | 3 | no tiers | — | 0 | **70** |
| **Fighter** | 5 | 2× T1 | 1× T1 | 0 | **100** |
| **Specialist** | 7 | 1× T2 · 2× T1 | 1× T2 | 1 | **145** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | 1× T3 | 2 | **185** |

^tbl-the-four-ranks-campaign

More points than a unit can spike into one stat, capped by tier so it *spreads* — full rules in [[Unit Design#Ranks (build budget)]]. Skills come off the stat line (one per tier a stat reaches).

> [!warning] The Campaign Start column is a first draft, and the sim says the **cap** is the problem, not the prices
> Those prices were **backed out arithmetically** from the Match Play column by subtracting skill Credit values (T1 20 / T2 35 / T3 55) — never measured. `test-bench/balance/campaign500.py` (2026-08-05, 30,000 games per configuration, six archetypes × four scenarios, sides swapped) found:
> - At **500** a crew is only **2–4 models**, and the mandatory Leader eats **34%** of the budget against Match Play's 24%.
> - **A shooting list cannot be built at 500.** Gunline won **18%**. Leader + rifle (270) + Fighter + rifle (175) = 445, and the cheapest third body is 65 — so a rifle-armed Leader puts the crew **below this note's own three-model minimum**.
> - **Six rank ladders were swept** — the one above, Match Play prices, skills-charged, and body-scale ×0.75 / ×0.5 / ×0.35. Spread never fell below **21 points**, and the only ladder that reached it did so by shrinking every crew to two models. **No ladder fixes it.**
> - **Sweeping the cap does.** Holding this ladder fixed: 500 → **46**-point spread · 625 → **32** · 750 → **32** · 875 → 37 · 1000 → 36. The penalty is specific to 500 and disappears by 625.
>
> The cleanest fix is therefore **not** a new rank ladder — it is to raise the Campaign Start cap to about **625–750**, or to cut the price of the mandatory Leader specifically. Left as-is pending your call.

### The pyramid — two versions
> **Match Play:** exactly one Leader. Every Specialist requires two fighters of lower rank. Every Recruit requires one Fighter or better. Minimum four fighters.

> **Campaign Start:** exactly one Leader, **minimum three models, no ratio requirement** — any mix inside the 500 cap. Deliberately looser: a green crew hasn't built a chain of command yet, it's just whoever the founding Leader could round up. **Untested** — dropping the ratio makes all-Specialist and all-Recruit lists legal for the first time.

**There is no unit cap on the crew you field.** The pyramid and the budget do it: at 1000 Credits the legal maximum is about **11 fighters** (Leader + 5 Fighters + 5 Recruits, with roughly 110 Credits of gear between them — a mob with bats).

> [!warning] Per-battle only — the roster IS capped
> "No unit cap" scopes to the **crew you field in one battle**. The **roster you own** is capped by housing: a base **12** body slots from the HQ, **+6** per Bunkhouse ([[Structures#The catalogue — 23 structures|Structures]]). **Housing is the only population brake** — there is no per-head upkeep *(Water cut 2026-08-01)*. Ownership and fielding are orthogonal — **Credits buy what you own, Crew Rating gates what you field.** *(HQ housing was 10 here and 12 in the decisions log; [[Full Rules System v1]] §17.2 rules **12**.)*

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

> [!success] Armour: 60 / 100 is the better number — re-measured 2026-08-05
> Two prices were live. [[Full Rules System v1]] §15 printed **60 / 100** (above); the costing engine `test-bench/points/ticks.py` carried **30 / 60**, marked *[measured]* — a **2× gap on every armoured fighter in the game**, and unresolvable, because `POINTS-COMPLETION-PLAN.md` M2 records that the file both `ticks.py` and `POINTS-TABLE.md` §7 cite as its source (`balance/armourprice.py`) **does not exist in the repo**.
>
> `campaign500.py armour` swapped only these two numbers and held everything else fixed, 30,000 games per side:
>
> | Armour price | Armoured crew win % | Overall spread |
> |---|:--:|:--:|
> | engine 30 / 60 | **64%** — top of the table | 46 |
> | **doc 60 / 100** | **51%** — mid-table | **37** |
>
> At 30 the Armoured list is the best crew in the game; at 60 it is an average one, and the whole field tightens by 9 points. **Adopt 60 / 100 and correct `ticks.py`.** One caveat kept honest: at 60 the Armoured crew drops to two models, so part of that fall is affordability rather than pricing, and this was measured at a 500 cap only. Worth repeating at 1000 before it is called settled.

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

Levels are a **fixed track**, not a freeform spend, and each rung has a price: 15 per stat point, 20/35/55 per T1/T2/T3 skill, 41 for the Level-7 wound. A fighter who runs the whole track carries **+241 Credits** over their rank body. Full table in [[Progression#Levels — the fixed advancement track]]. *(This replaces the old flat "+2 per Advance", which was written on the retired 100-point scale.)*

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
- [ ] Match Play **70/100/145/185 at 850** — bodies re-derived from the measured stat ladder 2026-08-19 and the scale halved 2026-08-20. Validated in the sim end-to-end (`catalogue-validation-n1500`: four archetypes at equal Crew Rating land in a 38–63% band), **not yet at a table**.
- [ ] Campaign Start **70/100/145/185 at 425** — the separate Campaign-Start body table was retired 2026-08-19; both tiers now use one derived ladder and differ only in the cap and the starting skill count. The old 65/75/125/170 figures were never validated and the sim contradicted them.
- [ ] NRV is close to a dead stat at Fighter level; it earns its keep only through Bravery *skills*.

## Rule ledger
_none yet — graduate a `core-00X List building` card after first playtest._

---
_See [[Rules System MOC]] · [[Unit Design]] · [[Weapons]] · [[Terrain]] · [[Crew Sim — Findings]]._

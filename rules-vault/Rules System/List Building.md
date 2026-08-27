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
> **§16 is canonical for costs and composition.** The old 5/8/16/24 ladder is deprecated, and so is the 1000-Credit scale that replaced it — everything is on the **850-Credit** scale as of 2026-08-20. Match Play skill counts are *exact* (one per tier a stat reaches), and Campaign Start keeps the Specialist ratio.

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
| **Match Play** — a one-off game, no campaign attached | **850** |
| Raid variant *(75%)* | **640** |
| Pitched variant *(150%)* | **1275** |
| **Campaign Start** — a fresh crew entering the settlement layer | **425** |

^tbl-budget

*The 100-point budget, its 5/8/16/24 ladder, **and the 1000/500 pair that replaced them** are all retired. The scale rebased 1000 → 1700 when bodies moved onto the measured stat ladder, then halved to **850** on 2026-08-20 so a standard crew is still six models rather than four. One number does both jobs: you buy with Credits, and the Credits you field are your Crew Rating.*

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

> [!check] The old Campaign-Start squeeze was fixed by the rebuild, not by a cap change
> A 2026-08-05 sweep (`campaign500.py`, 30,000 games per configuration) found the 500-cap crew badly squeezed: **2–4 models**, the mandatory Leader eating **34%** of the budget, and **a shooting list that could not be built at all** (Gunline won 18%, because Leader + rifle at the old prices was 270 Credits on its own). Six rank ladders were swept and none fixed it; only raising the cap did.
>
> **The weapon reprice dissolved the problem from the other side.** On the 850 scale a rifle costs **35**, not 130 — so a Leader with an Assault Rifle is **220 of 425**, not 270 of 500, and a three-to-four model Campaign Start crew can carry real guns. The end-to-end check is `catalogue-validation-n1500`: at equal Crew Rating the win-rate spread across four archetypes tightened from **31–70%** to **41–61%**.
>
> **Still open:** the one remaining structural skew is that **Assault — the melee archetype — loses every matchup** (61.2% against it at worst). Whether melee is overpriced or `hold_claim` simply undervalues closing cannot be separated at 1-of-5 scenario coverage. That is a table question now.

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
| Light | −1 | **10** |
| Heavy | −2 | **20** |

^tbl-armour-equipment

> [!success] Armour is **measured**, not argued — and the doc/engine split is closed
> The old 30/60-vs-60/100 fight is over. Both were priors: the engine's 30/60 cited `balance/armourprice.py`, **a file that has never existed in any commit on any branch**, and the doc's 60/100 came from a single 500-cap sweep. Armour has since been **measured directly with zero prior** (`armour-level-n2500`) and lands at **10 / 20** on the 850 scale.
>
> **Corroborated by rebuild-to-pay**, which denominates armour in weapons surrendered rather than in a prior: `light + (rifle→pistol)` measures **+0.140 ± 0.200 — fair trade, parity**, with Heavy bracketed on both sides. First time an armour price here has been expressed in a measured quantity.
>
> **Heavy is not twice Light**, and that question is closed: the "each point is −10% so −2 must cost 2×" argument runs on the wrong quantity, because linear in injury *probability* is not linear in *win-points*. Measured ratio **1.745 ± 0.416**.

*Armour carries no drawbacks, and the ladder is linear — each point is a flat −10% on the Injury roll, so Heavy costs exactly twice Light. Improvised was cut once its penalty went; it was Light armour under a second name. Full note in [[Weapons#3 · Armor]].*

| Equipment | Effect | Credits |
|---|---|:--:|
| Med-Kit | Cancels the −2 on Stabilize / treating Bleed & Poison ([[Damage]]) | **20** |
| Breach Kit | **+1 to the hack test** ([[Hacking]]) | **20** |
| Exploit Suite | **+2 to the hack test** ([[Hacking]]) | **40** |
| Deployable | Turret · mine · trap · beacon — see [[Deployables]] | **5–25** *(9 of 24 priced)* |

> [!warning] Four lines is the whole equipment catalogue
> Every fighter carries **two** equipment slots and there are effectively two things worth putting in them. This is the thinnest catalogue in the game and the cheapest to widen — equipment is the one category that can add breadth **without touching the combat maths**, because most of it modifies a test that already exists. Flagged, not fixed.

^tbl-armour-equipment-2

## Campaign rosters
You keep a persistent **roster** and field a **crew** to the scenario's budget each battle.

> **Each Level a fighter has gained adds its own printed Credit cost to that fighter. Scars cost nothing and refund nothing.**

Levels are a **fixed track**, not a freeform spend, and each rung has a price: a stat point off the **measured ladder** (not a flat rate), **10 / 20 / 30** per T1/T2/T3 skill, and **20** for the Level-7 wound. A fully-levelled fighter carries roughly **+140 Credits** over their rank body, depending on which stats they grew. Full table in [[Progression#Levels — the fixed advancement track]].

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
- [x] Match Play **70/100/145/185 at 850** — bodies re-derived from the measured stat ladder 2026-08-19, scale halved 2026-08-20, propagated to every note 2026-08-27. Validated in the sim end-to-end (`catalogue-validation-n1500`: spread tightened 31–70% → **41–61%**), **not yet at a table**.
- [x] Campaign Start **70/100/145/185 at 425** — the separate Campaign-Start body table is retired; both tiers use one derived ladder and differ only in the cap and the starting skill count.
- [ ] **Assault (melee) loses every matchup** — the one remaining structural skew in `catalogue-validation-n1500`. Cannot be separated from single-scenario coverage without table data.
- [ ] NRV is close to a dead stat at Fighter level; it earns its keep only through Bravery *skills*.

## Rule ledger
_none yet — graduate a `core-00X List building` card after first playtest._

---
_See [[Rules System MOC]] · [[Unit Design]] · [[Weapons]] · [[Terrain]] · [[Crew Sim — Findings]]._

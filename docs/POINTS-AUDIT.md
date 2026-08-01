# Settlements — Points Costing Inventory & Audit

**Purpose.** A complete inventory of everything in Settlements that has, or will need, a points cost — ahead of a rebuild onto a single global atomic points system (points rescaled ×10; crew budget 100 → 1000; a unit's cost *is* its crew rating).

**Method.** Read-only sweep of the live rules vault (`C:\Users\Admin\Documents\Obsidian Vault\Settlements\Rules System\`, 57 notes + 13 Rules Ledger cards), the repo planning docs, and every simulation script in `test-bench\` including the untracked `engine2d\`. The repo mirror `rules-vault\` was deliberately **not** read (auto-overwritten, may be stale).

**Evidence key used throughout:**

| Tag | Meaning |
|---|---|
| **SIM** | A simulation measured it and the number traces to a script |
| **HAND** | Hand-set by the designer, internally consistent, never measured |
| **GUESS** | Explicitly labelled provisional / first-pass / anchored-by-analogy in the source |
| **UNCOSTED** | No number exists anywhere |

---

## 1 · Executive summary — the nine things that most constrain the design

**1. Points currently buy only bodies and guns. Stats and all 150 skills are free.**
> "Points buy **bodies and guns**. Stats and skills are **free**." — `List Building.md:21`
> "Buying a rank IS buying its stats." — `List Building.md:22`

Every sim implements this literally: `crew_sim.py:66`, `weapon_sim.py:105` and `engine2d\data.py:94-99` all compute unit cost as `rank + weapon + armour (+ equipment)`. **No simulation has ever priced a stat.** Moving to atomic costing means pricing something for which zero evidence exists.

**2. Terrain density is a bigger lever than any points cost, and always will be.**
> "The crew sim measured a **66-point swing** in win rate from terrain density alone — bigger than any points cost could ever produce." — `Terrain.md:133`

This is the load-bearing design fact. A global points system cannot be the primary balancer; it can only be fair *within* the 9–12 density band.

**3. Two ceilings are thresholds, not curves — and thresholds cannot be priced at all.**
> "Range stops at 24". Deployment zones sit **24" apart**… That is a **threshold**, not a linear advantage, and **no points cost can balance a threshold** — the sim found an uncapped long-range crew beating every other list by 13–30 points." — `Weapons.md:40`
> "Damage stops at +4, and only Brutal reaches it. Armour only runs to −2; if weapons ran past +4 the armour ladder would be decorative." — `Weapons.md:38`

An atomic system must keep hard gates alongside prices, not replace gates with prices.

**4. The weapon system is the only sim-validated atomic cost spine, and it is arithmetically perfect.**
All 16 entries in the sample armoury (`Weapons.md:150-167`) reconcile exactly to `class base + Σ characteristics − Σ drawbacks`, and every one is legal under its slot limit. `weapon_sim.py:55-76` machine-enforces the ceilings as assertions. **This is the model to extend** — it already works.

**5. The rank ladder's validation is stale in three specific, quantified ways — and one of them is disqualifying.**
- Every unit in every crew sim was built **exactly 3 stat points below** the current rank grant (Recruit 0/3, Fighter 2/5, Specialist 4/7, Leader 6/9 — `crew_sim.py:292-327` vs `Unit Design.md:101-106`). The vault already concedes this: *"the richer stat lines run meaningfully stronger, so expect the ladder to move **up** after a re-cost pass"* — `Unit Design.md:121-122`.
- The published headline table — "eight archetypes … 11-point spread" (`Crew Sim — Findings.md:11`) — **cannot be reproduced from any tracked script.** Four of its eight list names (Firebase, Snipers, Storm, Mob) do not exist in `crew_sim.py:329-337` (7 lists, different names) or `weapon_tests.py:103-105` (9 lists, different names). It came from a doctrine-era version now deleted.
- ⚠ **The swarm lists used in that validation are illegal under the current pyramid.** `crew_sim.py:325` comments its 14-model list *"needs The Mob doctrine (Recruit w/o Fighters)"*; `weapon_tests.py:99` says the same of its 13-model Mob; and `weapon_tests.py:112` **explicitly whitelists** the pyramid violation (`e == ["each Rabble needs a Recruit or better"]`). Doctrines were removed (`Crew Sim — Findings.md:28`). At 100 points the legal maximum is **11 models** (`List Building.md:46`), yet `Initiative & Activation.md:84` still says *"crews run from 4 to 14 models"* and `Terrain.md:133` still cites the 14-model horde as the terrain-swing benchmark. **The elite-vs-swarm balance case rests on a list that can no longer be fielded.** Resolve before any rescale.

**6. The entire settlement and campaign layer is uncosted — 25 structures, every upgrade tier, Groundworks, the founding budget, repair, and every resource number.**
> "The Goods budget and every build cost below are unpriced." — `Structures.md:150`
There are **zero** points or resource numbers in `Economy.md`, `Settlement.md`, `Infrastructure.md`, `Territory.md`, `Campaign.md`, `Factions.md`, `Progression.md` or `Components.md` (verified by grep — no matches for `pts` / `N points` / `Cost`).

**7. Several headline numbers are 1v1 and/or WND-3 and must not be generalised to crew play.**
The duel matrix (`sim_report.py:156-157`) runs **WND 1, no terrain, no cover, 1v1**, and its `attack()` function (`sim_report.py:119-128`) **never reads AGI or INT at all**. The skills marquee table (`skills_sim.py:99-103`) runs **WND 3, 1v1**. Section 5 below flags every such row explicitly.

**8. The 2051 arsenal is 62 named items, every one uncosted, and several are specified in mechanics the engine bans.**
`SETTING-TECH-2051.md` catalogues 62 pieces of kit across eight categories, each ending in a one-line `GAME HOOK`. **Not one carries a points cost, and none is mapped onto the existing class + characteristic system.** Worse, the hooks repeatedly reach for resolution currencies Settlements deliberately does not have — **saves** (`SETTING-TECH-2051.md:148, 154, 160, 178, 328`) against *"no separate save"* (`BLKOUT-RULES-ANALYSIS.md:137`), **ignore-cover** (`:40`) and **re-rolls** (`:346, :410`) against explicit bans (`BLKOUT-RULES-ANALYSIS.md:239`). The costing pass for this kit is scheduled **last** (`RULES-INTERVIEW-PLAN.md:161`).

**9. Nothing in the vault is Locked, and the rescale itself is unrecorded.**
> "**Nothing is 'Locked.'** Every rule is `Drafted`. **All balance numbers are sim-derived, never table-derived.**" — `RULES-COMPLETION-PLAN.md:21`
No note in the system has reached `Testing` or `Done` on the `Not Started → Designing → Drafted → Testing → Done` ladder (`Quick Reference — Writing Rules.md:40`). And **no document anywhere mentions a ×10 rescale, a 1000-point budget, or a "global atomic points system"** — every figure in the vault is on the 100-pt / 5-8-16-24 scale.

**10. A complete, working atomic points engine is already sitting in the project root — and nobody referenced it.**
`ff.py` (2,337 lines, untracked, modified 2026-07-27) is a full wargame costing engine from another system. Its `Weapon.calculate_cost` (`ff.py:135-290`) already solves the exact problem §4 of this audit describes: **non-linear stat lookups**, **multiplicative** terms for anything that scales output, **additive** terms for flat effects, **negative** costs for drawbacks, and **interaction terms** where a trait's price depends on the stat it is attached to. The numbers don't transfer; the architecture does. Full analysis in **§6C**.

---

## 2 · Master inventory

### 2.1 Stats

Six stats plus Wounds. Only five take points.

| Stat | Governs | Scale | Costed? | Evidence | Source |
|---|---|---|---|---|---|
| **WND** — Wounds | Hits before going down | **Fixed at 1** | Not buyable | HAND | `Unit Design.md:47-49`, `Damage.md:64` |
| **MOV** — Move | Inches per Move action | **Fixed at 6"** | Not buyable | HAND | `Unit Design.md:51-53`, `Skill Paths.md:30` |
| **STR** — Strength | Melee, force, breaching, hauling, barricades | −1…+6 | Free (rank-bundled) | HAND | `Unit Design.md:55-57` |
| **AGI** — Agility | Jumping, climbing, vaulting, balancing, dodging, escaping | −1…+6 | Free (rank-bundled) | HAND | `Unit Design.md:59-61` |
| **DEX** — Dexterity | Ranged, throwing, lockpicking, traps, delicate equipment | −1…+6 | Free (rank-bundled) | HAND | `Unit Design.md:63-65` |
| **INT** — Intelligence | Hacking, crafting, repair, medicine, searching, deploying | −1…+6 | Free (rank-bundled) | HAND | `Unit Design.md:67-69` |
| **NRV** — Nerve | Mental state under pressure, Stress | −1…+6 | Free (rank-bundled) | HAND | `Unit Design.md:71-73` |

**Scale and tiering** (`Unit Design.md:78-89`): −1 Impaired · 0 Civilian baseline · +1 Capable · **+2 Tier 1 Skilled** · +3 Trained · **+4 Tier 2 Veteran** · +5 Elite · **+6 Tier 3 Peak**. Max **+6** (`Unit Design.md:89`).

**Each +1 ≈ +10% on a core test, bounded 10–90%** — `Unit Design.md:76`, measured exactly at `Dice Mechanic — Sim Findings.md:16-25` (SIM).

**Are stats bought?** No. Stat points come free with rank, capped by tier so they must spread:

| Rank | Stat points | Tier caps | Skills granted |
|---|:--:|---|:--:|
| Recruit | 3 | none — no tiered stats | 0 |
| Fighter | 5 | up to 2× T1 | ~2 |
| Specialist | 7 | 1× T2 · 2× T1 | ~3 |
| Leader | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 |

Source: `Unit Design.md:101-106`. Rationale: *"pricing them again is double-counting"* (`List Building.md:22`) and *"you cannot price a stat fairly in a vacuum"* (`List Building.md:24`).

> **For the rebuild:** +5 and +6 read identically on an *unmodified* flat roll (both 90%, the natural-1 floor) — `Unit Design.md:89`, confirmed at `Dice Mechanic — Sim Findings.md:24-25`. The 6th point only earns its keep against cover, armour and opposed rolls. **Linear stat pricing is therefore provably wrong at the top of the ladder.**

### 2.2 Ranks

| Rank | Cost | Stat pts | Tier caps | Skills | Orders | Weapon gate | Evidence |
|---|:--:|:--:|---|:--:|:--:|---|---|
| **Recruit** | **5** | 3 | none | 0 | 0 | Unarmed · Light Melee · Sidearm · Thrown | GUESS |
| **Fighter** | **8** | 5 | 2× T1 | ~2 | 0 | + One-Handed Melee · Standard Ranged | GUESS |
| **Specialist** | **16** | 7 | 1× T2 · 2× T1 | ~3 | 1 | + Heavy Melee · Heavy Ranged | GUESS |
| **Leader** | **24** | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 | 2 | everything | GUESS |

Costs: `List Building.md:36-39` · `Unit Design.md:103-106`. Weapon gate: `Weapons.md:45-50`.

Explicitly provisional:
> "**Costs are provisional — a re-cost is owed.** The **5 / 8 / 16 / 24** fielding costs are inherited from the old, thinner stat line… expect the ladder to move **up**." — `Unit Design.md:121-122`

Partial sim support (SIM, but see §5 caveats):
> "The rank ladder holds… Recruit-at-5 and Fighter-at-8 are priced correctly against one another." — `Crew Sim — Findings.md:70`

Structural identity to preserve: **a Specialist costs exactly two Fighters** (16 = 2×8) — *"the central trade of the system"* (`List Building.md:41`).

**Budget:** Standard **100** points; 75 = raid; 150 = pitched — `List Building.md:29`. Also printed player-facing at `playtest-kit\reference-tables.html:43`.

### 2.3 Skills — 150 of them, all free

The task brief estimated "~40+". The actual catalogue is **exactly 150**: 5 paths × 3 tiers × 10 skills. Verified by enumeration of `Skill Paths.md:52-235`. `Skill Sim — Findings.md:11` independently states "~150 skills".

| Path | Stat | Covers | T1 | T2 | T3 | Source |
|---|---|---|:--:|:--:|:--:|---|
| Combat / Muscle | STR | melee, force, grappling, breaking, hauling | 10 | 10 | 10 | `Skill Paths.md:52-87` |
| Shooting / Perception | DEX | ranged, aim, spotting, trick shots | 10 | 10 | 10 | `Skill Paths.md:89-124` |
| Movement / Acrobatics | AGI | climbing, dodging, repositioning, escaping | 10 | 10 | 10 | `Skill Paths.md:126-161` |
| Expertise / Knowledge | INT | hacking, traps, medicine, tech, terrain | 10 | 10 | 10 | `Skill Paths.md:163-198` |
| Bravery / Morale | NRV | rallying, resisting fear, reckless aggression | 10 | 10 | 10 | `Skill Paths.md:200-235` |

**Cost: zero, all 150.**
> "Each skill fills **one tier-slot** off its stat's path — you don't pay for it separately; **the stat reaching the tier *is* the payment**." — `Skill Paths.md:41`

Skills ride the stat line: a stat at +4 grants its T1 **and** T2 skill; at +6, T1 + T2 + T3 — `Skill Paths.md:14`, `Unit Design.md:112`. There are **no prerequisites** (`Skill Paths.md:41`).

**Skills that break otherwise-global constraints — the highest-priority costing targets:**

| Skill | Path/Tier | What it breaks | Source |
|---|---|---|---|
| **Tough** | STR T3 | +1 WND — "a named exception to the normal fixed WND value" | `Skill Paths.md:78` |
| **Fleet** | AGI T2 | MOV 8" not 6" — "a named exception to the normal fixed MOV value" | `Skill Paths.md:145` |
| **Quick Shot** | DEX T3 | Two attacks — "overrides the one-attack limit" class | `Skill Paths.md:116` |
| **Dual Wield** | AGI T3 | Two attacks — "This overrides the one-attack limit" | `Skill Paths.md:153` |
| **Gunslinger** | DEX T3 | Two attacks at two targets | `Skill Paths.md:117` |
| **Double Dash** | AGI T2 | Sprint costs one slot, not both — rewrites the action economy | `Skill Paths.md:144` |
| **Iron Will** | NRV T3 | Auto-pass one Break test per game | `Skill Paths.md:226` |

`Tough` and `Fleet` are the **only** levers on the two "fixed" stats in the entire game, and both are free.

**Three skills are already flagged as out-competed by a weapon characteristic** — a live costing contradiction between the free layer and the paid layer:
- **Long Barrel** (T1 DEX, +5" if you don't Move) vs **Long Range** (6 pts, +6" unconditional). *"The skill is dead and wants a rewrite."* — `Weapons.md:188`
- **Knockback** (T1 STR) vs **Heavy Impact** (3 pts) — *"Distinct enough to keep both — but watch them."* — `Weapons.md:189`
- **Ghost Blade** (T3 AGI) vs **Balanced** (2 pts) — *"Distinct, but the margin is thin."* — `Weapons.md:190`

### 2.4 Weapons — the atomic system that already works

#### Classes (`Weapons.md:24-33`) — SIM-validated, mirrored exactly in `weapon_sim.py:29-38`

| Class | Cost | Damage | Range | Hands | Min rank | Slots | Always has |
|---|:--:|:--:|:--:|:--:|---|:--:|---|
| Unarmed | 0 | +0 | melee | — | Any | 0 | — |
| Light Melee | 0 | +1 | melee | 1 | Recruit | 2 | free basic loadout |
| One-Handed Melee | 4 | +2 | melee | 1 | Fighter | 2 | — |
| Heavy Melee | 8 | +3 | melee | 2 | Specialist | 3 | Two-Handed |
| Thrown | 2 | +1 | 6" | 1 | Any | 2 | Limited (one use) |
| Sidearm | 4 | +2 | 8" | 1 | Recruit | 2 | Sidearm, Loud |
| Standard Ranged | 10 | +3 | 18" | 2 | Fighter | 3 | Two-Handed, Loud |
| Heavy Ranged | 14 | +3 | 24" | 2 | Specialist | 4 | Two-Handed, Loud, Cumbersome (−1 MOV) |

#### Characteristics — 24 of them, each takes one slot

| Characteristic | Cost | Effect | Restriction | Source |
|---|:--:|---|---|---|
| Brutal | 4 | +1 Damage (max +4) | Melee only, or ranged **with** Short Range | `Weapons.md:59` |
| Armour Piercing | 4 | Target's Armor −1 on Injury | — | `Weapons.md:60` |
| Accurate | 3 | +1 hit if you did not Move/Sprint/Climb | — | `Weapons.md:65` |
| Spread | 3 | +1 hit at ≤half range, −1 beyond | Ranged only | `Weapons.md:66` |
| Concussive | 3 | Payload: Off-Balance | — | `Weapons.md:75` |
| Crippling | 3 | Payload: Hobbled | — | `Weapons.md:76` |
| Blinding | 3 | Payload: Blind | — | `Weapons.md:77` |
| Shocking | 3 | Payload: Shocked | — | `Weapons.md:78` |
| Toxic | 3 | Payload: Poison | — | `Weapons.md:79` |
| Incendiary | 3 | Payload: Fire | — | `Weapons.md:80` |
| **Bleeding** | **4** | Payload: Bleed — *"at WND 1 this is a two-round death clock… The deadliest payload; priced for it."* | — | `Weapons.md:81` |
| Heavy Impact | 3 | Push target 2" away | — | `Weapons.md:82` |
| Hook | 2 | Pull target 1" toward you | Melee only | `Weapons.md:83` |
| Suppressive | 4 | Target may not clear the Pin with its Move | Ranged only | `Weapons.md:84` |
| Blast | 4 | Resolve against every model within 2" | Thrown / Heavy Ranged only | `Weapons.md:89` |
| Smoke | 3 | Place a 3" Dense Smoke instead of attacking | Thrown only | `Weapons.md:90` |
| Long Range | 6 | +6" range, to the 24" ceiling | Ranged only | `Weapons.md:95` |
| Balanced | 2 | AGI instead of STR for melee | Light / One-Handed Melee only | `Weapons.md:96` |
| Defensive | 3 | +1 on opposed melee when not attacker and did not Move | Melee only | `Weapons.md:97` |
| Cleaving | 5 | On a melee win, Injury vs every Engaged enemy | Heavy Melee only | `Weapons.md:98` |
| Breaching | 3 | +2 on STR tests vs Breachable terrain | — | `Weapons.md:99` |
| Concealable | 2 | May start Hidden / be smuggled | — | `Weapons.md:100` |
| Quiet | 2 | No reveal from Hidden, no noise/alarms | — | `Weapons.md:101` |
| Compact | 2 | Counts as one-handed | Heavy classes only | `Weapons.md:102` |

All 24 costs are mirrored verbatim in `weapon_sim.py:41-45`. Evidence: **SIM** (structurally validated), **HAND** (the specific numbers were set by the designer, not solved for).

#### Drawbacks — refund points, take no slot, **max 2 per weapon** (`Weapons.md:104`)

| Drawback | Refund | Effect | Restriction | Source |
|---|:--:|---|---|---|
| Short Range | −3 | Halve max range | Ranged only | `Weapons.md:109` |
| Slow | −3 | May not Charge | **Melee only** | `Weapons.md:110` |
| Unstable | −2 | Natural 1 to hit destroys the weapon | — | `Weapons.md:111` |
| Cumbersome | −2 | −1 MOV while carried | — | `Weapons.md:112` |
| Limited | −3 | One use per battle | — | `Weapons.md:113` |

Machine-enforced at `weapon_sim.py:46-50, 69-73`. The governing rule, and the reason `Awkward` was cut:
> "**A drawback must bite no matter how you play.** … A drawback you can dodge by how you play is just a discount." — `Weapons.md:115-120`

#### Sample armoury — all 16 verified arithmetically correct

I recomputed every entry against the atomic tables. **16 of 16 reconcile exactly**, and all satisfy their slot limits and range maths.

| Weapon | Build | Quoted | Recomputed | ✓ |
|---|---|:--:|:--:|:--:|
| Baseball Bat | Light Melee | 0 | 0 | ✓ |
| Kitchen Knife | Light Melee + Balanced + Concealable | 4 | 0+2+2 | ✓ |
| Crowbar | One-Handed + Breaching | 7 | 4+3 | ✓ |
| Great Axe | Heavy Melee | 8 | 8 | ✓ |
| Sledgehammer | Heavy Melee + Heavy Impact + Breaching | 14 | 8+3+3 | ✓ |
| Fire Axe | Heavy Melee + Brutal + Bleeding | 16 | 8+4+4 | ✓ |
| Reaping Hook | Heavy Melee + Cleaving + Defensive | 16 | 8+5+3 | ✓ |
| Pistol | Sidearm | 4 | 4 | ✓ |
| Pipe Shotgun | Std Ranged + Brutal + Spread − Short Range − Unstable | 12 | 10+4+3−3−2 | ✓ |
| Assault Rifle | Std Ranged + Accurate | 13 | 10+3 | ✓ |
| Nailgun | Std Ranged + Bleeding | 14 | 10+4 | ✓ |
| Grandpa's Hunting Rifle | Std Ranged + Accurate + Long Range | 19 | 10+3+6 | ✓ |
| Squad Machine Gun | Heavy Ranged + Suppressive + AP | 22 | 14+4+4 | ✓ |
| Makeshift Flamethrower | Heavy Ranged + Incendiary + Blast − Short Range − Limited | 15 | 14+3+4−3−3 | ✓ |
| Molotov | Thrown + Incendiary + Blast | 9 | 2+3+4 | ✓ |
| Smoke Grenade | Thrown + Smoke | 5 | 2+3 | ✓ |

Source table: `Weapons.md:150-167`. Ranges also check out: Grandpa's = 18+6 = **24"** (at ceiling); Pipe Shotgun = 18÷2 = **9"**; Flamethrower = 24÷2 = **12"**.

**This is the single strongest asset going into the rebuild.** A 24-characteristic additive system with restriction gates, drawback refunds and slot limits already produces 16 internally consistent, distinct weapons.

#### Cut characteristics — kept so they don't creep back (`Weapons.md:173-182`)

Rapid · Precision · Reliable · Quick Draw · Crushing · Awkward · Intimidating (**parked**, not rejected) · Area Effect (merged into Blast). Each with a stated reason. **Rapid** is the most important: *"Selling it to a Fighter for 4 points destroys the entire skill economy"* — `Weapons.md:175`.

### 2.5 Armour and equipment

| Armour | Injury | Drawback | Cost | Evidence |
|---|:--:|---|:--:|---|
| None | 0 | — | **0** | HAND |
| Thick clothing | 0 | ignore the first Environmental Stress once per game | **0** | HAND |
| Improvised | −1 | −1 AGI | **3** | HAND |
| Light | −1 | — | **6** | HAND |
| Heavy | −2 | −1 MOV, −1 AGI, counts as Loud | **10** | HAND |

Source: `Weapons.md:126-132`. Also at `List Building.md:60-65` (**divergent — see §6.1**) and `playtest-kit\reference-tables.html:147-150`. Mirrored in `crew_sim.py:58`, `weapon_sim.py:96`, `engine2d\data.py:58-63`.

| Equipment | Effect | Cost | Evidence | Source |
|---|---|:--:|---|---|
| Med-Kit | Cancels the −2 on Stabilize / treating Bleed & Poison | **4** | HAND | `List Building.md:69` |
| Breach Kit | +1 to the hack test | **4** | HAND | `List Building.md:70`, `Weapons.md:141` |
| Exploit Suite | +2 to the hack test | **8** | HAND | `List Building.md:72`, `Weapons.md:142` |
| Deployable | see §2.6 | "4–14" *(wrong — see §6.2)* | — | `List Building.md:71` |

Hacking gear ladder (`Weapons.md:138-142`): Bare-handed +0 (0) · Breach Kit +1 (4) · Exploit Suite +2 (8). **Note the implied price of a flat +1 to one test type is 4 points; a +2 is 8.** That is the only explicit "modifier → points" exchange rate anywhere in the game, and it is linear. Its own note concedes the ladder is unset:
> "**Hack-modifier ladder** — set the gear/skill +/− values once first playtests show how reliable an unmodified hack feels." — `Hacking.md:116`

**Carry limits** (`List Building.md:55`): one armour · two hands (Two-Handed takes both) · up to **two** pieces of equipment. **Free to every fighter** (`List Building.md:54`): fists, one Light Melee weapon, thick clothing.

### 2.6 Deployables — 4 families, 20 costable items

All costs from `Deployables.md`. Evidence: **GUESS** by the note's own admission —
> "Costs are **first-pass**, anchored to [the armoury] (Trap 4 · Med-Kit 4 · Molotov 9 · Assault Rifle 13) and checked against [[Deployables Sim — Findings]]. **Validate at the table**." — `Deployables.md:158`

**Family A · Turrets** — standing hardware, both equipment slots (`Deployables.md:91-97`)

| Turret | Build | Cost | Range | Profile |
|---|:--:|:--:|:--:|---|
| Autoturret | Complex −1 | **12** | 18" | 1 shot/rd, Damage +3 |
| Sniper Turret | Intricate −2 | **15** | 24" | 1 shot/rd, +3, **+1 to hit** |
| Burst Turret | Intricate −2 | **18** | 18" | **2 shots**/rd at +2 each |
| Blast Turret | Complex −1 | **14** | 12" | 1 shot/rd, +3, Blast 2" |
| Reinforced Turret | Complex −1 | **15** | 18" | 1 shot/rd, +3, always Heavy cover |

Burst was **repriced 16 → 18** by the sim (`Deployables Sim — Findings.md:11, 34`) — the only points change in the game ever made *by* a simulation.

**Family B · Mines** — chassis + payload (`Deployables.md:104-117`)

| Chassis | Cost | | Payload | Cost |
|---|:--:|---|---|:--:|
| Proximity | **5** | | Explosion | **+4** |
| Remote | **7** | | Fire | **+3** |
| Seeker | **8** | | Poison | **+3** |
| | | | Shock | **+3** |
| | | | Smoke | **+2** |

Range 7–12. All four quoted example builds verified correct (`Deployables.md:119`; machine-checked at `deployables_sim.py:73-79`).

**Family C · Traps** (`Deployables.md:124-130`): Trip Wire **3** · Spike Strip **4** · Covered Pit **5** · Leg Clamp **5** · Razor Barrier **4**.

**Family D · Beacons** — 6" aura, both equipment slots (`Deployables.md:139-147`): Munitions **8** · Targeting **8** · Aegis **8** · Cover **6** · Cleansing **8** · Revive **12** · Dread **7**.

**Build rating** — an intrinsic modifier on the deploy INT test (`Deployables.md:66-71`): Simple **+1** · Standard **0** · Complex **−1** · Intricate **−2**. **This is currently free** — it is not priced, it is a balancing gate. Under atomic costing it becomes a candidate for a discount/surcharge.

**Actual catalogue range: 3 (Trip Wire) to 18 (Burst Turret).** `List Building.md:71` says "4–14". See §6.2.

### 2.7 Settlement structures — 25 entries, **all unpriced**

> "The Goods budget and every build cost below are **unpriced**. Set them with [[Economy]]." — `Structures.md:150`

Every one of the 25 is **UNCOSTED**. They have a *floor-space* cost and a *Power* draw, but no Goods/Materials/points price.

| # | Structure | Category | Class | Size | Pwr | Points/resource cost |
|:--:|---|---|---|---|:--:|---|
| 1 | Water Reclaimer ★ | Sustain | Plant | 3×3 | −1 | **UNCOSTED** |
| 2 | Cistern | Sustain | Plant | 3×3 | 0 | **UNCOSTED** |
| 3 | Generator ★ | Sustain | Plant | 3×3 | **+3** | **UNCOSTED** |
| 4 | Bunkhouse | Sustain | Building | 6×9 | 0 | **UNCOSTED** |
| 5 | Storehouse | Sustain | Building | 6×6 | 0 | **UNCOSTED** |
| 6 | Equipment Shed | Sustain | Station | 3×2 | 0 | **UNCOSTED** |
| 7 | Processor ★ | Convert | Plant | 3×5 | −1 | **UNCOSTED** |
| 8 | Salvage Yard ★ | Convert | Yard | 5×7 | 0 | **UNCOSTED** |
| 9 | Trader's Kiosk | Convert | Station | 3×2 | 0 | **UNCOSTED** |
| 10 | Workbench | Convert | Station | 3×2 | 0 | **UNCOSTED** |
| 11 | Fabricator | Convert | Building | 6×6→6×10 | −2/−3 | **UNCOSTED** |
| 12 | HQ ★ | Operate | Building | 6×6 | −1 | **UNCOSTED** |
| 13 | Vault | Operate | Plant | 3×3 | −1 | **UNCOSTED** |
| 14 | Scout Post | Operate | Plant | 3×3 | 0 | **UNCOSTED** |
| 15 | Comms Mast | Operate | Plant | 3×3 | −1 | **UNCOSTED** |
| 16 | Server Core | Operate | Building | 6×6 | −2 | **UNCOSTED** |
| 17 | Drone Bay | Operate | Building | 6×8 | −2 | **UNCOSTED** |
| 18 | Med-bay | Recover | Building | 6×6 | −1 | **UNCOSTED** (`+X` on Fate roll also unset) |
| 19 | Holding Cells | Recover | Building | 6×6 | −1 | **UNCOSTED** |
| 20 | Mess Hall | Recover | Building | 6×8 | −1 | **UNCOSTED** (Stress value also unset) |
| 21 | Perimeter Wall | Defend | Line | 1"×6" seg | 0 | **UNCOSTED** |
| 22 | Gatehouse | Defend | Building | 6×6 | −1 | **UNCOSTED** |
| 23 | Watchtower | Defend | Plant | 3×3 | 0 | **UNCOSTED** |
| 24 | Turret Mount | Defend | Plant | 2×2 | −2 | **UNCOSTED** |
| 25 | EW Mast | Defend | Plant | 3×3 | −2 | **UNCOSTED** |

Source: `Structures.md:252-341`. Category counts (Sustain 6 · Convert 5 · Operate 6 · Recover 3 · Defend 5 = 25) at `Structures.md:347`.

**Upgrade ladders — also all unpriced** (`Structures.md:230-239`):

| T1 | T2 | T3 | Space |
|---|---|---|---|
| Equipment Shed 3×2 | Armory 6×6 | — | 6 → 36 |
| Water Reclaimer 3×3 | Water Tower 3×5 | — | 9 → 15 |
| Workbench 3×2 | Workshop 6×8 | — | 6 → 48 |
| Trader's Kiosk 3×2 | Trade House 6×6 | — | 6 → 36 |
| Fabricator 6×6 | Robotics Workshop 6×8 | Advanced Weapons Lab 6×10 | 36 → 48 → 60 |
| HQ 6×6 | HQ II | HQ III | dispatch + storage; gates the Vault |
| Med-bay 6×6 | Med-bay II | — | scar healing at T2 |
| Storehouse 6×6 | Storehouse II | — | capacity, not footprint |

**Groundworks** (a project, not a catalogue entry) — also uncosted: Base 12"×36" (432 sq) → Groundworks I 18"×36" (648) → Groundworks II 18"×48" (864). `Structures.md:78-83`.

**The critical rule the points system must respect:**
> "**Ownership buys availability, never free board power.** Built structures grant **auto-deploy**… the piece itself **still costs crew-points** and still sits inside the **9–12** density band. **A bigger settlement never means a bigger army.**" — `Structures.md:49`, repeated at `Deployables.md:61`, `Structures.md:344`, `Terrain Interaction.md:137`

### 2.8 Infrastructure — 12 board features, all uncosted (and correctly so)

`Infrastructure.md:118-129` catalogues twelve operable features: **Cargo Crane** (`:118`) · **Blast Door** (`:119`) · **Roller/Security Gate** (`:120`) · **Retractable Bridge** (`:121`) · **Elevator/Cargo Lift** (`:122`) · **Conveyor Belt** (`:123`) · **Window Shutters** (`:124`) · **Floodlights** (`:125`) · **Flood Gates** (`:126`) · **HVAC/Gas Vent** (`:127`) · **Trash Compactor/Crusher** (`:128`) · **Power Generator/Junction** (`:129`). Plus a custom-battle building menu (`Infrastructure.md:139-145`).

**None has a points cost, and none should** — infrastructure is board scenery placed under the density band, not bought. The firewall is explicit:
> "**Infrastructure changes the board — it does not exist to damage models.**" — `Infrastructure.md:35`
> "**If it only exists to hurt people, it's a Deployable, not infrastructure.**" — `Infrastructure.md:167`

A sub-cap ties it to the density band: *"guideline **one Infrastructure Feature per building**"* (`Infrastructure.md:137`), *"put infrastructure on **roughly half** of the eligible buildings"* (`Infrastructure.md:148`).

### 2.9 The 2051 arsenal — 62 named items, **every one uncosted**

`SETTING-TECH-2051.md` is compiled setting research (`:12` — *"Compiled 2026-07 from real-world programme reporting"*), where each entry ends in a one-line `GAME HOOK` sketching a mechanic. **No entry carries a points cost. No entry is mapped onto the class + characteristic system.** The mapping is scheduled for Interview 15 (`RULES-INTERVIEW-PLAN.md:146-152`) and the costing for Interview 16, the last (`RULES-INTERVIEW-PLAN.md:161`).

| Category | Count | Line range | Named items |
|---|:--:|---|---|
| **Infantry small arms & kinetics** | 6 | `:16-52` | XM7/XM250 NGSW rifle (`:18`) · 6.8×51mm hybrid-case ammo (`:24`) · XM157 fire-control optic (`:30`) · guided small-arms rounds, EXACTO-class (`:36`) · cased-telescoped/caseless ammo (`:42`) · lightweight weapon materials (`:48`) |
| **Soldier systems** | 5 | `:56-86` | IVAS / Anduril EagleEye AR HUD (`:58`) · networked squad vision (`:64`) · **powered exoskeletons & exosuits** (`:70`) · health-monitoring wearables (`:76`) · adaptive/active camouflage (`:82`) |
| **Directed-energy** | 8 | `:90-138` | DE M-SHORAD "Guardian" 50 kW (`:92`) · Army Guardian / HELWS (`:98`) · UK DragonFire (`:104`) · Iron Beam / Light Shield (`:110`) · LOCUST / P-HEL / AMP-HEL squad lasers (`:116`) · **THOR** HPM (`:122`) · **Leonidas** counter-swarm HPM (`:128`) · counter-drone DE premise (`:134`) |
| **Active protection & base defence** | 6 | `:142-178` | Trophy APS (`:144`) · Iron Fist light APS (`:150`) · Iron Curtain / top-attack APS (`:156`) · ROSY multispectral obscurants (`:162`) · Centurion C-RAM (`:168`) · ERA / adaptive / electric armour (`:174`) |
| **Drones & counter-drone** | 10 | `:182-242` | Black Hornet 4 nano recon (`:184`) · Switchblade 300/600 (`:190`) · ZALA Lancet (`:196`) · one-way FPV / fibre-optic drones (`:202`) · **autonomous swarms** (`:208`) · DoD Replicator mass-attritable autonomy (`:214`) · Anduril Roadrunner-M (`:220`) · Anduril Anvil/Anvil-M (`:226`) · Anduril Bolt/Bolt-M (`:232`) · C-UAS counter-swarm stack (`:238`) |
| **Ground robotics** | 5 | `:246-276` | RCV / Textron Ripsaw M3 (`:248`) · Ghost Robotics Vision 60 / SPUR quadruped (`:254`) · XM30 optionally-manned IFV (`:260`) · Milrem Type-X / THeMIS (`:266`) · S-MET resupply mule (`:272`) |
| **EW, cyber & comms** | 6 | `:282-318` | GNSS jamming/spoofing (`:284`) · electronic-attack systems TLS-BCT/Krasukha (`:290`) · MANET mesh networks (`:296`) · AI tactical cyber (`:302`) · assured PNT (`:308`) · LPI/LPD counter-EW (`:314`) |
| **Sensing / AR optics** | 5 | `:322-352` | multispectral/hyperspectral targeting (`:324`) · through-wall radar, Xaver (`:330`) · unattended ground sensor networks (`:336`) · AI target recognition, Project Maven (`:342`) · acoustic gunshot detection (`:348`) |
| **Power, logistics & autonomy** | 11 | `:356-422` | Project Pele microreactor (`:358`) · ANPI/Janus fixed reactors (`:364`) · tactical microgrids (`:370`) · conformal wearable battery (`:376`) · autonomous ground resupply (`:382`) · DARPA RACER autonomy stack (`:388`) · TRUAS/TRV150 resupply drone (`:394`) · SPEE3D expeditionary 3D printing (`:400`) · Palantir Maven / CJADC2 C2 aid (`:406`) · SFC Jenny silent fuel cell (`:412`) · DEW power/cooling packs (`:418`) |
| **TOTAL** | **62** | | |

**New game objects the hooks propose that do not exist today** (each needs its own cost *and* its own rules):

| Proposed object | Hook | Collides with |
|---|---|---|
| **Heat / cooldown track** on lasers | `:96` | lightweight bookkeeping (`Out of Scope.md:41`) |
| **Capacitor charge** — shots/turn gate | `:422` | as above |
| **Per-model "power budget"** that drains and downgrades stats | `:380` | *"Every new status token or mid-activation subsystem is a tax"* (`BLKOUT-RULES-ANALYSIS.md:408`) |
| **Weight-per-clip / ammo economy + resupply token** | `:28` | *"No hit-location tables, ammo-counting, or encumbrance spreadsheets"* (`Out of Scope.md:41`) |
| **"Signature" stat** with visual + thermal channels | `:86` | a sixth stat; sensor-vs-camo rock-paper-scissors |
| **Weapon "weight class" modifier** | `:52` | a new weapon axis alongside class/characteristics |
| **AI-targeting token pool** (spend to re-roll) | `:346` | re-rolls are banned (`Weapons.md:177`) |
| **Intercept saves** (APS ×3, ERA, electric armour) | `:148, :154, :160, :178` | *"no separate save"* (`BLKOUT-RULES-ANALYSIS.md:137`) |
| **Control / authorisation resource** for autonomous fire | `:258` | a new resource |
| **Exo-rig trooper type** | `:74` | a unit, not gear — needs a rank/profile |
| **Faction-level cost discount** for expendable units | `:218` | the only *discount* mechanic proposed anywhere |

**Five faction archetypes sketched in the same doc** (`:426-445`), all uncosted, all with explicit price-band claims: The Remnant — *"the **fewest, most expensive models**"* (`:430`) · The Scavengers — *"**Cheap, numerous**"* (`:433`) · The Swarm — *"buy expendable autonomous drones by the crate"* (`:436`) · The Ghosts — *"Small, elite, **force-multiplier list**"* (`:439`) · The Foundry — *"**no crew-morale penalties** … rebuilds losses mid-campaign"* (`:442`). Tuning intent: *"a rough **rock-paper-scissors** … That triangle is the tuning surface"* (`:445`).

⚠ **These are a different five from the vault's** (`Factions.md:34-52`: Civilians · First Enforcers · Laborers · Lost Batallion · The HACKERS). See §6.13.

### 2.10 Everything else undrafted but planned

| Item | Status | Source |
|---|---|---|
| **Vehicles** | Ledger card, `status: parking-lot`, v0.0, *"No rule text yet"* | `Rules Ledger\adv-001 Vehicles.md:5, :16` |
| **Drones** | Ledger card, parking-lot, no text | `Rules Ledger\adv-002 Drones.md:5, :16` |
| **Civilians / non-combatants** | Ledger card, parking-lot, no text; tied to the Escort caravan | `Rules Ledger\adv-003…:5, :16`; `Scenarios.md:159` |
| **Weather / climate** | Ledger card, parking-lot, no text | `Rules Ledger\adv-004…:5, :16` |
| **Campaign rules** | Ledger card, parking-lot, no text | `Rules Ledger\adv-005…:5, :16` |
| **Factions** (vault's five) | `status: Not Started`; *"Factions are **planned but not yet designed**"* | `Factions.md:5, :29, :34-52` |
| **Balance** (the costing-formula note itself) | `status: Not Started`; *"Not drafted yet."* | `Balance.md:5, :29` |
| **Economy** — every resource rate | `status: Not Started`; *"Not drafted yet."* | `Economy.md:5, :29` |
| **Territory · Downtime · Events · Narrative · Diplomacy · Solo & Co-op** | all `status: Not Started`, all undrafted | `Territory.md:5` · `Downtime.md:5` · `Events.md:5` · `Narrative.md:5` · `Diplomacy.md:5` · `Solo & Co-op.md:5` |
| **Components · Rulebook · Edge Cases · Playtesting** | all `status: Not Started` | `Components.md:5` · `Rulebook.md:5` · `Edge Cases.md:5` · `Playtesting.md:5` |
| **10 starting locations**, one boost each | Named but undrafted; *"we need to lock these in"* | `Settlement.md:42-44`; `RULES-INTERVIEW-PLAN.md:5, :27-29` |
| **Advance award rates** | Unticked | `Rules System — Master Roadmap.md:279` |
| **Scar effect tables** | Unticked; Fate spread is *"a first-draft"* | `Rules System — Master Roadmap.md:280`; `Campaign.md:53` |
| **Bottle → withdrawal roster-save "with a price"** | Price undefined | `Morale.md:102-103`; `Interviews — Completing the Rules System.md:155` |
| **Glorious Deed** — name, qualification and resource value | *"placeholder name"* | `Core Game Format.md:57` |
| **Doctrine layer** (8 archetypes) | Pulled from the battle rules to the campaign layer | `Rules System — Master Roadmap.md:200`; `RULES-AUDIT.md:5, :43` |
| **Forced movement** as a universal rule | Currently skill-owned | `Rules System — Master Roadmap.md:111` |
| **Psychic abilities / Mental stat; 50mm "beasts"** | Flagged ⚠ as an unresolved scope boundary | `Out of Scope — What Settlements is NOT.md:20` |
| **Deeper hacking (Program / Firewall)** | **Parked**; *"In v1 **neither is a stat**"* | `Hacking.md:123-136` |
| **Recruiting Board** | Cut — *"blocked on hiring rules that don't exist yet"* | `Structures.md:42` |
| **Hiring rules / Cash hire-price per rank** | Do not exist; open question unanswered | `Structures.md:376`; `Interviews….md:78-79` |

---

## 3 · Constraints register

Every hard ceiling, floor, band and locked rule a points system must respect, with the reason it is load-bearing.

| # | Constraint | Value | Source | Why it is load-bearing |
|:--:|---|---|---|---|
| C1 | **Damage ceiling** | **+4**, and only Brutal reaches it; base classes stop at +3 | `Weapons.md:38` | "Armour only runs to −2; if weapons ran past +4 **the armour ladder would be decorative**." The whole armour economy collapses above it. |
| C2 | **Armour floor** | **−2** (Heavy) | `Weapons.md:132` | The mirror of C1. Measured: heavy weapon +3 vs heavy armour −2 is "almost exactly cancelled" (`Dice Mechanic — Sim Findings.md:49-55`). |
| C3 | **Range ceiling** | **24"** | `Weapons.md:40` | Deployment zones sit 24" apart, so 24" = "fire from your own deployment zone on turn one". **A threshold, not a curve — no points cost can balance it.** |
| C4 | **Deployment distance** | 6" from opposite board edges on a 3'×3' = **24" apart** | `Core Game Format.md:35`, `Core Game Format.md:33` | The physical origin of C3. Changing the board changes the weapon ceiling. |
| C5 | **Global modifier cap** | **±3** on any roll | `Skill Paths.md:47`, `Hacking.md:71,105`, `Deployables.md:38,64,136`, `Out of Scope.md:39` | Prevents modifier stacking. Means the marginal value of the 4th +1 is **zero** — fatally non-linear for additive pricing. |
| C6 | **Cover is a separate axis from the ±3 cap** | Cover counted separately | `Terrain Hacking Cover — Sim Findings.md:65` | Ruled deliberately: under a shared cap "Shaken does NOTHING vs a Hidden target" (20% vs 30%). Implemented at `weapon_sim.py:11,120-127,200`. |
| C7 | **WND fixed at 1** | Every unit | `Damage.md:64`, `Unit Design.md:76` | Kills heroes without an anti-hero cap: *"a 40-point Leader in plate dies to one lucky pistol shot"* (`List Building.md:51`). It also caps how much any defensive investment can be worth. |
| C8 | **MOV fixed at 6"** | Every unit | `Unit Design.md:76`, `Skill Paths.md:30` | Raised only by the **Fleet** skill. |
| C9 | **Stat maximum +6** | Campaign cap = +6 (T3) | `Unit Design.md:89`, `Progression.md:37` | "keeps the clean 2-point tier cadence". +5 and +6 are identical on a flat roll. |
| C10 | **Terrain density band 9–12** | Large features on a 3'×3' | `Terrain.md:110, 122` | **The single most important balance constraint in the game.** Density is chosen *after* lists are locked, so it must be closed: "'Nine minimum, as crowded as you like' hands the game to whoever pushes the dial" (`Terrain.md:135`). |
| C11 | **The pyramid** | Exactly 1 Leader · every Specialist needs 2 lower-rank · every Recruit needs a Fighter+ · minimum 4 fighters | `List Building.md:44` | The **only** structural composition rule. It, plus the budget, replaces a unit cap. Encoded at `weapon_tests.py:22-32`. |
| C12 | **No unit cap** | None per battle | `List Building.md:46` | The pyramid + budget do the work. At 100 pts the legal max is **11 models** (Leader + 5 Fighters + 5 Recruits = 89 pts, ~11 pts of gear) — verified arithmetically. |
| C13 | **Roster cap ≠ fielding cap** | Base **10** body slots from the HQ, raised by Bunkhouses; every head consumes Water | `List Building.md:49` | "**Goods/Materials buy what you own, points gate what you field.**" Two orthogonal economies — the atomic system governs only one. |
| C14 | **Campaign: +2 per Advance, −2 per scar** | On a fighter's cost | `List Building.md:77` | "the anti-snowball valve: **veterans crowd out rookies**". A ×10 rescale makes this ±20; whether the *ratio* should hold is an open question. |
| C15 | **Advances never raise WND or MOV** | Only specific skills do | `Progression.md:38` | Protects C7 and C8 from campaign drift. |
| C16 | **Carry limits** | one armour · two hands · **two** equipment | `List Building.md:55` | The hard brake on gear-stacking. Standing hardware (turrets, beacons) eats **both** equipment slots (`Deployables.md:85, 133`). |
| C17 | **Max 2 drawbacks per weapon** | Enforced | `Weapons.md:104`, `weapon_sim.py:61` | Stops refund-farming. |
| C18 | **Slot limits per weapon class** | 0/2/2/3/2/2/3/4 | `Weapons.md:24-33`, `weapon_sim.py:60` | Caps characteristic stacking per weapon independently of cost. |
| C19 | **Rank gates weapon class** | Recruit → Leader ladder | `Weapons.md:45-50` | "a Recruit physically cannot hold a rifle" — a hard gate, not a price. |
| C20 | **One attack per activation** | Unless a skill says otherwise | `Skill Paths.md:49` | The action-economy floor. Broken only by Quick Shot / Dual Wield / Gunslinger. |
| C21 | **Beacon auras: no self-stacking, max 2 per model** | | `Deployables.md:136-137` | "the brake on a death-star stack". Directly non-linear (see §4). |
| C22 | **A hit does exactly one thing** | It wounds, **or** it delivers its payload — never both | `Weapons.md:13`, `Damage.md:44`, `Deployables.md:38` | Why payload characteristics can be priced flat: they only fire on the non-wounding branch. |
| C23 | **Difficulty is a modifier, never a raised target** | −1/−2/−3 within the cap; no 9+/11+ targets | `Skill Paths.md:48` | Keeps everything on one curve, which is what makes +1 ≈ +10% universally true. |
| C24 | **One dice mechanic, no re-rolls** | | `Weapons.md:177` | "Reliable *(re-roll)* introduces re-rolls, a dice mechanic that exists nowhere in Settlements. **Breaks the one-mechanic ceiling.**" |
| C25 | **Settlement canvas** | 12"×36" (432 sq"); catalogue would need ~651 sq"; ~300 usable | `Structures.md:56, 222` | Space, not points, is the settlement limiter. "**Scarcity produces divergence; tech trees produce convergence**" (`Structures.md:211`). |
| C26 | **No build prerequisites** | Nothing is chained | `Structures.md:41, 208-209` | Cost + floor space are the only gates. |
| C27 | **Structures are binary** | Functional or Disabled — no HP, no collapse tracking | `Structures.md:50` | A bookkeeping limit that constrains what a structure cost can buy. |
| C28 | **Power balance** | Generator **+3**; the five starters draw exactly 3 | `Structures.md:154-156` | "You begin at exactly capacity." A second currency the points system must not double-count. |
| C29 | **Anti-hero cap: CUT** | The old ⅓-of-budget cap is removed | `List Building.md:51` | Do not reintroduce it — C7 already forbids heroes. |
| C30 | **No pay-to-win** | "A bigger model budget must not beat better play" | `Out of Scope.md:23` | Tenet-level. |
| C31 | **Game length** | **6 rounds**, ~90 min target | `Core Game Format.md:39`, `Rules Engine.md:36`, `Rules Ledger\core-008…:16` | Caps how many activations any purchase can pay back over. BLKOUT analysis recommends tightening to **45–75 min** (`BLKOUT-RULES-ANALYSIS.md:396, :410`). |
| C32 | **Board 3'×3'** | Standard | `Core Game Format.md:33` | The origin of C4 and C10. |
| C33 | **Activation economy** | 1 Move slot + 1 Action slot; Sprint/Charge = 2×MOV and **both** slots | `Rules Engine.md:59, :63-64` | The denominator of every efficiency calculation. |
| C34 | **Orders per rank** | Recruit 0 · Fighter 0 · Specialist 1 · Leader 2; **cannot chain**; **one Order received per unit per round**; issued **only in the issuer's own activation** (locked 2026-07-13) | `Rules Engine.md:67-71`, `Initiative & Activation.md:73-75` | Quantified: activation-bound Orders hold a 4-model elite at 4 activations + 4 Ready; free timing *"would push that to **7 shots from 4 models**"* (`Rules Engine.md:74`). |
| C35 | **Ready: one token max**, react once per token | | `Initiative & Activation.md:46, :54` | Caps the reaction economy that makes small crews viable (N12). |
| C36 | **Reaction trigger floor** | Enemy must end a Move **greater than half its MOV** | `Initiative & Activation.md:56`, `Movement.md:41` | A cliff, not a gradient — see N22. |
| C37 | **Reaction attacks are nerfed** | Reaction Charge = MOV (not 2×) and **no** Charge +1; Snap Shot takes **no** extra −2 | `Initiative & Activation.md:65-66` | |
| C38 | **Underdog +1 Priority is the only catch-up rule** | *"No free-hold surge rule"* | `Initiative & Activation.md:78`, `Rules Ledger\core-005…:22` | *"not an exploit for small crews — it is their **compensation**"* (`:85`). |
| C39 | **Complexity ceiling** | **~2 activations per fighter**; a fighter activates **in under a minute**; **a rule must fit its reference card** | `Out of Scope.md:38-42` | The nearest thing to a printing/bookkeeping constraint that exists. |
| C40 | **No ammo, encumbrance or hit locations** | Explicit ban | `Out of Scope.md:41` | Blocks several 2051 hooks (§2.9). |
| C41 | **Fall bands** | under 3" nothing · **3"+ Prone** · **6"+ Injury** at +1 Damage per full 2", ignoring armour | `Terrain.md:103, :158`, `Infrastructure.md:79` | *"First injuring fall (6") = +3 = 70% vs WND1; drop to +2 if it plays too hot."* |
| C42 | **Board damage maims, never executes** | CRUSH and FALL leave a model **Down**, never straight **Out** | `Infrastructure.md:82` | Keeps terrain from being a kill engine you could buy. |
| C43 | **No structural integrity** | No damaging walls/cover, no collapse; features are two-strike (Online → Offline → Destroyed), **repairable once** | `Terrain Interaction.md:101, :112-116, :164` | Bookkeeping limit; also caps what a "durability" purchase could ever mean. |
| C44 | **Feature durability** | **WND 1, Armour −2**; Heavy (−2) cover to hit **unless attacker within 6" → Open** | `Terrain Interaction.md:109-111` | The fragility that discounts every deployable. |
| C45 | **Conditions never stack** | Reapplying refreshes duration, never deepens; +1 Stress only on **first** application | `Conditions.md:44-45` | Direct anti-linearity, written as a rule. |
| C46 | **Morale numbers are locked** | *"**do not touch these numbers**"* | `Morale.md:85` | Two softeners were tested and **both broke the game** (`Morale.md:85-90`). |
| C47 | **Break ladder** | Shaken at **1+** Stress (flat −1, does not deepen); Break test at **2+**; 2 = Bolt · 3 = Broken · **4+ = BugOut** | `Morale.md:48, :50, :62-66` | The first Stress point is *"a **free buffer**"* (`Morale.md:55`). |
| C48 | **Bottling timing gate** | Rounds 1–3 withdrawal only; **Round 4+** a clean bottle = opponent wins | `Morale.md:95-98` | *"an early bottle is never free."* |
| C49 | **Hacking range bands** | Close 0 · Short −1 · Medium −2 · Long −3, **max 24"**; **no breach roll in v1** | `Infrastructure.md:100, :104`, `Rules System — Master Roadmap.md:189` | |
| C50 | **Triggers cannot be destroyed** | Manual operation in base contact always remains available, and **cannot be Interrupted** | `Infrastructure.md:92, :110` | *"the payoff for exposing yourself in base contact."* |
| C51 | **Never invent a new condition** | Infrastructure and terrain effects must reuse existing Conditions | `Infrastructure.md:73`, `Terrain.md:84` | Caps the design surface any new costed item may claim. |
| C52 | **Terrain composition floor** | At least **2 Buildings/Ruins** and real interactive pieces; *"a bare board is not a Settlements board"* | `Terrain.md:114` | A quality floor under the 9–12 count. |
| C53 | **Building access floor** | **Every floor** must have at least one **no-test** route | `Terrain.md:76` | *"Climbable walls are optional shortcuts, never the only way up."* |
| C54 | **Settlement never buys board advantage** | A developed settlement changes *what* fills its three squares, **never how many** | `Terrain.md:127-128` | The structural firewall between the two economies. |
| C55 | **Scenario hard numbers** | Hold radius **3"**, no enemy within 3"; **no scoring in Round 1**; Take a Hold max **15 VP** | `Scenarios.md:69, :73, :97` | All flagged as open dials (`Scenarios.md:150-154`). |
| C56 | **Alpha content slice** | **1 faction · 10 units · 10 buildings · 5 resources · 3 scenarios** | `RULES-COMPLETION-PLAN.md:73` | Bounds how much must actually be costed for alpha. ⚠ "5 resources" is stale — see §6.11. |
| C57 | **Every structure has a mechanical purpose, never décor** | Design law | `RULES-INTERVIEW-PLAN.md:9`; `Structures.md:46-47` | No structure may be priced as flavour. |
| C58 | **Tabletop-first** | *"no rule may **require** the app"* | `SETTLEMENT-DESIGN-QUESTIONS.md:26`; `Out of Scope.md:22` | A points system may not depend on a calculator. |
| C59 | **Depth lives in the settlement layer, not in point-buy** | *"Keep list-building minimal — let terrain + base-building shine (your flagged **BIG RULE**)"* | `SETTLEMENT-DESIGN-QUESTIONS.md:24`; `Ideas Inbox.md:34` | ⚠ **The single strongest constraint on how elaborate the rebuild may become** — and it points the opposite way to atomic costing. See §6.16. |
| C60 | **Not a stat-driven optimisation game** | *"Victory should not come from list building alone. **Tactical play on the battlefield must outweigh pre-game optimization.**"* | `Game Vision.md:77-78` | Tenet-level ceiling on how much the points system may decide. |

---

## 4 · Non-linearity register — where linear pricing provably fails

This is the section that most constrains an atomic system. Each entry states the mechanism and, where measured, the number.

### N1 · Range is a threshold, not a curve — **measured, and it defeated pricing**
> "Uncapped, a long-range crew beat every list by **13–30 points** *at any price*. **Hard cap: 24".**" — `Crew Sim — Findings.md:67`
> "That is a **threshold**, not a linear advantage, and **no points cost can balance a threshold**." — `Weapons.md:40`

The 24th inch is worth categorically more than the 23rd, because it crosses the deployment gap. **Long Range costs a flat 6 points** (`Weapons.md:95`) for +6", which is correctly priced *below* the ceiling and infinitely underpriced *at* it — which is why it is capped rather than costed.

### N2 · The ±3 modifier cap makes stacked bonuses worth zero at the margin
Under C5, a fighter already at +3 gains nothing from a fourth +1. So a Targeting Beacon (8 pts, +1 to hit — `Deployables.md:142`) is worth ~+10% to an unmodified ally and **0%** to a capped one. Priced flat; worth a variable amount. Same for the Breach Kit / Exploit Suite ladder.

### N3 · The 90% success ceiling — +5 and +6 are identical on a flat roll
> "A flat test still tops out at 90% (the natural-1 floor), so **+5 and +6 read the same on an *unmodified* roll** — the extra point earns its keep against cover, armour, and opposed rolls." — `Unit Design.md:89`

Measured: `Dice Mechanic — Sim Findings.md:24-25` (+5 = 90%/89.7%, +6 = 90%/90.0%). **Diminishing returns are total, not gradual, at the top of the stat ladder.** A linear stat price is wrong by construction for the 6th point.

### N4 · Multi-attack is the biggest DPS lever in the game — and superlinear in cost terms
> "A second attack even at −2 is a **~+60–67% output** spike — the biggest raw DPS jump in the game." — `Skill Sim — Findings.md:36`

Measured (`Skill Sim — Findings.md:28-34`): Quick Shot 0.36 → 0.60 wounds/activation (**+67%**); Dual Wield 0.23 → 0.37 (**+62%**).

Consequences already visible in the costs:
- Burst Turret was **repriced 16 → 18** purely for being two shots (`Deployables Sim — Findings.md:34`).
- The proposed **Rapid** characteristic was **cut**: *"Selling it to a Fighter for 4 points destroys the entire skill economy"* — `Weapons.md:175`.

> ⚠ **Caveat the findings note does not state.** `skills_sim.py:54` measures this against a target of *"WND=inf, no cap"* — `ew_ranged()` (`skills_sim.py:55-58`) sums both shots' expectations unconditionally. At the game's actual **WND 1**, the second attack is wasted whenever the first kills. **+67% is an upper bound that does not hold in the real game.**

### N5 · Gunslinger is worth literally zero in a 1v1 and non-zero at crew scale
> "**Gunslinger** (2 targets) — **0 in a 1v1**; only pays vs multiple foes." — `Skill Sim — Findings.md:34`, implemented at `skills_sim.py:69`

The cleanest demonstration in the project that **model count changes a thing's value discontinuously**. Any ability that reads "different targets", "each enemy within", "every model within 2"" (Blast), or "every enemy Engaged with you" (Cleaving) has value proportional to enemy clustering — which is set by the board, not the price.

### N6 · Beacon auras scale with ally count, and are capped to stop it
Measured: each ±1 aura is "**~+10%** per affected ally" (`Deployables Sim — Findings.md:52`, `deployables_sim.py:126-137`). A flat 8-point Munitions Beacon is worth +10% × N clustered allies. Two brakes exist precisely because of this:
> "An aura **does not stack with itself** (two Munitions Beacons ≠ +2)… **A model benefits from at most two friendly beacon auras at once.**" — `Deployables.md:136-137`

**Explicit anti-linearity written into the rules.**

### N7 · Composure skills scale with fight length — near-worthless at WND 1, dominant at WND 3
> "**Steady / Rattle-Proof (+23%)** are only that strong because WND-3 fights *last*. In a fast **WND-1** fight — the common case — Stress rarely reaches 2, so **they're worth close to nothing**." — `Skill Sim — Findings.md:84`

Same skill, same tier, value swings from ~0 to +23 percentage points purely on the WND value. Since WND is fixed at 1 (C7) but **Tough** (free, STR T3) raises it, a crew containing Tough changes the value of its *other* skills.

### N8 · Terrain density swings win rate by 66 points — the master non-linearity
Measured, Cadre (4 models) vs Recruit horde (14), Cadre win % as LOS-blocking rises (`Crew Sim — Findings.md:16-18`, generated by `crew_calibrate.py:65-77`):

| LOS blocked | 10% | 20% | 30% | **40%** | 50% | 60% |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **Cadre wins** | 81% | 73% | 62% | **45%** | 29% | 15% |

**A 66-point swing from terrain alone.** Parity sits at 40–45% blocked, which is what 9–12 features produces. The costing implication is blunt: **a unit's points value is a function of the board, and the board is only pinned within a band.** Any global points number is a statement about the *centre* of that band.

### N9 · Stat value is scenario-dependent, not intrinsic — AGI and INT price at zero in combat
> "the Objective Grabber wins **24%** on bare ground and the Heavy Gunner **69%**. **The board prices stats. Points price bodies and guns.**" — `List Building.md:24`
> "AGI and INT are worth **literally zero** in it **by construction**" — `Crew Sim — Findings.md:73`

⚠ **This is the finding that has already caused one real error.** See §5.2 — it is a 1v1, terrain-free, cover-free measurement in which the resolution code *never reads AGI or INT*. The 2D engine, which *does* have objectives, reaches the opposite conclusion (see N10).

### N10 · Objectives invert the combat ranking — the spatial engine contradicts the abstract one
Measured at crew scale with real objectives, 2000 games/cell, sides swapped (`engine2d\README.md:57-64`):

| row \ col | balanced | runner | hunter |
|---|--:|--:|--:|
| **balanced** | 49 | **100** | **60** |
| **runner** | 0 | 50 | 2 |
| **hunter** | 41 | 98 | 50 |

> "A crew that **only kills and ignores objectives (hunter) loses to balanced, 41 vs 60** — **killing isn't the win; you must stand on the point.**" — `engine2d\README.md:64`

The abstract sim says pure combat power dominates. The spatial sim says pure combat power **loses**. Both are right about their own scenario. **A global points system that prices combat output alone will systematically overprice hunters and underprice objective-capable units.**

### N11 · Action economy — a deployable costs points but no activations
> "Turrets sit slightly above the body's raw output-per-point — **correct, because they cost zero activation after setup** and fire 360°, and the discount is their one-hit fragility." — `Deployables Sim — Findings.md:39`

Measured (`Deployables Sim — Findings.md:31-36`): Autoturret 0.0233 w/rd/pt vs the Assault-Rifle body baseline 0.0200 w/rd/pt. **Points bought per-round output; activations were not part of the price.** An atomic system needs an explicit activation-economy term, or turrets will always price wrong.

Conversely: **Sprint consumes both slots**, which is why the **Quick Draw** characteristic was cut — *"there is no Action left to fire with. It silently invents a new action economy."* (`Weapons.md:178`)

### N12 · Model count changes the value of Ready / reactions
> "The elite crew converts its last activations into **Ready** and snap-shoots the tail as it moves — 4 models = 4 banked reactions, so **every fighter effectively shoots twice**." — `Crew Sim — Findings.md:63`

A 4-model crew converts a numbers deficit into an action surplus. Plus the **underdog +1 Priority** (`crew_sim.py:255-256`, `engine2d\engine.py:546-547`) — an explicit rule that pays you for having fewer models. **Both make small crews worth more per point than a linear model would predict.**

### N13 · Drawbacks are only worth their refund if they always bite — otherwise they are free points
> "**Slow on a rifle is free points** — a rifleman never Charges anyway. **Awkward** *(may not Move and attack)* **is free points on a sniper** — he never moves anyway, and it **synergises** with **Accurate**, which pays you for standing still. **Awkward is cut.**" — `Weapons.md:117-118`

The Awkward case is a *negative-cost synergy*: a drawback that pays you refund points **and** improves a build. Machine-guarded now at `weapon_sim.py:69-73`. **Any global system with negative-cost options must re-run this check on every combination.**

### N14 · Conditional bonuses are worth ~+20% only when the condition is met
Measured (`Skill Sim — Findings.md:18-24`): a +2 conditional (Feint / Ghost Blade / The Muscle) is a ~+20% swing *when its condition fires*; "**that condition is the balancer**". A flat price implies an assumed trigger frequency that is never stated anywhere.

### N15 · Bleed is a two-round death clock specifically because WND is 1
> "**Bleeding** | 4 | **Bleed** — *at WND 1 this is a two-round death clock unless treated. The deadliest payload; priced for it.*" — `Weapons.md:81`

Bleeding costs 4 while every other payload costs 3. **The +1 premium is entirely a consequence of C7.** If WND ever moved, this price would be wrong — and **Tough** (free) moves it.

### N16 · Grapple is a lock, not a linear debuff
Measured (`Skill Sim — Findings.md:41-46`): a STR+2 grappler lands it **64%**; the victim escapes only **28%** per turn; ~40% to injure each Squeeze in between. Compounding across turns. Verdict: *"**STR grapplers are a hard lock** — points-cost or scenario counters needed so they don't neutralise single elites for free"* (`Skill Sim — Findings.md:106`). **A lock's value scales with the target's cost** — it is worth far more against a 40-point Leader than a 5-point Recruit.

### N17 · Chained probabilities collapse — the triple-gate lesson
The parked hacker shut-out chained opposed-INT × effect roll × outcome table and landed at **14% real effect for a whole activation** at even INT (`Terrain Hacking Cover — Sim Findings.md:20-27`). **Multiplying gates destroys value far faster than adding costs reduces it.** Any priced ability with two or more sequential rolls needs measuring, not estimating.

### N18 · Interrupt is a hard counter — 1 hacker can never beat 1 interrupter
> "1 unit alone = **0%** — a lone hacker can't beat an interrupter. Bring bodies." — `hacking_sim.py:44`

You need **two** successful hacks to push one feature past one interrupter (`hacking_sim.py:5-6, 38-43`). **A discontinuity at N=1 → N=2 models.** No per-model price can express "the first one is worth nothing".

### N19 · Height advantage is nearly free — the cover term barely matters
Measured sensitivity sweep, 3000 games each (`engine2d\README.md:71`): none **49.1%** · ignore-Light (RAW) **48.9%** · −1 any cover **50.6%** · −2 any cover **51.0%**.
> "win% is **flat across the whole range**… **You can tune the height-cover bonus freely (even −2) without breaking balance.**"

The driver is **see-over LOS + objective control**, not the modifier. **A mechanic's points value can be almost entirely decoupled from its printed modifier.**

### N20 · The settlement/points firewall is itself an anti-non-linearity device
"Ownership buys availability, never free board power" (C-rule above) exists to stop settlement investment compounding into battlefield points. Auto-deploy removes only the INT test; the deployable still costs crew-points and still eats a density slot (`Deployables.md:61`). **Without this, structures would be a points multiplier rather than a points sink.**

### N21 · The density effect is **U-shaped**, not monotonic
Measured spreads across the band (`List Building.md:86-88`, `Crew Sim — Findings.md:47-49`): sparse = **35**-point spread (shooters dominate) · legal 9–12 = **11** points (tightest) · crowded = **34** points (swarms dominate). The system is not "more terrain = better for swarms, price accordingly" — it is a **minimum at the centre of the band with divergence in both directions.** No single points table can be correct off-centre.

### N22 · The reaction trigger is a cliff at half MOV
> "a short shuffle of **≤ half MOV** doesn't draw fire" — `Initiative & Activation.md:56`, `Movement.md:41`

Moving half your MOV draws nothing; moving one inch further draws full reaction fire. **MOV therefore has a discontinuous defensive value at exactly 3"** (half of 6"), and any MOV purchase changes where that cliff sits. The BLKOUT analysis calls this out as a feature: *"turning movement **distance** into a tactical dial … a huge amount of tactical texture for one sentence of rules"* (`BLKOUT-RULES-ANALYSIS.md:401`).

### N23 · Quality has a hard ceiling that quantity does not
> "swarms out-produce elites on raw output, because **WND is fixed at 1 and the Injury roll ignores stats, so quality has a hard ceiling that numbers don't**." — `Initiative & Activation.md:85`

The Injury roll reads **weapon damage and armour only** — never a stat. So investment in stats improves *hitting*, never *killing*. **There is a hard asymptote on what any amount of points spent on one model can achieve**, and none on what spreading them across bodies achieves. This is the deepest structural non-linearity in the game.

### N24 · Modifiers past the cap still constrain, so condition count is not linearly valuable
> "**Conditions past the cap still matter** — they still restrict actions and still have to be cleared." — `Conditions.md:46`

The numeric part saturates at ±3; the *restriction* part keeps accruing. A costed condition-applier therefore has two value curves that diverge, one flat and one linear.

### N25 · Matchup-conditional value — items worth zero against half the field
The 2051 hooks are riddled with these, and none can be priced in isolation:

| Item | Statement | Line |
|---|---|---|
| Leonidas HPM | *"**hard-counters swarm factions, worthless vs conventional armour**"* | `SETTING-TECH-2051.md:132` |
| THOR | *"disables all drone/electronic units … **no effect on hardened troops**"* | `:126` |
| Assured Nav | *"**ignore the Jammer-zone penalty**"* — worth nothing vs a non-EW list | `:312` |
| Trophy APS | *"**ineffective vs direct KE rounds** and (until upgraded) top-attack"* | `:148` |
| Iron Curtain | *"the **only** APS that saves vs overhead/loitering-munition strikes"* | `:160` |
| Fibre FPV drone | *"**ignores ECM/jammers**"* | `:206` |
| Spectral scanner vs adaptive camo | *"an **arms race** with adaptive camo"*; *"sensor-vs-camo **rock-paper-scissors**"* | `:328`, `:86` |
| C-UAS layer | *"a force with no C-UAS is **auto-punished** by drone factions"* | `:242` |

The doc names the consequence itself: the faction set *"form a rough **rock-paper-scissors** … That triangle is the **tuning surface**"* (`:445`). **A rock-paper-scissors meta cannot be costed with a single global scalar per item.**

### N26 · Saturation thresholds — defences whose value collapses past an attacker count
- C-RAM: *"reliable but **ammo-limited and saturable, so massed cheap attacks can overwhelm it**"* — `SETTING-TECH-2051.md:172`
- Lancet: *"**can salvo to defeat point defence**"* — `:200`
- Swarms: *"**spreads to saturate, reforms after losses**"* — `:212`
- Iron Beam: *"reshapes the game by **taxing artillery and air spam**"* — `:114`
- The premise: *"cheap drones are a **currency**, and DE is the **'sink'** that stops them dominating"* — `:138`

Also measured in the genre analysis: with no morale, *"the game skews toward **alpha-strike snowballing** — remove models first and the **activation/dice advantage compounds**"* (`BLKOUT-RULES-ANALYSIS.md:295`).

### N27 · Network effects — one purchase buffing N models
- Squad vision: *"**any model's line-of-sight spots for the whole unit**"* — `SETTING-TECH-2051.md:68`
- Relay Node: *"extending a **command/coordination aura**; killing nodes shrinks the network and **cuts squad buffs**"* — `:300`
- C2 node: *"**while the command node lives**, units share a targeting picture (**reroll to-hit / act out of activation order**); destroy the node and the army **fights blind**"* — `:410`
- Reactor: *"powers a faction's directed-energy and C2 assets; capturing or breaching it **browns-out those systems**"* — `:362`

**A single point of failure whose price is the sum of everything downstream of it** — the exact inverse of an atomic cost.

### N28 · Enablers price off the delta they unlock, not their own output
- S-MET mule: *"offloads carry-weight (**unlocks heavier loadouts**)"* — `SETTING-TECH-2051.md:276`
- Autonomy module: *"usable on **multiple chassis**"* — `:392` — one price, many hulls
- Lightweight materials: *"lighter guns improve movement/AP **or** let a lone trooper carry a heavy weapon"* — `:52`
- In-game: the **Med-Kit at 4 points** is priced almost entirely against Bleed, *"the harshest condition in the game by a wide margin"* (`Conditions.md:65`) — its value is a function of how much Bleeding the enemy bought.

### N29 · Uncapped resources cannot be priced against a bounded budget
*"**unlimited power** for shields/DEW"* (`SETTING-TECH-2051.md:368`) · *"**unlimited ammo**"* (`:96`) · *"**never runs out of shots**"* (`:102`) · *"**near-free trigger**"* (`:108`) · *"'reusable' = **doesn't deplete on a miss**"* (`:224`). The doc offers two rate limiters (heat track `:96`, capacitor charge `:422`) — **both are new bookkeeping**, which collides with C39/C40.

### N30 · Composure is deliberately not free — an explicit design position on pricing
> "**Deliberately: composure is a build choice, not free.**" — `Morale.md:108`

The one place the vault takes an explicit stance that a *defensive* quality must be paid for rather than granted. Worth noting because it cuts against "stats and skills are free".

### N31 · Escalating tier costs are already the stated anti-inflation lever
> "Anti-inflation: **storage caps** + **escalating costs** + raids (no decay)" — `Interviews — Completing the Rules System.md:63`; also `SETTLEMENT-DESIGN-QUESTIONS.md:207`

**Non-linear pricing is already the intended shape on the settlement side.** Whatever the crew-points system does, the resource economy is planned to be superlinear.

### N32 · Structure over-claiming self-corrects through opportunity cost, not price
> "Re-reserve the bigger footprint on the sheet — **it costs you other structures, so it self-corrects.**" — `Board Representation.md:25`

A worked example of the design's preferred mechanism: **scarcity of space instead of a price**. `Structures.md:211` states the principle — *"**Scarcity produces divergence; tech trees produce convergence**"*.

---

## 5 · Simulation evidence register

Everything the sims have ever measured, with the conditions attached. **This is the only hard evidence any costing decision can rest on.**

### 5.0 The harness — what exists, and its state

| Script | Lines | Tracked? | Seed | Sample | Scale | Purpose |
|---|:--:|---|---|---|---|---|
| `sim_report.py` | 216 | ✅ | 20260708 | N=10,000/test | **1v1 + exact math** | Core-engine validation + archetype duel matrix |
| `stress_pen.py` | 55 | ✅ | 20260709 | N=40,000 | **1v1** | Is Shaken's −1 the right severity? |
| `skills_sim.py` | 238 | ✅ | 20260710 | N=10,000 | **1v1, WND 3** | Per-skill value |
| `crew_sim.py` | 429 | ✅ **modified** | 20260713 | N=3,000/matchup | **Crew, 1D board** | List-building cost validation |
| `crew_calibrate.py` | 111 | ✅ | 20260713 | N=3,000/point | **Crew, 1D board** | Terrain sweep + stat-allocation |
| `weapon_sim.py` | 379 | ✅ | 20260713 | *(library)* | **Crew, 1D board** | Built-weapon engine — no `__main__` |
| `weapon_tests.py` | 197 | ✅ | 20260713 | N=2,500/cell | **Crew, 1D board** | Weapon battery + crew matrix |
| `terrain_hacking_sim.py` | 131 | ✅ | 20260713 | N=10,000 | **Exact + 1v1** | Cover / fall / hack / disengage battery |
| `hacking_sim.py` | 56 | ✅ | — | exact combinatorics | **N/A** | Hacking v1 interrupt maths |
| `deployables_sim.py` | 182 | ✅ | 20260715 | exact + MC N=40,000 | **1v1 / analytic** | Deployables catalogue check |
| `index.html` | 905 | ✅ | — | interactive | 1v1 | Browser probability calculator (not a results file) |
| **`engine2d\`** | ~1,400 | ❌ **untracked** | 20260717/18 | 2,000–3,000 games | **Crew, true 2D + objectives** | Full Take-a-Hold games |

**No saved output of any kind exists.** No JSON, CSV or log files anywhere under `test-bench\` (verified by `find`). Every published number lives only in the vault's findings notes. `__pycache__` timestamps show last import: `crew_sim` 2026-07-13 15:59 · `crew_calibrate` 16:01 · `weapon_sim` 16:47 · `engine2d\engine` **2026-07-23 02:10** (the most recent run in the project).

#### 5.0.1 The uncommitted `crew_sim.py` change — **cosmetic, findings still stand**

`git diff` shows 22 insertions / 22 deletions, and **every one is a rank rename**: `Rabble → Recruit` and `Recruit → Fighter`, plus the matching label strings. `RANK` values are unchanged (`crew_sim.py:59`: `{'Recruit': 5, 'Fighter': 8, 'Specialist': 16, 'Leader': 24}`). **No numeric or mechanical change. All published crew-sim findings remain valid.**

> ⚠ **But the rename broke a sibling script.** `crew_calibrate.py:99` still builds its horde from `CS.fighter('Recruit', 'bat', **kw)`. Under the old naming that was the **8-point middle rank**; under the new naming it is the **5-point bottom rank**. So `crew_calibrate.py` §3 ("what should a Recruit actually buy?") now builds a *different, cheaper* crew than the one that produced the published `14/35/63` numbers — **and the bottom rank is not even allowed tiered stats** (`Unit Design.md:113`). **Re-run required before that finding is used again.**
>
> Separately, `weapon_sim.py:39, 97-98` and all of `weapon_tests.py` **still use the old names** (`Rabble` / `Recruit`). The harness is now internally inconsistent about rank naming.

#### 5.0.2 The stat-line gap — **every sim ran units 3 stat points below the current rules**

| Rank | Stat pts the sim gave | Stat pts the rules grant | Gap |
|---|:--:|:--:|:--:|
| Recruit | **0** | 3 | −3 |
| Fighter | **2** | 5 | −3 |
| Specialist | **4** | 7 | −3 |
| Leader | **6** | 9 | −3 |

Sim lines: `crew_sim.py:292-327` (e.g. Leader `dex=4, str=2` = 6 pts; Specialist `dex=4` = 4; Fighter `dex=2` = 2; Recruit no stats = 0). Rules: `Unit Design.md:101-106`. Independently encoded in `engine2d\data.py:10-16` as the legacy `RANKS` table (`stat_pts=0/2/4/6`) alongside the current `RANKS_V2` (`points=3/5/7/9`, `data.py:24-29`).

The gap is **uniform**, so *relative* rank pricing is probably preserved; **absolute** power is understated across the board. The vault already anticipates the consequence (`Unit Design.md:121-122`).

#### 5.0.3 Stats are free in **every** engine
`crew_sim.py:66` · `weapon_sim.py:105` · `engine2d\data.py:94-99` all compute cost as `rank + weapon + armour (+equip/deployable)`. **No simulation in this project has ever attached a price to a stat point.**

---

### 5.1 Crew-scale evidence (1D abstract engine)

Conditions common to all rows: **1D board 36" long, deployment 6" from each edge (24" apart), 6 rounds, WND 1, N=3,000 battles/matchup, seed 20260713.** Terrain is a *probability knob* (`crew_sim.py:9-11, 43-47`), not geometry. Win = last crew standing, or at 6 rounds the larger surviving *share* with a 5% draw margin (`crew_sim.py:286-288`). **Not modelled: objectives, skills, hacking, terrain interaction, flanking, Hidden, stabilise/bleed-out** (`crew_sim.py:13-14`).

| # | Measured | Headline | Scale | Conditions | Source | Still current? |
|:--:|---|---|---|---|---|---|
| S1 | Terrain density vs elite/swarm balance | **66-point swing**: Cadre(4) beats horde(14) 81% at 10% blocked → 15% at 60%. Parity at 40–45% | **CREW** | 4v14 models, WND 1, N=3000/point, blocked swept 10–60%, witness rate co-varies | `Crew Sim — Findings.md:16-18`; run by `crew_calibrate.py:65-77` | ✅ Reproducible |
| S2 | 8-archetype balance at 100 pts | **11-point spread** on a legal board; 35 sparse; 34 crowded | **CREW** | "42% blocked", 100-pt lists, N=3000 | `Crew Sim — Findings.md:31-49` | ⚠ **NOT reproducible — see §6.5** |
| S3 | Morale softeners | Both broke the game: "ignore Stress while bunched" → horde **93–96%**; "cap Stress at 1/round" → **60–88%**. As-written: 19/39/54/85% | **CREW** | Recruit horde vs Cadre, blocked 10/30/40/60% | `Crew Sim — Findings.md:54-58`; `crew_calibrate.py:80-92` | ⚠ Tests **The Mob doctrine**, since removed (`Crew Sim — Findings.md:28`) |
| S4 | Break cascade rate | **0.6 BugOuts/battle** on a legal board vs **5.3** on a sparse one | **CREW** | N=400/density (`crew_sim.py:397`) | `Crew Sim — Findings.md:60` | ✅ |
| S5 | What a Fighter should buy | **STR+2: 14/35/63%** · NRV+2: 10/21/40 · DEX+2: 5/16/36 (sparse/mid/dense) | **CREW** | 9-model horde vs Cadre(4), blocked 10/35/55% | `Crew Sim — Findings.md:69`; `crew_calibrate.py:94-109` | ⚠ **Broken by the rename — see §5.0.1** |
| S6 | Rank ladder consistency | 9-Fighter horde, 11-model pyramid and 14-model horde land within **3 points** of each other at every density | **CREW** | as above | `Crew Sim — Findings.md:70` | ✅ (subject to §5.0.2) |
| S7 | Long-range cap | Uncapped long-range crew beat **every** list by **13–30 points** at any price | **CREW** | as above | `Crew Sim — Findings.md:67` | ✅ — the reason for C3 |
| S8 | Melee elites | A 4-model melee crew wins ~**10%**; with the Storm doctrine's armour budget, **51%** | **CREW** | as above | `Crew Sim — Findings.md:68` | ⚠ Storm removed — "a **live balance question**" |
| S9 | Weapon-variant acceptance threshold | *"A variant >15 pts of win rate above its baseline at similar cost is a problem"* | **CREW** | 4-model chassis probes vs Mob/Horde/Standard at 42% blocked, N=2500 | `weapon_tests.py:166`, probes at `:146-158` | ✅ Stated threshold; **results never published** |
| S10 | DEX vs STR | Gunline(4, 99 pts) vs Brawlers(6, 99 pts) swept across blocked 20–60% | **CREW** | N=2500/point | `weapon_tests.py:183-196` | ✅ Test exists; **results never published** |

### 5.2 ⚠ 1v1 evidence — **do not generalise to crew scale**

> **The error this section exists to prevent.** `Dice Mechanic — Sim Findings.md:113` concludes that utility builds are near-useless from a duel matrix in which the resolution function **never reads AGI or INT**. `attack()` at `sim_report.py:119-128` uses only `dex`, `str`, `dmg`, `arm`, `cov`. The Objective Grabber (`sim_report.py:114`: `str=1, dex=2, agi=4, int=2, dmg=1`) loses 24% of the time **because it has low STR/DEX/damage — its AGI 4 is never rolled once.** The finding is a tautology about the model, not a measurement of AGI's worth. The 2D engine, which does have objectives, reaches the opposite conclusion (S20–S22).

| # | Measured | Headline | ⚠ Scale | Conditions | Source |
|:--:|---|---|---|---|---|
| S11 | Core test curve | ±10%/point, floored/capped 10–90%; **+5 = +6** on a flat roll | Exact math | Full enumeration + N=10,000 | `Dice Mechanic — Sim Findings.md:16-25`; `sim_report.py:45-50` |
| S12 | Difficulty ladder | Raising the target by 2 ≈ **−20%** | Exact math | 7+/9+/11+ | `Dice Mechanic — Sim Findings.md:31-35` |
| S13 | Cover ladder | Open 59.8% hit / 2.8 shots-to-Down → Hidden 30.0% / 5.7. **Cover roughly halves lethality** | **1v1** | DEX+2, weapon +2, unarmoured, **no terrain geometry** | `Dice Mechanic — Sim Findings.md:42-47`; `sim_report.py:67-73` |
| S14 | Weapon vs armour | Heavy +3 is "almost exactly cancelled" by heavy −2 (41.9% → 29.4%) | **1v1** | open target, DEX+2 | `Dice Mechanic — Sim Findings.md:51-55` |
| S15 | Melee & charge | Even fight = **46.5%** attacker (defender tie-edge); **Charge ≈ +8%**, flipping it to 54.8% | **1v1** | opposed STR, light weapon +1, no armour | `Dice Mechanic — Sim Findings.md:63-69` |
| S16 | Opposed contests | Each point of advantage ≈ **±9–10%** | Exact math | ties→defender | `Dice Mechanic — Sim Findings.md:78-83` |
| S17 | **Duel matrix** | Heavy Gunner **68.9%** → Objective Grabber **24.1%** | ⚠⚠ **1v1, WND 1, NO terrain, NO cover** | 10,000 fights/pair, random first, Stress on. **AGI/INT never read.** | `Dice Mechanic — Sim Findings.md:88-110`; `sim_report.py:110-117, 156-157` |
| S18 | Stress/Nerve firing | WND 1: **0.089 cracks/fight** (fights last 1.6–2.3 rounds). WND 3: **1.75 cracks/fight** | ⚠ **1v1; the 1.75 is WND 3, not the game's WND 1** | `sim_report.py:210-215` | `Dice Mechanic — Sim Findings.md:120-123` |
| S19 | Shaken's −1 severity | A Shook brawler drops an even fight to **33%**; a Shook shooter to **~40%**. −1 = exactly one stat point | ⚠ **1v1** | N=40,000/cell | `Dice Mechanic — Sim Findings.md:135-140`; `stress_pen.py` |
| S20 | Flat skill modifiers | Dead Eye +10% · Heavy Hands +10% · Feint +19% · Ghost Blade +19% · The Muscle +20% | Exact math | closed-form, no board | `Skill Sim — Findings.md:18-24`; `skills_sim.py:40-49` |
| S21 | Multi-attack | Quick Shot **+67%**, Dual Wield **+62%** output | Exact math ⚠ **target WND=∞** | `skills_sim.py:54-68` — no overkill cap | `Skill Sim — Findings.md:28-34` |
| S22 | Grapple chain | STR+2 grappler lands 64%; victim escapes 28%/turn; Squeeze injures 40%/use | Exact math | opposed STR, ties→defender | `Skill Sim — Findings.md:41-46` |
| S23 | Bravery path | Rattle-Proof / Braced each shave **~10%** off breaking | Exact math | NRV+2 at Stress 2/3/4 | `Skill Sim — Findings.md:52-56` |
| S24 | **Marquee skill duel** | Quick Shot **+24** · Dual Wield +23 · Rattle-Proof +23 · Steady +23 · Feint +20 · Ghost Blade +20 · Tough +15 · Weave +13 · Dead Eye +10 · Iron Will +6 · The Muscle +3 · Feed the Anger −1 · Fanatic −7 · Red Mist −14 | ⚠⚠ **1v1 mirror, WND 3** — *not the game's WND* | 10,000 duels/skill, seed 20260710. WND set to 3 explicitly "so fights last long enough" | `Skill Sim — Findings.md:63-78`; `skills_sim.py:99-103, 193-234` |
| S25 | Fury-skill spam | Red Mist spammed = **1.7%**; Feed the Anger spammed = **36%** | ⚠ 1v1 WND 3 | `skills_sim.py:219-226` | `Skill Sim — Findings.md:80` |
| S26 | Cover vs the ±3 cap | Cover-separate ruling holds: Shaken stays worth −10% into Hidden (20% vs 30% shared-cap) | Exact math | `terrain_hacking_sim.py:43-51` | `Terrain Hacking Cover — Sim Findings.md:65` |
| S27 | Fall damage | 2–3" fall = **50% wound = 50% Down at WND 1** — "a coin-flip kill". 4"=60%, 6"=70%, 8"=80% | Exact math | ignoring armour | `Terrain Hacking Cover — Sim Findings.md:35-39` |
| S28 | Height advantage | Attacker 2"+ up ignores Light: 50%→60% to-hit, **~+20% lethality** | Exact math | Heavy cover still counts from above | `Terrain Hacking Cover — Sim Findings.md:58` |
| S29 | Disengage cost | **14%** Downed fleeing 1 engager, **26%** fleeing 2 — *and* you lose the whole activation | 1v1/1v2, N=10,000 | `terrain_hacking_sim.py:100-111` | `Terrain Hacking Cover — Sim Findings.md:48-51` |
| S30 | Heavy armour on terrain | **−10% on every terrain test** — "the lever that makes terrain punish the Heavy Gunner" | Exact math | AGI 0…+6 with/without −1 | `Terrain Hacking Cover — Sim Findings.md:68` |
| S31 | Search EV | INT+2 attempt ≈ **0.24 Resource + 0.18 gear**, 6% self-Pin | Exact math | one attempt per piece | `Terrain Hacking Cover — Sim Findings.md:66` |
| S32 | Brutal shotgun at close range | +3 & Brutal(+1) = **+4 = 80% wound at Armor 0** — top of the scale | Exact math | `terrain_hacking_sim.py:120-125` | `Terrain Hacking Cover — Sim Findings.md:59` |
| S33 | Hacker shut-out (parked system) | Even-INT does something real only **14%** of the time; triple-gated | Exact math | ⚠ **Supersededment — tests the parked pre-v1 breach system** | `Terrain Hacking Cover — Sim Findings.md:20-27`; note at `:10-11` |
| S34 | Hacking v1 curve | INT+0 at Long range = **10%**; clean band ladder | Exact math | `terrain_hacking_sim.py:71-75` | `Terrain Hacking Cover — Sim Findings.md:66` |
| S35 | Interrupt maths | 1 hacker vs 1 interrupter = **0%**; needs ≥2 successful hacks | Combinatorics | `hacking_sim.py:37-44` | — *(never written up in the vault)* |

### 5.3 Deployables evidence (analytic + Monte-Carlo, **not crew-scale**)

Conditions: exact math against the engine, plus a Monte-Carlo of **one turret vs one advancing rifleman over 6 rounds, N=40,000, seed 20260715** (`deployables_sim.py:141-171`). **This is a 1-vs-1 harness, not a crew battle.**

| # | Measured | Headline | ⚠ Scale | Source |
|:--:|---|---|---|---|
| S36 | Structural conformance | No Damage over +4, no aura over ±3, no range over 24"; every mine's chassis+payload adds up | Assertion check | `Deployables Sim — Findings.md:14`; `deployables_sim.py:62-80` |
| S37 | Deploy gate | INT+0 fumbles an Intricate build **80%**; INT+2 = 40%; INT+4 = 60% success | Exact math | `Deployables Sim — Findings.md:19-23` |
| S38 | Turret efficiency | Baseline = **21-pt Assault-Rifle body → 0.42 w/rd → 0.0200 w/rd/pt**. Autoturret 0.0233 · Sniper 0.0233 · **Burst 0.0300 → repriced to 0.0267** · Blast 0.0200 · Reinforced 0.0187 | ⚠ **1v1** | `Deployables Sim — Findings.md:31-36` |
| S39 | Burst repricing | **16 → 18** — the only sim-driven price change in the game | ⚠ 1v1 | `Deployables Sim — Findings.md:11, 34`; flag logic at `deployables_sim.py:104-105` (>1.4× baseline = HOT) |
| S40 | Turret Monte-Carlo | Turret kills ~**0.6–1.0 bodies** before contact if it survives; MC matched analytic within 1–4 points (73/88/93/63/73%) | ⚠ **1 turret vs 1 rifleman** | `Deployables Sim — Findings.md:38` |
| S41 | Mine lethality | Proximity+Explosion (9 pts) auto-lands a **70%** wound vs unarmoured, no to-hit roll; 60% vs light, 50% vs heavy | Exact math | `Deployables Sim — Findings.md:44-49` |
| S42 | Beacon aura value | **~+10% per affected ally** per ±1 aura | Exact math | `Deployables Sim — Findings.md:52` |

**The baseline is traceable:** 21 pts = 8-point body + 13-point Assault Rifle (`weapon_tests.py:62`: `unit = 8 + w['cost']`). Note the "8" is the *old* `Recruit` = today's **Fighter**.

### 5.4 ⭐ Crew-scale spatial evidence — `engine2d\` (untracked, newest)

**This is a genuinely different engine and the most decision-relevant evidence in the project.** It plays full games on a real 36"×36" board with true line-of-sight, geometric cover, 2.5D elevation, objective scoring and swappable AI.

**Conditions common to all rows:** 3'×3' board; **3 objectives on the centreline** at (6,18),(18,18),(30,18); deploy bands 0–6" and 30–36" (**24" apart**); **11 terrain pieces**, mirror-symmetric (3 objective structures at heavy cover/height 4 + 4 LOS-blocking buildings + 4 light scatter) — `board.py:129-158`. **6 rounds** (`engine.py:110`), **WND 1**, **6 models a side** (`crews.py:14-22`), **1 VP per objective held uncontested per End Phase from round 2** (`engine.py:502-518`), winner = higher VP (`engine.py:576-580`). **Every matchup swaps sides** to cancel board/first-move bias (`run.py:31-44`).

| # | Measured | Headline | Scale | Conditions | Source |
|:--:|---|---|---|---|---|
| S43 | Policy matrix | balanced beats runner **100%**, beats hunter **60/41** | **CREW, objectives** | 2,000 games/cell, sides swapped | `engine2d\README.md:57-64` |
| S44 | Lone-runner degeneracy | 5 fight + 1 pure rusher = **44.7%** vs **49.2%** — more VP (3.3 vs 2.7) but a fighter short | **CREW, objectives** | 6v6, sides swapped | `engine2d\README.md:65` |
| S45 | **Deployables at crew scale** | Autoturret crew (**97 pt**) **50.8%** vs plain crew (**98 pt**) **43.0%**. VP 3.0 vs 2.7; survivors 2.1 vs 2.6 | **CREW, objectives** | 3,000 games, sides swapped. Acceptance band stated in code: *"~50-60% = strong-but-fair. >70% = oppressive (nerf)"* (`run.py:145`) | `engine2d\README.md:67` |
| S46 | Roof camping | Roof **48.9%** vs ground **44.2%**; VP **4.1 vs 2.5** but survivors **1.5 vs 3.2** | **CREW, objectives, 2.5D** | 3,000 games, sides swapped | `engine2d\README.md:69` |
| S47 | Height-cover sensitivity | **Flat across the whole range**: none 49.1% · RAW 48.9% · −1 50.6% · −2 51.0% | **CREW, objectives** | 3,000 games/row | `engine2d\README.md:71` |
| S48 | Roof vs other policies | Roof beats Hunter **55/36**; crushes Runner **100%** | **CREW, objectives** | `run.py:222-224` | `engine2d\README.md:71` |
| S49 | Combat symmetry | Pure-combat Hunter mirror = **50/50** — no side bias in the core loop, LOS, cover or morale | **CREW** | `run.py:81-87` | `engine2d\README.md:74` |
| S50 | Known residual | *Balanced* mirror shows a **~6-point side-0 edge**, isolated to the `keep_moving` Order repositioning an ally onto an objective at the buzzer. Side-swapping cancels it in every comparative test | **CREW** | bisected with Orders off / skills off | `engine2d\README.md:75` |

**Costing-relevant nuance in `engine2d\data.py`:** weapon prices differ from both `crew_sim.py` and the vault. `data.py:67-75` has `crowbar` 7 ✓ (matches Weapons.md), `pistol` 4 ✓, `molotov` 9 ✓, but `rifle` **10** (a bare Standard Ranged, not the 13-point Assault Rifle) and `sledge` **8** at dmg 3 (that is the *Great Axe* profile, not the 14-point Sledgehammer). Equipment (`data.py:77-81`) and deployables (`data.py:85-89`) match the vault exactly.

**`data.py` also encodes three competing stat systems** — the most directly relevant artifact to the rebuild:

| Table | Recruit | Fighter | Champion/Specialist | Leader | Caps |
|---|:--:|:--:|:--:|:--:|---|
| `RANKS` (legacy, `data.py:10-16`) | 0 | 2 | 4 (Specialist) / 7 (Champion) | 6 | none |
| `RANKS_V2` (`data.py:24-29`) | 3 | 5 | 7 | 9 | strict: Fighter **1× T1** |
| `RANKS_V2_GENTLE` (`data.py:31-36`) | 3 | 5 | 7 | 9 | loose: Fighter **2× T1** |

`RANKS_V2_GENTLE` matches the vault (`Unit Design.md:105` — Fighter "up to 2× T1"). `RANKS_V2` is **stricter than the rules**. Both use the rank name **"Champion"** for the 16-point slot, which the vault calls **"Specialist"**.

**A test for exactly the rebuild's central question already exists and has never been reported.** `run.py:166-206` (`statsystem`) pits GENTLE vs STACKED vs SPREAD stat allocations under a hack-to-claim scenario, with the hypothesis written into the code:
> "GENTLE winning both = the sweet spot is a strong primary + one real secondary — not maximal forced spread, and not pure stacking." — `run.py:205-206`

**No results are recorded anywhere.** This is the highest-value cheap run available.

### 5.5 The BLKOUT import battery — built, apparently run, never written up

`engine2d\blkout_test.py` (untracked, 2026-07-23) A/B-tests two proposed mechanics against the locked engine via module-level toggles `engine.DODGE_ON` / `engine.DIST_GATE` (`engine.py:27-28`, both default **False** = pre-import behaviour):

- **DODGE** — a Ready target may Dodge a shot: **opposed AGI vs DEX**, ties to the dodger; a win = miss + reposition out of LOS + Pinned; **ignores cover**. Policy: dodge only when cover < Heavy (`engine.py:202-203`).
- **DIST_GATE** — movement overwatch fires only on a Move > **half MOV** (creeping is safe) (`engine.py:293`).

It measures four things (`blkout_test.py:110-150`): symmetry with both on; lethality (survivors/side) and trigger frequency across `baseline / dist-gate only / dodge only / both`; whether objective-primacy survives (against the stated pre-import baselines of ~100% vs runner and ~60% vs hunter); and a **200,000-trial** dodge micro-sim of P(survive one shot) vs a DEX+2 rifle at dmg 3, by cover × dodge AGI 0/2/4.

**Status: `__pycache__\engine.cpython-313.pyc` is timestamped 2026-07-23 02:10, one minute after `blkout_test.py` was written — so the module was imported and the battery almost certainly ran. No output was saved and no findings note exists.** The vault's Skill Paths does not contain a Dodge skill; the equivalent measured entry in the published table is **Weave** (+13, `Skill Sim — Findings.md:72`), which `skills_sim.py:148, 212` implements under the flag name `dodge`.

**Why this matters for costing:** if Dodge is adopted, **AGI acquires a defensive combat value for the first time** — directly overturning the "AGI is worth zero" premise (N9/S17) that the current "stats are free" position rests on.

### 5.6 What the sims have **never** measured — the evidence gaps

A global points system will have **no evidence at all** for the following. Each is a required new run.

**Stats and skills**
1. **The price of a stat point.** Never measured. Every engine treats stats as free.
2. **The value of the 3 extra stat points** the current ranks grant over what every sim ran (§5.0.2).
3. **Tier caps** — whether forced spread beats stacking. The test exists (`run.py:166-206`) but has never been reported.
4. **136 of the 150 skills.** `skills_sim.py` covers ~14 named skills; `engine2d` wires exactly **3** (Knockback, Stare Down, Keep Moving — `engine2d\README.md:44-48`) and stubs the rest. *"Only ~40 of the ~150 skills resolve to a probability"* (`Skill Sim — Findings.md:11`) — and only ~14 of those 40 were actually run.
5. **Any skill at crew scale.** Every skill number in the project is 1v1, most at WND 3.
6. **Skill *combinations*.** The 14 example role combos at `Skill Paths.md:241-254` have never been tested.

**Gear**
7. **Armour at equal points.** Armour is present in every engine but never A/B'd as a purchase (is 10-point Heavy worth 10 points?).
8. **Med-Kit, Breach Kit, Exploit Suite.** Never measured — the 4/4/8 prices are pure HAND.
9. **The +1 → 4 points exchange rate** implied by the hack-gear ladder. Never validated.
10. **Weapon characteristic probes.** `weapon_tests.py:146-158` defines 11 characteristic probes with an explicit acceptance threshold; **no results were ever published.**

**Deployables**
11. **Mines, traps and beacons in play.** *"Still to wire: mines, traps, beacons, and hacker hijack"* — `engine2d\README.md:81-82`. Only the Autoturret has crew-scale evidence (S45).
12. **Beacon stacking against the 2-aura cap.** Never tested at the table or in a sim.

**Board and scenario**
13. **Terrain density in the spatial engine.** `engine2d`'s board is **fixed at 11 pieces** (`board.py:129-158`); the single most important dial in the game (C10/N8) has only ever been swept in the *abstract* 1D model.
14. **Crew-size asymmetry with objectives.** `engine2d` only ever runs **6v6** (`crews.py:14-22`). The 4-vs-14 result (S1) is 1D-abstract only.
15. **Scenarios other than Take-a-Hold.** One scenario has crew-scale evidence.
16. **Hacking with real terminals at crew scale.** Stubbed in `engine2d` (`engine.py:14-16`); `hacking_sim.py` is pure combinatorics.
17. **Terrain interaction / infrastructure.** Never simulated anywhere.

**Campaign and settlement**
18. **Every structure.** Zero evidence, zero costs.
19. **The +2/Advance and −2/scar valve.** Never simulated.
20. **Any resource economy number.**
21. **Factions.** Do not exist.
22. **Vehicles, drones, the 2051 arsenal, exosuits, directed-energy.** No rules, no costs, no sims.

---

## 6 · Contradictions and duplications

### 6.1 The armour table diverges between two notes — *content*, not cost

| | `Weapons.md:126-132` | `List Building.md:60-65` |
|---|---|---|
| **None** row | present (0 / — / 0) | **absent** |
| **Thick clothing** drawback | "ignore the first Environmental Stress once per game" | "— *(free)*" |
| Improvised / Light / Heavy | −1/3, −1/6, −2/10 | −1/3, −1/6, −2/10 — **identical** |

**The costs agree; the rows and the effect do not.** `List Building` drops the "None" option entirely and reduces Thick clothing's once-per-game Environmental Stress benefit to a blank. The player-facing kit follows `Weapons.md` (`playtest-kit\reference-tables.html:149`). **Weapons.md should be treated as canonical.**

### 6.2 The deployables range is wrong in two places — stated "4–14", actual **3–18**

> "| Deployable | Turret · mine · trap · beacon — full costed catalogue in [[Deployables]] | **4–14** |" — `List Building.md:71`

The real catalogue runs from **Trip Wire at 3** (`Deployables.md:126`) to **Burst Turret at 18** (`Deployables.md:95`). The error is **understated at both ends**, and it has propagated into the player-facing kit: `playtest-kit\reference-tables.html:165` also prints "4–14". Note that Burst was raised 16 → 18 *after* the range was written, so this is partly staleness — but 3 was never 4.

### 6.3 The rank ladder is duplicated across five places

| Location | Form |
|---|---|
| `Unit Design.md:101-106` | full table — **canonical** ("The rank price *is* the stat price", `:118-119`) |
| `List Building.md:34-39` | full table with costs |
| `List Building.md:93` | restated inline as a locked decision |
| `Skill Paths.md:20-25` | table, stat pts + tier caps + skills (no costs) |
| `playtest-kit\reference-tables.html:34` | printed player-facing copy |
| *(plus)* `engine2d\data.py:24-36` | **two** code variants, one of which disagrees (§6.4) |

All the *costs* agree (5/8/16/24). The maintenance risk is real: a ×10 rescale must touch **six** locations.

### 6.4 `RANKS_V2` in code is stricter than the vault, and renames a rank

`engine2d\data.py:27` gives **Fighter** `caps={1: 1}` — one T1 stat. `Unit Design.md:105` grants **"up to 2× T1"**. Only `RANKS_V2_GENTLE` (`data.py:33`) matches the rules. Additionally both V2 tables use **"Champion"** for the 16-point rank that the vault calls **"Specialist"** (`data.py:27, 34`), while the legacy `RANKS` table (`data.py:13-14`) contains *both* names as separate entries with different stat totals.

### 6.5 The headline crew-balance table cannot be reproduced from any tracked script

`Crew Sim — Findings.md:31-41` publishes **eight** archetypes: Firebase, Snipers, Standard, Pyramid, Storm, Horde, Cadre, Mob.

- `crew_sim.py:329-337` defines **seven** lists: Cadre (pure DEX), Cadre (DEX/STR), Standard, Fighter horde (9 STR), Fighter horde (9 NRV), Pyramid mob (11), Recruit horde (14).
- `weapon_tests.py:103-105` defines **nine**: Cadre, Firebase, Bleeders, Cleavers, Standard, Firebugs, Horde, Pyramid, Mob.

**"Snipers" and "Storm" appear in neither.** The note itself explains why — the doctrine layer was removed (`Crew Sim — Findings.md:28`) — but the consequence is that **the single most-cited balance result in the project is archival and not re-runnable.** It should be regenerated before any rescale is validated against it.

### 6.6 The density labels in the findings note don't match the script

| | Findings note (`Crew Sim — Findings.md:47-49`) | `weapon_tests.py:118-120` | `crew_sim.py:43-47` |
|---|---|---|---|
| Sparse | "Sparse **30%** (illegal)" | `0.20` "sparse 20%" | `open` = 0.10 |
| Legal | "Legal **42%**" | `0.42` ✓ | `medium` = 0.30 |
| Crowded | "Crowded **55%**" | `0.60` "crowded 60%" | `dense` = 0.55 |

The legal figure agrees; the sparse and crowded labels are drawn from a third parameterisation. The note appears to have mixed `crew_sim.py`'s presets (30/55) with `weapon_tests.py`'s run values (20/60).

### 6.7 `Damage.md` contradicts itself on multi-wound units

`Damage.md:23` (in the "should nail down" scaffold) still says *"multi-wound leaders/champions"*, while `Damage.md:64` rules definitively: *"**Every unit has WND 1**… The *only* way to have more is a specific **skill**."* Line 23 is stale scaffolding.

### 6.8 The harness is internally inconsistent about rank names

`crew_sim.py:59` uses the new names (Recruit/Fighter/Specialist/Leader); `weapon_sim.py:39, 97-98` and all of `weapon_tests.py:26-29` still use the old (Rabble/Recruit/Specialist/Leader); `crew_calibrate.py:99` uses a string that has silently changed meaning (§5.0.1); `engine2d\data.py` uses the new names plus "Champion". **Four scripts, three conventions.**

### 6.9 Three skills are out-competed by a paid characteristic
Already flagged in-vault but unresolved (`Weapons.md:186-190`): **Long Barrel** is called *"dead"*; **Knockback** and **Ghost Blade** are *"thin"*. A free skill losing to a 2–6 point characteristic is a costing signal, not just a design one.

### 6.10 ⚠ **Crew size: "legal maximum 11" vs a 14-model horde used throughout the validation**

| Claim | Source |
|---|---|
| "at 100 points the **legal maximum is 11 fighters**" | `List Building.md:46` |
| "List Building lets crews run from **4 to 14 models**" | `Initiative & Activation.md:84` |
| "A 4-model elite crew beats a **14-model horde** 81% of the time on a sparse board" | `Terrain.md:133` |
| "took a **14-model horde** to 93–96% win rate at every terrain density" | `Morale.md:87` |
| "the **14-model Recruit horde** land within three points of each other" | `Crew Sim — Findings.md:70` |

**Resolved by the code, and the answer is bad:** `crew_sim.py:325` comments the 14-model list *"needs The Mob doctrine (Recruit w/o Fighters)"*, `weapon_tests.py:99` says the same of its 13-model Mob, and `weapon_tests.py:112` **explicitly whitelists** its pyramid failure. Doctrines were removed from the ruleset (`Crew Sim — Findings.md:28`, `RULES-AUDIT.md:5, :43`).

**So the swarm end of the elite-vs-swarm balance case — including the headline 66-point terrain swing and the "morale cascade is load-bearing" result — was measured with a list that is now illegal.** This is the highest-priority contradiction in the audit: it does not necessarily invalidate the *direction* of those findings, but it does mean the legal 11-model pyramid has never been measured against a 4-model cadre at the extremes.

### 6.11 Resource count: locked at **4**, still written as **5** in the newer plan
- Locked: *"**Goods + Materials + Power + Water**"* — `SETTLEMENT-DESIGN-QUESTIONS.md:130` (Fork 8, locked 2026-07-20), with `:188` explicitly offering to "revise the '~5' down". Confirmed at `Settlement.md:26`, `Components.md:34`, `RULES-INTERVIEW-PLAN.md:8`.
- Still says five: *"1 faction, 10 units, 10 buildings, **5 resources**, 3 scenarios"* — `RULES-COMPLETION-PLAN.md:73` (dated 2026-07-23, i.e. **after** the lock).
- And `Settlement.md:74-82`, the actual resource prose, defines only **Goods, Materials, Power** — **Water is never mentioned there at all**, despite `Settlement.md:26` listing it.
- Power's model also diverges: *"Power will be gained by **building generators**"* (`Settlement.md:82`) vs *"Power (Reactor **capacity**, not gathered)"* (`RULES-INTERVIEW-PLAN.md:8`).

### 6.12 Currency naming: **Goods** vs **Cash**
`SETTLEMENT-DESIGN-QUESTIONS.md` uses **Goods** throughout (`:18, :51, :120, :130, :211-218`), and `Structures.md:36` explicitly **reverted** the rename: *"**Currency stays Goods** — the Cash rename (07-24) is reverted."* But `RULES-INTERVIEW-PLAN.md:8` still reads *"**Cash** (currency, formerly 'Goods')"* and uses Cash at `:20, :31, :43, :49, :52, :103, :104`. `Rules System — Master Roadmap.md:254` and `Components.md:44` still say Goods/Materials. **Any costing table must pick one name; the vault's ruling is Goods.**

### 6.13 Two different sets of five factions
- `Factions.md:34-52` — **Civilians · First Enforcers · Laborers · Lost Batallion · The HACKERS**
- `SETTING-TECH-2051.md:426-443` — **The Remnant · The Scavengers · The Swarm · The Ghosts · The Foundry**

No note reconciles them. Both are uncosted. Alpha ships **1** faction (`RULES-COMPLETION-PLAN.md:73`, `SETTLEMENT-DESIGN-QUESTIONS.md:125`) while release targets **5** (`RULES-INTERVIEW-PLAN.md:5`).

### 6.14 Structure count: **25** catalogued vs **"5 to 10"** answered vs **~10** for alpha
- 25: `Structures.md:245`, `Rules System — Master Roadmap.md:251`, `Components.md:39`, `Settlement.md:29`
- *"There should be **5 to 10** structures"* — `Interviews — Completing the Rules System.md:36`
- ~10 for alpha: `Settlement.md:26`, `Final Alpha.md:19`, `RULES-COMPLETION-PLAN.md:73`

`Structures.md:39` claims the conflict was ruled — *"the '5 to 10' answer was scoped to **release count**, a different question"* — but the interview note was never updated, so the raw answer still reads as a contradiction. **Materially: you may be about to price 25 things the design intent says should be 5–10.**

### 6.15 Category count: **5** vs **7**
`Structures.md:39` and `Rules System — Master Roadmap.md:251` lock **Sustain / Convert / Operate / Recover / Defend** (5). `Interviews — Completing the Rules System.md:32` answers with **seven** (Scavenger, Processor, Crafter, systems, utility, defenses, housing) and the checkbox is **still unticked**.

### 6.16 ⚠ The core tenet points the opposite way to atomic costing
> "**Keep list-building minimal — let terrain + base-building shine (your flagged BIG RULE). Depth lives in the settlement layer, not in point-buy.**" — `SETTLEMENT-DESIGN-QUESTIONS.md:24`, originating at `Ideas Inbox.md:34`
> "**Tactical play on the battlefield must outweigh pre-game optimization.**" — `Game Vision.md:78`

Against this stand: a 24-characteristic weapon builder with refunding drawbacks, a **150-skill** catalogue (which `RULES-AUDIT.md:44` recommends *"**curate** down to a starter set"*), a 25-structure catalogue, and a 62-item 2051 arsenal. **A global atomic points system makes list-building deeper, which is the thing the flagged BIG RULE asks to keep shallow.** This tension is not resolved anywhere and should be settled explicitly before the rebuild, not discovered during it.

### 6.17 The modifier cap is stated as universal but is only scoped to conditions
- Universal claim: *"**Modifier cap ±3** — never stack endless modifiers"* — `Out of Scope.md:39`
- Actual rule: *"However many **conditions** a unit carries, the total modifier on any single roll never exceeds −3 (or +3)"* — `Conditions.md:46`
- And the engine expects worse: the core-test probability table has a *"**−4 or less**"* row (`Rules Ledger\core-000 Core Test.md:43`), which is reachable as Hidden −3 (`Terrain.md:56`) + Shaken −1 (`Morale.md:48`) — precisely because **cover is a separate axis** (C6).

So there are really **two** caps: a ±3 cap on conditions, and cover stacking outside it. Pricing must respect both separately.

### 6.18 The 2051 hooks reach for three banned mechanics
- **Saves**, five times (`SETTING-TECH-2051.md:148, :154, :160, :178, :328`) — against *"no separate save"* (`BLKOUT-RULES-ANALYSIS.md:137, :324`)
- **Ignore-cover** (`:40`, `:166`) — *"Seeking↔ignore-cover which Settlements deliberately **bans**"* (`BLKOUT-RULES-ANALYSIS.md:239`); reinforced by the cut of **Crushing**, *"**Cover never touches the Injury roll.** That is the load-bearing line of the entire engine"* (`Weapons.md:179`)
- **Re-rolls** (`:346`, `:410`) — *"introduces re-rolls, a dice mechanic that exists nowhere in Settlements"* (`Weapons.md:177`)

Four kit families therefore need re-expressing as Injury-roll modifiers inside the ±3 cap before they can be costed at all.

### 6.19 Objective claiming: hack-to-claim vs bodies-only
`Scenarios.md:96, :99` — a terminal is claimed by **INT 7+** in base contact and *"you can't score a terminal you haven't hacked"*. `Board Representation.md:38` describes a different version: *"held by **bodies within 3"** … **no claim token yet**. **If/when the hack-to-claim hook returns**…"*. The 2D engine implements **both**, switchable (`engine2d\engine.py:126, :490, :507`). **This directly determines whether INT has objective value — i.e. whether INT can be priced at all.**

### 6.20 Interrupt: does it cost a Ready token?
- `Initiative & Activation.md:68` lists Interrupt among the **Reaction options** (Ready + reach)
- `Hacking.md:74` — *"It costs **no Ready token**; its price is the **Overload**"*
- `Rules Ledger\core-005 Activation order.md:21` — *"interrupt Interact (a network hack — **no LOS/Ready**)"*

The ledger and Hacking agree; Initiative & Activation does not. **Action-economy costing depends on this.**

### 6.21 Smaller inconsistencies with costing relevance

| # | Contradiction | Sources |
|:--:|---|---|
| a | **Base sizes** — 25/32/50mm vs 28/40–50mm, with the roadmap ticking the item using the value the note contradicts | `Core Game Format.md:27` vs `:61`; `Rules System — Master Roadmap.md:70` |
| b | **Setting year and premise** — 2050 post-alien-invasion vs 2051 grounded near-future vs modern civil war, while the scope guard bans aliens outright | `Narrative.md:30-32` vs `RULES-INTERVIEW-PLAN.md` (2051) vs `Game Vision.md:35` vs `Out of Scope.md:24` |
| c | **Tenet numbering** doesn't match between notes; already self-flagged as *"**two conflicting lists exist** … Reconcile into one canonical set before locking"* | `Game Vision.md:44-57` vs `Out of Scope.md:20-23`; `Rules System — Master Roadmap.md:58` |
| d | **Duplicate `build_order: 17`** — Scenarios and Economy claim the same slot, making the Open Decisions dataview sort non-deterministic | `Scenarios.md:5` · `Economy.md:6` |
| e | **`Components.md` dependency contradicts itself** — `depends_on: ["Structures"]` vs "Depends on: —" | `Components.md:7` vs `:14` |
| f | **`status: Not Started` notes containing drafted content** — Narrative, Factions and Components all have substantive bodies, so they mis-bucket in the dashboards | `Narrative.md:5, :30-33` · `Factions.md:5, :32-52` · `Components.md:5, :29-44` |
| g | **`Damage.md:23`** still says "multi-wound leaders/champions" against `:64` "Every unit has WND 1" *(also §6.7)* | `Damage.md:23` vs `:64` |
| h | **Hacking range bands** — Ideas Inbox's origin text says "3 × 12" bands" (36" reach); the shipped rule is four bands capped at 24" | `Ideas Inbox.md:28` vs `Infrastructure.md:100` |
| i | **The stat-scale justification in Ideas Inbox assumes armour modifies the hit roll**, which the engine forbids — so the original argument for the stat scale no longer holds as written | `Ideas Inbox.md:44` vs `Rules Engine.md:118`, `Rules Ledger\core-000…:46` |
| j | **Fork 7's "owned scenery" is listed as a *rejected* candidate but is what got locked** (fenced by the settlement sheet) | `SETTLEMENT-DESIGN-QUESTIONS.md:185` vs `:132` |
| k | **Settlement deploy-rights are stated as settled in the rules but still open in the interview**, and the **slot/aura caps** half has never been decided | `Terrain Interaction.md:136-137` vs `Interviews….md:124-125` |
| l | **`RULES-INTERVIEW-PLAN.md:64`** still asks for the grid scale that `SETTLEMENT-DESIGN-QUESTIONS.md:223` marks RESOLVED (12"×36" on a 1" grid) | as cited |
| m | **BLKOUT-RULES-ANALYSIS body text recommends Return Fire as "steal #1"** while its own dated footnote records it as **cut** | `BLKOUT-RULES-ANALYSIS.md:391, :399` vs `:412` |
| n | **CRITICAL, already logged: Disengage cost.** The ledger card and roadmap say **both slots**; the resolved rule is **Move slot only**. *"A rulebook built from the ledger would ship the **rejected** rule."* | `RULES-COMPLETION-PLAN.md:31`; `Movement.md:67-73` vs `Rules Ledger\core-001 Movement.md:22` |
| o | **"Dodge" now names two different mechanics** — the imported BLKOUT reaction (opposed AGI vs DEX) and the pre-existing melee −1 skill | `RULES-COMPLETION-PLAN.md:34` |
| p | **Ready token clearing** — Board Representation clears Ready every End Phase, but Ready **persists across rounds**; the play-sheet *"would **silently break the validated Ready-banking balance**"* | `RULES-COMPLETION-PLAN.md:35` |

---

## 6A · The eight locked design forks (2026-07-20)

Recorded because each one constrains the points architecture. Source: `SETTLEMENT-DESIGN-QUESTIONS.md:118-141`. The derived spine (`:120`):
> "***Ownership and fielding are orthogonal.*** Goods/Materials establish what you **own** (persistent, campaign layer); crew-points establish what you **field** (per battle)."

| Fork | Question | **LOCKED TO** | Line |
|:--:|---|---|---|
| **1** | Battle budget — same pool or separate? | **HYBRID (build then deploy).** Structures built with Materials off-table; deploying a piece costs **crew-points, competing with bodies**. **Points stay the sole battle gate.** Settlement pieces occupy density slots *within* 9–12 (replace neutral terrain, never stack). Ownership buys availability + auto-deploy, **not** free board power. | `:122` |
| **2** | Does the settlement sit on top of, or replace, point-buy? | **SIT ON TOP** of the sim-validated **100-pt** point-buy. Roster = the pool; points = the gate. | `:127` |
| **3** | Structural-damage model | **BINARY + SABOTAGE.** No structure HP. Functional \| Disabled only. Repair = flat Materials cost. Still no wall/cover HP. | `:123` |
| **4** | Bounded vs endless meta; can a settlement be razed? | **ENDLESS DEFAULT + OPTIONAL SEASON.** Base damaged, never razed; opt-in season layer permits razing, always with a guaranteed comeback. | `:124` |
| **5** | Roster model | **ONE ROSTER + PER-CYCLE ASSIGNMENT.** Battle / Work / Mission; sending one out means it can't fight (**opportunity cost**). One housing pool. | `:131` |
| **6** | Alpha meta scope | **LOCAL SLICE + CAPTURE LOOP.** 2-settlement frame. Global map, alliances, faction-war **PARKED**. Factions → 1. | `:125` |
| **7** | Physical board representation | **OWNED SCENERY AS FLAGSHIP LOOK, *FENCED*.** The settlement sheet is the mechanical source of truth; Cover/Movement/Tags declared at setup from the sheet, **never inferred from the model**. Owning better terrain changes the look, **never what the board does**. | `:132` |
| **8** | Resource roster | **FOUR RESOURCES — Goods + Materials + Power + Water.** Water = per-head population upkeep, soft-caps crew count, raidable. Power = output-vs-draw flow, **not a banked currency**. | `:130` |

**Four supplementary locks (round 3):** Location ⟂ Faction are orthogonal pre-game choices (`:136`) · Capture is a post-battle Fate hook, no new in-battle action (`:137`) · Growth is post-battle Advances only — the downtime "train" action was **cut to protect the +2/Advance valve** (`:138`) · BUILDER is an emergent **role**, not a new rank, with **one on-table build per game** (`:139`).

---

## 6B · The BLKOUT import — what changed, and what it does to costs

Status is authoritative and dated: *"**Drafted into the Obsidian vault (`Rules System/`), not just proposed.**"* — `BLKOUT-RULES-ANALYSIS.md:412`

| Change | Outcome | Effect on costing |
|---|---|---|
| **Dodge** (was BLKOUT's "Juke") | **ADOPTED** — *"an **opposed AGI vs DEX** evasion (win = shot misses + move full MOV out of LOS, then Pinned), a **resourced exception** to the 'can't dodge a bullet' tenet"* (`:412`) | ⚠ **Systemic re-pricing, not a line item.** It gives **AGI a defensive combat value for the first time** and makes **DEX** matter on the shooter's side, while reducing the value of raw shooting. It directly undermines the "AGI is worth zero in combat, so the board must price it" premise (N9/S17) that "stats are free" rests on. **Whether Dodge is free/universal or must be bought is uncosted.** Implemented behind `engine.DODGE_ON` (`engine2d\engine.py:27`) and measured by `blkout_test.py` — **results never written up** (§5.5). |
| **Distance-gated Snap Shot / Overwatch** | **ADOPTED** — *"only a Move > half MOV ending in enemy LOS triggers it"* (`:412`); propagation verified clean (`RULES-COMPLETION-PLAN.md:44`) | ⚠ **Devalues Ready/overwatch builds** (creeping dodges them) and **raises the value of MOV**, since half-MOV is now a defensive distance. No new points cost. See N22. |
| **Simultaneous Return Fire** | **CUT** — *"sequential shoot-back already exists as Settlements' **Snap Shot** … the simultaneous version was **rejected as too swingy / anti-shooter**"* (`:412`) | No new cost. Had it landed it would have re-priced every ranged weapon by adding attacker risk. |
| **Stress / suppression** | **KEPT unchanged** — *"Keep yours — it's your edge … Your current Stress design is actually already lean … **Guard it.**"* (`:390, :408`) | A pricing input rather than a cost: any unit **immune** to Stress (robots, `SETTING-TECH-2051.md:252, :443`) is being priced against a live morale system. |
| **Player-built weapons** | **KEPT** — *"more strategic expression at list-building than BLKOUT offers"* (`:393`); shape confirmed at `RULES-AUDIT.md:42` — *"buy a class, add trait characteristics (each **costs points + a slot**), optional **drawbacks refund points**"* | **This is the atomic engine the rebuild generalises.** |
| **Cover math (−1/−2)** | **KEPT** — *"fits your single-die engine and is less swingy"* (`:392`) | No change. |
| **One playstyle-defining rule per faction** | Recommended (`:402`), **deferred** — *"Factions still deferred"* (`:412`) | All faction rules uncosted. The lock at `SETTLEMENT-DESIGN-QUESTIONS.md:136` requires *"faction-wide buffs **AND** nerfs"* — a net-zero design intent rather than a price. |
| **"One Action = one test = one clear effect"** | Guidance (`:403`) — *"Your **Hacking/Deployables/Terrain-Interaction risk becoming pace-killing subsystems**"* | Constrains how the 2051 kit may be mechanised, and therefore priced. |

---

## 6C · Prior art already in the repo — `ff.py`

**Not part of the brief, not authored by this audit, and worth more to the rebuild than anything else in the project.**

`D:\AI-Workstation\Antigravity\apps\Settlements\ff.py` — **2,337 lines, untracked, last modified 2026-07-27 02:09** — is a **complete, working atomic points-costing engine** for a wargame. It is not a Settlements file (the keyword set — `jedi`, `sith`, `duellist`, `quality`, `defense`, `tough` — indicates a One Page Rules-family / Star Wars skirmish derivative), but it is a **reference implementation of exactly the system Settlements is trying to build.**

**Architecture** (`ff.py:9, :495, :1308, :1371`): four classes — `Weapon`, `Model`, `ModelList`, `UpgradeList`. Every trait is a keyword argument on the constructor; every keyword has a matching cost dictionary.

**The three structural lessons it already encodes — each one answers a problem in §4 of this audit:**

**1 · Stat costs are a non-linear lookup, not a multiplier.**
```
self.quality_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
self.defense_cost_dict = {6: 2, 5: 4, 4: 6, 3: 8, 2: 12}
```
`ff.py:79-80`, repeated at `:609-610`. The ladder runs 2 → 4 → 6 → 8 → **12** — linear for four steps, then a **50% jump** at the top. That is precisely the shape N3 says Settlements needs (the +6 stat that only pays off against modifiers). It also shows the answer to §8 Q1: **a per-value dictionary, not a per-point price.**

**2 · Output-scaling traits MULTIPLY; flat effects ADD.**
```
primary_cost = (
    effective_quality_cost
    * range_multiplier * attacks_multiplier * pierce_multiplier
    * ammo_multiplier  * blast_multiplier   * deadly_multiplier
    … 17 multipliers in total …
    + fixed_cost_reduction + suppressive_cost_increase
    + ion_cost_increase + immobilise_cost_increase
    + disorient_cost_increase + melee_cost_reduction
)
```
`ff.py:252-276`. **This is the direct answer to N4, N5 and N6.** Settlements currently adds every weapon characteristic (`Weapons.md:24-102`) — which is why *Rapid* had to be **cut** rather than priced (`Weapons.md:175`) and why the *Burst Turret* needed a hand repricing (`Deployables Sim — Findings.md:34`). A multiplicative term for anything that multiplies output (extra attacks, blast, range) prices those correctly by construction.

**3 · Sub-linear scaling is applied explicitly where the effect saturates.**
```
effective_quality_cost = np.sqrt(self.quality_cost_dict[quality]) * 2.2
```
`ff.py:138-139`. A square root with a tuned coefficient — the standard treatment for a stat whose marginal value decays. Compare N3 (the 90% ceiling) and N24 (the ±3 cap).

**Also present and directly transferable:**
- **Per-trait cost dictionaries** including **negative costs** for drawbacks — `immobile_cost_dict = {False: 0, True: -3}` (`ff.py:643`), the same shape as Settlements' refunding drawbacks (`Weapons.md:107-113`).
- **Conditional/threshold traits priced by lookup table** — `cover_cost_dict` (`:613`), `hunter_cost_dict` (`:637`).
- **Interaction terms** — e.g. `torrent_multiplier = 3 * (10 / effective_quality_cost)` (`ff.py:158`), where a trait's price *depends on the stat it is attached to*. This is the mechanism N16 (grapple value scales with target cost) and N28 (enablers) require.
- **Combinatorial evaluation of multi-mode weapons** — `combinations(weapon_indices, 1)` over secondary fire modes (`ff.py:279-290`), i.e. the cost of an option set is solved, not assumed.

**Caveats, stated plainly:** I read its structure and its cost formula, not all 2,337 lines. It is **untracked in git**, has **no README or docstring**, uses `pandas`/`numpy` (neither is a current Settlements dependency), and its stat scale is a **roll-under 2–6 quality** system, not Settlements' `1d10 + Stat vs 7+`. **The numbers do not transfer; the architecture does.**

> **Recommendation:** before designing the Settlements costing formula from scratch, read `ff.py:135-290` (`Weapon.calculate_cost`) end to end. It is a solved version of the multiplicative/additive split that §4 of this audit says Settlements needs, and it took someone a long time to write.

---

## 7 · Design tenets, bookkeeping limits and aesthetic requirements

Things a global points system must not break, gathered from across the vault.

| # | Requirement | Source |
|:--:|---|---|
| T1 | **The stat scale itself is the display format.** Stats run **−1…+6** on a 2-point tier cadence (`Unit Design.md:78-89, :110`), and *"**A rule must fit its reference card**"* (`Out of Scope.md:42`). ⚠ **However — no note anywhere states that stats must *display* as small integers if internally rescaled.** I searched the full vault and all repo docs; that requirement is not written down. It is a real constraint if the designer holds it, but it is currently **undocumented**, and the two notes that would own it (`Components.md`, `Board Representation.md`) do not contain it. | `Unit Design.md:78-89`; `Out of Scope.md:42` |
| T2 | **One mechanic.** `1d10 + Stat + mods vs 7+`. No second dice mechanic, no re-rolls, no raised target numbers. | `Weapons.md:177`, `Skill Paths.md:48`, `Damage.md:30` |
| T3 | **The three-lever contract.** "Stats decide if you land it · Weapons decide how bad it is · Skills decide what else happens." A weapon must **never** grant an effect a skill grants. | `Weapons.md:11`, `Skill Paths.md:8` |
| T4 | **Skills are verbs, not numbers.** "A skill is a **verb or a conditional exception**… **not** a flat stat increase (those are the least interesting, so we avoid them)." | `Skill Paths.md:8` |
| T5 | **Weapons are built, not bought.** Class + characteristics, named after your miniature. | `Weapons.md:8` |
| T6 | **Conditions are applied, never redefined.** Every condition lives in `Conditions.md`. | `Weapons.md:12`, `Deployables.md:37`, `Skill Paths.md:50` |
| T7 | **A hit does one thing.** Wound *or* payload, never both. | `Weapons.md:13` |
| T8 | **Structures are binary** — Functional or Disabled. No structure HP, no collapse tracking. An explicit bookkeeping limit. | `Structures.md:50` |
| T9 | **Every structure must earn its slot.** "No flat `+1`." | `Structures.md:46` |
| T10 | **Every structure is a real object on the board.** "If it can't be placed and described, it isn't a structure — it's a bonus." | `Structures.md:47` |
| T11 | **Nothing interactive is invisible.** Every Tag must be physically marked on the table. | `Structures.md:118-119` |
| T12 | **Close enough is correct** on terrain sizes — within 2" for Buildings, 1" for Plant/Stations. "Nobody measures your scenery." | `Structures.md:108-112` |
| T13 | **No pay-to-win / collection-to-win.** "A bigger model budget must not beat better play." | `Out of Scope.md:23` |
| T14 | **Modifier cap ±3 — "never stack endless modifiers."** | `Out of Scope.md:39` |
| T15 | **The board is the great equaliser** (Tenet 1) — terrain and scenario carry the balance, not points. | `Out of Scope.md:23`, `List Building.md:90` |
| T16 | **Ownership and fielding are orthogonal.** "Goods/Materials buy what you own, points gate what you field." | `List Building.md:49` |
| T17 | **Scarcity produces divergence; tech trees produce convergence.** No build prerequisites. | `Structures.md:211` |
| T18 | **Depth belongs in the settlement layer, not point-buy** — the flagged "BIG RULE". | `SETTLEMENT-DESIGN-QUESTIONS.md:24`; `Ideas Inbox.md:34` |
| T19 | **Tactical play must outweigh pre-game optimisation.** *"Not a stat-driven optimization game."* | `Game Vision.md:77-78` |
| T20 | **Every new status token or mid-activation subsystem is a tax** against the fast-paced goal. *"Guard it."* | `BLKOUT-RULES-ANALYSIS.md:408` |
| T21 | **One Action = one test = one clear effect.** If a system needs its own mini-phase, it's fighting the pace goal. | `BLKOUT-RULES-ANALYSIS.md:403` |
| T22 | **Lightweight bookkeeping** — the designer explicitly resists tracking granular damage; upkeep should be "one number"; the territory ledger is "paper-first". | `SETTLEMENT-DESIGN-QUESTIONS.md:28, :206, :261` |
| T23 | **No hit-location tables, ammo-counting, or encumbrance spreadsheets.** | `Out of Scope.md:41` |
| T24 | **A player with no scenery at all must be able to build a full settlement from the printed sheet** — this is what keeps the no-collection-to-win tenet honest. | `Components.md:37` |
| T25 | **Never invent a new condition** in terrain or infrastructure; reuse the existing set. | `Infrastructure.md:73`; `Terrain.md:84` |
| T26 | **Cover never touches the Injury roll** — *"the load-bearing line of the entire engine."* | `Weapons.md:179` |
| T27 | **Setting-tone guard** — how far can structures push (grids, terminals, turrets) before it stops feeling like a fought-over suburb? Plus *"grounded, not triumphalist"* and *"plausible extrapolation, not space opera"*. | `SETTLEMENT-DESIGN-QUESTIONS.md:284`; `RULES-INTERVIEW-PLAN.md:152`; `SETTING-TECH-2051.md:3` |
| T28 | **Don't finalise a component until its system is Locked**; a chapter can only be written from a Locked phase. | `RULES-COMPLETION-PLAN.md:83-84` |

> [!warning] Two things the brief assumed that are **not** in any source
> 1. **No card-display / number-formatting rule exists.** Searched the full vault (57 notes + 13 ledger cards), all six repo docs and the playtest kit. The aesthetic constraints that do exist are about **tone** and **token load**, not about how digits print. See T1.
> 2. **No document mentions the ×10 rescale.** There is no reference anywhere to a 1000-point budget or a "global atomic points system". Every figure in the project is on the 100-pt / 5-8-16-24 scale. **The rebuild is not yet recorded in the rules.**

---

## 8 · Open questions — genuinely undecided

**Costing structure**
1. Should stats be **bought atomically**, or stay bundled in the rank price? The vault's current position is that pricing them is "double-counting" (`List Building.md:22`) — the rebuild inverts this, and there is **no evidence either way**.
2. If stats are bought, what happens to the **tier caps**? They currently force spread for free. Under atomic pricing, spread could be priced instead of mandated — the GENTLE/SPREAD/STACKED test (`run.py:166-206`) was built to answer this and has never been run.
3. Do **ranks survive** as purchasable bundles, or become emergent from the stat spend? If emergent, the pyramid (C11), the Orders economy and the weapon gates (C19) all lose their anchor.
4. Should the **+2/Advance, −2/scar** valve scale ×10 to ±20, or is its *ratio* to the crew budget the real design constant? (`List Building.md:77`)
5. Does the **±3 cap** get a pricing rule (declining marginal cost) or stay a hard wall?

**Skills**
6. How are **150 free skills** priced — individually (150 numbers), by tier (3 numbers), or do they stay free with the stat as the payment?
7. **Tough** and **Fleet** are the only levers on WND and MOV and are currently free. What do +1 WND and +2" MOV cost in a game built on WND 1?
8. Do the three out-competed skills (`Weapons.md:186-190`) get rewritten, repriced, or cut?

**Explicitly open in the vault**
9. Budget 100 and the 5/8/16/24 ladder are "**validated in sim, not yet at a table**" — `List Building.md:94`
10. "**NRV is close to a dead stat at Fighter level**; it earns its keep only through Bravery *skills*." — `List Building.md:95`
11. **Melee-elite viability** is "a live balance question for the table" now that the Storm doctrine is gone — `Crew Sim — Findings.md:68`
12. Whether the **Burst Turret**'s two shots and the **Revive Beacon** survive contact with a table — `Deployables.md:160-161`
13. Whether **turret auto-fire** (one free Reaction shot/round) is oppressive — `Deployables.md:162`
14. Whether the **both-slots + two-auras-per-model** brakes actually bite — `Deployables.md:163`
15. The **hack-modifier ladder** values — "set… once first playtests show how reliable an unmodified hack feels" — `Hacking.md:116`
16. Whether **Interrupt** is too strong as a hard counter — `Hacking.md:114`

**Settlement layer (all of `Structures.md:363-378`)**
17. Board size confirmation (3'×3' recommended)
18. **Build cost in Materials per structure**
19. All **storage numbers** — HQ base cap, gatherer buffer, Storehouse, Vault, Equipment Shed/Armory, Water per tank
20. **"Is owned gear *also* points-costed to field (two-gate), or does ownership replace the points cost?"** — `Structures.md:366`. **This one directly determines whether the crew points system and the settlement economy are one system or two.**
21. What a holed Water tank costs
22. HQ tier costs and the dispatch-slot increment
23. How much a successful raider actually takes
24. **Founding Goods budget and per-structure founding price**
25. **Upgrade tier costs**, including the Station → Building space cost
26. **Groundworks cost**
27. **Repair cost** — flat Materials per structure, or one flat rate
28. Med-bay `+X` on the Fate roll
29. Mess Hall Stress value
30. Recruiting Board effect — blocked on hiring rules that don't exist
31. Whether all 25 structures are available at founding or gated behind research

**The architectural fork — the biggest one, and it is explicitly unresolved**
32. > "**We need to decide how settlements are pointed when used in battles**…are they a **separate points limit** or **incorporated into a single points limit** allowing players to choose if they want more terrain or more crew… ***This will need to be tested***" — `Ideas Inbox.md:54`

    Fork 1 (`SETTLEMENT-DESIGN-QUESTIONS.md:122`) locks the *hybrid* answer — build with Materials, deploy for crew-points — but the underlying "one pool or two" question is still flagged as needing a test, and it decides whether the global atomic system has one budget or two.
33. **Cash hire-price per rank** — *"separate scale from the 5/8/16/24 battle points, or reuse them?"* (`Interviews — Completing the Rules System.md:78-79`, **`Answer:` blank**). `SETTLEMENT-DESIGN-QUESTIONS.md:215` argues they must be separate: *"don't conflate balance with economy pacing."*

**Economy values that do not exist**
34. **Inflow base numbers** and what objectives/deeds pay — `Interviews….md:59` (unanswered)
35. **Water per-head upkeep rate** — `Interviews….md:61` (unanswered)
36. **Storage caps and the escalating tier costs** — `Interviews….md:63` (unanswered)
37. **Power: each structure draws N, the Reactor supplies M** — `Interviews….md:65` (unanswered). The only anchor is Generator **+3** vs a starting draw of exactly **3** (`Structures.md:154-156`).
38. **Starting Goods/Materials amounts** — `Settlement.md:46` (*"we will need to lock this in together"*)
39. **Housing base headcount (~10?) and the Bunkhouse increment** — `Interviews….md:80` (unanswered)
40. **Ransom / prisoner economy**, and the Cash-Materials cost of scar healing — `Interviews….md:161-167` (unanswered)
41. **Advance award rates** and the **scar effect tables** — `Rules System — Master Roadmap.md:279-280` (unticked); Fate spread is *"a first-draft"* (`Campaign.md:53`)
42. **The proposed "repair costs half the structure's initial cost" rule** — explicitly tentative (*"or whatever"*) and uncosted — `Settlement.md:88`

**Consistency questions that must be answered before pricing**
43. ⚠ **Is the legal crew maximum 11 or 14?** (§6.10). The elite-vs-swarm validation used a doctrine-dependent 14-model list. **Answer this first — it is the foundation of every current price.**
44. **Which five factions?** Two disjoint sets exist (§6.13). **Alpha needs 1, release targets 5.**
45. **25 structures or 5–10?** (§6.14)
46. **Four resources or five?** (§6.11) — and is Power gathered or a flow?
47. **Goods or Cash?** (§6.12) — `Structures.md:36` reverts to Goods; the interview plan still says Cash.
48. **Hack-to-claim or bodies-in-area?** (§6.19) — this decides whether INT has objective value and therefore whether INT is priceable.
49. **Does Interrupt cost a Ready token?** (§6.20)
50. **Slot / aura caps on settlement deploy-rights** — never decided anywhere (`Interviews….md:124-125`)

**Evidence**
51. Does the abstract 1D sim's "combat specialists dominate" (S17) or the spatial engine's "killing isn't the win" (S43) govern the points system? **They disagree, and the disagreement is about scenario, not maths.**
52. Now that **Dodge** is drafted in, AGI gains defensive combat value for the first time — does the "board prices utility stats" thesis still hold? `blkout_test.py` was built to answer this and its results were never recorded.
53. The `engine2d` **~6-point side-0 residual** (`engine2d\README.md:75`) is localized but unresolved.
54. Every number in the project is sim-derived. *"**the table is the authority**"* (`RULES-COMPLETION-PLAN.md:63`) — and no table playtest has happened (`Rules System — Master Roadmap.md:205`).

---

## 9 · Recommended reading order, and what to do first

**Read in this order:**
1. **§1** — the nine constraints.
2. **§6.10** — the 11-vs-14 model legality problem. Everything currently priced rests on it.
3. **§4** — the non-linearity register. This is where a naive atomic system will break.
4. **§5.0** — the harness caveats (the uncommitted rename, the uniform −3 stat gap, stats-are-free-in-every-engine) before trusting any number in §5.
5. **§5.2 header** — the 1v1 warning, and why it has already caused one wrong conclusion.
6. **§5.6** — the evidence gaps: the shopping list of runs to commission.
7. **§2.4** — the weapon system, because it is the working model to generalise.
8. **§6C** — `ff.py`, the working atomic engine already in the repo. Read `ff.py:135-290` before writing a formula.
9. **§6.16** — the tenet that points the other way, which should be settled deliberately rather than discovered mid-rebuild.

**Decide before costing anything** (each is cheap, and each invalidates work if left):
- Is the legal crew maximum **11 or 14**? (§6.10)
- Do stats get bought, or stay bundled in rank? (§8 Q1)
- Is there **one budget or two** — crew and settlement? (§8 Q32)
- **Hack-to-claim or bodies-in-area** for objectives? (§6.19) — it decides whether INT is priceable at all.

**Cheapest high-value runs available right now** (all already written, none reported):
- `py -3.13 run.py statsys 3000` — GENTLE vs SPREAD vs STACKED stat allocation under hack-to-claim. **This is the rebuild's central question and the test already exists.**
- `py -3.13 blkout_test.py` — apparently run 2026-07-23, never written up. Tells you whether Dodge gives AGI real combat value.
- `py -3.13 weapon_tests.py` — the 11 characteristic probes (`:146-158`) and DEX-vs-STR (`:183-196`), both defined with explicit acceptance thresholds.
- Re-run `crew_sim.py` / `weapon_tests.py` with the **current** stat lines (+3 per rank) and a **legal** swarm list, to replace the stale and doctrine-dependent ladder validation.
- Fix `crew_calibrate.py:99` (the rename broke it) before reusing the stat-allocation finding.
- Sweep terrain density **in `engine2d`** — the board is currently fixed at 11 pieces, so the game's most powerful dial has never been measured in the spatial engine.

---

### Coverage note

**Read in full:** the live vault `Rules System\` — 54 markdown notes + 13 Rules Ledger cards + this audit's cross-checks; `apps\Settlements\docs\` — all 6 planning documents; `test-bench\` — all 12 tracked scripts; `test-bench\engine2d\` — all 8 untracked modules plus its README; `playtest-kit\` — spot-checked against the vault for cost divergence.

**Deliberately not read:** `apps\Settlements\rules-vault\` (auto-overwritten mirror, may be stale) and `_Rules Map.canvas` / `Rules System.base` (non-prose Obsidian artifacts).

**Not verified:** no simulation was executed as part of this audit — every measured figure is quoted from a findings note or read out of the script that generates it. Where a published number could not be traced to a runnable script, it is flagged as such (§5.0.1, §5.0.2, §6.5, §6.6, §6.10).

*Read-only audit. No vault or rules file was modified; the only write was this document.*

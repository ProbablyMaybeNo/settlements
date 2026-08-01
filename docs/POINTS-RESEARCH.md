# Points Research — How Wargames Build Atomic Costing Systems

*Research pass for the Settlements 1000-point rescale. Compiled 2026-07-27.*

**Scope:** how tabletop wargames (and the deepest RPG point-buy systems) derive costs from a shared set of locked component prices, rather than hand-costing each entry. What works, what breaks, and what Settlements should do.

**Evidence standard used throughout.** Every claim is tagged:
- **[FACT]** — verifiable in a published rulebook, official document, or open-source implementation, with a URL.
- **[CONSENSUS]** — repeated, consistent community/competitive opinion, not a published number.
- **[INFERENCE]** — my own derivation or reasoning. Labelled every time.
- **[NOT FOUND]** — searched, found nothing. Stated rather than padded.

---

## 0 · Executive summary — the ten findings that should change the design

**1. Settlements' engine is unusually well-suited to atomic costing, and the reason is worth understanding.**
Under `1d10 + mod vs 7+`, `P(success) = (4 + mod)/10`, bounded 10–90%. That is *exactly linear* in the modifier. So the absolute gain in kill probability from each successive +1 is **constant**, not diminishing — the 5th point of a stat adds the same 0.07 to P(kill) as the 1st (worked numbers in §4.3). Most games have curved probability (2d6, dice pools, opposed rolls) where linear costing is provably wrong. Settlements does not. **A flat, linear price per +1 is defensible here in a way it is not in most games.** This is the single biggest advantage the engine hands you, and the rescale to 1000 exists precisely to let you express it. [INFERENCE, from the published engine]

**2. But the engine is multiplicative *across* factors, and that is where linear costing breaks.**
`P(kill) = P(hit) × P(injure)`. The marginal value of +1 to hit is proportional to the *damage* side, and vice versa. At `h=+2, d=+2` a point of hit and a point of damage are worth exactly the same; at `h=−1, d=+4` a point of hit is worth **2.67×** as much as a point of damage (§4.3). **A single flat price for "+1" is only correct along the diagonal where hit and damage modifiers are roughly equal.** The good news: Settlements' existing hard caps (damage +4, armour −2, ±3 modifier cap, stat max +6) are precisely what pins builds near that diagonal. The caps are not just balance patches — **they are what makes atomic costing valid.** Treat them as part of the costing system, not separate from it.

**3. Every successful derived system multiplies the things that multiply, and adds the things that add.** This is the most consistent structural lesson across every system examined.
- **BattleTech BV2:** `BV = (Defense × DefensiveFactor) + (Offense × SpeedFactor)`, then the whole thing × a pilot-skill multiplier. Mobility and crew quality are **multipliers**; armour and weapons are **addends**. [FACT — §1.1]
- **Song of Blades and Heroes:** `Cost = (5 × Combat + ΣSpecialAbilities) × (7 − Quality)/2`. Quality — which governs *how often you activate* — is a pure **multiplier** on everything else. [FACT — formula derived and verified 34/34 against the official chart, §1.2]
- **Hero System:** Advantages multiply the base cost; Limitations divide it. [FACT — §3]

- **One Page Rules:** `UnitCost = ((Quality + Defense)×Tough + Weapons + Rules) × Models`, where **weapon costs are multiplied by the unit's Quality value**. [FACT — official calculator recovered and verified 4/4 against OPR's own worked examples, §1.3]

  The rule that falls out: **anything that changes how often — or how reliably — a model acts must multiply. Anything that changes how well one action lands can be added.** Settlements currently adds everything. That is fine for weapon characteristics (they mostly land on different terms of the same product) and wrong for skills, ranks, and anything touching the action economy.

  **OPR's version of this is the one to copy.** Because Quality is *additive* in the base and *multiplicative* on every weapon, a Quality step automatically costs ~1.75× a Defense step — correct offence/defence coupling, for free, with no separate budget. In Settlements the equivalent is: **DEX/STR should multiply the weapon's cost, not sit beside it.** A rifle in the hands of a Specialist genuinely is worth more than the same rifle on a Recruit, and no additive table will ever say so.

**4. Action economy cannot be priced on the same scale as anything else, and this is arithmetically provable in your engine.**
For a baseline model (h=+2, d=+3, P(kill/attack)=0.42), one extra attack per turn raises output to 0.664 — a **×1.58**. Spending the *entire remaining stat and damage budget* (to h=+5, d=+4, the hard ceilings) only gets you to 0.72 — a ×1.71. **One extra action is worth 81% of everything else the model could ever buy.** [INFERENCE, §4.5] Your own `Skill Sim — Findings` independently measured Quick Shot at **+24 win%**, the largest single-skill swing in the game. The two results agree. **Extra actions must be gated by rank/tier, never sold at a price** — which is what Settlements already does, and should keep doing.

**5. Thresholds are the one failure mode no points system anywhere has solved with points.** Every game examined solves them by **hard cap, hard gate, or removal** — never by charging more. Settlements already discovered this independently (the 24" range ceiling; the sim found an uncapped long-range crew "beat every list by 13–30 points *at any price*"). BattleTech has the same bug, unfixed, in published form: weapons dealing 60+ damage get a flat 20% BV bonus, so the AC/20 pays a threshold premium and the AC/10 pays nothing, with no gradation between. [FACT — §6.1] **The design instruction: enumerate the game's breakpoints explicitly, and put a gate on each. Do not attempt to price them.**

**6. Two currencies are the standard industry answer to "some things must not scale with budget."** Infinity (Points + SWC), Necromunda (Credits + Gang Rating), X-Wing 2.5 (Squad Points + Loadout Value), Settlements' own plan (Goods to own + Points to field) all reach for the same tool. The reason is structural: a single currency lets a player convert *quantity* into *quality* without limit, and some capabilities (heavy weapons, special characters, action-economy abilities) must be capped as a *fraction of the force*, not bought freely. §2 and §7 cover what each game gates and why.

**7. The board prices what points cannot — and your own sim has already quantified this better than any published source found.**
`Crew Sim — Findings` measured a **66-point swing** in a single matchup from terrain density alone, and an 11-point spread across eight lists on a legal board versus 34–35 on an illegal one. No published game found in this research has data that clean. **This is a genuine asset, not a limitation.** It means Settlements can legitimately do what almost nobody else does: *derive costs from simulation against a fixed board specification*, and declare the board spec part of the rules. §8.7 recommends exactly that.

**8. The campaign layer is where costing errors compound, and two shipped precedents settle open questions.**
- **Stashed gear must not count toward crew rating.** 1995 Necromunda states it outright, and it is what makes underdog banding work: *ownership is wealth; rating is fielded power.* This settles the open Armoury fork and matches the already-locked "Goods buy what you own, points gate what you field" principle. [FACT — §10.1]
- **Play frequency out-snowballs skill.** A 100,000-run Necromunda simulation found median campaign income of **750 credits at one game per week versus 1,170 at two.** Settlements persists *outside* campaigns by design, which is exactly the exposed structure. A diminishing-returns income "wash table" is the cheapest shipped mitigation. [FACT — §10.5]
- And Trench Crusade's campaign shape is worth copying wholesale: a **published fixed threshold schedule** so every player's ceiling rises identically, a **rubber-band the losing player opts into at a real price**, a **hard cap on veteran count with a finite veteran lifespan**, and **`LIMIT: N` printed next to the price on every catalogue entry.** [FACT — §7.10]

**9. Games Workshop ran the "should gear cost points?" experiment for 25 years, and the answer arrived last month.** [FACT — §7.14] Per-item costs (3rd–7th) → dual system (8th) → quiet deletion (9th) → **all wargear free** (10th) → **June 2026, 11th edition partially reversed it**: gear is free by default and priced *only* where one option provably dominates, with the cost rebased out of the chassis so default loadouts stay points-neutral. Four things to take from it:
- **GW's stated reason for going free was never fairness — it was overhead versus yield.** Cruddace: per-item costs *"added to the complexity of working out your army, for little gain regarding the actual output of the unit on the battlefield."* The question to interrogate is not *"can we cost gear correctly?"* but *"is the cost of costing it worth what it buys?"*
- **The hidden dependency:** free wargear only holds if options are **sidegrades**, which GW said explicitly. 11th's reversal is the admission that some weren't. **That is a testable audit you can run against `Weapons.md` today** — any characteristic that is a straight upgrade rather than a sidegrade must be priced or gated.
- **The hidden price, and it is the sharpest lesson in the report:** to make N options cost the same you must make them *worth* the same, so you homogenise the profiles — GW's Death Guard flails, cleavers and maces all collapsed into one identical weapon. **You cannot escape paying for differentiation. Either you pay in points arithmetic, or you pay in flavour.** For a game whose pillar is a DIY armoury, flavour is the expensive currency — which argues for keeping priced characteristics and importing only the **points stepper** and *"cost the decision, not the item."*
- **Per-item costing collapses on its own terms.** In one 4th-edition codex a heavy bolter cost **+5 on a Tactical Squad and +15 on a Command Squad** — a 3× spread on identical wargear, because the number was really pricing the *slot*. Once an atom needs context-dependent prices, it has stopped being an atom and has kept all the bookkeeping.

**10. And the settlement layer has a different problem, which one game has already solved.** [FACT — §7.15] Every other system here answers *"what does this cost?"* **Oathmark answers *"what are you entitled to field at all?"*** — your kingdom's composition determines your legal army list. McCullough's central rule, verbatim: *"the kingdom might gain new territory, or it might have its territory occupied, but **when it comes to each game, the players are still playing to the same points value.**"*
> **The settlement should widen the menu, never the budget.** Growth is lateral, not vertical. That single decision is what makes a persistent base safe to bolt onto a points-buy game — and it is exactly the principle already locked here as *"Goods buy what you own, points gate what you field."* Oathmark proves it scales to a full campaign.

Plus four mechanisms to take directly: **concentric rings with a rarity gate** (thematic crews with no prohibition rules); **caps that reward diversity** (Oathmark's 4-unit limit doesn't carry across races, so diversity is the only legal route to a wider army); **heroes capped by buildings rather than a points percentage**; and **soft, reversible losses** — occupied, never destroyed. Full detail at §8.12.

**The headline recommendation:** build the cost function as **`Cost = (Body + Gear + Modifiers) × ActionEconomyMultiplier × QualityMultiplier`**, price the additive core at a locked **10 points per +1 on any single test** (at the 1000-point scale), keep every existing hard cap as a costing precondition, and gate thresholds and extra actions by rank rather than pricing them. Full detail in §8.

---

## 1 · Systems with genuinely derived costing

### 1.1 BattleTech — Battle Value 2 (the deepest published derivation in the hobby)

**Status: fully published, and independently verifiable in open-source code.** This is the gold standard, and the only system in this research where the entire derivation is public, complete, and machine-checkable.

**Mechanism.** [FACT]

```
BV = (Defensive Battle Rating) + (Offensive Battle Rating)
   = (Defense × DefensiveFactor) + (Offense × SpeedFactor)
then × PilotSkillMultiplier
```

**Defensive side:**
- `Defense = 2.5 × ArmorPoints + 1.5 × StructurePoints + 0.5 × Tonnage (gyro)` — each term carries a **type multiplier**: e.g. structure × 0.5 for Industrial/Composite, × 2.0 for Reinforced; engine type × 1.0 standard, × 0.75 Clan XL, × 0.5 IS XL. Defensive equipment (AMS = 32, ECM, probes, pods) is a flat additive block. Explosive ammo and Gauss criticals subtract.
- `DefensiveFactor = 1 + (max Target Movement Modifier / 10)`. Verified in MegaMek source: `1 + (Math.max(tmmRunning, Math.max(tmmJumping, tmmUmu)) / 10.0)`.

**Offensive side:**
- `Offense = Tonnage + Σ(weapon BV)`, where weapon BV is *approximately* proportional to `damage × range`.
- `SpeedFactor = round( (1 + (MP − 5)/10) ^ 1.2 , 2 )` where `MP = RunMP + round(max(JumpMP, UmuMP)/2)`. Verified verbatim in MegaMek: `Math.round(Math.pow(1 + ((mp - 5) / 10.0), 1.2) * 100.0) / 100.0`.
- **Heat efficiency (the important part).** For a 'Mech, `HeatEfficiency = 6 + heat capacity`. Weapons are **sorted by BV descending**, then heat is accumulated weapon by weapon; once cumulative heat reaches the efficiency limit, **every subsequent weapon counts at half BV**. Verified in `HeatTrackingBVCalculator.processWeapons()`.
- **Ammo cap.** Ammunition BV is capped at the BV of the weapons that can fire it (the "excessive ammo" rule) — verified in `BVCalculator.processAmmo()`, line ~1050.

**Pilot skill multiplier.** [FACT] A 9×9 lookup table indexed `[gunnery][piloting]`, normalised so Gunnery 4 / Piloting 5 = **1.00**. Verified verbatim in MegaMek `BVCalculator.bvMultipliers`:

| G\P | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| **0** | 2.42 | 2.31 | 2.21 | 2.10 | 1.93 | 1.75 | 1.68 | 1.59 | 1.50 |
| **1** | 2.21 | 2.11 | 2.02 | 1.92 | 1.76 | 1.60 | 1.54 | 1.46 | 1.38 |
| **2** | 1.93 | 1.85 | 1.76 | 1.68 | 1.54 | 1.40 | 1.35 | 1.28 | 1.21 |
| **3** | 1.66 | 1.58 | 1.51 | 1.44 | 1.32 | 1.20 | 1.16 | 1.10 | 1.04 |
| **4** | 1.38 | 1.32 | 1.26 | 1.20 | 1.10 | **1.00** | 0.95 | 0.90 | 0.85 |
| **5** | 1.31 | 1.19 | 1.13 | 1.08 | 0.99 | 0.90 | 0.86 | 0.81 | 0.77 |
| **6** | 1.24 | 1.12 | 1.07 | 1.02 | 0.94 | 0.85 | 0.81 | 0.77 | 0.72 |
| **7** | 1.17 | 1.06 | 1.01 | 0.96 | 0.88 | 0.80 | 0.76 | 0.72 | 0.68 |
| **8** | 1.10 | 0.99 | 0.95 | 0.90 | 0.83 | 0.75 | 0.71 | 0.68 | 0.64 |

Three things to steal from this table:

- **Skill is a multiplier on the whole unit, not an addend.** A better pilot makes the armour *and* the guns better, so it scales the total. Structurally correct, and the reason BV survives across a 200:1 unit power range.
- **The bonus/penalty asymmetry is deliberate anti-exploit design.** Improving Gunnery 4→3 costs **+20%**; degrading 4→5 refunds only **−10%**, and each further step down refunds just 5%. Piloting bonuses cost 10% (6% above skill 2) but penalties refund 5%. Officially confirmed by the line developer: *"Piloting upgrades are now 10% (dropping to 6% for Piloting Skills 2 and better)"*, and Gunnery *"has broadly stayed at 20%, 15% for the leap to Gunnery 0."* [FACT] **You cannot farm points by fielding deliberately bad models.** Settlements needs this the moment scars give a −2 rebate.
- **Improvements taper at the top** (the last Gunnery step is 15% not 20%), matching the fact that a better skill runs into the roll's ceiling.

**Verdict.** [CONSENSUS + FACT] Widely regarded as the most serious attempt at derived costing in the hobby, and it *works* well enough to run tournaments on across a vast unit catalogue. It is also **openly criticised, with specifics**. Scott Boehmer (software engineer, Scott's Game Room) published an eight-point critique; the substantive ones for Settlements:

1. **The formula assumes a to-hit number that real games don't produce.** BV prices weapons assuming a base to-hit of 4; actual play runs 6–8. Consequence: accuracy-boosting weapons are systematically **undercosted** (a Medium Pulse Laser is 48 BV at the assumed to-hit, but ~66 BV at a realistic one) and penalty-carrying weapons overcosted. **This is the single most transferable warning in this whole report: if you derive costs at one assumed difficulty and play happens at another, every accuracy modifier is mispriced.** [FACT — published analysis with numbers]
2. **Defensive scaling is linear but hit probability is not.** Units at +4 TMM are ~2.08× harder to hit than the linear `1 + TMM/10` factor prices. Fast jumpers are consequently undercosted.
3. **Speed is priced as a defensive/offensive multiplier but not as a *threat-range* multiplier.** A very fast light with short-range guns crosses the board and only pays for a fraction of the reach that gives it.
4. **Uneven unit counts are unaddressed** — more activations is an inherent advantage BV does not price. Boehmer's suggested fix is to pair BV limits with unit-count restrictions. (This is the same conclusion Settlements reached with the pyramid.)
5. **Downsides are ignored.** MASC and superchargers cost the same as permanent movement despite failure risk.
6. **Ammunition pricing breaks at the boundaries** — one-ton weapons underpay, multi-ton overpay. Concrete case: Rache Battle Armor is strictly superior to Elementals yet costs 372 BV vs 404, entirely because of two-shot vs one-shot SRM ammo costing.

**What's stealable:** the multiplicative skeleton; skill-as-multiplier; the asymmetric bonus/penalty ladder; the ammo cap; and above all **the heat-efficiency mechanism** — sort components best-first, spend a usage budget, and halve everything past it. That is a general, published solution to "you can't use all of this in one turn," and it maps directly onto action economy in a skirmish game (§6.4).

---

### 1.2 Song of Blades and Heroes — the closest published analogue to Settlements

**Status: the cost chart is published as an official PDF; the underlying formula is not stated, but it is fully recoverable from the chart.**

This is the most useful find in the research. SoBH is a small-model-count skirmish game (Ganesha Games, Andrea Sfiligoi) whose entire unit costing is a published two-axis lookup table: rows are Quality × Combat, columns are total Special Ability points, cells are the final cost. Special Abilities have their own flat published price list.

**The derivation.** [FACT — chart is published; the formula below is my derivation, validated 34/34 against transcribed cells *and* against all three of the publisher's own worked examples]

```
Cost = round( (5 × Combat + Σ SpecialAbilityPoints) × (7 − Quality) / 2 ),  minimum 1
```

Publisher's own examples, all reproduced exactly:
- *"Q5, C2 figure with no Special Abilities = 10 points"* → (10 + 0) × 1.0 = **10** ✓
- *"Q3, C3 figure with 7 points of Special Abilities = 44 points"* → (15 + 7) × 2.0 = **44** ✓
- *"Q2, C2 figure with 15 points of Special Abilities = 63 points"* → (10 + 15) × 2.5 = 62.5 → **63** ✓

The Quality multiplier is therefore exactly `(7 − Q)/2`: **Q5 → ×1.0, Q4 → ×1.5, Q3 → ×2.0, Q2 → ×2.5.**

**Why this structure is right.** In SoBH, Quality is the activation roll — it governs *how many actions you get*. Because actions multiply everything a model can do, Quality multiplies the entire cost including every special ability. A Stealth ability (3 SA points) costs 3 on a Q5 militia and 7.5 on a Q2 hero, automatically, with no separate table. **This is the cleanest published solution anywhere to "the same ability is worth more on a better model."** Compare the Board Game Designers Forum thread where a designer identifies exactly this problem — *"Regular troops and hero units often have access to the same power-up, but have to pay different amounts for it"* — with no solution offered. SoBH solved it with one multiplier. [FACT for the problem statement; the connection is my [INFERENCE]]

**The Special Ability price list** is flat and published (selected): Slow −5; Animal, Short Move −3; Coward, Dogged, Greedy, Protect, Stubborn −2; Bodyguard, Evil, Solar Force, Standard Bearer, Were 0; Shieldwall 1; Ghost Blade, Mountaineer, Paladin, Shooter (Short) 2; a large 3-point band (Acrobat, Fearless, Heavy Armor, Lethal, Poison, Stealth, Swarm, Undead, …); Berserk, Sharpshooter, Shooter (Medium) 4; Huge, Magic Resistance, Reckless 5; Mounted 6; Shooter (Long) 7; Beastmaster, Drain, Running Blow 8; Champion, Gargantuan 9; Bard, Combat Master, Flying, Long Move, Shield-Mage 10; Distract, Teleport 12; a large 15-point band (Assassin, Blast, Hero, Leader, Magic-User, Terror, Tough, …); Immortal 20. [FACT]

Notable design decisions visible in that list:
- **Ranged reach is priced as a stepped ladder, not a continuous variable:** Shooter Short 2 / Medium 4 / Long 7. The steps **accelerate** (2 → +2 → +3), correctly reflecting that reach compounds with mobility.
- **Pure-flavour abilities are explicitly priced at 0** (Evil, Standard Bearer, Were, Solar Force). A zero price is a legitimate, published answer for things that are narrative rather than mechanical.
- **Negative traits refund**, with the biggest refund (−5, Slow) on the one that costs you tempo.

**Verdict.** [CONSENSUS] SoBH is well regarded as a light, fast system and the point formula is the reason it supports thousands of user-created warbands across dozens of settings. The publisher ships a warband-builder app that does the arithmetic, which is a strong signal that a formula this simple still wants tooling. The known weakness is the same one every flat-list system has: a 3-point ability band lumps together things of quite different value (Stealth and Heavy Armor and Poison are not really equal), so the *granularity* of the SA list is coarser than the formula deserves. [INFERENCE from the list structure — I found no published critique quantifying this.]

**What's stealable — this is the highest-value transfer in the report:**
1. **`(additive core) × (activation multiplier)`** as the top-level shape.
2. Ability prices as a **single flat list**, scaled automatically by the model's quality multiplier — so you never maintain per-rank ability tables.
3. **A stepped, accelerating price ladder for range**, not a linear per-inch price.
4. **Zero-cost flavour traits as an explicit category.**

---

### 1.3 One Page Rules — the most complete atomic system in modern tabletop

**Status: the full official formula was recovered and verified. This is the single most directly applicable find in the report.**

The **"AoF: Point Calculator v1.10"** (18pp, credited *Game Design: Gaetano Ferrara*) is an official One Page Rules document. OPR paywalls it behind Patreon Tier 3 and it has since been removed from their public resources page, but an archived copy was recovered and read in full. [FACT]

**Unit construction:**
```
Base Cost       = (Quality + Defense) × X          where X = Tough(X), else 1
Total Unit Cost = (Base + Weapons + Special Rules) × Models
                → rounded to the nearest multiple of 5
```

**The stat ladder** — identical lookup for Quality and Defense: [FACT]

| Stat | 6+ | 5+ | 4+ | 3+ | 2+ |
|---|---|---|---|---|---|
| Points | 2 | 4 | 6 | 8 | **16** |

**+2 per step, then a doubling at 2+.** A deliberate super-linear term at the top of the ladder to make extreme stats self-limiting.

**Weapon construction:** [FACT]
```
Weapon Cost = Range × Attacks × Special Rules
Total Cost  = Weapon Cost × Quality        ← the unit's Quality POINT VALUE, not its die number
```
Range multipliers: Melee 0.25 · 6" 0.125 · 12" 0.25 · 18" 0.375 · 24" 0.5 · 30" 0.625 · 36" 0.75 · 42" 0.875 · 48" 1.0
Weapon-rule multipliers: AP(1) ×1.5 · AP(2) ×2 · AP(3) ×2.5 · AP(4) ×3 · Blast(X) ×X · Deadly(3) ×2 · Deadly(6) ×4 · Indirect ×1.25 · Poison ×1.25 · Rending ×1.5.
Special rules mix flat, derived and multiplicative: Fear = 20 · Artillery = 15 · Impact(X) = 3X · Regeneration = 6×Tough(X) · Stealth = 2×Tough(X) · Wizard(X) = 20X+5 · Flying/Fast/Scout/Ambush = Quality · Slow = −Quality · Immobile = −3×Quality · Strider = Quality/2 · **Hero = 0** · Fearless = recompute the base at Quality+1.

**Verification.** The formula was implemented and reproduces OPR's own published worked examples **4/4 exactly** — including the 5-model Orc Archers unit (Q5+/D5+, Bow, Hand Weapon, Furious) landing on 60, and a Q3+ Hand Weapon → Great Weapon upgrade at 5. [FACT — reproduced computation]

**The single most elegant thing in the system.** Because Quality is *additive* in the base cost but *multiplicative* on every weapon, while Defense enters only the base: [INFERENCE — computed, 5 models with Bow + Hand Weapon]

| Quality | Cost | | Defense | Cost |
|---|---|---|---|---|
| 6+ | 37.5 | | 6+ | 45 |
| 5+ | 55.0 | | 5+ | 55 |
| 4+ | 72.5 | | 4+ | 65 |
| 3+ | 90.0 | | 3+ | 75 |
| 2+ | **160.0** | | 2+ | **115** |

**A Quality step costs ~1.75× a Defense step, automatically, with no separate offence/defence budget.** `Tough(X)` multiplies the whole base but **not** weapons — so durability compounds while guns stay linear.

**Points do not equal balance, and OPR says so.** They ship a **second, orthogonal validator** [FACT — patch notes, 26 Jan 2024]: *"In order to make sure that individual units are not too overpowered, we use a simple system of comparing how many potential wounds a unit can deal vs how many wounds the unit can take."* It drives the "balanced"/"not balanced" badges on community armies, and OPR concede unbadged armies *"may have wildly unbalanced units."* **Architecture: the formula sets the price; a damage-ratio cap catches what the formula misses.**

**And they add a written guideline where maths can't reach** [FACT — from the calculator book itself]: *"avoid using Quality 2+ and 6+ because players feel like they are not very balanced, even if point costs compensate for the rolls."* **Costing the extremes correctly is not the same as making them fun.**

**Caveats.** [CONSENSUS] Balance opinion is mixed — *"it's definitely easy to break if you want and some stuff is overpowered or underpowered"* versus *"surprisingly well balanced for what it is"*; OPR's own 3rd-edition notes admit an offensive/defensive cost-ratio problem needing a global retune. The recovered v1.10 is ~2020 and a forum thread title indicates the live Army Forge engine has since **diverged** from the published book (thread body unreadable — search-index snippet only, flagged as unverified). A community reverse-engineering exists (`kdj0c/onepagepoints`, MIT) but is a *different, continuous* model — `defense_cost(d) = (0.9d² + d + 10)/2`, `ap_cost(ap) = 1.2^ap` — with two hard-coded fudge factors *"to match onepagerules current prices."*

**What's stealable — this is the highest-value list in the report:**
1. **One stat multiplies offence and adds to defence.** You get correct offence/defence coupling for free.
2. **Multiplicative rule modifiers** self-scale across cheap and expensive weapons — no per-weapon tables to maintain.
3. **Price upgrades as deltas, rounded up** — `cost(new) − cost(old)`, kills the "sidegrade costs 0" exploit.
4. **A super-linear jump at the top of the stat ladder** (8 → 16) so extremes self-limit.
5. **Ship a second, orthogonal validator.** Points ≠ balance.
6. **Round to a coarse grid** (nearest 5) — hides floating-point noise, keeps lists mentally addable.

### 1.4 What "1000 points" actually buys you

Settlements is rescaling 100 → 1000 for granularity. Two published data points bracket what that's worth:

- **SoBH** operates on a scale where a militia model costs 5–10 and a fully-loaded hero costs ~125, with a **1-point** resolution and multipliers of 1.0/1.5/2.0/2.5 producing half-point intermediate values rounded to integers. It works because rounding error (≤0.5) is small against a ~25-point average model. [FACT]
- **BattleTech BV2** operates in the ~500–3,000 range per unit and rounds only at the very end (0.5 rounds up), keeping full floating-point precision throughout the calculation. [FACT]

[INFERENCE] The lesson is not "more points is better" — it is **round once, at the end**. A 1000-point budget with a 10-point atomic unit gives you exactly the same expressive range as 100 with a 1-point unit; what it buys is **headroom for multipliers and conditional discounts to land on integers**. A ×0.75 conditional discount on a 40-point characteristic is 30; the same discount on a 4-point characteristic is 3 and loses the distinction between ×0.7 and ×0.8 entirely. **That is the real argument for 1000, and it is a good one.** The corollary: if you rescale and then keep pricing in round tens, you have gained nothing. Spend the granularity on the multipliers.

---

## 2 · Dual-currency systems — why so many games use two

*(Detail on Infinity's SWC, Necromunda credits/rating, Warmachine, Malifaux and Kill Team is in the per-system profiles below, from the parallel research streams.)*

The recurring structural argument, which is consistent across every game that reaches for a second currency: **a single currency permits unlimited substitution between quality and quantity, and between "generically useful" and "specialist" capability.** A second currency exists to make one axis *non-fungible* — you cannot sell your heavy weapons to buy more bodies, because heavy weapons are bought with a currency bodies don't use.

For Settlements this matters because the design already contains three things that are structurally "SWC-like" — capabilities that should be capped as a *fraction of the crew*, not freely purchasable:
- **Orders** (Leader/Specialist only) — already gated by the pyramid.
- **Extra-action skills** (Quick Shot, Dual Wield) — already gated by tier.
- **24" range** — already gated to Heavy Ranged at Specialist rank.

[INFERENCE] Settlements has therefore *already built* an SWC equivalent — it just implemented it as **rank gates** rather than a second currency. That is a legitimate and arguably better choice for a game this size: rank gating needs no extra bookkeeping and reads off the model. The recommendation in §6 is to keep it and make it explicit as a design principle, rather than adding a second battle currency on top of the Goods/points split already planned.

---

## 3 · RPG point-buy — the deepest published atomic systems, and their documented breakages

These are the most rigorously costed systems in existence, they have been stress-tested by millions of players for forty years, and **their failure modes are the best-documented in the hobby.** Three findings here should change the Settlements design directly.

### 3.1 The warning that should be read first

**Gutschera, WotC Director of Development** [FACT — §5]: *"Balancing a class-based RPG (where you are forced to play a single 'color') is hard enough; balancing a pure point-buy RPG (where you can put any card you like in your 'deck') is very difficult, and **has arguably never been done successfully.** These systems appear to offer great variety, but in practice tend to degenerate to a single viable character build."*

Every system below is a partial refutation and a partial confirmation.

### 3.2 GURPS 4e — the derived-stat arbitrage

**Published attribute costs** [FACT — GURPS Basic Set: Characters pp.14–17, corroborated by GURPS Lite 4e]:

| Trait | Cost | Derivation |
|---|---|---|
| ST | ±10 / level | — |
| DX | ±20 / level | — |
| IQ | ±20 / level | — |
| HT | ±10 / level | — |
| HP | ±2 per ±1 | "HP equal to your ST" |
| Will | ±5 per ±1 | "Will is equal to IQ" |
| Per | ±5 per ±1 | "Per equals IQ" |
| FP | ±3 per ±1 | "FP equal to your HT" |
| Basic Speed | ±5 per ±0.25 | "(HT + DX)/4" |

**The failure mode: a derived stat that is both free-from-a-parent *and* separately purchasable gives the parent a hidden discount.** Strip the bundle: [INFERENCE from the verified numbers; the same decomposition is published on MyGURPS]

| Buy | Cost | Free derived value included | Net cost of the "pure" stat |
|---|---|---|---|
| ST +1 | 10 | +1 HP (worth 2) | **8** |
| DX +1 | 20 | +0.25 Basic Speed (worth 5) | **15** |
| IQ +1 | 20 | +1 Will (5) + 1 Per (5) | **10** |
| HT +1 | 10 | +1 FP (3) + 0.25 Speed (5) | **2** |

GURPS patches this with **GM-discretion drift caps**, not with maths [FACT]: *"the GM should not allow HP to vary by more than ±30% of ST"*; *"You cannot raise Will past 20, or lower it by more than 4, without GM permission"*; *"the GM should not allow characters to alter Basic Speed by more than 2.00 either way."* **The caps exist because the arbitrage exists.**

**The second failure mode: flat-linear attribute cost against a flat-marginal skill cost.** The skill table accelerates then flattens at **+4 points per level**; attributes are a flat 20. [FACT for both tables] **Break-even is 20 ÷ 4 = 5 skills** [INFERENCE] — and DX and IQ each govern roughly half of GURPS' ~300 skills. Any character with six or more DX-based skills is strictly better off buying DX. This is structural, and the community identified it in **1994**, a decade before 4e shipped the partial fix (splitting Will and Per out of IQ).

**GURPS admits its own percentage system breaks at scale** [FACT — GURPS Powers, optional Multiplicative Modifiers rule]: *"The additive model is a good 'default,' but the multiplicative model can be fairer in campaigns where huge enhancements (like Cosmic, +300%) occur routinely."* Worked contrast: +20% and −50% gives 70% of cost additively, **60% multiplicatively.** The divergence grows with modifier size.

**The floor** [FACT]: *"Modifiers can never reduce cost by more than 80%... you cannot lower the cost of a trait to less than 1/5 its base cost."*

### 3.3 Hero System — the purest published statement of the problem

**The formula** [FACT, verified from the 6e Basic Rulebook with worked examples]:
```
Active Cost = Base Cost × (1 + ΣAdvantages)
Real Cost   = Active Cost ÷ (1 + ΣLimitations)
```
Modifiers move in **±¼ steps**, ranging to ±2 or higher. Published worked example: *"Blast 8d6, No Range Modifier"* = (40 × 1.5) = 60 Active; with *"12 Charges (−¼)"* and *"Obvious Accessible Focus (−1)"* → 60 ÷ 2.25 = 26.67 → **27 points.**

**Why the multiply/divide asymmetry is correct** [INFERENCE from the verified formula]: advantages scale linearly (+¼ → ×1.25), but limitations **decay hyperbolically** (−¼ → 20% off; −1 → 50% off; −4 → 80% off). The discount asymptotes to 100% and never reaches it. **Hero is the only one of the three systems that needs no floor at all — the functional form does the work.** GURPS hard-clamps at −80%; M&M bolts on an advisory 1:5 floor.

**And the single best sentence found in this entire research pass**, on Hero 5e's Figured Characteristics [FACT — Game Design Fanatic, verbatim]:

> *"A well-known strangeness of previous versions was that purchasing STR and CON actually gave you more points worth of figured characteristics than you paid for the primary characteristic. This meant that, in some sense, **these characteristics had a negative cost — increasing them could make the character cheaper!**"*

> *"To deal with this, it was necessary to put limits on how many figured characteristics you could buy down, **artificially limiting your character design**."*

**Hero 6e's fix was to delete derivation entirely** and raise starting point totals to compensate [FACT]. Every characteristic is now bought directly: STR 1/point, DEX 2, SPD **10**, OCV/DCV 5 each. The stated purpose: it *"reduces the **'Uberstat' effect** of having all characters with high DEX even if their concept doesn't really fit."* **DEX went from the dominant purchase to a fair one by unbundling, not by repricing.**

**A residual failure mode Hero still has** [INFERENCE]: because limitations divide the *entire* Active Cost — advantages included — a power with +1 advantage and −2 limitation costs **two-thirds of the plain base power.** The incentive is to stack limitations you don't care about so your advantages come cheap. Hero's only guard is social: *"A Limitation which doesn't limit the character isn't worth any bonus!"*

**SPD is the action-economy lesson again** [FACT + INFERENCE]: SPD costs a flat 10 points per +1, and each +1 gives another Phase per Turn — multiplying *everything* the character does. Going 2→3 is +50% output for 10 points; 6→7 is +17% for the same 10. **Linear price on a multiplicative quantity.** Exactly the trap §4.5 identifies in Settlements.

### 3.4 Mutants & Masterminds — the cap layered over the economy

**Points = PL × 15** [FACT]. Atomic costs: Abilities 2/rank, Defenses 1/rank, Skills 1 per 2 ranks, Advantages 1 each.

**The Power Level caps** [FACT — verbatim from the 3e SRD]:

| Cap | Rule |
|---|---|
| Skill modifier | ≤ PL + 10 |
| **Attack + Effect rank** | ≤ **2 × PL** |
| **Dodge + Toughness** | ≤ 2 × PL |
| **Parry + Toughness** | ≤ 2 × PL |
| **Fortitude + Will** | ≤ 2 × PL |
| Non-attack effects | rank ≤ PL |

**The published rationale, and it names the cost honestly** [FACT — M&M 2e core p.25]: *"Not raising the power level **forces player characters to diversify**, improving their less powerful or effective traits, and acquiring new ones, but it **can make the players feel constrained and the heroes start looking the same** if it isn't raised occasionally."*

**Points and PL are explicitly orthogonal** [FACT]: NPCs *"are not restricted by the series power level"*, and an NPC's effective PL *"is not necessarily related to the NPC's Character point total."*

> **The pattern to steal: points buy breadth; the cap rations depth.** The points economy answers "how much stuff do you have"; the cap answers "how good is your best thing." Only the second governs table playability.

**The clause worth copying verbatim** [FACT — Enhanced Trait]: *"Your enhanced trait is still subject to power level limits, so your **unenhanced rank must be below the limit by at least the amount of the enhancement** to accommodate it."* — i.e. **caps apply to the resulting value, not the purchase.** Any cap checked at build time but not at play time gets routed around.

**M&M's own structural flaw: additive per-rank modifiers are not scale-invariant** [INFERENCE from the published cost table]. Base effect costs range 1/rank (Damage, Affliction, Protection) to 8/rank (Shapeshift, Mimic). A "+1 per rank" extra is therefore **+100%** on a 1/rank effect and **+12.5%** on an 8/rank one — **an 8× proportionality error on every extra in the book, by construction.** Percentage systems don't have this problem; they have GURPS' large-magnitude problem instead. **Pick one, and if you pick additive, keep base costs in a narrow band.**

**The sharpest single mispricing found anywhere** [FACT + INFERENCE]: **Summon costs 2 points/rank** and yields *"an independent character with (effect rank × 15) character points"* — against the game's own published rate of 15 CP per PL. That is a **7.5:1 return on the system's own exchange rate.** Meanwhile **Variable costs 7/rank for 5 CP of allocatable traits** — a 1.4× *premium* for flexibility. The same designers priced flexibility at 1.4× and an entire extra character at 0.13×.

**Kenson's own post-mortem is the most useful part** [FACT — official 2e→3e conversion notes]. Every trait he cut or rebuilt for mispricing was a **cheap flat-rate bolt-on**: Sneak Attack (*"created too many potential conflicts with power level limits on damage"*), Fearsome Presence (*"as a 1 point per rank advantage"*), Luck (*"deemed too broadly effective to be handed out for just 1 point per rank"*), and the 1–2-point Alternate Effect. **The per-rank effect costs held up across two editions. The leaks were all in the fixed-price traits.**

### 3.5 What this means for Settlements

1. **Never let a value be both free-from-a-parent and separately purchasable.** Settlements is currently *safe* here — rank bundles stats and skills, and you cannot buy stats separately ("the rank price *is* the stat price"). **Guard that.** The moment a campaign rule lets a player buy a single stat point outside a rank, the GURPS/Hero arbitrage opens.
2. **The conditional-discount mechanism should divide, not subtract** (§8.3). Hero's form needs no floor.
3. **Settlements' hard caps are its PL system**, and they are doing the M&M job — but they should be checked against the *resulting value*, not the purchase (§8.4).
4. **Expect the leaks in flat-priced bolt-ons, not in the per-point spine.** Three published systems agree. In Settlements that means Med-Kit (4), Breach Kit (4), Exploit Suite (8), Deployables (4–14), and the drawback refunds — not the stat ladder.

---

## 4 · The engine math — what Settlements' own dice curve implies

All numbers in this section are computed directly from the published engine (`1d10 + mod ≥ 7`, natural 1 auto-fails, natural 10 auto-succeeds), which gives `P = clamp((4 + mod)/10, 0.1, 0.9)`. [INFERENCE — arithmetic on your own rules, not a claim about any other game.]

### 4.1 The probability ladder

| mod | −3 | −2 | −1 | 0 | +1 | +2 | +3 | +4 | +5 | +6 |
|---|---|---|---|---|---|---|---|---|---|---|
| **P(success)** | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 80% | 90% | 90% |

**+6 is worthless on an unmodified roll** — it is only reachable past the cap against cover, armour and opposed rolls. This is already documented in `Unit Design`. It means the Leader's signature T3 stat is priced for a benefit it only sometimes receives.

### 4.2 The two-factor kill chain

`P(kill per attack) = P(hit) × P(injure)`, where `h` = net to-hit modifier and `d` = Damage − Armour.

### 4.3 Marginal value of +1 — the key result

**Absolute gain in P(kill) from +1 to HIT** (rows = h, columns = d):

| h \ d | 0 | +1 | +2 | +3 | +4 |
|---|---|---|---|---|---|
| −1 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| 0 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| +1 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| +2 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| +3 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| +4 | 0.040 | 0.050 | 0.060 | 0.070 | 0.080 |
| **+5** | **0** | **0** | **0** | **0** | **0** |

**Absolute gain in P(kill) from +1 to DAMAGE:**

| h \ d | 0 | +1 | +2 | +3 | +4 |
|---|---|---|---|---|---|
| −1 | 0.030 | 0.030 | 0.030 | 0.030 | 0.030 |
| 0 | 0.040 | 0.040 | 0.040 | 0.040 | 0.040 |
| +1 | 0.050 | 0.050 | 0.050 | 0.050 | 0.050 |
| +2 | 0.060 | 0.060 | 0.060 | 0.060 | 0.060 |
| +3 | 0.070 | 0.070 | 0.070 | 0.070 | 0.070 |
| +4 | 0.080 | 0.080 | 0.080 | 0.080 | 0.080 |

**Read these two tables together and the whole costing problem becomes visible:**

- **Down a column, the value of +1 is constant.** Stacking to-hit modifiers has *no diminishing returns in absolute output* until the cap. This is why a flat linear price is legitimate here.
- **Across a row, the value of +1 to hit rises with the damage side, and the value of +1 damage rises with the hit side.** They are the two factors of a product.
- **The implied fair-cost ratio (hit : damage):**

| h \ d | 0 | +1 | +2 | +3 | +4 |
|---|---|---|---|---|---|
| −1 | 1.33 | 1.67 | 2.00 | 2.33 | 2.67 |
| 0 | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |
| +1 | 0.80 | 1.00 | 1.20 | 1.40 | 1.60 |
| +2 | 0.67 | 0.83 | **1.00** | 1.17 | 1.33 |
| +3 | 0.57 | 0.71 | 0.86 | **1.00** | 1.14 |
| +4 | 0.50 | 0.62 | 0.75 | 0.87 | **1.00** |

**On the diagonal (h = d), +1 to hit and +1 to damage are worth exactly the same.** Settlements' typical build sits at h ≈ +2 to +3 (DEX/STR +2 or +3) and d ≈ +2 to +3 (Damage +3 vs Armour 0–1) — **on or adjacent to the diagonal.** So one flat price for "+1 anywhere on the kill chain" is correct for the intended build space, and drifts by at most ~±20% at the edges of it. **The caps are what keep you there.**

This also *validates the current weapon table*: Brutal (+1 Damage) = 4 and Armour Piercing (−1 enemy Armour) = 4 are correctly priced identically — both are +1 to `d`. That is already an atomic derivation; it simply has not been written down as one.

It also flags an inconsistency: **Accurate (+1 to hit) at 3 is cheaper than Brutal (+1 damage) at 4**, but on the diagonal they are worth the same, and *below* the diagonal +1 to hit is worth **more**. The 1-point discount is presumably paying for the "did not move" condition. If so, it should be stated as a conditional multiplier, not buried (§6.3).

### 4.4 Diminishing returns — where they actually are

Stacking to-hit at d=+3:

| h | −1 | 0 | +1 | +2 | +3 | +4 | +5 | +6 |
|---|---|---|---|---|---|---|---|---|
| P(kill) | 0.210 | 0.280 | 0.350 | 0.420 | 0.490 | 0.560 | 0.630 | 0.630 |
| absolute step | — | +0.070 | +0.070 | +0.070 | +0.070 | +0.070 | +0.070 | **+0.000** |
| relative step | — | +33% | +25% | +20% | +16.7% | +14.3% | +12.5% | +0% |

**Absolute returns are perfectly flat; relative returns diminish; and then there is a cliff.** Which of those you price against determines your whole cost curve:
- Price against **absolute** output → flat linear cost per +1. Correct if what matters is "how many enemies die per turn."
- Price against **relative** output → a decreasing cost curve. Correct if what matters is win probability in a duel.

[INFERENCE] For a WND-1 game where models die to one hit and the objective is board control, **absolute output is the right metric** — the marginal kill matters as much whether it is your first or your sixth. Price linearly. But note the cliff: **the +6th point is worth literally zero on an unmodified roll**, so anything that pushes a model past net +5 should be either refused or refunded.

### 4.5 Action economy — the arithmetic proof it cannot be priced

Baseline model, h=+2, d=+3 → P(kill/attack) = **0.4200**

| Option | P(kill/turn) | × baseline |
|---|---|---|
| Baseline | 0.4200 | — |
| Spend **the entire remaining budget** (h→+5, d→+4, i.e. every cap maxed) | 0.7200 | **×1.714** |
| **One extra attack**, same profile | 0.6636 | **×1.580** |

**One extra action delivers 81% of the value of maxing out every stat and damage cap in the game simultaneously.** No price on the same scale as a +1 can be correct.

Compounding further attacks does show diminishing returns (1→2 attacks: +0.244; 2→3: +0.141; 3→4: +0.082), which is why a *second* attack is catastrophic and a *fourth* is merely strong — but the first extra action is the break point.

Cross-check against the project's own data: `Skill Sim — Findings` measured Quick Shot at **+24 win%** (74% vs a 50% baseline) — *"biggest single-skill swing"* — and multi-attack at **+67% output**. Two independent methods, same conclusion. [FACT — in-repo simulation]

### 4.6 Model count — why the same points is not the same power

Under a Lanchester-square framing (n models firing concurrently concentrate fire, so effective power scales with N² × quality rather than N × quality), two "linearly equal" crews are not equal:

| Crew | Models | Kill rate each | Linear power (N×q) | Square power (N²×q) |
|---|---|---|---|---|
| A — elite | 4 | 2× | 3.36 | 13.44 |
| B — numerous | 8 | 1× | 3.36 | **26.88 (2.0×)** |

[INFERENCE — standard Lanchester reasoning applied to your numbers; the parallel research stream's findings on Lanchester's application to miniatures games are in the failure-mode catalogue below.]

**Settlements' answer is already better than most games'**, and it is worth recording *why* it works: `Crew Sim — Findings` shows the 9-Fighter horde, the 11-model pyramid and the 14-model Recruit horde landing **within three points of each other at every density**, i.e. Recruit-at-5 and Fighter-at-8 are correctly priced *against each other*. The mechanisms doing that work are:
- **Reaction banking** — 4 models = 4 banked Ready reactions, so an elite crew effectively shoots twice.
- **The Stress cascade** — friendly-Down Stress punishes bunching, so the swarm pays a morale tax the elite crew doesn't. The sim explicitly found that softening the cascade pushed Recruit-horde win rates to **93%**. *"The cascade is not a bug; it is the only thing keeping a swarm honest."*
- **Underdog +1 Priority** as explicit compensation.
- **WND fixed at 1**, so quality has a hard ceiling that numbers do not.

**That is a complete, working answer to the horde/elite problem, arrived at by mechanism rather than by pricing.** It should be documented as such — it is the model for how to handle every other non-linearity.

### 4.7 Cover, and why it is not a linear penalty

| base h | open | light (−1) | heavy (−2) | % of hits heavy cover removes |
|---|---|---|---|---|
| +0 | 40% | 30% | 20% | **50%** |
| +1 | 50% | 40% | 30% | 40% |
| +2 | 60% | 50% | 40% | 33% |
| +3 | 70% | 60% | 50% | 29% |
| +4 | 80% | 70% | 60% | 25% |
| +5 | 90% | 80% | 70% | 22% |

**Cover is worth twice as much against a bad shooter as a good one.** [INFERENCE] Consequence for costing: any defensive ability that imposes a to-hit penalty has value inversely proportional to the *enemy's* skill — i.e. its value is set by the meta, not by the model carrying it. This is the defensive mirror of the BattleTech "assumed to-hit of 4" flaw (§1.1), and it is the reason defensive modifiers are the hardest single thing to price atomically. The mitigation used by every game that gets this right is to **fix the assumed opposing skill by decree** and cost against it — and then *say so in the design doc*, so that when the meta shifts you know exactly which assumption broke.

---

## 5 · The canonical text — and what it says you are doing

The single most important source found in this research is not about wargames at all, but it is explicitly *addressed* to them:

**K. Robert Gutschera, Director of Development, Wizards of the Coast — "Magic Lessons: Designing and Balancing Game Objects," GDC 2007.** Read in full and verified. Gutschera's stated scope: *"collectable object games... trading card games like Magic: the Gathering, or collectable miniatures games like Warhammer 40K or Mage Knight."* Acknowledgements thank Richard Garfield. This is as close to a canonical text on costing as the field has, it is free, and every claim below is a verbatim quote. [FACT]

**The fifteen rules, in the author's own order of importance:**
1. Adjust costs, not effects
2. The single knob theory
3. Color wheels are everywhere
4. Rock-paper-scissors
5. Don't neglect the vanilla curve
6. Processes
7. Watchlists
8. Simple databases to help designers
9. Playtesting vs. theorizing
10. Developing for multiple environments
11. The Black Lotus effect
12. Dangers of non-scalable effects
13. Balancing powerful effects that occur late or rarely
14. Flexibility is sometimes worth less than you think
15. Miss on the other side of the target

**The seven that bear directly on Settlements:**

**Rule 2 — the numeraire.** *"You generally want a single number that represents your cost in the sense that it's the number you will tune... You're creating what economists would call a numeraire (a single, perhaps arbitrary, unit in which all your costs can be measured), and for essentially the same reasons."* Settlements' numeraire should be **one point of modifier on one test**, and *everything* — a body, a gun, a skill, a structure — should be expressible in it. Anything that cannot be converted into the numeraire will go unpriced. That is the whole argument for the 1000-point rescale, stated by WotC.

**Rule 5 — the vanilla curve comes first.** *"It pays to focus on the vanilla curve: the costs for those objects that have just basic stats and no special powers... When you do get your vanilla curve (mostly) right, you'll be able to look at objects and say 'well, the stats are worth this much, and we've made other objects with this ability, so we know the ability is worth that much.'... If you can't do it this way, then each object becomes a new thing to playtest, and you will run out of testing resources long before you are done."* **This is the exact task Settlements has in front of it, described precisely.** The vanilla curve here is: what does a rank cost, given only its stat line and no skills, no gear?

**Rule 8 — value and cost are two different numbers, and the gap is the design.** *"Each different gameplay stat is converted into a cost, any special abilities are converted to costs... and some reasonable math will combine them all into a number that represents (with as much accuracy as possible) the utility of the item. Then the cost of that item in the game is also represented. Note these numbers should **not** necessarily be equal. A game, to be interesting, needs good bargains and bad bargains. But a good game developer should know which are which, and by how much."* And the diagnostic: *"Good prospects for testing are items where the cost is a lot less than the value. Good prospects for re-evaluating your database formulas or unique ability values are items where the listed value is less than the cost, but people are playing them a lot anyway."* **Settlements should build the derivation as a value model, then set prices deliberately off it, and record the deltas.** A perfectly-flat cost=value table is a design failure, not a success.

**Rule 12 — non-scalable effects, and the explicit naming of the extra-attack problem.** *"Most objects are scalable: they add to your stats, or they do a certain amount of damage... But some objects are not... These objects can be dangerous."* And: *"If your spell that destroys any enemy creature costs (say) 4, it will be very hard for you to make good creatures that cost much more than 4... Your one spell that kills a creature is cool, but is it worth all the expensive creatures that you can no longer make?"* Then, naming the case directly: *"It's always good to get a free attack... It's hard to avoid non-scalable items, because getting rid of them often means taking something simple and cool ('gain an extra attack') and turning it into something less elegant ('gain an extra attack against an opponent of level 40 or below')."* **A single unconditional non-scalable effect caps the top of the entire cost curve.** In Settlements the relevant non-scalables are: extra attacks, ignore-cover, re-rolls (already banned), and instant-kill effects. The design already refuses re-rolls and ignore-cover on exactly this instinct; this is the published justification.

**Rule 14 — flexibility is worth less than you think, focus is worth more.** *"A ring that adds +3 to four different stats should cost less than a ring that adds +12 to one stat. A card that lets you pick one of two different effects is not twice as good as a card that lets you do just one of those effects (in fact, our experience is that to first order the two are equally good, that is, their cost difference tends to be less than 1 mana)."* **This is a direct challenge to Settlements' tier-cap philosophy**, which deliberately *forces* stat points to spread. Per Gutschera, a spread stat line is genuinely worth *less* than a spiked one — which means the tier caps are not just a flavour device, they are a **real price reduction the player is being forced to accept**, and the rank costs should reflect that. Note this cuts against the current note that *"the richer stat lines run stronger — a re-cost pass is owed"*: the richer lines run stronger in absolute output, but by Gutschera's rule the *forced spread* is a partial discount. Worth measuring rather than assuming.

**Rule 15 — bracket the target, don't creep toward it.** *"If Rogues keep coming up weak, tune them to be too strong. If the Sword of Doom is too strong, tune it to be terrible. Once you've missed on both sides of the target, it should be much easier to hit it on the next iteration."* Cheap and immediately applicable to the sim.

**Rule 4 — 60/40 beats 50/50.** *"If your game has three gameplay units A, B, and C, and you try to balance them so that each one wins against the other 50% of the time, you will surely slip up and find that B, say, wins 53% of the time against A and 57% of the time against C. Everyone will stop playing A and C and just play B. But if you try to balance so that A beats B beats C beats A, each 60% of the time, then as long as you're off by less than 10% in each case, all three units remain viable."* Footnote 9: *"what we're really talking about here is Von Neumann/Nash game theory. A 'viable object' is what game theory would call a 'non-dominated strategy'."* **A deliberate rock-paper-scissors triangle is more robust to costing error than perfect symmetry.** For Settlements this argues for making the archetypes (gunline / swarm / melee-elite / techie) intentionally cyclic rather than trying to land all eight on 50%.

**And the warning that must be recorded honestly:**

> *"Balancing a class-based RPG (where you are forced to play a single 'color') is hard enough; balancing a pure point-buy RPG (where you can put any card you like in your 'deck') is very difficult, and **has arguably never been done successfully**. These systems appear to offer great variety, but in practice tend to degenerate to a single viable character build."*

That is WotC's Director of Development saying pure point-buy has arguably never been balanced. And Settlements' own `Crew Sim — Findings` reports exactly the predicted symptom: **"A Fighter has one real build: STR"** — STR+2 wins 14/35/63% across densities versus DEX+2 at 5/16/36%. The degeneration Gutschera describes is already visible in the data. [FACT — both sources]

**The mitigation Gutschera names is rule 3: colour wheels — forced correlations that make commitment pay.** In Settlements the existing candidates are rank gates (a Recruit cannot hold a rifle), skill paths (a skill rides *its own* stat's tier), and faction rules. **The design already has the tool; it has not yet been pointed at this problem.** §6.6 makes this concrete.

---

## 6 · The failure-mode catalogue

Each mode: what it is, real cited examples, and the mitigation games actually use.

### 6.1 Thresholds and breakpoints

**What breaks.** An ability whose value jumps discontinuously at a specific number. Linear cost cannot express a step function.

**Real examples:**
- **BattleTech's assumed to-hit baseline** [FACT]. BV prices to-hit modifiers assuming a base to-hit of 4; real games run 6–8. A Medium Pulse Laser costs **48 BV** but recalculates to **~66 BV** under realistic conditions — ~37% underpriced by one wrong baseline assumption. (Boehmer)
- **BattleTech's headshot bonus** [FACT]. Weapons dealing 60+ damage get a flat 20% BV bonus. The AC/20 and Gauss Rifle qualify; *"the AC/20 receives a huge bonus while potent weapons like AC/10 and PPC get nothing."* A pure cliff with no gradation. (jgf1123 on Medium; proposed fix is a graduated bonus: AC/20 5%, Gauss 3%, AC/10 1%.)
- **BattleTech's linear defensive factor on a non-linear curve** [FACT]. `DefensiveFactor = 1 + TMM/10` is linear, but a +4 TMM unit is hit 41.66% of the time vs 72.22% at +2. Fast jumpers are systematically underpriced. (Boehmer)
- **Dice-curve dependence** [FACT]. Delta Vector: *"a -1 and -2 modifier on 2d6 are not a linear progression like it would be on a d10; the -2 modifier is much more powerful."* Also notes cover halves lethality in both LOTR (16.5%→8%) and Infinity (30%→15%) — an identical mechanical effect worth very different amounts in different lethality regimes.
- **Settlements' own 24" range threshold** [FACT — in-repo sim]. Deployment zones are 24" apart, so a 24"-range weapon fires from its own deployment zone on turn one. *"Uncapped, a long-range crew beat every list by 13–30 points at any price."*
- **40k Strength vs Toughness breakpoints** — the canonical 40k case. [UNVERIFIED] Goonhammer's "Hammer of Math: Toughness Distribution" is the reference analysis but the site blocked automated fetching across multiple attempts; figures circulating in search snippets (T8 at ~2% of competitive points; a +2S bonus on a S4 model improving the wound roll against 43% of units by points) could **not** be confirmed by reading the page. Treat as unconfirmed.

**Mitigations games actually use:** **none of them price it.** Every one caps, gates, or removes.
- Settlements: hard 24" ceiling, gated to Heavy Ranged at Specialist rank with Cumbersome.
- Settlements: damage stops at +4, and only Brutal reaches it; on a ranged weapon Brutal requires Short Range.
- Gutschera rule 1: *"changing costs should be your first thought, and usually your second and third as well"* — **but** rule 12 concedes that some effects *"really can't be costed effectively without doing damage elsewhere to your system,"* and those get rewritten, not repriced.

**Design instruction for Settlements: enumerate every breakpoint in the engine explicitly, and gate each one.** The known list: 24" = deployment distance; net +5 = the 90% ceiling; net −3 = the 10% floor; Damage +4 vs Armour −2; WND 1 (any WND 2 model changes the entire kill-chain math). Write them down as a costing precondition list.

### 6.2 Synergy and combination

**What breaks.** Two components, each correctly priced in isolation, that are broken together. This is the failure mode with the *least* published math and the *most* published practice.

**Real examples:**
- **Magic's reanimator clauses** [FACT — stated by WotC's Director of Development as design practice]. Gutschera, footnote 6: *"That low cost might be right for the object's general use, but a specific use (perhaps in combination with some other unusual objects) might lead to the object needing to cost a great deal more. To preserve the original idea of the object, one needs to tweak the object's effect so that the general use still works but the specific use does not. (For example, in Magic, cards like Darksteel Colossus or Serra Avatar have clauses to prevent their reanimation.)"* **The mitigation is a clause, not a price.**
- **40k "soup"** [FACT]. Chris Morgan, Frontline Gaming (2018): 8th-edition detachments from different factions combined with a shared command-point pool and access to multiple stratagem libraries, with no mechanical penalty for allying. Each codex is designed with intentional weaknesses; soup imports a solution to every one. The "Loyal 32" — a minimum Imperial Guard detachment taken purely for command points, screening and board control — is the named artefact. **The eventual fix was structural (detachment restrictions), not repricing.**
- **The bodyguard problem** [CONSENSUS — designer essay]. Jake Thornton (Mantic): *"powerful shooting units are generally weak in melee. If they are protected by another unit then that weakness can be ignored, and the discount they were given... is now unwarranted."* **A discount granted for a weakness evaporates the moment a separately-priced unit covers that weakness.** This is the single most dangerous synergy pattern for Settlements, because *every drawback in the weapon table is a discount granted for a weakness.*
- **Same ability, different carriers** [CONSENSUS]. BGDF: *"Regular troops and hero units often have access to the same power-up, but have to pay different amounts for it, because of the synergy."*
- **Settlements' own caught case** [FACT — in-repo]. Awkward (may not Move and attack) was cut because it *"is free points on a sniper — he never moves anyway, and it synergises with Accurate, which pays you for standing still."* Two separately-priced components — a drawback and a conditional bonus — whose conditions were the *same condition*. **This is the canonical synergy bug and the design already found it in-house.**

**Mitigations:**
1. **Rewrite the effect with a clause** (Magic).
2. **Restrict the legality graph** (40k detachment rules; BLKOUT's BLKLIST units cannot use Battle Drills / Armory / Force rules).
3. **Scale ability cost by carrier quality** — SoBH's Quality multiplier does this automatically and for free.
4. **Watchlists** (Gutschera rule 7): *"get all the developers in a room and list all the things that people think might be broken. Then assign each one to somebody to test... make sure to listen especially hard to the people she was testing against. If they think it's OK, it probably is. If she thinks it's fair but they all hate it, that's a danger sign."*
5. **The Settlements-specific rule already discovered and worth elevating to a design law:** *"A drawback must bite no matter how you play."* Generalise it: **check every drawback's trigger condition against every bonus's trigger condition. If they overlap, one of them is free.**

### 6.3 Diminishing and accelerating returns

**What breaks.** The Nth point of a stat is not worth the 1st — and the direction of the error flips depending on which stat.

**Real examples:**
- **Accelerating returns on concentration** [FACT]. Gutschera rule 14: *"a ring that adds +3 to four different stats should cost less than a ring that adds +12 to one stat."* Spiking beats spreading.
- **Accelerating returns on durability — "you don't pay to be fat"** [CONSENSUS]. In BattleTech, heavyweights with huge armour/structure and mediocre guns are cheap in BV, because once durability crosses the opponent's damage output its marginal value goes near-infinite. Linear armour pricing cannot express a threshold effect. (Discussed at Scott's Game Room and tabletopbattles.com.)
- **Diminishing returns on repetition** [CONSENSUS]. Thornton: *"A unit of 20 models is unlikely to have exactly the same game value as 2 units of 10 each."*
- **Non-linear combat factors** [CONSENSUS — snippet level]. John's Wargame Page on DBA argues linear pricing of combat factors is unfair because higher factors are non-linearly harder to double.
- **Settlements is the exception, and this is the good news** [INFERENCE — §4.3/4.4]. Because `P = (4+mod)/10` is exactly linear and bounded, **absolute returns to stacking modifiers are flat**, and only relative returns diminish. Settlements has no diminishing-returns problem *within the modifier range*; it has a **cliff** at net +5 and net −3.
- **But Settlements has an accelerating-returns problem it may not have noticed** [INFERENCE]. Current rank costs are 5/8/16/24 for 3/5/7/9 stat points — i.e. **1.67, 1.60, 2.29, 2.67 points per stat point.** The curve already accelerates, correctly (higher ranks also carry skills, Orders, and weapon access). But it was not derived, and the Leader's marginal cost per stat point is only 17% above the Specialist's while the Leader gains a **T3 skill and a second Order** — the two most action-economy-relevant things in the game.

**Mitigations:** build a non-linear vanilla curve explicitly and check it against the actual probability chain (Gutschera rules 5 + 8), then bracket-tune (rule 15).

### 6.4 Conditional abilities

**What breaks.** How much do you discount "+1 but only if you didn't move"?

**Honest finding: no published game or design essay gives a formula for discounting conditionals.** [NOT FOUND] Nobody publishes "conditionals are worth 60%." What the literature does give is three hard constraints:

1. **Hero System's multiplicative structure** is the only published *mechanism* [FACT]:
   ```
   Active Cost = Base Cost × (1 + Σ Advantages)
   Real Cost   = Active Cost ÷ (1 + Σ Limitations)
   ```
   Limitations are listed as negatives but *added as positive numbers* into the divisor. Modifiers move in **±¼ (25%) steps**, ranging to ±2 or more. Two properties worth stealing: **(a)** because it divides, a Limitation can never take a cost to zero or negative — there is a natural floor, unlike subtraction; **(b)** the discount automatically scales with the size of the thing being discounted, so the same "only when standing still" limitation is worth 25% of a cheap trait and 25% of an expensive one.
2. **GURPS' percentage limitations** do the same thing additively-on-a-percentage-base.
3. **Gutschera rule 14 implies designers systematically over-discount conditionals.** If a *free choice between two effects* costs less than 1 mana more than a single effect, then a restriction that bites only sometimes should shave *less* than intuition suggests.

**What games actually do — observed practice rather than published formula:**
- **BattleTech** prices conditionality by *sorting and halving*: past the heat-efficiency budget, a weapon counts at **×0.5**. That is a published, concrete conditional discount — and it is **50%, applied to the components you are least likely to use.**
- **SoBH** prices Heavy Armor at 3 and Shieldwall at 1 — the more conditional trait costs a third as much. [INFERENCE from the price list]
- **Settlements today** prices Accurate (conditional +1 hit) at 3 vs Brutal (unconditional +1 damage) at 4 — an implicit **×0.75**, undocumented and non-generalising.

**Recommendation (detailed in §7.3): replace the implicit subtraction with an explicit, published multiplier ladder.** Three bands is enough: ×0.75 (bites occasionally — "if you did not Move"), ×0.6 (bites often — "at half range or less"), ×0.4 (rarely available — "on the first Charge only"). Then **verify each band against the sim**, because the correct multiplier is the *observed frequency the condition is met*, and the sim can measure that directly. This is the one place where Settlements can do materially better than every published game, because the condition-satisfaction rate is exactly the kind of thing `crew_sim.py` can count.

### 6.5 Opportunity cost and action economy

**What breaks.** Abilities that grant or save an action are worth more than any modifier, and are chronically underpriced.

**Real examples:**
- **Gutschera rule 12 names it explicitly** [FACT]: *"It's always good to get a free attack... getting rid of them often means taking something simple and cool ('gain an extra attack') and turning it into something less elegant."* Free attacks are the archetypal non-scalable effect.
- **BattleTech BV cannot price activations** [FACT]. Boehmer lists "Unit Count Advantage" as a named flaw: more activations is an edge BV does not quantify. His proposed fix is to pair BV limits with unit-count restrictions.
- **BV's perverse incentive** [CONSENSUS]. Giant Battling Robots documents that because BV penalises a lack of heat sinks, **overgunned designs that physically cannot fire all their weapons become BV-optimal** — the Black Hawk Prime is the named example. A costing system paying you to build something the game says is bad.
- **Settlements' own numbers, from two independent methods** [FACT + INFERENCE]: Quick Shot measured at **+24 win%** and **+67% output** in `Skill Sim — Findings`; my own arithmetic (§4.5) puts one extra attack at **81% of the value of maxing every stat and damage cap simultaneously.**

**Honest caveat:** the specific claim that action-saving abilities are *chronically* underpriced across the hobby is **strong community consensus with a genuine evidence gap** — no rigorous published measurement was found. The supporting sources reach the conclusion obliquely (BV can't price activations; Gutschera's non-scalable-effect argument). State it as a prior, not a citation.

**Mitigations games actually use:**
- **Gate, don't price.** Settlements gates multi-attack behind Tier 3 (a stat of +6, Leader-only, campaign-earned) and attaches load-bearing riders ("no Reactions this round" / "no Charge"). The sim explicitly notes: *"without them these are auto-includes."* **This is correct and should be stated as a design law: extra actions are never sold, only earned.**
- **Convert action economy into the numeraire and multiply.** SoBH's Quality is literally an activation stat and is a pure multiplier on the whole cost. BattleTech's pilot skill likewise multiplies.
- **Cap unit count structurally** (Settlements' pyramid; 40k force org; BLKOUT's three-unit slot).

### 6.6 Model count — horde vs elite

**What breaks.** The same points buying 4 elite or 14 cheap models is not equivalent, and terrain density swings it further.

**The theory, with real citations:**
- **Lanchester's square law**: fighting strength scales with the *square* of numbers × per-unit efficiency. Formalised for wargaming as **PN²** (P = hit probability, N = number of troops) by Flanagan, Lambert, Lipscombe, Northey & Robinson, "Lanchester's Fighting Strength as a Battle Outcome Predictor Applied to a Simple Fire and Manoeuvre Wargame" (IntechOpen, 2024). **Empirical result: fighting strength predicted the final result in 33 of 34 wargames with asymmetric forces (~97%).** [FACT]
- **The direct costing implication**: Ernest Adams, "Kicking Butt by the Numbers: Lanchester's Laws" (Game Developer) — *"the aliens will have a force twice as large, but four times as strong, and costing only twice as much."* **Cost scales with N; combat power scales with N². Therefore any linear points system systematically undervalues model count.** [FACT]
- **Two published caveats that stop you from over-correcting** [FACT]:
  1. **Close combat follows the *linear* law; ranged combat follows the *square* law.** Giant Battling Robots: *"no single point system can be correct in every setting."* Also: the square law is driven by **rate of target acquisition**, so anything throttling how many models can acquire targets per turn — LOS blockers, alternating activation, facing arcs, activation limits — drags the exponent back toward 1.
  2. **The square law only describes annihilation.** Historical fits land on a mixture of linear and square, and the laws say nothing about who wins when victory is defined by objectives rather than wiping out the enemy. **Objective-based scoring partially defuses the square law** — which is exactly Settlements' victory condition.

**Net [INFERENCE]:** N² is an *upper bound on the direction of the error*, not a cost formula. The true exponent sits between 1 and 2 — closer to 2 for simultaneous-fire attrition with unrestricted target acquisition, closer to 1 for alternating-activation, LOS-constrained, objective-scored games. **Settlements is at the low end of that range by construction**, which is why its linear costing survives.

**Settlements' answer is already complete, and it is mechanism rather than price** [FACT — in-repo sim]. The 9-Fighter horde, the 11-model pyramid and the 14-model Recruit horde land **within three points of each other at every density**. Four mechanisms do the work:
1. **Reaction banking** — 4 models = 4 banked Ready reactions, so an elite crew effectively shoots twice.
2. **The Stress cascade** — friendly-Down Stress punishes bunching. Softening it pushed Recruit-horde win rates to **93%**. *"The cascade is not a bug; it is the only thing keeping a swarm honest."*
3. **Underdog +1 Priority** as explicit compensation.
4. **WND fixed at 1** — quality has a hard ceiling that numbers do not.

**Plus the finding that dwarfs all of them: terrain density.** *"A 66-point swing from terrain alone. No points value could move a matchup that far."* Spread across eight lists: **11 points on a legal board (9–12 features, ~42% LOS blocked), 34–35 on an illegal one.** [FACT — in-repo]

**Mitigations others use:** structural count caps (force org, BLKOUT's 3-unit slot), alternating activation, objective-over-kill scoring, and super-linear pricing for the Nth model.

**The design instruction:** **the legal board specification is part of the points system.** It should be written into the costing document as a precondition, not left in the terrain rules. A cost derived at 42% LOS-blocked is only valid at 42% LOS-blocked.

### 6.7 The mode nobody lists: context-dependence

**What breaks.** An ability's value depends on the *scenario*, the *opponent*, and the *game length* — none of which the cost function can see.

This is not usually named as a separate failure mode, but Settlements has already measured it twice, in-house, with numbers cleaner than anything published:

- **Stat value is set by the board, not the model** [FACT]. `Dice Mechanic — Sim Findings`: the Objective Grabber wins 24% on bare ground and the Heavy Gunner 69%. `List Building` draws the correct conclusion: *"you cannot price a stat fairly in a vacuum... The board prices stats. Points price bodies and guns."* **AGI and INT are worth literally zero in the combat sim by construction.**
- **Skill value scales with fight length** [FACT]. `Skill Sim — Findings`: Steady and Rattle-Proof measure at **+23 win%** in a WND-3 duel, but *"in a fast WND-1 fight — the common case — Stress rarely reaches 2, so they're worth close to nothing."* Same skill, near-zero to +23 depending on a parameter the cost function never sees.
- **Cover value is inversely proportional to enemy skill** [INFERENCE — §4.7]. Heavy cover removes 50% of incoming hits against a shooter at h=0 but only 22% against one at h=+5.
- **BattleTech's parallel** [FACT]: Gutschera rule 10 makes the general point — *"What's balanced in one environment might not be in another. Thus there's no Platonic perfectly balanced set of items, not even in theory."* His advice: *"pick the environment that puts the most pressure on object balance (this is probably your most competitive environment) and test there."*

**Mitigation:** **fix the environment by decree and cost against it.** Declare a reference scenario — board size, terrain density, round count, objective type, and an assumed opposing stat line — and derive every cost against it. Then *publish the assumption*, so when the meta shifts you know which assumption broke. This is precisely what BattleTech failed to do (it assumed to-hit 4 and never revisited it when play settled at 6–8), and it is the single most avoidable large error in this whole report.

---

## 7 · Per-system profiles

### 7.0 BLKOUT — the honest answer: there is no costing system

**Mechanism: slot currency, not points.** Confirmed, not inferred. The publisher states it directly:

> *"Forget the tedious task of point-counting; in BLKOUT, you simply choose a force and pick three units."*
> — blkoutgame.com/pages/the-game [FACT]

Supporting published detail [FACT]:
- Force construction is slot-based: *"Just choose a force and three Unit cards to form your army"*; *"List building is incredibly simple"*; *"no math or modifiers are required."* Matched play runs 8–12 models per side, scaling to 32+.
- A Matched Play group is a fixed template: `1× Handler Unit + 1× Force Card + 3× different Units from the chosen Force`, one of which may be swapped for a BLKLIST model.
- **Control Points are an in-game resource, not a list-building currency** — 3 per game, spent on Battle Drills, Handler Activation, Chained Activation. There is one list-adjacent use: *"Players may exchange all of their Control Points to replace a Unit in their group with a Duster"* — a mid-game trade, not a purchase economy.
- **The balance levers are access restrictions and card design, not price.** BLKLIST units *"cannot use Battle Drills, Armory Items, or Force Special Rules."* Power Cards are *"intentionally less potent than standard force cards, but they open the door for highly thematic and flexible force-building."*

**What could not be verified.** No unit card face was obtained (the free rulebook sits behind a $0.00 Shopify checkout; mirrors returned metadata only or 403; the fan wiki is deliberately lore-only). So it cannot be stated as fact that *no number* is printed on a card — only that the publisher's own copy explicitly disclaims point-counting and every force-building rule found is slot-and-restriction based. **There is essentially zero public discussion of BLKOUT costing, because there is nothing to discuss** — no Reddit, BGG or RPG Pub thread on balance, no designer interview on costing methodology, no errata addressing unit valuation. [NOT FOUND — stated rather than padded.]

**Verdict.** [INFERENCE] BLKOUT's balance model is **slot currency + legality gating**. Every unit is notionally equal-cost because the currency is the slot. That pushes 100% of balance work into card design and legality restrictions. It is the *opposite* architecture to a derived points system, and it is a legitimate working design — it trades list-building expressiveness for zero costing risk.

**The theoretical objection is in the canonical text, and it is exact.** Gutschera: *"'Everyone gets to bring 16 pieces to the table' is a costing system for choose-your-own-army chess (each piece you bring costs you 1 of your 16 slots) but it's not robust, since players will choose nothing but queens."* [FACT] **That is precisely why BLKOUT must lean so hard on card design and access tiers** — and it is the reason Settlements' points approach buys real expressiveness that BLKOUT cannot.

**What's stealable:** nothing about costing. The transferable lesson is the *negative* one — a slot system removes costing risk entirely at the price of customisation, and Settlements has already chosen the other trade deliberately. The BLKOUT ideas worth stealing are in `BLKOUT-RULES-ANALYSIS.md` §19 and are about reactions and faction identity, not points.

### 7.1 Warmachine / Hordes — the only published account of a points rescale

**This is the most directly relevant precedent in the entire report, because Privateer Press did exactly what Settlements is about to do and said why.** Will Shick, Privateer Press, April 2016, on the MK2→MK3 transition: [FACT]

> *"The adjustment of the point costing system in WARMACHINE and HORDES was one of the first things we knew we wanted to implement in the new editions. After compiling years of data from both internal testing and, more important, from our global community of players, **we knew we needed to introduce a points system that allowed for greater granularity**. We settled on the foundation of doubling the current point system; **however, this initial determination was little more than the first step** on what would be a long, arduous, yet infinitely rewarding journey toward the new points system."*

Two things to take from this:
1. **Granularity was the stated motive, derived from play data.** Exactly Settlements' reason.
2. **The multiplication was the container, not the answer.** They re-costed everything from scratch inside the new space, and called it *"long and arduous."* **Budget for the re-costing pass, not the rescale.**

**And the scale arithmetic is the most useful number here.** [FACT for the figures, INFERENCE for the conclusion] MK2 standard games ran ~35 points; MK3 standard is **75 points** — while all costs doubled. So army *size* stayed roughly constant (×2.1 budget against ×2 costs) and the entire gain went into **resolution**. Community commentary confirms the payoff was felt: MK3 generated a whole essay titled "The Ten Point Problem" about how tight a 10-point band is in a 75-point game — a problem you can only have once your points are granular enough for 10 points to be a real constraint.

**The Settlements implication:** a ×10 rescale should hold crew size constant and spend all of it on precision. If the 100-point crew becomes a 1000-point crew of the same nine-to-eleven models, correct. If it becomes a 1000-point crew of ninety models, the rescale has been misspent.

**Non-points levers** [FACT/CONSENSUS]:
- **Field Allowance (FA)** — a per-entry cap on copies (`FA: 1/2/3/4`, `FA: C` for characters, `FA: U` unlimited), independent of points. Notably, **Theme Forces *raise* FA** for thematically-appropriate units — FA used as a *flavour unlock*, not only a restriction.
- MK3 deliberately **relaxed** FA once costing got better: *"we realized we no longer needed to limit the FA of unit attachments... Instead, we were able to balance them from the ground up."* Replaced with a flat structural ceiling — **max three weapon attachments per unit.**
- **Requisition Points** — *"1 Requisition Point per 25 points of game size,"* spendable only on a short list of free additions. A budget that **scales with game size and is spend-restricted rather than amount-restricted.** Same shape as Infinity's SWC.
- **Warjack/Warbeast Points** — a pool granted by your caster, usable only within their battlegroup.

**MKIV's stated comp philosophy is a warning worth quoting in full** [FACT]. Privateer removed a rule requiring N non-lesser Cohort models by game size, because it *"did not impact all armies equally"* — some factions have cheap light cohorts, others *"completely lack light Cohort models altogether."*

> *"**All Cohort models are not created equal**, and any requirement that treats them as such indulges the larger issue of this inequality."*

They sought *"the most fair and balanced approach to army composition across the armies **without adding more burdensome and complicated army composition rules**."*

[INFERENCE] The transferable lesson: **any structural requirement written in terms of a category smuggles in an assumption that the category's members are interchangeable.** Settlements' pyramid says *"every Specialist requires two fighters of lower rank"* — that is safe precisely because rank *is* the cost tier. A rule saying "you must take two ranged specialists" would not be.

**Is the derivation published?** **No.** [NOT FOUND] Shick describes a data-driven iterative process — *"years of data from internal testing and, more important, from our global community of players"* — plus a scale change and hand rebalancing. No formula, no spreadsheet. Nothing from Jason Soles or Matt Wilson on methodology.

**Community verdict on which edition balanced best: there isn't one, and this report will not manufacture one.** [CONSENSUS] MK3's *launch* was poorly received and is blamed for commercial decline; *late* MK3, after aggressive errata, is regarded positively; a counter-view holds that the errata cadence itself was the problem. **Crucially, nobody argues the granularity was wrong.** [INFERENCE] The rescale is a low-controversy move — the arguments are always about individual costs, never about resolution.

### 7.2 Infinity — the dual-currency reference implementation

**Mechanism** [FACT — official N5.2 wiki]:

> *"Support Weapons are the weapons or Special Equipment not included in the basic or standard equipment. These Support Weapons have a specific cost named Support Weapons Cost (SWC)... **In game terms, each 50 Army Points will provide 1 point of SWC** to spend on Troopers with Support Weapons. For example, in a standard 300 Point game, players will have 6 SWC points available."*

- **Every profile row carries two costs**: `SWC` and `C` (Army Points).
- **SWC granularity is 0.5**; values in use run 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, plus `+1`/`+2`.
- **"+X" profiles *grant* SWC** rather than costing it — *"Troopers whose SWC value has the + symbol will provide the player that many extra SWC points... it will not cost the player any SWC to field these Troopers."* Typically gated behind fielding that model as Lieutenant.
- **Both Cost and SWC are Private Information** — your opponent may not ask what anything costs.
- Stacked alongside: **AVA** (per-unit availability caps), **Combat Groups** (max 10 order-generating troopers each), exactly one Lieutenant, and in N5 a hard **15-trooper cap**.
- **N5 Reinforcements splits the budget in both currencies** — *"assign a total of 100 points and 2 SWC to build their Reinforcements Section, and the rest... to the Main Section."*

**The load-bearing discovery — the same weapon costs more SWC on a better platform** [FACT — figures from the N3 rulebook PDF]:

| HMG carrier | SWC | Points |
|---|---|---|
| Fusilier (PanO line infantry) | 1 | 18 |
| Zhanshi (Yu Jing line) | 1 | 19 |
| Ghulam (Haqqislam line) | 1 | 20 |
| Moblot / Govad | 1.5 | 29 |
| Nisse / Zúyong / Djanbazan | 1.5 | 34–35 |
| Janissary (Heavy Infantry) | 2 | 40 |
| Hsien (HI) | 2 | 61 |
| Squalo (TAG), MULTI HMG | 2 | 93 |

*(Honest counter-example: the Missile Launcher is a flat 1.5 on both a 15-point Fusilier and a 49-point Father-Knight, rising to 2 only on top-tier HI. So platform-scaling is a strong designer **habit**, not a stated rule.)*

**Lieutenant options are priced in SWC, not points**: a Ghulam HMG is SWC 1; the Ghulam *Lieutenant* HMG is SWC 0.5. Joan of Arc as Lieutenant is **+1 SWC** — she pays you. Corvus Belli uses the second currency as the dial for the leader tax rather than touching points at all.

**Is the derivation published?** **No.** [NOT FOUND] No formula, no spreadsheet, no credible community reverse-engineering. Designer Gutier Lusquiños' published reasoning is qualitative and fictional: *"The Red Fury is designed as a light machine gun which is why it costs less SWC. It's more of an anti-personnel weapon than the Spitfire."* Costs are hand-set per profile row and iterated on playtesting. He also notes *"Game balance, translations and checking layout are the three most time consuming tasks."*

**Why two currencies?** [INFERENCE, well-supported] Points alone cannot prevent the degenerate list, because in Infinity the *order economy* makes cheap bodies individually mandatory. A single currency would force the designer to price HMGs so high nobody takes them. SWC lets them price the gun **cheaply in points** (a Fusilier HMG is only +8 points over a Combi) while **hard-capping how many exist**. Points buy bodies and order count; SWC buys the *right to have force-multipliers at all*. Two independent knobs on two independent failure modes.

**Verdict** [CONSENSUS]: it has survived four editions essentially unchanged, which is the strongest evidence available. N4 rebalanced individual values; N5 kept the mechanic verbatim and extended it. The only recurring complaint is that **SWC value is table-dependent** — long-ranged support weapons are worth less on dense terrain — which is the same context-dependence problem as §6.7.

**What's stealable:** the derived-budget pattern (currency #2 = f(currency #1), so it auto-scales); **half-point granularity on the scarce currency and integers on the abundant one**; platform-scaled gate costs; "+X" profiles that grant budget; pricing the leader tax in currency #2.

### 7.3 Malifaux — structural costing, and the best small idea in the report

**Correction to a common belief: M3E did *not* remove upgrade-buying.** Upgrade Cards exist in M3E, carry Costs, and are purchased during hiring. What changed was their scope and volume. [FACT — verified against the official M3E Rules Manual]

**Mechanism** [FACT, all quotes from the M3E Rules Manual]:
- Standard game **50 Soulstones**; models cost roughly **2–15 SS**. Very coarse atoms.
- **The Leader is free**: *"each player must hire their chosen Leader. However, **that Leader's Cost is treated as 0** when hiring."*
- **Totems are conditionally free**: *"If this Master is a Crew's Leader, the Totem's Cost is considered to be 0 during hiring."*
- **Extra Masters are costed as a fraction of game size**: combined cost must be *"less than half this encounter's size,"* and each costs *"the cost of 1 additional Soulstone to hire."*
- **Leftover budget converts to an in-game resource, capped**: *"any unspent points become Soulstones in your Crew's Soulstone Pool. A Crew's Soulstone Pool cannot exceed 10 Soulstones during hiring."*
- **Upgrades are capped at list-building, uncapped in play**: *"During hiring, **any model can pay for and Attach a single Upgrade**. This limit only applies during hiring; there is no limit to the number of Upgrades a model may Attach during gameplay."*
- Upgrade limitation vocabulary: `Restricted (Name)`, `Special (Name)` (cannot be hired, only attached in-game), `Plentiful (X)`.

**The standout idea — the keyword tax** [FACT]:

> *"A player may hire any models that share one or more Keywords with their Leader... Additionally, a player may hire any models that belong to their declared Faction, though **models that do not share a Keyword with their Crew's Leader have their Cost increased by +1 during hiring**. The exception to this rule are models with the **Versatile** Characteristic, which do not have their Cost increased."*

**One flat, tiny, universally-applied modifier makes thematic lists cheaper than optimised ones — without banning anything and without a second price list.** Plus a named exemption (`Versatile`) so the designer can hand-pick which units are meant to travel. This is the cheapest possible implementation of Gutschera's "colour wheel" (§5, rule 3), and it is directly applicable to Settlements' factions.

**The upgrade failure mode, stated by the designers** [CONSENSUS — the quote surfaced via search and the original URL could not be confirmed, so attribute cautiously]: Emissary upgrades were *"generally used as patches to sub-par Masters and were either not impressive enough to see the table or so strong that they became mandatory hires."* Removing them let designers *"focus on making each Emissary good on its own merits."*

[INFERENCE] **This is the atomic-costing failure mode in its purest form: a costed option collapses into "never taken" or "auto-taken," and the band between is narrow.** An upgrade written to patch a weak unit will land on auto-take by construction, because the patch is worth more than its price *by design intent*. M3E's fix was structural — one upgrade per model at hiring — and the deeper fix was to fold auto-take content into the base card so it stops being a purchase decision at all.

**Is the derivation published?** **No.** [NOT FOUND] Wyrd publishes errata that adjust individual Costs, never the reasoning.

**What's stealable:** the **+1 out-of-keyword tax** and its `Versatile` exemption (top of the list); free Leader and conditionally-free Totem so the budget is spent only on real choices; second-leader cost as a *fraction of game size*; leftover budget → capped in-game resource; **one upgrade per model at purchase, unlimited in play**; the tiny `Plentiful/Restricted/Special` constraint vocabulary.

### 7.4 Kill Team — the cleanest natural experiment in the hobby

Same company, same setting, same scale, **three different costing philosophies in six years.** [FACT]

**2018 — full atomic costing.** 100-point cap; *"Each model and each of their pieces of wargear has an associated points cost."* Specialist progression itself is priced: Level 1 +0, Level 2 +4, Level 3 +8, Level 4 +12.
[INFERENCE] **100 points with per-item wargear costs is the worst possible combination: coarse atoms in a tight budget.** Every item is a large fraction of the budget, so a small mispricing is decisive. [CONSENSUS] Contemporary verdict: *"Despite the complex lists and fiddly point values the teams devised were terribly unbalanced, with certain factions dominating others."*

**2021 — points removed for models, retained for gear.** GW's own article title is the thesis: *"New Kill Team Replaces Points With a Fast, Finely Balanced List-building System."* The designers *"effectively **baked your operatives' points values into the way you pick your rosters**,"* with balance from *"restrictions on specialist numbers rather than point calculations."* And a footnote that is the entire industry's attitude to published derivations in one line: *"They have thought about it all quite hard. We've even heard **there's an algorithm**."*

**But points survived for equipment** at a separate budget: matched play gives **10 Equipment Points**. [INFERENCE] **GW did not abolish points in 2021 — they split the problem.** Models structural, gear costed, two budgets. That is a dual-currency system arrived at from the opposite direction to Infinity's.

**The cost of removing per-item pricing, stated cleanly** [CONSENSUS]:
> *"If your operative has the choice between only a bolt pistol and plasma pistol, **there's no reason to ever not pick the plasma pistol** — the stronger option just always wins with no cost involved."*

GW's answer was to remove the *choice* as well as the cost — fixed loadouts.

**2024 — points removed entirely, including for gear.** *"Each player instead may choose **up to four equipment options**... It is important to note that **equipment no longer corresponds to any individual operative**... Each option may only be taken once per battle, and players **alternate setting them up** prior to operative placement."* The universal list is mostly battlefield furniture and consumables — barricades, ladders, ammo cache, razor wire, comms device, mines, grenades.

[INFERENCE] The move is subtle and clever: by **detaching equipment from operatives**, GW turned a *pricing* problem into a *slot* problem. Four slots, each item costs one slot, no numbers to balance — and because items are team-level, the combinatorial interaction with individual operatives (the thing that made 2018 unbalanceable) vanishes entirely. The price paid is that equipment can no longer express "this specific model is kitted differently."

**The arc: atomic → structural → structural-with-slot-budget.** GW ended up back at a resource system; they just made the resource unit-less.

**What's stealable:** **slots instead of prices for the long tail** — "pick 4" is unbreakable, instantly learnable, and needs no balance pass on the budget; reserve real pricing for the things that carry the game. Also: **team-level rather than model-level equipment** kills both the "key model dies, kit wasted" swing and the combinatorial pricing problem in one move; and **alternating placement** turns a list-building decision into an interactive one. And the warning: **if you strip the cost off a choice without stripping the choice, the strictly-better option always wins. If you make something free, make it mandatory.**

### 7.5 Bolt Action — the naive atomic system, and exactly where it breaks

**Mechanism** [FACT — from published cost tables]: per-man body cost priced by troop quality, with weapons as flat add-ons.

| Troop quality | Cost per additional rifleman |
|---|---|
| Inexperienced | **7 pts** |
| Regular | **10 pts** |
| Veteran | **13 pts** |

Confirmed across multiple entries and stable through the 2nd→3rd edition change (*"Regs are still 10pts and Vets are still 13pts"*).

[INFERENCE] **The structure is additive, not multiplicative** — it is *not* `base × veteran modifier`. It is a flat quality-priced body (steps of +3) with weapon upgrades added at a **quality-independent** price. Back-derived the ladder is 0.7 / 1.0 / 1.3, suspiciously clean, but weapon costs being flat regardless of carrier argues against a multiplier being the actual mechanism, and no published statement says otherwise.

**Weapon costs are flat per item — the exact opposite of Infinity's platform scaling.** LMG: 20 pts in 2nd edition, **15 pts** in 3rd. Rifles +2 per model on unarmed Soviet inexperienced bodies at 5 pts each.

**And the failure mode is exactly what the flat structure predicts** [CONSENSUS]: *"you should never take anything other than Inexperienced mortars — you need 6s to hit anyway."* When a weapon's performance is independent of the carrier's quality, paying the veteran body tax is pure waste. **3rd edition's fix was to change the rules, not the price** — giving veteran vehicles a mechanical benefit they previously lacked, *"an attempt to make veteran vehicles more attractive."*

**Other 3rd-edition changes worth noting** [CONSENSUS]: vehicles completely re-costed (a Veteran tank 666 → 528 pts); infantry per-man costs unchanged; support costs cut hard (Regular Forward Observer 100 → 75); the generic platoon selector replaced with **six platoon types** that unlock different unit pools (rated the best change in the edition); standard game 1000 → 1250 pts; and **Germany's unit catalogue cut from "over 200 unit types" to about 50.**

**Is the derivation published?** **No — and Warlord's own forum confirms the vacuum.** [FACT] A player asking exactly this question on the official community forum got no official answer; the only resource offered was an **unofficial fan-made** "Bolt Action Vehicle Design System" PDF. The best advice on the thread: *"If the tanks feel overpowered, hike up the price, test again, and try again until the tank hits a sweet spot in terms of points."*

**But the community does the maths, and it reveals an implicit unit of account** [FACT for the analysis, INFERENCE for the conclusion]. Warlord's own community site hosts an LMG cost-effectiveness piece: *"For the price of two Regular soldiers with rifles (20 points) you add a net **TWO** shots to the squad"* — the gunner and loader lose their rifle shots, so 4 minus 2 = net +2, plus range 24″→36″. Verdict: marginal. **The implicit exchange rate is `1 Regular rifleman = 10 points = 1 shot at 24″`,** and Warlord dropping the LMG to 15 in 3rd edition is consistent with them concluding it was overpriced.

**What's stealable:** the **named atomic reference unit**. Having a public, stated exchange rate ("1 point = 1 tick = 1/10 of a probability step") makes every other price arguable in the open and lets playtesters audit the design. This is the practical face of Gutschera's numeraire, and Settlements should declare one explicitly. Also: **culling the catalogue** — every entry deleted is one you no longer have to cost correctly.

### 7.6 Gaslands — points plus an unbuyable capacity

**Mechanism: dual currency, where the second currency cannot be purchased.** Everything costs **cans** (points) *and* **build slots**; slots are fixed by chassis and cannot be bought. Teams are typically 50 cans. [FACT — Osprey official QRS v3]

Sample: Bike 5 cans/1 slot · Car 12/2 · Truck 15/3 · Bus 30/3 · Tank 40/4 · War Rig 40/5. Machine Gun 2/1 · Minigun 5/1 · Rockets 5/2 · 125mm Cannon 6/3 · **BFG (the biggest gun in the game) 1 can / 3 slots.** Armour Plating (+2 Hull) 4/1 · Extra Crewmember 4/0 (capped at 2× starting Crew) · Nitro Booster 6/0. **Turret mounting = ×3 the weapon's cost.** Crew-fired weapons cost **0 slots**.

**Is the derivation published? No.** [NOT FOUND] No formula anywhere — not on Hutchinson's studio site, not in his 160-episode *Rule of Carnage* design podcast, not in BGG designer threads. Balance came from an iterative community beta; he calls Gaslands Refuelled *"a sort of 1.5 version… nothing's been fundamentally changed, it's just rebalanced and tweaked."*

**One exchange rate is derivable** [INFERENCE from two published facts]: Armour Plating = +2 Hull for 4 cans, and the Prison Car errata reads *"Reduce the cost of this vehicle by 4 Cans… Reduce the hull value of this vehicle by 2."* → **1 Hull ≈ 2 cans, applied consistently in both directions.** But it does **not** govern chassis costs. **Chassis and add-ons sit on different price scales, and the game is fine.**

**The BFG is the design lesson.** [FACT + INFERENCE] Biggest gun in the game, **1 can** — because it eats 3 slots, has Ammo 1, and firing it shoves you backwards, drops you to Gear 1 and adds 3 Hazard tokens. **Price the drawback, not the number.** That is how you put spectacular toys in a game without distorting the economy.

**What's stealable:** points + an unbuyable capacity (slots decouple "how strong" from "how much fits", and cannot be points-optimised around); multiplicative mounts (Turret ×3 stays proportionate on a 2-can MG and a 6-can cannon); **publishing the inverse of your exchange rate to prove it** (+2 Hull/+4 cans *and* −2 Hull/−4 cans makes the rate self-auditing); a zero-slot category as a pressure valve; and the permission to run two price scales without reconciling them.

### 7.7 The Rampant line (Mersey, Osprey) — legibility buys forgiveness

**Mechanism: coarse integer atoms on a very small budget.** [FACT] Lion Rampant 1e/2e and Dragon Rampant 1e = **24 points**, 4–10 units. Xenos Rampant = 24-point detachments.

Lion Rampant 2e archetypes: Elite Cavalry 6 · Elite Infantry 6 · Heavy Cavalry 4 · Heavy Infantry 4 · Archers 4 · Light Infantry 3 · Skirmishers 2 · Levied Infantry 1.

**The atomic layer is real and repeatable**: "Veteran" is **+2 on every archetype it appears on**; Fearsome +2; Bloodthirsty +3, universally. Dragon Rampant is the most explicit build system — base chassis plus purchased Fantastical Rules (Cleric 4, Spellcaster 4, Flying 3, Fear 2, Undead 2, Venomous 1, **Fearful −2**) with a hard clamp: *"no unit's cost may be boosted above 10 points or reduced below 1 point."* Xenos Rampant is strictly `archetype_base + Σ(options)`, **verified arithmetically across 21 independent published unit builds by two authors, all reconciling exactly.**

**But it context-prices where it matters:** Javelins are **−1 on cavalry** and **+1 on foot** — the same widget, priced by its *net swing* on that chassis.

**No fractional costs exist anywhere in the line** [NOT FOUND — checked LR1e, LR2e, DR1e, DR2e and both published and fan Xenos Rampant]. Every cost is an integer. What creates the impression of fine granularity is the routine use of **negative-cost options**.

**The granularity lesson, and it is the most important one for the rescale** [FACT]: Dragon Rampant 2e (Oct 2025) **raised the warband from 24 to 30 points** because *"24 points never quite gave them enough scope to buy the units they wished to field along with the special rules they wanted"* — and grew the upgrade list from 16 to ~48. **He solved granularity pressure by raising the budget, not by subdividing the atom.**

**Verdict** [CONSENSUS]: essentially no balance complaints, because legibility bought forgiveness. The sharpest structural critique, on Xenos Rampant, is the true failure mode of additive systems: *"The points values of basic heavy and light infantry are deceptively low. Once you start adding upgrades the units become expensive."* **A cheap chassis barely constrains anything.**

### 7.8 Horizon Wars — cost as a property of the force, not the unit

**Mechanism.** Five stats; **P (Presence) is simultaneously the unit's points cost and its close-combat value.** [FACT] Conventional elements have fixed profiles with P ∈ 1–3; only mechs and aircraft get a true point-buy budget.

⚠️ **The actual mech construction maths could not be verified** — the rules aren't reachable and no preview shows the Mustering chapter. **Do not treat Horizon Wars as a verified formula-driven system.** What *is* verified from the official errata: **`max_upgrades = P`** — *"An aircraft may have a maximum number of upgrades equal to its P."*

**The genuinely novel mechanism: CHQ repricing.** [FACT] Force construction starts with a free Command HQ whose *type re-prices the entire rest of the roster* — a Heavy Cavalry CHQ discounts Light Cavalry and Heavy Infantry by 1 each — paired with a composition mandate: *"you must have at least one element of the chosen type per 5 points of Battle Force."* **Cost is a property of the element AND the force it sits in.** That produces faction identity from pure arithmetic, with no faction lists to write and maintain — **directly relevant to a settlement/base-building meta-layer.**

**The most honest sentence in the entire research pass** [FACT — official Horizon Wars Errata & FAQ, verbatim]:

> **Q.** *"If I take, say a Hvy Cav or Lt Cav CHQ, I seem to be able to build armies that are much more potent than ones with, say, a Lt Inf CHQ. Is this right?"*
> **A.** *"Yes. HW battlegroups are **not necessarily balanced or fair. This is intentional**… If, however, you'd like a more competitive, balanced gaming experience, try the New Adventures from this book which… **adds intelligence as a handicap system**."*

The designer of a formula-driven construction system stating publicly that the formula does **not** produce balanced forces, that he knew, and that his fix was **a separate handicap layer rather than repricing the atoms.** [INFERENCE] Corroborating: the same designer, moving to skirmish scale in *Zero Dark*, **abandoned points entirely** for a mission-clock/opportunity-cost currency.

**What's stealable:** make the cost stat do double duty (one number, used twice — cost *feels* like a physical property); **gate the upgrade budget off the cost stat** (`max_upgrades = P` kills "cheap chassis + 40 points of bolt-ons" with zero bookkeeping); **pair every discount with a mandate** (discount alone gets exploited; discount + quota produces thematic forces); and if the points won't balance, **ship a handicap layer and say so.**

### 7.9 Games Workshop's published formulas — the ones nobody remembers

**GW's public "we don't use a formula" line is false twice over.** GW published two complete atomic costing engines — both as *player-facing construction kits*, never as an account of its own internal costing. [FACT]

**Rogue Trader (1987)** — a published formula, verified verbatim against two archive scans. Additive per-characteristic deltas from a human baseline (human = **5 points**), then a non-linear multiplier band, then flat equipment. The crucial admission, in GW's own words:

> *"Values worked out from the formula given above tend to **undervalue the larger creatures**. To compensate for this a modifier is applied to any creature whose points value works out greater than 10."*

Bands: 11–15 ×1½ · 16–20 ×2 · 21–30 ×3 · 31–40 ×4 … 91–100 ×10. **Games Workshop identified and patched the super-linearity problem in 1987 and printed the fix.** ⚠️ The per-characteristic modifier table is a graphic destroyed in both OCR passes; the circulating community transcription could not be verified. **The method is published fact; the individual modifier numbers are community consensus.**

**40k Vehicle Design Rules (Jervis Johnson, WD251 2000 / Chapter Approved 2001)** — a full published formula. Buy armour per facing → the **sum of all four facings becomes a scalar budget (36–56) that simultaneously gates hull class, speed class, and the open-top modifier** → add weapons from race-specific charts → apply percentage upgrades (Gun Battery **+50%**, Shorter Barrel **−25%**, Slower Rate of Fire **−25%**, Titan-Killer **+50%**). **Weapons are priced by race AND by Ballistic Skill** — Heavy Bolter +20 at BS4 / +15 at BS3; Lascannon +35/+25. *The same gun costs more on a better shooter.* That is the cleanest published solution to platform-dependence found anywhere.

And the anti-abuse governor is **not mathematical** [FACT]:
> *"it is VITAL that people using the VDR obey 'The Most Important Rule', which is that in order to use a vehicle created with the VDR it MUST be represented by a PAINTED WYSIWYG MODEL."*
> *"Almost all of the arguments I've seen for unlikely 'game-winning' vehicles fall down on the fact that the author is clearly never going to be able to produce a painted wysiwyg model."*

**Jervis Johnson priced abuse in painting labour.** It was still exploitable ("Gatling Lascannon Skimmers"), and when GW revived VDR in 2018 it was restricted to **Open Play only.**

**Warhammer Fantasy (4th/5th)** — no published formula, but a community reconstruction that **validates**: it ships a **16-row residuals table** of GW-published versus computed values (Goblin 2.5/2.5 · Orc 5.5/5.5 · Minotaurs 40/40 · Clanrats 6/6 · Chaos Warrior 24/24.5 · Trolls 65/66.5 · Black Orc 9/10) — most exact, worst error ~7%. Structure: human baseline PV 5, per-characteristic deltas, M > 6 doubles the whole value, characters = base **×5 (Champion) / ×13 (Hero) / ×20 (Lord)**. [CONSENSUS — but the strongest evidence anywhere that **GW was running an internal formula while denying it.**]

**Battlefleet Gothic** — GW's non-use is explicitly documented in the community formula's own introduction: *"Games Workshop themselves used absolutely no 'points formula' for creating their ships."* The semi-official **Smotherman Formula** (published in GW's own *BFG Magazine #2* but *"never made official"*) is purely linear-additive — Hits 5 · Shields 10 · Turrets 5 · Weapons Battery at 30/45/60cm = **1.5 / 3 / 4.5** per Strength (exactly ×1/×2/×3) — with faction identity as **override layers** (Eldar double their Hits cost, double their speed cost, and pay a **+15 "too many weapons on too small a ship" surcharge**).

**Epic / NetEA — the most important negative result in the report** [FACT]:
> *"Applying points costs in Epic is more of an art than a science."*
> *"It's to do with the way the attributes of a unit fits in **both with any formation it belongs to and with that formation's place in an army**."*

Points attach to **formations in army context**, so unit cost is **not separable** from what it's bundled with. **This is the clearest articulated argument against atomic costing in the whole corpus, and the lesson is: if your units are only meaningful inside a container, cost the container.**

**Necromunda — the sharpest idea for a campaign game** [FACT for the structure]. Base fighter and weapon costs have no published derivation. **But the advancement table is a genuine published marginal-cost table** — GW prints what one point of a stat costs in credits — and N18 publishes an **escalating XP cost: each advance costs base XP +2 per prior advance.** *(Specific credit figures need a rulebook check; the existence of the published column is certain.)*

> **Necromunda solves the derivation problem by only ever publishing *deltas*, never the absolute derivation.** Base costs stay hand-tuned and opaque; growth is fully transparent and rules-legible. You get a designer-controlled starting point *and* a player-verifiable progression system, and you never have to defend a global formula.

### 7.10 Trench Crusade — a modern dual-currency campaign economy

*(Tuomas Pirinen — lead designer of Mordheim — with Mike Franchina and James Sherriff. Primary sources read directly.)*

> ⚠️ **Version warning.** Trench Crusade is in open playtest and **every page of v1.6.3 is stamped PLAYTEST RULES.** Two revisions were read for this report and they disagree on several numbers; both are flagged inline. Pirinen's own foreword: *"these are not the final rules… due to the constant cycle of playtesting and revisions, there are bound to be mistakes as well as plenty of rules that are going to change."* **Treat the structure as the finding and every individual number as provisional.**

**Build currency: Gold Ducats.** A campaign warband starts at **700 ducats** [FACT]. Equipment is atomically priced with a **`LIMIT: N`** tag, and price and cap are carried side by side on every entry.

**Complete New Antioch armoury (v1.6.3, cross-checked against the BattleScribe `.cat` — the two agree on every item)** [FACT]:

| Ranged | Ducats | LIMIT | | Melee | Ducats | LIMIT |
|---|---:|---|---|---|---:|---|
| Molotov Cocktail | 5 | — | | Trench Knife | 1 | — |
| Pistol | 6 | — | | Bayonet | 2 | — |
| Grenades | 7 | — | | Trench Club | 3 | — |
| Bolt Action Rifle · Shotgun | 10 | — | | Sword/Axe | 4 | — |
| Semi-Auto Rifle · Auto Shotgun | 15 | —/2 | | Shotel | 5 | — |
| Incendiary Grenades · Satchel Charge | 15 | 2 / 3 | | Polearm | 7 | — |
| Heavy Shotgun · Automatic Pistol | 20 | 2 / 3 | | Great Hammer/Maul | 10 | — |
| SMG · Grenade Launcher · Flamethrower | 30 | 2 / 2 / 3 | | Great Sword/Axe | 12 | — |
| Sniper Rifle | 35 | 3 | | Lochaber Axe · Misericordia | 15 | — / 1 |
| Automatic Rifle | 40 | **1** | | Tank-Splitter Sword | 15 | 3 |
| Machine Gun | 50 | 2 | | | | |
| Heavy Flamethrower | 55 | **1** | | | | |

Armour and kit: Trench Shield 10 · Standard Armour 15 · Reinforced Armour 40 (ELITE only) · Machine Armour 50 (LIMIT 1, ELITE only) · Gas Mask / Shovel / Medi-Kit / Helmet 5 each · Musician's Instrument 15 (LIMIT 1) · **Troop Flag 1 Glory · Martyrdom Pills 1 Glory (LIMIT 2) · Field Shrine 2 Glory.**

**Troop costs are per-model with `0-N` roster caps** [FACT — Heretic Legion]: Wretched 25 · Trooper 30 (→ Legionnaire +10, capped at half your Troopers) · Chorister 65 (0-1) · Priest 80 (mandatory, exactly 1) · Death Commando 90 (0-1) · Artillery Witch 90 (0-2, and *only* in a warband worth over 1000 ducats) · Anointed Heavy Infantry 95 (0-5) · War Wolf 140 (0-1). New Antioch: Yeoman 30 · Shocktrooper 45 · Sniper Priest 50 · Trench Cleric 60 · Combat Medic 65 · Lieutenant 70 (mandatory) · Combat Engineer 80 · Mechanized Heavy Infantry 85.

**Note the cap that keys off warband value** — *"You may include 0-2 Artillery Witches in a warband worth more than 1000 ducats."* [INFERENCE] **A roster cap gated on total force value is a third dial beyond price and LIMIT**, and it is how you let a capability exist at high budgets without it distorting small games.

**The campaign power curve is a published fixed schedule, not an emergent one** [FACT]. ⚠️ **The two revisions disagree** — v1.6.3 is a flat +100 per battle over 12 battles; the campaign-rules revision read earlier accelerates and reaches 2200 over 11:

| Battle | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Threshold (v1.6.3)** | 700 | 800 | 900 | 1000 | 1100 | 1200 | 1300 | 1400 | 1500 | 1600 | 1700 | 1800 |
| **Max Field Strength (v1.6.3)** | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 22 |
| *Threshold (earlier revision)* | *700* | *800* | *900* | *1000* | *1100* | *1250* | *1400* | *1550* | *1750* | *1950* | *2200* | — |

[INFERENCE] The **Max Field Strength** track is the more interesting of the two and was missed on the first pass: **a separate published ceiling on model count that rises alongside the budget.** Budget and headcount are capped independently, so a player cannot convert a rising budget purely into bodies. That is a direct structural answer to the Lanchester problem in §6.6.

**Everyone's ceiling rises on the same schedule regardless of who is winning.** Resupply also scales with battles fought, not with performance.

**The rubber-band has a real, stated price** [FACT]. To rebuild up to threshold you must: *"Forego Exploration Phase completely"*, *"Give up/Sell all Weapons, Armour and Equipment that is not assigned to any of your models"*, *"Empty your Warband treasury of all ducats"*, and *"Do not keep any leftover ducats."* **Catching up is always available and always costs you the upside phase.** That is a far better anti-snowball design than a win-rate-scaled handicap, because the losing player *chooses* it.

**Veteran inflation is capped structurally, not priced** [FACT]: a warband may have **a maximum of 6 ELITE models** (7 with the Bad Company skill); ELITE models have **exactly two Battle Scar slots and die on the third**; promotion is a dice pool (1 die if you lost, 2 if you won, +1 per Glorious Deed, max 2 per model, promote on a 6, **only one promotion per battle**). Some models carry a **Limited Potential** keyword — a hard cap of 3 Skill Advancements — and some *"cannot be promoted"* at all. ⚠️ *Revision conflict: the earlier text reads "You can NOT dismiss any warrior from your warband"; v1.6.3 reads "You can dismiss any warrior you wish after the battle if they have 2+ Scars." The no-culling rule appears to have been relaxed to a scar-gated release.*

**And the decision that matters most: Trench Crusade never re-prices veterans.** [FACT — unambiguous] The post-battle sequence defines warband value verbatim as *"the total cost in Ducats of **all your models and their weapons, armour and equipment**."* Experience, Skill Advancements and ELITE promotion are **not in that formula.** A Lieutenant with 18 XP and six skills counts against the 700-ducat ceiling at exactly the 70 ducats he cost on day one.

[INFERENCE] The consequences are structural and deliberate:
- **Advancement is free power.** The Threshold ladder limits models and gear only; skill growth is unbounded by the economy and gated purely by the 6-ELITE cap and by models actually surviving.
- **Two models at identical ducat cost are not equal.** The one that has fought ten battles is worth far more, for free. That is a campaign-attachment mechanism — your veterans are precious *because* the ledger doesn't tax them.
- **Injuries drain ducats without inflating value:** one Trauma result reads *"you must deduct 10 ducats from your Paychest… This payment does not count towards your Warband's Threshold Value."*
- **Glory purchases dodge the ceiling entirely**, because Threshold is measured in ducats and Glory Items have no ducat price. **Glory is the deliberately uncapped power axis.**

> **This is the opposite of Settlements' current design**, where *"Each Advance a fighter carries adds +2 points to its cost."* Both are defensible: Settlements taxes veterans so they crowd out rookies (an anti-snowball valve); Trench Crusade lets them run free and caps the *count* instead. **What you should not do is half of each.** Pick the valve — price or cap — and let the other axis run.

**Faction rules modify the economy itself, not just the stats** [FACT — Knights of Avarice]: *"Your force may have no models that cost less than 80 ducats (including their equipment)"* — a **minimum** model cost as a faction identity; plus banned keywords (*"No weapon with the Keyword FIRE or SHRAPNEL"*), a cross-faction unlock (*"you can select one Weapon, suit of armour or piece of equipment type from New Antioch and from Sultanate Equipment lists each"*), and a hard exclusion (*"Knights of Avarice may include no Death Commandos"*).

**Every item carries two independently-tuned dials, and the errata prove it** [FACT — Trench Crusade V1.4 Change List, read directly]. The same patch adjusts *prices* and *caps* as separate levers:

| Change | Dial adjusted |
|---|---|
| *"Viscera Cannon: Cost reduced to 50 ducats"* | price |
| *"Putrid Shotgun: Cost reduced to 20 ducats"* | price |
| *"Flamethrower: 30 ducats"* · *"Alaybozan 10 ducats"* | price |
| *"Grenade Launcher: New **LIMIT: 2**"* | cap |
| *"Alba: Sniper Priests are **0-1, not 0-2**"* | cap |
| *"Black Grail Musician's Instrument: Cost 15 ducats. **LIMIT: 1**"* | both, together |

[INFERENCE] **Two orthogonal dials per item means a designer can fix "too strong" without making it unaffordable, and fix "too common" without making it weak.** A single price has to do both jobs at once and does neither well. Note also the third notation — **`0-N` unit caps** on roster entries, distinct from item `LIMIT: N`.

**How `LIMIT` actually works — per warband, persistent, and breakable** [FACT, two verbatim statements]:

> *"**LIMIT (X):** You can only purchase as many of this piece of equipment… as indicated by the number in parenthesis **for your warband**. **If you find more via looting/exploration, you can break this limit.**"*
> *"…If you lose any of these weapons during the campaign, you can buy replacements with available funds up to a maximum of two."*

So it caps **purchasing**, not possession; it persists across the whole campaign; **Allies are exempt** (*"a mercenary's equipment never counts toward the LIMIT"*); and the BattleScribe encoding separates it cleanly from the per-model rule — `max=N:selections/roster` is LIMIT, `max=1:selections/parent` is "one gas mask per model". [INFERENCE] **A cap on acquisition that loot can exceed is a genuinely clever middle path**: it constrains list-building without forbidding the narrative moment where you take the enemy's machine gun off the field.

**Glory Points buy what ducats cannot** [FACT]. The core rules are explicit: *"Glory Points… can be used to purchase powerful troops and famous warriors known as Allies… **They cannot be purchased with ducats** – the only way to attract their services is to perform glorious deeds on the battlefield!"* Glory Items are effects with no ducat equivalent anywhere — armour that defeats armour-ignoring attacks (Damascus Armour, 5 Glory), a weapon that chains between targets (Locust Spitter, 6), and one that removes a model from the game outright (Beelzebub's Embrace, 20).

**Glory is earned by named deeds, first-come-first-served** [FACT]: *"Players score one Glory Point for every model that completes any of the following Glorious Deeds. Victory Points for these can only be gained once – whichever player completes them first gets the Glory!"* — Sniper, Sharpshooter, Lord of War, Blood Sacrifice, Suicidal Bravery, King of the Hill, Kill their Leaders, and ~20 more. [INFERENCE] **Glory is a currency you earn by playing dramatically rather than efficiently**, and because deeds are claimed once per campaign it is inherently self-limiting — the second player to do a thing gets nothing.

**The only stated exchange rate is a single data point**: one exploration result lets you *"sell the book for either 150 ducats or 5 Glory Points"*, implying **1 Glory ≈ 30 ducats** [FACT for the quote, INFERENCE for the ratio]. The designers never state a general conversion, and everything else suggests they deliberately avoid one.

**Is there a formula? Melee yes; ranged no — and this is the most interesting single finding in the section.** [INFERENCE, with the working shown]

Taking Trench Club (3 ducats, 1-handed, no modifiers) as baseline and deriving increments from controlled pairs — CRITICAL = +1 (Sword/Axe 4), Ignore Shield = +1 (Shotel 5), anti-charge ≈ +4 (Polearm 7) — then predicting two weapons **not** used to fit anything:

- **Great Sword/Axe** = Great Hammer 10 + CRITICAL 1 + "+1D Injury" upgrade 1 = **12**. Published: **12** ✔
- **Lochaber Axe** = Great Hammer 10 + CRITICAL 1 + anti-charge 4 = **15**. Published: **15** ✔

Two exact out-of-sample hits with the anti-charge increment derived from a different weapon pair. **Melee costs are built, not eyeballed.**

Ranged has exactly one clean increment — **ASSAULT = +5**, confirmed on two independent pairs (Bolt Action 10 → Semi-Auto 15; Shotgun 10 → Auto Shotgun 15) — and then collapses:
- **Attacks are non-linear.** The second attack costs +25 (Semi-Auto 15 → Automatic Rifle 40); the third costs about +15 (Machine Gun 50, 3 attacks). *Decreasing* marginal cost, which no additive formula produces.
- **Range is not priced at all.** Flamethrower (8") is 30 and Sniper Rifle (48") is 35 — a 6× range difference for 5 ducats.
- **The variable that actually predicts ranged cost is LIMIT.** Every New Antioch weapon at 30+ ducats carries a LIMIT tag; no weapon at 15 or below does.

**And the clincher against any universal formula: the same profile is priced in different *currencies* for different factions.** [FACT] Automatic Rifle = **40 ducats (LIMIT 1)** for New Antioch and **2 Glory (LIMIT 2)** for the Heretic Legion. Submachine Gun = 30 ducats / 2 Glory / 25 ducats depending on faction and variant. Martyrdom Pills = 1 Glory (New Antioch) or 20 ducats (Trench Pilgrims). **No function of range, dice and keywords outputs both "40 ducats" and "2 Glory Points" for one identical profile.** Currency choice *is* the balancing lever.

**Faction variants rewrite the economy wholesale** [FACT] — far beyond the one example found on the first pass:

| Variant | Economic rule |
|---|---|
| **Knights of Avarice** | *"Your force may have no models that cost less than 80 ducats (including their equipment)"* — a **minimum** model cost |
| **Papal States Intervention Force** | Recruited with *"**500 ducats and 11 Glory Points**"*; Threshold calculated at **−200 ducats**; **+4 Glory every time it takes Reinforcements** — a wholesale swap of one currency for the other |
| **Procession of the Sacred Affliction** | Holy Icon Shields become **20 ducats and universal** instead of **2 Glory and ELITE-only** |
| **A Heretic light-infantry variant** | Submachine Guns become **25 ducats** instead of 2 Glory |
| **House of Wisdom** | *"treats Alchemist Armour as if they had a LIMIT of 2"* — a variant rewriting a LIMIT value |
| **Heretic Wretched** | *"None of their weapons, armour or equipment can cost more than **10 ducats** each"* — a per-model spend ceiling; and uniquely *"can be sold… for their **full** ducat value"* |
| **Trench Pilgrims** | A dead Pilgrim may be re-bought as a Martyr-Penitent for **45 ducats** — paid resurrection |

Universal floor rules: **sale value is half base, rounding up** *"including Glory Items"*; **death destroys gear** (*"It is not possible to reallocate fallen warriors' weapons or equipment once they die"*); loot income is **10 × Exploration Score in ducats**.

**Is the overall derivation published? No** [NOT FOUND] — and **no Mordheim comparison appears anywhere** in the rulebooks despite Pirinen having designed it. The single authorial remark on the design is: *"I firmly believe it is the best ruleset I've written in my 27-year career as a professional game designer."*

**What's stealable — this maps almost one-to-one onto the Settlements campaign design:**
1. **A published, fixed threshold schedule** so the campaign power curve is identical for every player and known in advance.
2. **A rubber-band the losing player opts into at a real cost** (skip your upside phase, empty your treasury) rather than an automatic handicap.
3. **`LIMIT: N` alongside the price on every item — independently-tunable dials.** Trench Crusade's errata adjust price and cap separately (Viscera Cannon cost → 50; Grenade Launcher LIMIT → 2), which lets you fix "too strong" without making something unaffordable, and "too common" without making it weak. A single price has to do both jobs and does neither well. In total they run **four** dials, and it is worth copying all four: **price**, **`LIMIT: N`** (per-warband purchase cap), **`0-N`** (roster slots), and **value-gated caps** (*"0-2 Artillery Witches in a warband worth more than 1000 ducats"*) — the last lets a capability exist at high budgets without distorting small games.
   **And make the cap a purchasing cap, not a possession cap.** Trench Crusade's LIMIT explicitly says *"If you find more via looting/exploration, you can break this limit."* That constrains list-building while still permitting the narrative moment where you take the enemy's heavy weapon off the field — exactly the texture a settlement campaign wants.

3b. **Cap budget and headcount on separate published tracks.** Trench Crusade v1.6.3 runs a **Max Field Strength** ladder (10 → 22 models) alongside the ducat Threshold. **A player cannot convert a rising budget purely into bodies.** This is a direct structural answer to the Lanchester problem (§6.6) and it costs one extra column on a table.
4. **A hard cap on veteran count** (6 ELITE) plus a **finite veteran lifespan** (2 scars then death). Settlements currently handles veteran inflation with a +2/−2 price nudge; Trench Crusade handles it with a ceiling and a clock, which is more robust.
5. **No roster culling.** Prevents the optimise-by-deletion exploit that a persistent roster otherwise invites.
6. **Faction rules that edit the economy** — minimum model cost, banned keywords, cross-faction unlocks. Cheap to write, strongly flavourful, and exactly the "colour wheel" Gutschera prescribes (§5, rule 3).

### 7.12 Frostgrave & Stargrave — two currencies that never touch

*(Joseph A. McCullough, Osprey. Primary sources read directly from the user's Drive.)*

**The headline structural finding: gold and experience are two economies with no exchange rate between them.** [FACT] Gold buys **bodies and items**. Experience buys **stats, spells and powers**. There is no way to buy a stat with gold and no way to buy a soldier with XP. **This is Settlements' own "points buy bodies and guns; stats and skills are free" principle, implemented as two hard-separated currencies** — and it is worth noting that a designer with ten years of campaign-game shipping arrived at the same conclusion independently.

**Budget: 400 gold crowns (Frostgrave) / 400 credits (Stargrave).** [FACT] The wizard/captain is **free**, their gear is **free**, spells and powers are **free** (limited by slots and count, not price). The budget covers only the apprentice (100gc) and soldiers. Warband cap **10 figures — leader + second + 8 soldiers, max 4 specialists.**

**The published price ladders** — note how few price points exist. Frostgrave: **Free / 10 / 50 / 75 / 100 / 125**. Stargrave: **Free / 10 / 20 / 50 / 75 / 100 / 150**. [FACT]

| Frostgrave soldier | Cost | | Stargrave soldier | Cost |
|---|---|---|---|---|
| Thug, Thief | **Free** | | Recruit, Runner | **Free** |
| War Hound | 10 | | Guard Dog | 10 |
| Infantryman | 50 | | Hacker, Chiseler | 20 |
| Man-at-Arms, Apothecary | 75 | | Sentry, Trooper | 50 |
| Archer, Crossbowman | 75 *(specialist)* | | Codebreaker, Casecracker, Commando | 75 *(specialist)* |
| Treasure Hunter, Tracker | 100 *(specialist)* | | Medic | 100 |
| Knight, Templar, Ranger, Barbarian, Marksman | 125 *(specialist)* | | Sniper, Grenadier, Burner, Gunner, Pathfinder | 100 *(specialist)* |
| | | | Armoured Trooper | 150 *(specialist)* |

[INFERENCE] The implied curve is legible even though no formula is published: Free = one good stat and nothing else; 50 = +3 Fight; 75 = +3 Fight *plus* protection, or a second good stat, or a utility role; 100 = two good stats; 125 = +4 Fight or a broad three-stat profile. Roughly **25gc per meaningful stat step**, with a deliberately flat but playable free tier.

**Is the derivation published? No — and this is a firm negative, not a gap.** [NOT FOUND] The only justification given is in-fiction (costs are "retainers"; specialists "require larger retainers and positions of authority"). The "Why A Second Edition?" designer essay discusses spell rebalancing in detail — ~20 of 80 spells were *"too weak or too situational"* — and **never mentions soldier pricing.** McCullough also states the game *"is less concerned with being a tactical exercise"* than with *"a shared sense of fun and adventure."*

**The two-stage constraint — a genuinely elegant piece of design** [INFERENCE, from published numbers]. 400gc minus the 100gc apprentice leaves **300gc for 8 soldiers — 37.5 average.** You cannot fill your 4 specialist slots at creation: 4 × 125 = 500gc on its own. The natural level-0 build is 100 + (4 × 75) + 4 free = exactly 400. **The specialist cap is not the binding constraint at creation — the budget is. The cap only starts biting several games into the campaign, once treasure accumulates.** Two constraints that take turns being the real one. Directly relevant to a settlement layer sitting on top of point-buy.

**Soldier stats never improve.** [FACT] Only the leader and second level up. *"The only way a soldier can improve is through carrying better gear."* A hard structural answer to veteran inflation: **the rank and file simply never inflate.**

**The improvement throttles — and Stargrave's fix to a Frostgrave exploit** [FACT]:

| | Frostgrave | Stargrave |
|---|---|---|
| XP per level | 100 (max 300 XP/game) | 100 (max 300 XP/game) |
| What a level buys | **Player chooses**: stat, spell improvement, or new spell | **Dictated by level number** on a fixed 10-step rotation |
| Throttle | Only **one** stat improvement and **one** spell improvement per game, even with multiple levels banked. New spells unlimited. | Per ten levels: 6 activation-number reductions, 2 stat bumps, 1 new power, 1 free choice |

[INFERENCE] Frostgrave's throttle rate-limits *depth* while leaving *breadth* unlimited — you can bank levels and dump them into spell variety, but not into raw power. **Stargrave removes the choice entirely**, which kills the "bank levels and spike one thing" exploit at the cost of player agency. Two different answers to the same problem, by the same designer, five years apart.

**The anti-snowball suite — five real mechanisms** [FACT]:
1. **Attrition tax.** Soldier Survival: **1–4 Dead, 5–8 Badly Wounded, 9+ Full Recovery.** A flat 20% death chance per downed soldier forces continuous re-spend — and the winner, who fought more, pays more. *(Stargrave softens this: Badly Wounded soldiers still play at half Health rather than missing a game.)*
2. **Injury gold sink.** A Badly Wounded spellcaster costs **150gc** or misses the next game; debt is allowed but **blocks all other spending until repaid**.
3. **Buy/sell spread on everything.** Grimoire **buy 500 / sell 200**. Scroll **buy 250 / sell 30** — an **88% haircut**. Wealth cannot be efficiently liquidated and re-deployed.
4. **A hard XP cap of 300/game.**
5. **The Level Difference Encounter Level Table** — and it is the interesting one:

| Level difference | Result |
|---|---|
| ≤ 7 | Play as written |
| 8–10 | A Level 1 random creature |
| 11–14 | A Level 2 creature |
| 15+ | A Level 3 creature |

**The lower-level player controls the creature** and it fights as a warband member. [INFERENCE] **This is an asymmetric ally handed to the underdog, not a nerf applied to the leader** — the winner's army is never touched, so their progress never feels confiscated. That is a materially better feel than a handicap, and it is the mechanism Settlements should copy for its underdog rule.

**The settlement-layer find: a base resource that edits the price list.** [FACT] Frostgrave's base is free; resources are bought once each. Among them:

| Resource | Price | Effect |
|---|---|---|
| **Carrier Pigeons** | **50gc** | **All soldiers cost 10gc less** |
| Kennel | 400gc | One war hound **above** the 8-soldier limit |
| Celestial Telescope | 250gc | +5 to one Initiative Roll per game |
| Summoning Circle | 300gc | Summoned demon **doesn't count against warband size** |
| Scriptorium / Giant Cauldron / Crystal Ball | 200–250gc | +1 use of a specific out-of-game action |

[INFERENCE] **This is exactly the mechanism the Settlements structure catalogue needs, and it comes in three distinct flavours worth separating deliberately:** resources that **change prices** (Carrier Pigeons), resources that **raise a structural cap** (Kennel, Summoning Circle), and resources that **grant an action or a one-off battle effect** (Telescope, Scriptorium). The first two are economy edits; the third is a battle effect. A structure catalogue that mixes them without naming which is which will be very hard to balance.

⚠️ **Truncation:** the Stargrave extract ends at p.79. The entire "Spending Loot" chapter — campaign soldier re-hire costs, advanced technology prices, ship upgrades — is **unrecoverable from that file**, and no Stargrave equivalent of the level-difference catch-up rule was found. Whether one exists is unknown and is not guessed at here.

### 7.13 Rangers of Shadow Deep — the archetype pattern, and the best idea in the report for factions

*(McCullough again. Solo/co-op. Primary source read directly.)*

**There is no currency at all.** [FACT] Nothing is bought with gold. Treasure results of "Gold and Jewels" convert to **+10 XP or 1 companion Progression Point** — never to purchasing power.

**Ranger build: 10 Build Points on a fixed base** (M6 F+2 S+1 A10 W+4 H18): [FACT]

| Purchase | Cost | Max BP in category | What 1 BP buys |
|---|---|---|---|
| Stats | 1 BP | **3** | +1 to one stat (**Armour can never be raised**) |
| Heroic Abilities & Spells | 1 BP | **5** | one ability *or* one spell |
| Skills | 1 BP | **5** | **+1 to eight different skills** |
| Recruitment Points | 1 BP | **3** | **+10 Base Recruitment Points** |

**The sub-caps total 16 BP against a 10 BP budget — the build is deliberately over-subscribed.** [INFERENCE] That is what forces a real choice: you cannot max any two categories.

**Companions are bought with Recruitment Points, recalculated before every mission, and cannot be banked.** [FACT] Base RP = 100, with the ranger's Leadership skill added to the *Total* after scaling. Companion prices run Hound 5 · Recruit 10 · Arcanist 15 · Archer/Guardsman/Man-at-Arms/Rogue 20 · Swordsman 25 · Tracker 30 · Barbarian/Knight/Savage/Templar 35. **The Conjuror is the only à-la-carte entry in the list** — 20 RP for two spells, 30 for three.

**Solo/co-op difficulty scaling — and the mechanism is the opposite of what you'd expect.** [FACT] There is **no formula that scales enemies to the Ranger's level.** What exists is:

| Players | Total RP | Max companions | Max activated in Ranger Phase |
|---|---|---|---|
| 1 | 100 | 7 | 2 |
| 2 | 40 | 3 | 1 |
| 3 | 30 | 2 | 0 |
| 4 | 10 | 1 | 0 |

**The formula-driven lever scales the players DOWN, not the enemy up.** Total party headcount stays near-constant at ~8 figures regardless of player count, while *quality* rises. Difficulty is otherwise handled by a **binary, hand-authored per-scenario "Challenge Level"** — a fixed lump of extra enemies written individually for each scenario, explicitly *"recommended for games featuring 3 or 4 players."* [INFERENCE] **Even in a game with no opponent to balance against, McCullough did not build a scaling formula — he wrote the harder version of each scenario by hand.** That is a strong data point for the "declare a reference environment and hand-tune against it" recommendation in §8.7.

Note the interaction [INFERENCE]: at 4 players a maxed 130-BRP ranger gets 13 RP against a fresh ranger's 10, so **the entire Base-RP reward track is worth ~90% less at 4 players**, while Leadership — added flat after the multiplication — becomes proportionally far more valuable. A scaling multiplier applied to one term and not another silently re-prices every reward downstream of it.

**And the single most transferable idea in this whole report — the archetype pattern.** [FACT] An archetype is *"a framework placed on top of the character generation rules."* It replaces the base stat-line, grants free Traits and Limitations (*"their cost has already been factored into the balance of the archetype"*), and **usually reduces the Build Point total below 10** *"which offsets the value of some of their special abilities."*

| Archetype | BP | Notable base-line change | Max BP→RP |
|---|---|---|---|
| *Standard Ranger* | **10** | — | 3 |
| Chthonian Mage | 10 | — | **1** |
| Servant of Seth | 9 | Will +5 | 1 |
| Varakian Archer | 9 | Fight +1, Shoot +2 | **2** |
| Red Hawk Knight | **8** | Fight +3 | 1 |
| Wasteland Firesword | **8** | Fight +3 | 1 |

> **The unit costs never change.** 1 BP always equals +1 stat / one ability / +1 to eight skills / +10 RP. **Archetypes are priced entirely by adjusting the budget and the per-category sub-caps — nothing in the catalogue is ever repriced.**

[INFERENCE] **This is the answer to how Settlements should build factions.** Ten distinct archetypes, all sharing one price list, differentiated purely by an 8–10 point budget and which sub-caps are loosened or tightened. It scales to any number of factions **without a costing audit each time** — which is precisely the cost that makes faction design expensive in every other game examined here.

**One more pattern worth naming: the same thing costs different amounts at different times.** [FACT] +10 Base RP costs **1 BP out of 10** at creation but **a whole level (100–1000 XP)** afterwards. Skills cost 1 BP for **+1 across eight skills** at creation but a whole level for **+5 total, max +2 each** later. **Character creation is dramatically more point-efficient than levelling.** [INFERENCE] A deliberately front-loaded curve: it makes the initial build feel generous and makes long-run progression slow enough that veterans don't run away with the campaign.

### 7.14 Warhammer 40,000 — the full arc, and the most decision-relevant case study in the report

**This is the one to read if you only read one profile.** It is a 25-year controlled experiment on the exact question Settlements faces: *should gear cost points at all?* GW tried every answer, in order, at enormous scale, with published reasoning.

**The arc:** per-item costs on every entry (3rd–7th) → per-item costs **plus** a parallel coarse system (8th) → per-item costs quietly deleted faction-by-faction (9th) → **all wargear free** (10th) → **selective costs return on outlier weapons only** (11th, June 2026).

#### The failure of per-item costing — and it is worse than "the same weapon cost different amounts in different codexes"

[FACT — read from archive.org codex scans] **The same weapon cost different amounts on different units inside a single book.** Codex: Space Marines, 4th edition (2004):

| Weapon | Tactical Squad | Veteran Squad | Command Squad | Gun Servitors |
|---|---|---|---|---|
| Heavy bolter | **+5** | +5 | **+15** | +15 |
| Missile launcher | +10 | +10 | **+20** | — |
| Multi-melta | +10 | +10 | **+20** | +25 |
| Lascannon | +15 | +15 | **+35** | — |
| Plasma cannon | +20 | +20 | **+35** | — |
| Flamer / meltagun / plasma gun | +6 / +10 / +10 | same | same | — |

Spread on identical wargear: **heavy bolter 3×, multi-melta 2.5×, lascannon 2.33×** — while flamers and meltaguns were flat everywhere. **The inconsistency wasn't even systematic.** The 3rd-edition codex shows the same pattern independently, and the flamer actually *inverts* between editions.

[INFERENCE] The design logic is recoverable: a Command Squad could take **two** heavy weapons and consumed no Heavy Support slot, so GW taxed the same gun ~3× to price **the slot, not the gun**. That is a defensible principle — and it is exactly why the system was doomed:

> **Once the same atom has different prices in different contexts, the atom is no longer the unit of costing.** The number attached to "lascannon" was never the value of a lascannon; it was a per-entry fudge factor wearing a wargear label. An atomic system that needs context-dependent prices has stopped being atomic and has kept all the bookkeeping.

**8th edition unified most weapon costs but kept principled exceptions** [FACT — parsed from BSData 8th-ed catalogues]: heavy bolter **8 pts** for Astra Militarum vs **10** for Grey Knights/CSM; multi-melta **15** vs **22**. The reason is sound — Guardsmen are BS4+, Marines BS3+, so the same gun genuinely delivers less. [INFERENCE] **Which proves the deeper point: a weapon's value is a function of its platform, so a global weapon price list is a category error.** Any atomic system must either accept per-platform prices — losing the atomic benefit — or accept mispricing. There is no third option. *(This is the same conclusion Infinity reaches by hand-setting higher SWC on better platforms, §7.2, and that OPR reaches by multiplying weapon cost by Quality, §1.3 — the elegant version.)*

#### GW's actual stated rationale for making wargear free ⭐

[FACT — Robin Cruddace, Warhammer Studio, 10th ed Munitorum Field Manual announcement]:

> *"The points cost of a unit's weapons and wargear are now incorporated into the cost of that unit – **there's no longer any need to count up all the individual weapon loadouts and do a bunch of arithmetic** just to determine the total points cost of one individual unit."*

> *"By comparing the profiles and abilities, you can see for yourself that **certain weapons are clearly better against different targets** – determining the 'best' loadout for any unit depends on what you want it to do and what you think you'll be facing, rather than just paying more for a 'better' gun."*

> *"…specific costs for different weapons typically **added to the complexity of working out your army, for little gain regarding the actual output of the unit on the battlefield**."*

**Read the last line carefully. GW's stated reason was never "it's more balanced" — it was overhead versus yield.** The arithmetic cost was high and the balance return was low. That is a cost/benefit judgement about a mechanic's *running cost*, and it is the argument Settlements should actually interrogate: **not "can we cost gear correctly?" but "is the cost of costing it worth what it buys?"**

**And note the hidden dependency in the second quote.** Free wargear only works if options are **sidegrades** — "clearly better against *different targets*". If they are straight upgrades, the system collapses immediately.

#### The hidden price of free wargear — and this is the finding that matters most

[FACT — Goonhammer, 10th ed Chaos review]:
> *"Their options are all free, but there's a lot less to love about that now that **flails and cleavers and maces are all just boring plague weapons/heavy plague weapons**."*
> *"As with late 9th edition, all the wargear options are free. **Unlike 9th edition, a bunch of the options don't matter any more.**"*

[INFERENCE] **To make N options cost the same, you must make them *worth* the same — so you homogenise the profiles.** Free wargear does not remove the balancing problem; it **relocates it from the points column into the rules text**, and you pay for it in flavour and differentiation. It converts "options nobody takes" into "options that are identical."

> **Whichever way you go, you cannot escape paying for differentiation.** Either you pay in points arithmetic, or you pay in homogenised profiles. That is the real trade, and it should be made deliberately.

The other documented loss [CONSENSUS]: **list-building granularity.** *"it makes writing a 2000 point list very difficult… no dropping a model or a special weapon to get back under the limit."* And: *"We've basically got Power Level now for everything, we're just calling it points."*

The genuine gains were real too, and large [FACT — Goonhammer, with numbers]: *"You no longer have to choose between keeping them cheap to play the mission or giving them special weapons to actually do damage. Now they can do both."* On T'au: *"**It was very easy — especially with 9th's escalating points costs for duplicating weapons on the same model — to price a unit out of its usefulness.**"* **Per-item costing had reached the point where equipping a unit with its own signature weapons made it unplayable.**

#### 11th edition (June 2026) — the synthesis, and the answer Settlements should probably copy ⭐

[FACT — GW]: *"**some weapon upgrades now cost points if they are significantly more powerful or effective than the other available options.**"* Worked example: the macro plasma incinerator on Redemptor Dreadnoughts costs **10 points**, but *"the basic cost of the Dreadnought drops by 10, so it nets out the same"* — it *"helps limit their impact when taken en masse, but doesn't overly punish players."*

> **Wargear is free by default, and priced only where one option provably dominates — with the cost rebased out of the chassis so the default loadout stays points-neutral.** Free wargear becomes the *baseline*; per-item cost becomes a *targeted balance lever* rather than a universal accounting system.

Plus a second new lever [FACT]: **points steppers** — units cost more for your 2nd or 3rd copy, *"designed to discourage always spamming three of whatever is most efficient right now."* Mostly biting at the 3rd unit; at the 2nd for potent or TITANIC units. *(This is the super-linear-in-quantity term that §6.6 argues for, shipped.)*

[CONSENSUS — Goonhammer's verdict, and the caveat is the useful part]:
> *"**How well this works varies.** For big threats centred around a main weapon, it's generally pretty good… **Where it feels more awkward is for some squad weapons like psycannons in Grey Knights, where each gun probably isn't 5pts better than the alternatives.**"*

And their proposed fix is directly applicable: *"rather than 5pts per gun, do 10pts on the unit if you take any psycannons"* — i.e. **cost the decision, not the item.** [INFERENCE] That is a genuinely good idea for Settlements: pricing "this fighter is a specialist shooter" once is cheaper to run, harder to game, and more legible than pricing each characteristic on the weapon.

#### The operational lessons

[FACT] **Never put balance numbers in the printed book.** GW moved points off the datasheet in 2017 specifically so *"points for units could change without invalidating existing books – so if one unit or weapon starts to dominate tournaments… we can address the balance."* **Every subsequent correction in three editions was made possible by that one packaging decision.**

[FACT] **The cadence is the enabling infrastructure.** Quarterly Munitorum Field Manual updates plus alternating Balance Dataslates; 11th ed ran *monthly* for its first three months. [INFERENCE] **The 11th-edition model requires a live data feed and a patch channel. If you cannot patch quarterly, you cannot run it** — which for a single-designer project is a real constraint and argues for getting more of the balance into structure and less into tunable numbers.

[FACT] GW balances on published win-rate data, and the community methodology is rigorous: a **45–55% healthy band** justified by significance testing, plus **TiWP Ratio** (share of tournaments-in-winning-position ÷ share of field; 1.0 = expected). Worked example: Sisters of Battle at 4.7% of the field but 8.1% TiWP share → ratio **1.83**, *"a prime target for a nerf."* And the honest caveat: *"a pure 50% win rate for 30 asymmetrical factions is impossible."*

⚠️ [UNVERIFIED] **No published dataset isolates free wargear's actual effect on balance.** Nobody ran the counterfactual. Every claim in either direction — including GW's — is argument, not measurement.

### 7.15 Oathmark — the one game that solves *entitlement* rather than costing ⭐

*(Joseph A. McCullough, Osprey 2020; 2nd edition August 2026. Sources: the official 8-page Kingdom Building extract and the official Osprey Army Planner PDF, from which 154 exact published point values were extracted.)*

**Every other game in this report answers "what does this cost?" Oathmark answers a different question: "what are you entitled to field at all?"** Its persistent layer is a **kingdom** whose composition determines your legal army list. That is structurally the Settlements meta-layer, and it is the closest published analogue found.

#### The central design decision, in the designer's own words ⭐

[FACT — McCullough, Osprey designer blog, verbatim]:

> *"The kingdom might gain new territory, or it might have its territory occupied, but **when it comes to each game, the players are still playing to the same points value, and theoretically have an equal chance of winning.**"*

> **The kingdom never buys you a bigger army. It only buys you a wider menu.**

Growth is **lateral, not vertical.** A 20-territory kingdom and a 10-territory kingdom both field 2,500 points. The winner's advantage is *optionality* — better matchup answers, access to rarer units — never *mass*. **That single decision is what makes a persistent base layer safe to bolt onto a points-buy game**, and it is the most important finding in this section.

And his stated reason for putting persistence on the territory rather than the army [FACT]:

> *"I quickly realised that I couldn't just have people's armies 'gain experience'… First off, **this would grow completely out of hand really quickly**… Then it hit me — players shouldn't focus on **armies, which are just temporary constructs for a given battle**, but upon **the kingdom which produced them**."*

#### How the kingdom is built — slots and a rarity gate, no currency

[FACT] The Kingdom Sheet is **five concentric circles**: Region 1 holds 1 territory (your capital), Region 2 holds 2, Region 3 holds 3, Region 4 holds 4 — **10 territories at creation** — and **Region 5 is empty, reserved for conquest.** It is explicitly *"not a map"* but *"a visual guide based on how far certain territories are from the seat of power."*

**There is no cost and no currency in kingdom building. There are slots plus a rarity gate that tightens toward the throne:**

| Region | Territories | From your capital's own race list | From any *other* race's list |
|---|---|---|---|
| 1 | 1 | your capital city (rarity 1) | — |
| 2 | 2 | rarity ≤ **2** | rarity ≤ **1** |
| 3 | 3 | rarity ≤ **3** | rarity ≤ **2** |
| 4 | 4 | **anything, no limitations** | **anything, no limitations** |
| 5 | 0 at start | conquest only | conquest only |

[INFERENCE] **Concentric permissiveness.** Your heartland is racially coherent by construction; your frontier is a free-for-all. **It produces thematic armies without a single "you may not take X" rule** — one table of rarity numbers replaces an entire chapter of faction restrictions.

#### How a territory becomes a roster line — two unlock modes

[FACT] Each of the 39 terrain types lists what it unlocks, in one of two grammars:
- **Uncapped** — *"you may purchase as many orc and goblin slaves as you can afford."*
- **Capped, and it stacks** — *"if you have one piece of Rivers terrain in your kingdom, your army may contain up to 6 trolls. If you have two pieces of Rivers terrain… up to 12 trolls."*

**The mechanism is access plus a cap — never a points discount and never a percentage of the army.** The kingdom is a *permission list*; points are spent entirely separately.

#### The second gate — a cap that rewards diversity

[FACT, verbatim]: *"your army may never contain more than four units composed of primarily the same type of figures… **This does not carry across races within an army**, so your force may have four units of human soldiers and four units of elf soldiers without breaking the four unit limit."*

[INFERENCE] **The only legal path to a wider army is diversity.** The kingdom grants the *permission* to diversify; the unit limit supplies the *reason*. That is how you get variety without ever writing "you must take at least one of X."

#### Heroes are capped by buildings, not by a points percentage

[FACT] There is no "no more than 25% on characters" rule. Instead: **one general per army, absolutely.** Each city territory grants 1 King *or* Prince, 1 General *or* 2 Captains, 1 Champion, 1 Spellcaster L1–2. Extra Champions each require a second-tier industrial territory. High-level casters (L3–5) each require a dedicated rarity-3 territory.

[INFERENCE] **Stacking heroes costs you kingdom slots.** A hero cap that spends *territory* rather than *points* is more thematic, harder to abuse, and creates real meta-layer decisions — and for Settlements, whose structure count is already constrained, it is an extremely efficient way to cap characters without a single extra rule.

#### Losses are soft and reversible — the anti-death-spiral rule

[FACT — McCullough, verbatim]:
> *"**You can never fully lose territory**, so you will never be in a situation where you can't use specific units that you have bought and painted (because that would be really annoying), but you can have territory **occupied**, which means those units fight at slightly less efficiency."*

[CONSENSUS] Occupation imposes an activation-roll penalty, reversible by retaking the land. **The loser's roster never collapses, so there is no death spiral** — and note the second, non-mechanical reason, which is about player goodwill toward models they have bought and painted.

#### Is the costing derived? The engine is systematic; the multipliers were not validated

[FACT] No designer statement on costing methodology exists anywhere. But 154 official point values were extracted from Osprey's own Army Planner, and the structure is visible. **The mounted upgrade is an exact fixed ladder, identical across all four races:** Champion +20, Captain +20, General +30, Prince +30, King +40, Spellcaster L1 +20 / L2 +30 / L3 +30 / L4 +40 / L5 +40. **Forty-plus data points, one deviation** (Goblin L5 at +50). Human and Orc characters are priced *identically* across the entire range (Captain 133/133, King 279/279, every spellcaster level equal) — two races sharing a statline sharing a price to the point. **That is a cost engine, not intuition.**

But the race multipliers on line infantry (Human = 1.00) tell a different story [INFERENCE from the published values]:

| | Soldier | Spearman | Archer | Warrior | Linebreaker |
|---|---|---|---|---|---|
| Goblin | 0.83 | 0.85 | 0.83 | — | — |
| Human | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Orc | 1.08 | 1.08 | 1.17 | 1.07 | 1.06 |
| Dwarf | 1.25 | 1.23 | 1.25 | 1.21 | 1.18 |
| **Elf** | **1.67** | **1.69** | **2.00** | **1.86** | **1.76** |

Four races sit in a tight 0.83–1.25 band; **Elves are a clear outlier.** And a Dragon at **700 points is 28% of a standard 2,500-point army in one model.** [CONSENSUS] Both are live community complaints, and McCullough has effectively conceded the monster one — 2E makes monsters less reliable and confines the dragon to the borderlands.

> **The lesson: build the generator, then validate the multipliers against play separately. Oathmark built the generator and skipped the validation** — which is precisely the failure §8.7 and §8.10 are designed to prevent.

**The strongest endorsement of the architecture is a negative finding** [INFERENCE]: **no dominant or broken *kingdom* build has been reported anywhere.** Every balance complaint attaches to unit costs or battlefield rules. The exploit reviewers *do* warn about attaches to the game's alternative **non-kingdom** quick-build method, which one experienced reviewer flags outright: *"WARNING: building armies this way leaves the game open to all kinds of min-maxing tricks that will eventually completely derail the game balance."* **The constraint layer is doing its job even where the costing layer is shaky.** *(Caveat: Oathmark has no tournament scene, so read this as "nothing surfaced in casual play," not "proven balanced.")*

#### ⭐ The 2nd edition retrospective — McCullough grading his own meta-layer after six years

[FACT — Osprey blog, 24 June 2026, verbatim]. This is the most valuable single document found for the Settlements design, because it is the designer listing what he got wrong:

> *"The first edition was very much a **'game of battles' with a campaign system added on. I've reoriented it so that is a 'game about kingdoms' with lots of rules for fighting battles.** So, the game now opens with the rules for building kingdoms… players are encouraged to **start their kingdoms with only 2 or 3 Regions filled. This allows players to start smaller**… it also allows for more room and time for kingdoms to grow organically."*

> *"Monsters… **should be the spice, not the main dish** of the game… most notably **the dragon, can only be included in a kingdom in the borderlands, making it inherently unreliable.**"*

> *"Confession – when I first wrote Oathmark, I was a little bit afraid of magic… I believe this fear drove me to **underpower spellcasters a little bit in the first edition.**"*

**Four lessons available to Settlements for free:**
1. **He started players too big.** Ten territories on day one left nothing to discover. 2E starts at 2–3 regions. **Start your settlement at roughly 30% of its ceiling.**
2. **He under-served the meta-layer's presentation.** The mechanic was fine, but leading the book with battles taught players to ignore the kingdom. **Lead with the settlement.**
3. **He needed a junk tier.** The new 6th region exists so powerful things can be *available but unreliable* rather than *banned or auto-include*. **Location became a balancing axis** — and it is free if you already have rings.
4. **Fear of a subsystem produces a dead subsystem.** He suppressed magic because it worried him, and got spellcasters nobody used.

### 7.17 Last Days: Zombie Apocalypse — the closest thematic match, and the best upkeep design found ⭐

*(Ash Barker, Osprey. Core rulebook + the **Seasons** campaign supplement, both read in full from primary PDFs — 145k and 117k characters of text respectively.)*

**Same genre, same fantasy, same shape: survivors, scavenging, a home base, a persistent roster.** And it makes the *opposite* structural choice to Oathmark, which makes the pair unusually instructive read together.

#### The Refuge is free, and described by exactly three numbers

[FACT] The Refuge costs **zero points**. It sits entirely outside the 100-point creation budget. Every Refuge is fully described by **Max Group Size / Empty Spaces / Built-In Perks**:

| Refuge | Max Group Size | Empty Spaces | Built-In Perks (free) |
|---|---|---|---|
| The Gun Shop | 6 | 3 | Armoury, Fortified Windows, Reinforced Doors |
| The Farm House | 8 | 5 | Fenced-Off Garden *or* Stable, Cold Cellar |
| The Church | 8 | 2 | Solid Structure, Watch Tower |
| The Police Station | 8 | 2 | Escape Vehicle, Radio Room |
| The Prison | 10 | 3 | Fences, Infirmary |
| The Mall | 12 | 8 | Store Room |
| Outdoor Campsite *(Seasons)* | 12 | 10 | **None** — and **Exposed**: every Perk costs **+5 SP** |
| Cabin in the Woods *(Seasons)* | 5 | 3 | Wood-Burning Stove |

[INFERENCE] **That is the entire interface, and it is a genuinely excellent piece of design.** The settlement never competes with the crew for the same budget, so choosing a base is a **shape** decision rather than a **spend** decision, and the trades are immediately readable: the Gun Shop gives you six models and three free Perks; the Campsite gives you twelve models and ten build slots but nothing free and a surcharge on everything.

**Empty Spaces (2–10) is the real constraint — money only decides *when*.** [FACT] Built-in Perks never consume a space and can never be demolished; Empty Spaces are the only slots you can build into, and most Perks may only be built once. Perk prices run **15–30 SP** (Solid Structure 30, Infirmary 25, Wood-Burning Stove 25, Armoury/Bunk Bed/Fences/Fortified Windows/Watch Tower/Escape Vehicle 20, Garden/Radio Room/Reinforced Doors/Store Room/Rain-Collectors 15).

**Same Perk, different price by context** [FACT]: an **Engineer** assigned to Build cuts the cost **25%, rounding up**; an **Exposed** Refuge adds **+5 SP** to every Perk. *(The book never states the order of operations — 35→27 versus 23+5=28. Genuinely unresolved.)*

#### Three payoff channels, and the split is the lesson

[FACT] Every Perk falls into exactly one of three categories:
- **Capacity** — Bunk Bed (+1 Max Group Size); **Stable (20 SP) unlocks 0–2 Horses at 15 SP each, and losing the Stable removes the Horses from the roster.**
- **Economy** — Fenced-Off Garden (D6 SP per post-game, **2D6 with an Agriculturalist**, or 1D3 Medicine with a Naturopath); Rain-Collectors (D3+3 purified water instead of D3+1); Store Room (re-roll a supply die); Cold Cellar (preserves surplus Meals, which otherwise perish); Wood-Burning Stove (**1 Fuel heats 2 rooms instead of 1**).
- **Battle effect** — Armoury, Fortified Windows, Radio Room, Fences, Reinforced Doors, Solid Structure, Watch Tower, Infirmary, Escape Vehicle.

[INFERENCE] **Crucially, only three Perks touch a normal away game** (Armoury, Fortified Windows, Radio Room). Everything else is economy, or fires **only in the one scenario where your base is on the table** (Home Defense). **The designer deliberately kept the settlement out of ordinary battles** — which is the Oathmark instinct, arrived at from a completely different direction.

#### But it does NOT hold points equal, and that is deliberate

[FACT] **There is no per-game points limit after group creation at all.** You spend 100 Scavenge Points once; after that there is no budget check before any battle. You deploy your **entire Group** in almost every Encounter, and new Characters are recruited between games capped only by Max Group Size.

**Veterans are never re-priced** [FACT]: Levels are bought with **Experience**, a completely separate currency from Scavenge Points, and the two never convert. *You cannot buy a stat with SP, and you cannot buy a body with XP.* A 3 SP Crony at Level 10 is still a 3 SP Crony on the roster.

> **Last Days is the opposite pole from Oathmark.** Oathmark holds points equal every game and lets the kingdom widen the menu. Last Days lets the campaign snowball unapologetically and applies the brakes through **attrition and upkeep** instead. Both work. **Read them as the two ends of the design space and pick your position on it consciously.**

#### The best anti-snowball idea in the research: development raises upkeep ⭐

[FACT — Seasons] **Rooms to heat = built-in Perks + the Empty Spaces the Refuge *starts* with. Each room consumes 1 Fuel per Encounter in cold months.** Plus every Character eats 1 Meal and drinks 1 Water per Encounter.

So the Outdoor Campsite (12 models, 10 spaces) burns **10 Fuel every winter Encounter**; the Cabin in the Woods (5 models, 3 spaces) burns 4 — and its free Wood-Burning Stove halves that to an effective 2.

> **A bigger, better-developed base costs more every single turn, forever.** That is a growth curve which self-limits without any points ceiling — and it is the single most transferable idea in this section for a game with a settlement layer.

[INFERENCE] Note the corollary: because the Stove exists, **the tech tree contains upkeep-reducers**, so "invest in efficiency" competes with "invest in capability" for the same Empty Space. That is a genuinely interesting build decision and it costs one Perk entry to create.

#### The automatic post-game base attack

[FACT] Every post-game, roll **2D6**: **−1 per Character Out of Action** at the end of the last Encounter, **+1 per Character assigned to Guard**, +1 for Fortified Windows, +1 if the Refuge is **Remote**, −2 if you gathered Fuel with a Chainsaw. **Result ≤ 2 and you lose the Refuge.**

Losing it: **all Perks lost** (built-in included) and must be rebuilt; **all stashed gear abandoned** *unless* you built the **Escape Vehicle** Perk; **Scavenge Points untouched**; forced move to a *different* Refuge type; anyone who doesn't fit the new Max Group Size is **left for the zombies** with their gear; and one random Character takes an **extra Injury roll** (which can be *Dead!*).

[INFERENCE] Two things worth stealing outright. **First, the coupling** — your battlefield casualties directly threaten your settlement, via a ten-second roll you make every single turn. Most base-building games never connect the two. **Second, the Escape Vehicle pattern** — a Perk whose entire function is *insuring against catastrophe*, competing for the same slot as capability. That is a great decision to put in front of a player.

#### Jobs — the between-game allocation minigame

[FACT] Every able-bodied Character must take exactly **one** Job; Out-of-Action Characters may take none. Core: **Guard** (+1 to the Zombie Attack) · **Work** a Perk (one Character per Perk) · **Build** a Perk · **Recruit** (Leader only) · **The Talk** (opposed Intelligence to convert another Character's Keyword). Seasons adds **Gather Food / Fuel / Water** and **Rest**.

[INFERENCE] **This is the mechanism that ties crew size to settlement throughput** — the model guarding is the model not building, and the model out injured contributes nothing and actively worsens your base-attack roll. Assign all Jobs before rolling any outputs and you get real opportunity cost with almost no rules overhead.

#### Conditions — attrition that isn't battlefield damage

[FACT] Four tracks — **Hunger, Health, Thirst, Warmth** — each with two boxes (Suffering / Critical). **Any two Conditions at Critical and the Character dies.** Critical in any one means they cannot deploy *and* count as a casualty for the Zombie Attack roll. Which Conditions are live depends on the season (Winter forces Hunger + Cold + Sickness; Summer forces Hunger + Sickness + Drought).

And a lovely piece of characterisation-as-mechanic [FACT]: **the Leader's Keyword determines who eats, drinks and stays warm first.** Selfish leaders eat first and freeze last; Selfless leaders eat last and freeze first. Zero extra overhead, and it makes the alignment choice matter every turn rather than once at list-building.

**Leadership Challenges** [FACT] fire when more than half the roster has a checked Condition box *and* a same-or-higher-Level Character of a different Keyword exists. An opposed test either **kills the Leader outright** (Selfish challenger) or **forces them to step down** (Selfless). [INFERENCE] It converts "I mismanaged my settlement" into a narrative event instead of a spreadsheet penalty.

#### Catch-up is XP, never points

[FACT] **Group Level Balancing** gives every surviving member of the *lower-Level* group bonus XP by level gap: **+1** at 0–5, **+D3** at 11–15, **+D6** at 16–20, **+6** at 21+. Plus **the lower-Level group chooses the Encounter.**

[INFERENCE] **The strong player is never nerfed; the weak player just climbs faster.** Same instinct as Frostgrave's ally-creature rule (§7.12) — asymmetric catch-up that preserves the fantasy.

⚠️ **The printed table is missing its 6–10 row** — verified directly against the PDF text layer. A genuine errata gap. Write yours complete.

#### The settlement *is* the win condition

[FACT] The core book's optional ending: the first Group to simultaneously fill **every** Empty Space with Perks, reach **Maximum Group Size**, and bank **300 unspent Scavenge Points** wins outright.

And the Seasons **Campaign Achievement** scoring: **+5** for a fully-built Refuge · **+1 per Character with no checked Condition boxes** · **−1 per Character at Critical** · **+1 per 10 unspent SP** · **+2** for a Leader who honoured their Keyword · and only **+5** for the highest Group Level.

[INFERENCE] **Raw military power is worth 5 points out of a potential 20+.** Settlement completion, husbandry and hoarding dominate the scoring. **If you want players to care about the base, score the base** — Last Days says so louder than any other game here.

#### Costing detail

[FACT] **100 Scavenge Points** at creation, covering Leader + Characters + all gear; leftovers bank. Leaders 12/15/18 SP; Characters 3–21 SP (Crony and Kid 3 · Gang Member and Survivor 6 · Cop/Dog/Goon/Good Samaritan/Rescue Worker/Tough Guy 9 · Builder/Burglar/Farmer/Firefighter/Outdoorsman/Soldier/SWAT 12 · Horse 15 · Survivalist 18 · Sarge 21). Firearms 2–10 SP, CQC weapons 2–3 SP.

**Group composition:** unlimited Characters sharing the Leader's Keyword; **up to 50% Neutral** (75% under a Merciless Thug); **≤25% of a different Keyword**; exactly one Leader ever.

**Rarity is a supply cap, not a price** [FACT] — a Rarity 1 or 2 weapon limits how many models may carry it at recruitment. And the sharpest costing idea in the book: **The Professional (18 SP Leader) converts all `*`-marked weapons' Rarity to `-`**, buying unlimited access to the best military hardware — at the cost of being locked out of every non-`*` item entirely. [INFERENCE] **A Leader whose price buys a change to the *availability rules* rather than to stats.** That is the Malifaux keyword-tax idea and the Horizon Wars CHQ idea in one 18-point package.

**Advancement is deliberately rate-limited** [FACT — the designer says so]: *"as a model increases in power further rolls on the tables cost more and more. This will curb models becoming too powerful, too quickly."* Level costs run 6/12/12/18/18/18/24/24/24/30 XP, **max Level 10**, characteristics capped at **6**. Master Skills require 3 basic skills in a category first, and *"you will only ever learn two Master Skills at the most... and that's only if your Character spends 8 of their possible 10 levels JUST working on those particular areas."*

**Skills that only matter at the settlement** [FACT]: Engineer (−25% build cost), Agriculturalist (2D6 instead of D6), Naturopath (garden produces Medicine), Hunter (+2 foraging), Street Surgeon (converts permanent injuries to Full Recovery). [INFERENCE] **These are what stop a base layer from being a pure tax on combat progression** — they make a non-combat advance genuinely worth an XP roll.

**Design philosophy, stated up front** [FACT] — and note that balance is not among the three named goals: *"Memorable Moments… Crackerjacks… Ever-Afters. Loathed in competitive wargaming, these are the things that separate skirmish games from strategy games."*

### 7.18 The Walking Dead: All Out War — a published custom-build formula, and the best neutral-threat design

*(Mantic. Anthology edition; rules, costing and campaign chapters read in full.)*

**Budget:** points matches at agreed limits (100/150/250/300 recommended); **campaign starts at 125 points**; hard cap of **12 Survivors** regardless of points. Group rule: **no more than half the models may share a Character Type — unless it's the Leader's type, which is unlimited.**

#### It publishes its custom-character costing formula — one of very few games that do

[FACT] Characteristic dice are priced **X / Y / Z** — pay X for your first die in that characteristic, Y each for a second, Z each for a third:

| Die tier | Melee | Shoot | Defense |
|---|---|---|---|
| Best (blue) | 10 / 12 / **16** | 12 / 15 / **20** | 7 / 10 / 12 |
| Mid (white) | 5 / 6 / 7 | 6 / 7 / **8** | 3 / 4 / 5 |
| Worst (red) | 3 / 3 / 5 | 3 / 4 / 6 | 2 / 2 / 3 |

Confirmed by the book's own worked example: *"two white dice and one blue… for the Shoot value that would be a whopping total of 36 points – 8+8+20."* Plus Nerve (Low +0 / Medium +5 / High +15), Health (3 = +0 rising to 8 = +20), Pack Slots (1 = +0 to 4 = +5), up to two Special Rules (2–20 pts) and one Leader Ability (5–10 pts).

**And then the designers admit, in print, that it doesn't quite work** [FACT — verbatim]:

> *"You'll notice that some of the Survivors in the game work out slightly different to the points values here would indicate. **As there's no way of accounting for every possible combination of characteristic and ability, it's hard to truly gauge the effectiveness of a custom character, so these rules include a slight premium.** As a result, it's best to only use custom characters in friendly games in which your opponent agrees to their use."*

[INFERENCE] **This is the most honest statement of the atomic-costing problem found anywhere in the research**, and the mitigation is instructive: they ship the formula, add a deliberate premium to cover the combinations they can't price, and then **quarantine the whole system to friendly play.** Compare Gutschera's rule 8 — value and cost *should* differ, and a good developer knows by how much (§5).

#### TWD re-prices veterans; Last Days does not

[FACT] *"any character that was not removed as a casualty during the game receives an Experience bonus of one red die, **and increases their points value by 3 points**."*

[INFERENCE] Two games in the same genre, released within two years, taking **opposite positions on the exact fork Settlements faces** (§8.11 Fork B). TWD taxes survival directly; Last Days never touches a veteran's cost. Neither is reported as broken.

#### The neutral threat is costed against the *game*, not against either player ⭐

[FACT] *"You will need a number of Walkers chosen to the same points limit as the game, rounding up. **Walkers are 15 points each**, so in a 50-point game you would need 4 Walkers, while in a 300-point game you would need 20."*

[INFERENCE] **This is genuinely elegant. The third-party threat scales linearly with the size of the fight, so a bigger game is not a safer game** — and nobody pays for it out of their own list. Walkers are fully neutral (*"enemy… refers to any model that is not part of your own Survivor group, be it one of your opponent's Survivors or one of the Walkers"*), and **both players get to aim them**: event cards instruct *each* player to move N Walkers in a direction of their choice, alternating.

**The Threat Tracker** is the pressure clock [FACT]: 18 spaces in four bands (All Quiet 1–3 / Low 4–8 / Medium 9–13 / High 14–18). MAYHEM raises it, melee raises it, Panic results raise it, running out of Walker models raises it. When Threat exceeds a Survivor's **Nerve band** that Survivor **Panics** before activating — and *"You may not skip an activation to dodge Panic."* **The game ends at the end of any turn the tracker maxes out**, which means a losing player can deliberately generate MAYHEM to run out the clock and force a draw.

[INFERENCE] Pair this with Last Days' **Noise Tokens** (each shot adds a token; roll D6 + tokens, 7+ summons a zombie at the nearest table edge) and you have a self-regulating third party that **punishes exactly the alpha-strike behaviour that breaks skirmish games** — which is a live concern in the existing `BLKOUT-RULES-ANALYSIS.md` §15.

#### Territory that widens the menu — and territory that costs you safety

[FACT] All Out War has **no base-building layer at all.** Its equivalent is Map Campaign territory control, and **six of the eighteen Special Locations do nothing but remove a purchasing restriction**: Gun Store (one gun over 20 pts, +1 free Ammo Reload), Campsites (may field Custom Survivors), Police Station / National Guard Outpost (specific weapon classes over 20 pts), Factory (special items over 20 pts), Home Territory (recruit at any points value; **upgrade characters to different versions of themselves, paying the difference**). Others give flat discounts (Mini-Mart −1 on Special Items; Farm −4 on rural gear; Prison −2 on riot gear).

**And the counterweight is the sharpest single idea in the book** [FACT]: **Danger Zones raise the starting Threat by +1 for every zone controlled by *either* player.** [INFERENCE] **Territory that costs you safety.** Expansion is not free, the penalty is symmetric, and it makes map greed a real decision rather than an obvious one.

**Catch-up** [FACT]: an **Underdog Bonus** die per full 15 points of difference, pooled, usable one per roll, lost at game end. Plus permanent health attrition, permanent character death, and a Free For All scenario where the **lowest-value player places the central scenery** and deployment is picked **highest-value-first**. Counter-pressure: the loser of a Map Campaign game gets **zero** Faction markers, so territory income does compound. **Net: a snowball with brakes, not a flat curve.**

### 7.16 Cross-cutting conclusions

**1. Formulas do exist — they are just mostly old, paywalled, or disowned.** The complete, verifiable atomic engines found are **BattleTech BV2** (§1.1), **Song of Blades** (§1.2), **One Page Rules** (§1.3), **Rogue Trader 1987**, and the **40k Vehicle Design Rules**. Among *currently-marketed* games, only OPR ships one, and it is behind a paywall and absent from their public downloads. Corvus Belli, Privateer Press, Wyrd, modern GW and Warlord publish nothing. [FACT/NOT FOUND]

**2. Every system that survived contact with big models added super-linear scaling.** Rogue Trader's multiplier bands (1987), WFB's ×5/×13/×20 character tiers, OPR's 8→16 jump and whole-base `Tough(X)` multiplier, Smotherman's Eldar hit-doubling. Four independent designs, decades apart, all concluded that **linear per-stat summation undervalues concentrated power** — and GW said so in print in 1987.

**3. Order of operations is a first-class design lever.** OPR multiplies weapons by Quality but not by Tough. Rogue Trader multiplies the profile, then adds gear flat. Both are deliberate and both are right: **gear should not get better because the thing holding it is tougher.**

**4. Points ≠ balance, and the best systems admit it.** OPR bolts on a wounds-dealt/wounds-taken validator. Jenkins ships a handicap layer and states in errata that his forces aren't fair. Jervis Johnson priced abuse in painting labour. **Every open construction system in this report needed a non-arithmetic governor.**

**5. Context-dependence is the hard ceiling.** Epic's designers say it plainly; VDR priced the same weapon differently by Ballistic Skill; Horizon Wars reprices the whole roster off the CHQ; Rampant prices javelins −1 on cavalry and +1 on foot. **If a component's value depends on its carrier, either gate it structurally or price it per-platform.**

**6. Ship a residuals table.** The WHFB reconstruction is credible *solely* because it publishes 16 computed-vs-published comparisons. The OPR formula is credible because it reproduces 4/4 worked examples. **That is how you tell a working model from a plausible-looking one — and Settlements should publish one for its own cost function.**

**7. Granularity: raise the budget, don't subdivide the atom.** Mersey's 24→30 is the cheapest known fix and it is a published fact. Privateer's 35→75-with-doubled-costs is the same move at larger scale.

**8. Legibility buys forgiveness — and creates expectation.** Rampant has no formula, coarse atoms, and near-zero balance complaints. Horizon Wars has a real construction system and had to publish a disclaimer. **An additive, publicly-visible system creates an expectation of balance; if your maths can't deliver it, the expectation itself becomes the bug.**

<!--RESEARCH-STREAMS-->

---

## 8 · Recommendations for Settlements at 1000 points

Concrete and opinionated, as asked. Every recommendation is traceable to a finding above.

### 8.1 Adopt one atomic unit and name it

**`1 tick = 1 point of modifier on one test = 10 points at the 1000 scale.`**

Justification: `P(success) = (4 + mod)/10`, exactly linear and bounded 10–90% (§4.1). One modifier point is one tenth of the probability space. Nothing else in the game is as clean a numeraire, and Gutschera rule 2 says you must have exactly one.

**Everything must be expressible in ticks.** A body, a weapon characteristic, an armour step, a hacking tool, a settlement structure. If something cannot be converted to ticks, it does not get sold — it gets gated (§8.5).

At the 100-point scale the current table already implies roughly this: Brutal (+1 damage) = 4, Armour Piercing (−1 armour) = 4 — both are +1 on the injury roll and both cost 4. **That is already the atomic derivation. Multiply by 10, make it explicit, and call it the spine.** Note the implied base tick is ~4 at the 100 scale, i.e. ~40 at 1000 — which suggests the natural budget is nearer 1000 points buying ~25 ticks of gear across a crew. Sanity-check that against the sim before locking it; the number that matters is the *ratio* of a tick to a body, not the tick's absolute value.

### 8.2 Make the cost function multiplicative where the engine is multiplicative

```
UnitCost = ( BodyCost + Σ GearTicks + Σ StatTicks ) × ActionMultiplier × ConditionMultipliers
```

- **Additive core** — anything that changes *how well one action lands*: damage, armour, to-hit, range, payloads. These land on different terms of the same product, so within the intended build space they add cleanly (§4.3).
- **Action multiplier** — anything that changes *how often the model acts*: extra attacks, extra Orders, extra reactions, bonus activations. This is the SoBH `(7 − Quality)/2` slot and the BattleTech pilot-skill slot. **Nothing in this category may ever be an additive line item.**
- **Condition multipliers** — the explicit conditional discount ladder (§8.3).

Precedent: BattleTech `(Defense × DefFactor) + (Offense × SpeedFactor)`, then × skill (§1.1); SoBH `(5×Combat + ΣSA) × (7−Q)/2` (§1.2); Hero System's Advantages/Limitations (§3).

**Immediate consequence for the rank ladder.** Ranks currently bundle stat points, skills, *and* Orders into one flat number (5/8/16/24). Orders and T3 skills are action-economy items. **Split the rank price into an additive stat component and a multiplicative command component**, e.g. `RankCost = (stat ticks + skill ticks) × OrderMultiplier`, where a Leader's two Orders multiply and a Recruit's zero Orders is ×1.0. This is the single highest-value structural change available, and it fixes the acknowledged problem that *"the 5/8/16/24 fielding costs are inherited from the old, thinner stat line."*

**Second consequence — steal OPR's shape for weapons.** Price weapons with the *carrier's* to-hit stat as a multiplier:

```
GearCost = Σ(weapon ticks) × HitStatMultiplier
```

A rifle on a DEX+3 Specialist should cost more than the same rifle on a DEX+1 Recruit, because it *is* worth more (§4.3: the value of +1 damage is proportional to the hit side). OPR gets this free; 40k's Vehicle Design Rules did it by printing separate BS4/BS3 columns; Infinity does it by hand-setting a higher SWC on better platforms. **Three independent games reached the same conclusion. Settlements' rank-gating of weapon classes is a crude version of it already — this makes it exact.** It also, for free, fixes the "cheap chassis plus expensive bolt-ons" exploit that Xenos Rampant is criticised for, and does the same job as Horizon Wars' `max_upgrades = P`.

**Third — add the super-linear term at the top.** OPR's stat ladder is 2/4/6/8/**16**; Rogue Trader multiplied any profile over 10 points by 1.5–10×; WHFB multiplied characters ×5/×13/×20. Every system that survived elite models added one. Settlements' rank ladder (5/8/16/24) already accelerates mildly; the sim's own warning that *"the richer stat lines run stronger"* suggests it does not accelerate **enough**. The Leader is the place to test this.

### 8.3 Publish an explicit conditional-discount ladder

Replace the implicit "Accurate is 3 instead of 4" with a stated **divisor**, borrowing Hero System's structure (§6.4):

```
Cost = UnconditionalCost ÷ (1 + L)
```

**And here is the part worth building the whole system around.** If a condition is satisfied a fraction **f** of the time, the trait is worth roughly **f × its unconditional value**. Setting `Unconditional ÷ (1+L) = Unconditional × f` gives:

> **L = (1 − f) / f**

That is not a fudge factor — it is a **directly measurable quantity**, and it lands exactly on Hero System's published quarter-step ladder: [INFERENCE, from the verified Hero formula]

| Condition met | **f** | **L** | Net multiplier | Meaning | Current examples |
|---|---|---|---|---|---|
| always | 1.00 | 0 | ×1.00 | unconditional | Brutal, Armour Piercing, Long Range |
| most activations | 0.80 | ¼ | ×0.80 | lightly conditional | Accurate ("did not Move") |
| two activations in three | 0.67 | ½ | ×0.67 | situational | Spread ("at half range or less") |
| about half | 0.50 | 1 | ×0.50 | narrow | Defensive (defender + didn't move) |
| two in five | 0.40 | 1½ | ×0.40 | rare | first-Charge effects |
| one in three | 0.33 | 2 | ×0.33 | very rare | once-per-game triggers |

Three reasons this beats every published system:
1. **It divides rather than subtracts**, so a discount can never reach zero and it scales correctly onto a 400-point trait and a 20-point one alike.
2. **It lands on Hero System's actual published quarter-step ladder** — so the numbers are not invented, they are a re-derivation of a system that has been in print since 1981.
3. **`f` is something `crew_sim.py` can count.** Instrument each conditional trait with a satisfaction counter, run the existing 3,000-battle pairings, read off `f`, compute `L`. **No published game does this** — every one of them guesses at `f`. It is a genuine edge and it is a day's work.

*(Caveat, per Gutschera rule 14: the player chooses **when** to trigger a conditional, so the true value sits slightly above `f × unconditional`. Expect measured costs to come in a little above the table. Round in that direction.)*

Do the same in reverse for drawbacks — a drawback that bites a fraction `g` of the time refunds `g` of an equivalent trait's cost — and enforce the existing law, **a drawback must bite no matter how you play**, by mechanically checking every drawback's trigger against every bonus's trigger for overlap (§6.2, the Awkward+Accurate bug). **A drawback whose measured `g` is near zero is not a drawback; it is a discount.**

### 8.3b Consider the 11th-edition settlement: free by default, priced at proven outliers

This is the newest and most directly applicable answer in the report, and it arrived from GW reversing itself after a full edition of free wargear (§7.14).

**The model:** gear is **free by default**; a characteristic costs points **only where it provably dominates its alternatives**; and when you do price one, **rebase it out of the base cost so the default loadout stays points-neutral.**

Why it's worth taking seriously for Settlements:
- **It directly addresses GW's stated objection** — the arithmetic overhead of per-item costing was judged not worth its balance yield. Settlements' weapon builder is *more* arithmetic-heavy than 40k ever was.
- **It preserves the thing Settlements actually cares about.** Player-built weapons are a core pillar; free-by-default keeps the expressiveness while removing the requirement that every characteristic be perfectly priced.
- **It admits the sidegrade dependency openly.** GW's own justification — options are *"clearly better against different targets"* — is a testable claim about your own characteristic list. **Any characteristic that is a straight upgrade rather than a sidegrade must be priced or gated.** That is a concrete audit you can run today against `Weapons.md`.

**But note the cost, because it is not free** [FACT — §7.14]: to make N options cost the same, you must make them *worth* the same, and GW paid for that in **homogenised profiles** (Death Guard's flails, cleavers and maces collapsing into one identical weapon). **You cannot escape paying for differentiation — either in points arithmetic or in flavour.** Settlements' whole appeal is the DIY armoury, so the flavour currency is the expensive one here. [INFERENCE] **That argues for keeping Settlements' priced characteristics and importing only two things from 11th edition:** the **points stepper** (a super-linear surcharge on your 2nd/3rd copy of a thing — §6.6, §7.14) and Goonhammer's **"cost the decision, not the item"** — price *"this fighter is a specialist shooter"* once, rather than pricing each characteristic separately. Cheaper to run, harder to game, more legible.

**And the operational lesson, which is free to adopt** [FACT]: GW moved points off the datasheet in 2017 *specifically* so costs could change without invalidating printed books, and **every balance correction across three editions depended on that one packaging decision.** Settlements should publish its costs in a single separate, versioned artefact from day one — never embedded in the rules text.

### 8.4 Keep every hard cap, and reclassify them as costing preconditions

The caps are not balance patches sitting alongside the points system. **They are what makes linear atomic costing valid** (§4.3): they pin builds near the `h ≈ d` diagonal where one flat tick price is correct.

Write them into the costing document as a precondition list:
- Damage caps at **+4**; armour at **−2**.
- Global modifier cap **±3**.
- Weapon range ceiling **24"** (= deployment separation).
- Stat max **+6**; net-modifier ceiling **+5** (the 90% wall) and floor **−3** (the 10% wall).
- **WND fixed at 1.**
- Legal board: **9–12 large features, ~40–45% LOS blocked, 3'×3'.**

Add one new rule that falls straight out of the math: **no purchase may take a model past net +5 on any test in its intended use case.** Past +5 the marginal value of a tick is exactly zero (§4.3), so selling it is selling nothing.

### 8.5 Gate thresholds and action economy — never price them

Codify as a design law, with the reasons attached:

> **Anything whose value is discontinuous, or which grants an extra action, is bought with a rank, not with points.**

- 24" range → Heavy Ranged, Specialist rank, Cumbersome. *(Already done.)*
- Multi-attack → Tier 3, Leader-only, campaign-earned, with load-bearing riders. *(Already done.)*
- Orders → Specialist/Leader only. *(Already done.)*
- Ignore-cover, re-rolls, instant-kill → **do not exist.** *(Already done.)*

**Settlements has independently arrived at the answer every game in this research uses.** The recommendation is to *write down that this is the policy*, so future additions get tested against it rather than re-litigated. Gutschera rule 12 is the citation: a single unconditional non-scalable effect caps the top of your entire cost curve.

This is also the answer to the dual-currency question (§2): **Settlements already has an SWC equivalent, implemented as rank gates.** Do not add a second battle currency. Rank gating needs no bookkeeping, reads off the model, and does the same job. Keep the Goods/points split for own-vs-field, which is a different axis entirely.

### 8.6 Build the costing database with value and cost as separate columns

Gutschera rule 8, verbatim: *"these numbers should **not** necessarily be equal. A game, to be interesting, needs good bargains and bad bargains. But a good game developer should know which are which, and by how much."*

Concretely, one table per priced object with: `derived_value_ticks` (from the formula), `listed_cost_ticks` (what you charge), `delta`, and `justification`. Then use his two diagnostics:
- **cost ≪ value → test it hard.** These are your breakage candidates.
- **value < cost but people play it anyway → your formula is wrong.** These tell you which term you are missing.

This is also the right home for the deliberate 60/40 rock-paper-scissors triangle (rule 4): archetypes should be *intentionally* cyclic, not all pinned at 50%. The existing 11-point spread across eight lists is close to the fragile 50/50 state Gutschera warns about — *"you will surely slip up."* A designed triangle (gunline beats swarm beats melee-elite beats gunline, ~60/40) survives a 10% costing error; a flat field does not.

### 8.7 Derive costs by simulation, and say so

This is the recommendation with the largest gap between what Settlements can do and what the industry does.

There is a real academic literature on exactly this — evolutionary and Bayesian optimisation over cost space, minimising win-rate disparity against a simulator (Volz/Rudolph/Naujoks 2016; GEEvo 2024; RuleSmith 2026). None of it has been applied to a commercial miniatures game as far as this research found. **Settlements already has the simulator.** The loop is:

1. Fix the reference environment by decree (§6.7): board 3'×3', 9–12 features, ~42% blocked, 6 rounds, objective victory, assumed opposing stat line stated explicitly.
2. Build the vanilla curve first (Gutschera rule 5) — rank costs with **no skills and no gear**. Get that right before touching anything else.
3. Layer gear, measure the delta in win rate per tick, and solve for the tick price that flattens it.
4. Instrument conditional traits to measure their satisfaction rate; set the discount band from the measurement.
5. Bracket-tune (rule 15): overshoot deliberately in both directions rather than creeping.
6. Record every assumption in the costing document. **BattleTech's largest published flaw is an unrecorded assumption about to-hit numbers that nobody revisited for eighteen years.**

And keep Gutschera rule 9 pinned above the desk: *"Theorizing is very often wrong, and playing is by far the best way to be sure... a good two hour discussion consists of a hundred minutes of pointless theorizing and twenty minutes of good stuff that saved a week's worth of work."*

### 8.8 The one thing to watch: point-buy degeneration

Gutschera: pure point-buy *"has arguably never been done successfully... in practice tend to degenerate to a single viable character build."* Settlements' own sim already reports the symptom: **"A Fighter has one real build: STR"** (STR+2 at 14/35/63% vs DEX+2 at 5/16/36%).

Three levers, in order of preference:
1. **Colour wheels (Gutschera rule 3)** — forced correlations that make commitment pay. Factions are the obvious home: give each faction one strong rule that makes a *different* stat the best buy. This is also the BLKOUT lesson from the existing analysis (*"one playstyle-defining rule per faction"*), and it is cheap.
2. **Make the board price the stats it already prices** — AGI and INT are worth zero in a pure combat sim by construction. That is a *scenario design* obligation, not a costing one: if no scenario rewards INT, INT is a dead stat regardless of price. Objective and terrain-interaction scenarios are the fix.
3. **Only then reprice.** If STR is 3× the win contribution of DEX at equal cost, the honest atomic answer is that STR ticks cost more than DEX ticks. That is ugly but it is what the data says, and BattleTech does the same thing (Gunnery costs 20% per step, Piloting 10%).

### 8.9 Anti-exploit: make refunds smaller than purchases

Steal BattleTech's asymmetry directly (§1.1). Improving Gunnery 4→3 costs **+20%**; degrading 4→5 refunds only **−10%**, then 5% per further step. Purpose: **you cannot farm points by fielding deliberately bad models.**

Settlements needs this now, because the campaign layer already has a refund channel: *"Each Advance a fighter carries adds +2 points to its cost. Each lasting scar subtracts 2."* Symmetric ±2 is exploitable the moment a scar is worth less than 2 points to the player — and a scar on a model you were going to use as a screen anyway is worth approximately nothing. **Recommendation: Advances cost full price, scars refund half.** Same for weapon drawbacks: a drawback should refund less than an equivalent-magnitude characteristic costs.

### 8.10 Ship a second, orthogonal validator — and a residuals table

**Two things separate a costing system that works from one that merely looks like it does.**

**(a) A validator that is not the price formula.** OPR's is the clearest model [FACT — §1.3]: *"we use a simple system of comparing how many potential wounds a unit can deal vs how many wounds the unit can take,"* and it drives a visible "balanced / not balanced" badge. Every open construction system in this report needed a non-arithmetic governor — OPR's wound ratio, Jenkins' handicap layer, Jervis Johnson's painted-model rule. **For Settlements the natural validator already exists: run the build through `crew_sim.py` against the reference board and check the win rate lands in-band.** Anything a player can build should be checkable, and the check should be *different in kind* from the price.

**(b) A residuals table.** The reconstructed Warhammer Fantasy formula is credible *solely* because it publishes 16 computed-vs-published comparisons. The OPR formula is credible because it reproduces 4/4 of OPR's own worked examples. **Settlements should publish the same thing: derived value vs listed cost vs measured win-rate contribution, for every entry in the armoury.** It is how you tell a working model from a plausible-looking one, and it is the artefact that makes the whole system auditable by playtesters.

### 8.11 For the campaign and settlement layer — steal Trench Crusade's shape

The campaign economy is where costing errors compound, and Trench Crusade (§7.10) has the best published structure for exactly the problem Settlements is about to have:

1. **Publish a fixed threshold schedule** (700/800/900/…/2200 by battle number). Every player's ceiling rises identically and knowably. This is strictly better than letting the curve emerge from performance.
2. **Make the rubber-band opt-in and expensive.** Rebuilding to threshold costs you the Exploration phase, all unassigned gear, and your entire treasury. **The losing player chooses to catch up and pays for it** — far more palatable than an imposed handicap, and it can't be farmed.
3. **Decide the veteran valve on purpose — price OR cap, not half of each.** A genuine fork, and both branches are shipped designs:
   - **Settlements today prices veterans** (*"Each Advance a fighter carries adds +2 points"*), so they crowd out rookies.
   - **Trench Crusade refuses to price them at all.** Warband value is *"the total cost in Ducats of all your models and their weapons, armour and equipment"* — XP, skills and promotion are **not in the formula**. It caps the **count** (max 6 ELITE), the **lifespan** (2 scars then dead), the **rate** (one promotion per battle, on a 6), and puts a `Limited Potential` ceiling (max 3 advancements) on specific models.

   [INFERENCE] Trench Crusade's way makes veterans feel *precious* — the ledger doesn't tax what the player is attached to — and moves the anti-snowball job onto caps, which are harder to game than prices. Settlements' way produces the narrative you've already written (*"the war grinds you down to a handful of hardened survivors who then can't hold enough ground"*), which is the better story. **Both work. The failure mode is a weak version of both — taxing veterans enough to annoy without capping them enough to contain.** Whichever you choose, add a `Limited Potential` equivalent: one keyword, and no single model can become the campaign.
4. **Put `LIMIT: N` next to the price on every catalogue entry — and make it a *purchasing* cap.** Trench Crusade's LIMIT is per-warband, persists across the campaign, exempts allies, and explicitly says *"If you find more via looting/exploration, you can break this limit."* Anything whose value is non-linear in quantity gets a cap rather than a repricing (§6.1, §6.3) — but looting past it is exactly the texture a settlement campaign wants. Run **four** dials as they do: price, `LIMIT: N`, `0-N` roster slots, and value-gated caps (*"0-2 Artillery Witches in a warband worth more than 1000 ducats"*).
4b. **Cap budget and headcount on separate published tracks.** v1.6.3 runs a **Max Field Strength** ladder (10 → 22 models) alongside the ducat Threshold, so a rising budget cannot be converted purely into bodies. One extra column on a table; a direct structural answer to the Lanchester problem in §6.6.
5. **Let faction rules edit the economy, not just the stats.** Minimum model cost, banned keywords, cross-faction unlocks, forbidden units. This is Gutschera's colour wheel (§5, rule 3) and Malifaux's +1 out-of-keyword tax (§7.3) in their most flavourful form — and it is the answer to the point-buy degeneration risk in §8.8.

**Two further campaign findings from the Necromunda/Mordheim lineage (§10) that bear directly on open Settlements decisions:**

6. **Stashed gear should NOT count toward crew rating.** 1995 Necromunda states it outright [FACT]: *"Any weaponry or other equipment that the gang keeps but does not give to a fighter is hoarded… its value is not included in the gang rating."* **This settles the open Armoury question** (`SETTLEMENT-DESIGN-QUESTIONS` — "gear OWNED and points-costed to field, or ownership replaces the points cost?"). The precedent is clean and it is what makes underdog banding mathematically sane: **ownership is wealth; rating is fielded power.** It also aligns exactly with the already-locked principle that *"Goods/Materials buy what you own, points gate what you field."*
   *(Note the deliberate contrast: Mordheim hand-tunes Hired Sword ratings with no consistent ratio to hire fee — Ogre 80gc→+25, Pit Fighter 30gc→+22, Halfling 15gc→+5 — while Necromunda uses a flat hire-fee × 5. Two shipped games, two opposite philosophies. Pick one on purpose.)*

7. **Play frequency is a bigger snowball source than skill, and Settlements is unusually exposed to it.** Goonhammer's 100,000-run Necromunda simulation [FACT]: *"The median credits earned after a full campaign was 750 credits assuming one game per week and with two it's at 1170."* **Whoever plays more wins the meta, with no skill or luck involved.** Settlements has deliberately chosen to persist *outside* campaigns — rosters and settlements grow game-to-game whether or not anyone is running one — which is precisely the structure that measures. **Any per-battle income tap creates this.** Shipped mitigations worth copying: Blood Bowl's *Expensive Mistakes* tax on hoarded gold plus free money for the loser; Mordheim's diminishing-returns wyrdstone "wash table"; Necromunda Outlanders' income wash table that softly enforced a gang-size band. **A wash table — diminishing returns on income above a threshold — is the cheapest of the three and fits the Materials economy directly.**

### 8.12 The settlement layer — steal Oathmark's architecture wholesale

The costing research answers "what does a thing cost?" **Oathmark (§7.15) answers the question Settlements actually has open: what does the settlement *entitle* you to field?** These are different problems and the settlement needs the second one solved.

**1. Territory grants permission, never points. Steal this first and everything else becomes tuning.**
The settlement should widen the **menu**, never the **budget**. Both players field the same points every battle regardless of settlement size. McCullough states it outright: *"the players are still playing to the same points value, and theoretically have an equal chance of winning."* This is the mechanism that makes a persistent base layer safe on top of a points-buy game — and it is fully consistent with the principle already locked in this project: **"Goods/Materials buy what you own, points gate what you field."** Oathmark is the proof that principle scales to a full campaign.

**2. Rings with a rarity gate, not a flat unlock list.** Core = restricted and coherent; periphery = permissive and strange. One table of rarity numbers replaces an entire chapter of faction restrictions, and it generates thematic crews without a single prohibition. Map it directly: inner ring = settlement core, outer rings = expansion, outermost = scavenged frontier.

**3. Two unlock grammars, and only two.** *"As many as you can afford"* versus *"6 Trolls per River, and 2 Rivers means 12."* Cheap, expressive, and it lets one structure be either a staple-enabler or a rare-unit valve. This is the grammar the Structures catalogue should use.

**4. Cap heroes with buildings, not with a points percentage.** One Leader ever; each additional Specialist costs a structure slot; the highest-tier capability needs a dedicated building. A cap that spends *territory* is more thematic, harder to abuse, and creates genuine settlement decisions. Given the 9–12 density constraint already in force, this is the most efficient character cap available.

**5. Make losses soft and reversible.** Occupied ≠ destroyed. Structures taken or damaged impose a penalty on what they unlock and come back when retaken. The designer's stated reason is worth keeping in mind: *"you will never be in a situation where you can't use specific units that you have bought and painted (because that would be really annoying)."* This is simultaneously the anti-death-spiral rule and a player-goodwill rule.

**6. An "unreliable frontier" tier for problem entries.** 2E solves the dragon without nerfing the dragon: it is available, but only from the ring whose troops are flaky. **Location as a balancing axis** — free, if you already have rings, and it is the right home for anything too strong to price and too fun to cut.

**7. Start the settlement small — his single biggest 2E regret.** He gave players 10 territories on day one and spent six years learning that left nothing to grow into. Start at ~30% of the ceiling.

**8. Lead with the settlement, not the battle.** His second-biggest regret: *"The first edition was very much a 'game of battles' with a campaign system added on. I've reoriented it so that is a 'game about kingdoms.'"* Presentation taught players which layer mattered — and it taught them wrong.

**9. Build in a negative-feedback event hook from day one.** Oathmark's only genuine subtractive mechanism (Kingdom Events — plagues and blights that cut access to specific territories) arrived two supplements late. It is the natural home for the wash-table / income-throttle recommendation in §8.11.

**10. If you ever want unit progression, use the quarantine pattern.** McCullough kept unit XP out of the core because it *"would grow completely out of hand really quickly,"* then reintroduced it under tight constraint: **max 3 honours per unit, costs extra points, and only one honoured unit may be fielded per battle.** That is the proven-safe shape.

**And one thing not to copy: Oathmark's actual numbers.** The cost *engine* is demonstrably systematic — a mounted-upgrade ladder identical across four races and ten roles, 40+ data points with one exception — but its race multipliers were never validated against play (Elves at 1.67–2.00× while everyone else sits in a 0.83–1.25 band; a Dragon eating 28% of a standard army). **Build the generator, then validate the multipliers separately.** That is exactly the step Oathmark skipped, and §8.7 and §8.10 exist to stop Settlements repeating it.

### 8.13 What *not* to do

- **Do not add a second battle currency.** Rank gates already do the SWC job (§8.5).
- **Do not price thresholds.** Nobody has ever succeeded (§6.1).
- **Do not chase a flat 50% across all archetypes.** Build the 60/40 triangle instead (§8.6).
- **Do not rescale to 1000 and keep pricing in round tens.** The granularity exists to let multipliers and conditional discounts land on integers (§1.3). If every price ends in 0, the rescale bought nothing.
- **Do not derive stat costs in a vacuum.** The project already proved you cannot (`Dice Mechanic — Sim Findings`), and Gutschera's rule 10 says the same thing in general. Fix the environment first.
- **Do not round until the end.** BattleTech carries full precision and rounds once (§1.3).

---

## 9 · Sources

★ = read in full and load-bearing for this report.

### Design theory — the canonical texts
- ★ **K. Robert Gutschera (Director of Development, Wizards of the Coast), "Magic Lessons: Designing and Balancing Game Objects," GDC 2007** — https://media.gdcvault.com/gdc07/slides/S3709i2.pdf — *the single most important source here. Verified in full; all 15 rules and every quote in §5 checked against the document.*
- Dylan Mayo, "Board Game Design Day: Balancing Mechanics for Your Card Game's Unique 'Power Curve'," GDC 2018 — https://gdcvault.com/play/1024913/Board-Game-Design-Day-Balancing — *session description verified; video not accessed. Introduces "proportional distance off the curve."*
- ★ Jake Thornton (Mantic designer), "Design Theory: Why Points Systems Will Always Be Broken" — https://quirkworthy.com/2011/10/15/design-theory-why-points-systems-will-always-be-broken/ — *three named failure modes (multiples, synergy, opposing forces) plus the terrain problem; and the methodological rule "change the calculator, not the individual cost."*
- Jake Thornton, "Deadzone Points Values" — https://quirkworthy.com/2014/04/20/deadzone-points-values/ — *fetched; contains no formula. He declines to publish the method. Recorded as a negative result.*
- Jake Thornton, design theory index — https://quirkworthy.com/design-theory/
- Delta Vector, "Game Design #61: Lethality and Modifiers" (2015) — http://deltavector.blogspot.com/2015/12/game-design-61-lethality-and-modifiers.html — *dice-curve dependence of modifier value; cover halving lethality in LOTR and Infinity.*
- Board Game Designers Forum, "Wargame points formula. Determining weights." — https://www.bgdf.com/forum/game-creation/design-theory/wargame-points-formula-determining-weights — *the "same ability, two prices by carrier" problem.*
- John's Wargame Page, "DBA Points System" — https://johnswargames.wordpress.com/2011/01/15/dba-points-system/ — *snippet level only.*
- Mark Rosewater, "Nuts & Bolts #15: Structural Support" — https://magic.wizards.com/en/news/making-magic/nuts-and-bolts-15-structural-support

### BattleTech Battle Value
- ★ **MegaMek open-source implementation** (authoritative, machine-checkable) — `megamek/src/megamek/common/battleValue/BVCalculator.java`, `MekBVCalculator.java`, `HeatTrackingBVCalculator.java` in https://github.com/MegaMek/megamek — *source of the verified skill-multiplier table, `tmmFactor = 1 + maxTMM/10`, `speedFactor = round(pow(1+(mp−5)/10, 1.2), 2)`, `heatEfficiency = 6 + heatCapacity`, the sort-and-halve heat rule, and the ammo cap.*
- Official TechManual Battle Value v4.1 (2021 revision) — https://battletech.com/wp-content/uploads/2025/06/100_TechManual-Battle-Value-v4.1.pdf — *returned HTTP 500 at time of research; listed for completeness.*
- Sarna BattleTechWiki, "Battle Value" — https://www.sarna.net/wiki/Battle_Value — *BV history: Combat Efficiency Factors → Combat Value (1992) → BV1 (Maximum Tech, 1997) → BV2 (TechManual, 2007) → 2021 revision → "BV 2.1" MUL tweaks. Atlas AS7-D = 1,897 BV2 vs 52 Alpha Strike Point Value.*
- Sarna, User:Mbear/BVWorksheet — https://www.sarna.net/wiki/User:Mbear/BVWorksheet — *step-by-step worksheet: armour ×2.5, structure ×1.5, gyro ×0.5 tonnage, engine/structure type multipliers, AMS = 32.*
- ★ Scott Boehmer, "Battle Value is Flawed" (2025) — https://scottsgameroom.com/2025/05/07/battle-value-is-flawed/ — *eight named failure modes with numbers; the Medium Pulse Laser 48→66 BV baseline error; +4 TMM hit rate 41.66% vs 72.22% at +2; Rache vs Elemental 372 vs 404 BV ammo bug.*
- Scott Boehmer, "What Is Battle Value?" — https://scottsgameroom.com/2025/04/23/what-is-battle-value/ — *`Defense = 2.5×Armor + 1.5×Structure + 0.5×Tonnage`; `DefensiveFactor = 1 + maxTMM/10`; `SpeedFactor = (1 + (Mobility−5)/10)^1.2`; heat rule; ammo ≈ ⅛ weapon BV per ton.*
- jgf1123, "Updated weapon Battle Value" — https://medium.com/@jgf1123/updated-weapon-battle-value-5ed38ee168c9 — *the 60+ damage headshot-bonus threshold bug; energy ×1.5 / other ×1.2 multipliers; proposed graduated replacement.*
- Official BattleTech forum, "Piloting & Gunnery BV Modifier Official Update" — https://battletech.com/forums/index.php?topic=67626.0 — *Xotl on the 2021 skill-cost change: Piloting 15%→10% (10%→6% above skill 2); Gunnery unchanged at "20%, 15% for the leap to Gunnery 0."*
- Ian, "The Absurdity of Battle Value" — http://giantbattlingrobots.blogspot.com/2009/05/absurdity-of-battle-value.html — *no stated threshold at which a BV gap predicts an outcome; the Black Hawk Prime overgunning exploit.*
- https://www.tabletopbattles.com/battletech-bv-and-the-code/

### Song of Blades and Heroes
- ★ **Official point-cost chart (PDF)** — https://s40683529a796d3ff.jimcontent.com/download/version/1586689165/module/11357602021/name/SOBH_costs_chart.pdf — *the full Quality × Combat × SpecialAbility table and the complete Special Ability price list. The formula in §1.2 was derived from this chart and validated 34/34 against transcribed cells and all three of the publisher's own worked examples.*
- Core rules (4th ed. v4.3) — https://files.spawningpool.net/docs/Vault2.0.-.TTRPG-Gamebooks/Collections/Kid%20Friendly/6.%20Beginning%20Miniatures%20&%20War%20Games/Song%20of%20Blades%20&%20Heroes%20-%20Core%20Rules%20(4th%20edition,%20v4.3).pdf
- BGG, "Point Cost System" thread 786025 — https://boardgamegeek.com/thread/786025/point-cost-system — *403 to automated fetch; not read.*

### BLKOUT
- ★ https://www.blkoutgame.com/pages/the-game — *"Forget the tedious task of point-counting..." — the key quote.*
- https://www.blkoutgame.com/blogs/news/getting-started-in-blkout
- https://www.blkoutgame.com/blogs/news/blkout-matched-play-updates
- https://www.blkoutgame.com/blogs/news/q2-matched-play-updates
- https://www.blkoutgame.com/blogs/news/blklist-tactics
- https://www.blkoutgame.com/pages/how-to-play · https://www.blkoutgame.com/pages/blkout-rules
- https://blkout.wiki.gg/wiki/BLKOUT_Wiki — *lore-only, no unit stats.*
- https://www.ontabletop.com/forums/topic/blkout-near-future-sci-fi-by-enemy-spotted-studios/
- https://gamefound.com/en/projects/enemy-spotted-studios/blackout — *no usable costing content.*

### One Page Rules
- ★ **AoF: Point Calculator v1.10** (official, 18pp, *Game Design: Gaetano Ferrara*) — `https://web.archive.org/web/2020id_/https://i.4pcdn.org/tg/1581848035316.pdf` — *read in full; the complete formula. Direct link 403s.*
- https://onepagerules.com/2019/08/01/new-point-calculator-quickplay-armies/ (via Wayback) — *"the system that we use to figure out the point costs… corner stone for our game engine"*; Patreon Tier 3 gate
- https://onepagerules.com/2020/02/27/point-calculators-ai-rules-updates/ (via Wayback) — Army Checklist, spell-list creation
- ★ https://www.onepagerules.com/news/patch-notes---janaury-26th-2024 — **the wounds-dealt vs wounds-taken validator and the balanced/not-balanced badges**
- https://www.onepagerules.com/news/3rd-edition-rules-updates-part-1 — admitted offensive/defensive cost-ratio retune
- https://www.onepagerules.com/resources — *Point Calculator absent from current public downloads*
- https://github.com/kdj0c/onepagepoints — community reverse-engineering (MIT, source read directly; a different continuous model)
- https://github.com/opr-official — *only `army-forge-issues`; no source code*
- https://github.com/vonreg/SW-Firefight — active 2026 fan implementation of the same architecture
- https://www.dakkadakka.com/dakkaforum/posts/list/798640.page — community balance consensus
- https://forum.onepagerules.com/thread/2789/forge-studio-points-published-calculator — **title + search-index snippet only; forum is JS-only and not archived. The "Army Forge has diverged from the published calculator" claim rests on this and is UNVERIFIED.**

### Gaslands
- https://www.ospreypublishing.com/media/ynedioak/gaslands-refuelled-quick-reference-sheet-v3.pdf — official cost/slot tables
- https://planetsmashergames.com/wp-content/uploads/2021/04/Gaslands-FAQ.pdf — the Prison Car errata that reveals the 1 Hull ≈ 2 cans rate
- https://planetsmashergames.com/news/gaslands-third-edition-beta-now-live/ · https://planetsmashergames.com/rule-of-carnage/
- https://www.tabletopgaming.co.uk/features/start-your-engines-an-inteview-with-gaslands-refuelled-designer-mike/
- *Unresolved lead:* **The Fundamentals of Tabletop Miniatures Game Design** (Ford & Hutchinson, CRC Press 2024) — https://www.routledge.com/The-Fundamentals-of-Tabletop-Miniatures-Game-Design.../p/book/9781032324012 (403). **Most likely place a costing rationale exists; could not confirm or rule out.**

### Rampant line
- https://www.ospreypublishing.com/us/osprey-blog/2022/lion-rampant-second-edition-getting-started/
- ★ https://www.ospreypublishing.com/ca/osprey-blog/2025/what-changed-in-dragon-rampant-second-edition/ — **the 24→30 budget increase and its stated reason**
- https://drive.google.com/file/d/1KmeL2bhHCA2btZYJQ4csuucEr_Zkopi6/view — LR2e Unit Matrix v5 (best single cost artefact)
- https://doctorphalanx.blogspot.com/2022/12/xenos-rampant-unit-profiles-for-near.html — 21 reconciled unit builds
- https://www.agentlemanlysport.com/review_xenos_rampant/ — the "deceptively low base cost" critique

### Horizon Wars
- ★ https://www.precinctomega.co.uk/_files/ugd/9346a6_2adedc5e5b274ab3bcc48d3c78fe5205.pdf — **official Errata & FAQ: "not necessarily balanced or fair… This is intentional"; `max_upgrades = P`**
- https://precinctomega.podbean.com/e/precinct-omega-podcast-design-8-points-systems-army-building-and-balance/ — **78 minutes by a working designer on points-system theory. No public transcript (Patreon ~£1). The single highest-value unexploited source found.**
- https://www.precinctomega.co.uk/_files/ugd/9346a6_7fb2ab4f0b1c4b68974db746daf00bbc.pdf — Zero Dark FAQ (points abandoned for a mission clock)

### Games Workshop — the published formulas
- ★ https://archive.org/stream/warhammer-40-k-rogue-trader-rulebook/Warhammer%2040K%20Rogue%20Trader%20-%20Rulebook_djvu.txt — **Rogue Trader 1987 points formula verbatim, including the "undervalue the larger creatures" admission**
- ★ https://www.oocities.org/warhammerkingdom/40kvehicles.pdf — **full Vehicle Design Rules, Jervis Johnson, Dec 2000; BS-dependent weapon pricing; the painted-model governor**
- http://yenlowang.free.fr/BFG/smotherman_formula_v205.pdf — Smotherman Formula v2.05 (BFG Magazine #2, never made official)
- `https://web.archive.org/web/20120115224353id_/http://wargametactics.com/wargame-extras/tactics-articles/how-to-compute-points-values-in-whfb.php` — WHFB reconstruction **with its 16-row residuals table**
- ★ https://www.tacticalwargames.net/taccmd/viewtopic.php?f=4&t=17977 — **Epic: "more of an art than a science"; cost is not separable from the formation**
- https://www.goonhammer.com/necromunday-campaign-progression-part-1-advancements/ · https://yaktribe.games/community/threads/lets-discuss-balance-points-costs.8945/
- https://www.belloflostsouls.net/2017/11/chapter-approved-dont-fear-the-vehicle-design-rules.html
- http://realmofzhu.blogspot.com/2011/11/oldhammer-universal-points-system.html — **UNVERIFIED** per-characteristic modifier numbers
- https://es.scribd.com/document/432046937/Points-Values-in-40k-2nd-Edition — **UNVERIFIED**, abstract only

### Oathmark (§7.15) — the settlement/entitlement analogue
- ★ **Official Osprey 8-page Kingdom Building extract** — https://drive.google.com/file/d/1uJDv2jh-Sm88ymjh8FsucFVDyFJWXjW4/view — *the actual rules text: regions, rarity gates, all five Terrain Lists, the Unit Limit. Downloaded and read in full.*
- ★ **Official Osprey Army Planner PDF** — https://drive.google.com/open?id=1fh-Owpzn7iqp3O-70hSoFkNZh2u__2Gx — *AcroForm dropdowns extracted: **154 exact published unit point values**. Osprey's own data, not a fan reconstruction.*
- ★ https://www.ospreypublishing.com/uk/osprey-blog/2020/designer-blog-creating-your-kingdom-in-oathmark-battles-of-the-lost-age/ — **McCullough on why persistence lives on the territory, and the "same points value every game" rule**
- ★ https://www.ospreypublishing.com/us/osprey-blog/2026/oathmark-second-edition-whats-changed/ — **the 2E retrospective: start smaller, lead with kingdoms, the unreliable-borderlands tier, the magic confession**
- https://www.ospreypublishing.com/ca/osprey-blog/2020/oathmark-battles-of-the-lost-age-army-planner/ — unit size limits
- https://www.ospreypublishing.com/ca/osprey-blog/2020/designer-blog-legendary-units-in-oathmark-battlesworn/ — Battle Honours and the quarantine pattern
- https://www.josephamccullough.com/oathmark-battles-of-the-lost-age/ · http://therenaissancetroll.blogspot.com/2017/10/oathmark.html
- Reviews: https://pijlieblog.blogspot.com/2020/06/oathmark-review.html *(best balance analysis; the min-maxing warning about the non-kingdom build method)* · https://mustcontainminis.com/2021/06/first-look-at-oathmark-bane-of-kings/ *(Kingdom Events)* · http://bloodbeard.blogspot.com/2020/04/review-oathmark-battles-of-lost-age.html · https://stourbridgewargames.wordpress.com/2021/10/05/oathmark-campaign-underway/ · https://fistfulsofdice.blogspot.com/2025/06/rebuilding-oathmark.html *(the Elf overcosting claim)* · https://www.dakkadakka.com/dakkaforum/posts/list/789022.page *(7/10 review, via curl)*
- ⚠️ **BGG inaccessible** (403 web, 401 XML API) — no ratings or weight figures obtained. **Reddit blocked** — the r/Oathmark monster-costing complaint is snippet-only.
- *Unauthorised scans of the full rulebook were available and were deliberately not mined; the campaign-chapter specifics are correspondingly the weakest part of §7.15 and are tagged.*

### Frostgrave / Stargrave / Rangers of Shadow Deep (primary sources, read directly from the user's Drive)
- `Frostgrave 2.0.pdf` — 400gc budget, full Standard and Specialist soldier tables, Base Resource table (incl. **Carrier Pigeons 50gc: all soldiers cost 10gc less**), Experience table, Treasure table, buy/sell spreads, **Level Difference Encounter Level table**
- `Osprey - Wargame - 01 - Stargrave.pdf` — 400cr budget, both soldier tables, captain/first-mate profiles, the **level-number-dictated improvement rotation**, loot tables. ⚠️ *Extract truncates at p.79; the "Spending Loot" chapter is missing.*
- `1. Rangers of Shadow Deep - Standard Edition Updated (2021).pdf` — the 10-Build-Point ranger, companion Recruitment Point list, player-count RP scaling, level cost table, the 4-step level rotation
- `ROSD Archetypes.pdf` — **the archetype pattern: budgets and sub-caps adjusted, catalogue never repriced**

### Trench Crusade (primary sources, read directly from the user's Drive)
- `Trench Crusade Rules v1.6.3.pdf` and `Trench Crusade Campaign Rules v1.6.3.pdf` (in `App Campaign Builder/Rules/`) — the authoritative current text; full New Antioch and Heretic Legion troop and equipment lists, LIMIT definitions, Threshold and Max Field Strength ladders, faction economic variants
- `BS Data TC/New Antioch.cat` + `Trench Crusade.gst` — BattleScribe XML, decoded and parsed: 64 generic weapon profiles, 87 costed entries; confirms `max=N:selections/roster` (LIMIT) vs `max=1:selections/parent` (per-model)
- `THE_IRON_SULTANATE_GLORY_ITEMS.pdf` · `BLACK_GRAIL_GLORY_ITEMS.pdf` — read in full; Glory price lists
- `Trench_Crusade_Campaign_Rules-4.pdf` — 700-ducat start, the Threshold Value schedule, Reinforcements, Resupply, 6-ELITE cap, injury/scar chart, promotion dice, "You can NOT dismiss any warrior"
- `MAMMON_WARBAND-2.pdf` (Knights of Avarice) — ducat-priced equipment with `LIMIT: N` tags; the 80-ducat minimum-model-cost faction rule; banned keywords; cross-faction unlocks
- `New Antioch Playtest rules V1.pdf` — Heavy Shotgun 20 ducats, `LIMIT: 2`
- `V1.4._Key_Changes-2.pdf` — the errata that prove price and `LIMIT` are tuned as **separate dials**; Glory-Point-priced items (*"Musical Instrument: 1 Glory Point"*); `0-N` roster caps

### BLKOUT (primary source, read directly from the user's Drive)
- ★ `Unit-Cards-Printable-2026.pdf` — **every unit card read. They carry Movement / Skill / Armor(X/Y) / model count and NO cost of any kind. This definitively confirms BLKOUT has no points system.**

### RPG point-buy systems
- ★ https://dn760002.eu.archive.org/0/items/pdf-gurps-lite-fourth-edition/pdf-gurps-lite-fourth-edition_compress_djvu.txt — GURPS Lite 4e full OCR (attribute and skill cost tables)
- https://anyflip.com/odiqo/zlcc/basic/1-50 (GURPS Basic Set: Characters scan) · https://anyflip.com/jezrn/avtc/basic/1-50 (GURPS Powers — the Multiplicative Modifiers admission). ⚠️ *AnyFlip OCR proved unreliable (returned "Luck: 5 points" against a verified 15); single-source AnyFlip numbers were discarded.*
- https://www.mygurps.com/index.php?n=Main.GURPSHouseRules — the published "just DX = 15 / just ST = 8" decomposition
- https://gamingballistic.com/2013/02/28/stats-and-pricing-in-gurps/ — Douglas Cole on DX/IQ underpricing
- https://groups.google.com/g/rec.games.frp.misc/c/OFXv1iA1xlM — "GURPS Is Broken" (1994), proposing the fix 4e shipped a decade later
- https://en.wikipedia.org/wiki/Hero_System — verified `Active = Base × (1 + Advantages)`, `Real = Active ÷ (1 + Limitations)`, ±¼ steps
- https://anyflip.com/qjyoi/oytn/basic — Hero 6e Basic Rulebook (characteristic costs, worked examples)
- ★ http://gamedesignfanatic.blogspot.com/2010/09/analyzing-hero-system-6th-edition-major.html — **the "these characteristics had a negative cost" quote**
- https://philgamer.wordpress.com/2009/06/11/hero-system-6th-edition-ch-ch-ch-ch-changes-with-apologies-to-david-bowie/ — the "Uberstat effect" quote
- https://www.enworld.org/threads/the-hero-system.85146/ — the Champions STR critique
- ★ https://www.d20herosrd.com/character-creation/ — M&M 3e PL caps verbatim · /6-powers/modifiers/ (cost formula + floors) · /6-powers/effects/ (base cost table) · .../summon-control/ · .../variable-general/ · .../enhanced-trait-general/
- ★ https://freeronin.com/2e_files/MM2eCh1.pdf — **the published PL rationale ("forces player characters to diversify… can make the heroes start looking the same")**
- https://freeronin.com/2e_files/MM2eFAQ.pdf — "hard limits"; non-combat powers "limited solely by how many points the character has"
- ★ https://freeronin.com/3e_files/MM2E3EConv.pdf — **Kenson's own mispricing post-mortem**
- https://freeronin.com/files/MNM3Epreview.pdf — POWER EFFECTS cost table
- ⚠️ **No first-hand Sean "Kromm" Punch quote was obtained** — sjgames.com 403s on every path, gurpswiki is in a redirect loop, Reddit blocked. **Nothing in this report is attributed to him.** Likewise no first-hand Steve Long / Aaron Allston commentary (herogames.com 403).

### Additional design theory
- ★ https://gamebalanceconcepts.wordpress.com/2010/07/21/level-3-transitive-mechanics-and-cost-curves/ — Ian Schreiber. *"[linear] is pretty rare"*; increasing curves *"you see this a lot in RPGs"*; names the bundle problem and the conditional problem and **offers no formula for either** (re-checked deliberately).
- https://gamebalanceconcepts.wordpress.com/2010/07/14/level-2-numeric-relationships/ — the cost-curve taxonomy incl. triangular
- ★ https://www.gdcvault.com/play/1025294/Understanding-Your-Enemy-A-Mathematical — **Leif Walter, Creative Assembly, GDC 2018: unit value as a Taylor expansion "linearized around a baseline value within the situational space." The formal statement that a points value is a first-order local approximation.**
- ★ https://www.leagueoflegends.com/en-us/news/dev/dev-champion-balance-framework/ — Riot: a champion is balanced *"if they can be considered balanced for **any**"* of four audience bands. **The target is an interval, not a scalar.**
- ★ https://www.sirlin.net/articles/balancing-multiplayer-games-part-1-definitions — Sirlin's option-count definition of balance
- https://www.gdcvault.com/play/1023564/Math-for-Game-Programmers-Balancing — Schreiber, GDC 2016
- ★ https://ojs.aaai.org/index.php/AIIDE/article/view/12513 — **Jaffe et al., "Evaluating Competitive Game Balance with Restricted Play," AIIDE 2012. Price a component by the win-rate delta between agents allowed and forbidden to buy it. Directly implementable against `crew_sim.py`.**
- https://digital.lib.washington.edu/researchworks/handle/1773/22797 — Jaffe dissertation
- https://arxiv.org/abs/1907.01623 — Evolving the Hearthstone Meta (IEEE CoG 2019); multi-objective re-costing that **minimises disruption** — the formal version of "errata as few things as possible"
- https://paradigmplus.itiud.org/volume1/number1/becker/ — Becker & Görlich: *"no two authors share identical understandings of game balancing"*; introduces **"shadow costs"**
- https://magic.wizards.com/en/news/making-magic/mana-action-2011-05-30 — Rosewater: cost exists *"to make different cards important at different parts of the game"* — pacing, not equalisation
- https://deltavector.blogspot.com/2014/01/game-design-11-balanced-points-system.html — the best community articulation of the isolation problem
- ⚠️ **Yannakakis & Togelius, *Artificial Intelligence and Games*** — TOC checked; **there is no game-balance chapter.** Do not cite one.
- ⚠️ The quote *"you can't cost a card correctly if it's conditional"* **could not be verified as Rosewater's.** The substance exists in community writing; the attribution does not.

### Research completeness — what did not finish
Two research streams were terminated early by an API session limit and their material is **not** in this report:
1. **Warhammer 40,000 wargear costing across editions** (3rd–5th per-item pricing, 8th's points/power-level dual system, 9th's free wargear, 10th's fixed costs and quarterly dataslate) — partially covered from other streams in §7.9, but GW's stated rationale for the 10th-edition move to all-free wargear was not captured.
2. **Frostgrave / Stargrave / Rangers of Shadow Deep** — the McCullough fixed-price soldier lists and RoSD's Ranger point-buy and solo difficulty-scaling. Primary-source PDFs are in the user's Drive and identified by file ID; **this is the highest-value re-run**, and RoSD in particular is the closest structural cousin to a Settlements crew.

A third stream on **Trench Crusade** was launched against the Drive sources; §7.10 reflects what was read directly rather than that stream's output.

### Lanchester's Laws and model count
- ★ Ernest Adams, "The Designer's Notebook: Kicking Butt by the Numbers: Lanchester's Laws," Game Developer — https://www.gamedeveloper.com/design/the-designer-s-notebook-kicking-butt-by-the-numbers-lanchester-s-laws — *"twice as large, but four times as strong, and costing only twice as much."*
- ★ Flanagan, Lambert, Lipscombe, Northey & Robinson, "Lanchester's Fighting Strength as a Battle Outcome Predictor Applied to a Simple Fire and Manoeuvre Wargame," *Recent Advances in Monte Carlo Methods*, IntechOpen, 22 Mar 2024 — https://www.intechopen.com/chapters/1169739 — *PN² formalisation; predicted the result in 33 of 34 asymmetric wargames.*
- Companion chapter (ternary mixed-force) — https://www.intechopen.com/chapters/1197733
- Ian, "Lanchester's Laws and Attrition Modeling" Parts I & II — http://giantbattlingrobots.blogspot.com/2010/06/lanchesters-laws-and-attrition-modeling.html · http://giantbattlingrobots.blogspot.com/2010/07/lanchesters-laws-and-attrition-modeling.html — *close combat = linear law, ranged = square law; the square law is about rate of target acquisition.*
- https://en.wikipedia.org/wiki/Lanchester%27s_laws
- "An Analysis of Wargame Rules Simulation Based on Stochastic Lanchester Models," ACM — https://dl.acm.org/doi/pdf/10.1145/3171592.3171612
- Naval Postgraduate School lecture notes — https://faculty.nps.edu/awashburn/Files/Notes/Lanchester.pdf

### Academic / automated balancing
- ★ Volz, Rudolph & Naujoks, "Demonstrating the Feasibility of Automatic Game Balancing," arXiv:1603.03795 — https://arxiv.org/abs/1603.03795 (HTML: https://ar5iv.labs.arxiv.org/html/1603.03795) — *multi-objective evolutionary balancing (SMS-EMOA) on Top Trumps; auto-generated decks matched or beat published ones on fairness; ~2,000 simulated games per evaluation.*
- Rupp & Eckert, "GEEvo: Game Economy Generation and Balancing with Evolutionary Algorithms," IEEE CEC 2024, arXiv:2404.18574 — https://arxiv.org/abs/2404.18574
- Zeng et al., "RuleSmith: Multi-Agent LLMs for Automated Game Balancing," arXiv:2602.06232 (Feb 2026) — https://arxiv.org/abs/2602.06232
- https://arxiv.org/abs/2503.18748 · https://arxiv.org/pdf/1705.01080

### Warhammer 40,000 — the wargear arc (§7.14)
- ★ https://www.warhammer-community.com/en-gb/articles/CXVAwhpX/get-all-of-your-points-for-free-with-the-first-munitorum-field-manual-of-new40k/ — **Robin Cruddace's 10th-ed rationale: *"added to the complexity… for little gain regarding the actual output of the unit"*, and the sidegrade justification**
- ★ https://www.warhammer-community.com/en-gb/articles/8wi6x7nq/new40k-points-apps-and-updates-incoming/ — **11th edition (June 2026): selective wargear costs return, points steppers, cadence**
- https://web.archive.org/web/20220811083206/https://www.warhammer-community.com/2017/05/12/new-warhammer-40000-points-power-levels-may12gw-homepage-post-4/ — **the 2017 decision to move points off the datasheet so they could be patched**
- https://www.warhammer-community.com/en-gb/articles/I5wfEd9K/metawatch-warhammer-40000-new-year-new-balance-dataslate-new-munitorum-field-manual/ — 9th ed *"wargear and weapon options are now largely free"*; win-rate language
- **Primary codex scans** — https://archive.org/details/warhammer-40-000-4th-edition-space-marines-codex ★ *(the heavy bolter +5 / +15 table)* · https://archive.org/details/warhammer-40-000-3rd-edition-space-marine-codex · https://archive.org/details/warhammer-40-000-5th-edition-space-marine-codex *(OCR corrupted — figures marked UNVERIFIED)*
- https://github.com/BSData/wh40k-8th-edition — 8th-ed catalogues parsed directly for cross-codex weapon costs (community transcription of official codices)
- ★ https://www.tabletopbattles.com/40k-11th-edition-points-review-overview — 11th-ed points steppers and selective wargear; the *"cost the decision, not the item"* proposal
- ★ https://www.goonhammer.com/the-goonhammer-review-the-10th-edition-munitorum-field-manual-chaos/ — **the homogenisation cost: *"flails and cleavers and maces are all just boring plague weapons"***
- https://www.goonhammer.com/10th-edition-roundtable-lessons-learned-from-our-practice-games/ — the anti-free-wargear argument
- https://www.tabletopbattles.com/the-goonhammer-review-the-munitorum-field-manual-xenos — *"priced out of its usefulness"*
- https://www.tabletopbattles.com/hammer-of-math-understanding-tiwp-and-faction-representation/ — TiWP methodology, 45–55% band, significance testing
- https://www.goonhammer.com/goonhammer-hot-take-the-big-power-levels-update — Power Level's granularity failure
- https://frontlinegaming.org/2017/06/18/making-the-case-for-using-power-level-points-in-tournaments/ — the pro-PL case; illegal-list overhead
- https://www.wargamer.com/warhammer-40k/points — cross-edition overview and the 9th-ed erosion
- Datasets: https://www.stat-check.com/the-meta · https://woehammer.com/2026/01/15/woehammer-data-literacy-why-faction-win-rates-alone-are-bad/ · https://listhammer.info/stats
- *Note: goonhammer.com blocks WebFetch but is reachable via curl, and now also publishes as tabletopbattles.com.*

### Warhammer 40,000 — army composition
- Chris Morgan, "40K Op-Ed: GW Wants Us to Eat Soup," Frontline Gaming (2018) — https://frontlinegaming.org/2018/10/02/40k-op-ed-gw-wants-us-to-eat-soup/ — *cross-faction detachment synergy; the "Loyal 32."*
- Goonhammer, "Hammer of Math: Toughness Distribution in Warhammer 40k" — https://www.goonhammer.com/hammer-of-math-toughness-distribution-in-warhammer-40k/ — **[UNVERIFIED]** *the site blocked automated fetching on every attempt (blank responses ×4). Figures circulating in search snippets were not confirmed by reading the page and are flagged as unconfirmed in §6.1.*
- https://www.belloflostsouls.net/2019/09/warhammer-40k-horde-vs-elite-competitive-armies.html
- https://www.belloflostsouls.net/2017/10/40k-why-8th-edition-made-hordes-the-best.html

### In-repo sources (this project's own data)
- `rules-vault/Rules System/List Building.md` — rank ladder 5/8/16/24, the "points buy bodies and guns" claim, the 11-point spread validation.
- `rules-vault/Rules System/Weapons.md` — the weapon construction system, class and characteristic costs, the two hard ceilings.
- `rules-vault/Rules System/Unit Design.md` — stat scale, tier caps, "the rank price is the stat price."
- `rules-vault/Rules System/Crew Sim — Findings.md` — the 66-point terrain swing; 11 vs 34–35 point spreads; the range-threshold finding (13–30 points at any price); horde/elite parity.
- `rules-vault/Rules System/Skill Sim — Findings.md` — Quick Shot +24 win% / +67% output; the flat +10%/point confirmation; Steady/Rattle-Proof context-dependence.
- `rules-vault/Rules System/Dice Mechanic — Sim Findings.md` — you cannot price a stat in a vacuum.
- `docs/BLKOUT-RULES-ANALYSIS.md` — the existing BLKOUT read-through.

### Searched and found nothing (recorded so the gap is known)
- **No published formula, in any game or design essay, for discounting a conditional ability.** The only published *mechanisms* are Hero System's Limitations division and GURPS' percentage limitations.
- **No rigorous published measurement of action-economy underpricing.** Strong consensus, genuine evidence gap.
- **No commercial miniatures game found that derives its costs from simulation.** The academic literature exists; nobody in the hobby appears to have shipped it.
- **X-Wing 2.5's "Loadout Value" dual-currency** was identified as a highly relevant case (ship points vs a separate upgrade currency) but **could not be verified** — the fan wiki returned HTTP 402 and Wikipedia's article does not cover squad-building economics. Flagged as the highest-value follow-up.
- Blocked to automated access: goonhammer.com, dakkadakka.com (403), boardgamegeek.com (403), reddit.com (all r/wargamedesign threads), springrts.com (anti-bot), tools.battletech.dev (403).

---

*Compiled 2026-07-27. All formulas quoted from published or open-source material; all arithmetic on the Settlements engine is labelled as inference and is reproducible from the rules as written.*


---

## 10 · Necromunda & Mordheim — the campaign-economy lineage

*The campaign-economy ancestor of everything Settlements is building: Blood Bowl → Necromunda (1995) → Mordheim → the 2017 relaunch. Primary sources: OCR of the 1995 Necromunda rulebook (archive.org), Mordheim rulebook PDFs (broheim.net), plus Goonhammer, yaktribe, r/necromunda and r/mordheim. The two findings with immediate design consequences — stash exclusion from rating (§10.1) and the play-frequency snowball (§10.5) — are carried into the recommendations at §8.11.*

### 10.1 · Rating is a snapshot, not cumulative spend — [FACT]

1995 Necromunda, verbatim: *"The gang rating is simply the total value of all the fighters in the gang plus their total Experience points."*

Three consequences the rules state explicitly:

- **Stashed gear does not count.** *"Any weaponry or other equipment that the gang keeps but does not give to a fighter is hoarded... its value is not included in the gang rating."*
- **Mercenaries convert by formula, not hire cost.** *"For purposes of the gang rating the value of a Hired Gun is his hire fee x5."* Verified consistent across Scummers (15→75), Bounty Hunters (35→175), Ratskin Scouts (15→75).
- Rating can **fall** after a game you spent money in, or **rise** with no spending at all (XP).

**Direct relevance to Settlements.** The Armory question — whether unequipped gear counts toward crew rating — has a strong precedent: **it should not.** Necromunda excludes stash explicitly, and it is what makes their underdog banding mathematically sane. Ownership is wealth; rating is fielded power.

**Contrast — Mordheim hand-tunes the same thing.** Its Hired Swords have flat Rating values with no consistent ratio to hire fee: Ogre 80gc→+25 (0.31), Pit Fighter 30gc→+22 (0.73), Halfling 15gc→+5 (0.33). A deliberate balance-by-feel choice. Two shipped games, two opposite philosophies — pick one on purpose.

### 10.2 · Starting budgets — [FACT]

Necromunda 1995: *"You have 1000 Guilder credits to spend on recruiting and arming your gang."* Mordheim: *"You have 500 gold crowns to spend"*, identical across all six warband lists.

Both land exactly where Settlements' rescale is heading.

### 10.3 · Underdog bonuses scale by rating difference — [FACT]

Two paired tables, both keyed to the **gap** between gangs, not to absolute wealth.

**Underdog XP bonus** (per surviving fighter, lower-rated gang): +1 win/+0 lose at a 1–49 gap, rising one step per band, to +10/+9 at 1500+.

**Giant Killer income bonus** (underdog who wins): +5 at 1–49, +10, +15, +20, +25, +50, +100, +150, +200, +250 at 1500+.

Scenario choice is *also* an underdog lever — the lower-rated gang rolls on the scenario chart in some formats.

The 2017 relaunch splits this in two: **Gang Rating** (whole roster, campaign standings) versus **Crew Rating** (only the fighters in this battle, for underdog math). Community had to write a clarifying FAQ because players could not keep them straight. **If Settlements ever builds both, the rule text must name which one every derived rule keys off.**

### 10.4 · Wealth gets gated twice, or once — a deliberate choice — [FACT]

- **1995 Necromunda double-gates:** you must be *offered* the item (D3 items, D66 roll on a rare chart) **and** pay a variable premium (*"40+3D6 credits... the extra variable cost is the additional rarity value"*).
- **2017 Necromunda single-gates:** fixed catalogue price, but roll `2D6−1` against the item's Rarity(N) to see whether it is on the shelf at all. A fighter can spend a post-battle action on *Seek Rare Item* to get an extra roll at `2D6+1` — trading income for access.
- **Mordheim single-gates with scaled cost:** `2D6` vs Rarity(N), only **Heroes** may roll, **one roll each**. So a 4-Hero warband gets at most 4 rare shots per cycle *regardless of gold*. Some items multiply rather than add (Gromril 4× at Rare 11, Ithilmar 3× at Rare 9).

**The shared principle: raw stockpiled money must not convert straight into the best gear.** Every one of these is an anti-snowball lever operating independently of the underdog bonuses.

### 10.5 · Play frequency can dwarf skill as a snowball source — [FACT]

Goonhammer, *Hammer of Math: Necromunda Campaign Economics Part 2* (Kevin Genson, Jan 2023), a 100,000-run simulation:

> *"The median credits earned after a full campaign was 750 credits assuming one game per week and with two it's at 1170."*

**This is the most directly threatening finding for Settlements.** The game deliberately persists **outside** campaigns — rosters and settlements grow game-to-game whether or not anyone is running a campaign. That is exactly the structure this measures: whoever plays more, wins the meta, with no skill or luck involved. Any per-battle income tap creates it.

Mitigations shipped by other GW games, per community consensus: Blood Bowl's *Expensive Mistakes* tax on hoarded gold plus free money for the loser; Mordheim's diminishing-returns wyrdstone "wash table"; Necromunda Outlanders' income wash table that softly enforced a gang-size band.

### 10.6 · Some failures cannot be priced away — [COMMUNITY CONSENSUS, strongly corroborated]

Mordheim's most notorious balance problem is **not** a mispriced item. Dual single-handed weapons beat shield/armour so reliably that armour is considered near-worthless — an emergent property of how parry and to-hit resolve. *"2x weapons is so extremely overpowered that it's basically always better to go with a 2nd weapon (even just your base free dagger) over a shield."* No per-item price fix addresses it, and GW never patched it.

Contrast with Skaven slings, which **are** a straightforward costing bug: community math shows 2 slingers wound an average henchman firing twice, at 44gc total, versus 3 pistol warriors at 120gc with worse range. That one got partially errata'd.

**Two distinct failure classes, and a costing system only fixes one.** A points rebuild must test for rules-interaction failures separately, because no amount of correct pricing will surface them.

### 10.7 · Designer intent — [FACT]

Andy Chambers, 1995 Necromunda co-designer, interviewed on yaktribe (Oct 2017):

> *"Necromunda worked on having a campaign and an RPG-like feel so it wasn't even necessary to make the scenarios all fair and balanced in a traditional sense as long as risk equaled reward for the players and the scenario itself had a good strong narrative going... Jervis Johnson's experience with Bloodbowl was absolutely key as it gave us the progression and loot rules that rewarded gangs for every game played, doubly so against tough opponents."*

Confirms the underdog-bonus concept as a direct Blood Bowl → Necromunda → Mordheim lineage, and that **competitive symmetry was explicitly not the design target.** Worth deciding on purpose rather than inheriting by default.

### 10.8 · Sources

**Necromunda primary:** archive.org `games-workshop-necromunda-rulebook` · `necromunda-hardback-rulebook-compilation` · `necromunda-outlanders`
**Necromunda 2017 (fan transcription):** killershrike.com/Necromunda/Underdog.aspx · /TradingPost.aspx · /Campaigns/GangWar/PostBattleSequence.aspx
**Commentary:** tabletopbattles.com/necromunday-underdogs-and-catch-up-mechanics/ · goonhammer.com/hammer-of-math-necromunda-campaign-economics-part-2/ · yaktribe.games/article/the_loaded_dice_table_talks_page_3.6/ (Chambers interview) · yaktribe.games/community/threads/underdog-gang-rating-and-tactics-cards.13678/ · reddit.com/r/necromunda/comments/webriy/
**Mordheim primary:** broheim.net/downloads/rules/ — Part 1 (Background & Rules), Part 3 (Campaigns & Optional Rules)
**Mordheim community:** reddit.com/r/mordheim/comments/1pe7xir/ · /mq1k5y/ · /6y7ekt/ · /vyjgo9/

---

## 11 · Known gaps — what this report does *not* cover

Two research threads terminated on an API session limit. Everything else in the original brief was completed.

**Everything in the original brief has now been covered.** The two streams that failed on a session limit were re-run successfully — 40k is at §7.14 and the McCullough games at §7.12–7.13.

**Verified and closed:** One Page Rules (§1.3 — full official formula recovered and verified 4/4 against OPR's own worked examples) · Trench Crusade (§7.10 — rulebooks and BattleScribe data read directly) · BLKOUT (§7.0 — unit cards read directly, confirmed to carry no cost of any kind) · 40k across all editions including the June 2026 11th-edition reversal (§7.14) · Frostgrave, Stargrave and Rangers of Shadow Deep (§7.12–7.13, from primary PDFs).

**Nothing outstanding — all streams complete.** Oathmark closed last (§7.15), from the official Osprey Kingdom Building extract and the official Army Planner PDF (154 exact published point values extracted).

**Known data problems to be aware of:**
- **Trench Crusade is in open playtest** and every page is stamped PLAYTEST RULES. Two revisions were read and they disagree on the Threshold ladder, on Coin Hammer's price (20 vs 25), on the no-culling rule, and on whether the Heretic Musical Instrument is 15 ducats or 1 Glory. Structure is reliable; individual numbers are not.
- **5th-edition 40k codex OCR is corrupted** (systematic 1→7 misreads). Those figures are flagged [UNVERIFIED] in §7.14 and were not used for any conclusion.
- **The Stargrave extract truncates at p.79**, so the entire "Spending Loot" chapter — campaign re-hire costs, advanced technology prices, ship upgrades — is missing (§7.12).
- **Reddit is fully blocked** in this environment. All Reddit-sourced community sentiment anywhere in this report is snippet-only and tagged [CONSENSUS] accordingly.
- **No first-hand Sean "Kromm" Punch quote** was obtainable; nothing is attributed to him.

**One note on the OPR find and this repo.** `ff.py` in the test-bench uses OPR vocabulary (Quality, Defense, Pierce, Blast, Deadly, Torrent, Rending). §1.3 now contains OPR's actual derivation, so that engine can be checked against the real formula rather than reverse-engineered.

**Unexploited leads, in priority order:**
1. **Precinct Omega Podcast, "Design #8 — Points Systems, Army Building and Balance"** (78 min, ~£1 for the transcript via Patreon) — a working designer talking directly about points-system theory. The richest single unexploited source found.
2. **The Fundamentals of Tabletop Miniatures Game Design** (Ford & Hutchinson, CRC Press 2024) — most likely place a published costing rationale exists; publisher sites blocked automated access.
3. **The current OPR Point Calculator** (Patreon Tier 3). The recovered v1.10 is ~2020 and the live Army Forge engine appears to have diverged.
4. **X-Wing 2.5's "Loadout Value"** — squad points plus a separate per-ship upgrade currency. Highly relevant to the dual-currency question; every source attempted was blocked.

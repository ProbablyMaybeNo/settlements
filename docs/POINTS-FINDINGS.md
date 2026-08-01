# Points & Settlement Research — Findings and Decisions

*Wrap-up of the costing research pass, 2026-07-27. Full evidence, sources and per-system detail in **`POINTS-RESEARCH.md`** (1,900 lines). This document is the decision layer: what we learned, what it means for Settlements, and what to do next.*

---

## 1 · What was covered

Eighteen systems, prioritising **primary sources** — rulebooks, official calculators, open-source implementations and machine-readable data — over commentary.

| System | What it gave us | Derivation published? |
|---|---|---|
| **One Page Rules** | **The complete official formula**, recovered and verified 4/4 against OPR's own worked examples | **Yes** (paywalled, since withdrawn) |
| **BattleTech BV2** | Full formula, verified against MegaMek source | **Yes** |
| **Song of Blades & Heroes** | Formula **derived by us** from the official chart, validated 34/34 | Chart yes, formula no |
| **Rogue Trader (1987)** | A published points formula, incl. GW's own super-linearity fix | **Yes** |
| **40k Vehicle Design Rules** | A published construction system with BS-dependent weapon pricing | **Yes** |
| **Warhammer 40,000, all editions** | The 25-year wargear arc, ending in June 2026's partial reversal | No |
| **Oathmark** | **Kingdom → army entitlement.** The settlement analogue | No |
| **Trench Crusade** | Modern dual-currency campaign economy; 4 tuning dials per item | No |
| **Frostgrave / Stargrave** | Two currencies that never touch; base resources that edit prices | No |
| **Rangers of Shadow Deep** | **The archetype pattern** — the best faction idea found | No |
| **Necromunda / Mordheim** | The campaign-economy lineage; rating vs stash | Partial (advancement only) |
| **Infinity** | Dual currency (Points + SWC), platform-scaled gate costs | No |
| **Warmachine/Hordes** | The only published account of a points **rescale** | No |
| **Malifaux** | The +1 out-of-keyword tax | No |
| **Kill Team** | Three costing philosophies in six years — a natural experiment | No |
| **Gaslands / Rampant / Horizon Wars / Bolt Action** | Slots, integer atoms, force-dependent cost, naive additive | No |
| **GURPS / Hero / M&M** | The deepest atomic systems and their documented breakages | **Yes** |
| **BLKOUT** | Confirmed: **no points system at all** | N/A |
| **Last Days: Zombie Apocalypse** | **The closest thematic match.** Free base, upkeep-scales-with-development | No |
| **The Walking Dead: All Out War** | A published custom-build formula + the neutral-threat design | **Yes** (custom characters only) |

**The canonical text**, read in full and verified: **K. Robert Gutschera (Director of Development, Wizards of the Coast), "Magic Lessons: Designing and Balancing Game Objects," GDC 2007** — explicitly addressed to *"collectable miniatures games like Warhammer 40K."* Free, and the closest thing the field has to a textbook.

---

## 2 · The five things that actually matter

### 2.1 Your engine is unusually friendly to atomic costing — and the caps are why

Under `1d10 + mod vs 7+`, `P(success) = (4 + mod)/10` — **exactly linear**. So the absolute gain in kill probability from each successive +1 is **constant**: the 5th point of a stat adds the same 0.07 as the 1st. Most games have curved probability where linear costing is provably wrong. Yours doesn't.

**But the engine multiplies across factors.** `P(kill) = P(hit) × P(injure)`, so the value of +1 to hit is proportional to the damage side and vice versa. At `h=+2, d=+2` they're worth exactly the same; at `h=−1, d=+4` a point of hit is worth **2.67×** a point of damage.

> **A single flat "+1" price is only correct near the diagonal where hit and damage modifiers are roughly equal. Your existing hard caps — damage +4, armour −2, ±3 modifiers, stat max +6 — are precisely what pins builds onto that diagonal.**
>
> **They are not balance patches. They are what makes your costing valid.** Reclassify them as costing preconditions and never quietly relax one.

This also validates the current weapon table: Brutal (+1 damage) at 4 and Armour Piercing (−1 enemy armour) at 4 are correctly priced identically — both are +1 on the injury roll. **That is already an atomic derivation; it just hasn't been written down as one.**

### 2.2 Multiply what the engine multiplies

Every successful derived system does this, and it's the most consistent structural finding in the research:

- **One Page Rules:** weapon costs are **multiplied by the unit's Quality value**. A Quality step therefore costs ~1.75× a Defense step, automatically, with no separate offence/defence budget.
- **Song of Blades:** `Cost = (5×Combat + ΣAbilities) × (7−Quality)/2` — activation quality multiplies *everything*.
- **BattleTech:** mobility and pilot skill are multipliers; armour and weapons are addends.
- **Hero System:** advantages multiply, limitations divide.

> **Anything that changes how often — or how reliably — a model acts must multiply. Anything that changes how well one action lands can be added.** Settlements currently adds everything.

Two concrete consequences: **the rank price should split** into an additive stat component and a multiplicative command component (Orders and T3 skills are action-economy items bundled into a flat number today); and **weapons should be priced with the carrier's to-hit stat as a multiplier** — a rifle on a DEX+3 Specialist genuinely *is* worth more than the same rifle on a Recruit, and no additive table will ever say so.

### 2.3 Action economy cannot be priced — and that's arithmetic, not opinion

For a baseline model (h=+2, d=+3, P(kill)=0.42):

| Option | P(kill/turn) | vs baseline |
|---|---|---|
| Baseline | 0.4200 | — |
| **Max out every stat and damage cap in the game** | 0.7200 | ×1.714 |
| **One extra attack** | 0.6636 | ×1.580 |

**One extra action delivers 81% of the value of maxing everything else simultaneously.** Your own `Skill Sim` independently measured Quick Shot at **+24 win%** — the largest single-skill swing. Two methods, same answer.

Gutschera names this exact case as the archetypal *"non-scalable effect"*: *"It's always good to get a free attack."* And a single unconditional non-scalable effect **caps the top of your entire cost curve**.

> **Extra actions are earned by rank, never sold at a price.** You already do this. Write it down as policy so future additions get tested against it rather than re-litigated.

### 2.4 You cannot escape paying for differentiation

This is the sharpest lesson in the research, and it comes from GW running the experiment at scale for 25 years.

The arc: per-item wargear costs (3rd–7th) → dual system (8th) → quiet deletion (9th) → **all wargear free** (10th) → **June 2026, 11th edition partially reversed it.**

GW's stated reason for going free was **never fairness** — it was overhead versus yield. Cruddace: per-item costs *"added to the complexity of working out your army, for little gain regarding the actual output of the unit on the battlefield."*

But the hidden price surfaced immediately. Goonhammer on 10th-edition Death Guard: *"there's a lot less to love about that now that **flails and cleavers and maces are all just boring plague weapons**… a bunch of the options don't matter any more."*

> **To make N options cost the same, you must make them *worth* the same — so you homogenise the profiles.** Free wargear doesn't remove the balance problem; it **relocates it from the points column into the rules text**, and you pay in flavour.
>
> **Either you pay in points arithmetic, or you pay in differentiation. For a game whose pillar is a DIY armoury, flavour is the expensive currency.**

And per-item costing collapses on its own terms anyway: in one 4th-edition codex a heavy bolter cost **+5 on a Tactical Squad and +15 on a Command Squad** — a 3× spread on identical wargear, because the number was really pricing the *slot*. **Once an atom needs context-dependent prices, it has stopped being an atom and you've kept all the bookkeeping.**

### 2.5 The settlement solves a different problem, and Oathmark already solved it

Everything else in the research answers *"what does this cost?"* **Oathmark answers *"what are you entitled to field at all?"*** — your kingdom's composition determines your legal army list.

McCullough's central rule, verbatim:

> *"The kingdom might gain new territory, or it might have its territory occupied, but **when it comes to each game, the players are still playing to the same points value, and theoretically have an equal chance of winning.**"*

> **The settlement widens the menu, never the budget.** Growth is lateral, not vertical.

That single decision is what makes a persistent base safe to bolt onto point-buy — and it is already this project's locked principle (*"Goods/Materials buy what you own, points gate what you field"*). **Oathmark is the proof it scales to a full campaign.**

The strongest evidence it works: **no broken *kingdom* build has ever been reported.** Every Oathmark balance complaint attaches to unit costs or battlefield rules. The constraint layer holds even where the costing layer is shaky.

---

## 3 · The decisions this research puts in front of you

Each of these is a genuine fork with shipped precedent on both sides.

### Fork A — Does gear cost points at all?

| Option | Precedent | Cost |
|---|---|---|
| **Keep priced characteristics** (status quo) | Necromunda, Trench Crusade, Infinity | Arithmetic overhead; every characteristic must be right |
| **Free by default, priced at proven outliers** | **40k 11th edition (June 2026)** | Needs a patch channel; risks homogenisation |
| Fully free | 40k 10th, Kill Team 2021 | Kills the DIY armoury |

**Recommendation: keep priced characteristics, and import two things from 11th edition** — the **points stepper** (a super-linear surcharge on your 2nd/3rd copy of a thing) and **"cost the decision, not the item"** (price *"this fighter is a specialist shooter"* once, rather than each characteristic separately). Full free-wargear costs you the pillar of the game.

**But run GW's audit on `Weapons.md` this week.** Free wargear only works when options are *sidegrades*; the corollary is that **any characteristic that is a straight upgrade rather than a sidegrade must be priced or gated.** That's a concrete pass you can do today.

### Fork B — Do veterans get re-priced?

| Option | Precedent |
|---|---|
| **Price them** — +2 per Advance (status quo) | Necromunda, Mordheim |
| **Never price them; cap the count instead** | **Trench Crusade** — warband value counts models and gear only; XP and skills are free, but max 6 ELITE, 2 scars then death, one promotion per battle |

**Recommendation: this is genuinely close, so pick deliberately.** Trench Crusade's way makes veterans feel *precious* and moves the anti-snowball job onto caps, which are harder to game than prices. Your way produces the narrative you've already written (*"the war grinds you down to a handful of hardened survivors"*), which is the better story.

**The failure mode is a weak version of both** — taxing veterans enough to annoy without capping them enough to contain. Whichever you choose, add a `Limited Potential` equivalent: a per-model ceiling on total advancements. One keyword, and no single model becomes the campaign.

### Fork C — How do factions get built?

**Recommendation: steal the Rangers of Shadow Deep archetype pattern.** It's the best single idea found for this.

An archetype replaces the base stat-line, grants free traits (*"their cost has already been factored into the balance of the archetype"*), and **adjusts the build-point budget and the per-category sub-caps** — 8 to 10 BP depending on how strong the freebies are.

> **The unit costs never change. Nothing in the catalogue is ever repriced.**

Ten distinct archetypes sharing one price list, differentiated purely by budget and caps. **It scales to any number of factions without a costing audit each time** — which is exactly the cost that makes faction design expensive in every other game examined.

Layer Malifaux's **+1 out-of-keyword tax** on top (one flat modifier makes thematic crews cheaper than optimised ones, with a named `Versatile` exemption for units meant to travel), and you have faction identity for almost no balance risk.

### Fork D — What does the settlement grant, and how is it constrained?

**Two shipped answers sit at opposite ends of the axis, and you should pick a position on it explicitly:**

| | **Oathmark** | **Last Days** |
|---|---|---|
| Points per battle | **Equal, always** | **No limit after creation** |
| Base grants | Menu width only | Capacity, economy, some battle effects |
| Snowball brake | The equal-points rule | **Attrition + upkeep** |

**Recommendation: take Oathmark's *entitlement* rule and Last Days' *upkeep* rule.** They're compatible, and together they're stronger than either alone.

**Recommendation: Oathmark's architecture, wholesale.** Permission, never points.

- **Concentric rings with a rarity gate** — core restricted and coherent, frontier permissive and strange. One table of rarity numbers replaces a whole chapter of restrictions.
- **Two unlock grammars only** — *"as many as you can afford"* or *"6 per structure, and 2 structures means 12."*
- **Heroes capped by buildings, not a points percentage.** Each additional Specialist costs a structure slot. Efficient, given your 9–12 density constraint.
- **Losses soft and reversible.** Occupied ≠ destroyed. His stated reason is worth keeping: players shouldn't lose access to models *"they have bought and painted (because that would be really annoying)."*
- **An "unreliable frontier" tier** for anything too strong to price and too fun to cut. Location as a balancing axis — free if you already have rings.

And from his 2nd-edition retrospective (June 2026), three regrets you can avoid for free: **start the settlement at ~30% of its ceiling** (he gave players everything on day one), **lead the rulebook with the settlement not the battle** (presentation taught players which layer mattered, and taught them wrong), and **don't suppress a subsystem out of fear** (he underpowered magic because it worried him and got spellcasters nobody used).

**Then bolt on Last Days' constraint layer** (§6):
- **The base is free and described by three numbers** — Max Group Size / Empty Spaces / Built-In Perks. It never competes with the crew for a budget, and choosing one is a *shape* decision.
- **Building slots are the real constraint; resources only decide *when*.**
- **Development raises upkeep** — upkeep scales with built structures *and* headcount, so a bigger base costs more every turn, forever. Include at least one **upkeep-reducer** structure so efficiency competes with capability for a slot.
- **One post-game roll couples the battlefield to the base** — 2D6, −1 per casualty, +1 per Guard, low result costs you structures. Plus an **insurance structure** that protects your stash if it happens.
- **Score the base.** If the settlement isn't in the victory condition, players will optimise around it.

### Fork E — One currency or two?

**Recommendation: you already have the right answer; don't add a third.** Goods/Materials for ownership, points for fielding. That's the Necromunda split (*"stashed gear does not count toward rating"* — ownership is wealth, rating is fielded power) and it settles the open Armoury question directly.

**Don't add a second battle currency.** Rank gates already do Infinity's SWC job — they need no bookkeeping and read off the model. What Trench Crusade adds worth copying is **four tuning dials per catalogue entry**: price, `LIMIT: N` (per-warband purchase cap), `0-N` (roster slots), and value-gated caps (*"0-2 of these in a force worth over X"*). Price and cap are independent levers; a single price has to do both jobs and does neither well.

---

## 4 · What to do next, in order

1. **Write down the caps as costing preconditions** (§2.1). Half a page. Everything downstream depends on it.
2. **Run the sidegrade audit on `Weapons.md`** (Fork A). Any characteristic that's a straight upgrade gets priced or gated. Cheap, and it's the single highest-value pass available today.
3. **Build the vanilla curve first** — rank costs with *no skills and no gear* (Gutschera rule 5: *"if you can't do it this way, then each object becomes a new thing to playtest, and you will run out of testing resources long before you are done"*).
4. **Instrument conditional traits in `crew_sim.py`** to measure `f`, the rate at which each condition is actually met. Then set the discount from the measurement: **`L = (1 − f)/f`**, applied as `Cost = Unconditional ÷ (1 + L)`. This lands exactly on Hero System's published quarter-step ladder — so the numbers aren't invented, they're a re-derivation of a system in print since 1981. **No published game measures `f`; they all guess it.** This is a real edge and it's about a day's work.
5. **Declare the reference environment** — board size, terrain density, round count, objective type, assumed opposing stat line — and derive every cost against it. **BattleTech's largest published flaw is an unrecorded assumption about to-hit numbers that nobody revisited for eighteen years.**
6. **Ship a residuals table** — derived value vs listed cost vs measured win-rate contribution, for every armoury entry. The reconstructed Warhammer Fantasy formula is credible *solely* because it publishes 16 computed-vs-published comparisons.
7. **Publish costs in a separate versioned artefact**, never embedded in rules text. GW moved points off the datasheet in 2017 specifically so they could be patched, and **every balance correction across three editions depended on that one packaging decision.**

---

## 5 · Risks worth monitoring

- **Point-buy degeneration.** Gutschera: pure point-buy *"has arguably never been done successfully… [these systems] tend to degenerate to a single viable character build."* Your sim already shows the symptom — *"A Fighter has one real build: STR"* (STR+2 at 14/35/63% across densities vs DEX+2 at 5/16/36%). The fix is Fork C plus scenarios that actually reward AGI and INT, not repricing.
- **Play frequency out-snowballs skill.** A 100,000-run Necromunda simulation found median campaign income of **750 credits at one game per week versus 1,170 at two.** Settlements persists *outside* campaigns by design — exactly the exposed structure. A diminishing-returns income wash table is the cheapest shipped mitigation.
- **Don't chase a flat 50% across archetypes.** Gutschera: *"if you try to balance them so that each one wins 50% of the time, you will surely slip up."* A deliberate 60/40 rock-paper-scissors triangle survives a 10% costing error; a flat field doesn't.
- **The 1000-point rescale is the container, not the answer.** Privateer Press did exactly this and called the re-costing that followed *"long, arduous."* They held army size constant and spent the entire gain on resolution — which is the right move. **If every price still ends in 0 after the rescale, it bought nothing.** Spend the granularity on the multipliers.

---

## 6 · Last Days & The Walking Dead — the closest thematic matches

Both read in full from primary PDFs. **Last Days is the single most relevant game in the entire research pass** — same genre, same fantasy, same shape — and it makes the *opposite* structural choice to Oathmark, which is why the pair should be read together.

### 6.1 The two poles of the design space

| | **Oathmark** | **Last Days** |
|---|---|---|
| Points per battle | **Equal, always** | **No limit after creation** |
| What the base grants | Menu width only | Capacity, economy, and some battle effects |
| Veteran pricing | n/a | Never re-priced (XP is a separate currency) |
| Anti-snowball via | The equal-points rule | **Attrition and upkeep** |

**Neither is broken. Pick your position on the axis deliberately** — the failure mode is drifting between them without deciding.

### 6.2 The best idea found for a settlement game: development raises upkeep

Last Days *Seasons*: **rooms to heat = built-in Perks + the Empty Spaces the Refuge starts with**, one Fuel each per Encounter in cold months — plus one Meal and one Water per Character per Encounter.

The Outdoor Campsite (12 models, 10 spaces) burns **10 Fuel every winter turn**. The Cabin in the Woods (5 models, 3 spaces) burns 4, halved to an effective 2 by its free Wood-Burning Stove.

> **A bigger, better-developed base costs more every single turn, forever.** A growth curve that self-limits with no points ceiling at all.

The corollary is just as good: because the Stove exists, **the tech tree contains upkeep-reducers**, so "invest in efficiency" competes with "invest in capability" for the same building slot. One catalogue entry buys a genuinely interesting decision.

### 6.3 The Refuge interface — steal this shape

The Refuge is **free** and sits outside the 100-point budget entirely. It is fully described by three numbers: **Max Group Size / Empty Spaces / Built-In Perks.**

The settlement therefore never competes with the crew for the same currency, and choosing a base is a **shape** decision rather than a **spend** decision. The trades read instantly: Gun Shop = 6 models but three free Perks; Outdoor Campsite = 12 models and 10 build slots but nothing free and +5 SP on everything.

**Empty Spaces (2–10) is the real constraint; money only decides *when*.** That gives every player a bounded, comparable settlement without the settlement needing a points value at all.

Three further mechanisms worth taking whole:
- **Buildings that unlock units, priced separately.** Stable (20 SP) → 0–2 Horses at 15 SP each; lose the Stable and the Horses leave the roster. Clean gate, honestly-costed unit.
- **Sort every structure into capacity / economy / battle-effect** — and note that Last Days confines almost all battle effects to the one scenario where your base is on the table. If you want equal points every game, that's how you get it while still having a meaningful base.
- **Jobs.** Every able-bodied model takes exactly one: Guard / Work a Perk / Build / Recruit / Gather. One Character per Perk, all assigned before any outputs are rolled. Real opportunity cost, near-zero overhead, and it ties crew size directly to settlement throughput.

### 6.4 Couple the battlefield to the settlement with one roll

**Every post-game: 2D6, −1 per casualty, +1 per Guard, +1 for the right Perk. Result ≤ 2 and you lose the Refuge.** Ten seconds, every turn.

Losing it costs all Perks and your entire stash — **unless you built the Escape Vehicle Perk**, whose whole function is insuring against that catastrophe. Banked currency survives; you're forced down to a smaller base type; anyone who doesn't fit is left behind.

Two things to steal: **the coupling** (your battlefield casualties directly threaten your base — most base-building games never connect the two), and **the insurance-Perk pattern** (a building that competes for a slot purely as catastrophe cover).

### 6.5 Score the base if you want players to care about it

Last Days' optional ending: first group to fill **every** Empty Space, hit **Max Group Size**, and bank **300 unspent points** wins outright. And the *Seasons* campaign scoring pays **+5** for a fully-built Refuge, **+1 per healthy survivor**, **−1 per critically-ill survivor**, **+1 per 10 banked points** — and only **+5** for having the strongest force.

**Raw military power is worth 5 points out of 20+.** The scoring deliberately does not reward the biggest army.

### 6.6 From The Walking Dead — three transferable ideas

**A published custom-build formula, plus the most honest admission in the research.** Characteristic dice cost X/Y/Z by tier and position; Nerve, Health and Pack Slots have flat prices. Then, verbatim: *"**As there's no way of accounting for every possible combination of characteristic and ability, it's hard to truly gauge the effectiveness of a custom character, so these rules include a slight premium.** As a result, it's best to only use custom characters in friendly games."* They ship the formula, **add a deliberate premium for the combinations they can't price**, and quarantine the system to friendly play. That is Gutschera's "value and cost should differ, and you should know by how much," implemented.

**The neutral threat is costed against the game, not against either player.** *"Walkers are 15 points each, chosen to the same points limit as the game, rounding up"* — 4 walkers in a 50-point game, 20 in a 300-point game. Nobody pays for them out of their list, and **a bigger game is not a safer game.** Combine with Last Days' Noise Tokens (each shot risks summoning a zombie) and you get a self-regulating third party that punishes exactly the alpha-strike behaviour flagged as a risk in `BLKOUT-RULES-ANALYSIS.md`.

**Territory that costs you safety.** Six of eighteen Special Locations do nothing but remove a purchasing restriction — pure Oathmark-style menu-widening. But **Danger Zones raise the starting Threat by +1 for every zone held by *either* player.** Expansion isn't free, the penalty is symmetric, and map greed becomes a real decision instead of an obvious one.

### 6.7 And one relevant data point on Fork B

**TWD re-prices veterans (+3 points per game survived). Last Days never does.** Two games, same genre, released within two years, taking opposite positions on the exact fork in §3. Neither is reported as broken — which is the strongest evidence available that this is a genuine design choice rather than a right answer.

---

*Full evidence and sources: `POINTS-RESEARCH.md`. Every claim there is tagged [FACT] / [CONSENSUS] / [INFERENCE] / [NOT FOUND] / [UNVERIFIED], with URLs.*

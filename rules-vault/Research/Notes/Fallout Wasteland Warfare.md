---
type: research-note
title: Fallout Wasteland Warfare
game: Fallout: Wasteland Warfare — post-apocalyptic skirmish with a base-building campaign layer
publisher: Modiphius Entertainment (under license from Bethesda Softworks / ZeniMax Media)
designer: James Sheahan (lead designer)
depth: primary — 5 official-line PDFs read in full (238 pages combined); one of the five (the Robots faction list) has unconfirmed official/fan provenance, flagged inline
retrieved: 2026-08-20
source_url: multiple product PDFs, see Source below
capture: research/sources/fallout-wasteland-warfare/
tags: [settlements/research]
---
# 🎲 Fallout Wasteland Warfare

> [!abstract] In one breath
> A **licensed Fallout miniatures skirmish game** built around a bespoke **d20 Skill Dice + up to four colors of stacked d12 Effect Dice** resolution — genuinely different machinery from anything Settlements can borrow wholesale — wrapped around a **Settlement/base-building campaign layer** (Homestead) and a **card-driven AI system** that runs everything from wilderness wildlife to enemy robots to full solo/co-op opponents. The dice engine doesn't transfer, but underneath it are several load-bearing structural ideas that do: a robot built from three interchangeable cards and priced as their sum, a named cheap-and-unreliable equipment tier, a settlement growth mechanic that widens a slot cap rather than a per-battle budget, and a swappable AI-override card that answers the same "does the board feel alive" want that [[Zona Alfa]]'s Zone Hostiles and [[Spectre Operations]]'s Solo/NPC rules already scored highly on.

| | |
|---|---|
| **Publisher · designer** | Modiphius Entertainment (license from Bethesda/ZeniMax) · James Sheahan (lead designer) |
| **Scale / format** | Skirmish, roughly 5–15 models a side, 32mm, 3'×3' typical battlefield |
| **Core resolution** | `d20 Skill Dice, roll ≤ adjusted Skill Value` (roll-under), modified by up to 4 stacked d12 **Effect Dice** per color (black=Damage, green=Accuracy, yellow=Armor Reduction, blue=Special Effect). An unmodifiable **X** result on the Skill Dice is always a failure. **[FACT — rules-of-play capture pp.10–11]**. This is fundamentally different machinery from Settlements' `1d10 + Stat vs 7+` — no mechanic below assumes it transfers as-is |
| **Depth of read** | **Primary** for 4 of 5 documents (official Modiphius product codes and trademark footers confirmed): Rules of Play (60pp), Into the Wasteland (24pp), Homestead Rules Expansion v2 (34pp), Automatron Player Rules (2pp). The 5th (Robots Battle Mode faction list, 11pp) has **unconfirmed** official/fan provenance — see its own section below and `meta.json` |
| **Raw capture** | `research/sources/fallout-wasteland-warfare/` in the Settlements repo — five capture files plus `meta.json` recording hashes, library paths, and the provenance question |
| **Source** | See **Source** section below — five separate product PDFs, all filed in `G:\My Drive\Wargaming\Fallout\` (a 1,211-file library; this run captured 5) |

---
## Why it's here

Fallout: Wasteland Warfare scored top of a 287-PDF sweep of Ross's library for tech-relevant content, and it's the closest whole-game match left uncaptured to Settlements' own shape: a genuine skirmish game (not an RPG), post-apocalyptic, with both a persistent crew *and* a base-building layer. Across the 135 mechanics logged in the hub before this capture, exactly one row mentioned hacking and one mentioned drones, and none mentioned robots, energy weapons, turrets, or optics — despite Settlements being 2051-grounded mil-tech with drafted but externally-unresearched [[Hacking]], [[Deployables]], and [[Infrastructure]] notes. Fallout is also the first source in the corpus to model **robots as a fully playable, buildable faction** (the Automatron system) rather than as flavor or a single enemy archetype, and its Homestead expansion is a genuine base-building layer that lands directly on [[Settlement]] and [[Structures]] — read here against [[Oathmark#The kingdom widens the menu]] and [[Last Days Zombie Apocalypse#The Refuge costs zero]], which disagree with each other about whether settlement growth should touch the per-battle budget.

The honest framing up front: **the dice engine is a hard no.** Settlements has no second dice type anywhere and a locked ±3 modifier cap; Fallout stacks up to four d12s per color on top of a d20 roll-under test. Every mechanic below had to be evaluated for whether its *value* survives being pulled out of that machinery — several don't, and are tagged accordingly.

---
## The core engine doesn't transfer — a d20 Skill Dice plus stacked d12 Effect Dice

**Type:** Dice · **Take:** 📎 reference (context, not a candidate)

A Skill Test rolls a single d20 **Skill Dice**, needing to roll **equal to or lower** than an adjusted Skill Value (roll-under, not roll-over). Alongside it, up to four d12 **Effect Dice** of a given color can be added by weapon/equipment: black adds flat Damage, green modifies the Skill Dice roll itself (typically making a higher roll count as lower — i.e. improving the odds), yellow reduces the target's Armor Rating, blue triggers named Special Effects. *"A single Skill Test cannot contain more than 4 of the same color Effect Dice. Any dice over this limit go unused."* **[FACT — rules-of-play capture p.11]** An unmodifiable **X** icon on the Skill Dice is always a failure regardless of bonuses. **[FACT — rules-of-play capture p.11]**

**Why it works.** It's a genuinely rich design — accuracy, damage, armor-piercing and special-effect triggers are four independently-tunable axes riding on one roll, so a weapon's identity is expressed by *which colors and how many* of each Effect Die it carries, not by a single flat stat block. That's real design value.

**For Settlements.** None of it is adoptable as-is — Settlements has locked `1d10 + Stat vs 7+` with **no second dice type anywhere** and a hard ±3 modifier cap, and this system is built from the ground up around a dice pool that can carry 16 additional dice (4 colors × 4 each) on a single test. Logged so every mechanic below can be read with the caveat already stated once: where a Fallout rule's value depends on this machinery, it's flagged, and the honest read is that the *idea* (e.g. "armor reduction is a separate dial from accuracy") is worth having, but the *implementation* is not portable.

---
## Computers — hacking as one Expertise skill among four, and a terminal that locks itself on a critical fail

**Type:** Hacking · **Take:** 📎 reference

There is no dedicated hacking subsystem. **Computers** is one of four **Expertise** skills (alongside Lockpick, Search, and Presence) usable via a single **Use Expertise** Action, gated by physical contact: *"Most Expertise Skill Tests require a model to be able to Interact with something. A model can Interact with an object if they are in base-to-base contact with it and they are not engaged."* **[FACT — rules-of-play capture p.29]** The rule itself is one sentence: *"This skill may be used to hack terminals or open safes with which the model is Interacting. If the Computers Skill Roll is an X, the terminal or safe is locked for the remainder of the current player's turn, during which no other Use Computers attempts can be made on that terminal."* **[FACT — rules-of-play capture p.29]** That's the entire hacking mechanic in the core rules — a flat Skill Test with a named lockout on the same critical-fail result (X) that fails every other Skill Test in the game, no separate hacking-specific dice, range band, or program menu.

**Why it works.** Reusing the existing critical-fail icon as the lockout trigger means "hacking" costs the rules nothing beyond one sentence and one Action name — no parallel resolution system, no new currency. The cost of that cheapness is that hacking here is flavor dressing on a generic skill-check Action, not a subsystem with its own texture.

**For Settlements.** Touches [[Hacking]] directly, and it's the single most useful negative result of this capture: **the highest-hacking-density file in the library sweep (into-the-wasteland, 22 hits) turned out to reference "hacked"/"hack" mostly in flavor text and AI-Trigger language, not in a deeper mechanic** — the actual rule lives entirely in this one paragraph in the core book. Compare against [[Infinity#Firewall — Comms Attack's version of Cover]] and [[Infinity#Total Control — possessing a TAG, and the four guardrails that stop it being a walking death sentence]], which is a considerably richer published hacking system than this one. If Settlements' own [[Hacking]] draft is worried about being *too thin*, this is reassurance that "one Skill Test, one named critical-fail consequence, done" is a real, shipped, sufficient answer at this scale — not every hacking system needs Infinity's depth. The honest gap: the **[NOT FOUND]** Campaign Handbook likely has more (terminal ranges, network effects on Robots/Turrets specifically) that this capture didn't reach.

---
## Investigation Markers and Searchable Markers — a two-layer scavenging pipeline gated by named skill icons

**Type:** Scenario · **Take:** ⚙️ adapt

Scavenging runs through two token types in sequence. **Investigation Markers** are placed face-down and can be looked at (no Action, no roll) by any model with both Line of Sight and range — *"A player can look at any face-down Investigation Marker(s) which are both: A. wholly or partly within the Awareness range, and B. within Line of Sight."* **[FACT — rules-of-play capture p.29]** Looking reveals one of: a Number (a specific scenario object), Blank (nothing), or **Searchable** (swap the marker for a face-down Searchable Marker). **Searchable Markers** require actual contact and are resolved by **which named skill icon appears on their underside** — Lockpick Required, Search Required, Computers Required, or a **Trapped** variant where success avoids a Danger card draw entirely. *"The Model can tell that this object is locked but it is also trapped. A successful Lockpick Skill Roll will gain the item without triggering the trap."* **[FACT — rules-of-play capture p.30]**

**Why it works.** The two-layer split (spot it for free at range, then resolve it up close with a skill-gated roll) means noticing loot and *getting* it are two separate risk decisions, and the skill-icon-on-the-token-itself design means the GM/scenario never has to write bespoke resolution text per object — the icon *is* the rule.

**For Settlements.** Touches whatever [[Scenarios]] eventually does with loot and hazard. Directly comparable to [[Zona Alfa#Salvage and Anomalies — loot and hazard sharing one system]], which collapses "search it" and "it might also be a hazard" into one system; Fallout keeps them as two sequential steps (spot, then resolve) gated by which of four skills the token demands, which is more moving parts (two token types, four skill icons) for a comparable amount of table texture. Worth weighing directly against Zona Alfa's single-system version for whichever is cheaper to teach.

---
## The Automatron — a robot built from three interchangeable cards, priced as the sum of its parts

**Type:** List · **Take:** ⭐ steal

*"Parts of different robots can be combined to create custom robots called Automatrons. Unlike most Units, an Automatron's Unit card consists of 3 cards: Head, Torso and Legs cards which are placed side-by-side to give the Automatron's total attributes, skills and abilities just like a single Unit card."* **[FACT — automatron capture p.1]** Construction is physical and literal: *"place a Head card, then a Legs card, and then a Torso card going left-to-right so the S.P.E.C.I.A.L. attributes are aligned. The combination of the numbers and skills along each attribute row gives the Automatron's attributes and skill values."* **[FACT — automatron capture p.1]** Pricing has no separate formula at all: *"The caps cost of an Automatron is the total of all the cards used to construct and equip it including weapons."* **[FACT — automatron capture p.1]** The AI for an unpiloted Automatron is likewise composited rather than bespoke: *"The AI for an Automatron uses the AI card that matches the Automatron's Head"* **[FACT — automatron capture p.1]**, with a stated fallback — *"if the Method is Ranged Combat and the model has no Ranged weapon, use Close Combat Method instead."* **[FACT — automatron capture p.1]**

**Why it works.** No new costing system was invented for a build-your-own unit — the existing per-card Caps prices simply sum, and the existing per-Head AI card simply gets reused with one stated fallback rule for the mismatch case. Modularity here is entirely free: three swappable slots, each independently priced and independently statted, recombine into a unit whose price and behaviour both fall out of arithmetic rather than a bespoke ruling.

**For Settlements.** The strongest single finding in this capture for the drone-operator want flagged in [[Ideas Inbox]] and for crafted-equipment tiering generally: **a unit built from N independently-priced, independently-statted parts, where the whole simply costs the sum, needs no new pricing machinery at all.** If Settlements ever wants a "build your own drone/robot chassis" system — swap a chassis, a sensor/weapon head, a mobility base — this is direct, load-bearing precedent that the arithmetic is genuinely free: no multiplier, no synergy tax, no combinatorial-explosion problem, because nothing about the pricing changes when the parts change hands between different combinations. The honest cost: it assumes every part is roughly commensurable (a Head is worth roughly what a Head is worth, whichever robot it came from) — the moment two parts have wildly different power levels for the same slot, "sum the parts" alone stops guaranteeing balance, the same failure mode any atomic-costing system risks (see [[Games Workshop published formulas#Epic — the negative result]]).

---
## Clunky — a named, priced-unreliable robot tier

**Type:** Costing · **Take:** ⭐ steal

*"Clunky robots are poorly built and, therefore, not totally reliable; however, they cost fewer Caps."* **[FACT — automatron capture p.0]** Mechanically, a Clunky robot rolls an extra die on activation that can add either a beneficial or a harmful token (discarded at the start of its next activation, so the swing never compounds), and the discount is a flat, unconditional percentage: *"A Clunky Robot's Caps cost is the cost of the entire Robot (including any cards equipped such as Mods, Weapons, Items, etc.) and then reduced by 20%."* **[FACT — automatron capture p.0]**

**Why it works.** One flat modifier (−20% Caps) plus one small random swing on activation is the entire rule — cheaper gear is named, priced, and made to *feel* cheaper (a genuine chance of a worse outcome each turn) rather than just being a smaller number on the same reliable chassis.

**For Settlements.** Directly relevant to the crafted < manufactured < near-future tech tiering the brief flags as an open want: **"cheaper and worse" doesn't have to mean strictly fewer stat points — it can mean the same stat block plus a flat price cut plus a small chance of an extra complication each activation**, which reads as authentically "budget-built" at the table in a way a pure stat-line discount doesn't. The honest cost: it's one more per-activation die roll, which is exactly the kind of table-friction Settlements' anti-bloat tenet watches for — worth it only if the "feels janky" payoff is worth a die roll per Clunky unit per turn.

---
## The Robot Controller — a Leader that converts a whole force into a single-faction robot swarm

**Type:** Faction · **Take:** ⚙️ adapt

A Robot faction requires a specific Leader card: *"To create a Robot faction, the Leader must be the Robot Controller (which cannot be a Dog, Creature, Robot, or Synth). Apart from the Leader, the force may only contain Robots."* **[FACT — automatron capture p.1]** In exchange, the Leader gets two abilities baked directly into their card for free — *"The Robot Controller Leader card itself gives nearby robots two abilities automatically: Hold and Observer"* **[FACT — automatron capture p.1]** — plus access to a dedicated pool of Robot Perks that only this Leader can equip, and which stop working the instant the Leader is removed: *"When a model with the Robot Controller Leader card is removed from the battlefield, their Robot Perks have no further effect."* **[FACT — automatron capture p.1]**

**Why it works.** Faction identity here is a single gate (must have this specific Leader) plus a dependency (the whole force's bonuses die with that one model) — cheap to state, and it creates a genuine tactical target: killing the Robot Controller doesn't just remove a body, it switches off the whole force's upgrade layer at once.

**For Settlements.** A clean, minimal shape for a hypothetical drone-operator archetype: gate an all-drone/robot list behind one specific Leader/Specialist choice, give that Leader's card two free abilities that only apply to nearby robots, and make every equipped Perk/upgrade die with the Leader. Touches [[Factions]] and [[Deployables]]. The honest objection: a single point of total-force failure is a strong tactical hook but also a strong incentive for the *opponent* to snipe one specific model turn one, which needs a deliberate call (is that the intended pressure, or an unintended "kill this one guy and win" pattern?).

---
## Turrets — pure-reaction automated defenses, aware at double range, firing at anyone regardless of faction

**Type:** Combat · **Take:** ⚙️ adapt

Turrets never activate on their own initiative — they exist entirely as a bundle of Reactions. *"Turrets have multiple Reaction Markers. Turrets start each round with the total number of Reaction Markers shown on their weapon card, regardless of any remaining from the previous round."* **[FACT — rules-of-play capture p.52]** Their alertness is doubled versus a normal model: *"Turrets are aware of all Triggers at a range of two Awareness lengths"* **[FACT — rules-of-play capture p.52]**, and they are deliberately indiscriminate: *"Turrets react to every Trigger they are aware of regardless of faction"* **[FACT — rules-of-play capture p.52]**, with almost any unused Action counting as a Trigger — *"All Actions (including Prepare) are Triggers for turrets. Plus, any Action (not Quick Action) that a model does not use is a Trigger."* **[FACT — rules-of-play capture p.52]** Turrets are explicitly not units for objective purposes and cannot be moved by any means once placed. **[FACT — rules-of-play capture p.52]**

**Why it works.** A turret needing no activation logic of its own, and reacting to *any* Trigger from *any* faction, means it can't be tricked by faction-specific stealth or timing tech the way a normal AI-controlled model might — it's a pure environmental hazard, which is the correct shape for "a fixed gun emplacement," and costs nothing beyond a Reaction-Marker count and an awareness-range doubling.

**For Settlements.** Directly comparable to whatever [[Deployables]]'s existing turret-hijack rule does — the hub already notes Infinity's Hackable-by-Troop-Type rule uses "the same shape our own [[Deployables\|turret-hijack]] rule already uses." Fallout's version adds one detail worth weighing: a turret that reacts to **any** faction's Triggers (including its owner's, implicitly, since it isn't faction-filtered) is a genuinely different design than a turret that only ever fires at declared enemies — worth an explicit check on whether Settlements' turrets are meant to be faction-blind hazards or faction-aware defenses.

---
## Power Armor's two-stage degrade — a second damage pool for one piece of gear

**Type:** Combat · **Take:** ⚠️ avoid (instructive contrast)

Power Armor carries its own separate damage track before the wearer takes any hits at all: *"When damage is applied to a model wearing undamaged Power Armor, Damage Tokens are placed beside the Power Armor card until the total Damage Tokens equal the armor's End bonus."* **[FACT — rules-of-play capture p.46]** Filling that pool doesn't destroy the armor — it **degrades** it to a weaker-but-still-functional state: *"Even when degraded, Power Armor continues to give benefits such as increased strength, negating falling damage, and other effects as shown on its card"* **[FACT — rules-of-play capture p.46]**, tracked physically by rotating the card 180° to its alternate printed side. Only one armor roll is ever made per hit regardless of how many layers are worn — *"A model wearing Power Armor only gets one armor roll when hit, regardless of any armor worn beneath it."* **[FACT — rules-of-play capture p.46]**

**Why it works.** A two-stage "tough, then merely durable" curve for one specific item is expressive — Power Armor visibly gets worse but never just falls off — at the cost of a dedicated damage-token pool tracked separately from the model's own Health, for exactly one equipment category.

**For Settlements.** A useful **contrast**, not a candidate: Settlements has already cut HP-based structure damage as a deliberate anti-bloat call (`AGENTS.md`), and this is the same shape of subsystem — a second, per-item hit-point pool with its own degrade state — applied to personal equipment instead of buildings. If Power Armor-style gear ever gets proposed for Settlements' near-future tech tier (exosuits are explicitly in scope per the 2051 setting), this is the concrete "what we already said no to" reference to hold it against: the mechanism is the same one Settlements rejected for structures, just relocated to a backpack.

---
## Land — a purchasable slot-cap that also funds a scenario-specific war-chest

**Type:** Settlement · **Take:** ⚙️ adapt

Buying **Land** does two things at once, and costs either money or a narrative milestone: *"500 OR Complete 5 Quests"* **[FACT — homestead capture p.8]**. First, it raises a hard ceiling on total Structures owned — *"Increase number of structures in Settlement. Start with 15, and each new Land allows 10 more. Does not count as a structure."* **[FACT — homestead capture p.8]** — the same shape as [[Last Days Zombie Apocalypse#Empty Spaces is the real constraint]]'s slot cap. Second, in the Homestead-specific physical-layout variant, it widens the buildable footprint on a fixed grid: *"the first purchase of new Land will allow the player to build within an area 24x24, the second purchase will increase that to 30x30, the third purchase will make it 36x36."* **[FACT — homestead capture p.9]** Third — and this is the part that complicates a clean "growth widens the menu, never the budget" reading — Land count directly scales the Caps budget of both sides in a **Settlement Attack Scenario**: at Attack Rating 1–4 the defender fields `200 + 150 per Land` and the attacker `200 + 200 per Land`, rising to `200 + 250` / `300 + 300` per Land at Attack Rating 9+. **[FACT — homestead capture p.17, full table]**

**Why it works.** Buying Land is one purchase that answers three questions at once (how many Structures can I own, how much physical space do I have, how big are the battles fought *over* this specific settlement) without three separate currencies — a genuinely Malifaux-style "one number, several jobs" economy.

**For Settlements.** This is a real, three-way answer to the [[Oathmark#The kingdom widens the menu]] vs [[Last Days Zombie Apocalypse#The Refuge costs zero]] fork, not a clean vote for either side: for **ordinary settlement growth**, Land behaves like Last Days' Empty Spaces (a slot cap, not a budget). For the **one scenario type that puts the settlement itself on the table**, Land explicitly *does* raise the fielded budget, scaled to how much territory there is to defend. What it does for an **ordinary away battle** — whether a bigger settlement lets you field more Credits/Crew Rating on a normal mission elsewhere — is **[NOT FOUND]**: that mechanic lives in the uncaptured Campaign Handbook, which Homestead explicitly assumes as a prerequisite (*"To use Homestead, a player must be using the Settlement rules included in the Campaign Handbook"* **[FACT — homestead capture p.3]**). Don't read this note as having answered the ordinary-battle half of the question — it hasn't, and that's a real, stated gap rather than a guess.

---
## Settlement Attacks — a computed Defense Rating, and whether the defender even sees it coming

**Type:** Detection · **Take:** ⚙️ adapt

A Settlement's Defense Rating is a small additive formula starting from a base of 3: *"add 1 [per Guard Post barricade side], add 2 [for 2-3 sides]... add 1 for every Watch Tower with power... For Machine Gun Turrets: add an amount equal to its Mk... Deduct 1 for every 4 Structures in the Settlement."* **[FACT — homestead capture p.16]** Structural Damage from an attack equals the amount the Attack Rating exceeds this Defense Rating, floored at zero. **[FACT — homestead capture p.16]** Before any of that resolves, though, the defender may not even know the attack is coming: *"If the defender has no Watch Towers, they are unaware. If the defender has any Watch Towers, roll [dice]. If the result is equal to or less than the number of Watch Towers with power in the Settlement, the defender has noticed the impending attack so is aware, unless a [critical] is rolled, which always means the defender is unaware."* **[FACT — homestead capture p.17]** Being aware matters mechanically, not just narratively — an aware defender can pre-allocate up to half their item pool to their models before the fight; an unaware one draws blind. **[FACT — homestead capture p.17]**

**Why it works.** Owning more Watch Towers doesn't just add flat Defense Rating points, it also improves the odds you get to prepare at all — one Structure type answers both "how hard is my base to break" and "do I even get advance warning," with a single die roll gating the second.

**For Settlements.** Touches [[Territory]] and whatever alert-state system [[Ideas Inbox]]'s stealth/noise want eventually produces at the settlement scale specifically (as opposed to the in-battle scale [[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll]] already covers well). The honest cost: this specific formula (base 3, +1/+2 per barricade side, −1 per 4 Structures) is entirely bespoke to Fallout's Structure catalogue and not directly transferable — the transferable *idea* is "a named defensive Structure category doubles as your surprise-roll gate," not the arithmetic.

---
## Two currencies for one settlement — Caps buys, Resources maintains

**Type:** Economy · **Take:** ⚠️ avoid (instructive contrast)

Homestead layers a second currency on top of the base game's Caps: *"Homestead introduces a new currency to Settlement Mode called 'Resources'. Resources represent critical components used for building and maintaining the settlement... required to repair damage to structures, reinforce structures, extend structures, and other tasks."* **[FACT — homestead capture p.3]** The split is strict — Caps buys new Structures and Land outright (the price tables throughout the book are denominated in Caps), while Resources is spent only on upkeep-shaped actions (repair, reinforce, extend a Structure's footprint, move a Small Structure). Resources is also the more fragile currency: *"Unlike Caps, Resources can only be kept between each Settlement Use if there is appropriate storage for them in a new type of Structure called Resource Sheds."* **[FACT — homestead capture p.3]**

**Why it works.** Splitting "acquire" from "maintain" onto two currencies means a player who wants to sit on a huge, static settlement doesn't need to keep earning the maintenance currency — but a player who wants to actively upgrade and repair does, which is a real design lever for pacing expansion versus upkeep.

**For Settlements.** A direct, useful **contrast** rather than a candidate: Settlements has explicitly cut Water upkeep and per-head upkeep as separate resource tracks (`AGENTS.md`'s anti-bloat ledger), and this is the same shape of problem (a second currency that exists mainly to gate maintenance actions) shipped by a game that made the opposite call from Settlements. Worth citing specifically when the "should upkeep be a second currency" question resurfaces: Fallout's version works fine at the table, but it is genuinely more bookkeeping (two running totals, one of which needs its own storage-capacity Structure just to persist) than Settlements' single-Credits answer.

---
## Survival Mode's own admitted snowball warning

**Type:** Campaign · **Take:** ⚠️ instructive failure

Homestead's persistent-roster mode gates recruitment behind the settlement's own economy — a new model must be *"'hired' which requires paying that Unit's Caps cost paid out of the Settlement's total Caps"* **[FACT — homestead capture p.29]** — and models damaged or lost carry consequences forward, unlike normal one-off battles. The book states its own risk in a sidebar, in full caps for emphasis: *"SURVIVAL MODE MAKES FALLOUT: WASTELAND WARFARE MUCH MORE DIFFICULT. ALSO, IF PLAYING VERSUS THE SAME OPPONENT MULTIPLE TIMES, IT CAN CAUSE AN INCREASING GAP BETWEEN WINNER AND LOSER. PLAYERS WHO WANT GAMES WITHOUT THE PERMANENT CONSEQUENCES SHOULD NOT USE SURVIVAL MODE."* **[FACT — homestead capture p.29]**

**Why it's here.** A designer-stated, printed admission that a permanent-roster campaign mode widens the gap between winner and loser over repeated play, shipped as an explicit **opt-out** rather than a fix, is worth more than an unexamined success — it's a direct, named acknowledgment of the exact snowball risk every persistent-crew campaign system has to answer somehow.

**For Settlements.** Touches [[Campaign]] and [[Progression]]. Compare against [[Necromunda and Mordheim#Play frequency beats skill]] (a *measured*, simulation-derived snowball source) and the veteran price-vs-cap fork already tracked via [[Trench Crusade#Cap the veterans, don't tax them]] and [[Spectre Operations#Veteran Pricing as a Flat Surcharge, Never a Cap]] — Fallout doesn't offer a price-or-cap mechanism at all here, it offers **an explicit off-switch**: if you don't want the snowball, don't opt into the mode that causes it. That's a legitimate fourth answer to add to the fork (price it / cap it / don't build it as persistent at all) worth having on record, even though it's closer to a disclaimer than a design.

---
## Natural Behavior — a swappable AI-override card entered and exited by named Triggers

**Type:** Solo · **Take:** ⭐ steal

Every AI-controlled model (wildlife, hostile factions, robots) normally uses a fixed **AI card** — a matrix read left-to-right by Situation, executing whichever Response (Attack/Move/Objective/Fall Back/Defend) matches the first true column. **Natural Behavior** temporarily replaces that card wholesale: *"A Natural Behavior is a special AI matrix which simply overrides an Inhabitant's usual AI matrix. When an Inhabitant notices something that is relevant to their Natural Behavior, they 'Exit' their Natural Behavior temporarily and use their usual AI matrix with a specific objective. When the incident is over or resolved, the Inhabitant 'Resumes' their Natural Behavior AI matrix again."* **[FACT — into-the-wasteland capture pp.9–10]** Behaviors (Grazing, Hunting, Traveling, Fleeing, and more) each ship as a physical card pair — an active-side summary card and its "Was [Behavior]" reverse side — so a glance at the token tells you both its current state and what will make it change. **[FACT — into-the-wasteland capture p.9]** The system adds exactly one new Response to the base four (Strike, a limited Attack-only-if-it-connects variant) rather than inventing a parallel rule set, and states its own edge-case fallback plainly: *"If the Natural Behavior AI card shows the Ranged Method but the model does not have a Ranged weapon, use the Close Combat Method instead."* **[FACT — into-the-wasteland capture p.10]** A worked example shows the state machine's texture: a Traveling model that Resumes its route mid-scenario ignores routine Activity Triggers for the rest of that turn but will still Exit for a Hostility Trigger, so "just got shot at" always overrides "was quietly walking a patrol route" even the instant it resumes. **[FACT — into-the-wasteland capture p.10]**

**Why it works.** Nothing here is a parallel AI system — it's the *existing* AI-card machinery (already needed for every enemy/creature in the game) plus one swap-in/swap-out layer with named Enter/Exit triggers per behavior. The same trick [[Spectre Operations#The Solo/NPC Rules — the detection system's own tables become the bot]] uses (reuse an existing state machine as the bot) appears here independently, but built the opposite way round: Spectre repurposes its *stealth* states as the AI; Fallout repurposes its *AI* system as a stealth/ambience layer, by giving "hasn't noticed you yet" its own overridable card.

**For Settlements.** Directly relevant to [[Solo & Co-op]] and to whatever wilderness/neutral-threat system [[Scenarios]] uses — a genuinely different, third shape next to [[Rangers of Shadow Deep#Scale the players, not the enemies]] (scale the human side, don't touch enemy AI) and [[Spectre Operations#The Solo/NPC Rules — the detection system's own tables become the bot]] (one state machine serves two jobs). Fallout's contribution is the **Enter/Exit/Resume vocabulary as a reusable pattern**: any creature or robot whose "normal" behavior should visibly pause and resume around combat (a robot on patrol, an animal that flees and comes back) gets that for free once you have (a) a base AI matrix and (b) one small override card with a stated re-entry rule — no new dice, no new currency, just a second card per behavior type. The honest cost: it is more physical bookkeeping (a Natural Behavior card *and* a summary card *and* the model's usual AI card, tracked per model) than a single unified table, which matters if Settlements wants this at scale across many neutral/wildlife threats at once.

---
## What it gets wrong

**The dice engine is the single biggest transfer barrier in this whole capture.** Every mechanic above had to be checked for whether its value survives being lifted out of the d20-roll-under-plus-stacked-d12-Effect-Dice system, and several (the Skill Test mechanics themselves, obviously) simply don't — logged as 📎 reference for exactly that reason rather than pretending they're adoptable with a coat of paint.

**This capture cannot answer the base Settlement/Crew-budget question, and says so rather than guessing.** Homestead is explicitly an expansion that assumes the Campaign Handbook's baseline Settlement rules (`"To use Homestead, a player must be using the Settlement rules included in the Campaign Handbook"` — homestead capture p.3), which is not among the five files captured this run. Everything above about Land, Structures, Caps, and Resources is accurate for what Homestead *adds*, but whether an ordinary away-mission Crew Rating scales with settlement size at all is a genuine, uncaptured **[NOT FOUND]** — not a "probably not" inferred from silence.

**One of five files has unresolved provenance.** The Robots faction list (`robots.pdf` / `BMCE-Robots-v-1-0.pdf`) carries neither the official Modiphius product-code convention (`FOWW <code>-111`) nor the Bethesda/ZeniMax trademark footer present on every other file in this capture, including the differently-named official Battle Mode Rulebook. A web search this run confirmed the general Battle Mode program is official and actively supported (a Second Edition is in development for 2026 — Fallout: Wasteland Warfare is **not** a discontinued line, correcting an assumption made mid-research) but did not resolve what "BMCE" stands for or whether these specific per-faction PDFs are official shorthand or a fan companion. Its price figures (the Battered-tier discounts cited above) are logged as reference data, not FACT-graded rulebook content, until that's resolved.

---
## Evidence & confidence

- **[FACT]** tags above are quoted or closely paraphrased directly from the four confirmed-official PDFs (product codes `FOWW 2PB-002-111`, `FOWW ITW-001-111`, `FOWW APR-001-111`, and the Homestead Rules Expansion v2, all verified against the Bethesda/ZeniMax trademark footer and/or a byte-identical or content-identical match against the library master in `G:\My Drive\Wargaming\Fallout\`). Page numbers cite the `=== PAGE N ===` markers (0-indexed) in this note's own capture files under `research/sources/fallout-wasteland-warfare/`, not necessarily the book's printed footer number.
- The Robots faction-list price figures (Battered-tier discounts) are **not** FACT-tagged — see **What it gets wrong** for why, and treat them as reference-only pending confirmation of the document's provenance.
- **[NOT FOUND]** is used twice, deliberately: once for whether ordinary away-battle Crew budgets scale with Land/settlement size (the answer lives in the uncaptured Campaign Handbook), and once for the "BMCE" acronym's meaning.
- **[INFERENCE]** was not needed for any load-bearing claim in this note — every mechanic above traces to a directly quoted rule.
- No **[CONSENSUS]** tags appear — nothing here comes from community discussion rather than the primary documents.

---
## Source

- Primary: *Fallout: Wasteland Warfare — Rules of Play* (60pp, product code FOWW 2PB-002-111), *Into the Wasteland* (24pp, FOWW ITW-001-111), *Homestead — Rules Expansion v2* (34pp), and *Automatron Player Rules v1.0* (2pp, FOWW APR-001-111), all Modiphius Entertainment. Plus *Robots (Battle Mode Faction List)* (11pp, provenance unconfirmed — see above).
- Capture: `research/sources/fallout-wasteland-warfare/rules-of-play.md`, `into-the-wasteland.md`, `homestead.md`, `robots.md`, `automatron.md` (all verbatim text extractions with page markers), plus `meta.json` (hashes, library paths, and the provenance/gap notes referenced throughout this note).
- Library: all five source PDFs are filed in `G:\My Drive\Wargaming\Fallout\`, which holds 1,211 files recursively — this capture covers 5. Not captured this run despite being directly relevant: the **Campaign Handbook** (defines the base Settlement/Caps loop and the full AI Response system this note's Natural Behavior and Land sections both depend on), the **Battle Mode Rulebook** (FOWW BTL-001-111 — explicitly disables Settlement Mode and Solo/Co-op, confirmed not where any of the above material lives), 13 further Battle-Mode-style faction Force Lists, and **Into The Vault** (a separate terminal/vault-crawl-themed expansion whose name overlaps with but is distinct from Into the Wasteland — a plausible next-highest-value hacking capture).
- Related: [[Wargaming Research Hub]] · [[Oathmark]] and [[Last Days Zombie Apocalypse]] (settlement-growth-vs-budget fork — see **Land**, above) · [[Zona Alfa]] (scavenging comparison) · [[Spectre Operations]] (Detection and Solo/NPC comparison) · [[Rangers of Shadow Deep]] (solo/co-op comparison) · [[Infinity]] (hacking-depth comparison) · [[Trench Crusade]] and [[Necromunda and Mordheim]] (campaign-snowball comparison) · [[Games Workshop published formulas]] (atomic-costing failure mode comparison for the Automatron)

---
*Add one row per mechanic to [[Wargaming Research Hub]] when this note is finished.*

---
type: research-note
title: Zona Alfa
game: Zona Alfa — Salvage and Survival in the Exclusion Zone
designer: Patrick Todoroff
publisher: Osprey Games
depth: primary — full 65-page rulebook read in full
retrieved: 2026-08-20
source_url:
capture: research/sources/zona-alfa/
tags: [settlements/research]
---
# 🎲 Zona Alfa

> [!abstract] In one breath
> A **STALKER/Chernobyl-inspired post-apocalyptic skirmish**: a 4–12 model crew runs "Zone Runs" into an irradiated exclusion zone for **Salvage**, dodging or fighting AI-controlled **Zone Hostiles** that spawn out of the terrain itself when you trigger a Mission Objective or a Hot Spot. Closest thematic match yet captured to Settlements' setting, and the best published example of a **neutral, territory-driven threat system** in the corpus — but it has **zero settlement or base-building layer**, and despite the STALKER pedigree, **no stealth or noise mechanic at all**.

| | |
|---|---|
| **Designer · publisher** | Patrick Todoroff · Osprey Games (2020) |
| **Scale / format** | 3′×3′ to 4′×6′ board, 4–12 models a side, 28mm (works at 15mm too), objective + Hot Spot driven |
| **Core resolution** | `XD10 vs a Stat`, roll **at or under** the (modified) target — low roll wins. Unmodified natural 1 = **Critical Success** (free bonus Action); unmodified natural 10 = **Critical Failure** (Pinned) |
| **Depth of read** | **Primary** — full 65-page rulebook, first run of the repo's new capture pipeline |
| **Raw capture** | `research/sources/zona-alfa/` in the Settlements repo |
| **Source** | Osprey Games, 2020. ISBN 9781472835697 (PB) |

---
## Why it's here

It is the genre match we didn't have yet: near-future irradiated exclusion zone, scavenger crews, mutants, anomalies, a black-market economy — closer to Settlements' 2051 setting than anything else captured so far, and it closes the "Fallout: Wasteland Warfare · This Is Not a Test · S.T.A.L.K.E.R.-likes" line on the hub's to-read list. It also directly answers three of our live open questions: **threat spawning** (its best mechanic, by a wide margin), **anomalies as interactive terrain**, and **scavenging that pays out via a shared, race-to-clear-it board** rather than a private draw.

Two honest caveats before the rest of this note. First, **Zona Alfa has no settlement, base, or territory layer whatsoever** — advancement is entirely crew-and-gear, tracked on a roster sheet; nothing here informs [[Settlement]] or [[Territory]] directly. Second, and surprisingly given the STALKER pedigree: **there is no stealth or noise mechanic anywhere in the book.** See the dedicated section below — this is a real, checked negative result, not an oversight in the read.

---
## Core resolution — an inverted D10, and a Critical that pays out immediately

**Type:** Dice · **Take:** 📎 reference (⚙️ adapt for the bonus-Action crit)

Roll the weapon's **Firepower** in D10s (or a single D10 for a Skill Check) against the relevant **Model Stat** (Combat Ability, Armor, Will) or **Weapon Stat**. *"A result of the base Target Number or less (+/- modifiers) is a Success. So, a high roll = bad. A low roll = good."* **[FACT — p.6]**

Crits are computed **once per round, not once per die**: *"A Critical Success is an unmodified D10 roll of 1: Regardless of the task's difficulty or modifiers, a roll of 1 means the Action/task attempted was automatically successful and the model gains a free, extra Action. This extra Action must be taken at the end of the model's current activation and does not roll over into the next turn."* A natural 10 is the mirror — automatic failure plus an immediate **Pinned** counter, regardless of modifiers. **[FACT — p.6]** If a pool contains both a 1 and a 10 ("Critical Mix"), they cancel and the roll resolves normally.

**Why it works.** However many dice you throw, you only ever get one bonus/penalty resolution per round — a big dice pool can't be farmed for extra free Actions. And the reward for a crit is wired directly into the same activation instead of a side-table roll.

**For Settlements.** Our core engine is a locked mirror-image of this (`1d10 + Stat + Modifiers vs 7+`, high roll good, natural 1 always fails, natural 10 always succeeds) — so there's nothing to change here, only to note the resemblance. The one transferable idea, if our own crit payout is still open for debate, is **a free bonus Action tacked onto the same activation** rather than a separate crit table: cheap, immediate, and it never compounds across a multi-die pool. [[Rules Engine]].

---
## Initiative and Alternating Activation

**Type:** Activation · **Take:** ⚙️ adapt

*"At the start of every turn, players will each roll a D10 to determine that turn's Initiative. This Initiative die roll result is modified (penalized) by the number of that player's currently Pinned Units."* **[FACT — p.11]** High roll (after the Pinned penalty) activates first, and units then alternate one at a time until both sides are exhausted. *"The winner of the Initiative Roll may also pass that option to their opponent, if they deem it tactically advantageous."* **[FACT — p.11]**

**Why it works.** Being suppressed compounds on itself for free — a crew that's taken a lot of Pins loses both Actions *and* tempo off the same counter, with no extra bookkeeping. The pass-the-choice option is a second, near-free lever: sometimes you'd rather see what the other side does first.

There's also a genuine opponent's-turn reaction, priced honestly: *"At the cost of two Actions, a unit may hold One Action in reserve to interrupt an opponent's Activation. This interruption can be any Action. For example, Move, Shoot, Aim, even Prep and Throw a Grenade etc."* **[FACT — p.12, the Alert Action]** Paying 2-for-1 to hold a single reactive Action is a steep but simple tax — a Veteran can Alert and still act; a Rookie effectively can't (it would burn its entire activation).

**For Settlements.** [[Initiative & Activation]]. The "pass the win to your opponent" option costs one sentence and hands a small tactical choice to whoever's ahead on the roll-off, without touching the roll-off mechanic itself. **Alert** is a minimal, single-rule reaction economy — 2 Actions banks 1 reactive Action of any kind — worth comparing against our own [[Initiative & Activation]] reaction rules for how cheaply an interrupt option can be priced.

---
## Combat Experience — one tier gates Actions, Skills, and Equipment Slots together

**Type:** Activation · **Take:** 📎 reference

Three tiers — **Rookie** (1 Action, 0 Skills, 1 Equipment Slot), **Hardened** (2 Actions, 1 Skill, 2 Slots), **Veteran** (3 Actions, 2 Skills, 3 Slots) — and every crew member sits on exactly one of them. **[FACT — p.11, 30–31]** Promotion (five missions survived) bumps a model up one tier automatically, *unless* that stat line has already been hand-improved by spent Advances, in which case the automatic bump is skipped for that stat. **[FACT — p.49]**

**Why it works.** One published rank answers three separate design questions — turn economy, character build depth, and loadout capacity — off a single number instead of three independently-tuned tracks.

**For Settlements.** [[Initiative & Activation]], [[List Building]]. This is the same shape as our own locked Rank ladder (Recruit/Fighter/Specialist/Leader → Orders 0/0/1/2, with tier caps on skills at creation) — a different designer converging on "one rank, several payoffs" independently. **[INFERENCE — convergent design, not a stated cross-reference in the book.]** Nothing to change; useful as citable precedent if that structure is ever questioned.

---
## Khrabrost' — a force-build currency made of Actions, not Credits

**Type:** List · **Take:** 📎 reference

*"A Zone Crew's Khrabrost' (K) is equal to the total available Actions among its members."* **[FACT — p.35]** A starting crew has 12 K; the Leader (always a Veteran) takes 3, leaving 9 to spend on recruits at **Veteran 3 / Hardened 2 / Rookie 1**. Unspent K can instead raise a single member's Movement, Combat Ability, or Will by 1. For pickup games, **Force Parity** is just "both players agree a K value (say 10, 12, or 16) and build under it" — no separate points list is consulted. **[FACT — p.39]**

**Why it works.** The list-building budget *is* the thing being budgeted — turn economy — with no abstraction layer standing between them. Leftover-K-into-a-stat-bump is structurally the same idea as Malifaux's leftover Soulstones becoming a capped in-game resource.

**For Settlements.** [[List Building]]. We deliberately keep **Credits** as the single face currency — the Credits you field *are* your Crew Rating — and this is proof a skirmish game can run with *no* monetary abstraction at all. It's a road we've already chosen not to take, for a good reason gear pricing gives us here: see **What it gets wrong**, below, for the cost. Compare [[Malifaux#Leftover budget becomes a capped resource]].

---
## Movement, field of view, and layered Cover

**Type:** Movement (see also Terrain, below) · **Take:** ⚙️ adapt

Every model gets a 360° field of view regardless of facing; a Move is measured **base-front to base-rear**, which the book notes flatly *"adds the base width to the Move Action but it really cuts down on arguments."* **[FACT — p.15]** Climbing anything over 1″ tall costs double distance (no ladder needed, at half rate); a horizontal Jump up to 2″ is a free part of a Move Action, beyond that it needs a Move plus a Will-based Skill Check.

Cover comes in four stacking tiers, and each tier taxes a **different combination of stats** at once:

| Cover | Attacker's Combat Ability | Defender's Armor | Defender's Will |
|---|:--:|:--:|:--:|
| Obstruction | −1 | — | — |
| Soft | −1 | — | +1 |
| Hard | −1 | +1 | +2 |
| Hardened | −2 | +2 | +3 |

**[FACT — p.15–16]** — and they're cumulative with each other. Then, one sentence undoes a tier of it: *"any Ranged or Melee attack made from a higher elevation against a target in Cover reduces the Defender's Cover level by one degree. This means Hard cover shifts to Soft, Soft cover shifts to Obstruction, and Obstruction modifiers are cancelled entirely when the Attacker is at a higher elevation than the Defender."* **[FACT — p.16]**

**Why it works.** Cover isn't one number to remember, it's three separate small numbers layered onto three separate rolls (to-hit, Armor Save, Pin check) — which lets Hard cover mean "harder to hit AND harder to hurt AND harder to rattle" without a single bespoke modifier. And the elevation rule gives high ground a second, purely mechanical reason to matter, on top of whatever it already does for LOS.

**For Settlements.** [[Movement]], [[Terrain]]. **The elevation-demotes-cover-a-tier rule is the standout steal candidate in this whole note** — it's one sentence, it reuses cover tiers we'd already have, and it directly reinforces the tenet that terrain density is our single strongest balance dial. Worth checking against [[Terrain Interaction]] before adopting, since it touches whatever elevation rules already exist there.

---
## Ranged Combat — the Armor Save decouples the hit from the wound

**Type:** Combat · **Take:** 📎 reference (independent convergent validation)

A Successful Hit still isn't automatically a wound: the Defender rolls an **Armor Save** (Armor − Weapon Damage, plus/minus Cover). Pass the save and it's a **Deflected Hit** — no wound, but it forces a Will check, and failing *that* leaves a Pinned counter. Fail the save and it's a **Successful Hit** — a Wound or a casualty. The book states the whole loop in three lines: *"Ranged Attack Successful Hit = Wound or Casualty… Ranged Attack Deflected Hit = Possible Pinned Counter… Miss = Miss."* **[FACT — p.24]**

**Why it works.** Every hit resolves into *something* — a wound, or a forced nerve check — and a Miss is the only truly free outcome. That is functionally identical to the tenet Settlements already has locked (a hit wounds *or* delivers Stress, never neither, never both) — reached independently, by a different designer, for a different genre.

**For Settlements.** [[Shooting]], [[Damage]], [[Morale]]. Nothing to change — this is validating precedent for an already-locked rule, worth citing the next time "does every hit need to do something" comes up again. **[INFERENCE — the "independently reached" framing is our read, not a stated cross-reference by Todoroff.]**

---
## Melee — simultaneous rolls, and paying Hits to Parry

**Type:** Combat · **Take:** ⚙️ adapt

Melee is not attacker-then-defender: *"In this simultaneous brawl, both the Attacker and Defender will roll the appropriate Firepower and Armor Save rolls at the same time for every round of Melee."* **[FACT — p.18]** After both sides roll, *"the Attacker then has the option to use any of their Successful Hits to Parry (i.e. cancel) an equal number of the Defender's Successful hits. Any remaining Hits are subject to Armor Saves and resolved as normal."* **[FACT — p.18]** A tied or inconclusive round is **Deadlocked** and rolls over into next turn; withdrawing from a Deadlock costs the withdrawer one free hit from the opponent first.

**Why it works.** Winning the exchange and taking damage happen on the same roll, so nobody is left waiting to see if the other player's attack even lands before their own matters. Naming the tied state (Deadlocked) turns an ambiguous non-result into an actual game state with its own exit rule.

**For Settlements.** [[Melee]]. Worth weighing against whatever our own melee sequencing currently is — simultaneous-with-Parry is a genuinely different table feel (both sides commit before either learns the result) and shouldn't be adopted just because it's tidy; it needs to earn its place against our activation-based turn structure specifically.

---
## Mission Objectives and Hot Spots — the Reaction Radius, and triggering a fight from range

**Type:** Scenario · **Take:** ⭐ steal

Every mission has one **Mission Objective** plus a number of secondary **Hot Spots** equal to `Threat Level × 2`, spread evenly so *"both sides equal accessibility."* **[FACT — p.40]** Both are area triggers, not switches: *"Anytime a player's models pass through or end their movement within 3″ of the Mission Objective or Hot Spot, the player has triggered the location. This 3″ distance, or 6″ diameter centered on the item, is known as the location's Reaction Radius."* **[FACT — p.40–41]** Triggering it means rolling on the Zone Hostiles Table (below) — engaging loot always means fighting something first.

You don't have to walk up to trigger one, either: *"Players can have one of their models Toss a Bolt into the location's 3″ Reaction Radius to make the Zone Hostiles spawn… Bolt Toss allows players to trigger the location remotely, either with a nearby comrade on Alert, or when a rival crew is in proximity."* **[FACT — p.41]**

**Why it works.** A neutral objective that's dangerous *by construction* (you cannot search it before clearing it) does double duty as both the scoring target and the board's built-in tension generator, with zero extra bookkeeping. Bolt Toss turns that same trigger into a weapon — bait a Hostile swarm onto an enemy crew standing near an untriggered Hot Spot, at the cost of one Action and a thrown die.

**For Settlements.** [[Scenarios]]. This is the strongest published example of "a board that feels alive" found so far — closer to what we want than [[The Walking Dead All Out War#The neutral threat]]'s points-matched Walkers, because the threat here is *tied to the terrain itself* rather than a pre-agreed shared pool, and a player can weaponize it against the opponent rather than just deploying it. Directly informs any noise/detection design too, since Bolt Toss is effectively "make noise on purpose" without the game ever naming noise as a mechanic.

---
## Zone Hostiles — Threat Level spawn scaling, and a four-rule AI

**Type:** Scenario · **Take:** ⭐ steal

| D6 | Threat 1 (Blue) | Threat 2 (Yellow) | Threat 3 (Red) |
|:--:|---|---|---|
| 1 | Vermin Swarm (1) | Vermin Swarm (×2) | Feral Dogs (6) |
| 2 | Vermin Swarm (2) | Feral Dogs (6) | Zombies (8) |
| 3 | Feral Dogs (4) | Zombies (6) | Rad Ghouls (6) |
| 4 | Zombies (4) | Rad Ghouls (6) | Bandits (4)* |
| 5 | Rad Ghoul (4) | Bandits (4)* | Mutants (2)* |
| 6 | Bandits (4)* | Mutant (1)* | Large Mutant (1)* |

**[FACT — p.41]** (`*` = an Anomaly is also present — see Salvage and Anomalies, below.) Every archetype has one stat line — Move / Combat Ability / Armor / Will / Weapon — deliberately generic so *"if you don't have feral dogs for instance, use spiders… scale their abilities to fit the threat they represent."* **[FACT — p.44]**

Zone Hostiles are AI-controlled by the *opposing* player, under four printed rules: they never range further than 12″ from their spawn point; they're aggressive and use Cover; *"they always attack the closest, visible model — enemies in the open take priority over those in cover"*, continuing on that target until it or they die; and only a Melee attack can pull their attention off their current target. **[FACT — p.43]** Their Action count scales with the area's Threat Level (1/2/3), same as a player crew's Combat Experience tier.

**Why it works.** Seven stat lines cover an unlimited bestiary because every entry is deliberately a reskin target, not a fixed miniature range — and four short rules produce legible, predictable monster behaviour without a full AI subsystem. Both crews can be attacked by the same Hostile group, which makes the spawn a genuine neutral hazard rather than a PvE side-fight.

**For Settlements.** [[Scenarios]]. This is the clearest, most complete published threat-spawn system captured yet — directly answers the "boards that feel alive" want. The **12″ leash + nearest-visible-target** pair is cheap enough to lift close to verbatim for any neutral-hostile mechanic Settlements adds.

---
## Salvage and Anomalies — loot and hazard sharing one system

**Type:** Scenario (Anomalies also touch Terrain) · **Take:** ⭐ steal

A Hot Spot can only be searched **after** its Hostiles are cleared, and **only once** — *"each Hot Spot can only be Searched once"* **[FACT — p.44]** — with a named exception: the **Scrounger** skill lets one model search twice. The payout scales with Threat Level (Salvage Value 200 at TL1/roll 1, up to 2,000 + two equipment rolls at TL3/roll 6).

**Anomalies** are the same system's sharp edge: on certain Hot Spot rolls (a 6 at TL1, 5+ at TL2, 4+ at TL3) the location also contains an Anomaly, and rolling on the Salvage table happens *in addition to* an Artifact roll. **[FACT — p.45]** Searching one costs an Action *and* a Will check — *"the Target Number for this Will check is the searching model's Will stat, with a negative modifier equivalent to the mission area's Threat Level"* **[FACT — p.45]** — and failure detonates the Anomaly as an area blast (Damage 2 on everyone in the template). Artifacts are worth real money (2,000–5,500 Zone Script) and some carry a permanent stat bonus (+1 Move/Armor/Will).

One more small, honest mechanic worth logging: **Messy Resolutions.** If two crews both contribute to clearing the same location, *"you get the Kill Credits and they get the Hot Spot Salvage credit."* **[FACT — p.49]** It isn't a loser's consolation prize — whoever searches first still takes the loot — but it does mean a crew that only fights, without ever reaching the Hot Spot itself, isn't shut out of *all* the payout.

**Why it works.** Loot and hazard are the same die roll, so "go get the treasure" and "something bad might be here" never need separate tables to track. Gating the Anomaly's real prize behind a Will check keyed to Threat Level makes deep-Zone Artifacts a genuine gamble rather than a guaranteed bonus once you've won the fight.

**For Settlements.** [[Scenarios]], [[Terrain]]. Anomalies are the strongest published "interactive terrain that isn't a building" found yet — a fixed location, a real risk (Will check, scaling with area danger), and a real reward, resolved with one extra roll layered onto an existing Hot Spot rather than a new subsystem. **On "loot that pays out even to the loser":** Zona Alfa does *not* have that — Salvage is race-to-clear-it, first-to-search-wins, with only the small Kill/Salvage credit split above as a consolation. **[NOT FOUND — no loser-payout mechanic exists in the book; Messy Resolutions is the closest thing, and it's a tie-break, not a design goal.]**

---
## Stealth and noise — searched for, and it isn't here

**Type:** *(no hub row — this is a checked negative, not a mechanic)* · **Take:** —

Despite the S.T.A.L.K.E.R./STALKER-genre pedigree, **Zona Alfa has no stealth, concealment, or noise-detection mechanic.** **[NOT FOUND — confirmed by full-text search across all 65 pages for "stealth", "noise", "conceal", "detect", "hidden", "quiet", "silent"; nothing describes a sound radius, a spotting roll, or a concealment state beyond ordinary Cover.]** The nearest adjacent ideas are ordinary terrain Cover (blocks LOS/LOF, no separate detection layer) and the **Detector** item (+2 to the Will check when searching an Anomaly — nothing to do with being seen or heard).

**Why it's here anyway.** This is [[Ideas Inbox]]'s stealth/noise want with **zero research behind it**, and Zona Alfa was our best genre-match candidate to find something. It didn't have it. That's a real, useful result: it tells the next researcher this specific STALKER-flavoured game is not where the mechanic lives, and the search needs to go to games that treat sneaking as a primary verb (classic infiltration-skirmish titles, not scavenge-and-shoot ones) rather than assuming genre similarity implies mechanical similarity.

**For Settlements.** Nothing to adopt from here. The open question stays exactly as open as it was.

---
## Campaign Advances — a crew-pooled XP economy, four payout channels

**Type:** Campaign · **Take:** ⚙️ adapt

Advances are never credited to an individual model — *"all Advances are credited to your entire Crew, not the individual… everything is an even split"* **[FACT — p.48]** — and accrue from four sources: **1** per model surviving a mission, **1** per kill, **3** per Hot Spot looted, **5** for the Mission Objective. Every 10 Advances from the pool raises **any** one crew member's Movement/Combat Ability/Armor/Will by 1, adds an Equipment Slot, or (every 15) grants a new Skill — Crew Leader's call, regardless of who actually earned it. Advances can also be bought outright at 1,500 Zone Script each.

**Why it works.** Pooling XP removes the "my guy didn't get to do anything this game" complaint entirely, and lets the Leader patch the crew's actual weak point instead of whoever happened to get a kill. The cost is narrative: no character arcs from individual growth, because growth is a Crew Leader spending decision, not a model's earned story.

**For Settlements.** [[Campaign]], [[Progression]]. This is a real, opposite answer to our own **per-unit persistence and injury** fork: crew-pooled advancement trades "which specific veteran grew" for "zero bookkeeping disputes and zero benched characters." Worth naming explicitly as the alternative to whatever per-model XP path Settlements is currently leaning toward, since it's a legitimate, shipped design — not a strawman.

---
## Battle Scars — permanent injury gated by bad luck, not by poverty

**Type:** Combat · **Take:** ⭐ steal

A model left **Out of Action** and not revived by a Med-Kit before the mission ends rolls on a 6-entry table: Battle Lust (must attack in LOS unless a Will check passes), Must Salvage (same, but toward the nearest Hot Spot), −1″ Movement and no free climbing, a Will check to enter Melee, −1 to all Will checks, or **"It's just a flesh wound. No Effect."** **[FACT — p.51]** *"Word of advice: any more than two, you might want to consider retiring them and hiring a new Crew member."* **[FACT — p.51]**

**Why it works.** The gate is Med-Kit access, not gold: a model only rolls for permanent injury if nobody could reach it in time, which makes carrying spare Med-Kits a genuine risk-mitigation purchase rather than pure stat padding. The table itself is gentle by genre standards — no death, no amputation — one in six results is nothing at all, which keeps a long campaign roster survivable.

**For Settlements.** [[Campaign]], [[Damage]]. Sits in the same lineage as [[Necromunda and Mordheim#Lasting injuries]] but resolves the "how punishing should this be" question differently: gate severity by *how the model was lost* (revived vs. abandoned) rather than by a flat post-battle roll for every casualty. Directly useful for the per-unit injury fork.

---
## Factions — a relationship grid instead of a rules chapter

**Type:** Faction · **Take:** ⭐ steal (grid) · 📎 reference (the specific numbers)

Six Factions (Military, Scientists, Bandits, Independents, Cultists, Traders), each with a starting-gear signing bonus, a Stalls discount, and a cheaper-recruit clause. Their mutual standing is a single non-reciprocal grid:

| | Military | Scientists | Bandits | Independents | Cultists | Traders |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **Military** | Allied | Allied | Enemy | Neutral | Enemy | Neutral |
| **Scientists** | Allied | Allied | Neutral | Allied | Neutral | Allied |
| **Bandits** | Enemy | Enemy | Allied | Neutral | Neutral | Enemy |
| **Independents** | Neutral | Allied | Neutral | Allied | Neutral | Allied |
| **Cultists** | Enemy | Neutral | Neutral | Neutral | Allied | Allied |
| **Traders** | Neutral | Allied | Enemy | Neutral | Allied | Allied |

**[FACT — p.38]** *"Notice the attitudes among the Factions aren't necessarily reciprocal; groups have their own motivations for helping others, reasons that might not be mutual."* Breaking an Alliance to attack a friendly crew costs the attacker a Difficulty-4 Will check; overriding a mandatory Enemy engagement (to still pursue loot instead) costs a Difficulty-2 one.

**Why it works.** Six factions' worth of relationship logic collapses into one 6×6 table instead of a paragraph of prose per pairing, and asymmetric cells (Military hates Cultists; Cultists are only Neutral back) read as *characterisation* for free.

**For Settlements.** [[Factions]]. The grid format is the steal — it's the cheapest possible way to give N factions a legible web of alliances and grudges without writing N² paragraphs. The specific per-faction discounts and starting kits are much less rigorously balanced (see **What it gets wrong**) and shouldn't be copied as numbers, only as a shape.

---
## The Stalls, and the 10,000 Ruble Plan

**Type:** Economy · **Take:** ⭐ steal

The Zone's whole cash economy rests on one implicit reference price: *"The Zone's economy is set at the 'AK Standard': the fixed exchange rate for a working AK-47."* **[FACT — p.51]** Selling anything at the Stalls costs a flat **10%** cut — *"Equipment, Artifacts, and Salvage sell for listed price, less the Traders' 10% cut."* **[FACT — p.51]** — and every Faction layers its own **context-priced** discount on top: Traders get a blanket 40% off everything and 25% off Veteran recruits; Military get 20% off weapons and 25% off Rookie hires; and so on per faction.

Campaigns get an explicit, player-chosen exit: track savings on the roster sheet, and *"once your retirement fund reaches 10,000, that crew can bow out."* **[FACT — p.58]** The book offers this as one of several interchangeable end-conditions — a fixed Artifact-collection quota (12 of them), or a ticking-clock "disarm/deliver the warhead" campaign structure — rather than mandating a single one.

**Why it works.** Naming the implicit exchange rate (Bolt Action does the same with "1 Regular rifleman = 10 points") gives every other price something to be checked against without publishing a formula. And offering the players an explicit, chosen soft end-condition sidesteps the snowball problem other campaign games spend whole chapters managing — the campaign just *ends*, by design, when the players decide it has.

**For Settlements.** [[Economy]], [[Campaign]]. Cross-link [[Bolt Action#The implicit unit of account]] — same idea, published in a completely different genre. The **chosen end-condition** idea is worth weighing against [[Trench Crusade#The published threshold ladder]]'s escalating-schedule approach: one lets players stop a campaign on their own terms; the other keeps every campaign converging on the same finish line. Different problems, both legitimate.

---
## How a 65-page rulebook holds a full campaign

**Type:** Production · **Take:** ⭐ steal

Core rules, full campaign layer (Advances, Battle Scars, Factions, the Stalls), a scenario-generation table, and a 3-mission intro campaign all fit in 65 pages, including art and sidebars. The designer states the goal outright in the closing section: *"Zona Alfa was ordered around the simple thought that the rules shouldn't interfere with the game. They should support rather than suffocate. They should minimize friction and streamline gameplay, not bog players down in complex record-keeping, gimmicky or tedious combat mechanics."* **[FACT — p.63]**

Three concrete techniques do the actual work, not just the stated intent: **[INFERENCE — our synthesis of the book's structure, not a stated design list]**
- **Deliberately generic catalogues.** Weapons are ~15 broad categories (not per-model), Zone Hostiles are 7 reskinnable archetypes (not a bestiary), Armor is 7 tiers. WYSIWYG statting substitutes for an exhaustive options list.
- **One force-build number.** Khrabrost' replaces a points catalogue entirely (see above) — there's no army-list chapter to write or maintain.
- **The base economy needs no formula.** Prices are simply printed (Equipment, Weapons, Grenades tables) with resale at a flat 50%/90% split — no published derivation, and none is needed for a book this size.

**Why it works.** Every one of these is a place most skirmish games spend pages on precision (per-model costs, per-monster stat blocks, a formula for the exchange rate) that Zona Alfa deliberately declines to buy, in exchange for staying short.

**For Settlements.** [[Rulebook]], [[Components]]. Direct evidence for the anti-bloat tenet: the size isn't an accident of having fewer subsystems, it's a consequence of choosing *coarse* catalogues over precise ones in the specific places where precision doesn't pay for itself at this scale. Worth reviewing our own catalogue granularity (weapons, gear, hostile/threat stat blocks) against this same question: does this entry need its own number, or does a category cover it?

---
## What it gets wrong

**Type:** *(cross-cutting)* · **Take:** ⚠️

- **Khrabrost' is gear-blind.** K is set entirely by Combat Experience tier (1/2/3) and is completely indifferent to what the model is actually carrying — a Veteran with an RPG, NODs, and Kevlar costs exactly the same 3 K as a Veteran with a knife. **[INFERENCE — read directly from the recruitment rules, p.30–35; no gear-cost adjustment is stated anywhere.]** It's the same "everyone gets N slots" trap Kill Team's 2018 edition ran into ([[Kill Team#The three-philosophy experiment]]) — Zona Alfa just never tries to solve it, because a 12–16 K pickup game is short enough that nobody optimises that hard. It would not survive a real campaign-length gear gap.
- **Faction bonuses aren't visibly balanced against each other.** Traders get a flat, permanent 40% discount on everything plus 25% off Veteran hires; Bandits get "one free Molotov Cocktail" as their recurring perk. **[INFERENCE — our own comparison across the six faction write-ups, p.36–37; the book states no balancing methodology between them.]** Thematically defensible (Traders *should* be cheap), mechanically uneven.
- **No stated tie-break for equidistant Zone Hostile targets.** The AI rule says "attack the closest, visible model," but two published crews rules don't say what happens when two models are exactly tied. **[NOT FOUND — a genuine small gap in the printed rules, not an inference.]**

---
## Source

- Primary: *Zona Alfa: Salvage and Survival in the Exclusion Zone*, Patrick Todoroff, Osprey Games, 2020. ISBN 9781472835697 (PB)
- Capture: `research/sources/zona-alfa/source.md` (full 65-page verbatim extraction; `research/sources/zona-alfa/meta.json` for provenance and hash)
- Related: [[Wargaming Research Hub]] · [[The Walking Dead All Out War]] · [[Bolt Action]] · [[Trench Crusade]] · [[Necromunda and Mordheim]] · [[Malifaux]] · [[Kill Team]] · [[Ideas Inbox]]

---
*Add one row per mechanic to [[Wargaming Research Hub]] when this note is finished.*

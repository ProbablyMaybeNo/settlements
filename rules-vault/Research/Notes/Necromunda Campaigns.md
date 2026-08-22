---
type: research-note
title: Necromunda Campaigns
game: Necromunda — all eight published campaign systems (N17 → N23, 2017–2024)
designer: Games Workshop Design Studio (multiple authors/books across ~8 years)
publisher: Games Workshop
depth: primary — official rulebook text via a fan consolidation site (NecroRAW), one section cross-checked page-for-page against the source PDF
retrieved: 2026-08-22
source_url: https://www.necroraw.com.ru/docs/campaigns
capture: research/sources/necromunda-campaigns/
tags: [settlements/research]
---
# 🎲 Necromunda — Campaign Systems

> [!abstract] In one breath
> **Eight distinct published campaign systems from one design team over eight years** — no other game in the corpus has more than one. The prize isn't any single system, it's the sequence: **one reusable "Territory" chassis gets reskinned five separate times** (Territories → Rackets → Sympathisers → Road Sections → Underhells camps), **one persistence mechanic (the splinter gang) gets reprinted nearly verbatim three times** across seven years, and the underdog-catch-up mechanism visibly **evolved from a stack of bonus cards into a proper spendable currency**. And buried in the Outlander Campaign is a **settlement-and-structures layer using the same two nouns as our own [[Settlement]] and [[Structures]] notes** — the single most directly comparable published system found so far.

| | |
|---|---|
| **Publisher** | Games Workshop |
| **Scale / format** | Escalating gang-vs-gang skirmish campaigns, 3–8+ players, one Arbitrator |
| **Core resolution** | *(shared with the core rules — see [[Necromunda]])* |
| **Depth of read** | Primary — official rulebook text, consolidated by the NecroRAW fan project; the Outlander settlement section additionally cross-checked page-for-page against `book-of-the-outcast.pdf` |
| **Raw capture** | `research/sources/necromunda-campaigns/` in the Settlements repo |
| **Source** | necroraw.com.ru/docs/campaigns (⚠️ not necroraw**.ru** — that domain is dead and now an unrelated adult link-farm) |

---
## Why it's here

Settlements' campaign and settlement layer is its least-settled area ([[Settlement]], [[Structures]], [[Territory]] all marked "Drafted"; [[Diplomacy]] is "Not Started"). Necromunda is the deepest published well available for exactly this problem, and uniquely lets us watch **one design team solve the same problems eight times** — territory control, catch-up, alignment/reputation, and campaign endings — across nearly a decade, keeping some choices every single time and abandoning others. A convergent choice repeated eight times is close to a "published constant"; a choice that changed between books is a live design fork, not a settled answer.

---
## The Outlander settlement — a Materials-costed structure catalogue with no research gate

**Type:** Settlement · **Take:** ⭐ steal — the single most important finding in this note

*Book of the Outcast*, p64–85. Each gang founds a **settlement** tracked on its own Settlement Roster sheet, separate from the gang roster. It starts with exactly **two free Structures** — an Isotopic Fuel Rod and a Water Still, both Supply-type — and grows from there. **[FACT — verified against the primary PDF, see Source]**

**24 Structures total**, in three named categories that are also the three things a settlement can *be for*:

- **Supply** (8 entries) — generate **Materials**: Power, Sustenance, Salvage. *"Materials represent such things as power cells, useful scrap, corpse-starch rations and other vital underhive commodities."*
- **Building** (10 entries) — a grab-bag of discrete bonuses: cheaper Hangers-on, more Recovery slots cleared, raising your own Supply/Building caps (Corpse Yard, Habs), Home Turf Advantage, immunity to being raided at all (Vault).
- **Defence** (6 entries) — battlefield-shaping terrain the defender places for free: a 6"×12" Chasm, Minefields, Walls and Gates, a Watchtower.

**Every Structure is exactly three fields** — Building (Type), Benefits, Build Costs/Requirements — and costs are paid **only in Materials**, never credits. Some Structures gate on owning another Structure or a named Hanger-on (*Bullet Hall* needs a *Drinking Hole*; *Doc Clinic* needs a *Rogue Doc*), but **there is no tech-tree ordering beyond that** — no research phase, no unlock sequence. *"There is no limit to the number of Structures that can be added to a settlement during a single post-battle sequence, provided the requirements are met."* **[FACT]**

**Why it works.** The three-category split does triple duty: it's the shopping catalogue, it's the settlement's identity (a Defence-heavy settlement plays differently in a raid than a Supply-heavy one), and — via the Location mechanism below — it's also the slot cap. One taxonomy, three jobs, the exact kind of compression Settlements' own design tenets reward.

**For Settlements.** This is a genuinely close structural cousin of [[Structures]]: both use a small fixed catalogue (Necromunda's 24 vs our 23), both cost a materials-like resource rather than the fielded-army currency, both cap structure count rather than gating behind research. The gap worth naming: Necromunda's Structures have **no footprint or physical board presence** — a Vault is a rules effect on a card, not a placed object on the settlement canvas the way our own [[Structures#The settlement canvas|12"×36" canvas]] insists every entry must be. Our "every structure is a real object on a real board" design contract (`Structures.md` rule #2) is *stricter* than Necromunda's, not looser — worth naming as a place we've already gone further than the closest published precedent.

---
## Settlement Locations — one choice caps three structure categories independently

**Type:** Settlement · **Take:** ⭐ steal

*Book of the Outcast*, p67. Before anything else, a player picks **one of five Locations** for their settlement — Factorum Run-off, Boneyard, Ghost Town, The Depths, Edge of the Hive — each rated **Defence / Resources / Toxicity, 1–6**, and **locked for the campaign** once chosen. **[FACT — verified against the PDF]**

| Location | Defence | Resources | Toxicity |
|---|:--:|:--:|:--:|
| Factorum Run Off | 3 | 6 | 3 |
| Boneyard | 4 | 4 | 4 |
| Ghost Town | 2 | 5 | 5 |
| The Depths | 6 | 3 | 3 |
| Edge of the Hive | 5 | 5 | 2 |

Those three numbers are **hard, independent caps** on the three Structure categories: *"A settlement may not have more Defence Structures than its Defence rating. …not more Building Structures than its Toxicity rating. …not more Supply Structures than its Resource rating."* A Depths settlement can build six Defence Structures but only three Supply and three Building; a Factorum Run-off is the mirror image.

**Why it works.** One decision, made once, produces **three separate resource ceilings** without three separate systems — and it's flavour-coherent (a toxic industrial site *should* support more buildings than a barren defensible pit, and the fiction explains the number instead of hiding it). It's a genuinely elegant three-for-one compression.

**For Settlements.** Places directly in the four-way comparison we already have running:

- [[Oathmark#The kingdom widens the menu]] — growth is a wider *menu*, never a bigger fielded army. Necromunda's Location caps agree completely: nothing here raises Gang Rating, only what you're *allowed to build*.
- [[Last Days Zombie Apocalypse#The Refuge costs zero]] — a single slot-cap number (Empty Spaces) outside the creation budget. Necromunda's Location is the same shape, but **splits the single cap into three independent ones** instead of one shared pool.
- [[Fallout Wasteland Warfare#Land — a purchasable slot-cap that also funds a scenario-specific war-chest]] — Land is a *purchasable*, single, growing cap; Necromunda's Location caps are **fixed at founding and never grow**. Necromunda's version is the "choose your ceiling once" answer; Fallout's is "your ceiling rises as you invest."
- [[Mordheim#The encampment layer — two full settlement rulesets we didn't know existed]] — Mordheim's Encampment layer is comparatively thin; Necromunda's three-axis Location cap is the more developed published version of "where you settled shapes what you can build," worth reading as the fuller draft of the same idea Mordheim only sketched.

The honest fork this raises for [[Settlement]]: our founding rules give every player the **same free four structures and the same 250 Materials + 150 Credits budget** regardless of chosen [[Settlement#Choosing a location|Location]] (the Location table only grants a *bonus structure or Materials*, not a differentiated cap). Necromunda's Location instead permanently **shapes the ceiling itself**, three ways. Adopting that would mean re-opening the Location table to add per-category slot limits — a bigger change than "which free structure do I get," and one that should be a deliberate ruling, not a drive-by addition.

---
## Territories — one boon chassis, reused across the entire product line

**Type:** Settlement · **Take:** ⭐ steal — the load-bearing structural finding for the cross-campaign comparison below

*Necromunda Core Rulebook (2023)*, p171–173 (Dominion Campaign). Every gang holds an unlosable **Settlement Territory** (their hideout), plus however many of a shared pool of named Territories the map generates — scaled directly to player count (9 at 3 players, up to 24 at 8). **[FACT]**

Each Territory grants exactly one of five **Boon** types while held, lost the instant it's lost: **Income** (credits to Stash), **Recruit** (a free fighter/Hired Gun/Hanger-on that still counts toward Rating and Wealth), **Equipment** (added to Stash), **Reputation** (a flat add), or **Special** (a bespoke rule, e.g. *Archaeotech Device* grants free weapon Traits; *Tunnels* lets fighters deploy from tunnel-entrance markers).

**Enhanced Boons** layer House-specific upgrades onto the same base entry — *"an Escher gang might be able to grudgingly sift some valuables from a Refuse Drift, but to a Cawdor gang the same refuse pile is a hoard of hidden relics."* An Enhanced Boon in the *same category* as the standard Boon **replaces** it; a different-category Enhanced Boon **stacks alongside**. Territory generation deliberately front-loads relevance: *"For each House represented by a player's gang, take the cards for those Territories that offer Enhanced Boons to gangs of that House"* and draw one per House before filling the rest randomly.

**Why it works.** A tight, closed vocabulary (5 Boon types, applied to ~25 named cards) generates enormous fictional variety without needing 25 bespoke subsystems — and the Enhanced-Boon layer means every player's map *should* contain at least one card that specifically rewards their choice of faction, without that card being useless to everyone else.

**For Settlements.** Direct input to [[Territory#The territory card — eleven required fields|the territory card's 11 required fields]] — field #7, **"Control benefit — access, never power,"** is already the same rule Necromunda enforces implicitly (every Boon either widens options or adds flat resources, never raw combat stats). The **Enhanced Boon** idea is new input worth weighing for [[Territory]] and eventually [[Factions]]: a shared territory deck where *some* cards specifically reward whichever faction identity a crew picks, without requiring a parallel faction-specific deck.

---
## Enhanced Boons, Linked Rackets, Sympathisers, Road Sections — the same chassis, reskinned five times

**Type:** Settlement · **Take:** 📎 reference — the real prize of this capture

This is the finding no other single game in the corpus can offer, because no other game published this system more than once. **The "own a card, get a benefit while you hold it, lose the benefit the instant you lose the card" chassis is not unique to Dominion's Territories** — it is the load-bearing pattern of the entire product line:

| Book | Name | Chassis element added |
|---|---|---|
| Core Rulebook (2023) | **Territories** | Base chassis: 5 Boon types + House Enhanced Boons |
| Book of Judgement (2023) | **Rackets** | Adds **Linked Rackets** — a synergy *graph*, not a flat bonus list (below) |
| Aranthian Succession — Cinderak Burning | **Sympathisers** | Same cards, renamed; adds a **second, phase-gated Boon** ("Spark of Rebellion Phase") layered on top of the standing one |
| Ash Wastes Rulebook | **Road Sections** | Territories become **edges in a graph**, not nodes — see below |
| Book of Desolation | **Underhells camps** | Territories held for exactly **one cycle**, discarded and re-rolled rather than kept — camp, don't settle |

**Why it matters.** Across five books and roughly seven years, the design team never once reinvented "a card that pays out while you hold it." They **varied exactly one thing per book** — what the card's second axis is (a synergy graph; a time-gated bonus; a graph edge instead of a node; a forced one-cycle churn) — while keeping the base Boon vocabulary, the ownership-gated payout, and the loss-on-loss rule completely constant. **That stability is itself the finding**: the *loss condition* (lose the card, lose the benefit, no grace period) is the one thing that never varies across eight years of published design, and it is worth treating as closer to load-bearing than any individual Boon number.

**For Settlements.** [[Territory]]'s existing 11-field card is already close to a synthesis of everything Necromunda tried — it has room for a graph relationship (field #10, "Adjacent territories"), a Boon-like "Control benefit" (field #7), and a "Supply requirement" (field #8) that could absorb the phase-gated-bonus idea (Sympathisers) or the road-network idea (Ash Wastes) as *variants of the same card format* rather than new systems. The honest reading: **we do not need five parallel territory systems** — Necromunda's own history argues for exactly one flexible card format, instantiated differently per campaign type, which is what [[Territory]] already is.

---
## Linked Rackets — boons that chain into a synergy graph

**Type:** Settlement · **Take:** ⭐ steal

*Book of Judgement*, p72. Each of ~26 named **Rackets** lists 1–2 **Linked Rackets**. Holding one linked Racket upgrades the base Boon to an **Enhanced Boon** (almost always a bigger income die — D6×10 → 2D6×10 with one link, 3D6×10 or 4D6×10 with both); holding both linked Rackets sometimes unlocks a qualitative special instead of just a bigger number (*Whisper Brokers* held with both links lets the controller **choose the scenario at stake**, or auto-attack via Ambush on a passed Intelligence check). **[FACT]**

> *"The Narco-distribution Racket grants an Income Boon of D6×10 credits. If a gang also controls Out-hive Smuggling Routes and Ghast Prospecting, they gain the Income Boon listed for having two linked Rackets, which is 3D6×10."*

**Guild Bond Rackets** (Water/Slave/Promethium/Coin Guild, etc.) are **mutually exclusive** — a gang can hold only one — and pay differently by alignment: Law Abiding gets a Guild alliance and a themed Entourage unit; Outlaw gets a free Bounty Hunter + Hive Scum instead.

**Why it works.** A flat bonus list rewards *quantity* of territory held; a **linked graph** rewards *specific combinations*, which turns territory-hunting into a genuine strategic-targeting problem — a rival holding your Racket's linked partner is worth attacking even if their Racket alone looks unremarkable.

**For Settlements.** Necromunda's own **Racket** name is a coincidence worth flagging: [[Mad Dogs with Guns#Taking over a Racket — a completion bonus with a matching vulnerability]] independently arrived at a "Racket" concept for the same genre-space, with a completion-bonus-plus-vulnerability shape rather than a synergy graph. Two unrelated designers reaching for the same word for "a controlled criminal enterprise that pays out" is itself a small confirming data point that the concept is a natural fit for this kind of game. For [[Territory]]: a graph of 2–3 mutually-reinforcing territory cards is a cheap way to make territory *choice* matter beyond raw count, at the cost of needing to print (or generate) the linkage graph up front.

---
## The Rule of Law and the Path of the Outlaw — a two-state alignment that can flip involuntarily

**Type:** Faction · **Take:** ⚙️ adapt

*Book of Judgement*, p36. Every gang declares **Law Abiding** or **Outlaw** at campaign start (some gang types are locked — Chaos Cultists always Outlaw, Palanite Enforcers always Law Abiding). The two states are strict mirrors: Law Abiding gets free Trading Post access, restricted Black Market, can Claim Bounties on Outlaw Captives, can form Guild Alliances; Outlaw gets the reverse (free Black Market, restricted Trading Post, every fighter carries a bounty, can form Criminal Alliances instead). **[FACT]**

**Alignment can flip two ways** — **Declared** (once per campaign, just tell the Arbitrator) or **Forced** (claim an Intrigue from the wrong category, then fail an Alignment check keyed to that Intrigue's own die size — see below). A flip costs **3 Reputation immediately** and swaps every currently-held Reputation Boon for the new alignment's equivalent bracket (below), plus the loss of all current Hangers-on.

**Why it works.** The mirrored effects mean neither state is strictly better, so the choice is a genuine trade (legal supply chain vs. cheap illegal gear), and the **forced-flip risk baked into off-category Intrigues** means a player can be tempted into betraying their own alignment mid-campaign by a single good in-battle opportunity, without the Arbitrator ever having to adjudicate it by hand.

**For Settlements.** The nearest published precedent yet found for our unstarted [[Diplomacy]] note's **"reputation/standing tracking and what it affects mechanically"** bullet. Compare [[Uprising Campaign]]'s three-way version below — Necromunda's own product line disagrees with itself on whether two aligned camps or three (with a genuine fence-sitting option) is the better shape, which is useful precisely because it's an unresolved internal fork, not a settled answer.

---
## Intrigues — a claimable sub-plot deck that risks your alignment

**Type:** Scenario · **Take:** ⭐ steal

*Book of Judgement*, p63. Draw **3 Intrigue cards** per battle (pre-battle step 4), keep them face-down, and claim any one whenever its printed **Criteria** are met by simply picking the card up. **[FACT]** 26 named Intrigues total, split by suit into a Law Abiding half and an Outlaw half, each carrying a **Category**, an **Alignment Test die** (D6 up to 4D6 — bigger reward, bigger die, bigger risk), a **Reward** (Reputation, credits, or an in-battle special), and **Criteria** (a concrete, checkable in-battle action — perform an action twice, take down the enemy Leader and every Champion, plant and detonate a bomb at battlefield centre).

Claiming an Intrigue from the *wrong* category for your current alignment (e.g. an Outlaw gang claims a Law Abiding Intrigue) forces an **Alignment check** using that Intrigue's own die during the post-battle sequence; failing it flips your alignment involuntarily. The designer's own note warns against stacking other sub-plot systems on top: *"it is recommended that other sub-plots are not used in a Law and Misrule Campaign as they add another layer of possibilities to games which, in addition to Intrigues, can make those games a bit overburdened with rules."*

**Why it works.** It's a self-contained, criteria-checked mini-objective layer that runs **inside** an existing battle rather than requiring a new phase, and the built-in temptation ("this off-category Intrigue pays more, but might cost you your alignment") gives every battle a small side-bet without a separate resolution step.

**For Settlements.** A cheap, portable pattern for [[Scenarios]] or [[Events]]: a small deck of criteria-gated bonus objectives drawn fresh each battle, claimable by either player, costing nothing to include beyond the deck itself. The explicit designer warning against **stacking** two sub-plot systems is worth carrying forward as a standing caution against our own anti-bloat tenet: if Settlements ever adds a comparable "side objective" deck (the [[Territory#The territory card — eleven required fields|territory card's field #3]] already reserves a slot for one), it should replace rather than sit alongside any other bonus-objective layer.

---
## Reputation Boons — a continuous, bracketed reward ladder that self-revokes

**Type:** Campaign · **Take:** ⚙️ adapt

*Book of Judgement*, p60. Reputation is tracked **per alignment** and unlocks Boons in six brackets (1–4, 5–9, 10–14, 15–19, 20–24, 25+), each bracket granting one Outlaw-side Boon *and* one Law-Abiding-side Boon at once — a gang only benefits from the column matching its current alignment. **[FACT]**

> *"As a gang's Reputation increases, so does the number of Boons it can claim. However, should a gang's Reputation ever fall, it will lose any Boons it is no longer entitled to."*

Boons escalate from flat market access (1–4: unrestricted Black Market / Claim Bounties) to free recruits (5–9, 15–19, 25+) to percentage discounts and bounty multipliers (10–14, 20–24) — a genuine ladder, not a single unlock.

**Why it works.** Because Boons are **revoked automatically** the moment Reputation drops below their threshold, the ladder never needs a separate "downgrade" rule — the same comparison that grants a Boon also strips it, with no special-cased edge conditions.

**For Settlements.** A clean, low-cost pattern if [[Diplomacy]] or [[Campaign]] ever wants a standing Reputation track: six numeric brackets, each printed once, auto-revoked on backslide, is cheaper to implement and referee than a points-and-events system that has to track *why* a bonus was granted in order to know when to remove it.

---
## House Patronage — underdog banding evolved into a spendable currency

**Type:** Campaign · **Take:** ⭐ steal — updates an existing hub finding, doesn't replace it

*Necromunda Core Rulebook (2023)*, p238. **Underdog** is defined precisely: ≥400 credits behind on Gang Rating (or starting-crew value). For every full 100-credit gap, the Underdog receives **100 "House Patronage" credits**, spendable **that battle only**, on a fixed menu — random or chosen gang tactics, temporary Hired Guns of several types, or +1 XP per model. **[FACT]**

| Benefit | Cost | Cap |
|---|---|---|
| Random extra gang tactic | 100cr each | 0–5 |
| Chosen gang tactic | 200cr each | 0–2 |
| Random Underdog gang tactic | 200cr each | 0–4 |
| Chosen Underdog gang tactic | 400cr each | 0–2 |
| Temporary Hive Scum | varies | 0–5 |
| Temporary House Ganger | varies | 0–3 |
| +1 XP per model this battle | 400cr | 0–3 |

^tbl-house-patronage-sample

Everything hired this way is **temporary**: not added to the permanent roster, cannot group-activate, doesn't count toward Bottle checks.

**Why it works, and why it's an update, not a new finding.** The vault already has [[Necromunda and Mordheim#Underdog banding|Underdog banding]] logged as **[FACT]**: *"Underdog bonuses scale by the difference in rating, not by win/loss record."* That claim came from the **older edition's mechanism** — extra gang tactics cards scaling with the rating gap, which the same note observes can produce *"a large hand of these that can be difficult to manage."* House Patronage is the **current core rulebook's direct fix for that exact problem**: instead of a growing hand of tactics cards, the gap converts into a **spendable currency** with a fixed shopping list — same self-zeroing-at-parity shape, same scale-by-gap mechanism, but now capped, itemised, and entirely temporary rather than accumulating. **Both mechanisms are real and both are [FACT]; they're sequential drafts of the same idea, seven-plus years apart.**

**For Settlements.** Reinforces [[Necromunda and Mordheim#Underdog banding]]'s core lesson for [[Campaign]] — scale the catch-up by the *rating gap*, not the scoreboard — and adds a second, sharper lesson: **cap the catch-up bonus's shape, not just its size.** An open-ended "more tactics cards" reward becomes unwieldy exactly as it becomes generous; a **fixed menu with per-item purchase caps**, funded by a gap-scaled currency, stays generous without ever becoming unmanageable. Compare [[Judge Dredd Miniatures Game#Underdog Big Meg Cards — a bonus resource that scales with the gap, not the scoreboard]] — a third independent confirmation that "resource scales with rating gap" is close to a converged answer across this whole sub-genre, even though the *shape* of the resource (cards vs. spendable credits) is still an open design choice.

---
## Unaligned as a third faction — the Uprising Campaign's fence-sitter

**Type:** Faction · **Take:** ⚙️ adapt

*Necromunda: Apocrypha Necromunda (2024)*, p76. Where Law and Misrule is strictly two-sided, the **Uprising Campaign** offers **Order / Chaos / Unaligned**, and each side gets a *different kind* of perk rather than a flat resource bump: **[FACT]**

- **Order**: re-roll credit-reward dice; +1 extra fighter when *defending*.
- **Chaos**: +1 extra Meat (a Chaos-specific resource) per scenario; +1 extra fighter when *attacking*.
- **Unaligned**: +1 extra Reputation on any scenario reward; the Leader earns bonus XP for surviving a battle undefeated.

Switching sides later is a **hard, one-way, condition-gated flip** (3+ fighters turned to Chaos Spawn tips Order → Chaos; 3+ willingly-returned Captives tips Chaos → Order) — there is **no free "just declare it" option** the way Law and Misrule allows once per campaign.

**Why it works.** The Unaligned perk isn't a diluted version of the other two — it's a genuinely different axis (Reputation + XP rather than resources + crew size), which makes staying neutral a real strategic choice rather than a placeholder state players rush to leave. And role-conditioned bonuses (attacker vs defender) mean the *same* alignment perk rewards different play depending on which side of a given battle you land on.

**For Settlements.** Direct input for [[Diplomacy]]'s **"how diplomacy scales from 2-player up to multiplayer"** open bullet: a three-state model where the middle state has its *own* distinct reward (not a lesser version of the other two) is a cheap way to make neutrality playable in a two-faction-flavoured setting, without inventing a third full faction's worth of content.

---
## The 3× kill-ratio threshold — gating territory control behind a decisive win

**Type:** Campaign · **Take:** ⚙️ adapt

*Necromunda: Apocrypha Necromunda (2024)*, p76, and independently, *Core Rulebook*'s **Classic Campaign** variant (p226). A battle only transfers Territory control if the winner inflicted **at least three times as many Out-of-Action results** as they suffered. **[FACT]** Below that ratio, the win still pays Reputation/XP/credits as normal — nothing about the *battle's* outcome changes — but the *map* doesn't move.

**Why it matters.** This is a structurally different anti-snowball lever from House Patronage or Reputation banding: instead of handicapping the stronger side, it **raises the bar for what counts as decisive**, so narrow, marginal wins accumulate personal rewards without accumulating map-control momentum. It's notable that **two unrelated campaign systems, four years apart, independently converged on the identical 3× ratio** — a rare case in this whole capture of a specific *number*, not just a mechanism shape, repeating across books.

**For Settlements.** A genuinely different tool than anything else logged for [[Campaign]] or [[Territory]]'s control-flip rules: decouple "you won" from "the map changed," and require a *margin*, not just a result, before territory/structures/standing actually transfer. Cheap to bolt onto any existing win condition, and it directly slows the rate at which a single strong crew can chain territorial gains battle after battle.

---
## Road Sections — territory as graph edges, and the same node paying two gangs at once

**Type:** Settlement · **Take:** ⚙️ adapt

*Necromunda: Ash Wastes Rulebook*, p114. Territories here are **36 named Road Sections**, each an *edge* connecting two places (a fixed location or another Road Section) rather than a node. Owning an **unbroken chain** of Road Sections between two named locations creates a **Trade Route**, which pays a separate, larger bonus on top of each individual segment's income. Crucially, **multiple gangs can hold the same Trade Route simultaneously** by routing through different segments — the map is a graph with more than one valid path, not a fixed set of exclusive tiles. **[FACT]**

**Raiders vs. Traders is a built-in structural split**, not a bolt-on variant: Outlaw gangs and Ash Waste Nomads can be designated **Raiders**, who earn the *same* per-segment income but a **separate Raiding Bonus** off the same Trade Route instead of the Trading Bonus — every route entry in the book prints both numbers side by side.

**Why it works.** Making territory an *edge* rather than a *node* means the map itself encodes adjacency and route-planning as the core spatial puzzle, and letting two gangs profit from the same route through different segments avoids the usual zero-sum "only one owner" territory problem entirely.

**For Settlements.** Feeds [[Territory#The territory card — eleven required fields|field #10, "Adjacent territories — the map graph"]] directly: this is a concrete published example of territory-as-graph-edge rather than territory-as-node, worth keeping in mind if [[Territory]] ever wants a supply-route or trade-lane layer on top of the base card format, rather than reinventing one from scratch. The **dual Trading/Raiding payout on one shared object** is also a clean, low-cost way to let two different playstyles profit from the same piece of the map without splitting it into two systems.

---
## Madness, Desolation and Darkness — three escalating hazard axes locked to campaign phase

**Type:** Morale · **Take:** ⭐ steal — direct input to the fear/terror open question

*The Book of Desolation* (Underhells Campaign), p71. Three **independent hazard axes**, each with exactly **three severity tiers**, and each tier hard-locked to one of the campaign's three phases: **[FACT]**

| Phase | Madness | Desolation | Darkness |
|---|---|---|---|
| Incursion | Ghosts of the Dead | Limited Trade | Heavy Skies (Visibility ≤18") |
| Delving | Echoes in the Abyss | Crane Cities | Toxic Deeps (Visibility ≤12") |
| Survival | Shadow of the Broodmind | Cut Off From The World | Stygian Depths (Visibility ≤9") |

**Madness is the fear axis, and it's a genuine second tier above the game's existing Broken condition, not a bolt-on track.** At the mildest level, a fighter who fails to rally from Broken risks gaining a worse **Insane** condition on a failed Willpower check; at the harshest level (Survival phase), *failing to rally from Broken skips straight to Insane, no roll*. **Desolation** throttles trade access, inflating Rare/Illegal ratings by +2 to +6 depending on faction and phase. **Darkness** is a flat, tightening Visibility cap.

**Why it works.** Three axes, three tiers each, and the *entire escalation schedule is pre-printed and phase-locked* — the Arbitrator never decides how bad things get this week, the campaign structure already decided it. And critically, **Madness escalates the fear system that already exists** (Broken → worse) rather than adding a parallel Sanity/Horror track next to it.

**For Settlements.** The single most useful data point in this capture for the open **"fear/terror beyond the current Stress track"** question. The mechanism worth stealing isn't the specific fiction (Broodminds, Genestealers) but the **shape**: a second, worse failure state layered directly on top of the existing Break/Broken mechanism, escalating on a **pre-printed schedule tied to campaign progress** rather than an ad-hoc GM call. If Settlements ever wants Stress to have a "this crew has been out past curfew too many times" escalation, this is the cleanest published template — extend the existing Stress/Break mechanism one rung further, on a schedule the campaign layer already tracks, rather than building a parallel dread meter.

---
## The Exploration-point race — the campaign advances on pooled player action, not the calendar

**Type:** Campaign · **Take:** ⚙️ adapt

*The Book of Desolation*, p67. The Underhells Campaign's three main phases (Incursion → Delving → Survival) are each **"Variable"** length — not weeks, not cycles. Every battle (win or lose) earns **Exploration points**; the *pooled sum across every player* is checked at the end of each cycle, and the moment it reaches **3× the player count**, the phase ends immediately, mid-cycle if necessary. **[FACT]**

Unspent Exploration points are then spent — or lost:

- Up to 5 points → D3×10 credits of gear, per point spent.
- 2 points → choose your *next* Territory instead of drawing randomly.
- 6 points → gain a *second* Territory that survives the whole phase instead of being discarded and re-rolled each cycle.

**Why it works.** Because the threshold is a **pooled aggregate**, the whole table's collective pace — not any one player's — decides when the campaign moves forward, which removes the "waiting on the slowest player" problem some campaign structures have without removing individual agency (everyone still contributes to, and draws from, the same pool). And a currency that's about to evaporate at a phase change creates a real spend-now-vs-save-for-later tension every single cycle.

**For Settlements.** A genuinely different campaign-pacing model than anything else logged so far — every other campaign captured in this vault ([[Fistful of Lead#Renown — one currency doing reroll, recruitment, upgrade, and campaign-end all at once]], [[Zona Alfa#The Stalls, and the 10,000 Ruble Plan]], [[Trench Crusade#The published threshold ladder]]) triggers its ending or its phase change off an **individual** player's accumulated total. This is the first case in the corpus of a **shared, table-wide pooled threshold** deciding pacing instead. Worth weighing for [[Campaign]] if a future draft wants downtime or escalation phases to advance on aggregate play rather than a fixed calendar.

---
## Splinter gangs — the one persistence mechanic every book keeps

**Type:** Campaign · **Take:** ⭐ steal — direct input to the per-unit-persistence open question

Published **three separate times**, nearly verbatim, across seven years: *Gang War* (2017, the pre-Dominion "Turf Wars" system, p25), *Book of Judgement* (2023, Law and Misrule, p62), and the *Core Rulebook*'s own Campaign Variants section (2023, p226 — reprinted specifically as a tool usable with *any* campaign type). **[FACT — confirmed by direct comparison of all three published texts]**

The mechanism is identical every time: pick **one Champion** from a gang played in a previous campaign to become the new gang's **Leader**, keeping their equipment, Advancements and permanent injuries, paid for at their existing Credits value. Up to two Juves/Specialists can follow as Champions, and up to half the Gangers can follow as Gangers. The rest of the roster is filled out from a fresh starting-credit budget, under the same composition rules as any new gang.

**Why it matters.** This is, by a wide margin, **the most stable single idea in the entire eight-campaign, seven-year product line** — more stable than any specific Boon number, Trigger threshold, or campaign length. When a design team keeps reprinting the *same* mechanism unchanged across three different books and two different campaign systems, that is strong evidence it solved a real, recurring problem cleanly: **letting a favourite character survive the death of their gang without carrying the old gang's full accumulated power forward wholesale.**

**Why it works.** It gives permanent-injury and Advancement investment somewhere to go even when the roster around a character collapses, **without** letting a veteran's full gang-worth transfer at once (only one Champion plus a capped handful of followers, and everyone pays full price again) — a controlled, partial persistence rather than an all-or-nothing "keep the whole gang" or "lose everything" choice.

**For Settlements.** The single best published answer found so far to the open **"per-unit persistence and injury"** question: when a crew is wiped or retired, let **one veteran** (with their gear, Advances, and scars intact) become the seed of the next crew, rather than either the whole roster surviving or nothing surviving. Cheap to implement — it's a recruitment-time rule, not a new tracked resource — and it directly rewards the kind of attachment [[Progression]] and the [[Necromunda and Mordheim#Lasting injuries|lasting-injury lineage]] are already trying to build.

---
## Twelve dials on one chassis — the official campaign variants

**Type:** Campaign · **Take:** 📎 reference — a design *technique* worth copying independent of any single variant

*Necromunda Core Rulebook (2023)*, p226. Twelve named, official variants, **every one of them a single, isolated change to the same base Dominion chassis** rather than a new system: **[FACT]**

| Variant | The one lever it pulls |
|---|---|
| Old Kingdoms | Skip Occupation entirely — start already holding Territory |
| Into The Unknown | Territories drawn face-down, revealed only when fought over |
| **Escalation Campaign** | **Removes credit rewards from combat outcome entirely** — flat 250cr/battle, capped 500cr/week, win or lose |
| Classic Campaign | Reverts equipment/weapon rules to an older edition; territory flips only on the 3× kill-ratio (above) |
| Ironman Campaign | One-shot 3,000cr gang, **zero replenishment ever** — ends when only one gang can still field fighters |
| Dome Rush | No held Territory at all — one shared Territory refreshes weekly, pays everyone at once |
| Last Gang Standing | Single shared Territory, permadeath, multi-player free-for-all every battle |
| Hive Empires | Full connected-zone map metagame — must be adjacent to attack |
| Nomads of the Underhive | Deliberately impoverished: capped weekly income, capped gear rarity, forced weekly Territory discard |
| Helmawr's War | Two-team campaign; only one team starts with any Territory at all |
| **Perpetual Campaigns** | Loops indefinitely; **crew-size cap scales directly with Gang Rating** (10/15/20/25 fighters at ≤1000/2000/3000/3001+cr) |
| Semi-Perpetual / Splinter | A **Triumph → next-campaign starting bonus** table (below) |

^tbl-twelve-dials-on-one-chassis

**Why it matters as a technique, independent of any one variant.** Every variant is stated as **"uses the following rules"** against the base Dominion chassis — a short delta list, never a rewritten campaign. That's the exact same "publish deltas, never the derivation" discipline the vault already logged in [[Necromunda and Mordheim#Publish deltas, never the derivation]] for the *advancement* system, now shown to apply equally well at the **campaign-structure** level.

**For Settlements.** A genuinely reusable authoring pattern for [[Campaign]]: once a base campaign chassis is locked, publish variant *play* as a short list of stated deltas against it (remove this reward, cap that number, add this one rule) rather than a parallel campaign write-up. The **Perpetual Campaign's Gang-Rating-scaled crew cap** (10/15/20/25 fighters by rating band) is also directly relevant to Settlements' own rank-body / Crew Rating scaling conversation — a concrete published example of "let the roster-size cap grow in steps tied to the same number that already gates power," worth weighing against our own campaign-start vs. match-play Crew Rating caps.

---
## Semi-Perpetual Campaigns — a Triumph-to-legacy-bonus table

**Type:** Campaign · **Take:** ⚙️ adapt

*Core Rulebook*, p226. When a campaign ends and a *new* one begins with carried-over fighters, each of the five Dominion Triumphs won in the *previous* campaign converts to a **small, specific starting bonus** in the next: **[FACT]**

| Triumph | Next-campaign benefit |
|---|---|
| Dominator | +1 extra starting Territory, drawn at random after everyone else has chosen |
| Slaughterer | +6 XP to distribute among returning fighters (max 2 per fighter) |
| Creditor | +100 starting credits in the Stash |
| Warmonger | +3 starting Reputation, and first choice of attacker/defender in the first battle |
| Powerbroker | One free starting Hanger-on, from a named list |

**Why it works.** It's a **legacy system with a hard ceiling** — the bonus is small, one-time, and tied to a specific prior achievement rather than a compounding stat bonus, so a dominant gang's *next* campaign starts meaningfully but not overwhelmingly ahead.

**For Settlements.** Relevant if a Settlements campaign ever runs in seasons: a small, capped, named-achievement-to-starting-bonus table is a controlled way to let a strong previous campaign matter in the next one, without the multi-campaign snowball a raw stat carryover would create.

---
## Campaign end conditions, compared across the line

**Type:** Campaign · **Take:** 📎 reference

Eight systems, and at least **four genuinely different end-condition shapes**, none of them wrong: **[FACT for each mechanism cited; the comparison itself is [INFERENCE]]**

- **Fixed calendar + tallied Triumphs** (Dominion, Outlander, Uprising): the campaign runs a printed number of cycles, then the Arbitrator hands out named Triumphs (most Territories, highest Wealth, most battles fought, etc.) — no single "winner," several parallel bragging rights.
- **Fixed calendar + a scored meta-verdict** (Law and Misrule): the same Triumph-tallying, but each Triumph is *also* worth exactly one point toward **"Weighing All in the Balance"** — a second-order score across the *whole table* for which alignment (Law vs Misrule) came out ahead, layered on top of individual results.
- **A climactic sudden-death final battle** (Turf Wars' **Apotheosis/Showdown**, 2017): the final cycle adds temporary catch-up rules (Desperation: the lower-Reputation gang discards their highest Bottle-test die; Consolidation: the loser's Turf shrinks; Ignominy: a lower-Reputation winner steals Reputation from a higher-Reputation loser), then the two highest-Reputation "Top Dogs" fight one **auto-pass-Bottle-tests** winner-take-all Showdown for the title of Overlord.
- **A pooled, aggregate threshold** (Underhells' Exploration-point race, above): there's no fixed calendar at all — the *table's* combined pace decides when each phase, and eventually the campaign, ends.

**For Settlements.** Directly extends the existing comparison at [[Fistful of Lead#Renown — one currency doing reroll, recruitment, upgrade, and campaign-end all at once]] (player-chosen Showdown trigger) and [[Zona Alfa#The Stalls, and the 10,000 Ruble Plan]] (player-chosen retirement fund) — both of those are **player-decided** endings. Necromunda's product line instead defaults to **Arbitrator-scheduled** endings almost everywhere, with Turf Wars' Showdown as the one genuinely dramatic exception (a *forced* final confrontation between the two leaders, not an opt-in). Also compare [[Judge Dredd Miniatures Game#The Notoriety phase ceiling — fixed schedule, catch-up top-up, never performance-tied]] — a fixed-schedule ceiling with a catch-up top-up is closer kin to Necromunda's House Patronage than to any of its own end-condition designs, a useful reminder that "how the campaign ends" and "how it stays balanced along the way" are separate design questions this whole corpus keeps answering independently.

---
## What it gets wrong

**Type:** *(cross-cutting)* · **Take:** ⚠️

- **The chassis-reuse discipline breaks down under supplement pressure.** By the time of *The Aranthian Succession*, the same Territory chassis has been renamed *twice* (Rackets, Sympathisers) purely for flavour, with the underlying mechanism unchanged. A new reader has to independently notice "Sympathisers = Territories" — nothing in either book states the equivalence. **[INFERENCE — confirmed by direct comparison of the published mechanisms, not stated anywhere in either source]** Settlements should name its own reused chassis once and keep the name, rather than let flavour renaming happen per-supplement.
- **Splinter gangs are reprinted three times with zero cross-reference.** Despite being functionally identical across *Gang War* (2017), *Book of Judgement* (2023) and the *Core Rulebook* (2023), none of the three texts references the other two — a reader who's only seen one book has no way to know the mechanism is a load-bearing constant rather than a one-off house rule for that specific campaign. **[INFERENCE]**
- **The Ironman Campaign variant has an unstated edge case.** *"No new fighters or equipment from any source"* combined with *"ends when only one gang can still field fighters"* means a campaign with fewer than four or five players risks ending in a single unlucky string of battles for the smaller side — the variant doesn't address minimum player counts or provide a soft floor. **[INFERENCE]**

---
## Evidence & confidence

- **[FACT]** — Every specific rule, table, and quoted line above is drawn from the NecroRAW consolidation of the named published book/page. The Outlander Settlement/Structures material (settlement founding, Location caps, all 24 Structure entries) is additionally **directly verified** against `research/sources/necromunda/book-of-the-outcast.pdf` pages 67, 68, 83 and 85 by PyMuPDF text extraction — see `research/sources/necromunda-campaigns/meta.json` for the verification record.
- **[INFERENCE]** — The cross-campaign comparative claims (the reused chassis across five books; splinter gangs as the single most stable mechanism; the "delta-publishing" pattern extending from advancement costs to whole campaign variants) are this note's own synthesis, built by direct comparison of the published texts, not a claim made by any single source.
- **[NOT FOUND]** — The full 52-card Dominion Territory deck and the full 24-Racket Law and Misrule deck were captured in the working session but are only sampled (not fully reproduced) in `source.md`, for length; anyone needing an exhaustive Territory-by-Territory or Racket-by-Racket reference should re-open the NecroRAW pages directly (URLs in `source.md`) rather than trust this note as the exhaustive listing.
- **[NOT FOUND]** — This capture did not read the full `/docs/scenarios/scenario-list/` page in depth (it is a very long index of one-line scenario blurbs across the whole game, most of it outside campaign scope) — flagged on the to-read list below rather than padded here.

---
## Source

- Primary: NecroRAW (necroraw.com.ru/docs/campaigns), consolidating *Necromunda Core Rulebook (2023)*, *Book of the Outcast*, *Book of Judgement*, *Necromunda: Ash Wastes Rulebook*, *Necromunda: Apocrypha Necromunda (2024)*, *The Aranthian Succession — Cinderak Burning*, *The Book of Desolation*, and the legacy *Gang War* / *Gang War 3* (Turf Wars system). All Games Workshop.
- Capture: `research/sources/necromunda-campaigns/source.md`, `meta.json`
- Cross-check: `research/sources/necromunda/book-of-the-outcast.pdf` (pages 67, 68, 83, 85 — direct PyMuPDF verification)
- Related: [[Wargaming Research Hub]] · [[Necromunda]] (core rules, captured concurrently) · [[Necromunda and Mordheim]] (the older-edition lineage this note updates in places) · [[Settlement]] · [[Structures]] · [[Territory]] · [[Diplomacy]] · [[Oathmark]] · [[Last Days Zombie Apocalypse]] · [[Fallout Wasteland Warfare]] · [[Mordheim]] · [[Mad Dogs with Guns]] · [[Trench Crusade]] · [[Fistful of Lead]] · [[Zona Alfa]] · [[Judge Dredd Miniatures Game]]

---
*Add one row per mechanic to [[Wargaming Research Hub]] when this note is finished — see `research/sources/necromunda-campaigns/hub-rows.md` for the proposed rows (this session does not own the shared hub file).*

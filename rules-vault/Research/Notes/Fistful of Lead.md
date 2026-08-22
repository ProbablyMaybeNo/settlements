---
type: research-note
title: Fistful of Lead
game: Fistful of Lead — Reloaded, 2nd Edition
publisher: Wiley Games
designer: Jaye Wiley
depth: primary — full 62-page rulebook read in full
retrieved: 2026-08-21
source_url: https://www.wiley-games.com
capture: research/sources/fistful-of-lead/
tags: [settlements/research]
---
# 🎲 Fistful of Lead

> [!abstract] In one breath
> A **playing-card-driven Old West skirmish** (5–8 models a side, generic engine reused across 17+ Wiley Games titles) whose entire turn structure runs on a shuffled deck instead of dice or alternating activation — the first **card-activation** system in the hub. It also runs its whole "how good is this model" question through **which size of die it rolls** (d8/d10/d12) rather than a modifier, which sits in direct, sharp contrast to Settlements' locked single-d10 engine. Both are genuinely good, well-tested ideas, and **both are, as published, a second randomiser** — the honest verdict below is that neither ports whole without breaking a locked rule, even though the specific *problem* the deck solves (hidden, variable activation order) is a real gap in what we've researched so far.

| | |
|---|---|
| **Designer · publisher** | Jaye Wiley · Wiley Games (2024, this 2nd edition; game originally 2001) |
| **Scale / format** | 5–8 models a side (up to 6–8 players), 28mm, 3'×3' to 6'×4' table |
| **Core resolution** | `1 die (size set by Quality) vs a target number` — Short range 5+, Long range 8+, Tasks 3+/5+/8+; natural 1 always bad, natural 10+ always good |
| **Depth of read** | **Primary** — full 62-page rulebook, clean embedded text layer, no OCR needed |
| **Raw capture** | `research/sources/fistful-of-lead/` in the Settlements repo |
| **Source** | Wiley Games, 2024. No ISBN listed; PDF acquired directly |

---
## Why it's here

Across everything captured so far, every activation system is dice-or-alternating: [[Zona Alfa#Initiative and Alternating Activation]] and [[BLKOUT]] both roll off for priority then alternate one model at a time; [[Spectre Operations]] runs a Momentum pool. **Nobody in the hub draws cards.** Fistful of Lead is the first, and it's a mature, thrice-reprinted commercial chassis, not a one-off indie experiment — worth reading precisely *because* it's the genre's most-played answer to "how do you decide who acts next," using a completely different randomiser than everything else in the corpus.

The read paid off in a way that isn't a simple steal: the card deck (and the Quality Die system beside it) are the cleanest possible test case for Settlements' own locked rule that **no second dice type exists anywhere in the game**. This note treats that collision as the actual finding, not an inconvenience to route around.

---
## The card-driven turn — hidden, variable activation order from a shuffled deck

**Type:** Activation · **Take:** 📎 reference — good mechanism, structurally incompatible with the locked engine

Each turn: *"Grab ALL the cards. That means the cards in the discard pile and the unplayed cards and shuffle them together before each turn."* Then *"Each player is dealt one card for every miniature they control"* and *"The turn is played out from highest (King) to lowest (Deuce) card."* **[FACT — p.4]** A Caller calls ranks top-down; everyone holding that rank throws it down and activates one model for two Actions. Ties between players holding the same rank break by suit: *"Spades go first, then Hearts, then Diamonds, then Clubs are last."* **[FACT — p.4]** Cards can't be banked — *"Cards cannot be saved for later"* — and a model already activated can't go again until the deck reshuffles next turn. **[FACT — p.4]**

**Why it works.** This buys three things off one shuffle: **variable order** (nobody knows in advance whether they'll go 1st or 14th this turn), **genuine hidden information** (a hand of cards is held face-down — an opponent can't see what you're about to do or when), and, via Special Cards below, **a bonus effect stapled onto the very same draw that sets the order.** No separate initiative roll, no separate crit table.

**The honest separability question.** A standard 52-card deck, reshuffled every turn and drawn without replacement within it, is unambiguously **a second randomising system** — richer in state than a second die type, not narrower. Settlements' `1d10 + Stat vs 7+` with **no second dice type anywhere in the game** is locked specifically to close this door, so a literal port is off the table, full stop.

What's more interesting is *which* of the deck's three benefits actually needs a deck. The bonus-on-the-same-roll trick (below, Special Cards) is separable — Settlements already has a version of it in the nat-10-always-succeeds rule, and Zona Alfa independently converges on the same idea (a free bonus Action on a nat-1) **[INFERENCE]**. Variable order alone is separable too — roll a d10 per model and go high-to-low, no deck required. **But the hidden part is not.** A die roll is a public, instantaneous event; the reason a hand of cards produces genuine fog-of-war is that it's held, not rolled. Reproducing "you don't know when your opponent's model with the best card will go" using an open d10 system would need blind or simultaneous declaration on top of the roll — more table overhead than the deck it was meant to replace, not less. **[INFERENCE]** So the specific thing that makes this activation system distinctive from every dice-and-alternation system already in the hub is exactly the piece that doesn't survive translation into Settlements' engine.

**For Settlements.** [[Initiative & Activation]]. Nothing here is adoptable as written — logging it closes the "card activation" gap in the hub honestly, as a **structural dead end for this specific engine**, rather than leaving it unresearched. If Settlements ever wants genuine hidden-order activation without alternating I-go-you-go, the actual lever is simultaneous/blind declaration, not a second randomiser — a different design conversation than "should we add cards."

---
## Special Cards — a bonus effect riding the same draw that sets turn order

**Type:** Activation · **Take:** 📎 reference

Certain cards do double duty when played to activate: *"Queen of Hearts- If the miniature activated with this card has any Wounds… ONE is healed… Queen of Spades- If the miniature activated with this card is Shaken… it recovers instantly… One-Eyed Jacks (Hearts & Spades)- …a +1 to any Shooting rolls this activation… Sevens (any suit)- …may re-roll any ONE die result this activation… Sixes (any suit)- …may reload automatically… Twos (any suit)- …may choose to roll 2 dice … and pick the best result."* **[FACT — p.5]** Aces are wild but constrained: *"An Ace is wild and can be any card the player wishes. It must, however, be played in sequence."* **[FACT — p.5]** — you can hold an Ace for exactly the rank you want, but a *real* card of that rank still goes first if one's out there.

**Why it works.** Every one of these is free — no extra roll, no side-table — because the reward is wired directly into the same card that already had to be drawn and played. It also gives Special Cards a second identity as a **scarce, trackable resource**: a player who knows there are only two Queens and four Aces in the deck can reason about when the good draws are more or less likely to surface, the way a card-counter would.

**For Settlements.** [[Rules Engine]]. Directly comparable to [[Zona Alfa#Core resolution — an inverted D10, and a Critical that pays out immediately]] — both games independently arrive at "the crit/bonus rides the same roll, not a separate one." Settlements already has the equivalent lever (nat-1 fail / nat-10 succeed) at the core-resolution layer; nothing to add, but worth citing as a second, unrelated designer converging on the same shape. **[INFERENCE — convergent design, not a stated cross-reference by either author.]**

---
## The Quality Die — "how good is this model" is expressed as die size, not a modifier

**Type:** Dice · **Take:** 📎 reference — the sharpest available contrast case for our own locked rule

*"Most of the time this will be a 10-sided-die (d10), but some traits may change this to an 8-sided-die or 12-sided-die… For example, the Veteran trait means ALL rolls by this miniature use a d12. The key there is 'all rolls'. Whereas, the Ranged Fighter trait means a miniature uses a d12 for Shooting and d8 for Close Combat."* **[FACT — p.4]** Rabble (cheap 3-for-1 mooks, see below) roll a **d8** and only have 1 Wound. **[FACT — p.24]** So the same target number (5+/8+ to hit, 3+/5+/8+ for Tasks) sits under three different distributions depending on who's rolling: a d8 model literally cannot roll a 9 or 10, a d12 model can overshoot every threshold by a wide margin and has better odds at every band.

**Why it works, on its own terms.** It collapses "how skilled is this model" into a single, highly legible physical fact — the die in your hand — with no arithmetic step at all. A player doesn't compute a modifier; they pick up the die the card tells them to. It's arguably *more* legible at the table than a modifier stack, at the cost of needing three sizes of die in the box.

**Why it's the sharp edge for us.** Settlements' core resolution is deliberately the opposite of this: `1d10 + Stat + Modifiers vs 7+`, **no second dice type exists anywhere in the game**, modifier cap ±3, precisely so "how good is this model" is always expressed as an additive number on one fixed die, never as a different randomiser. Fistful of Lead is a working, successful, long-running published counter-example to that choice — proof the alternative ships fine and reads clean at the table — but it is not evidence *against* Settlements' rule, since the two are solving the same problem with genuinely different production overhead (one die size vs. three). **[INFERENCE]** Worth having on record specifically because it's the single clearest real-world instance of "the thing our locked rule explicitly forbids," should the ±3 modifier cap ever get re-litigated.

**For Settlements.** [[Rules Engine]]. Nothing to adopt — flagged as precedent and as the concrete shape of the road not taken, not as a recommendation to reconsider the lock.

---
## Traits and Equipment Slots share one build-resource pool

**Type:** List · **Take:** ⚙️ adapt

There's no points-buy for a gang at all — roster slots are fixed by role (Leader 4 Equipment Slots, Sidekick 3, Regulars and Rabble 2 each) and every model may unilaterally convert 2 Equipment Slots into 1 Trait: *"In this initial build part of creating your Gang, each member may elect to 'trade' 2 equipment slots for a trait for themselves."* **[FACT — p.30]** Gear and character-flavour compete for literally the same pool, at a fixed, published exchange rate.

**Why it works.** There's no currency to balance — a Leader who wants to be a walking arsenal simply doesn't get Traits, and one who wants five Traits shows up with a knife. The trade-off is visible on the roster sheet with no arithmetic beyond "2 for 1."

**For Settlements.** [[List Building]], [[Weapons]]. Directly comparable to [[Zona Alfa#Khrabrost' — a force-build currency made of Actions, not Credits]] — a second published example of a skirmish game running list-building with **no monetary abstraction at all**, this time at the individual-model level rather than the whole-roster level. Settlements deliberately keeps **Credits** as the one face currency (`AGENTS.md` locked mechanic), so this isn't a literal port, but the *shape* — two build resources being made explicitly fungible against each other at a flat rate, rather than each getting its own price tag — is a legitimate alternative to a fully priced Equipment list, worth naming if equipment tiering (one of Settlements' own open questions) ever wants a slot-based escape hatch instead of a per-item Credit cost.

---
## One Negative Trait buys one Positive Trait — a slot swap, not a refund

**Type:** List · **Take:** 📎 reference — third data point, different mechanism

*"The Traits listed above are Positive Traits… you may choose to take on a Negative Trait for a miniature… Negative Traits let you pick another Positive trait for the miniature. You may normally only take one Negative Trait."* **[FACT — p.28]** The list is short and flavourful — Brittle (+1 to Wound rolls against you), Coward (must roll 5+ to enter Close Combat), Drunkard (start Wounded), Greenhorn (d8 for all rolls), Slow (−1" move), Small (−1 to be hit, only 2 Wounds), Squeamish, Unlucky, Unskilled, Weakling (2 Wounds) — no point values attached to any of them.

**Why it's a different shape than our other two data points.** [[Song of Blades and Heroes#The Quality multiplier]] and [[The Rampant line#Integers, and negative costs]] both refund a **spendable point value** — a negative cost that reduces what you owe, clamped so it can't be arbitraged. Fistful of Lead has **no points system to refund into at all**: a Negative Trait doesn't lower a cost, it **unlocks exactly one extra Positive Trait slot**, capped at exactly one use per model, full stop. It's the same underlying want — "let me buy character flaws back into character strengths" — solved by trading a scarce build-slot 1-for-1 instead of arithmetic on a shared currency.

**For Settlements.** [[Skill Paths]], [[Campaign]]. Settlements currently has no separate Trait/flaw slot to attach this to — skills ride the stat in fixed, exact counts per tier and are never charged Credits (`AGENTS.md` locked mechanic, D22/D27), so there's no hook for a slot-swap today. Logged as the cleanest available precedent for a flaw-for-perk exchange that needs **zero** point economy, should Settlements ever add a Traits layer independent of the Skill-per-tier system.

---
## Tasks — three flat difficulty tiers, and a ratchet that punishes repeated failure

**Type:** *(cross-cutting — Movement, Detection, Combat all route through this)* · **Take:** ⚠️ avoid — conflicts with a standing Settlements preference

*"Tasks can be broken down into Easy, Regular and Hard"* at **3+ / 5+ / 8+** respectively, with situational escalation — *"If an enemy is within close range or within an enemy move, move the Task difficulty up one level"* — and a failure ratchet: *"Failing a Task without rolling a 1, makes the Task one level harder the next try… If they fail again, the barricade was well built and it will take a 10+ on all subsequent attempts."* **[FACT — p.19]**

**Why it's flagged, not just logged.** This is a genuinely well-built three-tier difficulty system with a memorable escalation rule attached — the mechanism is fine on its own terms. But Settlements has an existing, explicitly stated preference against exactly this shape: *"Keep all stat tests binary pass/fail against the flat TN 7+ mechanic. Do not add per-task difficulty modifiers — trivial actions (pushing a button) auto-pass, everything else is a straight 7+ test. Ross has pushed back on added test complexity repeatedly."* (`AGENTS.md`, Learned User Preferences). Fistful of Lead's Task system is a tiered-difficulty system by definition — this is exactly the shape that's been rejected here before, for reasons unrelated to whether Fistful of Lead does it well.

**For Settlements.** Nothing to adopt — logged specifically so the next researcher who finds a nice tiered-task system doesn't re-propose the same rejected shape. If a good idea is ever wanted from this section, it's the narrower one: the escalating-failure ratchet (a failed attempt makes the *next* attempt at the *same object* harder) is a separable idea from "difficulty has three published tiers" and could in principle attach to a flat single-TN system — but that's a repackaging, not what's published here, and isn't proposed as a ruling in this note.

---
## Hiding and Spotting — a real stealth mechanic, where Zona Alfa found none

**Type:** Detection · **Take:** ⭐ steal

*"You may use an action to hide if your miniature is in terrain or cover. The miniature cannot hide if there is an enemy within line of sight… Once concealed, the miniature cannot be targeted by an attack, unless spotted by an enemy by making a Hard (8+) Task roll. The enemy must be within 12" to make this roll and have line of sight to the hiding place. A hidden miniature is automatically spotted if an enemy is within 6"."* **[FACT — p.20]** Breaking concealment is absolute and immediate: *"While hidden they are immediately revealed if they move or perform any other action like shooting."* Re-hiding requires first breaking line of sight entirely — closing the loophole of shoot-then-reconceal in the same activation. **[FACT — p.20]**

**Why it works.** Three clean states (hidden-and-safe / auto-spotted-at-close-range / spotted-by-a-roll-at-medium-range) cover the whole design space with one Task roll and two distance bands, no separate noise or detection track needed. Any action at all breaks it — there's no partial stealth to argue about.

**For Settlements.** This is a genuine, checked answer to the open **stealth and noise** question — the same genre-adjacent search that found nothing in [[Zona Alfa#Stealth and noise — searched for, and it isn't here]]. The distance-banded auto-spot / roll-to-spot / can't-be-targeted-at-all structure is a clean, minimal template: a Hard (8+)-equivalent roll within a "near" band, automatic detection within a "very near" band, full immunity beyond both. Directly worth weighing against whatever shape the open stealth question eventually takes, since it needs no new resource track — only a state flag and one roll.

---
## Retreat — triggered by comparing two counters, no roll required

**Type:** Morale · **Take:** ⭐ steal

*"If a miniature has MORE Shock markers than Wounds left it must Retreat. The retreating miniature must immediately fall back away from the enemy 2 moves. This move ignores any terrain (other than impassable) or Shock penalties as the figure runs away."* Afterward, *"remove all the excess Shock so that the number of Shock markers equals the number of Wounds left on the miniature."* **[FACT — p.18]**

**Why it works.** No morale test, no extra die — the trigger is a pure comparison between two trackers the game is already maintaining (Shock vs. remaining Wounds). It self-resolves too: the forced move burns off exactly the excess Shock, so the model comes out the other side of its own panic run at a stable, playable state rather than needing a separate recovery step.

**For Settlements.** [[Morale]]. This is a genuinely elegant answer to "how do you force a withdrawal without a new roll" — worth comparing against however Stress currently escalates into a forced-Break state. A pure counter-comparison (Stress exceeds remaining Wound capacity, or some Settlements-native equivalent pairing) costs nothing new to track if the two numbers are already being tracked separately, which per the locked rules they are (a hit wounds *or* delivers Stress, never both).

---
## The unified Wound Chart — one roll, one table, escalating with existing damage

**Type:** Combat · **Take:** 📎 reference — convergent validation, different shape than our own rule

Every hit — Shooting, Close Combat, or a fall — resolves on one table: *"0 or less: No effect · 1-5: Shock · 6-8: Wounded & Down · 9-10+: Out of Action,"* with *"A +1 … added to the die roll for each Wound already sustained."* **[FACT — p.15]** Three Wounds is always Out of Action, regardless of path. **[FACT — p.15]**

**Why it works.** One table produces all four outcomes (nothing / Shock / Wound / OOA) off one roll, and the existing-Wounds bonus means a model that's already hurt gets meaningfully more fragile on every subsequent hit without a separate rule for it — the escalation is baked into the same +1-per-Wound line that already exists for other purposes (movement and to-hit penalties use the identical count).

**For Settlements.** [[Damage]], [[Morale]]. This satisfies the same "every hit does something" instinct Settlements already has locked, but by a different route: Fistful of Lead puts Shock, Wound, and Out-of-Action **on one table with one roll**, where Settlements' locked rule is a **branching dichotomy** (a hit wounds *or* delivers Stress, never both, off a to-injure roll separate from the to-hit roll). Both are legitimate, independently-reached solutions to "nothing should be a total whiff" — worth citing alongside [[Zona Alfa#Ranged Combat — the Armor Save decouples the hit from the wound]] as a second convergent example, not as a case for changing the current split-roll structure.

---
## Renown — one currency doing reroll, recruitment, upgrade, and campaign-end all at once

**Type:** Economy · **Take:** ⚙️ adapt

Renown Points are earned from scenario objectives (never from Survival scenarios) and traits, and spend four different ways: as an in-game reroll on a strict 1-for-1, once-per-turn basis (*"You can't reroll a reroll"*); to replace a dead or missing Gang member (Sidekicks 5 RP, Regulars 4 RP, Rabble 3 RP — no listed cost for a Leader, who can only be replaced by promoting the Sidekick); to buy an extra Trait for an existing member at double its normal cost; and, once a player banks 20 unspent Renown, to trigger the campaign's final battle: *"Once a player has acquired 20 points of unspent Renown, he may call for a Showdown with his Campaign opponent… This is a winner-take-all final battle to the death."* **[FACT — p.35, p.47]**

*(One small, honestly-flagged wording inconsistency: the trait-purchase-cost line reads **"8 RPs, 10 for a Specialist and 14 for a Leader"** — but no role called "Specialist" exists anywhere else in the roster, which is Leader/Sidekick/Regular/Rabble. Almost certainly means Sidekick. [FACT — as printed, p.35; the inconsistency is the book's, not this note's.])*

**Why it works.** One number is simultaneously a tactical in-game resource, a roster-repair currency, an upgrade currency, and the player-chosen trigger for the campaign's own ending — four jobs off one tracked value, with no conversion step between any of them.

**For Settlements.** [[Economy]], [[Campaign]]. Settlements' **Credits** already carries the "one number, one job description" role for roster cost (`AGENTS.md`: *"the Credits you field are your Crew Rating"* — never a second currency), so Renown isn't a literal analogue of Credits; it's closer kin to a **reward/reroll currency layered on top of a roster that's already priced some other way** — precedent for a single number doing double duty as both a tactical resource and a campaign-progress tracker, worth remembering if a Settlements campaign layer ever wants one number to do more than one job rather than adding a second tracked resource. The **player-chosen 20-Renown Showdown trigger** is also a third data point (after [[Zona Alfa#The Stalls, and the 10,000 Ruble Plan]] and [[Trench Crusade#The published threshold ladder]]) on "does the campaign end on a fixed schedule or when a player decides" — this is squarely in the *player decides* camp, same as Zona Alfa's retirement fund, and the opposite of Trench Crusade's escalating ladder.

---
## Rabble — three bodies on one activation card

**Type:** List · **Take:** ⚙️ adapt

*"Rabble function just like normal models except they use an 8-sided-die (d8) and only have 1 Wound… The flip side is you get 3 for the price of one model. They all activate on one card, so only deal one card for each Rabble 'group'… Normally, you may only have one group of Rabble in your gang, and they get only 1 trait, which they all share."* **[FACT — p.24]** They still act as individuals once activated — different targets, different actions — and even share bonuses from the same Special Card: *"If a Seven Special Card were to be used to Activate, each Rabble gets a re-roll this turn."* **[FACT — p.24]**

**Why it works.** It buys headcount without buying activation-tempo: three extra bodies would normally mean three extra cards in a hand (and three chances at good Special Cards), but Rabble collapses that back down to one draw, at the cost of a worse die and a single shared Trait. The books limits the trick to exactly one group per gang, which caps how far the tempo-for-quality trade can be pushed.

**For Settlements.** [[List Building]]. Directly relevant if Settlements ever wants a cheap-mass unit type that doesn't proportionally inflate whatever the activation-economy cost of "one more model" already is — the pattern here is specifically **"group activates together, but resolves as individuals,"** which is a different shape than a single multi-wound blob unit. Worth weighing the headcount-vs-tempo trade this buys against Settlements' own rank-based Orders economy (Recruit/Fighter get 0 Orders; only Specialist/Leader grant 1–2).

---
## What it gets wrong

**Type:** *(cross-cutting)* · **Take:** ⚠️

- **There is no costed force-build system anywhere in the book.** **[NOT FOUND — checked the full Building Your Gang, Traits, Negative Traits, Gang Traits, and Weapons chapters; roster size and composition are fixed role-slots (Leader/Sidekick/3 Regulars, or a Rabble group in a Regular's place), not a points list.]** There is nothing here to derive a formula from — a genuine, checked negative result, not a gap in the read.
- **The Trait list has no stated weighting, and it shows.** Quick (+1" move) and Two Gunned (an entire second combat mode, Burst fire, near-immunity to Out of Ammo) sit in the same undifferentiated list with no price or tier separating them. **[INFERENCE — read directly against the full ~50-entry Trait list, p.25-29; no weighting scheme is stated anywhere.]** This is the same coarse-list failure mode flagged in [[Song of Blades and Heroes#The Quality multiplier]]'s "known weakness" — except there, at least, a formula exists to catch the worst cases; here, nothing does.
- **The Task escalation ratchet has no stated floor or reset.** A twice-failed Task locks at "10+ on all subsequent attempts" **[FACT — p.19]** with no rule for ever lowering it again — a permanently-unsolvable Task is possible as printed, which is a real design smell even in a game this informal.
- **Rabble's activation-tempo advantage is entirely uncosted**, because nothing in this game is costed. Three bodies on one card is a genuine tactical edge (see above) that exists purely as a role-slot substitution with no accounting for the tempo it buys back — fine in a book this light, but it wouldn't survive being ported into any system that does price activations.

---
## Source

- Primary: *Fistful of Lead: Reloaded, 2nd Edition*, Jaye Wiley, Wiley Games, 2024
- Capture: `research/sources/fistful-of-lead/source.md` (full 62-page verbatim extraction; `research/sources/fistful-of-lead/meta.json` for provenance and hash)
- Related: [[Wargaming Research Hub]] · [[Zona Alfa]] · [[BLKOUT]] · [[Spectre Operations]] · [[Song of Blades and Heroes]] · [[The Rampant line]] · [[Trench Crusade]] · [[Necromunda and Mordheim]]

---
*Add one row per mechanic to [[Wargaming Research Hub]] when this note is finished.*

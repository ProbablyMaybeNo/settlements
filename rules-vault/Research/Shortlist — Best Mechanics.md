---
type: research-shortlist
title: Shortlist — Best Mechanics
tags: [settlements/research]
status: Living
updated: 2026-08-22
---
# 🥇 Shortlist — the best mechanics for Settlements

> **What this is.** A curated pass over all **235 mechanics** in [[Wargaming Research Hub]], filtered to the ones that genuinely earn a place in **Settlements battles** and **the campaign/persistence layer**. 121 were tagged ⭐ steal; these are the ones that survived a second, harder cut.
>
> **What this is not.** **Nothing here is adopted.** This is a candidate list for Ross to rule on. Adoption happens in [[Full Rules System v1]] and nowhere else.

> [!info] The filter used
> Every entry had to clear four bars:
> 1. **Engine-compatible** — works with `1d10 + Stat + mods vs 7+`, the **±3 modifier cap**, and **no second dice type anywhere**.
> 2. **Cheap** — earns its rules text and its table time. Anti-bloat is a locked tenet, and this is where it bites hardest.
> 3. **Solves a stated open problem** — not merely clever in someone else's game.
> 4. **Not already in the rules.** Where we've already adopted something, it's noted rather than re-pitched.
>
> Things that failed the bar despite being excellent: card-driven activation ([[Fistful of Lead]] — a deck is a second randomiser), the Quality Die (same), Infinity's full hacking suite (correct, unaffordable), tiered task difficulty (ruled against repeatedly).

---
## ⚔️ Battles — the top eight

### 1. The living board, as one system ⭐⭐⭐
**[[Zona Alfa#Mission Objectives and Hot Spots — the Reaction Radius, and triggering a fight from range|Hot Spots + Reaction Radius]] · [[Zona Alfa#Zone Hostiles — Threat Level spawn scaling, and a four-rule AI|Zone Hostiles]] · [[Last Days Zombie Apocalypse#The Menace Phase — shooting creates the zombies that punish shooting|the Menace Phase]] · [[The Walking Dead All Out War#The neutral threat|scale it to the game]]**

The single highest-value cluster in the vault, and the four pieces compose into one mechanic:

- **Objectives and loot are area triggers** with a printed **3″ Reaction Radius**. Engaging loot always spawns a fight first.
- **Spawned hostiles run four rules in strict order** — 12″ leash from the location, nearest visible model, melee-only aggro pull, opposing player controls them. Seven reskinnable archetypes cover an unlimited bestiary.
- **Shooting manufactures its own threat**: every shot drops a Noise Token, and next turn `1D6 + tokens` vs a target spawns more. No generator to bookkeep.
- **The threat is costed against the game, not either crew**, so a bigger fight is not a safer fight and nobody buys the danger out of their own list.
- And the piece that turns it tactical: **a model can throw a Bolt into the radius to trigger it remotely**, baiting the swarm onto a rival crew.

**Why it's the best.** It answers the [[Ideas Inbox]] "boards that feel alive" want completely, it's **positional rather than purchased**, and both crews can weaponise it. Three independent designers ([[Zona Alfa]], [[Last Days Zombie Apocalypse]], [[The Walking Dead All Out War]]) converged on *ordered rule list beats random table* for the AI.

**Touches:** [[Scenarios]] · [[Events]] · [[Terrain Interaction]] · [[Territory]]
**Cost:** a spawn table per territory type, and marker discipline. **The objection:** this is the biggest single addition on the list, and marker load is already our silent threat to pace.

---
### 2. States of Awareness — one track, three jobs ⭐⭐⭐
**[[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll]]**

Three named states — **Unaware / Uneasy / Alert** — and the state simultaneously gates the action pool, the Stress floor, **and which actions are legal at all.** An Unaware element can only take Unaware actions.

Paired with an **asymmetric audio rule**: an unsuppressed weapon makes *every* enemy Alert immediately with **no roll at all**; a suppressed one only gives them a roll to hear it, modified by range band.

**Why it's the best.** Stealth has come back thin three times ([[Zona Alfa]] had **nothing**, [[Mad Dogs with Guns]] one roll, [[Fistful of Lead]] a decent three-state version). This is the only complete answer found, and a suppressor changing *whether a roll happens* rather than modifying a number is exactly the kind of rule that costs one sentence.

**Touches:** [[Morale]] (the Stress link is free) · [[Shooting]] · [[Weapons]] (a `Suppressed` property) · [[Solo & Co-op]]
**Cost:** one state token per crew, not per model, if we scope it to the crew.

---
### 3. Detection prices movement ⭐⭐⭐
**[[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll|Spectre]] · [[BLKOUT#Reactions — the beating heart|BLKOUT]]**

**+2 to spot anyone who moved fast this turn.** Spectre gives a flat bonus to detect a target that spent more than one point of its action pool moving; BLKOUT only triggers Overwatch on a move longer than **half** the Movement Value.

**Why it's the best.** *Moving fast is what gets you seen* — two unrelated games reached it independently, it converts movement **distance** into a live tactical dial, and it costs one clause. **We already adopted the BLKOUT half.** The Spectre half — speed feeding *detection* as well as *overwatch* — is the free extension.

**Touches:** [[Movement]] · [[Shooting]]

---
### 4. Wound Severity by margin of failure ⭐⭐⭐
**[[Spectre Operations#Wound Severity by Margin of Failure]]**

A failed injury roll's **own margin** selects the outcome — miss by 1 / 2 / 3+ picks Incapacitated / Minor Injury / Narrow Escape. **No second table, no second roll.** Counter-intuitively inverted: failing by *1* is the worst result, because a near-miss on the threshold means the shot nearly killed you.

**Why it's the best.** Our engine already computes a margin on every `1d10 + Stat vs 7+`. **The information is sitting there unused.** This is the cheapest possible route to granular injury — and it's the one entry here that costs *negative* rules text, because it can replace a roll rather than add one.
*(Note: it's an optional rule in the source.)*

**Touches:** [[Damage]] · [[Progression]]

---
### 5. Retreat off two counters you already track ⭐⭐
**[[Fistful of Lead#Retreat — triggered by comparing two counters, no roll required]]**

If Shock exceeds remaining Wounds, forced withdrawal fires **automatically — no morale roll** — and the move burns off exactly the excess as it resolves.

**Why it's the best.** We already track Stress and WND. This is a morale outcome with **zero new dice and zero new tokens**, and the self-clearing move is elegant. Compare [[Last Days Zombie Apocalypse#Breaking Point — group morale keyed to casualties taken, not damage dealt|Last Days]], which proves a group-level circuit breaker can coexist with per-model fear without the two colliding.

**Touches:** [[Morale]] · [[Damage]]

---
### 6. Lean Out ⭐⭐
**[[BLKOUT#Lean Out]]**

Spend **half your move** to place a marker and peek. Enemies who can only see the *marker* treat it as the model, and the leaner has cover from them. **Lean-only doesn't count as "moving"** for other rules — which is the load-bearing half.

**Why it's the best.** It models the most common real infantry action — exposing the minimum of yourself to see and shoot — for one marker and one sentence, and creates a real decision that costs tempo rather than dice. **Not yet adopted**, unlike its two BLKOUT siblings.

**Touches:** [[Movement]] · [[Terrain Interaction]]

---
### 7. Elevation demotes Cover by one tier ⭐⭐
**[[Zona Alfa#Movement, field of view, and layered Cover]]**

An attack from higher ground drops the target's Cover a **full tier** — Heavy → Light → none.

**Why it's the best.** One sentence, and it makes **terrain density** — our single most powerful balance dial, worth a measured 66-point win-rate swing — do more work without adding a feature to the board. High ground becomes mechanically worth taking, not just a better view.

**Touches:** [[Terrain]] · [[Shooting]]

---
### 8. Capturability as a weapon property ⭐⭐
**[[Judge Dredd Miniatures Game#The Stun/Injury fork — capturability as a weapon property, not a coin-flip]]**

A knockout is tagged **Stun or Injury by the weapon that caused it** — not by range, not by a post-battle roll. Only an Injury tag risks death; a Stun-only knockout risks capture instead.

**Why it's the best.** We already have a full **Captured** thread on the Fate table (§26.3a — Recruits and Fighters only, with Ransom and Brainwash in Downtime). What we lack is *agency over it.* A `[Non-Lethal]` weapon property makes taking prisoners a **loadout decision** made before the battle, instead of an accident of how a wound resolved.

**Touches:** [[Weapons]] · [[Campaign]] · [[Damage]]

---
## 🏛️ Campaign & persistence — the top ten

### 1. Growth widens the menu, never the budget ⭐⭐⭐
**[[Oathmark#The kingdom widens the menu]]** · independently confirmed by **[[Necromunda Campaigns]]**

Oathmark's core rulebook, p82 — *a printed rule, not a designer aside*: **"Every game you play has a fixed number of points you can spend."** The kingdom generates *"a list of available figures"* — a menu, never a bigger budget. A 20-territory kingdom and a 10-territory kingdom field the same points.

**And Necromunda agrees independently:** settlement size never feeds the fielded gang.

**Why it's the best.** It is *the* rule that makes a persistent base safe to bolt onto a points-buy game, and it is now confirmed by two unrelated published games. It settles what [[Settlement]] growth should pay out: **unlocks, not budget.** It's also already our locked principle — this is the external proof.

**Touches:** [[Settlement]] · [[Structures]] · [[Territory]] · [[List Building]]

---
### 2. One Location choice sets three permanent ceilings ⭐⭐⭐
**[[Necromunda Campaigns#Settlement Locations — one choice caps three structure categories independently|Necromunda Outlander]]**

Pick where your settlement sits. Each Location is rated **Defence / Resources / Toxicity, 1–6**, and that one locked choice caps **three separate structure categories independently and permanently.** The trade is printed in the book: *"the more desolate the starting location, the easier it will be to defend, though the poorer its Materials will be."*

**Why it's the best.** It is the strongest settlement-shape mechanic in a **five-way** comparison ([[Oathmark]] / [[Last Days Zombie Apocalypse]] / [[Fallout Wasteland Warfare]] / [[Mordheim]] / Necromunda). One decision, made once, generating a permanent and legible identity — and it uses **our own three nouns**: Settlement, Structures, **Materials**.

**Touches:** [[Settlement]] · [[Structures]] · [[Territory]]
**Note:** our "every structure is a real object on a real board" rule is *stricter* than Necromunda's roster abstraction. That's a deliberate difference, worth keeping consciously.

---
### 3. Slots bind, money only decides when ⭐⭐⭐
**[[Last Days Zombie Apocalypse#Empty Spaces is the real constraint]]** · **[[Gaslands#Points plus an unbuyable capacity]]** · **[[Fallout Wasteland Warfare]]**

**Empty Spaces (2–10) is the binding limit**, not cash. Built-in perks never consume one; most structures build only once. Gaslands does the same with unbuyable build slots; Fallout does it with *physical area on the layout canvas.*

**Why it's the best.** Income accelerates over a campaign; **slot count doesn't.** A slot cap cannot be optimised around the way a price can — it's what stops a rich crew eventually owning all 23 structures. Three independent games, same answer.

**Touches:** [[Settlement]] · [[Structures]] · [[Economy]]

---
### 4. Keep the settlement out of ordinary battles ⭐⭐⭐
**[[Last Days Zombie Apocalypse#Keep the base out of ordinary battles]]**

Of ~16 base upgrades, **only two touch a normal away game.** Everything else is economy, or fires only in the one scenario where your base is on the table.

**Why it's the best.** It's what lets the settlement layer be as deep as you like **without slowing down or unbalancing the firefight** — and it's the same instinct [[Oathmark]] reached from the opposite direction. Given our pace target and the marker-load risk, this is a discipline to adopt as a *design constraint*, not a mechanic: *a structure pays out in [[Downtime]], or in a raid on your own settlement — not in a territory battle.*

**Touches:** [[Structures]] · [[Downtime]] · [[Settlement]]

---
### 5. Capability is leased, not owned ⭐⭐⭐
**[[Last Days Zombie Apocalypse#Structures own their unlocks]]**

*"Stable unlocks 0–2 Horses at 15 SP each, and **losing the Stable removes the Horses from the roster**."*

**Why it's the best.** This is the **enforcement mechanism** the crafting want needs. If structures unlock craftable equipment tiers, then losing the structure has to cost you the unlock — otherwise raids on a settlement never really hurt, and the settlement layer is a ratchet. It also gives raids a target that isn't a body.

**Touches:** [[Structures]] · [[Settlement]] · [[Weapons]]

---
### 6. A published ceiling ladder, plus a separate headcount cap ⭐⭐⭐
**[[Trench Crusade#The published threshold ladder]]**

Everyone's budget ceiling rises on the **same printed schedule** (700 → 1800 over 12 battles) **regardless of who is winning** — and a **separate Max Field Strength track** caps model count independently, so a rising budget cannot simply be converted into bodies.

**Why it's the best.** It removes the single largest snowball source we have measured evidence for: [[Necromunda and Mordheim#Play frequency beats skill|a 100,000-run simulation put campaign income at 750 credits at one game a week versus 1,170 at two]]. **Schedule, not skill, is the real snowball** — and a fixed ladder makes frequency affect *progress rate* rather than *power*. Settlements persists outside campaigns by design, which is exactly the exposed structure.

**Touches:** [[Campaign]] · [[List Building]] · [[Progression]]

---
### 7. An opt-in rubber band with a real price ⭐⭐⭐
**[[Trench Crusade#The rubber band you choose]]**

To rebuild to the threshold you must forego the Exploration Phase, sell all unassigned gear, and **empty your treasury**.

**Why it's the best.** Catching up is **always available and always costs the upside phase — and the losing player chooses it.** Nobody is handed charity and nobody is punished for winning, which is the failure mode of every automatic handicap. It composes directly with our [[Downtime]] three-phase turn, because foregoing a phase is a cost we can already express.

**Touches:** [[Campaign]] · [[Downtime]]

---
### 8. Rating is a snapshot; the stash is a separate number ⭐⭐⭐
**[[Necromunda#Gang Rating vs Wealth — two numbers, confirmed the same way across 28 years]]**

Stashed gear **does not count toward rating** — stated word-for-word in **both the 1995 and the 2023 rulebooks**, four independent statements 28 years apart. N23 goes further and promotes the excluded pile to its own named stat, **Wealth**.

**Why it's the best.** *Ownership is wealth; rating is fielded power.* It's what makes underdog banding work at all, it settles our open **Armoury fork**, and it's the most durably-verified claim in the entire vault. The N23 refinement is the actionable bit: **track it as a second visible number** rather than leaving it implicit.

**Touches:** [[List Building]] · [[Economy]] · [[Campaign]]

---
### 9. The veteran fork — and the third option that dissolves it ⭐⭐⭐
**[[Oathmark#Two prices for one veteran, spent not stored]]**

Four games disagree on how to stop veterans snowballing. [[Trench Crusade#Cap the veterans, don't tax them|Trench Crusade]] **caps** and never re-prices. [[The Walking Dead All Out War#Re-pricing veterans|TWD]] and [[Spectre Operations]] **tax** and never cap. Our current design taxes (+2 per Advance).

**Oathmark does both — cap at 3 *and* +10% compounding, verified 418 → 460 → 506 → 557** — and gets away with it because of a third element: **veteran power is a reroll token that fully refreshes each battle, never a permanent stat.**

**Why it's the best.** It converts an either/or into a design rule: **pick one valve — unless the veteran benefit is spend-not-store, in which case you can afford both.** That's a genuinely new option on a fork that has been open in this project for months.

**Touches:** [[Progression]] · [[Campaign]] · [[List Building]]

---
### 10. Deals with a hidden break check ⭐⭐⭐
**[[Necromunda Homebrew Campaigns#Striking a Deal — a one-roll table with a hidden hedge for betrayal|Striking a Deal]] · [[Necromunda Homebrew Campaigns#The Meet and the Double-Cross — betrayal staged as a scenario, not a narrated event|the Double-Cross]]**

Two leaders meet; **one open D6** sets the tier (refused / one scenario / long-term). But the **break check is rolled in secret by an impartial third party** — neither player knows whether betrayal is coming. And betrayal isn't bookkeeping: it resolves as **an actual scenario**, with a hidden ambusher or a hidden traitor, and a real chance both duped crews shoot *each other* by mistake.

**Why it's the best.** [[Diplomacy]] is one of three unfinished notes in the campaign layer and had **nothing** behind it across 235 mechanics. This is cheap, engine-compatible, and the secret-third-party roll is the piece that makes an alliance feel genuinely unsafe. ⚠️ `[COMMUNITY]` — fan-made, never commercially playtested.

**Touches:** [[Diplomacy]] · [[Campaign]] · [[Scenarios]]

---
## 🥈 The next five — strong, and cheaper than the top ten

| Mechanic | Source | Why it's here |
|---|---|---|
| **Splinter gangs** — a Champion leaves with gear, Advances and injuries and founds a new crew | [[Necromunda Campaigns#Splinter gangs — the one persistence mechanic every book keeps\|Necromunda]] | **Reprinted near-verbatim three times in seven years** with no cross-reference — the most stable single idea in the genre, and a real answer to per-unit persistence |
| **"The lad's got talent"** — a henchman advance roll of 10–12 promotes one model to Hero, keeping all accumulated XP and stat increases | [[Mordheim#Lads Got Talent — henchmen graduate into heroes\|Mordheim]] | A promotion path built **entirely from existing advance-roll machinery** — zero new rules, and it creates attachment for free |
| **Glory** — a second currency earned only by named deeds, **first-come-first-served** | [[Trench Crusade#Glory]] | The mechanical shape our Glorious Deeds want has been reaching for. The once-per-campaign claim is what makes it self-limiting. ⚠️ Watch the one-economy tenet — this must not become a second *purchasing* currency |
| **One downtime action per surviving fighter** | [[Necromunda Homebrew Campaigns#The post-battle action — one downtime action per surviving fighter]] | Forces a real per-model trade-off — injury care *or* income *or* training — instead of doing every downtime task every turn. Lands straight on [[Downtime]] |
| **Linked territory boons** — each territory lists 1–2 linked ones; holding the pair upgrades the payout | [[Necromunda Campaigns#Linked Rackets — boons that chain into a synergy graph]] | Turns territory-hunting from a **count** into a **targeting problem**, for one extra field per card |

---
## ✅ Already in the rules — don't re-pitch these

| Mechanic | Where it landed |
|---|---|
| Active dodge ([[BLKOUT]]'s Juke) | Adopted as **Dodge** — opposed AGI vs DEX |
| Move-half-to-dodge-Overwatch | Adopted — distance-gated Snap Shot |
| Sequential shoot-back | Already **Snap Shot**; BLKOUT's *simultaneous* Return Fire was evaluated and **cut** as too swingy |
| Two currencies that never convert | Locked — Credits buy bodies and gear; **stats and skills are never charged** |
| Lasting injury tables | Drafted as the **Fate table** — and [[Mordheim]] confirms **Captured** and **Hardened** are inherited names |
| Every hit does something | Locked tenet, and [[Last Days Zombie Apocalypse#Knockback and Shoot Them in the Head — the zombie's own wound/no-wound split\|Last Days]] and [[Spectre Operations]] both converge on it independently |

---
## ⛔ Deliberately not on this list

- **Card-driven activation** and the **Quality Die** ([[Fistful of Lead]]) — both good, both a second randomiser. A held hand's hidden information is precisely what a public d10 cannot reproduce. Structural dead end.
- **Infinity's full hacking suite** — and [[Infinity#Three editions of simplification — N3's five program families collapse into N5's two|Corvus Belli has spent three editions shrinking it]]. [[Fallout Wasteland Warfare]]'s hacking is *one sentence*. Two sources say our thin [[Hacking]] layer is right-sized.
- **Tiered task difficulty** — ruled against repeatedly; flat TN 7+ stands.
- **Per-resource upkeep** — [[Last Days Zombie Apocalypse#Zero upkeep in the core game, four tracked conditions in Seasons|the core game tracks none at all]], and the optional supplement that adds it costs three ordered lists resolved after *every* encounter. Evidence for the Water/per-head cut, not against it.
- **A second spendable currency to fix a dead stat** — a homebrew designer diagnosed Reputation as *"pretty much meaningless after a point"* and cured it the one way our one-economy tenet forbids. Symptom logged, cure rejected.

---
*Curated from [[Wargaming Research Hub]] — 235 mechanics, 32 sources. Coverage status in [[Library Coverage]]. Sourcing queue in [[Candidate Games]].*

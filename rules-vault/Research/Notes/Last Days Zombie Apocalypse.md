---
type: research-note
title: Last Days - Zombie Apocalypse
game: Last Days - Zombie Apocalypse
publisher: Osprey Games
designer: Ash Barker
depth: primary — core rulebook + Seasons supplement, both read in full (148k + 119k characters), full second pass covering core resolution, turn structure, the zombie horde, noise, injury, and solo/co-op
tags: [settlements/research]
---
# 🎲 Last Days: Zombie Apocalypse

> [!abstract] In one breath
> Survivors, scavenging, a home base and a persistent roster — **the closest thematic match to Settlements in the entire corpus**, and the best settlement/upkeep design found. Its **Refuge costs zero points**, sits entirely outside the crew budget, and is fully described by three numbers. A second full pass adds the rest of the game: a Menace Phase where **the players' own shooting spawns the zombies that punish shooting**, a four-rule zombie AI that converges with two other games in this corpus, and a same-designer natural experiment on upkeep — the core game has **zero** food/water/fuel tracking, and only the paid *Seasons* supplement puts it back in, at real table-time cost.

| | |
|---|---|
| **Designer · publisher** | Ash Barker · Osprey (+ the *Seasons* campaign supplement) |
| **Creation budget** | **100 Scavenge Points**, spent once |
| **The base** | **Free.** Outside the budget entirely |
| **Depth of read** | **Primary** — both PDFs read in full, twice (settlement layer, then everything else) |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.17 ⭐ |

---
## Why it's here

Same genre, same fantasy, same shape as Settlements — and it makes the **opposite** structural choice to [[Oathmark]] on the budget question, which makes the pair unusually instructive read together. Oathmark holds points equal forever; Last Days abolishes the per-game budget entirely after creation. Both work.

The first pass through this book only mined the settlement/Refuge chapter. This pass reads the rest: core resolution, the turn, the zombie horde as a system, noise, scavenging, injury, the *Seasons* weather cycle, and solo/co-op — the parts of Last Days that make it, mechanically, the single closest analogue to Settlements in the whole research corpus.

---
## Core resolution — 1D6 + Stat vs a movable TN, except combat, which is nailed to 7

**Type:** Core · **Take:** 📎 reference — and one half of it is a pattern we've already rejected

Last Days runs on a plain **1D6**, not a d10 or d20, and every stat runs 0–6 (only Action Points go higher). **[FACT, p.10]** General Tests use a bespoke target number chosen per task — the book's own example is *"Intelligence/8"* — so task difficulty is modeled by moving the number, not by modifying the die. Opposed Tests (most CQC, most Horror/Courage checks) have both sides roll 1D6 + stat; ties go to the higher characteristic, and if that's still tied, *"it goes to the Character that did not initiate the Test (the defender)."* **[FACT, p.10]**

Combat itself is the exception: **Firearms and CQC tests are both pinned to a flat "Lucky 7s" target of 7**, regardless of the attacker's stat. **[FACT, p.52, p.55]** The two things that happen dozens of times a battle get one memorized threshold; everything else gets a designer-tunable number.

**Why it works.** It cleanly splits the design space — general adjudication (pick a lock, forage, negotiate) is allowed to have per-task difficulty, while combat, which repeats constantly, is standardized so no one looks up a number mid-firefight.

**For Settlements.** Ross has already ruled the opposite way on the general-Test half of this: *"Keep all stat tests binary pass/fail against the flat TN 7+ mechanic. Do not add per-task difficulty modifiers — trivial actions auto-pass, everything else is a straight 7+ test."* Last Days' variable-TN Test format is exactly the pattern already rejected here — recording it so it doesn't resurface later looking like untested genre convention. Where it **does** converge with us: the tie-goes-to-the-defender rule on opposed tests is identical to our own locked convention (*"ties go to the defender"*) — an independent designer arriving at the same answer is a small but real validation.

---
## The Menace Phase — shooting creates the zombies that punish shooting

**Type:** Turn Structure / Neutral Threat · **Take:** ⭐ steal

Every turn opens with a phase in which the players have almost no agency. **[FACT, p.38-44]** In order: **Noise Tokens** resolve, then **Ammo Tokens**, then **all zombies activate** — a full "turn within a turn" — all *before* either side moves or shoots that turn.

Every Rate-of-Fire point a model spends shooting drops a Noise Token on it. In the *next* Menace Phase, that model rolls `1D6 + accumulated Noise Tokens`; on a **7+** it draws a fresh zombie onto the table at the edge nearest itself. *"Any model that achieves a total of 7 or higher will draw a zombie to the battlefield."* **[FACT, p.39]** At 6+ tokens a zombie is summoned automatically and a second roll is made against the excess. Ammo Tokens run the identical two-step engine off the same trigger (a RoF point spent) but check against the weapon's Reload Number instead of a flat 7, and — per the book's own contrast — persist until the gun is actually reloaded, *"Unlike Noise Tokens, Ammo Tokens are only removed once a gun is reloaded."* **[FACT, p.53]** The text never states explicitly when Noise Tokens themselves clear; the contrast implies they're spent each Menace Phase regardless of outcome. **[INFERENCE]**

**Why it works.** One player action — firing a gun — produces two consequences from a single die roll's worth of bookkeeping: you might miss, and either way you might just have rung the dinner bell. The threat is manufactured by the players' own tactical choices rather than rolled off a neutral generator — the same instinct as [[Zona Alfa#Zone Hostiles — Threat Level spawn scaling, and a four-rule AI]]'s Threat Level track, achieved here with nothing more than a die sitting next to the model.

**For Settlements.** Touches [[Initiative & Activation]] and any future noise/detection layer. If Settlements ever wants a neutral-threat or stealth system, this is the cheapest version found in the corpus so far: don't build a new spawn table, make the thing already being tracked (shots fired) double as the spawn trigger.

---
## Noise as an attribute, not a subsystem

**Type:** Stealth · **Take:** ⭐ steal

Noise isn't confined to the Menace Phase math — it's a first-class weapon/equipment/Character **attribute**, `Noisy X`, stacking flat additional tokens onto the exact same shared counter. **[FACT, p.72]** A Motorcycle carries `Noisy 3` just for existing each Menace Phase; the Gather Fuel Job's Chainsaw option adds +3 Fuel but subtracts 2 from the *next* Zombie Attack roll for the racket made cutting wood. **[FACT, Seasons p.38]**

Exactly one skill answers it — **Stalker**: *"They do not generate Noise Tokens when they run."* **[FACT, p.71]** One skill, one clean counter to one attribute, not a parallel stealth roll.

**Why it works.** Noise is never a separate mini-game bolted onto the side; it's additive tags on the same token pool everything else already writes to.

**For Settlements.** Direct evidence for the [[Ideas Inbox]] stealth/noise want. Set against the other three data points in this corpus: [[Zona Alfa#Stealth and noise — searched for, and it isn't here]] (nothing at all), [[Mad Dogs with Guns#Hiding, Creeping, and noise — the stealth mechanic Zona Alfa didn't have]] (a dedicated roll), and [[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll]] (a full alert ladder). Last Days sits at the cheap end of that range — noise-as-attribute is the lightest-weight implementation found so far, and the one that would cost the least rules-surface to adopt.

---
## Zombie AI in four rules, and Sticky Horror instead of a morale check

**Type:** Neutral Threat / AI · **Take:** ⭐ steal

The zombie AI is four rules, checked in strict priority order. **[FACT, p.60]**

1. Spend all AP moving toward the **nearest non-zombie model in Line of Sight**, trying to reach Contact.
2. If already in Contact, do nothing — wait to fight in the CQC Phase.
3. If no living model is in LOS, move toward the **closest model that generated a Noise Token this Menace Phase**, regardless of LOS, even breaking through doors to get there.
4. If the nearest target is already engaged by another zombie, retarget the **next-closest unengaged model with LOS**; if none exists, treat this as having no LOS at all (fall back to rule 3, then idle).

Instead of a fear/morale roll on contact, Horror vs Courage produces a state the book calls **"Sticky"**: if the zombie's Horror total beats the Character's Courage total, that Character simply *cannot spend Action Points to Break Contact for the rest of the turn.* **[FACT, p.61]** Fear is modeled as an action-lock, not a save-or-flee roll.

**Why it works.** No random walk, no scripted patrol, no separate alert state — the whole horde is deterministic once LOS and Noise are known. "Sticky" replaces an entire sub-roll (does this zombie scare you off?) with a straightforward gate on an action already being tracked.

**For Settlements.** A third data point for the neutral-threat comparison this sweep exists to run. [[The Walking Dead All Out War#The neutral threat]] and [[Zona Alfa#Zone Hostiles — Threat Level spawn scaling, and a four-rule AI]] both land on the same shape — **a short, strictly-ordered priority list beats a random behavior table.** Three unrelated designers converging independently on "four rules, checked in order" is itself the finding: if Settlements ships a neutral threat, that's the validated pattern, not a d66 table.

---
## Knockback and Shoot Them in the Head — the zombie's own wound/no-wound split

**Type:** Combat · **Take:** 📎 reference

Zombies never touch the human Damage Capacity math. A hit from Shooting or CQC instead rolls 1D6: **5–6 destroys the brain and removes the zombie**; **1–4 does nothing to Damage Capacity but adds Knockback Tokens** equal to the weapon's Knockback stat, each token cutting 1 AP from that zombie's *next* activation (5+ tokens and it can't move at all that turn), discarded at the end of its activation. **[FACT, p.44, p.61]**

**Why it works.** Every hit against a zombie does something: it's dead, or it's staggered and arrives a turn later — never neither, and never both a wound that doesn't matter *and* a delay. Resolving the horde's threat through tempo (fewer AP, later arrival) rather than a hit-point race is what lets 20+ zombie models stay cheap at the table: no HP tracked on any of them, just a token count that self-clears.

**For Settlements.** Close kin to our own locked tenet — *"every hit does something: a hit wounds or delivers its payload, never both, and a failed wound becomes Stress."* Last Days reaches the identical shape (binary resolution, no wasted rolls) from the opposite direction: theirs delays the enemy's turn, ours delays the enemy's nerve. Worth citing in [[Damage]] as independent validation that "every hit resolves to exactly one of two outcomes" outperforms a graduated wound track.

---
## Breaking Point — group morale keyed to casualties taken, not damage dealt

**Type:** Morale · **Take:** ⚙️ adapt

Any turn a Group takes at least one casualty, it rolls `1D6 + total casualties taken this game` against `the Leader's Courage + surviving fighter count`. **[FACT, p.57]** Fail, and the whole Group flees and the Encounter ends — if both sides took a casualty that turn and both fail, it's a draw. A Leader may pre-emptively fail this test on purpose from turn 3 onward, if a casualty was taken that round.

**Why it works.** Morale is a single roll for the whole Group, triggered only by a casualty, rather than a per-model check every turn — cheap at the table, and it answers "how much punishment can this crew take before it's over" as one number instead of a cascade of individual checks.

**For Settlements.** Relevant to [[Morale]]. We already run individual Stress/NRV per model; Last Days runs *both* an individual fear mechanic (Sticky Horror, above) *and* this separate Group-level circuit breaker without the two colliding — evidence that a Group-level morale check can coexist with per-model Stress rather than duplicating it.

---
## Zero upkeep in the core game, four tracked conditions in Seasons

**Type:** Economy · **Take:** ⭐ steal the cut / ⚠️ avoid the add-on unless it's explicitly wanted

The **core rulebook has no food, water, or fuel economy at all.** **[FACT — confirmed on the full read]** The core Refuge Perks table (12 Perks total) and the Agriculturalist skill both convert the Fenced-Off Garden's output directly into **Scavenge Points**, never into a food resource. Scavenging is entirely abstracted into one currency and one Supply Token conversion table.

The optional ***Seasons*** campaign supplement — a separate, paid book — bolts on four tracked **Conditions** (Hunger, Health, Thirst, Warmth), each with a Suffering → Critical ladder; any two Conditions simultaneously Critical **kills the Character outright.** **[FACT, Seasons p.10-16]** Running it in earnest costs real table time: a season-by-season schedule of which Conditions must be managed which months (with dice-gated exceptions — *"roll 1D6 in March, on a 1 also manage Cold"*), three new Jobs (Gather Food / Fuel / Water) each with their own dice, a heating formula (`Starting Perks + Empty Spaces = Rooms to heat, 1 Fuel per Room`), a Rest/Medicine recovery mechanic, and — the expensive part — **three separate ordered feeding/warming/watering lists, one per Leader Keyword**, resolved after *every* Encounter for *every* Character in the Refuge.

**Why it matters as evidence.** This is a same-designer, same-game natural experiment. Ash Barker shipped the genre-canonical **zero-upkeep** version as the core game, and only added per-resource tracking two years later as a clearly-optional hardcore module. That is a real data point that the upkeep math is overhead the designer himself judged didn't belong in the default experience.

**For Settlements.** Directly bears on the already-cut Water/per-head-upkeep tenet. **[INFERENCE]** This doesn't prove the cut correct on its own, but it's the closest same-genre precedent available, and it points the same direction already chosen: ship the abstracted version, and if a "hardcore mode" is ever wanted, make it an opt-in module exactly like *Seasons* — never the default rules. Touches [[Economy]] and [[Downtime]].

---
## The Injury Table — one roll for maiming, capture, infection, and death

**Type:** Progression / Injury · **Take:** ⭐ steal

A single 2D6 table, rolled once per Out-of-Action Character at game's end, covers the entire space. **[FACT, p.84]**

| Roll | Result |
|:--:|---|
| 2 | **Dead** — removed from the roster, equipment lost |
| 3 | **Captured** — playable as a Rescue Encounter, or lost with their gear |
| 4 | **Arm Injury** — loses two-handed weapon use; rolled again = Dead |
| 5 | **Blinded in One Eye** — permanent −1 Firearms; rolled again = Dead |
| 6–8 | **Full Recovery** (three results of eleven — the modal outcome) |
| 9 | **Shell-Shocked** — permanent −1 Action Points |
| 10 | **Leg Injury** — costs extra AP to move; rolled again = Dead |
| 11 | **Infected!** — 1D6: 1–3 Dead, 4–6 amputate and roll Arm or Leg Injury instead |
| 12 | **"I'm Never Doing That Again"** — Full Recovery **and** 1D6 bonus XP |

**Why it works.** No separate infection sub-system, no separate capture sub-system — one table resolves all of it, weighted so outright death is rare (1/36) but permanent maiming is common enough that a veteran roster visibly accumulates scars. The escalation clause — roll the *same* wound type twice and the Character dies — lets an old injury make the *next* injury roll more dangerous without a separate stacking rule.

**For Settlements.** Feeds [[Progression]] directly. Our WND-2/WND-3 veteran ceiling already caps how much punishment a model carries; this table is a candidate *shape* for what happens the game a model actually goes down, rather than what gets rolled for it. The "same wound twice = dead" clause is the cheapest permadeath-with-mercy mechanic seen anywhere in this research line.

---
## Seasons and Weather — four tables that reskin the same six Encounters

**Type:** Campaign / Events · **Take:** ⚙️ adapt

*Seasons* doesn't add new mechanics to combat itself — it adds **weather as a pre-game 2D6 roll**, one table per Season, layered onto any of the base game's six Encounters or four new Season-specific ones. **[FACT, Seasons p.10-24]** Effects stay entirely tabletop-legible: LOS capped to 12"/18", ground floors count as Difficult Terrain, a Fire Line that spreads 6" per turn and sets zombies ablaze — no new resource, just battlefield conditions rolled before terrain goes down.

The four Season-specific Encounters (a Spring flood, a Summer wildfire, a Fall zombie-hunt, a Winter blizzard-raid) each reuse the base game's Supply Token / Breaking Point structure, changing only the hazard and the win-state detail.

**Why it works.** "A season" is delivered entirely as reskinned battlefield conditions plus the parallel resource-condition track (above) — it never touches the combat engine. The campaign feels different by month at zero cost to rules the players already know.

**For Settlements.** A cheap template for [[Events]]' battlefield-only scope and the [[Ideas Inbox]] want for boards that feel alive: a small seasonal/weather roll before terrain set-up (an LOS cap, one moving hazard, one altered zone) could deliver the same feel without inventing a new combat system — as long as it stays a pre-game table and never becomes a mid-battle one.

---
## Solo Play recycles the Keyword axis as its targeting AI

**Type:** Solo/Co-op · **Take:** ⭐ steal

Every Character already carries one of four Keywords — Selfish / Selfless / Trained / Neutral — set at recruitment to govern Group composition limits and, in *Seasons*, who eats/drinks/warms up first when supplies run short (see above). **[FACT]** Solo Play (*Seasons* p.66-73) reuses that **exact same axis** as its targeting AI: Selfish Characters must shoot or fight the nearest zombie to themselves first; Selfless Characters must help whichever Character is worst off; Trained Characters choose freely and may decline to act at all; Neutral Characters choose freely. **[FACT, p.70-71]**

The only other changes for solo play: drop Aggressor/Defender and activate in any order, field 30–40 zombies instead of 20, and add an escalating `1D6 + current turn number` random-event table in the End Phase — weather changes, alarm chains, a breakout of 2D3 hidden zombies, a "Horde Inbound" result that starts spawning multiple zombies per Noise draw — so tension ratchets up the longer the game runs. **[FACT, Seasons p.70-73]**

**Why it works.** One property does three jobs — recruitment limit, resource-rationing order, and solo targeting priority — with zero new Character data added. That's the same "reuse, don't add" instinct already logged elsewhere in this corpus, and it's the cheapest solo-AI implementation found so far.

**For Settlements.** A third data point for [[Solo & Co-op]], alongside [[Rangers of Shadow Deep]] (a full scripted monster-behavior table) and [[Spectre Operations#The Solo/NPC Rules — the detection system's own tables become the bot]] (the detection ladder doubles as the bot). All three converge on one principle: **the solo bot should run on a system the game already has**, never a parallel AI engine bolted on for one game mode. If Settlements ever ships a faction-disposition or alignment tag for any other reason, it's a free solo-AI hook already paid for.

---
## The Refuge costs zero

**Type:** Settlement · **Take:** ⭐ steal

The Refuge costs **zero points** and sits entirely outside the 100-point creation budget. Every Refuge is fully described by **three numbers** **[FACT]**:

| Refuge | Max Group Size | Empty Spaces | Built-In Perks (free) |
|---|:--:|:--:|---|
| The Gun Shop | 6 | 3 | Armoury, Fortified Windows, Reinforced Doors |
| The Farm House | 8 | 5 | Fenced-Off Garden *or* Stable, Cold Cellar |
| The Church | 8 | 2 | Solid Structure, Watch Tower |
| The Police Station | 8 | 2 | Escape Vehicle, Radio Room |
| The Prison | 10 | 3 | Fences, Infirmary |
| The Mall | 12 | 8 | Store Room |
| Outdoor Campsite *(Seasons)* | 12 | 10 | **None** — and **Exposed**: every Perk costs **+5 SP** |
| Cabin in the Woods *(Seasons)* | 5 | 3 | Wood-Burning Stove |

**Why it works.** **That is the entire interface**, and it's a genuinely excellent piece of design. The settlement never competes with the crew for the same budget, so choosing a base is a **shape** decision rather than a **spend** decision — and the trades read instantly. The Gun Shop gives you six models and three free Perks. The Campsite gives you twelve models and ten build slots but nothing free and a surcharge on everything.

> [!note] Provenance check on the Farm House row
> The core rulebook's own Farm House entry is **8 / 6 / Fenced-Off Garden** (one Perk, six spaces). **[FACT, core p.20]** The row above — 5 spaces, three Perks including Stable and Cold Cellar — is *Seasons*' explicit errata replacement: *"the following existing Refuge entry should replace the one from the Last Days: Zombie Apocalypse rulebook."* **[FACT, Seasons p.64]** The table above was already correct; it just wasn't flagged as a supplement overwrite of a core-book number. *Seasons* also adds a second, orthogonal tag layer on top of the three-number interface — **Remote** (permanent +1 to the off-table Zombie Attack roll) and **Exposed** (+5 SP to every Perk built) — worth folding into any Settlements version of this pattern as an optional fourth descriptor rather than a fourth number.

**For Settlements.** [[Settlement]] and [[Structures]]. Our HQ already carries housing (12, +6 per Bunkhouse) — the **Max Group Size / Empty Spaces / Built-In** triple is a candidate summary line for every settlement in the game, and it would make "which settlement do I want?" a legible question rather than a spreadsheet.

---
## Empty Spaces is the real constraint

**Type:** Settlement · **Take:** ⭐ steal

**Empty Spaces (2–10) is the binding limit; money only decides *when*.** **[FACT]** Built-in Perks never consume a space and can never be demolished. Empty Spaces are the only slots you can build into, and most Perks may only be built once. Perk prices run **15–30 SP** — Solid Structure 30, Infirmary 25, Wood-Burning Stove 25, Armoury / Bunk Bed / Fences / Fortified Windows / Watch Tower / Escape Vehicle 20, Garden / Radio Room / Reinforced Doors / Store Room / Rain-Collectors 15.

**Why it works.** A slot cap cannot be optimised around the way a price can. Income accelerates over a campaign; slot count doesn't. **The slot is what stops a rich player owning everything.** Same family as [[Gaslands#Points plus an unbuyable capacity]] and [[Kill Team#Slots instead of prices for the long tail]].

**For Settlements.** Our [[Structures]] list runs to 23. A **build-slot count per settlement** would do more balance work than any per-structure price, and it directly serves the anti-bloat tenet — you can ship all 23 without every crew eventually owning all 23.

---
## Keep the base out of ordinary battles

**Type:** Settlement · **Take:** ⭐ steal

Of the twelve core Perks, only two unambiguously touch an ordinary Encounter's own resolution or selection. **[FACT — corrected on the full read, see note below]** Everything else is economy, or fires **only in the one scenario where your base is physically on the table** (Home Defense), or fires only in the off-table, abstracted Zombie Attack roll that happens every campaign turn whether or not a battle was played.

> [!warning] Correction to the original claim
> The first pass through this book asserted *"only three touch a normal away game — Armoury, Fortified Windows, Radio Room"* on inference from the Perk list alone, without reading each Perk's actual trigger text. Having now read them: **Armoury** re-rolls failed Ammo Rolls *"during the next Encounter"* — any of the six ordinary Encounter types, confirmed. **Radio Room** lets you shift the `1D6` **Scenario roll** by ±1 after it's made **[FACT, p.98, p.81]** — a real touch on which ordinary battle you get, though it acts before the battle rather than inside it. **Fortified Windows**, however, only ever appears in the text as *"during a Zombie Attack the Group may add +1 to the Attack Roll"* **[FACT, p.83]** — the abstracted, off-table defense check, never an on-table Encounter of any kind, Home Defense included. It belongs with Watch Tower's off-table half, not with Armoury and Radio Room. **The corrected list of Perks that touch an actual tabletop battle is smaller than originally claimed, not larger** — which if anything strengthens the underlying finding.

**Why it works.** It means the settlement layer can be as deep as you like without slowing down or unbalancing the ordinary firefight. **The designer deliberately kept the base out of normal battles** — which is [[Oathmark]]'s instinct arrived at from a completely different direction.

**For Settlements.** A real design constraint worth adopting explicitly in [[Structures]]: *a structure's benefit fires in [[Downtime]], or in a raid on your own settlement — not in a territory battle.* It protects the pace goal and stops the settlement becoming a second army list.

---
## Three payoff channels

**Type:** Economy · **Take:** ⭐ steal

Every Perk falls into **exactly one** of three categories **[FACT]**:

| Channel | Examples |
|---|---|
| **Capacity** | Bunk Bed (+1 Max Group Size); Stable unlocking 0–2 Horses |
| **Economy** | Fenced-Off Garden (D6 SP post-game, **2D6 with an Agriculturalist**); Rain-Collectors (D3+3 water instead of D3+1); Store Room (re-roll a supply die); Cold Cellar (preserves surplus Meals); Wood-Burning Stove (**1 Fuel heats 2 rooms instead of 1**) |
| **Battle effect** | Armoury, Fortified Windows, Radio Room, Fences, Reinforced Doors, Solid Structure, Watch Tower, Infirmary, Escape Vehicle |

**Why it works.** One structure, one job. It makes the settlement legible, makes the three-way trade explicit at build time, and is what makes the "only [two] touch an away game" discipline enforceable — you can *count* it.

**For Settlements.** A clean taxonomy for the [[Structures]] table, and it maps onto the already-locked worker model (a worker assigned or not, ten benefits shipped and ten parked). Note the pattern in the Garden and Stove entries: **the upgrade improves a rate, not a number** — `1 Fuel heats 2 rooms` is a better upgrade than `+1 Fuel` because it scales with play.

---
## Structures own their unlocks

**Type:** Economy · **Take:** ⭐ steal

> *"Stable (20 SP) unlocks 0–2 Horses at 15 SP each, and **losing the Stable removes the Horses from the roster.**"* **[FACT]**

**Capability is leased, not bought outright.** The structure is a standing precondition, not a one-time purchase.

**For Settlements.** This is the enforcement mechanism the [[Ideas Inbox]] crafting want needs: if new [[Structures]] unlock new craftable equipment tiers, then **losing the structure has to cost you the unlock**, or raids on a settlement never really hurt. It also gives raids a target that isn't a body.

---
## Context-priced construction

**Type:** Settlement · **Take:** ⭐ steal, ⚠️ and note the bug

The **same Perk costs different amounts by context** **[FACT]**: an **Engineer** assigned to Build cuts the cost **25%, rounding up**; an **Exposed** Refuge adds **+5 SP** to every Perk.

⚠️ **The book never states the order of operations.** 35 → 27, or 23 + 5 = 28? **Genuinely unresolved in print**, confirmed still unresolved on the full read of both books.

**For Settlements.** Take the mechanic — a worker who reduces build cost is exactly our worker model — and **take the warning too.** Any time two modifiers touch the same number, the rules must state the order. That's a [[Rules Engine]] house-convention issue, and it's the sort of thing [[Edge Cases]] exists to catch.

---
## What it does *not* do: hold points equal

**Type:** Campaign · **Take:** 📎 reference

**There is no per-game points limit after group creation at all.** **[FACT]** You spend 100 SP once; after that there is no budget check before any battle. You deploy your **entire Group** in almost every Encounter, and recruitment between games is capped only by Max Group Size.

**Veterans are never re-priced.** Levels are bought with **Experience**, a completely separate currency from Scavenge Points, and the two never convert. *You cannot buy a stat with SP, and you cannot buy a body with XP.* A 3 SP Crony at Level 10 is still a 3 SP Crony on the roster.

**For Settlements.** The XP/SP separation is the same principle as [[Frostgrave and Stargrave#Two economies, no exchange rate]] and matches our own locked "skills are never charged Credits". The **no per-game budget** half we should *not* take — [[Oathmark#The kingdom widens the menu]] is the better answer for a competitive-capable game, and Crew Rating caps are already locked.

---
## Source

- Primary: Last Days core rulebook + *Seasons* supplement, both PDFs read in full, twice — first for the settlement/Refuge layer, second for core resolution, the turn, the zombie horde, noise, injury, weather, and solo/co-op
- Capture: `research/sources/last-days/` (`original.pdf` = core rulebook, `seasons.pdf` = campaign supplement)
- Long-form: `docs/POINTS-RESEARCH.md` §7.17
- Related: [[Wargaming Research Hub]] · [[Oathmark]] · [[Trench Crusade]] · [[The Walking Dead All Out War]] · [[Zona Alfa]] · [[Mad Dogs with Guns]] · [[Spectre Operations]] · [[Rangers of Shadow Deep]] · [[Settlement]] · [[Structures]] · [[Economy]] · [[Progression]] · [[Morale]] · [[Damage]] · [[Events]] · [[Solo & Co-op]] · [[Ideas Inbox]]

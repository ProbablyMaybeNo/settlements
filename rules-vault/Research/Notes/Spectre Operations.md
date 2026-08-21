---
type: research-note
title: Spectre Operations
game: Spectre Operations — modern/near-modern military skirmish
designer: Stephen May
publisher: Spectre Miniatures
depth: primary — 3rd Ed Revised 07-25 (143pp) + Official Errata (5pp) + Solo/NPC Rules (5pp), all read in full
retrieved: 2026-08-20
source_url: https://spectreminiatures.com/pages/rules
capture: research/sources/spectre-operations/
tags: [settlements/research]
---
# 🎲 Spectre Operations

> [!abstract] In one breath
> A **contemporary special-operations skirmish game**: squad-scale "Elements" (1–20 models) fight over Resources-limited Forces, activated through a shared **Momentum** economy that pays for both your turn and your reactions. The closest tonal and technological match in the whole research corpus to Settlements' 2051 setting — grounded mil-tech, drones, EW, night optics — and it is also the first source that answers our stealth/detection want with an actual system: three alert states, an asymmetric noise-detection roll, guard AI built from Points of Interest and Areas of Patrol, and a Covert Action layer with a numeric, decaying Cover Level. Where [[Zona Alfa]] came back **[NOT FOUND]** and [[Mad Dogs with Guns]] came back with one SMARTS roll, this book has a whole subsystem.

| | |
|---|---|
| **Designer · publisher** | Stephen May · Spectre Miniatures (first published July 2023) |
| **Scale / format** | Squad-level skirmish. 1 or more **Elements** (1–20 models, usually 4–8) a side, 28mm, table 2′×2′ minimum, 3′×3′–4′×4′ typical |
| **Core resolution** | `1D10 vs a Stat` (Ballistics / Awareness / Stress), roll **equal to or higher** to succeed. *"Regardless of modifiers (unless explicitly stated), a 1 is always a fail and a 10 is always a pass."* **[FACT — p.10]** — the same natural-1/natural-10 rule Settlements has locked, arrived at independently |
| **Depth of read** | **Primary** — 3rd Ed Revised 07-25 (143pp) + Official Errata (5pp) + Solo/NPC Rules (5pp), all read in full. Where the Errata corrects the 3rd Ed, the Errata wins throughout this note |
| **Raw capture** | `research/sources/spectre-operations/` in the Settlements repo |
| **Source** | Spectre Miniatures, 2023–2025. Four editions exist in the library (`G:\My Drive\Wargaming\Spectre Operations [FULL COLLECTION]\`); 2nd Ed and 2nd Ed Hard Copy Scan are image-only and unread, 1st Ed is superseded and unread — see **Source** below |

---
## Why it's here

Every other game captured so far has been graded partly on setting fit; this is the first one that scores highly on **mechanical** fit too. It is contemporary special-operations combat — the same register of professional soldiers, irregular militia, drones, jamming, and night-vision that 2051 grounded mil-tech asks for — and unlike [[Zona Alfa]] (STALKER-flavoured, zero settlement layer, **no** stealth mechanic at all) or [[Mad Dogs with Guns]] (Prohibition gangsters, one SMARTS-plus-cover roll for stealth), Spectre Operations has spent an entire Advanced Rules chapter on **exactly** the open want at the top of our list: alert states, detection, noise, and covert disguise. It also has a real suppression/morale cascade, a Solo/NPC ruleset that visibly reuses the detection system's own tables as bot AI, and a campaign layer that resolves the veteran price-vs-cap fork in the "price it" direction with two separate, quotable data points.

The book is not without rough edges — see **What it gets wrong** — but as a source, this is the single richest capture in the corpus for our stealth/detection and suppression open questions.

---
## Momentum — one pool pays for your Actions and your Reactions

**Type:** Activation · **Take:** ⭐ steal

There is no per-model action allowance and no alternating IGOUGO. Each Force generates a shared **Momentum** pool at the start of every turn — *"Your Force gains 2 Momentum points for each Element in your Force… During turns 1-3, an additional +1 Momentum is also generated."* **[FACT — p.20]** Every Action (Manoeuvre, Engagement, Assault, Rally, Breach, …) costs 1 Momentum, and spending *more* than 1 on the same Action usually buys more dice at a cost — e.g. Manoeuvre: each extra Momentum moves you again but shortens the distance by 1″ cumulatively; Engagement: each extra Momentum adds a die per model but costs −1 to hit.

Momentum degrades under fire and is a genuine morale valve, not just an action budget: **−1 Momentum for each Suppressed Element, −2 for each Pinned Element**, floored so *"even with negative modifiers, a Force always generates a minimum of 1 Momentum each turn."* **[FACT — p.20]** Reactions (Return Fire, Snap Shot, Go to Ground, Break Contact) are paid from the **same pool**, so a player choosing to spend everything on their own turn is explicitly trading away their ability to react on the opponent's — *"it may be worth considering leaving some Momentum unused, so Reactions may be made."* **[FACT — p.21]** Any Momentum left unspent at end of turn is lost — confirmed in the Errata FAQ: *"Q: Does Momentum Generated carry on to the next turn? A: No, Momentum resets at the Start of the next turn. The only way to carry Momentum over is to reserve one for Escalations."* **[FACT — errata p.2]**

**Why it works.** Suppression, activation economy, and reaction economy are all the same number. A Pinned Element isn't just individually crippled — it drains the *whole Force's* tempo, and every player choice ("spend it all now" vs "hold some back") is a single legible trade-off rather than three separate systems (actions, morale, reactions) each needing their own tuning pass.

**For Settlements.** [[Initiative & Activation]]. This is a genuinely different shape from our own turn structure and worth comparing directly against whatever reaction/interrupt economy we land on — it answers the open **"reaction/interrupt economies"** sweep on the hub's to-read list with a real, working example: reactions aren't a separate resource, they're a *choice not to spend* the same currency your turn runs on. The honest cost: it requires tracking one shared Force-level number plus per-Element Suppressed/Pinned flags, which is more bookkeeping than a flat "N actions per model, no more."

---
## The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll

**Type:** Detection · **Take:** ⭐ steal

This is the payload. Every Element sits in one of three **States of Awareness (SoA)**, each gating Momentum, Stress, and available Actions **[FACT — p.85]**:

| State | Momentum | Stress | Awareness Tests | Restriction |
|---|---|---|---|---|
| **Unaware** | 1 | 1 | −1 modifier | Only *Hang Around*, *Take a Walk*, *Meetup*, *Relax* |
| **Uneasy** | 2 | 2 | No modifier | Only *Patrol*, *Scan*; may Detect but not Engage |
| **Alert** | Standard | 2 (min) | No modifier | Full access to all Actions |

Detection is resolved by a free test (no Momentum cost) that fires *"immediately after movement, but after Engagements are resolved in the Phase"* **[FACT — p.86]**, with a distance-and-behaviour modifier table (target within 6″ **+6**, within 12″ **+3**, within 18″ **+2**, target spent >1 Momentum this phase **+2**; Light Cover **−1**, Heavy Cover **−2**, Prone **−2**). Becoming **Alert** is triggered explicitly by: an enemy detected, a casualty observed, being targeted by a noisy attack, or an alarm/escalation.

**Audio detection is the sharp, asymmetric edge.** Unsuppressed weapons don't roll at all: *"If an Unsuppressed Weapon is used: All enemy Elements become Alert immediately. No Awareness Test required."* **[FACT — p.87]** Suppressed weapons instead give nearby Elements a chance to hear it, scaled by range (CQB **+3**, Engagement **+2**, Extreme **+1** to the listening roll). Spotting a casualty cascades further: *"The entire force becomes Alert if: Casualties are witnessed AND An Element communicates (e.g., yelling, radio use)"* **[FACT — p.87]** — and the force gets a **free Escalation die** as compensation for the exposure. An optional **Suspicion** state sits between Uneasy and Detected for a near-miss detection roll.

**Guard behaviour and stealth-mission design ride the same states.** Undetected/Unaware/Uneasy forces are scripted with **Points of Interest (PoI)** — *"a fixed terrain feature that enemy Elements are assigned to occupy, guard, or move between… The PoI includes: the interior of the terrain feature, all accessible walkways, balconies, and rooftops, up to 2″ around the outer boundary"* **[FACT — p.87]** — and **Areas of Patrol (AoP)**, a linear route with a Start Point and End Point that Elements must enter, walk, and only exit at the far end *"unless interrupted by a reaction (e.g., detection or alert status)"* **[FACT — p.88]**. **Sentries** (1–2 models, deployed only while the force is Unaware/Uneasy) patrol AoPs even when the rest of the defending force is confined to PoIs.

**Why it works.** One shared vocabulary (SoA) answers four separate design questions at once: what a guard is allowed to do before it notices you, how noise gives away your position, how a single dead body can cascade into a whole-map alert, and — per the next entry below — what a solo bot does on its turn. Nothing here needed a second rules chapter; the Detection Mechanics chapter just gets reused everywhere the concept of "does the enemy know I'm here yet" comes up.

**For Settlements.** This is the most direct precedent yet found for [[Ideas Inbox]]'s stealth/noise want — the "sneak at half speed, noise/shooting snaps you out of it, 12″-ish detection radius" idea sketched there is structurally close to what Spectre actually ships, but Spectre's version is considerably more load-bearing: three named states rather than a binary hidden/spotted flag, and the states double as morale (Stress floor) and tempo (Momentum cap) levers, not just visibility. The **audio asymmetry** (unsuppressed = automatic Alert, suppressed = a roll) is the single cheapest, most transferable idea here — it turns "did you use a suppressor" into a real tactical decision with one binary branch, no dice needed for the loud case. Touches [[Movement]], [[Terrain]] (PoI/AoP behave like scripted terrain zones), and directly informs the open stealth/noise question that [[Zona Alfa#Stealth and noise — searched for, and it isn't here]] and [[Mad Dogs with Guns#Hiding, Creeping, and noise — the stealth mechanic Zona Alfa didn't have]] both left thin or empty.

---
## Covert Action and Cover Level — a decaying resource under scrutiny

**Type:** Detection · **Take:** ⭐ steal

Any Element can be declared Covert — *"disguised in civilian or enemy uniforms, and carry concealed weapons"* **[FACT — p.88]** — and is rated by a numeric **Cover Level** by training tier (Civilian 1, Conscript 1, Militia 2, Enlisted 2, Criminal / Veteran 3, Tier 2 4, Tier 1 5 **[FACT — p.89, Cover Table]**). Maintaining the act under scrutiny is its own Stress-shaped test: *"Roll a number of d10 equal to the current Cover Level. For each result lower than [the Element's Stress Value], the Cover Level is reduced by 1."* **[FACT — p.89, quoted with one interpretive clarification — see below]** Reaching 0 **Blows** the cover outright: the Element becomes Detected, targetable normally, and *"all enemy Elements become Alert"* plus every other Covert Element on the same force takes **+2 Stress** in sympathy. **[FACT — p.90]**

The enemy's counter-play is a dedicated **Scrutinise** action (Momentum-costed, forces the target's Cover Level test) and a **Physical Search** action, which auto-detects outright if the target is carrying armour (Untrained searcher) or armour *or any weapon* (Trained searcher) **[FACT — p.90]**. Scrutinise dice scale with proximity and the target's own kit — within 6″ **+2 dice**, an Alert Scrutiniser **+2 dice**, a weapon without the Compact rule **+1 die**, without Compact *or* Covert **+3 dice**, Body Armour **+1 die** **[FACT — p.89]** — so carrying a rifle openly is a real, priced cost against staying hidden in plain sight. Engaging while Covert is allowed but risky: firing a suppressed weapon only triggers a free Scrutinise from nearby enemies, firing unsuppressed blows Cover automatically. **[FACT — p.89, table p.90]**

**Why it works.** "How good is your disguise" becomes a single depleting number instead of a binary hidden/not-hidden flag, so a Covert Element's risk visibly ticks down over the course of a mission rather than snapping from safe to blown on one bad roll — and the +2 Stress sympathy penalty on Blown Cover means one operative's mistake has a mechanical cost for the rest of the covert team, not just a narrative one.

**For Settlements.** Touches [[Ideas Inbox]]'s stealth want directly, and is the strongest evidence yet that a *resource* model for concealment (a number that bleeds down under pressure) is a genuinely different, and arguably richer, design than a *state* model (hidden/spotted). The honest cost: it needs its own small stat (Cover Level) per Element plus two new enemy actions (Scrutinise, Physical Search) to make the pressure real — not a free addition to an existing test. Note the source text itself is ambiguous about what value the Cover-Level test compares against (see **What it gets wrong**).

---
## The Solo/NPC Rules — the detection system's own tables become the bot

**Type:** Solo · **Take:** ⭐ steal

The 5-page Solo/NPC supplement adds **no new detection subsystem** — it reuses SoA, PoI, and AoP verbatim as the bot's decision tree. Setup is literally: *"designate a number of areas as PoI and AoP as described in Spectre Operations… Deploy the NPE within or up to 4″ outside of the edge of the PoI… NPEs should start the game as Unaware or Uneasy."* **[FACT — solo p.2]** Each NPE Element's turn resolves as a scripted die roll: Unaware Elements roll on a 3-entry table (*Hang around* / *Take a Walk* toward the nearest PoI / *Meetup* with a friendly Element), Uneasy Elements roll a similar table biased toward *Patrol*, and once an Element is **Alert** its behaviour switches to a target-seeking table — engage the nearest valid enemy, spending a Momentum-scaled amount of dice rolled on a D10 (1–3 → 1 Momentum, 4–8 → 2, 9–10 → 3) **[FACT — solo p.4]** — with common-sense weapon selection (no rifles at armour, Anti-Tank rules reserved for vehicles/buildings).

Reactions are handled the same way, deliberately unreliable: *"NPE are able to make Reactions as normal… Reactions will, in general, only be made on the role of 6+, giving some unpredictability."* **[FACT — solo p.5]** Suppressed/Pinned NPEs are forced to attempt Rally before any other roll.

**Why it works.** No parallel AI system had to be designed. The stealth chapter already had to answer "what does an unaware guard do before it notices you," and that exact answer *is* a solo bot's turn — one subsystem doing two jobs (scripted mission-design behaviour and a full solo/co-op opponent) for the cost of a single extra page adding a target-seeking table for the Alert state and a flat 6+ gate on Reactions.

**For Settlements.** [[Solo & Co-op]]. Directly comparable to [[Rangers of Shadow Deep#Scale the players, not the enemies]] — a genuinely different axis of the same solo-design problem. Rangers scales the *players'* Recruitment Points down as more people join, so the enemy side never needs its own AI logic beyond fixed encounters. Spectre instead builds a real (if simple) opponent AI, but pays for almost none of it separately: the AI *is* the stealth-detection state machine with one behaviour table bolted onto each state. If Settlements' solo/co-op design leans toward "the AI actually decides things" rather than "scale the human side," this is the cheapest published way to get there — **conditional on already having built a stealth/detection layer to reuse**, which is exactly the fork Settlements hasn't resolved yet.

---
## The Engagement Pipeline — Accurate Fire, a Situational Awareness "save," then Lethality

**Type:** Combat · **Take:** 📎 reference (independent convergence)

A shot resolves in the same order every time: **(1)** the Engaging Element rolls Accurate Fire per model (vs Ballistics, or vs current **Stress** instead of Ballistics inside CQB range — *"elements must test to hit using their current Stress Level, rather than Ballistics"* **[FACT — p.29]**, a small, elegant detail: panic degrades your marksmanship exactly where marksmanship matters least and reflexes matter most); **(2)** for every accurate hit, the Target Element rolls a **Situational Awareness** test (modified by Cover: Light +1, Medium +2, Heavy +3, and −2 if shot from outside its own Field of Fire, −1 if the shooter used entirely Suppressed weapons) — pass, and no casualty results, but the Element still gains Stress for the close call; **(3)** only failed Awareness tests roll for **Lethality**, and only Lethality successes remove models; **(4)** everything — passed Awareness tests, failed Lethality rolls (until the Errata — see below), casualties — feeds one shared **Stress Test** at the end. **[FACT — pp.28–31, full sequence quoted]**

**Why it works.** Every accurate shot produces *something* — either the target flinches into more Stress, or it dies — never nothing and never both. That's the same "every hit does something, wounds or delivers a payload, never both" tenet Settlements already has locked, reached by a completely independent designer.

**For Settlements.** [[Shooting]], [[Morale]]. Nothing to adopt structurally — the convergence is the finding, not a new idea — but the CQB-uses-Stress-not-Ballistics wrinkle is a genuinely transferable one-liner if Settlements ever wants a cheap way to make close-range combat feel more chaotic without a separate CQB sub-system: reuse the existing fear stat as the accuracy stat at close range, for free.

---
## The Stress Result Table — a graduated cascade, and Trained keeps more than Untrained

**Type:** Morale · **Take:** ⚙️ adapt

A single shared mechanism (roll 1D10 per source of Stress, compare to the Element's current Stress Value, count failures) reads off one of two 9-step tables depending on training:

| Failures | Untrained result | Trained result |
|---|---|---|
| 0 | Defiant — no effect | Defiant — no effect |
| 1 | *Startled* — 1 Momentum next Action, Reactions OK | *Tactical Pause* — 1 Momentum next Action, Reactions OK |
| 2 | *Disarray* — +1 Stress, no Actions/Reactions this turn | *Go to Ground* — free 3″ move to cover |
| 3 | *Shocked* — Suppressed this turn only | *Suppressed* |
| 4 | *Suppressed* | *Fragmented* — +1 Stress, barred from Component/Fire Support Actions |
| 5 | *Pinned* — Go to Ground, no Actions | *Pinned* — Return Fire / Break Contact / Rally only |
| 6 | *Routed* — full move to table edge | *System Shock* — +2 Stress, must Break Contact if Rally fails |
| 7 | *Fleeing* — as Routed, +1 Stress/turn | *Combat Fatigue* — must Rally before any other action |
| 8+ | *Collapse* — removed from play | *Collapse Under Fire* — removed from play |

**[FACT — pp.31, both tables quoted in full]** The training-gate is explicit and structural, not flavour: *"Untrained Elements cannot make Reactions while Pinned or Suppressed… Trained Elements may always make Reactions unless otherwise stated."* **[FACT — p.31]**

**Why it works.** One roll, one shared comparison, two different tables read off the same failure count — Trained forces don't just resist Stress better (their Base Stress is lower), they get a materially different *menu of consequences*, keeping Reaction access two states longer than an Untrained force would. It's a training difference expressed entirely in what happens after the dice, not in the dice themselves.

**For Settlements.** [[Morale]]. Worth weighing against our own Stress/Nerve cascade for the same idea: **does training change what a failure means, not just how often it happens?** The two-parallel-tables approach is more bookkeeping than a single shared table (two tables to remember, two sets of named states) — a real cost against the benefit of a sharper trained/untrained distinction.

---
## Wound Severity by Margin of Failure

**Type:** Combat · **Take:** ⭐ steal

An optional but clean rule: when a Lethality roll fails, the model isn't just "not killed" — how far it missed by directly selects the outcome from one table, no second roll needed. *"When a Lethality Roll is failed, determine how much the roll missed by… e.g., Lethality 7, roll of 5 → failed by 2."* **[FACT — p.97]**

| Failed by | Outcome | Effect |
|---|---|---|
| 1 | **Incapacitated** | Downed, may bleed out — a friendly model must reach it and pass a Stress Test (−1/turn since injury) to stabilise it, or it's removed as a Casualty |
| 2 | **Minor Injury** | Wounded — Sidearm only, no Heavy Weapons |
| 3+ | **Narrow Escape** | Stunned — no Actions this turn, still counts for Cohesion |

**[FACT — p.97]** A Wounded or Incapacitated model hit again by any successful Engagement, Area Effect, or another failed Lethality roll is automatically killed **[FACT — p.97, "Finishing Off Wounded Models"]**, and an optional Triage & Medkits rule lets a Medic reroll a failed stabilisation once and, in a Campaign, roll for recovery instead of losing the model permanently.

**Why it works.** No separate injury-table roll is needed — the same die that determined the failed Lethality test also grades its severity, entirely for free. A weapon with Lethality 9 produces harsher near-misses on average than one with Lethality 6, because the margin distribution differs by weapon, without a single extra line of rules.

**For Settlements.** [[Damage]], [[Progression]] — direct, load-bearing precedent for the **per-unit persistence and injury** open question. This is a genuinely different shape from [[Necromunda and Mordheim#Lasting injuries]] and [[Zona Alfa#Battle Scars — permanent injury gated by bad luck, not by poverty]] (both roll a *separate* injury table after the fact): here the failed roll's own margin *is* the severity roll, collapsing two dice rolls into one. Worth weighing directly against those two for whichever direction the WND/injury design goes — margin-of-failure is cheaper at the table (one fewer roll per casualty) but only works if the underlying test already produces a graded miss rather than a flat pass/fail.

---
## Reactions — Return Fire, Snap Shot, Go to Ground, Break Contact

**Type:** Reactions · **Take:** 📎 reference

A standard-shape reaction suite, each costing 1 Momentum from the shared pool (see **Momentum**, above): **Return Fire** (shoot back at −1 to hit after being engaged, Trained Elements may first move 2″ to a better position), **Snap Shot** (an Overwatch-style reaction against a mover entering LoS, resolved against the reactor's **Awareness** stat rather than Ballistics — *"representing the difficulty of reactive shots"* **[FACT — p.24]**), **Go to Ground** (declared after the Accurate Fire roll but before Situational Awareness, granting +2 to that Awareness test), and **Break Contact** (Trained-only, substitutes a retreat move for the end-of-Engagement Stress Test entirely).

**Why it works.** Nothing structurally novel next to [[BLKOUT#Reactions — the beating heart]] or [[Zona Alfa#Initiative and Alternating Activation]]'s Alert Action — but the training gate matters: **Untrained Elements lose all Reaction access while Suppressed or Pinned; Trained Elements keep it** (see the Stress Result Table entry above), which means the same reaction suite plays very differently depending on who's holding it.

**For Settlements.** [[Initiative & Activation]]. Table stakes for the genre, logged mainly for the Snap-Shot-uses-Awareness-not-Ballistics detail (a cheap way to make reactive fire feel worse than aimed fire without a flat penalty) and the trained/untrained Reaction-access gate, which pairs with the Stress Result Table entry above as one combined design lever rather than two.

---
## Veteran Pricing as a Flat Surcharge, Never a Cap

**Type:** Campaign · **Take:** ⭐ steal (as a data point for the fork)

Two separate, quotable mechanisms both resolve Spectre's veteran-inflation problem the same way — by price, not by a cap. Within a single force build, upgrading a trained soldier a tier costs a flat surcharge: *"Task Force Veterans: Enlisted Elements may be upgraded to Veterans for 10r per model."* **[FACT — errata p.2]** Between campaigns, keeping an experienced Element taxes it directly for every point of growth it's banked: *"If you wish to keep an Element after a Campaign, increase the Resources cost for the Element by 10r for Each point of Experience they have spent on Statistics increases or Skills."* **[FACT — p.141, "Veteran Elements For Hire"]** There is no headcount ceiling, no Battle-Scar-slot limit, no maximum-tier cap anywhere in the veteran-retention rules — inflation is left running, and priced.

**Why it works.** Both rules are the same idea at two different scales (in-list upgrade, cross-campaign carry-over): every point of earned capability has an explicit Resources price tag, so a min-maxed veteran Element is never *free* to field again, it's just *expensive* to field again. No bookkeeping beyond "how much XP did this Element spend."

**For Settlements.** [[Campaign]], [[Progression]] — this is the **"price it" side of the live veteran price-vs-cap fork**, sitting opposite [[Trench Crusade#Cap the veterans, don't tax them]] (never re-price a veteran; cap ELITE count and Battle Scar slots instead) and alongside [[The Walking Dead All Out War#Re-pricing veterans]] (flat +3 points per surviving game, no cap either). Three published games, three different combinations — Spectre and TWD both tax, Trench Crusade caps — and Settlements' own rules currently tax (per `AGENTS.md`'s note that this fork is still live). Spectre's version is the simplest of the three taxing examples: one flat rate (10r) per point of XP spent, no compounding schedule.

---
## "Stress Raised Too Quickly" — a Shipped Mistake, Fixed in Errata

**Type:** Morale · **Take:** ⚠️ instructive failure

The 3rd Edition as first printed added Stress twice for the same bad outcome: a successful Situational Awareness test added Stress, *and* a subsequently failed Lethality roll added another point. The Errata removes the second source outright, and states the reason in the designer's own words: *"Q: Can a frag hit cause two stress increases, 1 for a successful awareness and one further for a failed lethality? A: The extra stress for Failed Lethality has now been removed - we found after wider playtesting that stress raised far too quickly."* **[FACT — errata p.3, verbatim]** A related Errata entry loosens the same axis from the other side: *"P.31 Stress Tests / Suppression: Elements may make the Rally Action when Suppressed."* **[FACT — errata p.1]**

**Why it's here.** A documented, designer-stated cause ("stress raised far too quickly," found via wider playtesting after release) is exactly the kind of shipped mistake worth more than an unexamined success — it's a real number of stress-accumulation-per-turn that was too high, caught only after the book was in players' hands.

**For Settlements.** [[Morale]]. A direct cautionary data point for calibrating Stress accrual rate: stacking two Stress sources off a single Engagement action (a "flinch" source and a "near-miss" source) reads as reasonable on paper and broke in actual play. Worth a specific gut-check on Settlements' own Stress triggers for the same double-counting shape — does a single bad roll ever feed Stress through two independent paths in the same resolution?

---
## Drone and UGV Warfare — a Stress-Free Element

**Type:** Combat · **Take:** ⚙️ adapt

Miniature UAVs (M **8** / B **7** / A **4** / S **0**) and UGVs (M **7** / B **6** / A **7** / S **0**) are full Elements — they generate Momentum, Manoeuvre, and Engage like any other — with one deliberate exception: *"Drones do not gain Stress or confer any Stress to their Parent Element."* **[FACT — p.80]** Engaging an M-UAV always counts as Extreme Range *"unless the Engagement is using an Anti-Drone Weapon"* **[FACT — p.80]**, and dedicated hard-counters exist on both the weapon side (a priced **Anti-Drone gun**, 50r in the Militia Armoury) and the armour side (**Cope Cage** — slat armour bolted to a vehicle's roof specifically *"to defend against drone attacks that usually crash into or detonate on the upper hull"* **[FACT — p.80]**). Electronic Warfare devices layer on top: an **IED Jammer** blocks detonation within a radius, a **Tactical EW System** blocks the enemy Commander's Escalation Requests and negates their Comms bonuses entirely, and Hardened Comms are the priced immunity to all of it.

**Why it works.** "No Stress, ever" is doing real design work in one line: a drone can't be suppressed, routed, or panicked, so it never needs its own morale rules despite otherwise following every ordinary Element rule — the exception is cheaper than writing a parallel "drones don't have feelings" carve-out into every Stress-triggering rule individually.

**For Settlements.** [[Hacking]], [[Deployables]]. Directly relevant to the 2051 tech layer: a drone/robot chassis that's mechanically a normal combatant except explicitly exempted from the fear/Stress axis is a clean, cheap template if Settlements' own Deployables ever field a stress-immune unit type. The hard-counter pairing (a named anti-materiel weapon category *and* a named armour upgrade, both explicitly for drones) is also a good reference shape for pricing counter-tech deliberately rather than leaving drones simply "harder to kill with normal weapons."

---
## Force Builder — One Price Ladder Prices a Militia and an Elite Operator

**Type:** List · **Take:** 📎 reference

Both Force Builders (Insurgent/Militia and Task Force) share one **Resources (r)** economy and one weapon/equipment catalogue; what changes is a straightforward per-model price ladder by training tier: a Militia rifleman costs **20r**; the same Infantry Element slot costs **30r** (Enlisted) / **40r** (Veteran) / **50r** (Tier 2) / **60r** (Tier 1), rising as high as **80r** for a Tier 1 Support Element specialist. The designer's note is explicit that the tiers aren't purely a stat/price ladder — they also gate *access*: *"although the capability of Tier 2 and Tier 1 Elements are extremely high, the access to some equipment is more limited than Veteran or Enlisted Elements… This is intended to represent the roles these highly specialised units take in real life."* **[FACT — p.110]** In practice this produces the book's own recommended pattern: cheaper Veteran/Enlisted Elements crew heavy weapons and vehicles for fire support, while expensive Tier 1 riflemen do the objective work.

**Why it works.** One catalogue, one price axis (per-model rate by tier), and the *equipment list itself* — not a separate points premium — is what keeps elite units from being simply "the same guy, costs more." Professional-squad and irregular-militia identity comes from what's on each list, not from a duplicated pricing formula.

**For Settlements.** [[List Building]], [[Factions]]. A useful contrast rather than a direct steal, since Settlements' crews are explicitly irregular throughout (no professional-military faction to price against a militia one) — but the underlying idea, **gate the top tier's identity by catalogue access rather than by a bigger price multiplier alone**, is worth comparing against how Settlements' own Rank ladder (Recruit/Fighter/Specialist/Leader) currently differentiates itself: partly by stat points, partly by Tier caps at creation, not by a restricted-equipment list. Spectre adds a third axis (gear-list gating) that Settlements doesn't currently use.

---
## What it gets wrong

**A first edition still settling its own rules text.** Five pages of Errata plus an FAQ is a lot for a 143-page book, and several of the FAQ answers aren't typo fixes — they resolve genuine ambiguity in the core resolution loop: how many dice a Stress Test actually rolls (players read two different sections and got 4 vs 9 dice for the same example), whether Momentum carries over, and whether losing Cohesion has action priority. **[FACT — errata pp.2–3]** The lesson generalises past this one book: a shared-pool activation economy like Momentum has more surface area for cross-rule ambiguity than a simple "N actions per model," and it shows up first in the FAQ, not the rulebook.

**An unresolved ambiguity survives even the Errata.** The Covert Cover Level test (**Covert Action and Cover Level**, above) instructs players to compare dice against *"the set Stress"* without ever defining, anywhere in the 143 pages or the 5-page Errata, what value that phrase refers to. **[NOT FOUND — the phrase "the set Stress" is not defined in the source text.]** The most consistent reading, by analogy with every other Stress Test in the book (roll dice, compare each to the Element's *current Stress Value*), is that "the set Stress" means the Covert Element's own Stress Value — but that is **[INFERENCE]**, not a quoted rule, and the Errata had the opportunity to clarify it and didn't.

---
## Evidence & confidence

- **[FACT]** tags above are quoted directly from the 3rd Ed Revised 07-25 rulebook (page numbers as printed in the book) or the Official Errata (page numbers as printed in the 5-page PDF, since the Errata carries no internal page footer of its own).
- **[INFERENCE]** is used exactly once, for the Covert Cover Level's ambiguous "set Stress" phrase, and flagged inline where it occurs.
- **[NOT FOUND]** is used for the same phrase's absence from both the rulebook and the Errata, and for nothing else in this note — the read did not come back thin anywhere else the brief asked it to look.
- No **[CONSENSUS]** tags appear in this note; every claim traces to the primary rulebook, its Errata, or its Solo Rules supplement, not to community discussion.

---
## Source

- Primary: *Spectre Operations*, 3rd Edition, Revised Version 0.1 (Second Printing July 2025), Stephen May, Spectre Miniatures. Plus the Official Errata (Spectre Miniatures, current as of scrape) and the Solo/NPC Rules supplement (5pp).
- Capture: `research/sources/spectre-operations/source.md` (main rules, 143pp verbatim), `errata.md` (5pp verbatim), `solo-rules.md` (5pp verbatim), `meta.json` (bibliographic + hash + extraction record for all three PDFs).
- Editions in the library not read this run: 2nd Ed (154pp) and 2nd Ed Hard Copy Scan (78pp) — both image-only, would need OCR; 1st Ed (77pp) — superseded, clean text but unread; 3rd Ed Quick Reference Guide (8pp) — image-only, unread.
- Supplements in the library not read this run (13 titles, all clean text, uncaptured): Frontlines v3, Aftermath, Jungle Supplement, Outbreak, Cosmic Horror, Criminal Element, Law Enforcement, Russian Forces, EOD rules, Baba Yaga, Blackout Rifle, and the Operation Harridan / Operation Gallowglass / Operation Leatherback scenario packs.
- Related: [[Wargaming Research Hub]] · [[Zona Alfa]] (stealth comparison — confirmed absent there) · [[Mad Dogs with Guns]] (stealth comparison — one thin roll there) · [[Rangers of Shadow Deep]] (solo/co-op comparison) · [[Trench Crusade]] and [[The Walking Dead All Out War]] (veteran price-vs-cap fork) · [[BLKOUT]] (reactions comparison) · [[Necromunda and Mordheim]] (injury-table comparison)

---
*Add one row per mechanic to [[Wargaming Research Hub]] when this note is finished.*

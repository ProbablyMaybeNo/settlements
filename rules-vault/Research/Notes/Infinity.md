---
type: research-note
title: Infinity
game: Infinity N3-N5
publisher: Corvus Belli
depth: official N5.2 wiki (hacking/EW, full pass 2026-08-20) + N3 rulebook figures (SWC costing, earlier pass)
retrieved: 2026-08-20
capture: research/sources/infinity-hacking/ (hacking/EW pass only — the SWC costing pass predates this vault's capture convention and is cited via docs/POINTS-RESEARCH.md §7.2 with no source folder)
tags: [settlements/research]
---
# 🎲 Infinity

> [!abstract] In one breath
> Two passes, two very different verdicts. The **dual-currency reference implementation** (SWC) has survived four editions essentially unchanged — the strongest evidence any mechanic in this vault has. **Quantronic Combat (Hacking)**, captured in full below, is the opposite kind of finding: the deepest, most decorated Electronic Warfare subsystem in the hobby, published by the one studio with the resources to make it work — and across three editions Corvus Belli's own trend has been to **shrink** it, not grow it. Judged against Settlements' own bar (`docs/BLKOUT-RULES-ANALYSIS.md` §19: *can it be one Action = one test = one clear effect?*), most of it cannot clear that bar as published, even though several of its individual patterns already match decisions Settlements has made independently.

| | |
|---|---|
| **Publisher** | Corvus Belli |
| **Currencies** | **Army Points** (abundant, integers) + **SWC** (scarce, 0.5 granularity) |
| **Depth of read** | Official N5.2 wiki + N3 rulebook cost figures (SWC); official N5.2 + N5 FAQ v0.0.0 wiki, full pass (Hacking/EW) |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.2 (SWC) |

---
## SWC — the derived second budget

**Type:** List · **Take:** ⭐ steal

> *"Support Weapons are the weapons or Special Equipment not included in the basic or standard equipment. These Support Weapons have a specific cost named Support Weapons Cost (SWC)… **In game terms, each 50 Army Points will provide 1 point of SWC** to spend on Troopers with Support Weapons. For example, in a standard 300 Point game, players will have 6 SWC points available."* **[FACT — official N5.2 wiki]**

- Every profile row carries **both** costs: `SWC` and `C`.
- **SWC granularity is 0.5**; values run 0, 0.5, 1 … 3.5, plus `+1`/`+2`.
- **Both Cost and SWC are Private Information** — your opponent may not ask what anything costs.
- Stacked alongside: **AVA** (per-unit availability caps), **Combat Groups** (max 10 order-generating troopers each), exactly one Lieutenant, and in N5 a hard **15-trooper cap**.
- N5 Reinforcements **splits the budget in both currencies** — *"assign a total of 100 points and 2 SWC to build their Reinforcements Section."*

**Why two currencies?** **[INFERENCE, well-supported]** Points alone cannot prevent the degenerate list, because Infinity's **order economy** makes cheap bodies individually mandatory. A single currency would force the designer to price HMGs so high nobody takes them. SWC lets them price the gun **cheaply in points** (a Fusilier HMG is only +8 points over a Combi) while **hard-capping how many exist**. **Points buy bodies and order count; SWC buys the right to have force-multipliers at all.** Two independent knobs on two independent failure modes.

**And the derived budget is the elegant part.** Because SWC is a function of points, it **auto-scales with game size** — no separate table per format. Half-point granularity on the scarce currency and integers on the abundant one is exactly right: the scarce currency needs resolution because you only get six of them.

**The load-bearing discovery — the same weapon costs more SWC on a better platform** **[FACT — N3 rulebook]**:

| HMG carrier | SWC | Points |
|---|:--:|---:|
| Fusilier (PanO line infantry) | 1 | 18 |
| Moblot / Govad | 1.5 | 29 |
| Janissary (Heavy Infantry) | 2 | 40 |
| Hsien (HI) | 2 | 61 |
| Squalo (TAG), MULTI HMG | 2 | 93 |

*Honest counter-example: the Missile Launcher is a flat 1.5 on both a 15-point Fusilier and a 49-point Father-Knight, rising to 2 only on top-tier HI. **Platform-scaling is a strong designer habit, not a stated rule.***

**For Settlements — the finding that matters.** Settlements has **already built an SWC equivalent**, but implemented it as **rank gates** rather than a second currency **[INFERENCE]**:

| SWC-like capability | How we gate it |
|---|---|
| **Orders** | Leader/Specialist only — the rank pyramid |
| **Extra-action skills** (Quick Shot, Dual Wield) | Tier gate |
| **24" range** | Heavy Ranged at Specialist rank |

That is a **legitimate and arguably better choice** for a game this size — rank gating needs no extra bookkeeping and reads off the model. **The recommendation is to keep it and state it as an explicit design principle, not to add a second battle currency on top of it.** See [[List Building]]. Note this is separate from the locked one-economy tenet: **Credits are the only currency the player ever sees**, and that isn't up for renegotiation.

---
## Profiles that pay you

**Type:** List · **Take:** ⭐ steal

Some profiles **grant** SWC rather than costing it **[FACT]**:

> *"Troopers whose SWC value has the + symbol will provide the player that many extra SWC points… it will not cost the player any SWC to field these Troopers."*

Typically gated behind fielding that model as **Lieutenant**. And Lieutenant options are priced **in SWC, not points**: a Ghulam HMG is SWC 1; the Ghulam *Lieutenant* HMG is SWC 0.5. **Joan of Arc as Lieutenant is +1 SWC — she pays you.**

**Why it works.** Corvus Belli uses the second currency as the dial for the **leader tax** rather than touching points at all. A negative price in a *scarce* currency is a strong incentive that costs the main budget nothing, and it steers list-building toward thematic leaders without a single restriction.

**For Settlements.** The transferable half is the shape: **a cost expressed in the constrained resource, not the abundant one, is a much sharper lever.** Our constrained resource is rank slots in the pyramid — so a "this Leader choice buys you back a Fighter slot"-style incentive is the analogue worth exploring in [[List Building]] and [[Factions]].

---
## What isn't published

**[NOT FOUND]** No formula, no spreadsheet, no credible community reverse-engineering of Infinity costs. Designer Gutier Lusquiños' published reasoning is qualitative and in-fiction: *"The Red Fury is designed as a light machine gun which is why it costs less SWC. It's more of an anti-personnel weapon than the Spitfire."* Costs are hand-set per profile row and iterated on playtesting.

**Verdict** **[CONSENSUS]**: four editions essentially unchanged. N4 rebalanced individual values; N5 kept the mechanic verbatim and extended it. The one recurring complaint is that **SWC value is table-dependent** — long-ranged support weapons are worth less on dense terrain. That is our own measured result too: `Crew Sim — Findings` put a **66-point swing** on terrain density alone. See [[Terrain]].

---
## The Hacking Device — a device grants a small, fixed menu of named Programs

**Type:** List · **Take:** ⚙️ adapt

A **Hacker** is an Automatic Skill, not a stat: *"Hackers may be equipped with a Hacking Device that will grant them access to certain Hacking Programs, depending on the type of Device they are using."* **[FACT]** The device itself is Comms Equipment, and each device type grants access to a **fixed, printed** list — nothing more, nothing less **[FACT — Hacking Device wiki page]**:

| Device | Programs granted |
|---|---|
| **Hacking Device** | Carbonite, Spotlight, Total Control, Oblivion |
| **Hacking Device Plus** | Carbonite, Spotlight, Total Control, Oblivion, White Noise, Cybermask |
| **Killer Hacking Device** | Trinity, Cybermask *(nothing else — a pure hacker-killer, no attack program that works on TAG/HI/REM)* |
| **EVO Hacking Device** | Assisted Fire, Enhanced Reaction, Fairy Dust, Controlled Jump *(pure support — no attack program at all)* |

On top of any device, a Hacker may carry named **Upgrade Programs** — *"custom-made software tailored to the style and preference of specific infowar operatives"* **[FACT]** — printed in brackets next to the model's name, the same way a weapon option is printed.

**Why it works.** "How good is this hacker" is answered once, at the catalogue level, not by a scaling stat. An EVO hacker is *mechanically incapable* of a killer attack and a Killer-device hacker is *mechanically incapable* of buffing a REM — no restriction text required, the capability is simply absent from that row of the table.

**For Settlements.** Touches [[Hacking#Modifiers — from gear & skills, not a hardening stat]], which already gestures at named hacking gear (*Breach Kit, Exploit Suite*) without saying what they'd actually grant. Infinity's answer — a device defines **access to a small menu of distinct effects**, not a bigger number — is the shape worth remembering if the parked deeper-hacking system (see [[Hacking#Parked — deeper hacking (a later version, do not build yet)]]) is ever revived: gate *which* named options a Breach roll can produce by which gear is carried, the way Infinity gates programs by device. The honest cost: Infinity supports this with **eleven** named programs across **four** devices; multiplying named hacking-effect types is exactly the kind of parallel-subsystem growth the project's anti-bloat tenet exists to prevent, and v1 [[Hacking]] is one generic INT test on purpose. Adapt the *shape*, not the *scale*.

---
## Hacking Area — the range mechanic is Zone of Control, not distance

**Type:** Hacking · **Take:** ⚙️ adapt

> *"In Infinity a Hacker's Hacking Area matches their Zone of Control, and the Zone of Control of Repeaters and Deployable Repeaters of either the Player or their Allies. In addition, if a Hacker is within the Zone of Control of an Enemy Repeater or Deployable Repeater, their Hacking Area includes all Enemy Troopers on the game table."* **[FACT]**

Range to a target is never measured in inches from the hacker — it's a **connectivity check**: are you inside a zone your side (or, through an enemy Repeater, the enemy's own zone) projects? A worked example on the wiki shows this in ARO: an active hacker with no line of fire to any enemy still triggers an **Oblivion ARO**, because they're standing inside the reactive hacker's Hacking Area via a Deployable Repeater. **[FACT]**

**Why it works, structurally.** It turns "can I even reach this target" into a single yes/no network-membership question instead of a distance measurement — genuinely well-suited to a subsystem that is explicitly *not* about eyesight (see the LOS-free ARO below).

**For Settlements.** Contrasts directly with [[Hacking#Range bands]], which measures **terminal → feature** in inches across four discrete bands (Close/Short/Medium/Long, max 24"). Infinity's model is richer — a single well-placed Repeater can, in principle, make **every enemy trooper on the table** a legal target from one Hacker — but that is exactly the kind of reach Settlements' own [[Hacking]] note keeps deliberately small ("v1 is deliberately small… one roll, one clean decision"). **[INFERENCE]** A connectivity-based range check is a fundamentally different *kind* of range mechanic than a distance band, and worth knowing exists as a design option — but importing the "whole table is reachable through one relay" half of it would fight the one-test bar directly: it turns every hack declaration into a table-wide network check rather than a local one. Log as a data point, not a candidate.

---
## Repeaters — a network relay either side can use, at a penalty

**Type:** Hacking · **Take:** ⭐ steal

> *"Repeaters extend the Hacking Area of all Hackers in the same Army List. Hackers within the Zone of Control of an enemy Repeater may use it to apply Hacking Programs against any enemy Hacker, but applying Firewall MODs (-3). There can be no reaction against a Repeater that is being used by an enemy Hacker, only against the Hacker, if possible."* **[FACT]**

A **Repeater** is automatic equipment carried on a model; a **Deployable Repeater** (`Disposable (3)`) can be dropped on the board like a mine. Neither can be shot to stop a hack going through it — *only the hacker can be targeted*. Third-party tactics commentary calls this out sharply: *"Repeaters are the terrain of the cyber battlefield, and engaging through one of your opponent's repeaters is like engaging when they have cover and you do not."* **[CONSENSUS]**

**Why it works.** A relay **either side can use**, at a flat, stated penalty (-3 Firewall) rather than "my network only," makes placing a Repeater a genuine two-edged risk instead of a pure buff — and pricing "using someone else's infrastructure" as one flat modifier avoids inventing a rule per network topology.

**For Settlements.** This is the single most transferable idea in the capture, because it lands on vocabulary [[Hacking]] and [[Infrastructure]] already have: terminals and Linked features, but **no relay/extension concept** — a terminal only reaches its own features within its own range bands; it can't project reach the way a Repeater does, and nothing currently lets a *captured* or *overloaded* terminal become a beachhead the other side can exploit. **[INFERENCE]** — worth flagging as a candidate for a future pass over [[Hacking]]/[[Infrastructure]], not proposed here: the shape (a network node either side can use, at a printed penalty that fits inside the existing ±3 cap) costs one clause and no new dice mechanic, which is unusually cheap for how much texture Infinity gets from it.

---
## Face-to-face hacking, and an ARO that doesn't need line of sight

**Type:** Reactions · **Take:** 📎 reference — independent convergence

> *"Enemies entering or acting inside the Hacking Area of a Hacker while remaining outside that Hacker's LoF and ZoC can be reacted to."* **[FACT]**

A hacking ARO is a genuine **face-to-face roll** — the wiki's worked example has a Reactive Trooper's **Carbonite** (WIP roll) opposed by the Active Trooper's own **Reset** (also a WIP roll), each side's die cancelling the lower value of the other. **[FACT]** A hacker can be answered *in kind*, too: a second worked example shows an enemy Hacker's **Oblivion** ARO racing the active hacker's own **Carbonite** declaration in the same exchange, both resolved as opposed rolls with Firewall MODs applied.

**Why it works.** This is a Reaction that fires **through the network, not through the eyes** — it doesn't need line of sight because it isn't the trooper's own senses reacting, it's the network the trooper is plugged into.

**For Settlements.** This is independent convergence with a decision already made and drafted: [[Hacking#Interrupt — contesting a hack]] states, almost word for word, the same design call — *"it bends two of the usual Reaction rules: it's declared as the enemy hacks (not after they finish), and it ignores the forward-180°/LOS requirement — you contest through the wire, needing only base contact with your own live terminal, not sight of the hacker."* Infinity ships the identical idea as an entire ARO category rather than one named exception, across four editions, without walking it back. **Read this as reassurance, not as a new idea to chase** — the existing Interrupt design is sound by the standard of the deepest published implementation of the same concept.

---
## Total Control — possessing a TAG, and the four guardrails that stop it being a walking death sentence

**Type:** Hacking · **Take:** 📎 reference

**Total Control** targets **TAG only**, Burst 1, PS 4, DA Ammo. **[FACT — Hacking Programs Chart]** A failed Saving Roll drops the target into **Possessed State [Null]** **[FACT]**:

- Cannot be activated or receive Orders from its owner's Order Pool; is treated as an **enemy** by its own side and an **ally** by the hacker's side.
- Fights instead for the **Combat Group of the trooper who hacked it**, without counting against that group's model cap.
- **Must use a fixed, generic replacement profile** — not its own: `MOV 4-4 · CC 13 · BS 12 · WIP 11` (ARM/BTS/STR/S stay the model's own). **[FACT]**
- **Counts toward neither player's Victory Points.**
- Cannot be part of a Fireteam.
- **Cancellation:** the owner may spend **1 Command Token**, no roll required, during their own turn — or the hacker's side can lose the state by successfully **Total Control**-ing it a second time.

Community counterplay for defending a TAG is concrete and cheap: *"start with a friendly model in base-to-base contact with it. This means that if the TAG is hacked then it immediately becomes Engaged in close combat, and has to therefore spend orders potentially having an ineffective slapfight instead of hosing down your backfield."* **[CONSENSUS]**

**Why it works.** Four separate guardrails stack: **(1)** scope — TAGs only, the rarest and most expensive unit type, never rank-and-file; **(2)** a **hostile, generic, worse-than-native profile** — a stolen war machine fights *worse* than its own crew would, never better; **(3)** **zero VP** either way, removing any scoring incentive to snowball off it; **(4)** a cheap, unconditional escape valve (spend 1 token, no roll).

**For Settlements.** This is the fully-shipped version of exactly the tail Ross's own team already reasoned through and **parked**. [[Hacking#Parked — deeper hacking (a later version, do not build yet)]] states it almost verbatim: *"The catastrophic 'steal the unit and walk it into lava' outcome is a tail you can't out-reward — bound it (System Shock) or quarantine it to duels; don't try to make features juicy enough to justify it."* Infinity's answer adds two guardrails the parked draft hadn't yet spelled out — the **generic-weak-replacement-profile** trick and the **zero-VP carve-out** — worth lifting alongside the already-drafted System Shock bound *if and only if* that parked system is ever revived. **The honest read:** even with all four guardrails, this is still a State, a replacement stat-line, a token-spend cancel, and a VP exception layered onto one effect — four sub-rules for one program. Ross's team parking this rather than building it now reads, after seeing the mature version, like the correct call rather than an under-baked one.

---
## Firewall — Comms Attack's version of Cover

**Type:** Hacking · **Take:** ⭐ steal

> *"Any enemy that declares a Comms Attack against a Trooper benefitting from a Firewall must apply a negative MOD to his WIP Attribute… A Trooper benefiting from a Firewall also applies a MOD of +3 to their Saving Rolls (SR) against Comms Attacks."* **[FACT]**
>
> *"The Firewall in a Comms Attack is the equivalent of Cover in a BS Attack, it hinders the Attack and aids the target's Saving Roll."* **[FACT — "Sibylla's Advice" designer-voice callout, official wiki]**

**Why it works.** Rather than invent a new "hack resistance" stat, Corvus Belli explicitly **reuses the shape of an existing subsystem** and renames it for the digital domain: same mental model (hinder the attack, aid the save), zero new rules literacy required once Cover is already understood.

**For Settlements.** This directly validates a design tenet [[Hacking]] already states outright: *"There is no separate 'hardened systems' stat; toughness is just a modifier… the global ±3 cap applies."* Infinity converged on the identical answer from the opposite direction — Firewall reads like a named stat but is implemented as nothing more than a flat modifier grant from gear. **Log this as confirmation the existing call is sound, not as a new idea to add.**

---
## Non-Hackable, ECM, and hunting the network — how a non-hacker force copes

**Type:** Hacking · **Take:** ⚙️ adapt

Three cheap, stackable soft counters exist rather than one hard one:

- **Non-Hackable** (Automatic Skill): *"cannot be the target of Hacking Attacks whose Requirements require the target have a specific Unit Type (HI, REM, TAG, etc.)"* **[FACT]** — a printed immunity tag, not a roll.
- **ECM** (Automatic Equipment): imposes a flat negative MOD on a named attack type when the owner is targeted by it, value printed per Unit Profile. **[FACT]**
- **Hunt the network.** Third-party tactics commentary lays out the meta directly: *"focus fire your opposition… engage by putting your entire burst into one enemy target at a time"*; bring an **Engineer** to repair Isolated/Immobilized troops; use a cheap, disposable model to physically **destroy the enemy's Repeater network**; and *"consider assassination… landing a drop trooper, impersonator, or infiltrator who can trade her life with that of an enemy lynchpin hacker."* **[CONSENSUS]**

**Why it works.** No single hard counter exists — instead a force with zero hacking investment gets a cheap floor (Non-Hackable tags on some units, ECM on others), and a force willing to spend a *little* more (an Engineer, a disposable repeater-hunter) can dismantle a hacking-heavy opponent's network directly, object by object.

**For Settlements.** Directly answers the brief's own question — *what stops hacking being an auto-include or a hard counter?* (cf. [[Kill Team#If you make it free, make it mandatory]]). Infinity's answer is "scale the counter-investment with the threat, and always leave a cheap floor," not Kill Team's binary. Touches [[Hacking]]'s own open **"hack-modifier ladder"** playtest dial directly.

**A genuine tension worth flagging, not resolving.** The same tactics article adds, as an aside: *"Hacking benefits from tight, closed spaces with lots of hook turns and vertical space. If you're consistently finding hackers impossible to engage that might be a sign that the tables you're playing on are too dense and you should open the map up some more."* **[CONSENSUS]** That runs the opposite direction from Settlements' own locked finding that **"terrain density is the single most powerful balance dial… density alone swung win rate 66 points."** **[INFERENCE]** These may not actually be the same axis — Infinity's complaint is that a *physical* counter-hacker needs line of sight to shoot a hacker, and dense terrain denies that; Settlements' own [[Hacking]] Interrupt is LOS-free by design (see above), so the same pressure may not transfer. Flagged, not resolved.

---
## Hackable by Troop Type, not by individual profile

**Type:** List · **Take:** ⭐ steal

The Hacking Programs Chart's **Target** column reads, verbatim, `TAG, HI, REM, VH, Hacker` — a printed **Troop Type** tag on the Unit Profile decides whether a model can be targeted at all by most attack Programs, not a bespoke sentence on every entry. **[FACT]** **Non-Hackable** (above) is the printed escape hatch for units whose systems are deliberately too primitive to qualify.

**Why it works.** "Which of my units can even be hacked" is answered once, at the type level, the same economy-of-rules-text Settlements already favours elsewhere (cf. [[Kill Team#Slots instead of prices for the long tail]]).

**For Settlements.** This is nearly identical, in shape, to a mechanic Settlements has **already shipped independently, at smaller scope**: [[Deployables#Family A · Turrets]] states *"There are no board-built turrets; every turret is a deployable. An enemy hacker can hijack one — deactivate it, lock it off their squad (Rewrite Killbox), or fire it at its own side (Turret Tamer)."* That is Settlements' own bounded version of "steal the enemy's own war machine," already scoped to one deployable category rather than TAGs/HI/REMs/Hackers broadly. The transferable, cheap idea: Infinity marks **which categories of unit are hackable at all** with one printed tag rather than one-offing it per structure — if [[Deployables]] or [[Infrastructure]] ever extends hacking's reach to **Robots** or **Exosuits** specifically (both named in the 2051 tech layer), a printed "Hackable" tag mirroring the existing turret-hijack shape is the cheap, already-precedented way to do it.

---
## Camouflage, Sensor, and the Multispectral Visor — a tiered detection ladder

**Type:** Detection · **Take:** ⭐ steal

**Mimetism** is a flat negative MOD on any enemy BS Attack or Discover roll against the wearer — *"does not apply to CC Attacks"* **[FACT]**. **Camouflage** lets its user deploy in, or enter, **Camouflaged State** — a marker stands in for the model. **[FACT]** **Sensor** is a one-Action area reveal: *"a Normal WIP +6 Roll (without applying Range or Mimetism MODs) to simultaneously Discover all enemy Troopers… in the Hidden Deployment or Camouflaged States, who are inside the user's Zone of Control"* — and it denies re-Camouflaging inside that zone. **[FACT]** The **Multispectral Visor** answers Mimetism in three priced, named steps rather than one binary unlock **[FACT]**:

| MSV level | What it neutralises |
|---|---|
| **L1** | Mimetism -3 → 0, Mimetism -6 → -3; LoF through Zero Visibility Zones at a flat -6; immune to Smoke Ammunition FTF |
| **L2** | All Mimetism / Visibility Zone MODs → 0 outright; LoF through Visibility Zones for free |
| **L3** | As L2, **plus** auto-succeed Discover vs Camouflaged targets, ignore Surprise Attack MODs, and **may BS Attack a Camo Marker directly** applying only its own printed MOD, no Discover roll first |

**Why it works.** Camouflage costs the wearer a flat, printed MOD; detection tech answers in the *same currency*, in graduated, priced steps — investing more in optics buys a legible, incremental return rather than an all-or-nothing tech flip, and even the top tier (L3) still costs an Action or a roll to fully neutralise a hidden target, never free vision.

**For Settlements.** A third, genuinely different shape for the stealth/detection want already flagged open, alongside [[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll]] (a state machine) and [[Spectre Operations#Covert Action and Cover Level — a decaying resource under scrutiny]] (a decaying resource). Infinity's version is the **cheapest of the three** to fit inside `1d10 + Stat + Mods vs 7+`: no new state track, no new resource — just a printed negative MOD on the hider and a printed positive MOD (or MOD-cancellation) on named optics gear, using the modifier vocabulary and **±3 cap** Settlements already has. Touches the not-yet-written Detection want (currently parked at [[Ideas Inbox]], no dedicated rules note) and [[Weapons]]/[[List Building]] for where an MSV-equivalent item would sit.

---
## Three editions of simplification — N3's five program families collapse into N5's two

**Type:** Hacking · **Take:** ⚠️ avoid — instructive, not by Corvus Belli's choice of complexity but by their own retreat from it

An official Corvus Belli forum community summary (2018, N3-era, hosted on CB's own forum but not itself an official rules document — **[CONSENSUS]**, not FACT) describes a much larger system than what N5.2 currently ships:

> *"There are different kinds of Hacking devices: Assault Hacking Device (AHD), Hacking Device (HD), Hacking Device Plus (HD+), Killer Hacking Device (KHD), Defensive Hacking Device (DHD), White Hacking Device (WHD) and EVO Hacking Device (EVO)."*
>
> *"Hacking programmes are broken down into five types SWORD, SHIELD, CLAW, GADGET and UPGRADE."* CLAW attacked HI/TAG/REM/Hackers; SWORD alone could deal physical damage between hackers; GADGET covered Supportware; **SHIELD** split further into passive **Army Shields** (*"EXORCISM allows you to cancel your TAG's Possessed state, HACK-TRANSPORT AIRCRAFT allows your Hacker to FTF an enemy's PH roll to drop with AD:3+, and U-TURN applies a -3 MOD to enemy Guided attacks"*) and reactive-only **Defense Protocols** (BREAKWATER, ZERO PAIN, COUNTERSTRIKE), each with their own narrow activation window.

**None of AHD, DHD, WHD, EXORCISM, U-TURN, HACK-TRANSPORT AIRCRAFT, BREAKWATER, or COUNTERSTRIKE appear anywhere on the current N5.2 wiki's Hacking Device, Hacker, or Hacking Programs Chart pages.** **[FACT — absence confirmed by direct page read, not inference]** The current game has **four** device types and only **two** labelled program categories (Upgrade, Supportware) — the rest are simply listed, unlabelled by family.

**Why it's instructive.** Corvus Belli is the one publisher in this entire hub with the resources, the dedicated playerbase, and the multi-edition runway to make a maximally deep hacking subsystem actually work at the table — and across three editions their own trend has been to **prune** program families and device types, not add them. That is the single strongest piece of evidence anywhere in this vault that "maximally deep hacking" and "fast, legible skirmish game" are in real tension, independent of Settlements' own worries about it.

**For Settlements.** This is the honest answer to the brief's central question. Judged against `docs/BLKOUT-RULES-ANALYSIS.md` §19's bar — *can it be one Action = one test = one clear effect?* — a **single** N5 hacking exchange mostly clears it (one Program declared, one face-to-face roll, one State applied). But the **system surrounding** that one exchange — a device-to-program grant table, a Hacking Area that can span the whole board through a Repeater chain, a family of stacking States (Immobilized-B / Isolated / Targeted / Possessed) each with its own cancellation clause, and a dedicated **Reset** action that exists mainly to patch all of it back to Normal in one roll — is exactly the parallel-subsystem weight the project's anti-bloat tenet exists to prevent, and even Corvus Belli's own editions have been paring it down, not up. **Recommendation, stated plainly:** Settlements' current v1 [[Hacking]] — one generic INT test, one Linked feature, one Interrupt exception — is already closer to the right size than anything in Infinity's own history, including Infinity's own most recent edition. This is a case where **"we cannot afford what the best published version of this looks like" is the correct, evidence-backed conclusion**, not a compromise to feel bad about.

---
## What it gets wrong

**The bookkeeping is the real cost, not any single rule.** Four separate named States can stack on one model from hacking alone (Immobilized-B, Isolated, Targeted, Possessed), each with its own activation trigger and its own cancellation clause, and community commentary confirms the stacking is real and punishing: *"if you are targeted, immobilized and isolated you take a -15 WIP to reset"* **[CONSENSUS]**. Tellingly, the **Reset** action — one roll that clears *every* current hacking state at once — reads like a patch that had to exist because the state list grew past the point of being individually trackable, not like a deliberately designed centrepiece.

**Edition-drift risk is real and was not resolved here.** The third-party tactics article cited above is written for **N4** and quotes flat damage numbers (Carbonite 13, Oblivion 16, Total Control 16, Trinity 14) that do not match the **N5.2** Hacking Programs Chart's PS-based values captured above — the two are presented side by side in the raw capture rather than reconciled, because reconciling them would require an N4 rulebook this pass didn't have. **[NOT FOUND]** — no primary N4 source was read to confirm exactly when the numbers changed.

---
## Evidence & confidence

- **[FACT]** tags above are quoted or paraphrased directly from infinitythewiki.com, Corvus Belli's own published rules reference, cited by exact page URL in `research/sources/infinity-hacking/source.md`.
- **[CONSENSUS]** tags mark the N3 forum community summary (CB-hosted, not itself an official rules document) and the third-party N4-era tactics article — both used only for edition-drift context and counterplay meta, never as a rules citation.
- **[INFERENCE]** is used for every place this note extrapolates a design implication (transferable shapes, the terrain tension, the connectivity-vs-distance framing) rather than reporting a published rule — flagged inline each time, per house rule.
- **[NOT FOUND]** — the exact edition (N3, N3.5, or N4) at which each Program's damage value changed was not tracked down; only that the N4-era figures and the current N5.2 figures visibly differ.

---
## Source

- Primary (SWC): official Infinity N5.2 wiki; N3 rulebook PDF for the cost figures. Long-form: `docs/POINTS-RESEARCH.md` §7.2, §2.
- Primary (Hacking/EW): official Infinity N5.2 wiki + N5 FAQ v0.0.0 (Oct 2025), 16 pages read in full — Quantronic Combat (Hacking), Hacker, Hacking Device, Hacking Programs Chart, Hacking Area, Repeater, Deployable Repeater, Firewall, Possessed State, Isolated State, Non-Hackable, ECM, Mimetism, Camouflage, Sensor, Multispectral Visor.
- Secondary, tagged CONSENSUS throughout: a Corvus Belli official-forum community summary of N3 hacking (inane.imp, 2018) for edition-drift; Thanqol Decadion, "Infinity Tactics: Cybersecurity," Tabletop Battles / Goonhammer, 2020 (N4-era) for counterplay meta.
- Capture: `research/sources/infinity-hacking/source.md` + `meta.json` (hacking/EW pass only — see frontmatter for why the SWC pass has no capture folder).
- Related: [[Wargaming Research Hub]] · [[Hacking]] (Interrupt convergence, Parked possession draft, range bands) · [[Deployables]] (turret hijacking as our own bounded possession analogue) · [[Infrastructure]] (network/terminal vocabulary a Repeater-style relay would touch) · [[Spectre Operations#The States of Awareness and Detection Mechanics — a full alert system, not a spotting roll]] and [[Spectre Operations#Covert Action and Cover Level — a decaying resource under scrutiny]] (sibling detection-mechanic data points) · [[Kill Team#If you make it free, make it mandatory]] (the hard-counter question) · [[Gaslands]] · [[Kill Team]] · [[List Building]]

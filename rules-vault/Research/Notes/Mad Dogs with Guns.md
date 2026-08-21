---
type: research-note
title: Mad Dogs with Guns
game: Mad Dogs with Guns — Wargaming in the Gangster Era
publisher: Osprey Games
designer: Howard Whitehouse & Roderick Robertson
depth: primary — full 116-page rulebook read in full
retrieved: 2026-08-20
source_url:
capture: research/sources/mad-dogs-with-guns/
tags: [settlements/research]
---
# 🎲 Mad Dogs with Guns

> [!abstract] In one breath
> A **Prohibition-era gangster warband campaign** in the Necromunda/Mordheim tradition — card-activated, D6-based, and openly built (per the designers' own Design Notes) to generate scenarios for gang warfare first and a business economy second. The core system is exactly as thin as advertised; what earns the book its place is the campaign layer — a two-tier bribery economy, a turf system built from repeatable generic businesses plus a handful of unique named landmarks, and a shared Public Outrage heat track. The escalating-bribery mechanic the project's prior summary of this book promised is real, but **narrower and more surgical than advertised**: a scoped, per-seat bidding war with a sideways spillover, not an economy-wide price rise.

| | |
|---|---|
| **Publisher · designer** | Osprey Games · Howard Whitehouse & Roderick Robertson |
| **Scale / format** | Gang-vs-gang skirmish, any headcount from a single figure to "carload upon carload of gunmen"; 28mm (Copplestone Castings' *Gangsters* range); city-wide monthly campaign turn |
| **Core resolution** | Card-driven activation (each player holds 7 cards of one suit, shuffled with the rest into one deck) + `D6 vs Stat, roll at or under to succeed` for most tests |
| **Depth of read** | **Primary** — full 116-page rulebook, all citations below by printed page number |
| **Raw capture** | `research/sources/mad-dogs-with-guns/` in the Settlements repo |
| **Source** | Osprey Games, 2017. ISBN 9781472819291 |

---
## Why it's here

This is the only book in the corpus that pairs a warband skirmish with a genuine political layer sitting *above* the turf economy — most territory-driven games in this vault ([[Oathmark]], [[Last Days Zombie Apocalypse]]) stop at "own the place, get the bonus." Mad Dogs adds a second, contested resource that isn't a place on the map at all: seats of civic corruption that gate a scenario-level tie-break (who gets raided this month), can spring an arrested crew member, and can move a shared heat track. It's the closest published shape to what Settlements' own Territory + Diplomacy split wants to be — which is exactly why the project's prior note on this book, written entirely from Ross's own paraphrase and not the rulebook, needed replacing before anyone designed against it.

---
## Turf, and the one named site

**Type:** Settlement · **Take:** ⭐ steal

Paradise runs four racket types — Booze, Prostitution, Gambling, Protection — and each neighborhood fields *"as many opportunities for each racket (called a 'business') as there are gangs in the city."* **[FACT — p.94]** So the generic tier scales with player count, not a fixed map. Every business comes with free guards scaled to its own output (see *Loot*, below) and, separately: *"The exceptions are the named businesses – the Paradise Brewery, Madame Louisa's, etc. There is only one of these businesses in the city."* **[FACT — p.94, verbatim]**

The prior version of this note claimed "one unique named site per type." Reading the actual racket chapter (pp.95–102), the distribution is uneven, not symmetrical:

| Racket type | Generic sites | Named unique site(s) |
|---|---|---|
| Booze | Low Dive, Speakeasy, Nightclub, Trucking Company | **Paradise Brewery** (1) |
| Prostitution | House of Ill Repute, Brothel, Gentleman's Club | **Madame Louisa's Diamond Escort Service** (1) |
| Gambling | Bookies, Numbers, Loan Sharks, Wire Service, Gambling Den, Gym, Casino | **Paradise Arena, Paradise Racetrack, Paradise Dog Track** (3) |
| Protection | (one generic entry, no sub-types) | **none** |

**[FACT — pp.95–102]** Protection is also the flat worst payer (`D6/2` Loot, $0 payoff) and is described outright as *"a good starting point for a small gang"* **[FACT — p.101]** — the designers clearly weighted the landmark count toward the rackets they wanted fought over, not spread it evenly.

**Why it works.** The generic tier makes the map fillable — there are always more speakeasies — while the landmark makes one specific site worth a campaign. Making the ratio *uneven* rather than 1:1:1:1 is itself doing work: it tells players which racket is the trophy (Gambling, three landmarks) and which is the entry-level grind (Protection, zero).

**For Settlements.** [[Territory]], [[Ideas Inbox]]. The generic/named split is still the piece worth stealing, but correct the shape: don't mandate exactly one named landmark per territory type. Let the *ratio itself* signal which territory type the campaign wants raided — a type with several landmarks reads as "this is where the fights are," a type with none reads as "this is where you start."

---
## Turf upkeep — the payoff that can foreclose a business

**Type:** Economy · **Take:** ⚙️ adapt

Every business carries a flat monthly **Payoff** — a bribe to the *local* cops, entirely separate from the city-official bribery below — and it is not funded by that business's own income: *"Payoff is a monthly bribe paid to the local cops to turn a blind eye on the illegal activities. This is a set fee and if the business doesn't make that much money, you'll have to get it from somewhere, or the cops will shut the business down. This means the business will make no money until the payoff is restored. After three months of no income, the business becomes independent and is up for grabs."* **[FACT — p.94, verbatim]** Figures: Low Dive $100, Speakeasy $200, Nightclub $300, Gambling Den $200, Casino $500, up to the Paradise Brewery's $900.

**Why it works.** A business's own income doesn't reliably cover its own payoff (a Low Dive nets `1D6-1` Loot = $0–500 against a flat $100 fee — fine most months, underwater on a bad roll), so an owner has to actively subsidize a losing site from the gang's central bank or watch it revert to independent and up for grabs in exactly three turns. It's a soft, automatic overextension check that applies to the market leader as much as anyone.

**For Settlements.** [[Territory]], [[Economy]]. Worth flagging precisely because it's easy to conflate with what's already been cut: this is **structure-level** upkeep, funded centrally, not the **per-head** upkeep the project already removed — a genuinely different shape. The honest objection: it's one more number to track per owned site every campaign turn, which is exactly the bookkeeping tax anti-bloat has been cutting elsewhere; it only earns its place if the three-month foreclosure clock does real comeback work for whoever's losing.

---
## Loot — the exchange rate, and the guards it buys

**Type:** Economy · **Take:** ⭐ steal

*"Each point of Loot is worth $100."* **[FACT — p.57 and again p.77, verbatim both times]** Loot comes from two channels: the monthly business-income roll, and whatever gets grabbed mid-scenario (a Smash and Grab literally puts 3–6 Loot objectives on the table to steal or destroy). The per-business dice are individually tuned, not flat — bottom tier (Low Dive, House of Ill Repute, Bookies, Numbers, Loan Sharks, Trucking Company) at `1D6-1`; middle tier (Speakeasy, Brothel, Gambling Den) around `2D6`; upper tier (Nightclub, Casino, Gentleman's Club, the two named Racetracks) around `3D6`; the named flagships (Paradise Brewery `5D6`, Madame Louisa's `4D6`) highest of all; Protection lowest at `D6/2`.

Defense is derived from the same income die rather than separately costed: *"a business needs 2 guards per D6 Loot that it produces."* **[FACT — p.94, verbatim]** A Paradise Brewery (`5D6`) defends itself with 10 free guards; a Bookies joint (`1D6-1`) with 2. Guards never leave the premises to raid elsewhere, but they're the defender's first line in any Raid on that specific site.

**Why it works.** A stated exchange rate plus a defense formula *derived* from the same die that sets income is a genuinely rare thing to find in a skirmish rulebook — a richer site is automatically harder to take, with no second stat to hand-tune.

**For Settlements.** [[Economy]], [[Territory]]. The 2-guards-per-D6-income formula is the cleanest single idea in this note — worth checking against whatever currently sets structure defense; if that's currently a flat number per structure type, deriving it from the structure's own income removes a second dial that needs independent balancing.

---
## Taking over a Racket — a completion bonus with a matching vulnerability

**Type:** Settlement · **Take:** ⚙️ adapt

Owning every business of one racket type in one neighborhood is explicitly a double-edged state: *"you are both more powerful and more vulnerable… you can increase the income of related businesses… by +1D6 Loot each. But another gang can take away an entire business type with a single Raid – by this point the stakes are high and entire neighborhoods are the battle ground."* **[FACT — p.104, verbatim]** Separately, stacking multiple businesses of the same type in the same neighborhood cuts their combined Payoff by −10% per additional site **[FACT — p.104]**, and unclaimed independent businesses are taken by a SMARTS-vs-GUTS intimidation roll, with simultaneous rival claims resolved by a battle for the site **[FACT — p.101, 103]**.

**Why it works.** The reward for total local domination is real (a flat `+1D6` to everything related) but it's paid for by turning the whole cluster into a single point of failure — one successful Raid strips the entire monopoly at once, rather than the leader losing it business by business. It's a comeback lever that only fires once a gang has already concentrated power, which is exactly when a comeback lever should fire.

**For Settlements.** [[Territory]], [[Scenarios]]. A genuine "bigger you get, bigger the target" mechanic worth weighing for a Territory cluster bonus. The honest cost: it requires tracking "does this gang own every site of this type in this neighborhood" as a live campaign-state check every turn — more bookkeeping than a flat per-site bonus.

---
## Bribery, and the price of corruption

**Type:** Campaign · **Take:** ⭐ steal — corrected and narrower than the prior write-up claimed

The project's own prior note on this book described a single, self-inflating price rising across the *whole* economy as gangs compete, built around the quoted phrase *"the crooked SOBs get greedier."* That phrase does not appear anywhere in the 116-page text — **[NOT FOUND]**, checked directly. It looks like Ross's own colourful paraphrase of the general idea, not a quote, and it shaped the old note into something broader and flatter than the actual mechanism. The real system is narrower and, honestly, cleverer.

**Two tiers of official, only one of them biddable.** *Non-exclusive* seats — the Mayor, the Police Chief, the City Editor — can each be bought by any number of gangs simultaneously at the flat listed rate, and Reporters are unlimited (a gang can run several). **[FACT — p.83–85]** Ties in a shared decision are broken by 1D6, high roll wins **[FACT — p.83]**. *Exclusive* seats — 3 Judges, 3 Police Captains (one per precinct), 12 City Councilors (one per district) — can each be held by exactly one gang at a time. **[FACT — p.83–84]** Only this tier is ever contested:

> *"If a gang wishes to buy an already-bought official, they may get into a bidding war with the current owner, bidding up the monthly payoff until someone calls quits."* **[FACT — p.86, verbatim]**

Then the actual escalation mechanism — the part worth stealing:

> *"If the bidding war is over positions that have several members (Judges, Police Captains, City Councilors, etc.), those officials who were not involved in the bidding may hear of the new rates and want the same. Each month roll against the official's SMARTS. If the official passes this test, he learned of the increase. The owning gang must match the new rate or release the official."* **[FACT — p.86, verbatim]**

**Answering the four open questions directly, now that the book has been read:**

- **Does the price rise globally or per-figure?** Neither, exactly — it rises **per seat, and spreads only sideways within the same office category.** A bidding war over Judge #1 can never touch the Mayor's rate or a Councilman's rate — only the other two Judges.
- **Does a bribe expire?** No passive expiration. It's an ongoing monthly subscription lost only by one of three named triggers **[FACT — p.86]**: *Failure to Pay* (miss a month, lose the seat); *Reports of Corruption* (a paid Reporter can roll SMARTS for an exposé; unless the City Editor squelches it, the target rolls SMARTS to survive or is replaced and the money already paid is simply gone); *Governmental Shakeup* (the Mayor can roll his SMARTS against any lower official's SMARTS to have them fired outright).
- **Can a rival outbid a figure you already hold?** Yes — explicitly, and only for the exclusive tier. That is the entire content of *Outbidding the Opposition*.
- **If so, does it drain everyone, or just the two richest?** **Neither.** A *third* gang holding, say, Judge #2 — who was never part of the Judge #1 bidding war between two other gangs — can still fail that gang's monthly SMARTS-hears-about-it check and be forced to match the new higher rate or lose their own Judge. It isn't the two richest who pay; it's whoever else holds a seat in the *same category*, rich or not.

Two more pieces the old note missed entirely. First, an entry gate ties the whole system back to hoarded wealth: every seat carries a Minimum Reputation to bid at all (Mayor 6; Judge/Police Chief 5; Councilman/Captain/Editor 4; Reporter 2), and Reputation itself is *"+1 to its Reputation for every each $500 that it has in the bank (i.e. not spent…)"* **[FACT — p.77, verbatim]** — so only a gang actively sitting on cash rather than spending it can even enter the bidding war for the best seats (see *Reputation*, below, for why this is a problem). Second, owning officials pays out directly in the **Something Must Be Done** roll-off that decides whose racket gets raided each month a Public Outrage trigger fires: Mayor and Police Chief each add +3, Police Captain +2, Judge and Councilman +1 **[FACT — p.84, 86]**; the City Editor can shift the underlying Public Outrage roll by ±2 and each paid Reporter by ±1, via their own SMARTS checks **[FACT — p.85]**.

**Why it works.** **[INFERENCE]** The real anti-snowball mechanism isn't "prices rise for everyone as the campaign goes on" — it's that the *scarce* tier (18 seats total: 3 Judges + 3 Captains + 12 Councilors) is a zero-sum resource whose price is set by whoever's willing to overpay for it, and that overpayment can ripple sideways onto a gang that never entered the auction at all. The tax lands on *concentration inside one office category*, not on wealth in general — a gang that spreads its bribery across different office types entirely dodges every spillover check.

**For Settlements.** [[Territory]], [[Diplomacy]], [[Economy]]. This is a *stronger* design than the flat "prices keep rising" version the old note credited it with, and cheaper to build: a scoped, category-contained bidding war with a sideways spillover check is far less bookkeeping than an economy-wide inflation tracker, and it still produces the "getting the best seat first raises everyone else's cost in that lane" dynamic that made the mechanic attractive in the first place. The gap to be honest about: the spillover only exists for a handful of genuinely scarce, exclusive-tier offices — a Settlements analogue (militia commanders, corporate security contractors, regional administrators, black-market brokers, federal remnants) needs to decide up front which offices are single-owner-scarce (worth a bidding war and spillover) versus shared-access-common (worth a flat, uncontested fee), because the interesting mechanic only exists on the scarce side.

---
## Reputation — the snowball the bribery economy doesn't fix

**Type:** Campaign · **Take:** ⚠️ avoid

Reputation is gained *"+1… for every each $500 that it has in the bank"* **[FACT — p.77]**, plus permanently from a lavish gangland funeral — +1 for a proper $500 send-off, +1 more per additional $200 spent **[FACT — p.79–80]**. Reputation gates hiring outside Muscle (Punks need Rep 1; Torpedoes need Rep 5) **[FACT — p.79]** and gates which city officials a gang is even allowed to bid on (Councilman/Captain/Editor need Rep 4; Judge/Police Chief need Rep 5; Mayor needs Rep 6) **[FACT — p.83]**.

**Why it's instructive.** **[INFERENCE]** The richer a gang already is, the higher its Reputation; the higher its Reputation, the more expensive muscle and more powerful officials it's *allowed* to buy — an uncapped, never-decaying wealth-gates-wealth loop running in the same campaign as the bribery system that's supposed to be the anti-snowball valve (above). Nothing in the rules caps or decays Reputation, so a gang that gets ahead early stays permanently gated in to the top tier of muscle and officials, regardless of how the bribery bidding wars play out.

**For Settlements.** [[Campaign]], [[Progression]]. Cite this the next time a gate-by-wealth mechanic is proposed anywhere in [[Territory]] or [[Diplomacy]] — it's a concrete instance of the failure mode: a flat, uncapped, non-decaying "richer gangs get better access" gate sitting right next to its own catch-up mechanic actively undermines it. Compare [[Necromunda and Mordheim#Underdog banding]], which scales its handicap off the rating *gap* specifically so this doesn't happen.

---
## Healing — spending money buys down your own risk of dying

**Type:** Campaign · **Take:** ⭐ steal

A wounded gangster loses total stat points (Light Wound 6, Wound 12, "It's Serious" 24) **[FACT — p.80]**, recovered over subsequent months at a rate set by the purchased care tier: Self-Care (free, heals 4/month, **+4** to the monthly Cripple Roll), Doctor Visits ($50/month, heals 6, **+2**), Hospital ($500/month, heals 8, **+1**), In-Home Doctor ($1,000/month, heals 8, **no modifier**). **[FACT — p.80]** Every recovery month, roll `2D6 + Cripple Roll Modifier`: 11 or under is fine, 12+ permanently costs the gangster 1 point off a still-injured stat, and boxcars kill outright regardless of care tier. **[FACT — p.81]**

**Why it works.** The Cripple Roll Modifier is the whole idea: spending more on recovery doesn't just heal faster, it directly buys down the flat probability of your own gangster dying or being permanently maimed that month, off the *same* number that sets the heal rate — no separate insurance mechanic required.

**For Settlements.** [[Damage]], [[Economy]]. A clean, minimal way to couple the campaign economy straight to the injury system. Worth comparing to whatever currently governs recovery cost and permanent-injury risk in [[Progression]] — if either is ever made spendable, this is the shape to check against: one modifier, two payoffs (speed and safety), instead of two separately-tuned numbers.

---
## Public Outrage — the heat track we already cut, recorded for the archive

**Type:** Campaign · **Take:** 📎 reference

A single citywide number, starting at 2, rises with visible violence (+1 per public gunfight, +2/+3 for citizen deaths, +1 for hostages taken, +2 for property destroyed by explosives, +2 if an official is targeted) and falls with quiet months (−2 if a month passes with no gang activity) or paid-for goodwill (−1 per $500 spent Influencing Public Opinion, or a Reporter's favorable story). **[FACT — p.87–88]** Each month, roll `2D6 + Public Outrage`: under 15 is fine, snake-eyes actively *reduces* it, 16+ triggers **Something Must Be Done** (the roll-off described under *Bribery*, above, deciding whose racket gets Police-Raided), and boxcars — or a high enough running total — permanently calls in 5 Feds, who raid indiscriminately from then on and can only be removed by wiping out an entire gang. **[FACT — p.88–90]**

**Why it's recorded, not recommended.** [[Territory]], [[Campaign]]. Settlements already tried and cut a Heat/Attention track. This is worth logging as a working example of the same shape (one shared number, rising with visible violence, escalating into a permanent consequence) in case the underlying want ever resurfaces — not as an argument to bring it back. The one piece worth remembering independently of the track itself is the **Something Must Be Done** resolution: rather than a fixed rule for who gets punished, every gang rolls `1D6` plus whatever officials it owns, and the winner *chooses which rival's business* eats the heat **[FACT — p.88]** — a competitive redirection roll-off is a cheaper answer to "who gets punished" than a fixed formula, independent of whether the track that triggers it is wanted.

---
## Hiding, Creeping, and noise — the stealth mechanic Zona Alfa didn't have

**Type:** Movement · **Take:** ⚙️ adapt

There is a real, if thin, stealth mechanic here — a genuine hit against the open want that came back **[NOT FOUND]** in [[Zona Alfa#Stealth and noise — searched for, and it isn't here|Zona Alfa]]. Creeping movement lets a figure *"move within 4″ undetected if opponent fails SMARTS to observe them."* **[FACT — p.15]** Separately, a stationary figure can actively Hide: *"Figures can hide by making a SMARTS roll and having appropriate cover – you can't hide behind a fire hydrant! Hidden figures cannot be seen (and thus cannot be attacked) by anyone. Hidden figures may move about in cover at the Creeping rate. Hidden figures will be revealed if they move out of cover, make loud noises (like firing a gun), or are spotted by enemies listening and watching for them."* **[FACT — p.17, verbatim]** A dedicated **Spot** action exists purely to hunt hidden enemies or objects via a SMARTS test. **[FACT — p.13]**

**Why it works.** **[INFERENCE]** Noise-breaks-stealth is stated directly rather than modeled with a separate detection radius or dice pool — firing a gun is named outright as one of the things that reveals a hidden figure, which is the "make noise on purpose" idea in one clause. It's the same insight [[Zona Alfa#Mission Objectives and Hot Spots — the Reaction Radius, and triggering a fight from range|Zona Alfa's Bolt Toss]] reaches from the opposite direction — bait, rather than betrayal.

**For Settlements.** [[Movement]], [[Terrain]]. Real precedent, but a thin one: one SMARTS roll to hide, one SMARTS roll to spot, no noise radius, no distinct "loud action" list beyond the single named example of firing a gun. It answers "does anything in the Prohibition-lineage skirmish corpus touch stealth" with a qualified yes, not the detailed system the open want is actually asking for — log it alongside Zona Alfa's confirmed absence as one more data point, not a design to copy wholesale.

---
## Core resolution and the card-driven turn

**Type:** Dice / Activation · **Take:** 📎 reference

Each player holds 7 cards of one suit (Ace, 2, 3, Jack, Queen, King, Ten), shuffled together with every other player's suit and both Jokers into one deck, drawn one at a time. Low cards (Ace–3) activate one figure (plus any ally within 2″); court cards (Jack/Queen/King) activate the *whole* gang at once; Tens activate civilians. **[FACT — p.12–13]** Any drawn card can instead be banked as a **Hold Card** (max 2) to interrupt an opponent's activation with one action of your own — and playing a second Hold Card trumps and goes first. **[FACT — p.13]** The first Joker is a warning (redraw); the second ends the turn and discards every unplayed Hold Card, unless it follows the first Joker immediately, in which case the round ends on the spot and the cops arrive. **[FACT — p.14]** Most tests are `D6 vs Stat`, rolling *at or under* the modified stat to succeed. **[FACT — p.20]**

**Why only a brief mention.** Card-driven activation with a bankable interrupt is a genre-conventional pattern rather than a novel solve for a problem Settlements has — comparable in shape to [[Zona Alfa#Initiative and Alternating Activation|Zona Alfa's Alert action]] — so it doesn't clear the bar for its own hub row. Recorded here for completeness per the read brief, not as a steal candidate.

---
## What it gets wrong

- **Reputation** (above) runs an uncapped, undecaying wealth-gates-wealth loop in the same book as the bribery system built to prevent exactly that snowball — the clearest internal tension found in the read.
- The designers say outright that the economy was never meant to bear much analytical weight: *"we wanted that system to be much more about creating scenarios for gang warfare rather than about the economics of running a full service illegal business empire… We really don't care if your speakeasy and poker parlor succeeds."* **[FACT — p.105, Design Notes, verbatim]** Treat every Loot die and Payoff figure as flavour-first, not a load-bearing balance formula — nothing here has the derivation rigor of, say, [[Song of Blades and Heroes#The Quality multiplier|Song of Blades and Heroes]] or [[Trench Crusade#Melee is built, ranged is eyeballed|Trench Crusade's melee costs]].

---
## Source

- Primary: Osprey Games, 2017. ISBN 9781472819291. Howard Whitehouse & Roderick Robertson.
- Capture: `research/sources/mad-dogs-with-guns/`
- Related: [[Wargaming Research Hub]] · [[Necromunda and Mordheim]] (same lineage) · [[Zona Alfa]] (stealth comparison, heat-track comparison) · [[Trench Crusade]] · [[Territory]] · [[Diplomacy]] · [[Economy]] · [[Campaign]] · [[Progression]] · [[Damage]] · [[Movement]]

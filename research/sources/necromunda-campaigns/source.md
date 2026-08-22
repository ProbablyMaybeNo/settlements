# Necromunda — Campaign Systems (NecroRAW capture)

Consolidated capture of the eight published Necromunda campaign systems plus
supporting arbitrator tools, scraped from **necroraw.com.ru** (a volunteer-run
Docusaurus site that transcribes campaign rules from ~24 official Games Workshop
books). `robots: noindex, nofollow` is set on every page, so `firecrawl_map`
returns nothing — every page below was reached by following in-page links from
the campaign index pages. **Do not confuse with `necroraw.ru`** (no `.com`) —
that domain is dead and now serves an unrelated adult link-farm.

Two load-bearing pages (Outlander "Settlements and Structures" p83 and "Setting
Up the Campaign" p64/67/68) were additionally cross-checked word-for-word
against `research/sources/necromunda/book-of-the-outcast.pdf` directly — see
the verification note at the end of this file. They match verbatim.

---

## 1. The Outlander Campaign
Source: *Necromunda: Book of the Outcast*

### Index — `/docs/campaigns/the-outlander-campaign/`
Four items: Using The Campaign (p62), Setting Up The Campaign (p64), Running
the Campaign (p69), Settlements and Structures (p83).

### Setting Up The Campaign — `/docs/campaigns/the-outlander-campaign/setting-up-the-campaign` (p64)

> Setting up an Outlander Campaign is a task that falls to the Arbitrator... The Outlander Campaign is divided into six campaign cycles, separated by a single cycle of downtime after the first three cycles, meaning the campaign will last a total of seven cycles.

**Founding Gangs.** Starting budget **1,000 credits**, any gang, unspent credits go to Stash.

**Starting Your Settlement.** Each gang gets a Settlement Roster sheet. First choice: **where** the settlement sits.

**Settlement Locations.** Five location types, each rated **Defence / Resources / Toxicity, 1–6**:

| Location | Defence | Resources | Toxicity |
|---|:--:|:--:|:--:|
| Factorum Run Off | 3 | 6 | 3 |
| Boneyard | 4 | 4 | 4 |
| Ghost Town | 2 | 5 | 5 |
| The Depths | 6 | 3 | 3 |
| Edge of the Hive | 5 | 5 | 2 |

Once chosen, a location cannot be changed (except in extreme circumstances) for the campaign's duration.

**Starting Structures.** All settlements start with two free Structures: an **Isotopic Fuel Rod** and a **Water Still** (both Supply). Additional Structures cost Materials (table below).

**Expanding Your Settlement.**
> During each post-battle sequence, gangs can expand their settlements, provided they have the Materials to do so... There is no limit to the number of Structures that can be added to a settlement during a single post-battle sequence, provided the requirements are met.

Location caps structure counts, independently, three ways:
> - A settlement may not have more Defence Structures than its Defence rating.
> - A settlement may not have more Building Structures than its Toxicity rating.
> - A settlement may not have more Supply Structures than its Resource rating.

### Settlements and Structures — `/docs/campaigns/the-outlander-campaign/settlements-and-structures` (p83)

> All Structures have three components: **Building (Type)**, **Benefits**, **Build Costs/Requirements**.

**Materials — three kinds:** Power, Sustenance, Salvage. Gained from scenario rewards or Structure Benefits.

**Supply Structures**

| Structure | Benefits | Build Costs/Requirements |
|---|---|---|
| Isotopic Fuel Rod | +10 units of Power | 15 Sustenance |
| Water Still | +10 units of Sustenance | 15 Power |
| Critter Farm | +15 units of Sustenance | 5 Sustenance, Critters (Defence) |
| Fungi Farm | +20 units of Sustenance | 20 Power, 10 Salvage |
| Gunk Tank | +5 units of Power and Sustenance | 5 Power, 5 Sustenance, 5 Salvage |
| Scrap Market | +10 units of any Material | 5 Power, 5 Sustenance, 5 Salvage, Scrap Mine (Supply) |
| Scrap Mine | +10 units of Salvage | 10 Power, 5 Sustenance |
| Scrap Reprocessing Plant | +20 units of Salvage | 10 Power, 20 Sustenance, Habs (Building) |

**Building Structures**

| Structure | Benefits | Build Costs/Requirements |
|---|---|---|
| Black Market | Reduce Legality of all Black Market items by 2 | 5 Power, 10 Salvage, Scrap Market |
| Bullet Hall | Add a Hired Gun free of charge | 15 Sustenance, 10 Salvage, Drinking Hole |
| Corpse Yard | +1 Supply Structure limit | 5 Power, 10 Sustenance, 10 Salvage |
| Doc Clinic | Remove up to 3 fighters from Recovery post-game | 20 Power, 10 Sustenance, 10 Salvage, Rogue Doc |
| Drinking Hole | −50% cost of Hired Guns and Hangers-on (round up) | 10 Power, 20 Sustenance, 20 Salvage, Habs |
| Gaol | +3 to Capture roll | 5 Power, 5 Salvage |
| Habs | +1 Building Structure limit | 10 Power, 20 Sustenance, 10 Salvage |
| Underhive Shrine | Always Home Turf Advantage | 10 Power, 5 Sustenance, 5 Salvage |
| Vault | Settlement cannot be a Settlement Raid target | 10 Power, 10 Salvage, Walls and Gates |
| Workshop | −50% cost of Defence Structures | 20 Power, 10 Sustenance, 10 Salvage, Ammo-jack |

**Defence Structures**

| Structure | Benefits | Build Costs/Requirements |
|---|---|---|
| Chasm | 6"×12" impassable terrain, defender-placed | 30 Salvage |
| Critters | Attacker subject to Horrors in the Dark | 30 Sustenance, 10 Salvage, Fungi Farm |
| Minefields | Up to 3 booby traps, ≥6" outside opponent's zone | 10 Power, 10 Salvage |
| Outpost | ±2 on scenario-determination roll | 5 Power, 10 Salvage |
| Walls and Gates | Walls around deployment zone | 50 Salvage |
| Watchtower | Watchtower in deployment zone | 20 Salvage |

### Running the Campaign — `/docs/campaigns/the-outlander-campaign/running-the-campaign` (p69)

Three phases: **Development** (3 weeks) → **Downtime** (1 week) → **Expansion** (3 weeks).

- Development: settlements can't be raided (no Settlement Raid / Market Mayhem / Stealth Attack); resource scenarios pay double Materials.
- Downtime effects: Fighters Recover, Captives Returned, Promotions, Fresh Recruitment (250cr), **Settlement Maintenance** — scrap up to 3 Structures (get half Materials back) and immediately build 3 new ones.
- Expansion: settlement raids now legal.

Scenario-selection table keys off **who has more Structures** (2–3 / 10–12 give the Structure-leader or Structure-trailer the choice).

Triumphs: Lord of the Badzones (most Structures), Outland Raider/Defender, Scavenger, Master of Coin (highest wealth).

---

## 2. The Dominion Campaign
Source: *Necromunda Core Rulebook (2023)*

### Index — 8 items: Using, Setting Up (p166), Running (p169), Territories (p171), List of Territories (p173), + 3 faction-specific supplements (Palanite Enforcers, Badzone Enforcers, Ash Waste Nomads).

### Setting Up The Campaign (p166)

Seven cycles (six + one Downtime), same shape as Outlander.

**Determine Territories** — count scales with player count:

| Players | Territories |
|---|:--:|
| 3 | 9 |
| 4 | 12 |
| 5 | 15 |
| 6 | 18 |
| 7 | 21 |
| 8 | 24 |

Generation method: draw one Territory per represented House from that House's Enhanced-Boon deck first (guarantees relevance), then fill the rest randomly from the remainder; discard what's left over.

**Issuing and Accepting Challenges.** One challenge per gang per cycle. Cycle 1: random order. Later cycles: **ascending Gang Rating order** (lowest challenges first) — a built-in first-mover advantage for the underdog. Occupation phase: challenger nominates an *uncontrolled* Territory (or, if none remain, a *controlled* one). Takeover phase: challenger nominates a *controlled* Territory. Decline a challenge → challenger auto-claims the Territory.

Scenario Selection Table keys off **Territory count** (2–3 / 10–12 rows again give the extreme player the choice; a 4-9 result plays specific paired scenarios by phase).

### Running the Campaign (p169)

**Occupation phase** (3 cycles) → **Downtime** (1) → **Takeover phase** (3 cycles). Occupation: only unclaimed Territories can be won. Takeover: only controlled (i.e., someone else's) Territories can be fought over.

Downtime: Fighters Recover, Captives Returned, Promotions (3+ Advancements this edition, not 5), Fresh Recruitment (250cr).

Triumphs: Dominator (most Territories), Slaughterer (most OOA+Wrecked), Creditor (Wealth), Warmonger (most battles), Powerbroker (Reputation).

### Territories (p171)

Every gang has an unlosable **Settlement Territory** (their hideout) that can never be staked.

**Boon types:** Income (credits to Stash), Recruit (free fighter/Hired Gun/Hanger-on, still counts toward Rating/Wealth), Equipment (added to Stash, lost if Territory lost), Reputation (flat add, lost if Territory lost), Special (bespoke rule).

**Enhanced Boons.** Territories carry a base Boon *plus* an upgraded Boon for named Houses — *"an Escher gang might be able to grudgingly sift some valuables from a Refuse Drift, but to a Cawdor gang the same refuse pile is a hoard of hidden relics."* Enhanced Boons of the same category (e.g. Reputation) **replace** the standard version; different-category Enhanced Boons stack alongside it.

Gaining Territory: win a battle it's staked on, or trade one for a Captive.

### List of Dominion Campaign Territories (p173) — sample of 25 (full deck is 52, one per playing card)

Representative entries (Boon / Enhanced Boon for the named House):

- **Settlement** (Ace ♦): Income D6×10, +1 Reputation, Recruit (2D6, 6s = free Juve, double 6 = free Ganger).
- **Old Ruins** (2♦): Income D3×10 (+1 per Dome Runner).
- **Rogue Doc Shop** (3♦): Outlaw gets Income D6×10; Law-Abiding gets a free Rogue Doc Hanger-on.
- **Promethium Cache** (4♦): 3 fighters get free incendiary charges; re-roll Ammo tests for Blaze weapons.
- **Wastes** (5♦): Special — choose the Territory at stake in Occupation phase; conditional free Ambush in Takeover.
- **Refuse Drift** (9♦, Cawdor): Income 2D6×5 with a double-roll injury risk for non-Cawdor; Cawdor gangs get +1 Rep and no risk.
- **Corpse Farm** (10♦, Cawdor): Income scales with fighters *deleted* from either roster last battle — Cawdor gets double the rate.
- **Bone Shrine** (J♦, Cawdor): Cawdor gets +2 Rep (vs +1) and 4D6×5 income (vs 2D6×5).
- **Drinking Hole** (Q♦, Delaque): re-roll failed Cool tests (with an addiction-marker downside); Delaque enhanced version can inflict a −1-to-hit "Intoxicated" marker on 3 enemy fighters.
- **Gambling Den** (K♦, Delaque): card-draw income minigame; a Joker means paying out all income to a random rival gang.
- **Needle Ways** (A♠, Delaque): grants Infiltrate to up to 3 fighters (6 for Delaque).
- **Synth Still** (2♠, Escher): treats chem/gas/toxin items as Common; Escher enhanced halves their cost too.
- **Stinger Mould Sprawl** (3♠, Escher): re-roll one Lasting Injury per battle; Escher can also remove one entirely, including Memorable Death.
- **Slag Furnace / Fighting Pit / Smelting Works** (Goliath): income + free Hive Scum recruitment + Reputation, several stacking with each other if held together.
- **Mine Workings** (8♠, Orlock): put Captives to work the mine for extra income instead of ransoming them, at the cost of never being able to Sell them to the Guild.
- **Tunnels** (9♠, Orlock): deploy up to 3 (6 for Orlock) fighters via tunnel-entrance markers, arriving on a 4+ each turn.
- **Generatorium** (J♠, Van Saar): controlling player can force Pitch Black rules mid-battle, which self-cancels on a 5+ each End phase.
- **Archaeotech Device / Tech Bazaar** (Van Saar): free weapon Traits (Blaze/Rad-phage/Seismic/Shock, plus Unstable) and a Haggle post-battle action for cut-price Rare gear.

**Full text of all 25 rows captured in the working session; not reproduced in full here for length — see the working transcript. The mechanism (base Boon + House-specific Enhanced Boon, drawn one per represented House first) is fully captured above.**

---

## 3. The Law and Misrule Campaign
Source: *The Book of Judgement*

### Index — 8 items: How the Campaign Works (p36), Setting Up (p40), Running (p44), Pre/Post-battle Sequence (p52), Rewards of Infamy and Duty (p60), Ending the Campaign (p62), Intrigues (p63), Rackets (p72).

### How the Campaign Works (p36)

Fought over control of **Rackets**, not territory tiles. Each battle stakes one Racket.

**Alignment: Law Abiding or Outlaw**, declared at the start. Some gang types are locked (Chaos Cultists always Outlaw; Palanite Enforcers always Law Abiding); House gangs and Genestealer Cults can be either and can switch.

Effects split cleanly: Law Abiding gangs can Claim Bounties on captured Outlaws, trade Captives only with other Law Abiding gangs, hire non-Outlaw support, have restricted Black Market access (free Trading Post access); Outlaw gangs are the mirror image (free Black Market, restricted Trading Post, every fighter has a bounty on their head, can form Criminal Alliances).

**Changing Alignment** — two paths:
1. **Forced**: claim an Intrigue from the wrong category and fail the resulting Alignment check.
2. **Declared**: once per campaign, just tell the Arbitrator.

Switching costs all current Hangers-on (not Brutes) and forces an Alliance re-test at +3 to the roll.

### Intrigues (p63)

Draw 3 Intrigue cards per battle (step 4 of pre-battle sequence), keep face-down, claim any time criteria are met by picking the card up. **26 named Intrigues**, one per card in a half-deck (Diamonds = Outlaw category, Spades = Law Abiding category), each with a **Category, Alignment Test die** (D6 to 4D6, scaling with how big the reward is), a **Reward** (Reputation, credits, or a special effect), and **Criteria** (an in-battle action, e.g. perform an action twice, take out the enemy Leader, plant a bomb). Claiming an off-category Intrigue risks an Alignment check (the listed die) during post-battle step 2; failing it flips your alignment.

Designer's note: don't stack other sub-plot systems on top of Intrigues — it overloads the game.

**Sample of the 26** (full 26 captured in the working transcript):
- *Wreck The Place* (Outlaw, D6, +1 Rep): perform Vandalise twice in the enemy zone.
- *Blow It Up!* (Outlaw, 3D6, +4 Rep): plant and detonate a bomb at battlefield centre.
- *The Price of Peace* (Law Abiding, D6, +4 Rep): bribe the opponent 250cr (not from Wealth) to forfeit outright.
- *Bring Them In Dead Or Alive* (Law Abiding, 4D6, 50cr/kill): only claimable vs an Outlaw gang.
- *Reveal The Imposter* / *Retrieve The Informer*: mirror-image Intrigues where a random enemy/friendly fighter becomes a temporary imposter fighting for the other side.

### Rackets (p72)

Same Boon taxonomy as Dominion Territories (Income / Recruit / Equipment / Special), **plus Linked Rackets**: each Racket lists 1–2 "linked" Rackets, and holding one or both linked Rackets upgrades the base Boon to an **Enhanced Boon** — almost always a bigger income die (e.g. D6×10 → 2D6×10 with one link → 3D6×10 with both), occasionally a qualitative special (e.g. controlling both linked Rackets for *Whisper Brokers* lets you choose your battle's scenario, or auto-win an Ambush scenario on a passed Intelligence check). This creates a **synergy graph** across ~26 named Rackets rather than a flat list of independent bonuses — e.g. *Narco-distribution* links to *Out-Hive Smuggling Routes* and *Ghast Prospecting*; holding all three multiplies one gang's income relative to a rival holding the same three scattered.

**Guild Bond Rackets** (Water/Slave/Promethium/Coin Guild etc.) are mutually exclusive — a gang can hold only one at a time — and pay differently depending on alignment (Law Abiding gets a Guild alliance and a themed Entourage; Outlaw gets free Bounty Hunter + Hive Scum instead).

### The Rewards of Infamy and Duty (p60)

**Reputation is a continuous, bracketed reward ladder, separately tracked per alignment.** Six brackets (1-4, 5-9, 10-14, 15-19, 20-24, 25+), each granting an Outlaw-side Boon *and* a Law-Abiding-side Boon (Black Market access tiers vs Bounty-claiming tiers). Boons are **lost automatically** if Reputation later drops below the threshold that granted them.

**Changing Alignment costs 3 Reputation immediately**, and swaps out every currently-held Reputation Boon for the new alignment's equivalent bracket.

### Ending The Campaign (p62)

Fixed end (when the Takeover-phase clock runs out). **Five Triumphs** (Racketeer/Hit Man/Financier/Muscle/Lord of Law or Misrule), each worth **exactly 1 point** toward **"Weighing All in the Balance"** — the side (Law or Misrule) with more Triumph-points overall wins the campaign's thematic verdict, independent of who "won" individually. Ties on a single Triumph award no one that Triumph.

**Splinter gangs**: normally you can't reuse an old gang in a new Law and Misrule campaign, but a **Champion can go solo**, becoming a new gang's Leader, keeping their gear/Advancements/injuries, paid for at their existing Credits value; Juves/Specialists can follow as Champions, Gangers as Gangers. New gang still obeys normal composition rules and the normal starting-credit cap.

---

## 4. The Uprising Campaign
Source: *Necromunda: Apocrypha Necromunda (2024)*

### Setting Up The Campaign (p76)

Three-way alignment: **Order / Chaos / Unaligned**, not two. Some gang types are locked to a side (Corpse Grinder/Helot Chaos Cult → Chaos; Palanite Enforcers/Genestealer Cults → Order); everyone else picks, including staying Unaligned.

Asymmetric per-side perks:
- **Order**: re-roll credit-reward dice; +1 extra fighter when defending.
- **Chaos**: +1 extra Meat (a resource) per scenario reward; +1 extra fighter when attacking.
- **Unaligned**: +1 extra Reputation on any scenario reward; Leader gets bonus XP if they survive undefeated. (The fence-sitter gets a *different kind* of catch-up, not a straight resource bonus.)

Changing sides is a hard, one-way, condition-gated flip (3+ fighters turned to Chaos Spawn ⇒ Order gang falls to Chaos; 3+ Captives voluntarily returned by captors ⇒ Chaos gang tips toward Order) — no free "declare it" option like Law and Misrule.

**Territory-flip threshold**: a battle only changes Territory control if the winner inflicted **at least 3× as many Out-of-Action results** as they suffered. Below that ratio, a win is still a win (Rep, XP, credits) but nothing changes hands. This is a **decisive-victory gate** distinct from underdog banding — it stops salami-slicing wins from snowballing map control.

---

## 5. The Succession Campaign (Aranthian Succession, 4 parts × 5 items each)
Source: *The Aranthian Succession — Cinderak Burning* et al.

Structured as **four narrative chapters** (Cinderak Burning → Road to Temenos → Fall of Helmawr → Reconquest of Primus), each its own mini-campaign with its own Using/Setting-Up/Running/scenario pages plus a chapter-specific territory reskin.

### Sympathisers (Cinderak Burning, p65)

**Territories renamed and reflavoured, not redesigned.** ~26 named "Sympathiser" factions/guilds, each with a standard Boon (mostly Income, occasionally Special) **plus** a second, separate **"Spark of Rebellion Phase"** bonus that only applies during that specific campaign phase — i.e. the *same* Territory pays two different things depending which of the four chapters is active. This is the clearest evidence in the whole product line that **Territories/Rackets/Sympathisers/Road Sections are one reusable chassis**, reskinned per book: a name, an owner-only Boon, and (increasingly, in later books) a second phase- or condition-gated Boon layered on top.

---

## 6. Underhells Campaign (7-item, multiplayer version)
Source: *The Book of Desolation*

### Madness, Desolation and Darkness (p71)

**Three independent hazard axes**, each with exactly **three severity tiers**, and each tier is locked to one of the campaign's three main phases:

| Phase | Madness level | Desolation level | Darkness level |
|---|---|---|---|
| Incursion | Ghosts of the Dead | Limited Trade | Heavy Skies (Visibility ≤18") |
| Delving | Echoes in the Abyss | Crane Cities | Toxic Deeps (Visibility ≤12") |
| Survival | Shadow of the Broodmind | Cut Off From The World | Stygian Depths (Visibility ≤9") |

- **Madness** governs how the existing Broken condition escalates to a second, worse **Insane** condition (which, at the worst tier, replaces Broken outright) — a genuine second fear-tier layered on the game's existing Nerve/Broken system, not a bolt-on new track.
- **Desolation** throttles trade access (Rare/Illegal ratings inflate by +2 to +6, differently for the two playable factions) — resource scarcity escalates with the same three-tier structure.
- **Darkness** is a flat visibility cap that tightens each phase.

### Running the Campaign (p67) — territories and the exploration-point race

Five phases: **Incursion** (variable length) → Downtime → **Delving** (variable) → Downtime → **Survival** (variable).

**Territories are held for exactly one cycle, then discarded and re-rolled** — representing moving camp — rather than kept and grown. Multiple gangs can hold the same Territory simultaneously.

**Phase advancement is a pooled threshold, not a calendar.** Gangs earn **Exploration points** from battles (win or lose). When the *sum across all players* reaches **3× the player count**, the phase ends immediately — regardless of whose battles produced them. Unspent Exploration points are then spent (or lost):

- Up to 5 points → D3×10 credits of gear each.
- 2 points → choose your next Territory instead of random.
- 6 points → gain a *second*, longer-lived Territory that survives to the end of the phase instead of being discarded each cycle.

This makes the whole table's aggregate play speed decide when the campaign moves on — a slow table stretches every phase; a fast one burns through content quickly — and gives players a real save-vs-spend decision on a currency that's about to evaporate.

---

## 7. The Ash Wastes Campaign
Source: *Necromunda: Ash Wastes Rulebook*

### Setting Up The Campaign (p114)

**Territories are edges in a graph, not nodes.** Each of the 36 named **Road Sections** connects two places (a fixed location or another Road Section); owning an *unbroken chain* of Road Sections between two named locations creates a **Trade Route**, which pays a *separate, bigger* bonus on top of each individual Road Section's income. **Multiple gangs can hold the same Trade Route simultaneously** by routing through different Road Sections. Two gangs start with 2 random Road Sections each; the deck is sized at "≥4 per player."

**Raiders vs Traders is a built-in faction split**, not a variant: Outlaw gangs and Ash Waste Nomads may be designated **Raiders**, who get the *same* per-Road income but disrupt Trade Routes instead of benefiting from them, earning a separate **Raiding Bonus** off the same route — every route table entry lists both a Trading Bonus and a Raiding Bonus.

---

## 8. Other Campaigns

### Turf Wars (legacy, *Gang War* / *Gang War 3*, pre-Dominion N17 system)

The predecessor chassis Dominion replaced. Notable structural DNA that **carried forward**:

**Ending a Turf War (p25)** — the earliest version of several mechanisms that reappear, near-verbatim, in later books:
- **Apotheosis**: the final Cycle of a Turf War adds three temporary rules — **Desperation** (the lower-Reputation gang rolls 2D6 and discards the highest on Bottle tests — a catch-up mechanic scoped *only* to the campaign's last stretch, not the whole run), **Consolidation** (losing gang's Turf Size shrinks by 1), **Ignominy** (a lower-Reputation winner steals Reputation from a higher-Reputation loser).
- **The Showdown**: a final, winner-take-all battle between the two highest-Reputation "Top Dogs," with automatic-pass Bottle tests. Winner becomes the Zone's **Overlord**.
- **Offshoot Gangs**: the *original* version of the splinter-gang mechanic later reprinted almost word-for-word in Law and Misrule (2023) and the Core Rulebook's Perpetual Campaigns section (2023) — pick one Champion as a new Leader, keep gear/Advancements/injuries, pay full cost, add up to 2 Juves and half the Gangers, fill the rest from a fresh 1,000cr budget.
- Existing gangs re-entering a new Turf War have their **Gang Rating hard-capped** (2,000, or 3,000 for the previous Overlord) by forced fighter retirement — a rare *mandatory* reset rather than an optional one.

### Arbitrator Tools — Campaign Variants (Core Rulebook, p226)

**Twelve official variants**, all dials on the *same* Dominion chassis, each isolating one structural lever:

| Variant | What it changes |
|---|---|
| Old Kingdoms | No Occupation phase — start with Territory already held, only Takeover phases |
| Into The Unknown | Territories drawn face-down; revealed only when staked |
| **Escalation Campaign** | **Removes credit rewards entirely.** Territories/scenarios pay everything *except* credits; gangs get a flat 250cr/battle (capped 500cr/week) regardless of outcome — win or lose, the money is the same |
| Classic Campaign | Reverts to blunter, older-edition equipment/weapon rules; no Hangers-on/Brutes/gang tactics; territory changes hands only on a 3× OOA ratio (same threshold Uprising uses independently) |
| Ironman Campaign | 3,000cr one-shot gang, **no replenishment ever** — no new recruits, no equipment purchases, campaign ends when only one gang can still field fighters |
| Dome Rush | No held Territory at all — a single shared Territory refreshes weekly and pays *everyone* simultaneously; winning a Territory battle converts straight to D6×50 credits instead |
| Last Gang Standing | Single shared Territory, multi-player free-for-all every battle, permadeath (no Lasting Injury table — OOA = gone), a Bottle-out costs D3 random fighters |
| Hive Empires | Full map-graph metagame — zones linked to zones, must be adjacent to attack, holding a zone = holding its Territory/Racket |
| Nomads of the Underhive | Deliberately poor: 700cr start, ≤100cr/week income cap, gear capped at Rare/Illegal(10), forced to discard down to 1 Territory every week |
| Helmawr's War | Two-side team campaign (Outlaw vs Deputised); only Outlaws start with Territory; deputised side wins by capturing all of it |
| **Perpetual Campaigns** | Loop Occupation→Downtime→Takeover indefinitely; **crew-size cap scales directly with Gang Rating** (10/15/20/25 fighters at ≤1000/2000/3000/3001+cr); Territories can be forced to "refresh" each loop, capped per-player at 1 retained Territory per full 1,000cr of Rating |
| Semi-Perpetual / Splinter | A **Triumph-to-legacy-bonus table** — each of the five Triumphs from the *previous* campaign grants a small, specific starting bonus in the *next* one if you carry over fighters (e.g. Dominator → one extra random starting Territory; Creditor → +100cr starting Stash) |

**Splinter Gangs is reprinted a third time here**, verbatim to the Turf Wars (2017) and Law and Misrule (2023) versions.

### Underdogs — House Patronage (Core Rulebook, p238)

The **current (N23) core-rulebook replacement** for scaling "extra gang tactics" as the underdog bonus. **Underdog** = ≥400cr behind on Gang Rating (or starting-crew credits). For every full 100cr of gap, the Underdog gets **100 "House Patronage" credits**, spendable *that battle only* on a fixed menu:

| Benefit | Cost | Cap |
|---|---|---|
| Random extra gang tactic | 100cr each | 0–5 |
| Chosen gang tactic | 200cr each | 0–2 |
| Random Underdog gang tactic | 200cr each | 0–4 |
| Chosen Underdog gang tactic | 400cr each | 0–2 |
| Temporary Brute/Hanger-on hire | varies | unlimited |
| Temporary House Ganger hire | varies | 0–3 |
| Temporary Juve hire | varies | unlimited (0–1 for Enforcers) |
| Temporary Dramatis Personae | varies | 0–1 |
| Temporary Bounty Hunter | varies | 0–1 |
| Temporary House Agent | 80cr | 0–1 |
| Temporary Hive Scum | varies | 0–5 |
| +1 XP per model this battle | 400cr | 0–3 |

Everything hired this way is **temporary** — not added to the permanent roster, can't group-activate, doesn't count for Bottle checks. This is a direct evolution of the mechanism the existing vault note ([[Necromunda and Mordheim#Underdog banding]]) describes from the older edition (extra *gang tactics cards* scaling with the rating gap) into a full **spendable currency** with a fixed shopping list, still gap-scaled, still self-zeroing at parity.

---

## Cross-check against the primary PDF

`research/sources/necromunda/book-of-the-outcast.pdf` (140pp), pages verified by direct `fitz` text extraction:

- **p67** ("Starting Your Settlement", "Settlement Locations") — matches the NecroRAW capture word-for-word, including all three Location rows checked (Factorum Run-off, Boneyard, Ghost Town).
- **p68** ("Maps and Environments", "Starting Structures", "Expanding Your Settlement") — matches verbatim, including the "no limit to the number of Structures... during a single post-battle sequence" line and the three location-based caps.
- **p83** ("Settlements and Structures") — matches verbatim, including the three Materials types and the three-component Structure format.
- **p85** (Structure tables) — every row (Supply/Building/Defence, 24 entries) matches the NecroRAW table exactly, cost-for-cost.

**Conclusion: the Outlander settlement material is [FACT], directly verified against the primary source, not resting on the wiki consolidation alone.**

---
type: research-note
title: Necromunda Homebrew Campaigns
game: Necromunda — homebrew and community campaign layer
publisher: Community / fan-authored (several historically hosted by Games Workshop's own fan-content channels)
designer: Multiple — Dalga Faik & Nick Piachaud; Torben Kastbjerg; Kacper Kuc & Alexander Lunde; Goonhammer.com; and others credited per section
depth: community reconstruction — 17 of ~94 library PDFs read, curated for deals/betrayal, the Arbitrator role, and cross-document convergence
retrieved: 2026-08-22
capture: research/sources/necromunda-homebrew/
tags: [settlements/research]
---
# 🎲 Necromunda — the homebrew and community campaign layer

> [!abstract] In one breath
> Seventeen fan campaigns, read for what the *official* rules left open. The single best find is
> **[[Necromunda Homebrew Campaigns#Striking a Deal — a one-roll table with a hidden hedge for betrayal|Striking a Deal]]** — the only source in this vault that gives alliance and betrayal actual dice
> teeth, at the cost of one D6 roll and an honest player to hide it. The bigger structural finding is
> the **Arbitrator** — a designed GM position that recurs, unprompted, in nearly every non-trivial
> homebrew campaign, and has clearly evolved well past "settles disputes" into curating rotating NPC
> pools, running dual-mode PvE monsters, and holding a costed wildcard slot for whatever the rules
> didn't anticipate.

| | |
|---|---|
| **Publisher · designer** | Community-authored; **[NOT FOUND]** whether every source here is purely fan-made — `arbitrator-campaign.pdf` reads as GW studio content, flagged below |
| **Scale / format** | Campaign-layer supplements only — no core combat rules touched |
| **Depth of read** | **Community reconstruction.** 5 read closely (making-deals, arbitrator-campaign, book-of-the-arbitrator, spire-of-babel, both settlement-events halves, lost-zone), the rest grepped/spot-checked for convergence signal — see `source.md` for exactly which |
| **Raw capture** | `research/sources/necromunda-homebrew/` |
| **Related notes** | [[Necromunda]] · [[Necromunda Campaigns]] · [[Necromunda and Mordheim]] |

---
## Why it's here

Our own [[Diplomacy]] note is an empty phase scaffold — no reputation tracking, no alliance mechanics,
no betrayal rules, nothing drafted at all. Necromunda's official campaign layer doesn't fill that gap
either. But thirty years of players have kept bolting the same handful of things onto it anyway, and
**what they keep re-adding, independently, is the actual measure of what the official game left out.**
This capture treats that recurrence as the evidence: not "is this homebrew rule good," but "how many
unrelated authors reached for the same fix."

---
## Cross-homebrew convergence — what keeps getting bolted on

> [!info] The actual output of this capture
> Across the ten-plus campaign documents read or spot-checked, four additions recur independently, in
> documents that don't cite each other:

- **A human referee with real authority (the Arbitrator).** Present, named, and load-bearing in
  `arbitrator-campaign`, `book-of-the-sump`, `lost-zone`, `expanded-campaign`, `frontier-campaign`,
  `book-of-the-arbitrator`, and grep-confirmed in `under-the-dome` and `underside-campaign` too — 8 of
  10-plus documents checked. **This is the strongest single signal in the whole capture.** Nobody
  trusts the printed rules alone to run a persistent multiplayer campaign; every serious homebrew
  re-invents a person with discretionary power to run the parts the book can't.
- **A second look at Reputation.** Heavy homebrew attention across `desperation-campaign` (71
  mentions), `spire-of-babel` (71), `lost-zone` (31, with an explicit rewrite), `book-of-the-sump` (11),
  `expanded-campaign` (12), `frontier-campaign` (21). Official Reputation exists but is, in one
  designer's own words, *"pretty much meaningless after a point"* — see
  [[Necromunda Homebrew Campaigns#Reputation, admitted broken, rebuilt as a second currency|below]].
- **Alliances, reached for constantly and built weak every time.** `under-the-dome`,
  `underside-campaign`, `frontier-campaign` (which explicitly bans them and substitutes NPC contracts
  instead), and `making-deals` all touch player-to-player pacts — but only the oldest of the four gives
  betrayal an actual dice check. See
  [[Necromunda Homebrew Campaigns#Alliances without teeth — the modern homebrew default|below]].
- **Multi-category "everyone can win something" endings.** `spire-of-babel`'s six-Triumph system
  (citing official N18 Dominion as its own precedent) and `desperation-campaign`'s scenario-scoped
  Saviour/Looter/Hunter both independently reject a single winner.

**What this rules out just as clearly.** Nobody independently invented a second currency for anything
*except* Reputation — no homebrew here proposes parallel credits, parallel XP, or a second combat
resolution system. The convergence is narrow and specific: **referee authority, reputation-as-a-real-
resource, weak alliances, and multi-winner endings** — not a general appetite for more subsystems.

---
## Striking a Deal — a one-roll table with a hidden hedge for betrayal

**Type:** Diplomacy *(no existing hub type covers this — see the note to the merging agent in
`hub-rows.md`)* · **Take:** ⭐ steal

**[COMMUNITY]** Two gang Leaders meet at a small skirmish table (16"×16", central terrain, D6+2
bodyguards each, no Heavies). Either side's **Bitter Enmity** with the other voids the whole thing
before a die is rolled. Then one open D6 on a three-way table decides the entire outcome:

> *"1-2 The gang with the higher rating refuses to deal... 3-4 A one scenario deal has been made. At
> the beginning of the scenario, the player with the gang with the highest rating rolls a D6 and writes
> it down hiding the result (in these circumstances it is always wise to have an impartial observer),
> on a 1-3 the deal sticks but on a 4-6 the deal is broken... 5-6 A long term deal has been made and the
> two gangs become friends."*

A permanent exclusion list sits underneath the roll — *"Escher and Goliath," "Redemptionist only with
Cawdor," "Spyrers and Ratskins with anybody"* — some pairings never get to roll at all, no matter the
dice.

**Why it works.** There is no ongoing trust stat, no reputation ledger between the two gangs, no
running tally of favours. **The entire question of "will this alliance hold" is answered once, by one
hidden die, and the tension comes from not knowing the result — not from tracking a number.** Hiding
the break-check behind an impartial third party is what makes it work at the table: both players
genuinely don't know if they're about to be betrayed, which is the actual feeling "diplomacy" is
supposed to produce, bought for the cost of one extra person glancing at a die.

**For Settlements.** [[Diplomacy]] is currently an empty scaffold with four bullet points and nothing
drafted. This is a direct, cheap answer to two of them at once — "alliance mechanics: truces and
betrayal" and, partially, "reputation." It maps onto our engine with zero friction: this is an event
table, not an opposed stat test, so it doesn't need a d10 conversion or a Stat — it's a flat lookup,
exactly like a Fate roll. The honest objection: it needs an impartial third party (or an app/token) to
hide the result, which is a real table-logistics cost in a 2-player game with no GM. **Compare
[[Necromunda Homebrew Campaigns#Alliances without teeth — the modern homebrew default|below]]** — every
newer homebrew we checked solved this by *removing* the hidden-roll mechanic rather than solving the
logistics problem, which should be read as a warning about how much friction it actually costs.

---
## The Meet and the Double-Cross — betrayal staged as a scenario, not a narrated event

**Type:** Diplomacy · **Take:** ⭐ steal

**[COMMUNITY]** Both companion scenarios in `making-deals.pdf` physically stage the betrayal instead of
resolving it with a roll and a sentence. In **The Meet**, a hidden third gang (the Ambushers) is
watching the deal-in-progress; each turn they fail-forward on a Leadership test or fire early, and once
they do, both allied gangs roll a **Panic Fire** test that can misfire the *right* way (spot the true
attacker) or the *wrong* way (each ally opens fire on the other, "suspecting foul play"). In **The
Double-Cross**, there's no third gang at all — the lower-rated ally is the traitor, up to half of it
deployed Hidden, and *"under no circumstances may a deal be struck between the two gangs"* in this
version — it exists purely to resolve a betrayal already committed to.

**Why it works.** The fog-of-war is mechanical, not narrated: both victim gangs get a real chance to
shoot each other by mistake, which is funnier and more tense at the table than a GM saying "you've been
betrayed." **Necromunda's whole design habit is turning an abstract campaign event into an actual
scenario** — this is that habit applied to diplomacy specifically.

**For Settlements.** Feeds [[Scenarios]] as much as [[Diplomacy]] — a reusable scenario shape ("a
meeting under threat of ambush, with a chance for the wrong side to get shot") that could sit alongside
our existing objective types with the deal/alliance content swapped for whatever fits our setting
(a black-market buy, a prisoner exchange, a ceasefire). The honest cost is table setup — this needs a
dedicated small scenario, not a rules paragraph.

---
## Hard-blocked pairings — some factions never get to roll

**Type:** Faction · **Take:** ⭐ steal

**[COMMUNITY]** Three named pairings in `making-deals.pdf` cannot make a deal at any roll result, full
stop — house rivalries baked in as an absolute veto rather than a modifier.

**Why it works.** It's the cheapest possible unit of faction identity: **one line of exclusion text
does more thematic work than a whole reputation sub-system**, because it tells you something true about
the two factions without requiring either of them to have fought yet.

**For Settlements.** Direct, nearly-free precedent for [[Factions]]: a short table of faction pairs that
simply cannot ally or trade, independent of any Diplomacy mechanic built on top. Costs one bullet list,
zero new tracked numbers.

---
## Alliances without teeth — the modern homebrew default

**Type:** Diplomacy · **Take:** ⚠️ avoid — an instructive gap, not a mechanic to copy

**[COMMUNITY]** Every modern territory/hex-map campaign checked treats "alliance" as a naming
convention with no betrayal-risk mechanic at all:

- `under-the-dome.pdf`: *"Players can choose together to be allies, but there isn't anything permanent
  in Necromunda. Alliance can be broken with a single shot instantly."*
- `underside-campaign.pdf`: alliances must be **named** and publicly declared, combine gang rating for
  scenario purposes, but *"may be ended at any time"* — disputes over spoils fall back to a leadership-
  challenge duel between the two allied Leaders, not a dice check on the alliance itself.
- `frontier-campaign.pdf` goes further and **bans player alliances outright**, substituting NPC-faction
  "Caravan Contracts" instead — explicitly because a two-sided pact is judged unworkable at their
  campaign's scale.

**Why this matters.** This is the direct opposite of `making-deals.pdf` above, and it's the newer,
larger, more-played campaigns that made the weaker choice. Read plainly: **the mechanical-betrayal
version is real and it works, but three independent, more-recent authors all quietly dropped it in
favour of a social-contract-only alliance** — almost certainly because the hidden-roll mechanic needs a
third party or a trusted app to arbitrate, and that's friction most groups don't want to carry every
game.

**For Settlements.** The honest read for [[Diplomacy]]: **don't assume the dice-backed version is
strictly better just because it's more mechanically interesting.** If Settlements can't guarantee a
neutral party (or a digital secret-roll tool) at the table, the unenforced "alliances are just table talk
until someone shoots" version is the one three separate homebrews independently converged on as the
sustainable default. Log this as the fork it actually is, not a settled question.

---
## The Arbitrator's Special — a costed, GM-adjudicated wildcard slot

**Type:** Campaign · **Take:** ⭐ steal

**[COMMUNITY]** `lost-zone.pdf` rebuilds Reputation as a spendable currency (see below) with exactly
four purchase options, the fourth being *"The Arbitrator's Special (cost varies)"* — a named, budgeted
slot that exists specifically so the referee can adjudicate something the printed rules didn't
anticipate, without that adjudication feeling unbounded or free.

**Why it works.** Every campaign eventually needs a ruling the book didn't cover. Most systems leave
that as ungoverned GM fiat. This gives it **a name, a cost field, and a place in the spend-list** — the
adjudication is still improvised, but its *shape* (it costs something, from the same pool as everything
else) is fixed in advance, so it doesn't feel arbitrary when it lands.

**For Settlements.** If Settlements ever adopts anything like an Arbitrator/campaign-referee role (see
next entry), this is the cheapest version of "and here's how the referee's discretion gets paid for" —
one costed catch-all line in [[Campaign]], rather than an unbounded house-rule habit.

---
## Arbitrator-curated rotating NPC pools — the same fix, invented twice

**Type:** Campaign · **Take:** ⭐ steal

**[COMMUNITY]** Two unrelated documents independently built the same tool. `lost-zone.pdf`'s
**Trading Post Generator** and **Unemployment Office**: once per campaign week, the Arbitrator
generates a limited, randomised list of buyable rare items or hireable Hangers-On (an optional
**Auction System** caps some items to `D3` total copies for the *entire* campaign, allocated
lowest-gang-rating-first). `expanded-campaign.pdf`'s **Tavern Mechanic** — explicitly credited as
*"inspired by... Heroes of Might and Magic"* — has the Arbitrator choose from a pool of available Hired
Guns each week and post them for recruitment.

**Why it works.** A static, always-available shop list makes the meta-game solvable — whoever has the
most credits just buys the best thing. **Rotating a small, Arbitrator-curated selection turns "what can
I buy" into a weekly event with its own tension**, and rationing scarce items by gang rating (lowest
first) is a free, built-in catch-up mechanic riding on top of the same tool.

**For Settlements.** Directly useful for [[Economy]] and whatever [[Downtime]] ends up being: a rotating,
capped availability list is cheap to run (one random-generation step per session) and quietly does
anti-snowball work for free. The honest cost is that it needs *someone* to run the generator — a solo
player or a 2-player game with no Arbitrator needs this automated, not GM'd.

---
## Arbitrator's Monster — a dual-mode PvE stat block

**Type:** Solo · **Take:** ⭐ steal

**[COMMUNITY]** `book-of-the-sump.pdf` tags several creature profiles *"Arbitrator's Monster"* and
specifies they can be run **either by a human Arbitrator, or by following a printed simplified-AI
ruleset** (the same ruleset already used for its ordinary Sump Spider wildlife) — the same stat block
works whether or not a referee is present.

**Why it works.** It solves the "what if we don't have a spare GM tonight" problem at zero extra design
cost — one stat block, two run-modes, and the printed AI rules only need to exist once because they're
reused across every creature that carries the tag.

**For Settlements.** Direct precedent for [[Solo & Co-op]]: any PvE opponent built for a
multiplayer/Arbitrated game should be designed from the start to also run on simple printed rules, so
the same content serves solo and refereed play without a parallel AI system.

---
## Reputation, admitted broken, rebuilt as a second currency

**Type:** Economy · **Take:** ⚠️ avoid, but read the diagnosis carefully

**[COMMUNITY, with an explicit designer critique of the official rule]**

> *"Reputation. Frankly, it's pretty much meaningless after a point in current Necromunda... In a Lost
> Zone campaign, Reputation is a spendable resource. Like credits, Reputation can be spent on upgrades,
> but instead of individual fighter upgrades, it's spent on gang upgrades."*

Spent on exactly four things (Hanger-On slot, Brute slot, Territory upgrade, Arbitrator's Special) —
narrow and closed, not an open-ended second economy.

**Why it's flagged, not stolen.** This is a genuine, named negative result about official Necromunda —
**a stat that exists on every gang sheet and does almost nothing** — which is exactly the kind of
shipped mistake worth logging. But the fix Lost Zone reaches for is a **second player-facing currency**,
and Settlements has already locked against that: *"One economy only... never introduce a second
parallel currency"* (`AGENTS.md`). The diagnosis transfers; the cure doesn't.

**For Settlements.** File the *symptom*, not the *treatment*, against [[Economy]]: a tracked number that
exists but gates nothing meaningful is worse than not tracking it at all. If Settlements ever adds a
Reputation-like stat, the Lost Zone critique is the test to run against it before shipping — *does this
number ever actually close a door, or does it just sit on the sheet* — without reaching for a second
currency to answer yes.

---
## Six-category Triumphs instead of one winner

**Type:** Campaign · **Take:** ⭐ steal

**[COMMUNITY, citing an official precedent]** `spire-of-babel.pdf`: *"Rather than having single player
being victorious Spire of Babel uses similar triumph system as N18 Dominion Campaign. There is total six
triumphs... In case of tie, no one wins the triumph."* Dominator (most territory) · Slaughterer (most
Out of Actions caused) · Creditor (highest wealth) · Warmonger (most games played) · Powerbroker
(highest reputation) · Achiever (most Achievements completed) — six independent "best at X" awards,
tracked all campaign via a shared spreadsheet, resolved once at the end.

**Why it works.** It recognises six different playstyles (aggression, wealth, table-time investment,
diplomacy, completionism, territory) without forcing any of them to compete on the same axis, and a tie
in any category simply awards nothing rather than needing a tiebreaker rule. `desperation-campaign.pdf`
independently reaches for the same shape at scenario scale (Saviour/Looter/Hunter over one Loot-Crate
economy), which is a second, unrelated data point for the pattern.

**For Settlements.** Direct support for the locked tenet *"you win on objectives, never on kills"* — a
multi-category end state is the campaign-scale expression of the same idea already locked at the
battle scale. Worth a note in [[Campaign]] as a candidate for how a Settlements campaign concludes
without crowning one winner and leaving everyone else with nothing to show for the campaign.

---
## Achievements with zero mechanical payout

**Type:** Campaign · **Take:** ⭐ steal

**[COMMUNITY]** ~28 one-time checkboxes in `spire-of-babel.pdf` (*"Cat Fall,"* survive a 10"+ fall
unwounded; *"Usurper,"* kill the enemy Leader with a Juve melee attack; *"Flawless,"* win with zero
injury rolls against your own gang) carry **no direct mechanical reward** — they only count toward the
Achiever Triumph category above. *"Any achievement can only be completed once. And once they are
completed they will stay completed even if criteria for achievement is no longer true."*

**Why it works.** Because there's no mechanical payout, there's no balance risk in writing more of
them — they're pure engagement bait, safe to add freely. Multiple players can complete the same one
(unlike a claimed-once resource), so there's no exclusivity tension either.

**For Settlements.** Read directly against
**[[Trench Crusade#Glory|Trench Crusade's Glorious Deeds]]**, which is the mirror image: Glory buys real
in-game power and is claimed first-come-first-served (*"whichever player completes them first gets the
Glory"*). Spire of Babel's Achievements are the *cheap* version of the same instinct — same "do a named
cool thing" trigger, zero power granted, zero exclusivity, purely a scorecard. **Both are legitimate
answers to our own Glorious Deeds want; they sit at opposite ends of one dial (reward size), and
Settlements should pick a point on that dial deliberately rather than default to either end.**

---
## The Campaign Events Table — catch-up baked into the randomness itself

**Type:** Campaign · **Take:** ⭐ steal

**[Provenance uncertain — see note below]** A D66 table rolled roughly weekly to biweekly, explicitly
framed as a balancing tool: *"The events tend to give more lucky breaks for upcoming gangs over
established old gangs so they are useful for balancing the campaign and stopping the older gangs
dominating the action."* Concretely: several entries single out the *highest-rated* gang for a penalty
(Watchmen Investigation, Discontentment, Scavvy King all specifically target them); **Old Pro** attaches
a free veteran fighter to whichever gang has the *lowest* rating, *"until they no longer have the lowest
gang rating"* — an automatically self-removing catch-up bonus with no manual bookkeeping. One entry runs
against the table's own bias: **New Turf** (recurring ~6 times in the 36-entry table) awards a new
territory to whichever gang's rating grew the *most* since the last event roll — rewarding growth with
more growth.

**Why it works.** Catch-up logic is usually a separate subsystem (underdog bonuses, banding) bolted on
top of the campaign. Here it's baked directly into the random-event table itself — the same roll that
adds flavour and unpredictability *also* does the balancing work, for free, with zero extra tracked
numbers. The one contradicting entry (New Turf) is worth keeping as a caution: **a catch-up-biased event
table can still contain an anti-catch-up entry by accident if nobody audits the whole table against its
own stated goal.**

**Provenance note.** This table's origin is ambiguous: `arbitrator-campaign.pdf` reads as Games Workshop
studio-authored (*"Here at the studio I have been running an Arbitrator campaign..."*), not fan
homebrew, and the identical table also circulates standalone as `campaign-events-orb.pdf` — the same
table, not independent corroboration. Flagged here rather than smoothed over.

**For Settlements.** Direct precedent for [[Events]] and [[Campaign]]: if Settlements ever runs a
periodic random-event table between battles, auditing every entry against "does this help the gang
that's behind, or the gang that's ahead" is a cheap, one-time design pass that buys most of the
catch-up value banding/underdog-bonus systems buy separately.

---
## Settlement visit as an encounter roll, not just a shop

**Type:** Settlement · **Take:** ⭐ steal

**[COMMUNITY — OCR-transcribed, see quality note in `source.md`]** In the `settlement-events` pair
(Tom Merrigan), visiting a settlement is gated twice: *"You may visit up to D3 locations each time your
gang goes into town"* caps how much shopping happens per trip, and — before any location is chosen —
the whole travelling party rolls once on a shared **D66 Settlement Events table** (Thrown Out of Town,
Pickpocket, a full Quick-Draw duel scenario triggered by an old grudge, Conscription, and more).
Two of the settlement's named locations are themselves self-contained push-your-luck mini-games:
**Gambling Dens** (bet, roll, then a separate "When to Quit" D6 gate that lets a winning streak keep
going but eventually calls time) and **Pit-Fighting Arenas** (enter a fighter against a random NPC
under a restricted "legalised weapons" list, with the same quit-gate).

**Why it works.** A settlement stops being a passive shop the moment it can roll something *at* you —
the D3-location cap and the shared random-event roll both cost nothing extra to run (one table, one
roll) but make every visit feel like it's happening somewhere, not in a menu. The "when to quit" gate on
the two sub-games is a clean, self-terminating push-your-luck loop that needs no new die type.

**For Settlements.** Directly feeds the "boards that feel alive" want and [[Settlement]]/[[Downtime]]: a
single shared event roll per settlement visit (not per location) is nearly free, and a visit-cap
(D3-equivalent) keeps downtime bounded without a hard rule against doing things. The
gambling/pit-fighting quit-gate is a reusable shape for any future push-your-luck side-activity.

---
## The settlement-nominee template — identity as reweighted odds, not a new system

**Type:** Settlement · **Take:** 📎 reference — thin, but the schema is real

**[COMMUNITY]** Three entries in a **"Necromunda Settlement Nominee"** community contest were checked
for a shared template. Two of three (Scum City, Sludge Harbour) share one: worldbuilding prose → power
structure → **one signature rule** (Scum City's flat income-tax-bracket shift, *"The Cut"*; Sludge
Harbour's Treacherous-Conditions probability shift) → **a reweighted D66 Territory Chart** reusing most
official territory names at different odds, plus one or two invented territories representing partial
business ownership rather than outright control. **The third entry, `settlement-martyr-town.pdf`, is
pure flavour text — zero mechanics.** Reported plainly: one of three contributed nothing rules-side.

**Why it's only a reference, not a steal.** There's a real, cheap template here (identity = odds-reweight
+ one signature rule), but it's thin — two data points confirming it, one contest entry with nothing at
all, and none of the three attempt anything Settlements' own [[Settlement]] work hasn't already
considered at a more developed level.

**For Settlements.** Worth naming as a *minimum viable* settlement-identity pattern if [[Settlement]]
ever needs a fast, low-cost way to differentiate a named location: don't design a new system, reweight
the existing table and add exactly one signature rule. Don't spend more design budget on this specific
source than that one sentence — the contest entries themselves didn't.

---
## The post-battle action — one downtime action per surviving fighter

**Type:** Campaign · **Take:** ⭐ steal

**[COMMUNITY]** `book-of-the-arbitrator.pdf`'s shared campaign turn structure (used across its
Territory/Exploration/Narrative campaign types alike) gates the entire downtime phase per-model:
*"A unit has a post-battle action, which he can use to perform up to one thing during the post-battle
sequence"* — one of rolling for injuries, gathering income, negotiating for captives, searching for
rare items, or spending on skills/equipment/events. Everything else in that list happens automatically
regardless (determine winner, assign XP, work out new rating); only this slate is gated.

**Why it works.** Downtime bookkeeping usually either does everything for every fighter (slow, and
nothing is ever a real choice) or gates nothing (fast, but also nothing is a real choice). **One scarce
action token per surviving fighter, spent on exactly one of several named things**, forces an actual
trade-off — do I send this ganger to chase rare loot, or does he sit still and let someone else do the
income run — without adding a new resource type to track long-term; the token doesn't carry over.

**For Settlements.** Direct candidate for [[Downtime]]: instead of "every surviving fighter can attempt
every listed downtime action," gate the phase with one token per fighter that must be spent on exactly
one action. Cheap to run (a token or a tick-box per model), and it turns downtime into a genuine
allocation puzzle instead of a checklist.

---
## What it gets wrong

- **Arbitrator campaigns assume a benevolent, present, trusted referee** — every mechanic above that
  routes through "the Arbitrator decides" (the Special, the rotating pools, event scheduling) silently
  assumes that person exists, has time every session, and won't favour their own gang. Several sources
  (`lost-zone`, `expanded-campaign`) are explicit that this person should also field a gang, with no
  enforcement mechanism beyond trust. **None of the 17 sources propose a check on Arbitrator fairness** —
  it's the one authority in this whole layer that nobody homebrewed a safeguard for.
- **The modern alliance consensus (unenforced, table-talk-only) is a quiet retreat**, not an improvement —
  see [[Necromunda Homebrew Campaigns#Alliances without teeth — the modern homebrew default|above]]. It
  reads as "this was too much friction," not "this was the wrong idea."
- **Reputation-as-second-currency (`lost-zone.pdf`) is a real fix to a real problem, built the one way
  Settlements has already ruled out.** Worth citing the diagnosis; do not import the cure.

---
## Evidence & confidence

- **[FACT]** — verifiable directly in the PDF text, quoted with page/section context in `source.md`.
  Everything in "Striking a Deal," "The Meet and the Double-Cross," "The Arbitrator's Special,"
  "Reputation, admitted broken," "Six-category Triumphs," "Achievements," and "The post-battle action"
  is quoted verbatim from its source.
- **[COMMUNITY]** — tagged on every mechanic in this note without exception, per this capture's brief:
  nothing here is an official Games Workshop rule, and unplaytested-at-commercial-scale homebrew should
  be weighted accordingly, however well-argued.
- **[INFERENCE]** — the convergence claims ("nobody proposed a second currency except for Reputation")
  are drawn from a targeted keyword search (`arbitrator`, `reputation`, `alliance`, `betray`,
  `negotiat`, `triumph`, `achievement`, `spreadsheet`) across the read/spot-checked documents, not a
  full read of all ten-plus. A full read could surface a counter-example this search missed.
- **[NOT FOUND]** — the exact allied-ganger dice notation in `making-deals.pdf` (OCR-garbled as
  `D[?]*2`); the promised Gamemaster-authority chapter in `book-of-the-arbitrator.pdf`'s own table of
  contents, which did not surface distinctly in this read; whether `arbitrator-campaign.pdf` is
  officially GW-published or fan-submitted through a GW-hosted channel (textual evidence points to
  studio authorship, but this is inference, not a confirmed publication record).

---
## Source

- Primary: 17 community PDFs, curated from a ~94-file library at
  `G:\My Drive\Wargaming\NECROMUNDA\Campaigns and Homebrews\` — see `meta.json` for per-file library
  paths and hash verification.
- Capture: `research/sources/necromunda-homebrew/source.md`
- Related: [[Wargaming Research Hub]] · [[Necromunda]] · [[Necromunda Campaigns]] ·
  [[Necromunda and Mordheim]] · [[Trench Crusade]] · [[Oathmark]]

# Necromunda — the homebrew and community campaign layer

Seventeen community/fan-made Necromunda PDFs, curated from a 94-file library, read for the unofficial
campaign layer specifically: deals and betrayal, the Arbitrator (GM) role, cross-document convergence,
settlement events/structure, and Triumphs/Achievements. **Nothing in this file is an official Games
Workshop rule** — see each entry's provenance line. Quotes are selective (exact wording that matters);
full rules tables that are reproduced here are print-run-common house-rule tables, not narrative
rulebook content, and originals are not committed to the repo (`original.pdf` is gitignored — see
`meta.json` for the library master paths).

---

## making-deals.pdf — "Striking a Deal..." (Dalga Faik, w/ Nick Piachaud)

**Provenance:** A reader-submitted article, credited "By Dalga Faik w/ playtest conspirator Nick
Piachaud," ending with a "Roolz Boyz" rules-hotline sign-off — house style for Games Workshop's
Necromunda-era fan-submission channels (this reads as the same publishing lineage as the
`settlement-events` pair below, likely the same webzine/annual). **Community-authored, GW-hosted.**
7 pages, clean embedded text (light OCR-era scan artifacts in a few words, does not affect the rules).

### The deal-striking procedure
Two gang Leaders meet at a small (16"×16") skirmish table with a central terrain feature (crates).
Deploy on table edges; Leaders converge on the centre to talk. Each side may bring **D6+2 bodyguards,
no Heavies** ("because if things go sour the gangs aren't going to want to risk losing a heavy
weapon"). A **Bitter Enmity** between any two models on opposing sides voids the whole negotiation
before it starts. Once the leaders are face to face across the crates, roll one D6 on this table:

> *"1-2 The gang with the higher rating refuses to deal with the other gang because they consider
> them to be below them and therefore scum."*
> *"3-4 A one scenario deal has been made. At the beginning of the scenario, the player with the gang
> with the highest rating rolls a D6 and writes it down hiding the result (in these circumstances it
> is always wise to have an impartial observer), on a 1-3 the deal sticks but on a 4-6 the deal is
> broken. The higher rated gang may attack or leave the gang it is supporting at any time during the
> scenario on a broken deal result... if the deal goes down for the whole game another deal may be
> struck."*
> *"5-6 A long term deal has been made and the two gangs become friends. Roll a further D6 at the
> beginning of each game either gang takes part in. On a 1-4, the higher rated gang continues to
> honour the deal, on a 5-6, the higher rated gang leaves but on good terms. If this type of deal
> falls through, it can be attempted again but any results on subsequent rolls must be adhered to."*

Hard exclusions, regardless of roll: *"Escher and Goliath"* · *"Redemptionist only with Cawdor"* ·
*"Spyrers and Ratskins with anybody."*

**Payoff.** A successful deal lets the "hiring" gang call on allied gangers from its partner in its
next fight — the text gives the dice notation as `D[garbled]*2` (OCR-uncertain, likely `D3+2` or
similar; **[NOT FOUND — exact notation illegible in the only capture]**). Allies are run by the
hiring player and count as that player's own gang for XP and Bottle purposes. *"Gangs are honour-bound
to their allies and can only 'stab them in the back' if the deal was broken (see earlier)"* — betrayal
is only legal once the dice have already said the deal failed.

### The Meet (scenario)
Both allied gangs deploy facing each other across the crates as above; a **third gang, the
Ambushers**, deploys Hidden in the upper levels/gantries, hired by an unnamed third party to break the
deal up. Each turn the Ambushers must pass a Leadership test on the Leader's Ld or fire early (breaking
Hidden). Once they do fire, each of the two treaty gangs rolls a Panic Fire test (D6): *"on a score of
1-4, the gang leader spots the Ambushers and orders his gang to fire upon them... On a roll of 5-6, the
Gang Leader hasn't spotted the ambushing gang and orders his Gangers to fire upon the gang they were
making a deal with, suspecting foul play."* Repeated triggers (each further hit/pin on a gang that
hasn't yet spotted the ambush) reroll the same test. If the true attacker is spotted before both
leaders are down, the Deal table above can still be rolled, with a −1 modifier if the two gangs fired
on each other before recovering composure, or +1 if both correctly identified and fired on the
Ambushers ("false sense of camaraderie").

### The Double-Cross (scenario)
Same staging, no third-party Ambusher — instead, the **lower-rated** gang itself is planning to betray
its "ally" mid-meet. Up to half of the double-crossing gang may deploy Hidden. Same Leadership-test
mechanic gates a premature reveal. *"Obviously, under no circumstances may a deal be struck between the
two gangs"* in this scenario — it exists purely to resolve a betrayal already committed to.

---

## arbitrator-campaign.pdf — "The Arbitrator Campaign"

**Provenance:** Reads as Games Workshop **studio-authored** supplementary material, not fan homebrew —
p.2: *"Here at the studio I have been running an Arbitrator campaign while I've been writing
Outlanders."* This is the original definition of the Arbitrator role and its campaign-events table;
staged in the homebrew capture set but its actual authorship is internal GW studio, not a community
submission. Flagging this plainly rather than mis-tagging it as fan content. 30 pages, clean text.

### The Arbitrator, defined
> *"In order to run an Arbitrator campaign the first thing you need to do is pick the Arbitrator, who
> should ideally be the most experienced and trusted player in the group. The Arbitrator has the
> responsibility of making sure the campaign runs smoothly, and, most importantly, organising some
> special scenarios for the players. The Arbitrator also keeps himself amused by dropping some random
> events into the campaign... The Arbitrator can still play a gang in the campaign himself as long as
> he doesn't take advantage of his position to give his gang any unfair advantages."*

### The Campaign Events Table (D66, rolled weekly-to-biweekly)
Explicitly framed as an anti-snowball tool: *"The events tend to give more lucky breaks for upcoming
gangs over established old gangs so they are useful for balancing the campaign and stopping the older
gangs dominating the action."* Selected entries (66-entry table, full text extracted, condensed here
to the mechanically distinct ones):

- **Watchmen Investigation / Discontentment / Scavvy King** — each explicitly penalizes the
  *highest-rated* gang (halved territory income, or lets a beaten higher gang be raided for territory).
- **Old Pro** — *"The gang with the lowest gang rating is joined by an old pro' fighter... He will
  remain with the gang for free until they no longer have the lowest gang rating."*
- **New Turf** (recurs ~6 times in the 36-entry table) — a new territory is generated but awarded, at
  the *next* event roll, to whichever gang's rating grew the *most* since this roll — rewarding growth
  with more growth, the one entry that runs against the table's stated catch-up bias.
- **Freelancer** — *"the most experienced fighter... leaves and goes freelance. The freelancer becomes
  a Hired Gun with a hire fee equal to his total Experience points and cost divided by 10 (eg, 80 cost
  plus 50 experience = 13 credit hire fee)."* A formula for converting a persistent character into a
  purchasable mercenary.
- **Master Teacher** — *"players can send a gang fighter that has gone up a level to be taught... at a
  cost of 25 credits. The player can then pick a result on the Advance Roll Table... instead of rolling
  for it randomly. Skills are still rolled randomly."* Buy certainty on one axis, not both.
- **The Healer** — cures the long-term effects of Serious Injuries for credits, explicitly *"can't cure
  death or capture though"* — a costed floor, not a full escape hatch.
- **Stinger Mould Harvest** — pay 5cr to reroll one Serious Injury result once (no result rerolled
  twice).

### Scenario: Lord of the Spire
A rating-gated (1,250+) arena race — hit the objective button atop a central tower first, 2–4 gangs,
substantial cash prize.

---

## campaign-events-orb.pdf — "Campaign Events Table"

**Provenance:** The *identical* table to arbitrator-campaign.pdf's Campaign Events Table (same D66
entries verbatim, minor OCR variance only) circulating as a standalone reference document. **Not an
independent second source** — a re-share/re-scan of the same original GW table. Logged so a future
capture doesn't double-count it as corroboration.

---

## book-of-the-arbitrator.pdf (Torben Kastbjerg, "Adventures in the Dark Millennium," v1.3)

**Provenance:** Fan-authored (community), explicitly named on the title page. 99 pages, clean text but
with a recurring OCR duplication artifact (headings render 3–4× repeated, e.g. `"0ampaigns 0ampaigns
0ampaigns 0ampaigns"`) — a rendering artifact of the source PDF's font layers, **not** evidence of
duplicated content; confirmed by reading the surrounding prose, which is single and coherent.

This is a large-scale conversion of Necromunda's engine into a general Warhammer 40,000 skirmish/RPG
hybrid (Rogue Traders, Space Marines, Genestealer Cults, full 40k unit archetypes, weapons and psychic
powers) — its own author frames the intent as *"Necromunda - nothing more, nothing less"* being enough
of an engine to run any 40k-setting story. Most of its bulk (equipment tables, archetype stat blocks,
Imperial/Xenos/Hereticus "Encounters") is genre-conversion content outside this capture's scope. Two
structural findings worth extracting:

**Three campaign types, one shared turn sequence.** Territory / Exploration / Narrative campaigns all
share one Pre-Battle Sequence (meet & compare ratings → roll scenario → terrain & pre-battle events →
play) and one Post-Battle Sequence. The post-battle sequence gates itself with a scarce resource:

> *"A unit has a post-battle action, which he can use to perform up to one thing during the post-battle
> sequence"* — one of: roll for injuries / gather income / negotiate for captives / search for rare
> items / spend on skills, equipment or events. *"The finer detailing for any campaign lies in how you
> gather income... but these lists are common to all campaigns."*

This constrains downtime bookkeeping into a genuine choice per surviving fighter, rather than doing
every downtime action for every fighter automatically.

**The Gamemaster/Arbitrator content is thin.** Despite the title and an indexed "Gamemaster Section,"
searching the extracted text found only one substantive Arbitrator-authority passage (p. ~57 internal,
on assigning equipment to NPC units at the GM's discretion) — the promised GM-authority chapter did not
surface distinctly from the surrounding conversion material in this read. Not a strong source for the
Arbitrator-role priority despite its title; **arbitrator-campaign.pdf and lost-zone.pdf are the load-
bearing sources for that question, not this one.**

---

## spire-of-babel.pdf — "Spire of Babel" custom campaign

**Provenance:** Community-authored (N18-era), explicitly built on Yaktribe tooling and community
playtesting; the Achievements section credits *"Yaktribe discord member beaut0x"* by name for the idea
— genuinely community-sourced, not a single author's solo design. 14 pages, clean text.

### Triumphs
> *"Rather than having single player being victorious Spire of Babel uses similar triumph system as N18
> Dominion Campaign. There is total six triumphs, which is awarded [to the] player having best score in
> each category. In case of tie, no one wins the triumph."*

The six: **Dominator** (most territory) · **Slaughterer** (most Out of Actions caused) · **Creditor**
(highest wealth) · **Warmonger** (most games played) · **Powerbroker** (highest reputation) ·
**Achiever** (most completed Achievements). Tracked via a shared Google Sheet/Form players submit
after every game (gang name, date, territory/wealth/reputation totals, OOAs caused, achievements
gained). **[FACT, per source]** the six-category structure explicitly cites N18's own Dominion Campaign
as precedent — this is not a purely fan-invented structure, it extends an official one.

### Achievements
~28 one-time, individually-earned checkboxes (examples: *"Cat Fall"* — survive a 10"+ fall without a
wound; *"Usurper"* — kill the enemy gang Leader with a Juve melee attack, not a coup de grace;
*"Flawless"* — win a battle with zero injury rolls for your own gang; *"Monopoly"* — control three
territories with an enhance-boon for a gang you are *not* playing). *"Any achievement can only be
completed once. And once they are completed they will stay completed even if criteria for achievement
is no longer true."* Achievements carry **no direct mechanical reward** — they exist solely to feed the
Achiever Triumph category at campaign end. Not exclusive/first-come like Trench Crusade's Glorious
Deeds; multiple players can independently complete the same achievement.

Remainder of the document (rulebook alterations to Stray Shots/Bottle Test/Shooting Engaged, the
Founding Gangs/Territory List) is standard N18 house-ruling and a per-house territory table closely
modelled on the official Dominion territory list — not distinct enough from official rules to log
separately here.

---

## Settlement Events, parts 1 & 2 (Tom Merrigan, "Gang War" webzine)

**Provenance:** Reader-submitted ("by Tom Merrigan, from Sydney, Australia... a regular contributor to
Gang War"), same GW-hosted-fan-content lineage as `making-deals.pdf`. **Both files were image-only —
0 extractable characters/page** — rendered at 300dpi and OCR'd with Tesseract (`--psm 6`). OCR quality
is moderate: character-substitution noise throughout (e.g. digit/letter confusion, "ffnger" for
"finger"-type errors from the scan/print era), but every rule and table entry below was legible and
internally consistent on inspection. **This is the honestly-reported quality bar — do not treat the
noise as a defect in the underlying source, and do not treat this transcription as verbatim-exact.**

### The visit structure
A gang may only visit a settlement if its Leader survived the last battle. *"You may visit up to D3
locations each time your gang goes into town"* — a hard cap on downtime actions per visit, not an
unlimited shopping trip. Before visiting any location, roll **D66 on the Settlement Events table** for
the whole travelling party — one shared random encounter per visit, not per location.

### Settlement Events table (~36 entries, D66)
Selected entries: **Thrown Out of Town** (no locations visited this trip) · **Pickpocket** (lose half
current credits) · **Ratskin Scout** (help or ignore a Ratskin being mugged; helping earns a map item
or a one-battle free Hired Gun) · **Slaver** (Initiative test per fighter or be captured and held for a
buy-back priced at `XP÷10` credits each) · **Shootout** (an old grudge triggers a full 1-v-1 Quick-Draw
duel, run using the actual Necromunda Shootout scenario rules with only the two named models) ·
**Conscription** (a fighter is drafted; 1-in-6 to escape and go AWOL, else gone for good) ·
**Riot/Illness/Lucky Find** — assorted D66 filler with credit/injury/recruitment swings.

### Gambling Dens
A full push-your-luck mini-game: bet, roll 1D6 (1 = lose the bet from stash, 2-5 = wash, 6 = win 10×
credits), then roll again on a **"When to Quit"** gate: *"On a roll of a 5-6 your leader decides to
chance his luck one more time... On a 1-4 your leader decides his luck has run dry... You may always
choose not to continue to gamble if you like. If your leader was a 'winner' on the last bet you may add
+1 to the dice roll."* Streak bonus, but the house (the dice) eventually calls time — the escalating-risk
loop is bounded without a hard turn cap.

### Pit-Fighting Arenas
A second full sub-game: enter a fighter against a randomly-generated Pit Fighter NPC, resolved as a
normal Close Combat inside a restricted "legalised weapons" list (no additional equipment; only knives,
chains/flails, clubs/mauls, massive axes/clubs, eviscerators). A 2D6 **Pit-Fighting Arena Random Event**
table layers complications (match-fixing accusations, pickpocketing, fatigue/inside-information
Initiative shifts, better-odds side-bets). Same "when to quit" streak gate as Gambling.

---

## lost-zone.pdf — Goonhammer "Lost Zone" campaign supplement

**Provenance:** Community-authored (Goonhammer.com), explicit fan supplement with companion web tools.
45 pages, clean text, the single richest document in this set for Arbitrator authority and the second-
currency Reputation redesign.

### The Arbitrator's toolset, explicit powers
Gating champion/prospect/brute/hanger-on access on a discretionary schedule (*"the decision to allow for
more champs and prospects should be placed in the hands of the campaign Arbitrator"*); running a named
**"catch-up mechanic"** — *"If a certain gang is lagging behind the others in your campaign, give them
the opportunity to hire [a champion] early"*; scheduling narrative campaign beats; curating shop
contents via a **companion web generator** — *"Click Here to visit the Goonhammer Lost Zone Trading
Post Generator... The Arbitrator chooses a number of items that the Guilder caravans have brought"* —
plus an optional **Auction System** where scarce rare items are limited to `D3` copies total across the
whole campaign and doled out lowest-gang-rating-first; an equivalent **"Unemployment Office"** generator
for Hangers-On, once per campaign week.

### Reputation, an admitted broken mechanic, rebuilt as a second currency
> *"Reputation. Frankly, it's pretty much meaningless after a point in current Necromunda... We feel
> that Reputation should function in a similar fashion [to real-world criminal reputation]: gangs can
> use it to open otherwise closed doors and enhance their revenue stream, hired help, and campaign
> experience... In a Lost Zone campaign, Reputation is a spendable resource. Like credits, Reputation
> can be spent on upgrades, but instead of individual fighter upgrades, it's spent on gang upgrades.
> Once Reputation is spent, it is removed from the gang's roster, just like credits or components."*

Spent on exactly four things: Unlock a Hanger-On roster spot (3 Rep, max 3 times) · Unlock a Brute
roster spot (7 Rep) · Upgrade a Territory (5 Rep) · **"The Arbitrator's Special"** (cost varies,
GM-adjudicated, no fixed menu). This is a second, non-credit currency, explicitly and deliberately —
worth weighing against Settlements' locked one-economy rule (see the vault note).

---

## Tier-2 campaign documents — read for cross-document convergence, not deep individually

Grepped and spot-checked for Arbitrator/Reputation/Alliance/Triumph content rather than read cover to
cover (time-budgeted; see the vault note's convergence section for what this search actually found):

- **under-the-dome.pdf** (13pp, hex-map 12-turn multiplayer campaign). Alliances exist but are
  explicitly non-binding: *"Players can choose together to be allies, but there isn't anything permanent
  in Necromunda. Alliance can be broken with a single shot instantly."* Combined gang rating for
  underdog-bonus purposes while allied. Confirms Arbitrator falls back to *"irc bots / google sheet
  random generators"* for absent-player rolls.
- **frontier-campaign.pdf** (24pp). Explicitly **bans player alliances** — *"gangs cannot make alliances
  in this campaign, this is due to the difficulty of receiving long term patronage so far from the hive
  cities"* — substituting NPC-faction "Caravan Contracts" instead of player diplomacy. Does allow
  negotiated prisoner exchange/trade between hostile players.
- **underside-campaign.pdf** (11pp). Named, publicly-declared hex-map alliances (*"must have a name...
  may be ended at any time"*), combined rating and combined attacks, with disputes over spoils resolved
  by a leadership-challenge duel between the allies. No betrayal-risk mechanic.
- **book-of-the-sump.pdf** (52pp, Kacper Kuc & Alexander Lunde). Explicit **"Arbitrator's Monster"**
  stat-block tag: a PvE creature usable *"either controlled by the Arbitrator, or in the same way as
  Sump Spiders"* (a printed simplified-AI ruleset) — a dual-mode monster, human-run when a referee is
  present, rules-run when not.
- **expanded-campaign.pdf** (36pp). A **"Tavern Mechanic"** (explicitly credited as *"inspired by...
  Heroes of Might and Magic"*) — the Arbitrator curates a rotating weekly pool of hireable Hired Guns —
  independently convergent with Lost Zone's Trading Post/Unemployment Office generators. Also
  **Personal Bounties** (Arbitrator-assigned side-objectives with named rewards) and an **"Action Game
  Mode"** explicitly for *"Dungeon Crawler/RPG style scenarios, where each player controls only 1-4
  models facing off against Arbitrator NPCs"* — a formalised solo/co-op PvE mode.
- **desperation-campaign.pdf** (21pp, "2_Minutes_Turkish"). A scenario-scoped mini-Triumph system
  (Saviour/Looter/Hunter) tied to a Loot-Crate economy — the multi-category-award pattern recurring at
  small scale, independent of Spire of Babel's campaign-wide version.

---

## Settlement design contest — settlement-scum-city / -sludge-harbour / -martyr-town

**Provenance:** Entries in a community **"Necromunda Settlement Nominee"** contest (each titled and
signed "By [Author]," each closing "About the Author"). Checked specifically for a shared template, per
the task brief.

**A shared template exists, and it is thin.** Scum City and Sludge Harbour both follow: worldbuilding
prose (founding/geography) → power structure/infrastructure → **one signature rule** (Scum City: double
rare-item finds on Mark Street, plus "The Cut" — a flat one-bracket income-tax shift for every gang
operating there) → **a reweighted D66 Territory Chart** re-using most official territory names at
different odds, with one or two new invented territories representing partial ownership of a business
rather than outright control (*"Trader Connection," "Mark Street Shop"*) → About the Author.
Sludge Harbour's signature rule is a Treacherous-Conditions probability shift (Methane Pockets) plus an
"Amateur Salvage" side-mini-game for otherwise-idle Gangers/Juves.

**settlement-martyr-town.pdf is pure flavour text — zero mechanics.** Four pages of founding myth and
the aftermath of a Hive Quake; the only rules-adjacent word in the whole document ("territory") appears
once, in an ordinary narrative sentence, not a rule. Reported plainly rather than padded: **one of the
three contest entries checked contributed nothing mechanical.**

---

## Text-quality note

All 15 non-OCR PDFs had clean embedded text (>1,300 chars/page minimum, most 2,600–5,900). Only
`settlement-events-1.pdf` and `settlement-events-2.pdf` were image-only (0 chars/page pre-OCR);
rendered at 300dpi via PyMuPDF and OCR'd with `pytesseract --psm 6` (`C:\Program Files\Tesseract-OCR\tesseract.exe`).
`book-of-the-arbitrator.pdf` has a font-layer rendering artifact that quadruples extracted heading text
(cosmetic to extraction, confirmed not present in the source's actual layout by checking surrounding
prose) — noted so a future capture doesn't mistake it for a genuinely duplicated section.

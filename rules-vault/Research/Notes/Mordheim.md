---
type: research-note
title: Mordheim
game: Mordheim
publisher: Games Workshop (1999); rules consolidated by the community at mordheimer.net
designer: Tuomas Pirinen
depth: primary — full rules-wiki read (core rules, campaign, encampments, psychology, income) cross-checked against the 122pp Living Rulebook PDF
retrieved: 2026-08-21
source_url: https://mordheimer.net
capture: research/sources/mordheim/
tags: [settlements/research]
---
# 🎲 Mordheim

> [!abstract] In one breath
> The **direct ancestor of our Fate table**, read properly for the first time instead of from a summary — and it turns out Mordheim **already has a base-building layer we didn't know about**. Two of them, in fact: a three-camp **Encampment** system and a completely separate **Lustria settlements** ruleset, neither of which appears in the core rulebook. The **Serious Injuries chart is confirmed word-for-word identical** between the community wiki and the official Living Rulebook — the one number in this whole vault we've been citing from memory is now nailed down exactly. And the psychology suite turns out to be a cautionary tale about scope creep: **six named mental states before a single optional supplement gets added, and the supplement roughly doubles the bookkeeping again.**

| | |
|---|---|
| **Designer · publisher** | Tuomas Pirinen · Games Workshop (1999) |
| **This read** | The New Mordheimer (mordheimer.net), a Docusaurus wiki with active 2026 maintenance, cross-checked against `living-rulebook.pdf` |
| **Depth of read** | **Primary** — full rules-wiki read of the core spine, campaign layer, encampments, psychology and income; cross-checked page-for-page against the official Living Rulebook where both exist |
| **Raw capture** | `research/sources/mordheim/` |
| **Related note** | [[Necromunda and Mordheim]] — the older, secondary-source read; kept in place, this note supersedes it for Mordheim specifically |

---
## Why it's here

Mordheim is cited constantly in this vault as the ancestor of lasting injuries, underdog banding and the death-spiral warning — but every one of those claims, until now, came from a **summary of a summary**. This pass reads the actual chart, the actual campaign chapter, and the actual optional-rules supplements, and finds two things nobody expected: **a published base-camp layer** (Encampments — three named settlements, each with its own housing chart and shops) and **a second, unrelated settlement system** for the Lustria campaign setting. Both land directly on our [[Settlement]]/[[Structures]] layer and now make Mordheim a genuine fourth data point on the campaign-base question, alongside [[Oathmark]], [[Last Days Zombie Apocalypse]] and [[Fallout Wasteland Warfare]].

---
## The Serious Injuries chart — confirmed line for line

**Type:** Combat · **Take:** ⭐ steal — verified, not summarized

**[FACT — verified against two independent copies of the same official chart: the community wiki's `/docs/campaigns` page and `living-rulebook.pdf` pp.79-80. Every single line matches, word for word, including the D66 roll ranges.]**

A Henchman taken out of action rolls **D6: 1-2 removed permanently, 3-6 fights next battle unharmed.** A Hero taken out of action rolls **D66** (first die = tens, second = units):

| D66 | Result |
|---|---|
| 11-15 | Dead — removed, all gear lost |
| 16-21 | Multiple Injuries — roll D6 more times, re-rolling Dead/Captured/Multiple Injuries |
| 22 | Leg Wound — permanent −1 Movement |
| 23 | Arm Wound — 1: amputated, one-handed weapons only; 2-6: miss next game |
| 24 | Madness — 1-3: Stupidity forever; 4-6: Frenzy forever |
| 25 | Smashed Leg — 1: may not run; 2-6: miss next game |
| 26 | Chest Wound — permanent −1 Toughness |
| 31 | Blinded in One Eye — permanent −1 Ballistic Skill; a second blinding forces retirement |
| 32 | Old Battle Wound — roll D6 before every future game; on a 1, sits out |
| 33 | Nervous Condition — permanent −1 Initiative |
| 34 | Hand Injury — permanent −1 Weapon Skill |
| 35 | Deep Wound — miss D3 games |
| 36 | Robbed — survives, loses all gear |
| 41-55 | Full Recovery |
| 56 | Bitter Enmity — gains Hatred (D6: individual / their leader / their warband / all warbands of that type) |
| 61 | Captured — ransom, prisoner swap, sold to slavers, or worse depending on the captor |
| 62-63 | Hardened — immune to fear from now on |
| 64 | Horrible Scars — causes fear from now on |
| 65 | Sold to the Pits — a scripted duel; win for 50gc + 2XP with gear intact, lose and maybe die, maybe walk away stripped |
| 66 | Survives Against the Odds — +1 Experience |

**Why it works.** It is the template every later "injury table" in the hobby is judged against, and the shape is
instructive on its own terms: roughly **45% of results are a full or near-full recovery** (41-55 plus 66, i.e. 16
of 36 D66 combinations), **death is a fixed ~14%** (11-15), and everything else is a **graded, mostly-temporary
cost** — miss-a-game penalties far outnumber permanent stat losses. It is not a 50/50 coin flip on a Hero's life;
it is heavily weighted toward keeping the roster intact, with a long tail of flavourful, table-friendly setbacks.

**For Settlements.** This is the chart our own **Fate** table (`natural 1 = Dead, natural 10 = Hardened, modifiers
capped at +2`) already descends from in spirit — Mordheim's own **62-63 Hardened** and **11-15 Dead** are the exact
two poles our system names on its own natural 1/10. Two structural notes worth carrying into [[Damage]] and
[[Progression]]:

- **The "re-roll and stack" shape of Multiple Injuries (16-21)** is a clean way to let one bad roll cascade
  into several minor penalties without ever risking a second death or capture in the same event — worth
  considering if Fate ever needs a "very bad but not fatal" outcome with more texture than a single line.
- **Sold to the Pits (65)** is the one result that's a *mini-scenario*, not a table lookup — it converts a
  bad roll into a second chance to reverse it through play, which is a nicer feeling than a pure dice outcome
  and costs nothing extra to run (it's a duel, not a new subsystem).

See also [[Necromunda and Mordheim#Lasting injuries]] — that note's summary-level treatment holds up completely
against this primary read; nothing there needs correcting, only reinforcing with an exact citation.

---
## The encampment layer — two full settlement rulesets we didn't know existed

**Type:** Settlement · **Take:** ⚙️ adapt — the single most important finding in this capture for our open question

**[FACT — community-consolidated optional rules from Town Cryer magazine, not the core rulebook or the Living Rulebook. `/docs/optional-rules/encampments` states outright: "These rules are purely experimental and although we would encourage players to use them they are as yet unofficial."]** Mordheim has a base-camp layer, and it long predates any of Necromunda's settlement content. It comes in **two entirely separate, non-interoperating systems**:

### System one — the three Encampments (core setting)

A warband picks **one** of three named camps to live in, after their first battle:

| Camp | Character | Cost of residence | Notable mechanic |
|---|---|---|---|
| **Sigmarhaven** | Safest, lawful, Sigmar-aligned | **Tithe: 2 wyrdstone shards per battle** | Racially restricted resident list (no mutants/Possessed) |
| **Brigandsburg** | Rougher middle ground | None stated, but hired swords cost only 75% | Rare-item searches risk ambush (Initiative test or lose the search) |
| **Cutthroat's Den** | Lawless, anyone welcome | Goods cost **double** | Goods found at **+2** easier; has a slaver and an underground fighting pit |

Each camp then rolls a **2D6 Housing chart** (Drinking Den / Old House / Tents / Ruined Farmhouse / Old Shrine /
Cellar, or camp-specific equivalents like Tavern/Farm/Barracks) that hands out a small passive perk — extra
Rare-item finding rolls, a bonus recruit slot, free healing herbs, an infiltration option via a cellar/sewer.
Between battles, a warband rolls **D3 "locations to visit"** (Smithy, Muleskinner, Merchant, a surgeon/apothecary,
a gambling den) and, between visits, rolls on a **d66-scale Settlement Events table** — pickpocketing, bar
brawls, forced conscription, a captain of the Watch trying to recruit you, drugged drinks, a lucky find. Every
one of these tables is a small, self-contained encounter, not a system that touches the battle rules.

### System two — the Lustria settlements (separate campaign setting, unrelated ruleset)

A completely independent settlement system for the Lustria supplement: **Santa Magritta** (best-equipped, a
town watch shows up mid-battle and can be bribed off, 10% income tithe, several races banned outright),
**Nuevo Luccini** (a pirate den, +2 to find goods at standard price), and **Skeggi** (a Norse colony, discounted
upkeep for five named Hired Sword types). It shares **no mechanical grammar at all** with the Encampments
system above — different chart shapes, different currencies of benefit, written by different Town Cryer
contributors for a different supplement. There is no unified "Mordheim settlement system"; there are two
separate, campaign-setting-scoped ones.

**Why it matters, structurally.** Both systems are built from the same three ingredients: **(1) a tithe or price
penalty for residency, (2) a random housing roll for a small passive perk, (3) a rotating menu of visitable
NPC shops, each with its own tiny sub-table.** Nothing here is a persistent, buildable base — there is no
construction, no upgrade path, no player agency over what the camp becomes. The "settlement" is a **flavourful
random modifier on the post-battle sequence**, re-rolled fresh at every visit rather than built up over a
campaign. This is the opposite end of the spectrum from Oathmark's structural kingdom or Fallout's buildable
Homestead.

**For Settlements — the four-way comparison.** [[Oathmark#The kingdom widens the menu]] persists structurally
(fixed territories, growth is lateral). [[Last Days Zombie Apocalypse#The Refuge costs zero]] persists as a
free, numeric base entirely outside the crew budget. [[Fallout Wasteland Warfare]]'s Homestead is a buildable,
upgradeable physical layout with real structural damage. **Mordheim's Encampments are the fourth and weakest
data point: a settlement that's mostly a random-table wrapper around trading, with almost no player-directed
construction.** That's genuinely useful as a *lower bound* — it tells us what "the least you could ship and
still call it a settlement layer" looks like, and it's clearly less than what [[Settlement]] and [[Structures]]
already have (a real footprint canvas, 23 buildable structures, Materials/Power resources). The one piece worth
lifting directly: **a residency tithe as the cost of a benefit**, rather than a flat upkeep number — Sigmarhaven's
"2 shards per battle for the safest camp" is a clean, single-number trade that a [[Settlement]] Location or
district choice could reuse for a "safe but taxed" vs "cheap but risky" fork. The Housing-chart-per-visit shape
(random small perk, re-rolled if the camp is lost) is much lighter than anything we'd want — it's built for a
Town Cryer article's worth of table content, not a campaign spine.

---
## Lads Got Talent — henchmen graduate into heroes

**Type:** Progression · **Take:** ⭐ steal

**[FACT]** On a Henchman-group advance roll of **10-12 (2D6)**, one model in the group is promoted to a full Hero:
it **keeps its accumulated Experience and every characteristic increase it already earned**, the player picks
two Skill lists it can now draw from, and it immediately makes one roll on the Heroes' own Advance table. The
rest of the group re-rolls their own advance (re-rolling further 10-12s, so only one promotion per roll).

**Why it works.** It is a **zero-cost, dice-triggered narrative moment** built entirely out of machinery the
game already has — no new currency, no new roll type, just a re-interpretation of an existing advance-table
result. A nameless mook becomes a named character exactly because he survived and rolled well, which is a
better story than anything a designer could script deliberately.

**For Settlements.** Directly relevant to [[Progression]] and to the project's own standing idea (already
recorded in [[Necromunda and Mordheim#Lasting injuries]]) that **a permanent injury should have a second life**
— a fighter losing a leg becoming a settlement worker. Lads Got Talent is the **mirror image** of that idea:
promotion upward (henchman → hero) instead of demotion sideways (fighter → worker). Together they suggest our
Level/Rank track could have **two exit ramps at the bottom**, not just a ladder going up: a low-rank
Recruit/Fighter who rolls well enough on a future advance could jump a rank tier the same way a henchman
group here jumps to Hero status, using the existing advance-roll machinery rather than a new promotion system.

---
## The underdog XP table — an independent third confirmation

**Type:** Campaign · **Take:** 📎 reference — confirms, does not correct

**[FACT — confirmed identical in the wiki, the Living Rulebook, and the Ultimate Reference Sheet]**

| Rating gap | XP bonus |
|---|---|
| 0-50 | None |
| 51-75 | +1 |
| 76-100 | +2 |
| 101-150 | +3 |
| 151-300 | +4 |
| 301+ | +5 |

This is the exact table already logged at [[Necromunda and Mordheim#Underdog banding]] — that note correctly
described the *mechanism* ("scales by the difference in rating") from a secondary source; this primary read
supplies the actual numbers and confirms them against two independent official documents. **No correction
needed** to the existing hub row; this is the citation that was missing.

**Warband Rating itself is also confirmed exactly as summarized:** `(warriors × 5) + accumulated Experience`,
with large creatures (Rat Ogres etc.) worth 20 points instead of 5 — verbatim identical in the wiki, the Living
Rulebook, and the Ultimate Reference Sheet. Three independent documents, zero disagreement.

---
## Wyrdstone — a price that falls twice, by design

**Type:** Economy · **Take:** ⭐ steal

**[FACT]** Selling wyrdstone pays out on a table keyed to **both** the number of shards sold in one sale *and*
the size of the selling warband:

| Shards sold | 1-3 warriors | 4-6 | 7-9 | 10-12 | 13-15 | 16+ |
|---|---|---|---|---|---|---|
| 1 | 45 | 40 | 35 | 30 | 30 | 25 |
| 2 | 60 (30ea) | 55 | 50 | 45 | 40 | 35 |
| 4 | 90 (~23ea) | 80 (20ea) | 70 | 65 | 60 (15ea) | 55 |
| 8+ | 155 (<19ea) | 140 | 130 | 120 | 110 | 100 |

*(full 8-row table in `research/sources/mordheim/source.md`)*

**Why it works.** Price per shard **falls** as you sell more at once (selling in dribbles is worth more per
piece than dumping a hoard) *and* falls again as the warband grows (a bigger warband's maintenance overhead
eats a bigger cut). Two independent diminishing-returns curves compress into one table, with no explicit
"maintenance cost" line item anywhere on a roster sheet — the tax is baked directly into the sale price instead
of being a separate upkeep subtraction.

**For Settlements.** Directly useful for [[Economy]]. If Settlements ever wants a soft brake on hoarding loot
before converting it to Credits, this is a proof that **the brake can live entirely inside the exchange rate**
rather than as a separate bookkeeping step — sell in smaller batches for a better rate, or take the hit for
convenience. It also quietly answers a version of the "play frequency beats skill" problem
([[Necromunda and Mordheim#Play frequency beats skill]]): a warband that's grown large from winning a lot pays
a worse per-shard rate from then on, a second, independent anti-snowball valve layered on top of underdog
banding.

---
## The Exploration table's multiples — one dice roll, two independent lotteries

**Type:** Economy · **Take:** ⚙️ adapt

**[FACT]** The same pool of exploration dice (1 per surviving Hero, +1 if you won, max 6) does double duty:
the **sum** determines shard count (table above), while **any matching pair or better** (doubles through
six-of-a-kind) triggers a lookup on a **30-entry Exploration Chart** — Wells, Shops, a Smithy, a Gunsmith, a
Graveyard, all the way up to a six-of-a-kind Noble's Villa or a chance at one of six named Magical Artefacts.
Rolling a double **and** a triple in the same batch only looks up the rarer one; the sum is unaffected either way.

**Why it works.** It's a genuinely efficient piece of design: **one dice pool answers two questions** (how much
loot, and did anything special happen) with **no extra rolling**. The rarity gradient is free — six-of-a-kind
on 6 dice is astronomically unlikely, so the best rewards gate themselves without a separate rarity roll.

**For Settlements.** Worth a look for [[Events]] or the post-battle sequence generally — if a resource-gathering
roll of some kind already exists, checking that *same* roll for a pattern (rather than adding a second
"anything special happen?" roll) is a free way to make results feel less uniform without adding table time.

---
## The classic psychology suite — six states before Insanity is even added

**Type:** Morale · **Take:** ⚠️ avoid the raw headcount, ⭐ steal the individual mechanisms

**[FACT — docs/rules/leadership-psychology]** Before any optional supplement, a Mordheim warrior can be subject
to: **Rout** (army-wide break test at 25% casualties), **All Alone** (lone-model nerve check with an automatic
free hit on failure), **Fear** (charge-or-be-charged Ld test, failure = need 6s to hit), **Frenzy** (forced
charge, doubled Attacks, temporary immunity to the other five states), **Hatred** (free re-roll in the first
round only), and **Stupidity** (Ld test each turn, failure = shamble or drool). Orc/Goblin models add a seventh,
**Animosity** (a further per-turn roll that can force infighting).

**Why it's worth naming as a cost, not just a feature list.** That's **six to seven separate named states**,
each with its own trigger condition, its own roll, and its own table-time — before the optional
**"At the Mouth of Madness"** Insanity supplement is added on top. **[FACT — Insanity is explicitly a bolt-on,
Town Cryer #8, not the core rulebook]** It layers a **second, parallel D66-scale advancement track** (Insanity
Points, marked from the opposite end of the same Experience boxes) with its own 21-entry, 4D6-keyed table of
named conditions (Amnesia, Paranoia, six flavours of phobia, multiple personalities, and outright removal from
the roster at the extreme). **The optional supplement roughly doubles the psychology bookkeeping the base game
already has.**

**For Settlements.** This is the load-bearing comparison for the stated want of Insanity/terror beyond the
current Stress track ([[Morale]], [[Conditions]]) — Mordheim's classic suite is the **genre-standard maximalist
version**, and it costs six-plus named states plus (optionally) a second full advancement track just to reach
"classic." Our locked design already collapses fear/suppression into **one mechanic** (a failed wound becomes
Stress) precisely to avoid this — this capture is direct, primary evidence for *why* that collapse was the
right call, not just an assertion. If [[Morale]] or [[Conditions]] ever wants a single "flavour" state worth
borrowing cheaply, **Frenzy's forced-charge-for-double-Attacks** is the one mechanism here that's genuinely one
line and self-contained, with no interaction table required.

---
## Rating, campaign spine and core resolution — confirmed, not corrected

**Type:** Dice · **Take:** 📎 reference

**[FACT]** The turn is IGO-UGO with four phases (Recovery, Movement, Shooting, Hand-to-hand — **both sides fight
in the HTH phase regardless of whose turn it is**). Stat tests are **D6 roll-under**, Leadership tests are
**2D6 roll-under**, to-hit uses opposed WS/BS charts, to-wound compares Strength against Toughness on a second
chart, armour saves are flat D6 thresholds (Light 6+, Heavy 5+, Gromril 4+, shield +1), and a natural 6 to wound
causes a critical hit (double wound, often ignoring armour, occasionally +2 to the Injury roll). **None of this
machinery ports to our engine** — Settlements runs a single flat `1d10 + Stat vs 7+` with **no second dice
type anywhere**, where WFB-derived Mordheim runs three separate opposed charts (to-hit, to-wound, armour save)
each keyed to a different characteristic pair. This is exactly the "genre-conventional, not our conventions"
gap the brief warned about — worth naming explicitly so nobody mistakes Mordheim's charts for a template.

**For Settlements.** Nothing to adopt mechanically from the dice engine itself. The value is entirely in what
sits on top of it (injuries, campaign, income, psychology) — captured above.

---
## Source disagreements found this pass

Two, both minor, both in the same direction (a community-condensed cheat sheet vs. two independent primary
sources that agree with each other):

- **`post-game-chart.pdf`** (a fan-made summary sheet, not the wiki or the Living Rulebook) prints **"23 Arm
  Wound: 2-5 = miss next game"** and **"25 Smashed Leg: 2-5 = miss next game."** Both the wiki and the Living
  Rulebook say **2-6** for both entries — the cheat sheet silently drops the "6" result in two places. **Trust
  the wiki/Living Rulebook pairing**; this looks like a transcription slip, not a rules variant.
- The same cheat sheet adds a **1-4/5-6 sub-roll on who holds a Captured prisoner** (winning warband vs. the
  warband that scored the KO) that appears in **neither** the wiki nor the Living Rulebook. Likely a
  multiplayer house addition by whoever compiled the sheet, not a published rule.

Everywhere else checked — the Serious Injuries chart, the Experience/Advance tables, the underdog table, the
Warband Rating formula, core armour costs — **the wiki and the Living Rulebook agree exactly**, which is itself
worth recording: this wiki earns its "faithful consolidation" billing on every load-bearing number checked.

---
## Source

- Primary: The New Mordheimer (mordheimer.net), `/docs/rules/*`, `/docs/campaigns/*`, `/docs/optional-rules/*` — a community-maintained Docusaurus wiki, active through Aug 2026 per its own blog, consolidating published Mordheim (core rulebook, Town Cryer magazine, Mordheim Annual, official supplements)
- Cross-check: `living-rulebook.pdf` (122pp), `ultimate-reference-sheet.pdf` (6pp), `campaign-reference.pdf` (2pp), `post-game-chart.pdf` (2pp) — all hash-verified against `G:\My Drive\Wargaming\Mordheim\`
- Capture: `research/sources/mordheim/source.md`, `research/sources/mordheim/meta.json`
- Related: [[Necromunda and Mordheim]] (the prior secondary-source read — see the pointer at the top of that note) · [[Wargaming Research Hub]] · [[Oathmark#The kingdom widens the menu]] · [[Last Days Zombie Apocalypse#The Refuge costs zero]] · [[Fallout Wasteland Warfare]] · [[Trench Crusade]] (same designer, later game) · [[Settlement]] · [[Structures]] · [[Progression]] · [[Damage]] · [[Economy]] · [[Morale]] · [[Conditions]] · [[Events]]

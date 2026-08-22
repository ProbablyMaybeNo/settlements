# Necromunda — Core Rules Capture (source-core.md)

Raw capture for the **core rules** slice of the Necromunda research pass. Campaign systems
(Dominion, Law & Misrule, Uprising, Outlander, Ash Wastes, Succession, Underhells) are being
captured separately by another agent into `Necromunda Campaigns.md` — not duplicated here.

**Primary secondary source:** NecroRAW (`https://www.necroraw.com.ru`), a community
Docusaurus site that consolidates verbatim ("RAW") Necromunda rules across ~30 publications,
currently covering N17/N23 with N26 in progress. Its own footer states it is *"a community
project not associated with Games Workshop."* Site is `robots: noindex, nofollow` — no sitemap
crawl is possible; every page below was reached by following child links from the section
roots given in the task brief.

**Primary sources held in the library, used for direct cross-check (see meta-core.json for
hashes and paths):**
- `G:\My Drive\Wargaming\NECROMUNDA\RULE BOOKS\Necromunda Core Rulebook Revised 2023.epub` —
  the actual N23 Core Rulebook Ross owns. **This is the correct primary source for "N23" claims
  below** — it is NOT the same file as the staged `research/sources/necromunda/core-rulebook.pdf`
  (see the correction note at the very top of the findings — that staged PDF is actually the
  **1995 Necromunda Living Rulebook**, mislabeled).
- `research/sources/necromunda/core-rulebook.pdf` — verified by direct text extraction to be
  the **1995 Necromunda Living Rulebook** (compiled by Andy Hall; QuarkXPress/Distiller 2005
  metadata), NOT the N23 Core Rulebook the filename implies. Kept and used deliberately as the
  **1995 primary-source data point** for the injury-table and gang-rating lineage comparison.
- `research/sources/necromunda/book-of-judgement.pdf`, `book-of-the-outcast.pdf`,
  `ash-wastes.pdf` — not needed for this core-rules pass (they're supplement/campaign books);
  flagged for the campaign-systems agent if useful.

---

## ⚠️ Correction: the staged "core-rulebook.pdf" is not the N23 rulebook

Direct `fitz` text extraction of `research/sources/necromunda/core-rulebook.pdf` (page 1) reads:

> *"Living Rulebook edition compiled by Andy Hall / A big thanks to Robert J. Reiner, Nick Jakos
> and john french"*

PDF metadata: `title: NECROLRB`, `creator: QuarkXPress: LaserWriter 8`, `creationDate:
D:20051212105907Z`. Its table of contents (page 2) lists "CHARACTERISTICS... THE TURN..." and
"HIVE PRIMUS... GANG RECRUITMENT... WEAPONS" — this is the **1995 Necromunda Living Rulebook**
compilation, not the 2023 Core Rulebook. Its own page numbering runs to only 120 pages, which
also doesn't match N23's citations (p124, p142, p148 etc. — those numbers are simply higher
than this PDF's page count).

The actual N23 Core Rulebook exists in the library as an **EPUB**, not a PDF:
`G:\My Drive\Wargaming\NECROMUNDA\RULE BOOKS\Necromunda Core Rulebook Revised 2023.epub`.
`fitz`'s page-render text extraction on this epub is badly truncated (each rendered "page"
returns only a handful of characters per line, apparently due to CSS multi-column reflow) —
**do not trust `fitz.get_text()` on this file.** Unzipping it as a plain zip archive and
stripping the embedded XHTML tags directly gives clean, complete text. Filenames inside encode
the print-page ranges they cover (e.g. `142-163_NM_Core_Rulebook_23_EPUB-8.xhtml`), which let
targeted page ranges be pulled without extracting the whole 714-entry archive. All "[FACT,
verified against N23 epub]" tags below used this method.

---

## 1. Lasting Injuries (N23) — `docs/the-rules/game-structure/the-action-phase/resolve-hits`

RAW ✔️ *Necromunda Core Rulebook (2023), p124* (NecroRAW citation) — cross-verified against
`Necromunda Core Rulebook Revised 2023.epub`, print pages 126–127 (epub's own running folio),
**word-for-word identical**.

### Resolving Hits Against Fighters

1. **Make Wound Roll** — cross-reference weapon Strength vs fighter Toughness, roll D6:

| Strength vs Toughness | D6 Roll Required |
|---|---|
| Strength **TWICE** Toughness or greater | 2+ |
| Strength **GREATER** than Toughness | 3+ |
| Strength **EQUAL** to Toughness | 4+ |
| Strength **LOWER** than Toughness | 5+ |
| Strength **HALF** Toughness or lower | 6+ |

2. **Make a Save Roll** — one Save roll per hit that wounds (or that leads to an Injury roll),
   regardless of how many Save types the fighter has. AP can cancel armour saves entirely.
   Positive save modifiers (partial/full cover vs Blast) can improve armour saves but not Field
   armour; an unarmoured fighter is treated as a 7+ save for modifier purposes. **Natural 1 on
   a Save roll is always an automatic failure**, regardless of modifiers.

3. **Inflict Damage** — each point of weapon Damage removes one Wound. At 0 Wounds, roll one
   Injury dice; any further Damage points each roll an additional Injury dice.

**Injury dice** (three symbols): **Out of Action** (removed from play, no further part in this
battle) · **Serious Injury** (Standing/Pinned → Prone and Seriously Injured; a second Serious
Injury result while already Seriously Injured instead adds a Flesh Wound) · **Flesh Wound**
(−1 Toughness; Toughness 0 = Out of Action).

Damage `-` weapons (toxins/gas) cause no Wound loss but still roll Injury dice as normal.

### Lasting Injuries — the D66 procedure

> *"Whenever a fighter goes Out of Action, the opposing player immediately rolls two D6, one
> after the other (a D66 roll) and looks up the result on the Lasting Injuries table... During
> Campaign play, the result is applied against the fighter... Rolling for Lasting Injuries must
> be done during Campaign play. Should players wish, they can forgo this step during Skirmish
> play..."*

Two outcomes gate participation: **Convalescence** (cannot perform post-battle actions or work
Territories, but IS available for the gang's next battle) vs **Recovery** (misses the gang's
next battle entirely, regardless of how many Lasting Injury rolls stack — only ever one missed
battle).

**Falling** (3"+ fall): automatic hit, Strength/AP/Damage keyed to distance fallen (3"-5":
S3/-/1 · 6"-7": S5/-1/1 · 8"-9": S7/-2/2 · 10"+: S9/-3/3). A model landed on takes an identical
hit.

**Characteristic Reductions**: Credits value never changes when a Lasting Injury reduces a
stat. No characteristic may drop below the table minimum; a result that would is simply not
applied.

### Lasting Injury Table (N23, verbatim) — verified against the epub, exact match

| D66 | Lasting Injury |
|---|---|
| 11 | **Lesson Learned:** Convalescence but gains D3 Experience. |
| 12 | **Impressive Scars:** +1 Cool. Once only — further results treated as Out Cold. |
| 13 | **Horrid Scars:** gains the Fearsome skill. If already has it, treat as Out Cold. |
| 14 | **Bitter Enmity:** gains Berserker skill vs the gang that inflicted this injury. If already has it or rolled again, treat as Out Cold. |
| 15-26 | **Out Cold:** misses rest of the battle, no long-term injury, available for post-battle actions. |
| 31-36 | **Convalescence.** |
| 41 | **Old Battle Wound:** D6 before every future battle; on a 1, Convalescence. |
| 42 | **Partially Deafened:** no penalty first time; −1 Leadership on a repeat. |
| 43 | **Humiliated:** Convalescence, −1 Leadership and −1 Cool. |
| 44 | **Eye Injury:** Recovery, −1 Ballistic Skill. |
| 45 | **Hand Injury:** Recovery, −1 Weapon Skill. |
| 46 | **Hobbled:** Recovery, −1 Movement. |
| 51 | **Spinal Injury:** Recovery, −1 Strength. |
| 52 | **Enfeebled:** Recovery, −1 Toughness. |
| 53 | **Head Injury:** Recovery, −1 Intelligence and −1 Willpower. |
| 54 | **Multiple Injuries:** roll D3 more times, re-rolling Captured/Multiple Injuries/Memorable Death/Critical Injury/Out Cold. |
| 55-56 | **Captured.** |
| 61-65 | **Critical Injury:** dies unless successfully treated by a Doc visit (Medical Escort) in the post-battle sequence. |
| 66 | **Memorable Death:** killed instantly. If caused by an Attack action, attacker gains +1 XP. |

### Nerve Tests

Cool test (+1 per non-Broken, non-Seriously-Injured friendly fighter within 3") triggered
whenever a friendly fighter is Seriously Injured/Out of Action within 3", or a friendly vehicle
Wrecked within 6". Fail = **Broken** (immediate free Running for Cover (Double), loses Ready
marker, −2 to Reaction attacks while engaged, rallies in End phase). Vehicles have an analogous
Nerve Test vs Wrecked vehicles within 6".

---

## 2. Lasting Injuries — the 1995 ancestor, "Serious Injuries" (verbatim from the primary PDF)

Extracted directly from `research/sources/necromunda/core-rulebook.pdf` (the 1995 Necromunda
Living Rulebook), pages 83–85 of the scanned text.

> *"SERIOUS INJURIES — During a game some fighters will go out of action and are removed from
> play... When you are playing a campaign it matters a great deal what happens to fighters who
> go out of action!... To find out what happens to fighters who go out of action roll two dice
> and consult the Serious Injuries chart. The first dice roll represents 'tens' and the second
> 'units'... This type of dice roll is referred to as a D66 roll."*

### Serious Injuries Table (1995, verbatim)

| D66 | Serious Injury |
|---|---|
| 11-16 | **Dead.** All weapons/equipment lost. |
| 21 | **Multiple Injuries:** roll D6 more times, re-rolling Dead/Full Recovery. |
| 22 | **Chest Wound:** −1 Toughness. |
| 23 | **Leg Wound:** −1 Movement (random leg). |
| 24 | **Arm Wound:** −1 Strength when using that arm (random arm). |
| 25 | **Head Wound:** D6 at the start of each game — 1-3 Stupidity, 4-6 Frenzy. |
| 26 | **Blinded in One Eye:** −1 Ballistic Skill (random eye); a second blinding forces retirement. |
| 31 | **Partially Deafened:** no penalty first time; −1 Leadership on repeat. |
| 32 | **Shell Shock:** −1 Initiative. |
| 33 | **Hand Injury:** lose D3 fingers, −1 Weapon Skill; losing all 5 fingers on a hand makes it unusable (no two-handed weapons). |
| 34-36 | **Old Battle Wound:** D6 before each game, on a 1 miss the battle. |
| 41-55 | **Full Recovery.** |
| 56 | **Bitter Enmity:** hatred (D6 sub-table: individual attacker / their leader / their gang / their whole House). |
| 61-63 | **Captured.** Exchange/ransom/sold to Guilders for D6×5 credits. |
| 64 | **Horrible Scars:** causes fear. |
| 65 | **Impressive Scars:** +1 Leadership, once only. |
| 66 | **Survives Against the Odds:** full recovery + D6 Experience. |

**Distribution (36 D66 combinations):** Dead 6 (16.7%) · named permanent/temporary debuffs
(Chest/Leg/Arm/Head/Blinded/Deafened/ShellShock/Hand/OldBattleWound) 11 (30.6%) · Multiple
Injuries 1 (2.8%) · Full Recovery 11 (30.6%) · Bitter Enmity 1 (2.8%) · Captured 3 (8.3%) ·
Horrible Scars 1 (2.8%) · Impressive Scars 1 (2.8%) · Survives Against the Odds 1 (2.8%).

Note the 1995 rulebook does **not** have Convalescence/Recovery as a systemic "sits out N
battles" mechanic at all — the only recurring miss-a-battle risk is Old Battle Wound's D6 check;
every other named debuff applies immediately with **no missed-battle clause**.

---

## 3. Gaining Experience & Advancements (N23) — `docs/the-rules/gaining-experience`

RAW ✔️ *Necromunda Core Rulebook (2023), p148* — cross-verified verbatim against the N23 epub
(print pages 149–150 in the epub's own folio).

XP awards: 1 XP causing a Serious Injury (+1 more if target is Leader/Champion) · 2 XP for
wrecking an enemy vehicle · 2 XP for taking an enemy fighter Out of Action (+1 more if
Leader/Champion) · 1 XP for taking part in a battle (only if the scenario doesn't already grant
it) · 1 XP for rallying from Broken · 1 XP for assisting another fighter's Recovery test.
*Fighters can only gain the Serious-Injury/Out-of-Action XP once per enemy fighter per
activation.*

### Advancement table (Leaders, Champions, Crews, Prospects, Juves & Specialists) — verbatim, verified against the epub

| XP Cost | Advancement | Credit Cost Increase |
|---|---|---|
| 3 XP | Improve Willpower or Intelligence by 1 | +5 credits |
| 4 XP | Improve Leadership or Cool by 1 | +10 credits |
| 5 XP | Improve Initiative by 1 | +10 credits |
| 5 XP | Add 1" to Movement | +10 credits |
| 6 XP | Improve Weapon Skill or Ballistic Skill by 1 | +20 credits |
| 6 XP | Random skill from a Primary Skill Set | +20 credits |
| 8 XP | Increase Strength or Toughness by 1 | +30 credits |
| 9 XP | Chosen skill from a Primary Skill Set | +20 credits |
| 9 XP | Random skill from a Secondary Skill Set | +35 credits |
| 12 XP | Increase Wounds or Attacks by 1 | +45 credits |
| 12 XP | Specialists only: promote to Champion + random Primary skill | +40 credits |
| 12 XP | Chosen skill from a Secondary Skill Set | +35 credits |
| 15 XP | Random skill from ANY Skill Set | +50 credits |

**The escalation rule — verbatim, and narrower than previously logged:**

> *"The more experienced a model is, the more certain Advancements cost to purchase in terms of
> XP. **The cost of each characteristic Advancement for the same characteristic taken is
> increased by 2 XP for each instance after the first.** For example, a Champion may increase
> their Initiative by 1 for 5 XP, but to increase it by 1 a second time will cost them 7 XP.
> **Juves and Prospects however are particularly fast learners, and as a result they suffer no
> such penalty on characteristic increases**; they may increase a characteristic any number of
> times (up to the maximum) for the basic XP cost shown each time."*

This is **not** a global "each advance costs +2 more than the last" rule — it escalates only
the **same named characteristic**, purchased again, and **Juves/Prospects are explicitly
exempt**. Skill purchases and different-characteristic purchases are unaffected.

### Gangers — the simplified track

Once a Ganger (not Specialist) hits 6+ XP, roll 2D6 on a separate table and spend exactly 6 XP
regardless of the result:

| 2D6 | Result | Credit increase |
|---|---|---|
| 2 | Becomes a Specialist + random Primary skill | +20 |
| 3-4 | WS or BS +1 | +20 |
| 5-6 | Str or Tough +1 | +30 |
| 7 | Movement +1" or Initiative +1 | +10 |
| 8-9 | Will or Int +1 | +5 |
| 10-11 | Ld or Cool +1 | +10 |
| 12 | Becomes a Specialist + random Primary skill | +20 |

**Maximum Characteristics**: no fighter may improve Movement/Strength/Toughness more than
twice beyond their category's basic profile, nor Wounds/Attacks more than once. If a Ganger
roll would breach this, treat the roll as a 12 instead.

---

## 4. The Post-Battle Sequence (N23) — `docs/the-rules/the-post-battle-sequence`

RAW ✔️ *Necromunda Core Rulebook (2023), p142.* Seven steps, in strict order, both players
present:

**1. Wrap-Up** — Succumbing to Injuries (Seriously Injured fighters roll D6: 3+ survive, 1-2
succumb → Out of Action → Lasting Injury roll) · Being Captured (D6 escape check, −1 if draw,
−2 if lost, −2 if Webbed; 4+ escapes to Convalescence, natural 6 always escapes) · Claiming
Scrap (sole survivor gang gets D3×10 credits per Wrecked enemy vehicle) · Captive Fighters
(Rescue Mission challenge, bounty/dispose/trade/sell-to-Guilders options) · Trading Captive
Models (freeform trade agreement between controlling players).

**2. Assign/Reassign Territory** — winner takes the staked Territory; draws leave it unclaimed
or unchanged.

**3. Receive Rewards** — scenario-specific rewards to Stash; Reputation gains applied before
losses.

**4. Collect Income** — credits from all controlled Territories added to Stash.

**5. Post-Battle Actions** — one action per fighter with Gang Hierarchy (X), in any order:
**Trade** (visit Trading Post) · **Sell to the Guilders** (Captive worth 50% of Cost, rounded
up to nearest 5) · **Claim Bounties** (Law Abiding vs Outlaw Captive, full Cost) · **'Dispose'
of Captives** (Outlaw only) · **Medical Escort** (pay 2D6×10 credits to save a Critical Injury,
D6: 1 dies / 2-5 Stabilised + Recovery / 6 Full Recovery + Recovery) · **Negotiate Repairs**
(D6: 1-3 quarter-cost repair but a Persistent Rattle remains / 4-5 quarter-cost clean repair /
6 tenth-cost repair).

**6. Update Roster** — six sub-steps: **A. Clean House** (dead fighters' gear to Stash unless
gang had zero survivors on the table; retire injured fighters; scrap Lasting-Damage vehicles
for 25% of Cost) · **B. Visit the Trading Post** (Hire a Fighter, Purchase a Vehicle, Recruit
Hangers-on & Brutes, Sell Unwanted Items at value minus D6×10 to a 5-credit floor, Purchase
Equipment, **Seek Rare & Illegal Equipment** — 2D6 + Leader's Trade (+2) + each Champion's Trade
(+1) + 1 per full 10 Reputation, gating Rare(X)/Illegal(X) access differently for Law-abiding vs
Outlaw gangs) · **C. Gain Boons from Territories** · **D. Distribute Equipment** · **E. Purchase
Advancements** · **F. Update Gang Rating** (recalculated last, so every earlier reference in
this sequence uses the *pre-update* rating).

**7. Report Results** — battle outcome, Territory changes, casualties, final Gang Rating and
Wealth reported to the campaign Arbitrator.

---

## 5. Gang Rating vs Wealth (N23) — settles the stash question, verbatim, verified against the epub

`docs/founding-a-gang/` → `The Gang Roster` (NecroRAW summary confirmed directly against epub
print page 92):

> **GANG RATING** — *"The Gang Rating is an indicator of how powerful the gang is – the
> proficiency of its models, how well equipped it is, and so on. **The Gang Rating is the total
> cost of all of the fighters and vehicles in the gang, including the cost of all the equipment
> and Upgrades they are equipped with.**"*

> **WEALTH** — *"In Campaign play, gangs also have a Wealth value – **this is equal to the
> total cost of all of the fighters and vehicles in the gang, plus the value of any credits or
> equipment they have in their Stash.**"*

The gang roster separately lists (element 7) **"its Stash (7), containing unspent credits,
surplus equipment (both weapons and Wargear)."** Rating counts only what's *equipped*; Wealth
adds the Stash on top. Two named, formally distinct tracked numbers.

### The 1995 ancestor — verbatim, from the primary PDF, pages 83 and 99–100

> *"THE GANG RATING — Each gang has what we call a gang rating – the higher the rating the
> better the gang. **The gang rating is simply the total value of all the fighters in the gang
> plus their total Experience points.** GANG RATING = VALUE OF FIGHTERS + EXPERIENCE"*

> *"ADJUSTING THE GANG RATING — The gang rating of each gang is equal to the value of its
> fighters plus their Experience points... **Any weaponry or other equipment that the gang keeps
> but does not give to a fighter is hoarded. It remains unissued in your hideout and its value
> is not included in the gang rating.**"*

Two more explicit examples of the same rule appear on page 89 for Screamers/Stummers: *"Screamers
are not carried by any particular model and their value is not included in the gang rating"* —
same wording, twice, for two different unassigned-equipment items.

**This is now a direct primary-source citation for both endpoints (1995 and 2023) of a 28-year
span**, not a secondary-source claim for 1995 as previously logged. 1995 had no separate
"Wealth" term — it simply excluded unassigned gear from the one Rating number. N23 keeps the
exact same exclusion but names and formalizes the excluded total as a second tracked stat,
Wealth.

---

## 6. Gang Creation & starting budget (N23) — `docs/founding-a-gang/gang-creation`

RAW ✔️ p81. **Campaign play: 1,000 credits** starting budget (Arbitrator may adjust). If
vehicles are used, **+400 credits** that can *only* be spent on Wargear granting the Mounted
condition, Crew, vehicles, or fighters that come with Mounted-condition gear by default —
unspent allowance from this pool is lost, not banked. **Skirmish play:** agreed budget, guideline
1,250–2,000 credits. Unspent credits go to Stash in Campaign play; are simply lost in Skirmish
play.

Equipment limits: 3 weapons per fighter on foot (2 if Mounted), weapons marked `*` take 2 slots.
Crew: 2 weapons max, gaining the Arc (Front) trait. **Tools of the Trade** special rule allows
multiple Fighter/Vehicle cards ("Equipment Sets") for one model at no extra cost — only one card
is used per battle, drawn at random if the scenario uses random models.

---

## 7. Conditions — `docs/general-principles/conditions`

RAW ✔️ p66. **Common:** Ready (placed on all models each Priority phase, removed on
activation) · Broken (from a Nerve Test fail; locked into Running for Cover, −2 Reaction
attacks if engaged) · Out of Ammo (per-weapon, from the Firepower dice) · Flesh Wound(s)
(stacking −1 Toughness).

**Other:** Blaze (auto S3/AP-1/D1 hit each activation, scatter move, extinguish on 6+ D6 +1 per
adjacent active friendly) · Blind (from Flash trait; loses Ready, Reaction-only hits on a
natural 6) · Concussion (−2 Initiative, min 6+, until end of round) · Hidden/Revealed ·
Intoxicated (effects vary by source) · Insane (D6 each activation: 1-2 auto-Broken/flees, 3-4
opponent controls the model this activation, 5-6 acts normally then a Willpower test to shed
it) · Webbed (treated as Seriously Injured for Recovery rolls; a failed Recovery roll while
Webbed maps to Out Cold on 1-4 or Captured on 5-6 instead of the full Lasting Injury table) ·
Mounted (a whole rules bundle: Hands Full, Ride By, Quick Retreat, Grounded, "I Get Knocked
Down…" — falls Prone instead of auto-pinning, graduated fall damage by distance moved).

**Additional (supplement-sourced):** Gunked (Book of Peril) — −1 Movement, −1 Initiative,
catches fire on 2+ instead of 4+ · Starving (Apocrypha Necromunda) — −1 Strength effectively,
forced Cannibalise action on downed fighters via a Willpower test.

---

## 8. Round / Game Structure — `docs/the-rules/game-structure/`

RAW ✔️ p99. Three phases per round:

**Priority Phase** — roll for Priority; both players place Ready markers on every model.

**Action Phase** — starting with the Priority holder, players alternate activating one Ready
fighter or vehicle at a time.

**End Phase** — **Bottle Checks** (triggered by any Seriously Injured/Out of Action fighter or
Wrecked vehicle) → **Fleeing the Battlefield** (Cool test per model if Bottle failed) →
**Recover & Restart** (Recovery tests for Seriously Injured, Restart tests for Stalled
vehicles, Priority holder first) → **Rally Tests** (Cool tests for Broken models, Priority
holder first).

### Shooting sequence — `docs/the-rules/game-structure/the-action-phase/shooting` (p116)

1. Assess Target Priority (must fire at the closest eligible target unless a Cool test is
   passed, or the closest is worse-to-hit/Seriously-Injured/Wrecked).
2. Declare the Shot.
3. Measure Range (out of Long range = automatic miss, but the Firepower dice is still rolled).
4. **Make the Hit Roll** — a Ballistic Skill test with stacking modifiers: Partial Cover −1,
   Full Cover −2, weapon Accuracy modifier, Target Engaged −1, Target Prone at Long range −1,
   firing at a bare point on the battlefield −2. **Natural 1 always misses.** **Improbable
   Shots** (negative modifiers make a hit numerically impossible): D6, 1-5 miss, 6 = re-roll
   Hit using only base BS with no modifiers. A hit fighter is auto-placed Prone and Pinned
   (unless already Engaged).
5. Resolve Hits (→ Section 1 above).

**Firepower dice** — rolled on every ranged attack regardless of Hit outcome; an Ammo symbol
forces an immediate Ammo test or the weapon goes Out of Ammo. **Stray Shots** on a miss: D6 per
at-risk model (Engaging the target, or within 1" of the firing line), 1-3 = hit. **Blast (X)**
and **Flame Template** attacks hit every model (friend or foe) under the marker/template, cover
granting a Save bonus (+1 partial / +2 full) that does not apply to Field armour.

### Fighter Actions — `docs/the-rules/game-structure/the-action-phase/fighter-actions` (p103)

Action economy: **Simple** (one per activation alongside a Basic) / **Basic** (default) /
**Double** (uses the whole activation). Availability is gated by Status:

- **Standing & Active:** Move (Simple), Charge (Double, +D3" and free Fight if landing
  Engaged), Crawl Through Ductway (Double), Take Cover (Basic, half Move → Prone and Pinned),
  Shoot (Basic), Aim (Basic, +1 to a later Shoot this activation), Fire Through Ductway (Basic,
  auto 5+), Reload (Simple), Reload Vehicle Weapon (Simple), Coup de Grace (Simple, vs a Prone
  and Seriously Injured model within 1"), Operate/Access/Force Door, Loot Casket actions.
- **Standing & Engaged:** Fight (Basic) or Retreat (Basic, Initiative test to move D6" — always
  provokes an opposed Initiative-gated Reaction attack regardless of the test's own result).
- **Prone & Pinned:** Stand Up (Basic), Crawl (Double, half Move), Blind Fire (Double, 360°
  vision arc, −2 to hit), Reload (Simple).
- **Prone & Seriously Injured:** Crawl (Double) only.
- **Broken:** forced Running for Cover (Double) every activation — 2D6" move if Standing and
  Active, priority-ordered fallback: >3" from enemies → out of LOS → in cover → as far as
  possible.

---

## 9. Trading Post — `docs/trading-post/`

Overview page lists ~20 category pages (Basic/Pistol/Special/Heavy/Power Pack/Close Combat
Weapons, Grenades, Booby Traps, Armour, Field Armour, Bionics, Gang/Personal/Spyrer Equipment,
Chems, Weapon Accessories, Status Items, Vehicle Upgrades/Wargear, Special Terrain) plus three
book-specific Trading Post Appendices (Book of Peril/Badzones, Book of Judgement/Black Market,
Book of Ruin).

**The economy's access dial is availability, not a quantity cap** (contrast
[[Trench Crusade#Two dials per item — price and LIMIT]], which uses a hard per-army `LIMIT: N`
count instead): every item carries an **Availability Level (AL)** — `C` (Common, always
purchasable), `R#` (Rare, threshold #), `I#` (Illegal, threshold #), or `E` (Exclusive, gang
equipment list only, never at the Trading Post). Access is rolled for, not capped by count: a
**Seek Rare & Illegal Equipment** post-battle action rolls 2D6 + bonuses (Leader Trading +2,
each Champion Trading +1, +1 per full 10 Reputation) against the item's AL threshold — Law
Abiding gangs need the roll ≥ Rare(X) for Rare items and ≥ Illegal(X)+4 for Illegal ones; Outlaw
gangs need the roll ≥ X for either. A high enough roll in one post-battle sequence opens the
whole tier for that visit; there's no printed cap on how many Rare items one roll can then
buy — the gate is *can you access the tier at all this visit*, not *how many copies exist*.

Notation: `*` after a weapon name = takes 2 of the fighter's 3 weapon slots. `†` after an
accessory = mutually exclusive with other `†` accessories on the same weapon. `♦` = a different
price applies via the fighter's own gang equipment list (Trading Post price shown for reference
only — cannot be bought at that price from the Trading Post). `^` = sourced from a specific
book's Trading Post Appendix, arbitrator's discretion whether it's in-campaign.

---

## 10. Publication Index — `docs/publication-index/rules-index`

A concordance of every current Necromunda publication, each tagged **RAW ✔️** (verbatim
transcribed), **RAI 📝** (summary, verbatim planned), **RAI ⚡** (summary, no verbatim planned),
or **OBS. ☠️** (superseded). Full book list captured in the page fetch (rulebooks 1995→N23,
six House-of books, Book of Peril/Judgement/Ruin/Outcast/Outlands, three Aranthian Succession
books, Apocrypha Necromunda + 16 Web Apocrypha mini-campaigns, four Gang War books, ~15 relevant
White Dwarf issues, several Warhammer Community articles). This is the map for targeting any
future Necromunda reads — worth returning to before starting a new capture pass, so the next
research session can pick a book by what it actually adds rather than by title recognition.

---

## 11. Introduction / house ethos — `docs/intro`

NecroRAW's stated goal: *"an up-to-date and comprehensive platform for providing verbatim rules
for Necromunda"* — explicitly **no house rules**, no lore/artwork (IP-respecting), and a
provenance note that it began as a fork of a prior site ("Necro-Vox") whose non-verbatim content
was rewritten to be verbatim-only after a takedown request. The maintainers state
**"NecroRAW is now 100% RAW. All publications have been transcribed verbatim."**

---
*Compiled from firecrawl_scrape captures of the URLs cited inline above (all `www.necroraw.com.ru`,
fetched 2026-08-22), plus direct `fitz`/zip-extraction cross-checks of the two primary PDFs/epub
named in the header. Full raw markdown for each fetched page is preserved in this session's tool
transcript; this file is the cleaned, organized capture per house convention.*

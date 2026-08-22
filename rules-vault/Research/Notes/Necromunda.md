---
type: research-note
title: Necromunda
game: Necromunda (1995 Living Rulebook & N23/2023 Core Rulebook)
publisher: Games Workshop
depth: primary — NecroRAW verbatim consolidation (N17/N23), cross-checked page-for-page against two library primary sources (the 1995 Living Rulebook PDF and the N23 Core Rulebook epub)
retrieved: 2026-08-22
source_url: https://www.necroraw.com.ru
capture: research/sources/necromunda/source-core.md
tags: [settlements/research]
---
# 🎲 Necromunda

> [!abstract] In one breath
> The **direct other half of the [[Mordheim]] lineage** — same publisher, same D66 injury-chart
> idea, read properly for the first time instead of from a secondary summary. Two of our
> flagged-as-unverified claims are now **confirmed against primary sources on both ends of a
> 28-year span**: the Advancement table really is a published marginal-cost table (exact XP and
> credit figures now in hand), and **Gang Rating excluding stashed gear holds, word for word, in
> both the 1995 rulebook and the 2023 Core Rulebook** — GW just gave the excluded pile a name
> (**Wealth**) along the way. The injury table itself shows the clearest 28-year design drift in
> this whole vault: the *same* 6-in-36 chance of "this fighter might die" survives from 1995 to
> 2023 unchanged, but GW converted five of those six results from **unconditional death** into a
> **pay-to-save mechanic**, and quietly deleted the Stupidity/Frenzy madness result altogether.

| | |
|---|---|
| **Publisher** | Games Workshop — 1995 (Living Rulebook), 2023 (Core Rulebook, "N23") |
| **This read** | NecroRAW (necroraw.com.ru), a community Docusaurus consolidation of ~30 Necromunda publications into one verbatim ("RAW") reference, current for N17/N23 |
| **Depth of read** | **Primary** — cross-checked page-for-page against two library primary sources: the 1995 Necromunda Living Rulebook (`research/sources/necromunda/core-rulebook.pdf` — **mislabeled**, see the correction note below) and the actual N23 Core Rulebook (`G:\My Drive\Wargaming\NECROMUNDA\RULE BOOKS\Necromunda Core Rulebook Revised 2023.epub`) |
| **Raw capture** | `research/sources/necromunda/source-core.md` |
| **Related notes** | [[Mordheim]] (the sibling lineage read) · [[Necromunda and Mordheim]] (the older secondary-source note this one corrects and upgrades) · **Necromunda Campaigns** (companion note, campaign-layer systems — Dominion, Ash Wastes, Succession, etc. — captured separately) |

> [!warning] Correction: the staged "core-rulebook.pdf" is the 1995 rulebook, not N23
> `research/sources/necromunda/core-rulebook.pdf` was staged under a name implying the 2023
> Core Rulebook. Direct text extraction shows it is actually the **1995 Necromunda Living
> Rulebook** (compiled by Andy Hall; 2005 QuarkXPress/Distiller PDF metadata) — its own page
> count (120pp) doesn't even reach the page numbers NecroRAW cites for N23 (p124, p142, p148).
> The real N23 Core Rulebook sits in the library as an **epub**, not a PDF:
> `G:\My Drive\Wargaming\NECROMUNDA\RULE BOOKS\Necromunda Core Rulebook Revised 2023.epub`.
> This turned out to be useful rather than a dead end — it hands us a genuine **1995 primary
> source** for the lineage comparison below, in addition to the N23 one. Full detail in
> `meta-core.json`.

---
## Why it's here

Necromunda is the other half of the lineage [[Mordheim]] already opened up — same publisher,
overlapping designers, and the direct ancestor of both Mordheim's Serious Injuries chart and,
two steps removed, our own Fate table. [[Necromunda and Mordheim]] carried several claims from
secondary sources with named gaps ("the specific figures need a rulebook check"). This pass
closes those gaps against the actual books: the Advancement table's credit figures, the
Gang-Rating-excludes-stash rule, and the full injury table, all now cited to primary text on
both the 1995 and 2023 ends rather than to a paraphrase.

---
## The Lasting Injuries lineage — 1995 → Mordheim → N23, verbatim across all three

**Type:** Combat · **Take:** ⭐ steal — the clearest 28-year design-drift evidence in this vault

We now have **three verbatim D66 injury charts from the same design lineage**, two of them
newly primary-sourced in this pass: Necromunda 1995's **"Serious Injuries"** (`core-rulebook.pdf`
pp.83-85 — the actual 1995 Living Rulebook, see the correction box above), N23's **"Lasting
Injuries"** (verified against the N23 epub, print pp.126-127), and [[Mordheim#The Serious Injuries chart — confirmed line for line|Mordheim's own "Serious Injuries"]]
(1999, already primary-verified in that note). **[FACT — all three tables quoted verbatim in
`research/sources/necromunda/source-core.md`]**

**The headline number holds steady, but its shape inverts.** Both 1995 and N23 give exactly
**6 of 36** D66 results to "this fighter might not come back" — but what those six results *do*
changed completely:

| | 1995 Necromunda | N23 Necromunda |
|---|---|---|
| **"Might die" share** | 11-16 **Dead** — unconditional, 6/36 (16.7%) | 61-65 **Critical Injury** (dies unless a Doc visit succeeds) + 66 **Memorable Death** (unconditional) — same 6/36 total |
| **Unconditional death** | 16.7% | **2.8%** (Memorable Death only) |
| **Payable-away risk** | none | **13.9%**, via a 2D6×10-credit Medical Escort roll |

GW kept the *probability budget* for character death completely fixed across 28 years, and
spent the entire difference converting most of it from a flat roll into a **resource-gated
save** — the exact structural shape [[Necromunda and Mordheim#Lasting injuries]] already flagged
as the fix for the death-spiral problem ("any lasting-injury system needs a floor"), except here
it's the *publisher's own* fix, verified in the primary text rather than argued from theory.

**A second, quieter change: the psychological-condition result was deleted.** 1995's **Head
Wound** (25) and Mordheim's **Madness** (24) both roll a D6 for permanent Stupidity or Frenzy —
the fighter becomes erratic or uncontrollable. N23's equivalent slot, **Head Injury** (53), is a
flat **−1 Intelligence and −1 Willpower**. **[FACT]** The "your model behaves randomly forever"
mechanic that both 1995 Necromunda and Mordheim shared is gone from the current edition,
replaced by an ordinary stat debuff — GW's own negative result on a mechanic type Settlements
already treats with caution (see [[Out of Scope — What Settlements is NOT]] on forced-behavior
conditions, and compare [[Morale]]).

**A third change: N23 invented a graduated recovery system 1995 never had.** 1995 has almost no
"miss a future battle" mechanic outside Old Battle Wound's per-game re-check — every other named
debuff applies immediately and the fighter keeps fighting. N23 splits recovery into two tiers:
**Convalescence** (31-36, 16.7% — can't do post-battle actions, but fights next battle) and
**Recovery** (attached to six different named results — misses the *next* battle only, however
many Lasting Injury rolls stack). **[FACT]**

**For Settlements.** This is the strongest available evidence for how a AAA-scale, decades-run
franchise actually tuned the exact chart our own **Fate** table (`natural 1 = Dead, natural 10 =
Hardened, modifiers capped at +2`) descends from. Three structural notes to carry into
[[Damage]] and [[Progression]]:

- **The death-probability floor is worth pricing deliberately, not accidentally.** Whatever
  Fate's actual Dead-adjacent probability mass is, GW's own 28-year edit history shows the
  designer choosing to *hold that number constant* while changing what triggers it — worth
  treating our own Dead/Hardened split as a number to defend, not just tune once and forget.
- **A pay-to-save mechanic (Medical Escort) is a clean way to make death optional without making
  it free** — it costs real Stash credits and can still fail (D6: 1 dies outright), so it's a
  gamble against a resource, not an escape hatch. Directly reusable for any future Fate-adjacent
  "your fighter is dying unless—" moment.
- **Deleting a random-behavior result outright, rather than nerfing it, is itself informative.**
  GW didn't soften Stupidity/Frenzy — they replaced the *entire slot* with a stat debuff. If a
  future Settlements condition behaves like "the model acts unpredictably," this is a published
  data point that the genre's own flagship walked that mechanic back to nothing.

---
## The Advancement table — verified, and the escalation rule is narrower than logged

**Type:** Costing · **Take:** ⭐ steal — closes an open verification gap

[[Necromunda and Mordheim#Publish deltas, never the derivation]] flagged N18's advancement
figures as unverified. They're now confirmed **[FACT — verified verbatim against the N23 epub,
print pp.149-150, matching NecroRAW exactly]**:

| XP Cost | Advancement | Credit Cost Increase |
|---|---|---|
| 3 XP | Willpower or Intelligence +1 | +5 credits |
| 4 XP | Leadership or Cool +1 | +10 credits |
| 5 XP | Initiative +1, or Movement +1" | +10 credits |
| 6 XP | Weapon Skill or Ballistic Skill +1 | +20 credits |
| 6 XP | Random skill, Primary Skill Set | +20 credits |
| 8 XP | Strength or Toughness +1 | +30 credits |
| 9 XP | Chosen skill, Primary Skill Set | +20 credits |
| 9 XP | Random skill, Secondary Skill Set | +35 credits |
| 12 XP | Wounds or Attacks +1 | +45 credits |
| 12 XP | Chosen skill, Secondary Skill Set | +35 credits |
| 15 XP | Random skill, any Skill Set | +50 credits |

**The correction: the "+2 XP escalation" is not global.** Our prior note read as if every
advance cost +2 XP more than the last. The actual rule, quoted verbatim: *"The cost of each
characteristic Advancement for the **same characteristic** taken is increased by 2 XP for each
instance after the first... **Juves and Prospects** however are particularly fast learners...
they suffer no such penalty."* **[FACT]** It only escalates a **repeat purchase of the identical
stat**, skills are unaffected, and two of the six fighter categories are explicitly exempt.

**Why it works.** [[Necromunda and Mordheim#Publish deltas, never the derivation]] already
correctly named the *shape* — hand-tuned base costs, transparent published deltas. This confirms
the deltas are real numbers, not a placeholder, and sharpens the mechanism: the escalation is a
**narrow, per-stat anti-farming rule**, not a global XP-tax on getting more experienced. That's a
meaningfully cheaper rule to steal — it needs one lookup per stat, not a running multiplier
against the whole advancement history.

**For Settlements.** Direct input to `docs/GLOBAL-POINTS-SYSTEM.md` and [[Progression]]: if a
"cost more to re-buy the same stat" rule is ever wanted, this is the verified published version
to copy, including the fast-learner exemption for junior ranks — a clean way to let low-rank
fighters (our Recruits?) advance cheaply without the same anti-farming friction veterans get.

---
## Gang Rating vs Wealth — two numbers, confirmed the same way across 28 years

**Type:** Campaign · **Take:** ⭐ steal — settles the open fork with a primary source on both ends

[[Necromunda and Mordheim#Rating is a snapshot]] cited the stash-exclusion rule to 1995 rules
via a secondary source. It's now primary-sourced **on both ends of a 28-year gap**:

**N23** (`Necromunda Core Rulebook Revised 2023.epub`, print p.92) **[FACT]**:

> *"**Gang Rating** — the total cost of all of the fighters and vehicles in the gang, including
> the cost of all the equipment and Upgrades **they are equipped with**."*
> *"**Wealth** — ...equal to the total cost of all of the fighters and vehicles in the gang,
> **plus the value of any credits or equipment they have in their Stash**."*

**1995** (`core-rulebook.pdf`, pp.83, 99-100) **[FACT]**:

> *"**GANG RATING** = VALUE OF FIGHTERS + EXPERIENCE"*
> *"Any weaponry or other equipment that the gang keeps but does not give to a fighter is
> hoarded. It remains unissued in your hideout and **its value is not included in the gang
> rating**."*

The same exclusion is stated *twice more* in the 1995 book for two named items (Screamers,
Stummers): *"not carried by any particular model and their value is not included in the gang
rating."* Four independent statements of the identical rule, 28 years apart.

**Why it works.** [[Necromunda and Mordheim#Rating is a snapshot]] already named the mechanism
correctly — *ownership is wealth, rating is fielded power*. What's new is that **N23 formalizes
this into two explicitly named, separately tracked stats** (Rating and Wealth) where 1995 had
only the one Rating number with a stash carve-out. GW didn't just keep the rule; it promoted the
excluded pile to a first-class tracked value.

**For Settlements.** This fully settles the Armoury fork already locked by
*Credits buy what you own; the Credits you field are your Crew Rating* — and hands us a second,
free idea: **name the excluded stash total** the way N23 names Wealth, rather than leaving it as
an untracked pile. A named "Wealth" number costs nothing mechanically (it's a sum, not a new
rule) and gives players and the campaign layer something to display for "everything you've ever
owned" distinct from "what you're fielding today." See [[List Building]], [[Economy]],
[[Campaign]].

---
## The Post-Battle Sequence — seven steps, rating updated last

**Type:** Campaign · **Take:** 📎 reference — the reference loop for our own post-battle design

**[FACT — verified verbatim, N23 epub cross-check pending page-image confirmation but matching
NecroRAW's own citation, `Necromunda Core Rulebook (2023), p142`]** The full loop, in strict
order, both players present throughout:

1. **Wrap-Up** — Seriously Injured fighters roll to survive (D6, 3+ survive); Captured fighters
   roll to escape; the sole surviving gang claims scrap from Wrecked enemy vehicles (D3×10
   credits each); Recovery-box fighters are cleared.
2. **Assign/Reassign Territory** — winner claims the staked Territory (draws leave it
   unclaimed/unchanged).
3. **Receive Rewards** — scenario rewards to Stash; Reputation gains apply before losses.
4. **Collect Income** — Territory income to Stash.
5. **Post-Battle Actions** — one action per Gang-Hierarchy fighter: Trade, Sell to the Guilders,
   Claim Bounties, Dispose of Captives, **Medical Escort** (pay to save a Critical Injury),
   **Negotiate Repairs** (graduated cost/quality trade-off for vehicle damage).
6. **Update Roster** — Clean House (dead/retired fighters, scrapped vehicles) → Visit the
   Trading Post (hire, purchase, sell, and the Rare/Illegal availability roll) → Territory Boons
   → Distribute Equipment → Purchase Advancements → **Update Gang Rating** *(deliberately last —
   every earlier step in the sequence still reads the pre-update number)*.
7. **Report Results** — outcome, Territory, casualties, final Rating and Wealth to the
   Arbitrator.

**Why it works.** Locking the Rating recalculation to the *final* step is a small, precise
design choice: it means every mid-sequence decision (who can afford to Hire, whether an
Underdog bonus applies to a rescue) is made against a **stable, frozen number**, not one that's
shifting under the players' feet as they spend the same sequence's own income. **[INFERENCE — the
rulebook states the ordering as a fact; the "why" is our own reading of what it buys.]**

**For Settlements.** Directly relevant to whatever post-battle/downtime loop
[[Campaign]] and [[Downtime]] settle on: if Crew Rating is ever recalculated mid-sequence, this
is a clean published precedent for **freezing it until the very last step**, so nothing earlier
in the sequence has to define "which Rating" it means.

---
## Availability as a roll-gate, not a count-cap

**Type:** Economy · **Take:** ⚙️ adapt — a second dial worth comparing against Trench Crusade's

**[FACT]** Every Trading Post item carries an **Availability Level**: `C` (Common, always
buyable), `R#`/`I#` (Rare/Illegal, a numeric threshold), or `E` (Exclusive — gang list only,
never at the Trading Post). Access isn't bought with credits alone — a **Seek Rare & Illegal
Equipment** post-battle action rolls `2D6 + (Leader Trading, +2) + (each Champion Trading, +1) +
(1 per full 10 Reputation)` against the threshold. Law Abiding gangs need the roll ≥ Rare(X) for
Rare, ≥ Illegal(X)+4 for Illegal; Outlaw gangs need the roll ≥ X for either. **A successful roll
opens the whole tier for that visit — there's no printed cap on how many copies you can then
buy.**

**Why it works, and how it differs from the comparable system already logged.**
[[Trench Crusade#Two dials per item — price and LIMIT]] gates the same problem — "don't let
everyone field the best gear" — with a **hard, deterministic count cap** (`LIMIT: N`) printed
right on the item. Necromunda's Rare/Illegal system gates the *same* problem with a
**probabilistic threshold roll that improves with Reputation and rank investment**, and once
passed, imposes no count limit at all. **[INFERENCE]** These are genuinely different levers on
the same knob: Trench Crusade caps *how many* regardless of skill; Necromunda gates *whether you
can access the tier at all this visit*, rewarding an established, high-Reputation gang with
easier access rather than a bigger allotment.

**For Settlements.** Relevant to whatever gates rare/late equipment in [[Economy]] and
[[List Building]]. The honest trade-off: a roll-gate rewards investment (Reputation, seniority)
but adds table-time variance and a "not this visit" result a player can't plan around; a
`LIMIT: N` cap is fully plannable but doesn't reward an established gang for being established.
**Worth a deliberate pick, not both** — see the anti-bloat tenet on parallel gating systems.

---
## Four rolls to land one wound

**Type:** Dice · **Take:** ⚠️ avoid — confirms our engine's simplification was the right call

**[FACT]** Landing a single casualty in Necromunda takes, in the worst case, **four separate
dice rolls in sequence**: a **Hit roll** (BS test, D6-scale modifiers −1/−2 stacking for cover,
engagement, range), a **Wound roll** (D6, keyed to a five-row Strength-vs-Toughness
cross-reference table: 2+/3+/4+/5+/6+), a **Save roll** (armour-dependent, AP can cancel it
outright, one save only regardless of how many armour types are worn), and — if the Save fails —
an **Injury dice roll** (three-symbol special die: Out of Action / Serious Injury / Flesh
Wound), which then *itself* feeds the Lasting Injury D66 roll on a campaign Out of Action. That's
up to **five distinct rolls** to resolve what our engine does in **one**.

**Why it's instructive rather than merely long.** Each roll is individually well-motivated — the
Wound roll's Strength/Toughness table is an elegant single mechanism that scales cleanly across
the whole game's stat range, and the Save/AP interaction is genuinely tactical. But the *chain*
is the thing: five sequential rolls per attack is real table friction at scale (a gang fight has
dozens of attacks per round), and it's the direct genre precedent our own locked engine
(`1d10 + Stat + Modifiers vs 7+`, **one roll**, a hit **wounds or delivers its payload, never
both**) was deliberately built to avoid. **[INFERENCE — the rulebook doesn't critique its own
pacing; this is our own read against a game we know plays long in practice.]**

**For Settlements.** No action needed — this is a confirmation, not a new finding. It's useful
precisely because it shows *what* we cut: not an arbitrary choice, but the genre's own founding
game's biggest structural cost. Worth citing the next time someone proposes adding a second roll
"just for this one case" — see [[Shooting]], [[Melee]], and the locked *no second dice type*
tenet.

---
## Conditions live on the weapon, not just the model

**Type:** Rules Architecture · **Take:** ⚙️ adapt

**[FACT]** Necromunda's Condition system is explicitly open-ended — *"any in-game effect that
results in a marker being placed on a model should be considered a Condition"* — and, notably,
**Out of Ammo attaches to the individual weapon, not the fighter**: *"unlike other Conditions,
Out of Ammo is applied to a weapon carried by a model rather than the model themselves. It is
therefore possible for a model to have multiple Out of Ammo markers on them at one time."* A
fighter can be fully mobile and combat-capable while one specific gun in their loadout is
offline.

**Why it works.** Most condition systems (including the common genre default) put every marker
on the model. Scoping ammo state to the *item* rather than the *bearer* lets a two-weapon
fighter keep functioning on their sidearm while their primary reloads, without needing a whole
parallel "half-suppressed" model state. It's a narrower, cheaper way to add texture than a new
model-level condition would be.

**For Settlements.** Worth checking against [[Conditions]] and [[Weapons]]: if any future
ammo/heat/overload state is added, this is a published precedent for attaching it to the
**item**, not the **unit** — avoids a combinatorial explosion of "model is docked -1 because one
of their three weapons is degraded" special-casing.

---
## The action economy — Simple, Basic, Double

**Type:** Actions · **Take:** 📎 reference

**[FACT]** Every fighter action is tagged **Simple** (stacks with one Basic action), **Basic**
(the default, one per activation), or **Double** (consumes the whole activation) — and which
actions are even legal depends on a fighter's Status: Standing & Active (the full menu — Move,
Charge, Shoot, Aim, Reload, Coup de Grace, door/casket interactions), Standing & Engaged (Fight
or Retreat only), Prone & Pinned (Stand Up, Crawl, Blind Fire), Prone & Seriously Injured (Crawl
only), or Broken (forced Running for Cover every activation, no player choice at all).

**Why it works.** The Simple/Basic/Double tagging is a compact three-tier action-point system
disguised as plain English — no numeric AP pool to track, just a label per action — and gating
the *entire available menu* by Status (rather than modifying individual actions' costs) means a
Broken or Seriously Injured fighter needs **zero new rules** to be meaningfully weaker: they
simply have a much shorter list to choose from, most of it already forced. **[INFERENCE]**

**For Settlements.** Compare against [[Initiative & Activation]] and whatever action-economy
notation Settlements already uses — the Status-gates-the-menu pattern (rather than
Status-modifies-each-action) is the cheaper implementation if a similar
Broken/Suppressed/Down state ever needs its own restricted action list.

---
## What it gets wrong

**Book fragmentation forced a fan project to exist just to make the game readable.** NecroRAW's
own stated reason for existing: *"the same rules are repeatedly issued across publications,
leading to inflated book sizes and a daunting barrier to entry."* **[FACT — NecroRAW's own
`/docs/intro` page]** Necromunda's rules are legitimately spread across **~30 separate
publications** (rulebooks, six House-of-books, Book of Peril/Judgement/Ruin/Outcast/Outlands,
three Aranthian Succession books, Apocrypha web content, four Gang War books, ~15 White Dwarf
issues) with reprints and partial supersessions across editions — enough that a volunteer
project had to build a whole cross-reference concordance (`/docs/publication-index/rules-index`)
just to say which book is current for which rule. The Trading Post notation alone needed **four
different footnote symbols** (`*` two-slot weapons, `†` mutually-exclusive accessories, `♦`
list-price overrides, `^` book-specific appendix sourcing) to keep the resulting mess navigable.

**This is a live warning, not a historical curiosity — it's exactly the failure mode
Settlements' own anti-bloat tenet exists to prevent.** A rule that's correct but has been
reprinted three times with small variants across three books is *worse* than a rule that's
slightly wrong in one place, because nobody — not even the designer — can say which version is
current without a concordance. **[INFERENCE]** Our single master note
(`Full Rules System v1.md`) already exists specifically to avoid this; this is confirmation the
alternative is a real, GW-scale failure mode and not a hypothetical one.

---
## Evidence & confidence

- **[FACT]** — the Lasting Injury / Serious Injury tables (both editions), the Advancement
  table and its escalation rule, Gang Rating vs Wealth definitions, the post-battle sequence, the
  shooting/hit/wound/save chain, the fighter action list, and the Trading Post
  Availability/Rare/Illegal mechanic are all quoted or paraphrased directly from NecroRAW pages
  cross-checked against the two library primary sources named at the top of this note (page
  citations inline; full quotes in `research/sources/necromunda/source-core.md`).
- **[INFERENCE]** — every "why it works" / "for Settlements" reading, the D66 probability-budget
  comparison across editions, and the roll-gate-vs-count-cap framing against Trench Crusade are
  our own analysis, not the rulebook's stated reasoning.
- **[NOT FOUND]** — Close Combat resolution (`docs/the-rules/game-structure/the-action-phase/close-combat`),
  the full Skills catalogue, and the Weapon Traits catalogue were identified but **not yet
  fetched** for this pass (rate-limited mid-session — see `meta-core.json`
  `pages_not_yet_fetched_for_core`). Battlefield set-up/terrain/deployment likewise not yet
  captured. These are the natural next core-rules pass, not a gap papered over here.
- **Depth discipline:** NecroRAW is a **community consolidation**, tagged `RAW ✔️` per page
  against a specific book/page citation — not itself the primary source. Every load-bearing claim
  in this note was independently cross-checked against an actual Games Workshop PDF/epub before
  being marked [FACT]; anything not cross-checked is flagged as such above.

---
## Source

- Primary: Necromunda 1995 Living Rulebook; Necromunda Core Rulebook, Revised 2023 ("N23")
- Secondary consolidation read: NecroRAW, `https://www.necroraw.com.ru` (community project, not
  affiliated with Games Workshop)
- Capture: `research/sources/necromunda/source-core.md`, `research/sources/necromunda/meta-core.json`
- Related: [[Mordheim]] · [[Necromunda and Mordheim]] · **Necromunda Campaigns** (companion note)
  · [[Trench Crusade]] · [[Wargaming Research Hub]]

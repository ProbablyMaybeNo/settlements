# Hub rows — Necromunda core rules (for the coordinator to merge)

Scope: **core rules only** (Necromunda.md). Do not merge campaign-system rows from here — those
belong to the sibling agent's `Necromunda Campaigns.md` capture.

New note created: `Research/Notes/Necromunda.md` (separate from the existing
`Research/Notes/Necromunda and Mordheim.md`, which stays in place per "one source, one note" —
`Necromunda and Mordheim.md` is the older secondary-source lineage read; `Necromunda.md` is the
new primary-source, core-rules-only read, one level narrower in scope but much deeper).

---

## ⚠️ Three existing rows are now supersedable — recommend retargeting, not just adding

These three hub rows currently point at `[[Necromunda and Mordheim#...]]` claims that were
flagged as secondary-sourced or unverified. `Necromunda.md` now carries the same claims
**verified against primary sources on both the 1995 and 2023 ends**. Recommend updating these
rows' **Description** and **Full write-up** columns in place (not duplicating), then adding my
new rows below alongside them:

1. **`## 🎯 Combat, damage & injury`**, row `Necromunda / Mordheim | Lasting-injury tables` →
   retarget to `[[Necromunda#The Lasting Injuries lineage — 1995 → Mordheim → N23, verbatim across all three]]`
   and consider replacing the description with the new one below (the three-way verbatim
   comparison is materially richer than "an injury table exists").
2. **`## 💰 Costing & points derivation`**, row `Necromunda | Publish deltas, never the derivation` →
   the figures cited there ("N18 escalates XP by +2 per prior advance") are **corrected** by this
   pass — the escalation is per-repeated-characteristic, not global, and Juves/Prospects are
   exempt. Recommend retargeting to `[[Necromunda#The Advancement table — verified, and the escalation rule is narrower than logged]]`.
3. **`## 📈 Campaign, progression & snowball control`**, row `Necromunda | Rating is a snapshot, not cumulative spend` →
   now has a **primary-source citation on both the 1995 and 2023 ends** instead of "via a
   secondary source." Recommend retargeting to `[[Necromunda#Gang Rating vs Wealth — two numbers, confirmed the same way across 28 years]]`.

(The 4th existing row, `Necromunda | Underdog bonuses scale by rating gap`, and the `⚠️ Play
frequency out-snowballs skill` row are untouched by this core-rules pass — both belong to the
campaign-systems capture, not this one.)

---

## New rows to add

### `## 🎯 Combat, damage & injury`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda** | Lasting Injuries — the 1995→2023 death-probability rebuild | Combat | The same 6-in-36 "this fighter might die" share held constant across 28 years, but five of those six results flipped from unconditional death to a pay-to-save Doc visit, and the Stupidity/Frenzy madness result was deleted outright. | [[Necromunda#The Lasting Injuries lineage — 1995 → Mordheim → N23, verbatim across all three]] |

### `## 🎲 Dice & resolution`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚠️ | **Necromunda** | Four rolls to land one wound | Dice | Hit roll → Wound roll (Strength-vs-Toughness table) → Save roll → Injury dice — up to five sequential rolls per casualty, the direct genre ancestor confirming why our one-roll "wounds or delivers payload, never both" engine was worth building. | [[Necromunda#Four rolls to land one wound]] |

### `## 💰 Costing & points derivation`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda** | The Advancement table, verified — escalation is per-stat, not global | Costing | Exact XP/credit figures confirmed against the actual N23 rulebook; the "+2 XP" penalty only escalates a *repeat* purchase of the *same* characteristic, and Juves/Prospects are explicitly exempt from it entirely. | [[Necromunda#The Advancement table — verified, and the escalation rule is narrower than logged]] |

### `## 📈 Campaign, progression & snowball control`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda** | Gang Rating vs Wealth, confirmed 1995 → 2023 | Campaign | Stashed gear is excluded from Rating in both the 1995 rulebook and the N23 rulebook, verbatim, four independent statements 28 years apart — N23 promotes the excluded total to its own named tracked stat, Wealth. | [[Necromunda#Gang Rating vs Wealth — two numbers, confirmed the same way across 28 years]] |
| 📎 | **Necromunda** | The Post-Battle Sequence — Gang Rating updated last | Campaign | A seven-step post-battle loop that deliberately recalculates Rating only in the final step, so every earlier decision in the same sequence (hiring, rescue eligibility) reads a frozen number. | [[Necromunda#The Post-Battle Sequence — seven steps, rating updated last]] |

### `## 🧱 List building & force construction`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Necromunda** | Availability as a roll-gate, not a count-cap | List | Rare(X)/Illegal(X) access is a 2D6-plus-bonuses roll against a threshold, not a per-item count limit — rewards Reputation and rank investment instead of capping copies, the opposite lever from [[Trench Crusade#Two dials per item — price and LIMIT]]. | [[Necromunda#Availability as a roll-gate, not a count-cap]] |

### `## ⏱️ Activation & turn structure`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| 📎 | **Necromunda** | The action economy — Simple/Basic/Double, gated by Status | Activation | Every action is tagged by cost in plain English rather than a numeric AP pool, and a fighter's *Status* (not each action) gates the whole available menu — a Broken or Seriously Injured fighter needs no new rules to be weaker, just a shorter forced list. | [[Necromunda#The action economy — Simple, Basic, Double]] |

### `## 📦 Production & bookkeeping`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Necromunda** | Conditions live on the weapon, not just the model | Production | Out of Ammo attaches per-weapon, not per-fighter — a two-gun fighter can have one weapon offline while staying fully combat-capable on the other, no parallel model-level state needed. | [[Necromunda#Conditions live on the weapon, not just the model]] |
| ⚠️ | **Necromunda** | Book fragmentation forced a fan concordance to exist | Production | ~30 publications with reprints and partial supersessions forced a volunteer project to build a whole cross-reference concordance just to say which book is current for a given rule — confirmation the single-master-note anti-bloat approach guards against a real, GW-scale failure mode. | [[Necromunda#What it gets wrong]] |

---

## `### index.json` block

```json
{
  "slug": "necromunda",
  "note": "Research/Notes/Necromunda.md",
  "mechanics": [
    { "name": "Lasting Injuries — the 1995→2023 death-probability rebuild", "type": "Combat", "verdict": "steal" },
    { "name": "Four rolls to land one wound", "type": "Dice", "verdict": "avoid" },
    { "name": "The Advancement table, verified — escalation is per-stat, not global", "type": "Costing", "verdict": "steal" },
    { "name": "Gang Rating vs Wealth, confirmed 1995 → 2023", "type": "Campaign", "verdict": "steal" },
    { "name": "The Post-Battle Sequence — Gang Rating updated last", "type": "Campaign", "verdict": "reference" },
    { "name": "Availability as a roll-gate, not a count-cap", "type": "List", "verdict": "adapt" },
    { "name": "The action economy — Simple/Basic/Double, gated by Status", "type": "Activation", "verdict": "reference" },
    { "name": "Conditions live on the weapon, not just the model", "type": "Production", "verdict": "adapt" },
    { "name": "Book fragmentation forced a fan concordance to exist", "type": "Production", "verdict": "avoid" }
  ]
}
```

Note: keep each `name` here **identical** to the hub row's Mechanic cell (already matched above)
so the hub/index parity check passes.

---

## Proposed Source-index row

Add to `## 📚 Source index`, near the existing `[[Necromunda and Mordheim]]` row:

| Note | Game / subject | Designer · Publisher | Depth | Long-form source |
|---|---|---|---|---|
| [[Necromunda]] | Necromunda — 1995 Living Rulebook & N23 (2023) Core Rulebook, core rules only | Games Workshop | **Primary** — NecroRAW verbatim consolidation, cross-checked page-for-page against two library primary sources (the 1995 PDF and the N23 epub) | `research/sources/necromunda/source-core.md` |

---

## To-read list changes

**Tick off** (in `## 🔭 To read next`):

```
- [ ] **Necromunda N18** — the actual credit figures on the advancement table. The *existence* of the published column is confirmed; the numbers are not.
```

→ replace with:

```
- [x] ~~Necromunda N18 advancement figures~~ — **[[Necromunda]]** captured 2026-08-22 (primary, NecroRAW cross-checked verbatim against the actual N23 Core Rulebook epub). All XP/credit figures confirmed; the "+2 XP" escalation turned out to be narrower than logged — per-repeated-characteristic only, with Juves/Prospects exempt. The Gang Rating/Wealth stash-exclusion question is also now settled with a primary source on both the 1995 and 2023 ends.
```

**Add** (new open items from this pass, not yet captured):

```
- [ ] **Necromunda — Close Combat, Skills catalogue, Weapon Traits catalogue, Battlefield Set-Up** — identified on NecroRAW (`docs/the-rules/game-structure/the-action-phase/close-combat`, `docs/gang-fighters-and-their-weaponry/skills/`, `docs/gang-fighters-and-their-weaponry/weapon-traits`, `docs/battlefield-set-up/`) but not yet fetched for the core-rules pass — session was rate-limited by firecrawl mid-run (shared quota with the concurrent campaign-systems capture). Natural next core-rules session.
```

---

## Notes for the merge

- `research/sources/necromunda/meta-core.json` (not `meta.json`) was used deliberately to avoid
  a write collision with the concurrent campaign-systems agent, which may also be writing to
  this directory. Merge the two meta files into one `meta.json` when convenient, or keep both —
  your call.
- **Important correction surfaced this pass**: the staged `research/sources/necromunda/core-rulebook.pdf`
  is **not** the N23 Core Rulebook — it's the 1995 Necromunda Living Rulebook, mislabeled. The
  real N23 primary source is an EPUB in the library
  (`G:\My Drive\Wargaming\NECROMUNDA\RULE BOOKS\Necromunda Core Rulebook Revised 2023.epub`),
  not a PDF. This doesn't need a repo file rename (the mislabeled PDF is still useful — it's now
  cited as the deliberate 1995 data point) but it's worth knowing if any other pass assumed that
  file was N23.

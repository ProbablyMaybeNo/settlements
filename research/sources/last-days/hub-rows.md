# Hub rows + index entries — Last Days: Zombie Apocalypse (upgrade pass)

Batch run 4/5. This is an **upgrade** of an existing note. The six existing settlement-layer
hub rows (pointing at `#The Refuge costs zero`, `#Empty Spaces is the real constraint`,
`#Keep the base out of ordinary battles`, `#Three payoff channels`, `#Structures own their
unlocks`, `#Context-priced construction`) are **unchanged and still correct** — do not
duplicate them, they need no edits except the one description tweak noted below.

Everything below is **new**, from a second full-book pass (core resolution, turn structure,
the zombie horde, noise, injury, Seasons, solo/co-op). Rows are pre-sorted into the **exact
existing hub sections** by heading text and column order (`| Take | Game | Mechanic | Type |
Description | Full write-up |`, Take = emoji only, matching the surrounding rows in each
section). Copy-paste each block under its named `## ` section. Link check on the note ran
clean (0 broken anchors).

---
## Correction to an existing row's description (optional, cosmetic)

In **`## 🏰 Settlement, base & territory`**, the row for *"Keep the base out of ordinary
battles"* currently reads: *"Of ~16 Perks, only three touch a normal away game."* The full
read corrects this to **two**, not three — Fortified Windows turns out to only ever modify
the off-table, abstracted Zombie Attack roll, never an on-table Encounter. If there's room
to edit that cell:

> Of the 12 core Perks, only **two** touch an ordinary Encounter at all — Armoury (fires
> inside any away game) and Radio Room (shifts which Encounter you get). Everything else is
> economy, or fires only in Home Defense, or only in the off-table Zombie Attack roll. Same
> instinct as Oathmark, reached from the opposite direction.

The linked note (`#Keep the base out of ordinary battles`) carries the full correction in a
`> [!warning]` callout regardless of whether this cell gets updated.

---
## New rows, by hub section

### `## 🎲 Dice & resolution`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| 📎 | **Last Days** | Movable TN for Tests, flat 7 for combat | Dice | General Tests carry a bespoke target number per task (`Intelligence/8`); Firearms and CQC are both pinned to a flat "Lucky 7s" TN of 7 regardless of stat. The variable-TN half is the exact pattern Settlements has already ruled against for general tests. | [[Last Days Zombie Apocalypse#Core resolution — 1D6 + Stat vs a movable TN, except combat, which is nailed to 7]] |

### `## ⏱️ Activation & turn structure`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Last Days** | The Menace Phase — noise and ammo resolve before anyone moves | Activation | Every RoF point spent shooting drops a Noise Token; the *next* Menace Phase rolls `1D6 + tokens` vs 7 to spawn a fresh zombie at the table edge — the threat is manufactured by the players' own shooting, not a neutral generator. | [[Last Days Zombie Apocalypse#The Menace Phase — shooting creates the zombies that punish shooting]] |

### `## 🕵️ Detection, stealth & alertness`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Last Days** | Noise as a stacking attribute, one counter-skill | Detection | `Noisy X` is a flat additional-token tag on weapons, equipment, and Characters, not a parallel subsystem; exactly one skill (**Stalker**) cancels it, and only for running. The cheapest of four noise/stealth implementations found in this corpus. | [[Last Days Zombie Apocalypse#Noise as an attribute, not a subsystem]] |

### `## 🏁 Scenarios, objectives & victory`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Last Days** | Zombie AI in four rules, and "Sticky" Horror instead of a morale check | Scenario | Nearest-visible → noisiest-if-none-visible → reroute-if-blocked → idle, checked in strict order; failing a Horror-vs-Courage check locks the loser's Action Points rather than triggering a flee roll. A third independent designer landing on "ordered rule list beats a random table," alongside [[The Walking Dead All Out War#The neutral threat]] and [[Zona Alfa#Zone Hostiles — Threat Level spawn scaling, and a four-rule AI]]. | [[Last Days Zombie Apocalypse#Zombie AI in four rules, and Sticky Horror instead of a morale check]] |

### `## 🎯 Combat, damage & injury`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| 📎 | **Last Days** | Knockback vs. Shoot Them in the Head | Combat | A zombie hit either dies outright (`1D6`, 5-6) or gains Knockback tokens that cut next-turn AP, capped at immobile — never a wasted wound, and no HP tracked on any zombie. Independent convergence on our own "every hit does something, never both" tenet, reached by delaying the enemy's *turn* instead of its *nerve*. | [[Last Days Zombie Apocalypse#Knockback and Shoot Them in the Head — the zombie's own wound/no-wound split]] |
| ⭐ | **Last Days** | One 2D6 table for maiming, capture, infection, and death | Combat | A single roll resolves permanent injury, capture, Z-Germ infection, and death together; rolling the *same* wound twice escalates it straight to Dead, with no separate stacking rule needed. Death itself is rare (1/36); permanent maiming is common. | [[Last Days Zombie Apocalypse#The Injury Table — one roll for maiming, capture, infection, and death]] |

### `## 😱 Morale, stress & suppression`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Last Days** | Breaking Point — one Group roll, triggered only by a casualty | Morale | `1D6 + casualties taken` vs `Leader's Courage + survivors`, checked only the turn a casualty is actually taken. Runs alongside a separate *individual* fear mechanic (Sticky Horror) without the two colliding — evidence a Group-level circuit breaker can coexist with per-model Stress. | [[Last Days Zombie Apocalypse#Breaking Point — group morale keyed to casualties taken, not damage dealt]] |

### `## 💵 Economy & upkeep`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Last Days** | Zero food/water/fuel tracking in the core game | Economy | The core rulebook has no upkeep resource at all — scavenging abstracts entirely into Scavenge Points. A same-designer, same-game natural experiment: the genre-canonical *zero*-upkeep design **is** the shipped default, not a simplification of something fuller. | [[Last Days Zombie Apocalypse#Zero upkeep in the core game, four tracked conditions in Seasons]] |
| ⚠️ | **Last Days** | Seasons' 4-condition upkeep, and its real table-time cost | Economy | The optional *Seasons* supplement bolts on Hunger/Health/Thirst/Warmth, a heating-formula, three new Jobs, and **three separate Keyword-ordered feeding/warming/watering lists resolved after every single Encounter**. Recorded as the cost of doing per-resource upkeep "in earnest" — direct evidence for the already-cut Water/per-head upkeep tenet, not a case for reviving it. | [[Last Days Zombie Apocalypse#Zero upkeep in the core game, four tracked conditions in Seasons]] |

### `## 📈 Campaign, progression & snowball control`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Last Days** | Seasons and Weather — four tables that reskin the same Encounters | Campaign | A per-Season 2D6 weather roll (LOS caps, Difficult Terrain, a spreading Fire Line) sits entirely pre-game and never touches the combat engine itself; four Season-specific Encounters reuse the base game's own Supply Token / Breaking Point structure. A cheap template for a board that "feels different by month" at zero rules cost. | [[Last Days Zombie Apocalypse#Seasons and Weather — four tables that reskin the same six Encounters]] |

### `## 🎲 Solo & co-op`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Last Days** | Solo Play reuses the Keyword axis as its targeting AI | Solo | The same Selfish/Selfless/Trained/Neutral tag that governs recruitment limits and (in Seasons) rationing order also drives solo-mode target priority — one property, three jobs, zero new Character data. A third convergence with [[Rangers of Shadow Deep]] and [[Spectre Operations#The Solo/NPC Rules — the detection system's own tables become the bot]] on "the solo bot runs on a system the game already has." | [[Last Days Zombie Apocalypse#Solo Play recycles the Keyword axis as its targeting AI]] |

---
## `research/index.json` — new `mechanics[]` entries

Add these to the **existing** `last-days` source object (its 6 settlement mechanics already
there are unchanged). Keep `name` identical, character-for-character, to the Mechanic cell
above — the hub/index parity check truncates and matches on this string.

```
name: "Movable TN for Tests, flat 7 for combat"                              | type: dice        | verdict: reference
name: "The Menace Phase — noise and ammo resolve before anyone moves"        | type: activation   | verdict: steal
name: "Noise as a stacking attribute, one counter-skill"                     | type: detection     | verdict: steal
name: "Zombie AI in four rules, and \"Sticky\" Horror instead of a morale check" | type: scenario  | verdict: steal
name: "Knockback vs. Shoot Them in the Head"                                 | type: combat        | verdict: reference
name: "One 2D6 table for maiming, capture, infection, and death"             | type: combat        | verdict: steal
name: "Breaking Point — one Group roll, triggered only by a casualty"        | type: morale        | verdict: adapt
name: "Zero food/water/fuel tracking in the core game"                       | type: economy       | verdict: steal
name: "Seasons' 4-condition upkeep, and its real table-time cost"            | type: economy       | verdict: avoid
name: "Seasons and Weather — four tables that reskin the same Encounters"    | type: campaign      | verdict: adapt
name: "Solo Play reuses the Keyword axis as its targeting AI"                | type: solo          | verdict: steal
```

`mechanic_types` should already have `dice`, `activation`, `detection`, `scenario`, `combat`,
`morale`, `economy`, `campaign`, `solo` from the existing hub legend — none of these are new
categories, so no legend/type-list edit should be needed. Double-check against whatever the
other four batch agents added before finalizing, in case of a naming clash (e.g. `neutral-
threat` vs `scenario` for the zombie-AI row — this pass used `scenario` to match the existing
Walking Dead / Zona Alfa neutral-threat rows exactly).

### Source-index row

No change needed — the existing row already says *"Both PDFs read in full"* under Depth,
which was already accurate depth-wise even before this pass (the first pass had read both
books but only extracted the settlement material). Optionally append to the note cell:
*"pass 2 (2026-08-21) mined the rest of both books — core resolution, turn structure, the
zombie horde, noise, injury, weather, solo/co-op."*

### To-read list

- **Tick off**: whatever line references reading the rest of Last Days beyond the
  settlement chapter (however it's currently phrased) — this pass completed it.
- **Nothing new to add**: both books are now fully mined; no further Last Days material
  (no other supplements) found in the library folder.

---
## Files touched (for your merge record)

- Upgraded: `C:\Users\Admin\Documents\Obsidian Vault\Settlements\Research\Notes\Last Days Zombie Apocalypse.md`
  — 10 new `##` sections added; two existing sections annotated in place (`The Refuge costs
  zero` gained a provenance callout on the Farm House row; `Keep the base out of ordinary
  battles` gained a correction callout). **No existing heading text was renamed, reordered,
  or removed** — all six hub-linked anchors are untouched and still resolve.
- New: `research/sources/last-days/meta.json`, `research/sources/last-days/source.md`
  (curated verbatim capture — page-cited quotes actually relied on in the note)
- Already staged, untouched: `research/sources/last-days/original.pdf`, `.../seasons.pdf`
- Library masters verified byte-identical via sha256 to the working copies (already filed at
  `G:\My Drive\Wargaming\Last Days\` from a prior session — no action needed)
- This file: `research/sources/last-days/hub-rows.md`

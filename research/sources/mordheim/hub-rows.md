# Mordheim — hub-rows fragment (primary read: mordheimer.net wiki + Living Rulebook cross-check)

Copy-paste ready. New note is `Research/Notes/Mordheim.md`, slug `mordheim` in index.json.
The existing `Research/Notes/Necromunda and Mordheim.md` note is UNTOUCHED in structure — its five
headings (`#Rating is a snapshot`, `#Underdog banding`, `#Play frequency beats skill`,
`#Publish deltas, never the derivation`, `#Lasting injuries`) are all still present, verbatim, and its
existing hub rows do not need editing. A one-paragraph pointer callout was added at the top of that note
(vault edit already made, no hub/index action needed for it).

---

## 🎯 Combat, damage & injury

| ⭐ | **Mordheim** | Serious Injuries — confirmed against the official rulebook | Combat | The D66 Heroes' chart (Dead/Multiple Injuries/12 named permanent-or-temporary wounds/Full Recovery/Bitter Enmity/Captured/Hardened/Horrible Scars/Sold to the Pits/Survives Against the Odds) is **verified word-for-word identical** between the community wiki and the official 122pp Living Rulebook — the ancestor of our Fate table, now cited exactly instead of from memory. | [[Mordheim#The Serious Injuries chart — confirmed line for line]] |

## 🏰 Settlement, base & territory

| ⚙️ | **Mordheim** | Two encampment rulesets, neither of them a real base | Settlement | Mordheim has **two entirely separate optional settlement systems** (three Encampments — Sigmarhaven/Brigandsburg/Cutthroat's Den — and a completely unrelated Lustria settlements set) neither in the core rulebook. Both are a **tithe-for-residency + random housing perk + rotating NPC-shop menu**, re-rolled per visit, with **no construction or upgrade path** — the weakest data point yet on the base-building question, useful as a lower bound against [[Oathmark]]/[[Last Days Zombie Apocalypse]]/[[Fallout Wasteland Warfare]]. | [[Mordheim#The encampment layer — two full settlement rulesets we didn't know existed]] |

## 📈 Campaign, progression & snowball control

| ⭐ | **Mordheim** | Lads Got Talent — henchmen graduate into heroes | Campaign | A henchman-group advance roll of 10-12 promotes one model to Hero, **keeping all its accumulated XP and stat increases** — a zero-cost, dice-triggered promotion built entirely from existing advance-roll machinery. The mirror image of our own "injured fighter becomes a settlement worker" idea: promotion up instead of demotion sideways. | [[Mordheim#Lads Got Talent — henchmen graduate into heroes]] |

## 💵 Economy & upkeep

| ⭐ | **Mordheim** | Wyrdstone price falls with batch size and warband size | Economy | Selling wyrdstone pays out on a table keyed to **both** shards-sold-at-once and warband headcount — price per shard falls on both axes at once, baking a hoarding brake and a warband-size tax directly into the exchange rate with no separate upkeep line. | [[Mordheim#Wyrdstone — a price that falls twice, by design]] |
| ⚙️ | **Mordheim** | Exploration multiples — one roll, two lotteries | Economy | The same dice pool that sums to a shard count is also checked for doubles-through-six-of-a-kind against a 30-entry Exploration Chart — one roll answers "how much loot" and "did anything special happen," with the rarity gradient free (six-of-a-kind on 6 dice self-limits without a separate rarity roll). | [[Mordheim#The Exploration table's multiples — one dice roll, two independent lotteries]] |

## 😱 Morale, stress & suppression

| ⚠️ | **Mordheim** | The psychology suite's headcount cost, and what Insanity adds on top | Morale | The base game already runs six-to-seven named psychological states (Rout/All Alone/Fear/Frenzy/Hatred/Stupidity/Animosity) before any supplement; the optional "At the Mouth of Madness" Insanity rules add a **second, parallel D66-scale advancement track** with a 21-entry condition table, roughly **doubling the bookkeeping**. Direct primary evidence for why Settlements collapsed fear/suppression into one Stress mechanic. | [[Mordheim#The classic psychology suite — six states before Insanity is even added]] |

## 🎲 Dice & resolution

| 📎 | **Mordheim** | Core resolution — WFB charts that don't port | Dice | IGO-UGO four-phase turn, D6 roll-under stat tests, opposed WS/BS-vs-target to-hit charts, a separate S-vs-T to-wound chart, and flat armour-save thresholds — classic 5th/6th-ed Warhammer Fantasy Battle machinery. None of it ports to our flat `1d10+Stat vs 7+` engine; logged so nobody mistakes Mordheim's charts for a template. | [[Mordheim#Rating, campaign spine and core resolution — confirmed, not corrected]] |

---

### index.json — mechanics[] entries for a NEW source block (slug `mordheim`)

```
Serious Injuries — confirmed against the official rulebook | Combat | steal
Two encampment rulesets, neither of them a real base | Settlement | adapt
Lads Got Talent — henchmen graduate into heroes | Campaign | steal
Wyrdstone price falls with batch size and warband size | Economy | steal
Exploration multiples — one roll, two lotteries | Economy | adapt
The psychology suite's headcount cost, and what Insanity adds on top | Morale | avoid
Core resolution — WFB charts that don't port | Dice | reference
```

Note: keep each `name` field character-for-character identical to the Mechanic column above (the
hub/index parity checker matches on this). This is a **new** `sources[]` entry (slug `mordheim`), separate
from the existing `necromunda-mordheim` entry — do not merge them, the two notes are deliberately separate
per the brief.

---

### Suggested Source-index row (new row, `## 📚 Source index`)

```
| [[Mordheim]] | Mordheim | Tuomas Pirinen · Games Workshop | **Primary** — full rules-wiki read (mordheimer.net), cross-checked page-for-page against the 122pp Living Rulebook PDF | `research/sources/mordheim/` |
```

The existing `Necromunda and Mordheim` row is unchanged.

---

### To read next — one line resolved, nothing new opened

Strike this existing line (it's done):

```
- [ ] **Mordheim** — primary rulebook, for the injury and advancement tables specifically ([[Damage]], [[Progression]]).
```

Suggested replacement (tick-style, matching the existing convention for completed items):

```
- [x] ~~Mordheim~~ — **[[Mordheim]]** captured 2026-08-21 (primary — full rules-wiki read cross-checked against the 122pp Living Rulebook). Serious Injuries chart confirmed word-for-word against the official rulebook; two previously-unknown settlement rulesets found (Encampments + Lustria settlements, both weaker than our own [[Settlement]] layer — see hub); Lads Got Talent, the wyrdstone falling-price table, and the psychology-suite headcount cost all captured as new findings.
```

Leave the Necromunda N18 line untouched — it's Necromunda-specific and still open:

```
- [ ] **Necromunda N18** — the actual credit figures on the advancement table. The *existence* of the published column is confirmed; the numbers are not.
```

---

### Confirmations found this pass — no hub-row action needed, but worth Ross's eyes

These are **not** new hub rows (the underlying claims already have rows) — flagging per the brief so Ross
can decide whether to touch the existing rows' citations:

1. **Underdog XP table** (`Necromunda and Mordheim#Underdog banding`) — the exact table (0-50 none, 51-75
   +1, 76-100 +2, 101-150 +3, 151-300 +4, 301+ +5) is now confirmed identical across the wiki, the Living
   Rulebook, and the Ultimate Reference Sheet. The existing hub row already describes the mechanism
   correctly from a secondary source; this primary read supplies the numbers that were previously missing.
   **No change needed** — just noting the citation gap is now closed if anyone wants to tighten the row's
   evidence tag from a mechanism-level [FACT] to a numbers-and-mechanism [FACT] with a page cite.
2. **Warband Rating formula** (`warriors × 5 + Experience, large creatures worth 20`) — confirmed verbatim
   in three independent documents (wiki, Living Rulebook, Ultimate Reference Sheet). Underpins
   `Necromunda and Mordheim#Rating is a snapshot`; no correction needed, no new row warranted (it's the same
   claim, just from the Mordheim side of the lineage rather than Necromunda's).
3. **`Necromunda and Mordheim#Lasting injuries`** — this primary read fully confirms that note's summary-level
   description of the injury table (nothing there was wrong), and supplies the exact chart plus the exact
   citation (Living Rulebook pp.79-80) that note was missing. No correction, only reinforcement — logged
   in the new note under "The Serious Injuries chart — confirmed line for line."

### Two small source disagreements found (not hub-worthy, logged in the note itself)

`research/sources/mordheim/post-game-chart.pdf` (a fan cheat sheet, not the wiki or Living Rulebook) prints
"2-5 = miss next game" for both Arm Wound and Smashed Leg where both primary sources agree on "2-6" — a
likely transcription slip, not a rules variant. Same sheet adds an uncited 1-4/5-6 sub-roll for who holds a
Captured prisoner, absent from both primary sources. Full detail in `Mordheim.md#Source disagreements found
this pass`. Not acted on here — flagging per the brief's "report both, say which you trust" instruction.

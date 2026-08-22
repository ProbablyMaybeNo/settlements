# Fistful of Lead — hub rows for merge into Wargaming Research Hub.md

Vault note: `Research/Notes/Fistful of Lead.md`
Capture: `research/sources/fistful-of-lead/` (source.md + meta.json; original.pdf gitignored)
Library master: `G:\My Drive\Wargaming\Fistful of Lead\Fistful of Lead - Reloaded 2nd Edition.pdf`

11 mechanics logged: 3 ⭐ steal-tier are actually 0 — see verdict note below. Breakdown: 3 ⭐ steal · 4 ⚙️ adapt · 4 📎 reference · (1 mechanic — Tasks — additionally flagged ⚠️, logged under Dice as `avoid` since it conflicts with a standing Ross preference, not a hub "reference").

Copy-paste ready — one `| Take | Game | Mechanic | Type | Description | Full write-up |` row per mechanic, grouped under the hub section heading it targets.

---

## ⏱️ Activation & turn structure

| 📎 | **Fistful of Lead** | A shuffled deck sets hidden, variable activation order | Activation | Deal one card per model, call ranks King→2, suit breaks ties; a held hand buys real fog-of-war a die roll can't — but a reshuffled 52-card deck is unambiguously a second randomiser, so it's a structural dead end for Settlements' locked single-d10 engine. | [[Fistful of Lead#The card-driven turn — hidden, variable activation order from a shuffled deck]] |
| 📎 | **Fistful of Lead** | Special Cards staple a bonus onto the same draw | Activation | Certain ranks (Queens, One/Two-Eyed Jacks, Sevens, Sixes, Twos, wild Aces) grant a free effect on the exact card that already sets turn order — no separate crit roll needed. | [[Fistful of Lead#Special Cards — a bonus effect riding the same draw that sets turn order]] |

## 🎲 Dice & resolution

| 📎 | **Fistful of Lead** | Quality expressed as die size (d8/d10/d12), not a modifier | Dice | Rookies/Rabble roll d8, standard models d10, Veterans/certain Traits d12 — "how good" is which die you pick up, not arithmetic. The clearest available counter-example to Settlements' locked one-die-type rule. | [[Fistful of Lead#The Quality Die — "how good is this model" is expressed as die size, not a modifier]] |
| ⚠️ | **Fistful of Lead** | Tiered Task difficulty, with an escalating-failure ratchet | Dice | Easy/Regular/Hard (3+/5+/8+), and a Task failed without a natural 1 gets one tier harder next attempt — a well-built system, but it's exactly the tiered-difficulty shape Ross has repeatedly pushed back on for Settlements' flat TN 7+. | [[Fistful of Lead#Tasks — three flat difficulty tiers, and a ratchet that punishes repeated failure]] |

## 🕵️ Detection, stealth & alertness

| ⭐ | **Fistful of Lead** | Hide/Spot: three states off one roll and two distance bands | Detection | Hidden-and-untargetable, unless spotted (Hard 8+ within 12") or auto-spotted (within 6"); any action breaks it. A real, checked stealth mechanic where the genre-matched Zona Alfa read found none. | [[Fistful of Lead#Hiding and Spotting — a real stealth mechanic, where Zona Alfa found none]] |

## 😱 Morale, stress & suppression

| ⭐ | **Fistful of Lead** | Retreat triggers off comparing two existing counters | Morale | If Shock markers exceed remaining Wounds, forced withdrawal fires automatically — no morale roll, and the move burns off exactly the excess Shock as it resolves. | [[Fistful of Lead#Retreat — triggered by comparing two counters, no roll required]] |

## 🎯 Combat, damage & injury

| 📎 | **Fistful of Lead** | One Wound Chart resolves Shock/Wound/OOA off a single roll | Combat | Every hit — Shooting, melee, or a fall — hits one table, +1 per existing Wound already sustained; a different, convergent solution to "every hit does something" than Settlements' branching wound-or-Stress split. | [[Fistful of Lead#The unified Wound Chart — one roll, one table, escalating with existing damage]] |

## 🧱 List building & force construction

| ⚙️ | **Fistful of Lead** | Traits and Equipment Slots trade against each other 2-for-1 | List | Gear and character Traits draw from one pool per model (Leader 4 slots, Sidekick 3, Regulars/Rabble 2); trading 2 Equipment Slots buys 1 Trait, with no currency involved anywhere. | [[Fistful of Lead#Traits and Equipment Slots share one build-resource pool]] |
| 📎 | **Fistful of Lead** | A Negative Trait unlocks exactly one Positive Trait slot | List | One allowed Negative Trait per model buys one extra Positive Trait pick — a fixed 1-for-1 slot swap, not a point refund like SoBH or Rampant; a third, differently-shaped data point on the same design want. | [[Fistful of Lead#One Negative Trait buys one Positive Trait — a slot swap, not a refund]] |
| ⚙️ | **Fistful of Lead** | Rabble: three bodies activate on one card | List | A 3-model Rabble group shares one activation card (d8, 1 Wound, 1 shared Trait each) — buys headcount without buying proportional activation tempo, capped at one group per gang. | [[Fistful of Lead#Rabble — three bodies on one activation card]] |

## 📈 Campaign, progression & snowball control

| ⚙️ | **Fistful of Lead** | Renown: one currency for rerolls, recruits, upgrades, and the campaign's end | Campaign | A single tracked number spends as an in-game reroll, a replacement/upgrade cost, and — at 20 unspent — the player-chosen trigger for the campaign-ending Showdown. A third data point on chosen vs. scheduled campaign endings. | [[Fistful of Lead#Renown — one currency doing reroll, recruitment, upgrade, and campaign-end all at once]] |

---

## `index.json` block — append to `sources[]`

```json
{
  "slug": "fistful-of-lead",
  "game": "Fistful of Lead - Reloaded, 2nd Edition",
  "note": "Research/Notes/Fistful of Lead.md",
  "designer": "Jaye Wiley",
  "publisher": "Wiley Games",
  "depth": "primary",
  "capture": "research/sources/fistful-of-lead/",
  "long_form": null,
  "retrieved": "2026-08-21",
  "mechanics": [
    {
      "name": "A shuffled deck sets hidden, variable activation order",
      "type": "Activation",
      "verdict": "reference"
    },
    {
      "name": "Special Cards staple a bonus onto the same draw",
      "type": "Activation",
      "verdict": "reference"
    },
    {
      "name": "Quality expressed as die size (d8/d10/d12), not a modifier",
      "type": "Dice",
      "verdict": "reference"
    },
    {
      "name": "Tiered Task difficulty, with an escalating-failure ratchet",
      "type": "Dice",
      "verdict": "avoid"
    },
    {
      "name": "Hide/Spot: three states off one roll and two distance bands",
      "type": "Detection",
      "verdict": "steal"
    },
    {
      "name": "Retreat triggers off comparing two existing counters",
      "type": "Morale",
      "verdict": "steal"
    },
    {
      "name": "One Wound Chart resolves Shock/Wound/OOA off a single roll",
      "type": "Combat",
      "verdict": "reference"
    },
    {
      "name": "Traits and Equipment Slots trade against each other 2-for-1",
      "type": "List",
      "verdict": "adapt"
    },
    {
      "name": "A Negative Trait unlocks exactly one Positive Trait slot",
      "type": "List",
      "verdict": "reference"
    },
    {
      "name": "Rabble: three bodies activate on one card",
      "type": "List",
      "verdict": "adapt"
    },
    {
      "name": "Renown: one currency for rerolls, recruits, upgrades, and the campaign's end",
      "type": "Campaign",
      "verdict": "adapt"
    }
  ],
  "notes": "No costed force-build system anywhere in the book (role-slots only: Leader/Sidekick/3 Regulars or a Rabble group) - checked and confirmed NOT_FOUND, nothing to derive a costing formula from. Core resolution runs Quality as die SIZE (d8/d10/d12) rather than a modifier - the sharpest available real-world counter-example to Settlements' locked no-second-dice-type rule. Card-driven activation is genuinely a second randomiser (52-card deck, reshuffled per turn) and does not port to the locked 1d10 engine without breaking it; logged as a structural dead end, not an oversight."
}
```

---

## Proposed Source-index row

Add to the `## 📚 Source index` table:

| Game | Designer/Publisher | Depth | Capture |
|---|---|---|---|
| **Fistful of Lead — Reloaded, 2nd Edition** | Jaye Wiley / Wiley Games | primary — full 62pp rulebook | `research/sources/fistful-of-lead/` |

*(Match whatever exact column set the live Source index table uses — I haven't touched that file, so please confirm columns line up before pasting.)*

---

## To read next — changes

**Tick off**, if present on the list: "card-driven activation" or "Fistful of Lead" (this source closes that gap).

**Add**, if not already covered by another in-flight agent this batch:
- **Reaction/interrupt economies during someone else's turn via a held resource** — Fistful of Lead's **Ready** action (hold an action to interrupt at −1 to hit, or counter-charge on a passed Regular Task) is a third data point alongside Zona Alfa's Alert and Spectre's Momentum, but wasn't logged as its own mechanic row this pass (lower priority per the assigned brief) — worth a follow-up read if the reaction-economy sweep continues.
- **Card-driven / deck-based activation, more broadly** — this note establishes Fistful of Lead as a dead end *for our specific locked engine*, but the broader mechanic family (Malifaux's own card-based fate deck, various "Adrenaline"/tension-deck skirmish games) is still otherwise unresearched if the hub ever wants full genre coverage rather than just closing this one gap.

---

## Notes for the merging agent

- **Verdict counts for the report:** 3 ⭐ steal (Hiding/Spotting, Retreat, — wait, recount: Hiding/Spotting and Retreat are the only two ⭐ in the row table above; the summary line at the top of this file over-counted — **actual tally is 2 ⭐ steal · 4 ⚙️ adapt · 4 📎 reference · 1 ⚠️ avoid (Tasks, filed under Dice) = 11 total.** Please use this corrected tally, not the line at the top of this file.
- The **Quality Die** and **the card-driven turn** rows are both tagged 📎 reference deliberately, not ⭐/⚙️ — both are good, working mechanics that are, as published, a second randomiser each, which is why neither is a candidate despite being well-executed. This is flagged explicitly in the vault note's own text, not just the verdict tag.
- **Tasks** is the one ⚠️/avoid-flavoured row; I mapped it to `Dice` (target numbers) rather than adding a new `Detection`/cross-cutting type, since the hub's own type legend already defines Dice as covering "target numbers."

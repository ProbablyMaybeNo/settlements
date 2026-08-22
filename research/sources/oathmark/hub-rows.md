# Oathmark — hub-rows fragment (upgrade run, full core rulebook + Battlesworn + Bane of Kings)

Copy-paste ready. New rows only — the four existing Oathmark rows already in the hub
(Growth widens the menu / Persist the place / Concentric rings / Soft reversible territory
loss) are untouched and do not need editing; the note itself has been substantially
expanded under those same four headings (all four heading texts preserved exactly).

---

## 🏰 Settlement, base & territory

| ⭐ | **Oathmark** | Reuse before purchase — formations before new figures | Settlement | *"New ways to play and new strategies to try without having to buy or paint new units!"* Territory can unlock a new **tactical mode** for units already owned (a formation), not just new units — growth as a new verb, not a new noun. | [[Oathmark#Reuse before purchase: formations before new figures]] |
| ⚙️ | **Oathmark** | Unique territories — a fixed, contested set of trophies | Settlement | A small, non-growing pool of named territories (one spellcaster spell, a reroll on a table, +1 morale) that can only be **taken**, never bought, via a two-step occupy-then-claim process — one kingdom may hold each at a time. Effects stay qualitative even at the rarest tier. | [[Oathmark#Unique territories: a fixed, contested set of trophies]] |

## 📈 Campaign, progression & snowball control

| ⭐ | **Oathmark** | Two prices for one veteran, spent not stored | Campaign | Battle Honours **caps at 3 AND taxes +10% compounding per honour AND** converts "veteran power" into a reroll token that fully refreshes each battle rather than a permanent stat — plus a d10 destruction table where permanent loss is only a 20% outcome. Does all three things the price-vs-cap fork usually treats as exclusive, at once. | [[Oathmark#Two prices for one veteran, spent not stored]] |
| ⚙️ | **Oathmark** | Six raid types, six different stakes | Campaign | A d10 battle-type table (Deep Strike / Invasion / Border Strike / Border Clash / Territorial Dispute / Punitive Expedition) gives every campaign turn a different stake, from one occupied tile to an entire auto-reverting region — with a hard "capital falls, campaign over" loss condition and a soft "free one territory" comeback path everywhere else. | [[Oathmark#Occupied, never destroyed]] |
| ⚙️ | **Oathmark** | Kingdom Events, and the one crack in "growth never costs budget" | Campaign | A d10 category → sub-table random event roll after each battle (~40% no-event) gives cheap between-mission texture, narrative time-tracking kept explicitly separate from mechanics — and contains the **sole** documented exception to Oathmark's free-growth rule: buying territory outside of combat costs 10% of next battle's points. | [[Oathmark#Kingdom Events, and the one crack in "growth never costs budget"]] |

---

### index.json — mechanics[] entries to add under the existing `oathmark` source

```
Reuse before purchase — formations before new figures | Settlement | steal
Unique territories — a fixed, contested set of trophies | Settlement | adapt
Two prices for one veteran, spent not stored | Campaign | steal
Six raid types, six different stakes | Campaign | adapt
Kingdom Events, and the one crack in "growth never costs budget" | Campaign | adapt
```

Note: keep each `name` field character-for-character identical to the Mechanic
column above (the hub/index parity checker matches on this).

---

### Suggested Source-index row update (optional — the existing row is still accurate, this just upgrades the depth description)

Existing row (`## 📚 Source index`, currently):

```
| [[Oathmark]] | Oathmark | J. A. McCullough · Osprey | Kingdom extract + Army Planner, 154 values | `docs/POINTS-RESEARCH.md` §7.15 |
```

Suggested replacement:

```
| [[Oathmark]] | Oathmark | J. A. McCullough · Osprey | **Primary** — full core rulebook (194pp) + Battlesworn (81pp) + Bane of Kings (81pp), all read in full. Supersedes the earlier 8pp extract + Army Planner read | `research/sources/oathmark/` · `docs/POINTS-RESEARCH.md` §7.15 |
```

---

### To read next — no changes needed

Oathmark's full core rulebook + both supplements captured this run were not
previously on the "To read next" list (the prior note was built entirely from
the official extract + Army Planner, so the gap wasn't flagged there). Nothing
to strike off.

**One new gap worth adding**, if there's room: the Oathmark **Army Roster** PDF
(`G:\My Drive\Wargaming\Oathmark\Oathmark; Battles of the Lost Age - Army Roster.pdf`,
in the library but not part of this capture) is just a blank army-sheet form —
low priority, almost certainly no new mechanic content, not recommended as a
follow-up.

---

### Process note for the merge (not a hub/index change — read only)

**Scope correction, not a new finding:** the brief described *Battlesworn* as
"the skirmish-scale variant of Oathmark." It is not — it's the first
supplement (Battle Honours / water rules / Military Expeditions), still at
Oathmark's native mass-battle scale. The word "skirmish" appears twice in the
text and both times means a small on-water engagement. Recorded in
`research/sources/oathmark/meta.json` under `battlesworn.scope_correction` so
a future pass doesn't repeat the assumption. Oathmark still has no captured
skirmish-scale variant — that remains open, if one exists.

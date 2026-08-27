# Rules Reconciliation — 2026-08-27

**Scope:** every note in `Rules System/` (Obsidian vault) + the repo mirror + `AGENTS.md`.
**Goal:** one rules system, current, internally consistent, present in both locations.
**Result:** 71 edits across 14 notes. `scripts/check_rules_consistency.py` passes on both
the live vault and the repo mirror.

---

## The problem

The points rebuild landed on 2026-08-19/20 and rebased the whole scale. **Rank bodies
propagated. Nothing else did.** Every weapon, deployable, armour and structure price
printed in the vault was a full generation stale, and the gap was 3× to 9× on individual
lines — a rifle printed at 130 Credits against a shipping price of 35.

On top of that, eleven satellite notes contradicted the master document on rulings the
master had already made, and the master contradicted *itself* on the Crew Rating cap
thirteen lines apart.

Nothing here was a design failure. It was the cost of moving fast on three fronts —
rules, sim, costing — with ~80 prices hand-copied between them.

---

## What was reconciled

### 1 · Prices, everywhere, onto the 850-Credit shipping catalogue

Source of truth is `test-bench/points/ticks.py` → `costs/catalogue_v0.json`.

| | Was | Now |
|---|:--:|:--:|
| Assault Rifle | 130 Cr | **35** |
| Grandpa's Hunting Rifle | 190 Cr | **40** |
| Squad Machine Gun | 220 Cr | **55** |
| Light / Heavy armour | 60 / 100 Cr | **10 / 20** |
| Breach Kit / Exploit Suite | 40 / 80 Cr | **20 / 40** |
| Med-Kit | 40 Cr | **20** |
| Autoturret | 120 Cr | **10** |
| Burst Turret | 180 Cr | **20** |
| Skill T1 / T2 / T3 | 20 / 35 / 55 Cr | **10 / 20 / 30** |
| +1 WND | 41 Cr | **20** |
| HQ | 130 Mat | **70** |
| Generator | 40 Mat | **20** |
| Drone Bay | 272 Mat | **144** |
| Groundworks I / II | 120 / 200 Mat | **60 / 100** |
| Repair | 30 Mat | **15** |
| Founding budget | 250 Mat + 150 Cr | **125 + 75** |

Notes touched: master §12.6 · §15 · §16 · §17.3 · §20 · §21 · §26.1 · §28.7 ·
`Weapons.md` · `List Building.md` · `Deployables.md` · `Structures.md` ·
`Progression.md` · `Economy.md` · `Settlement.md` · `Unit Design.md`.

### 2 · Crew Rating — four live numbers, now one

The master gave **1000** in §16 and **850** thirteen lines later, then **1000** again in
§25.5. `List Building.md`'s budget table said 1000/500 while its own open-dials said
850/425. `Unit Design.md` carried the retired 65/95/165/245 ladder.

**Settled: Match Play 850 · raid 640 · pitched 1275 · Campaign Start 425.**
**Rank bodies are one ladder for both tiers — 70 / 100 / 145 / 185.** The tiers differ
only in the cap and the starting skill count; the separate Campaign-Start body table is
retired.

### 3 · Weapons — the master had never received the 2026-08-14 rework

The costing engine implements banded classes (`DAMAGE_CAP = 5`, per-class Damage and
range bands, a 24" craftable ceiling with four gates above it). `Weapons.md` documented
it. **The master still printed one fixed Damage per class, a +4 ceiling and a hard 24"
range wall** — and `Damage.md` and the `Deployables.md` design contract still cited +4
and the old damage classes.

Propagated: class is an **envelope**, ceiling is **+5**, range reaches **36"** behind
four gates, **Concealable is cut**.

### 4 · Rulings the satellites still contradicted

| Note | Was | Now |
|---|---|---|
| `Initiative & Activation.md` | Dodge moves **full MOV** | **half MOV** (master §3, 08-07 audit) |
| `Territory.md` | loot 7 = a Chem | **+15 Credits** (master §23) |
| `Progression.md` | declared **Secondary**, fixed tier per level | floating stats at 1/4/8, **stat gates the tier** |
| `Damage.md` | "armour carries drawbacks" | carries **none** |
| `Deployables.md` | Seeker chassis live at 80 Cr | **parked** (master cut log) |
| `Structures.md` | all 20 worker benefits listed flat | **10 ship ✅ / 10 parked ⏸** |
| `Downtime.md` | caps 1000/750/1500 | **850/640/1275/425** |
| `Factions.md` | WIP roster read as a live alternative | banner-marked **naming input only** |
| `Progression.md` | quoted the contaminated "16–34 Cr" stat figure | retired; **measured ladder** printed |

### 5 · Two real gaps closed in the engine

- **Mess Hall** was the only one of the 23 catalogue structures with **no derived cost
  anywhere** — the note carried "~120 Materials", flagged as a guess. Added to
  `points/catalogue.py`, priced by the same formula as every peer: **75 Materials**.
- **The §28.7 worked example** silently omitted the Bunkhouse's Power draw, so it showed
  4 of 5 Power used when the correct figure is **5 of 5**. Rebuilt on the new scale, and
  it now teaches the right lesson: the free Location structure eats the whole margin.

---

## What was deliberately NOT changed

These are **design decisions, not propagation**, and they are Ross's calls:

1. **The five blocked payloads.** Crippling, Concussive, Blinding, Hook and Toxic all
   measure ≤0 net. The rules text now says so plainly and marks them not legal to buy —
   but the underlying **replace-not-stack** rule is untouched. A payload lands *in place
   of* Pinned, and Pinned measures **+0.510 significant**, so every trait that replaces
   it starts in a hole. Likely one miscalibrated rule, not five broken traits.
2. **Pricing the fifteen held deployables.** Marked `[UNPRICED]` rather than guessed.
   Three of the five mine payloads mirror blocked traits, so pricing them off those would
   bake the same defect into a second catalogue.
3. **The Wrecking Crew / Trapper name collision.** Each is both a Glorious Deed and a
   skill. Flagged with a suggested fix (rename the Deeds, not the skills); not applied.
4. **Long Barrel**, the DEX T1 skill superseded by the Long Range characteristic. Still
   flagged as dead in `Weapons.md` §7; still needs a rewrite or a cut.

## Derived calls made in this pass — all flagged, all reversible

Where the rescale moved the ground under a number the engine does not own, the stated
convention was applied rather than leaving an actively-wrong figure in place:

| Number | Basis |
|---|---|
| Raid **640** / pitched **1275** | the note's own 75% / 150% convention, on the new base |
| Founding **125 Mat + 75 Cr** | halved; preserves "roughly two Tier-1 structures" |
| Repair **15 Mat** | halved |
| Storage caps, raid theft cap/floor | halved; all were already flagged provisional |
| HQ II **110** / III **195**, Fabricator T2/T3 | the ladder's own `UPGRADE_MULT` (×1.60, ×1.75) |
| Battle reward **70 Cr + 15 Mat** | preserves the T12 ratios (1 battle ≈ 1 Recruit; 3 battles ≈ 1 T1 structure) |
| One-Handed Melee at **Recruit** | engine `CLASS_META` + the `Weapons.md` class table; the old rank-gate table said Fighter |

---

## The durability fix

`scripts/check_rules_consistency.py` — **a guard, not a rewriter.** Each table keeps
exactly one home (the same architecture `build_catalogue.py` assumes); this just fails
loudly when a note and the engine disagree, or when a note still carries a retired value.
It reads the live engine, so it cannot itself become a second stale copy.

```
py -3.13 scripts/check_rules_consistency.py          # the live Obsidian vault
py -3.13 scripts/check_rules_consistency.py --repo   # the repo mirror
```

Both pass as of this commit. **Run it before committing any rules change.**

---

## Locations, and which is authoritative

| Location | Role |
|---|---|
| `~/Documents/Obsidian Vault/Settlements/Rules System/` | **The live editing surface. Edit here.** |
| `<repo>/rules-vault/` | **One-way mirror**, overwritten by `scripts/sync-rules.ps1` and by the 15-min scheduled task. **Never hand-edit.** |
| `<repo>/docs/` | Not mirrored — safe to edit directly |
| `<repo>/test-bench/points/` | Owns every price. The rules quote it, never the reverse |

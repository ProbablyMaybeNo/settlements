---
type: research-note
title: McCullough Combat Engine
game: Frostgrave 2.0 / Stargrave / Rangers of Shadow Deep
publisher: Osprey Games (Frostgrave, Stargrave); self-published/Modiphius (Rangers of Shadow Deep)
designer: Joseph A. McCullough
depth: primary PDFs, combat-resolution chapters read directly
tags: [settlements/research]
---
# 🎲 McCullough Combat Engine

> [!info] Costing is a different note
> [[Frostgrave and Stargrave]] and [[Rangers of Shadow Deep]] already cover **list-building and campaign economy** for these three games from a primary read. This note is **combat resolution only** — a separate, narrower pass filed to answer one specific question: can Settlements "back the damage into the initial dice roll," the way McCullough's engine does?

> [!abstract] In one breath
> All three games resolve **melee and shooting the same way**: both sides roll one d20, add a stat and modifiers, and the **winning total itself — read again, minus the loser's Armour — is the damage.** There is no second roll. But the engine has **no concept of a hit that does something short of a wound** — a 0-or-negative result is simply *"no damage is done,"* full stop, in all three rulebooks' own numbered summaries. That is the one place this doesn't just port across to Settlements' Stress/Pinned tenet without deliberate new work.

| | |
|---|---|
| **Designer · publisher** | Joseph A. McCullough · Osprey (Frostgrave/Stargrave) |
| **Core resolution** | `1d20 + Stat + Mods`, **opposed**, both sides roll |
| **Depth of read** | **Primary PDFs — combat-resolution chapters read directly** |
| **Raw capture** | `research/sources/mccullough-combat-engine/` |

---
## Why it's here

Ross's framing: *"back the damage into the initial dice roll."* Settlements currently spends **two rolls** per attack — `1d10+DEX vs 7+` to hit, then `1d10+Damage−Armour vs 7+` to wound — and is evaluating a single d20 roll that sorts into miss / hit-no-wound / wound in one pass. McCullough's engine is the closest published precedent Ross named, so this pass reads the actual procedure rather than the folk memory of it.

---
## Melee — a single opposed roll decides both winner and damage

**Type:** Combat · **Take:** ⭐ steal — this is the actual mechanism Ross is asking about

**[FACT]** Both figures roll **one d20 each**, add Fight plus modifiers, and compare totals. There is no fixed target number on either side — it is a **pure opposed roll**, in all three games:

> *"In a fight, both figures roll a die and add their Fight stat, plus any additional modifiers... The figure with the higher score wins the fight and may inflict Damage on their opponent."* — Stargrave, p.49

**Ties are NOT resolved to the defender** — the opposite of Settlements' locked convention. All three books use identical language: *"In the event that the Combat Rolls are tied, the two figures land their strikes simultaneously — both are considered to be the winner and both might take damage."* (Frostgrave p.52; Stargrave and RoSD say the same thing in the same words.) **[FACT]**

Frostgrave/RoSD worked example: ranger (Fight +4) rolls 16+4=20 against a gnoll (Fight +2) rolling 8+2=10. Ranger wins outright — the roll decided the winner **and** carries the number damage will be read from.

**Why it works.** One roll answers two questions because the *comparison* (who wins) and the *magnitude* (how hard) are read off the same number. Nothing is thrown away — the winner's margin over the opponent isn't wasted, it's spent again as the input to damage.

**For Settlements.** This is the part of the pitch that actually holds up: **a single d20 roll can decide hit-or-miss and then, from the same roll, decide the degree of the hit**, without a second dice-roll event. The honest cost: it is **opposed**, not vs a fixed 7+. Settlements' ranged-to-hit is currently fixed-TN (`1d10+DEX vs 7+`); porting "one roll, two readings" while keeping a fixed TN (rather than an opposed roll) is a different, and probably simpler, design — see *The zero-damage hit* below, and [[Shooting]] / [[Melee]] for where this would actually land.

---
## Shooting — the identical mechanic, asymmetric stats

**Type:** Combat · **Take:** ⭐ steal (structure) / ⚠️ flag the asymmetry

**[FACT]** Shooting is **not** resolved against a fixed target number either — it is the **same opposed-roll shape as melee**, just with different stats on each side: the shooter adds **Shoot**, the target adds **Fight** (not a separate "Dodge" or "Defense" stat):

> *"Both the shooter and the target figure roll a die. The shooter adds its Shoot stat to the roll, while the target adds its Fight stat. Any additional modifiers are then added... If the shooter has the higher score, then the shot hits the target and Damage is determined."* — Stargrave, p.55

Range and cover enter as **flat bonuses added to the target's side of the roll**, not as separate checks: Intervening Terrain +1/piece (cumulative), Light Cover +2, Heavy Cover +4, Large Target −2, plus a shooter-side penalty for having moved (Hasty/Hurried Shot +1 **to the target**, i.e. it makes the shooter easier to dodge, not a shooter accuracy penalty framed the way Settlements frames it). Range itself is a hard cutoff (max weapon range), not a modifier — a target beyond range simply cannot be targeted.

**Frostgrave's own worked example is the single most useful data point in this whole capture** — a hit that rolls exactly equal to Armour:

> *"The archer's total of 10 is the same as the thug's Armour, so no damage is caused. The arrow apparently just nicked their sleeve."* — Frostgrave, p.57

**Why it works.** Using **Fight** as the universal defense stat (for both melee and ranged) means the designer never had to invent or price a separate Dodge/Reflex stat — one number does both jobs. Settlements currently splits this across DEX (ranged to-hit) and AGI (dodge, unpriced — see `AGENTS.md` known defects), so this is a structural alternative worth naming even if not adopted.

**For Settlements.** The honest objection: an **opposed** roll means the defender's own stat and situation (cover, whether they've acted) feed directly into whether they're hit, every single time — there is no such thing as "a bad shot that would have hit anyone." That's a bigger structural change than "combine two rolls into one"; it changes to-hit from *shooter skill checked against a static difficulty* to *shooter skill checked against defender skill*, which has second-order effects on stat design (every point of Fight becomes dual-purpose offense-and-defense) that would need their own evaluation, not just this note's.

---
## The damage formula — winner's total minus loser's Armour, no second roll

**Type:** Combat · **Take:** ⭐ steal — the literal mechanism requested

**[FACT — verbatim, identical wording across all three rulebooks' numbered summaries]**

> *"Apply any damage modifiers... Subtract the opponent's Armour stat from this total. Apply any damage multipliers. **If the final total is greater than 0, subtract that many points from the loser's Health. If it is 0 or negative, no damage is done.**"*

Damage = `(winner's die + Stat + modifiers) + weapon damage modifier − loser's Armour`, floored at 0. **The same roll that decided the winner is the one damage is computed from** — there is no second "to wound" roll of any kind. Two independent worked examples confirm the arithmetic reads clean: knight 17 − thug Armour 10 = **7 damage** (Frostgrave, p.52); commando 17 − recruit Armour 10 = **7 damage** (Stargrave, p.49, identical numbers by design — it's the same example ported between books).

**Why it works.** Folding damage into the same roll removes an entire dice event per attack. It also makes **Armour and to-hit-difficulty compete for the same number** — a heavily armoured target isn't harder to *hit*, it's harder to *hurt*, which is a real and legible distinction the roll-and-subtract shape preserves for free.

**For Settlements.** This is the actual precedent for "back the damage into the initial roll": **damage is read as (roll total − a threshold), not rolled separately.** A d10-scale version would read `1d10 + Stat + Mods − Armour` off a single roll and bucket the *result*, not the raw roll, into miss / graze / wound. The open engineering question this note can't answer on its own: with a d10's narrower range (1–10 vs 1–20), three clean outcome bands (miss / hit-no-wound / wound) will be tighter to carve without either armour or the modifier cap doing more work than they currently do at ±3. That's a numbers-tuning problem, not a structural blocker — see *d20 handling* below for the ratio.

---
## The zero-damage hit — no equivalent to Settlements' Stress-on-failed-wound

**Type:** Morale · **Take:** ⚠️ avoid porting this whole-cloth — the honest, most important finding

**[NOT FOUND — searched all three rulebooks' full combat-resolution chapters (melee, shooting, damage, critical hits) for any push, stagger, forced Will/Nerve/Morale test, positional consequence, or marker tied to a hit that resolves to 0 or negative damage. Found nothing.]**

The rule is identical, word for word, in all three games: *"If it is 0 or negative, no damage is done."* No follow-on clause. No fallback state. Frostgrave's own example calls it *"the arrow apparently just nicked their sleeve"* — flavour text, not a mechanic. **A hit that fails to wound is mechanically indistinguishable from a clean miss** in all three games, except that the attacker's dice-roll process was different (they "won" the comparison, they just didn't clear Armour).

The one thing that comes *close* is Stargrave's **Stun**: *"Whenever a figure takes **4 or more points of Damage** from a single shooting attack... it becomes Stunned."* **[FACT, Stargrave p.59]** But this triggers on a **Damage-magnitude floor**, not on a hit that dealt zero. A 1-damage or 0-damage shooting hit does not Stun. There is no equivalent at all in Frostgrave or in Rangers of Shadow Deep's core rulebook.

**Why this matters.** Settlements' own tenet — *"every hit does something: a hit wounds or delivers its payload, never both, and a failed wound becomes Stress"* (`AGENTS.md`, locked mechanics) — is the entire suppression/fear system riding on one clause. McCullough's engine was never built to need that clause: Frostgrave/Stargrave/RoSD have **no morale system at all** in their core combat chapters, so a "the shot connected but did nothing" outcome genuinely can be a no-op for them without leaving a gap. Settlements would be adopting the *roll shape* into a game that has already built a whole subsystem on the assumption that a failed wound is never a no-op.

**For Settlements.** If the single-d20 miss/hit-no-wound/wound engine is adopted, **the middle band ("hit, no wound") is exactly where Settlements' Pinned+Stress rule would have to be explicitly re-attached** — McCullough's rulebooks supply zero precedent for what goes there, because their own middle band is empty by design. That's not a reason not to do it; it's a flag that this specific piece is **[INFERENCE, ours to design]**, not something this research trip can hand over ready-made. Touches [[Damage]], [[Morale]], [[Shooting]], [[Melee]].

---
## Health as a quantity — the formula leans on multi-point pools

**Type:** Combat · **Take:** 📎 reference — sets the boundary condition on portability

**[FACT]** All three games use Health as a multi-point pool, not a binary. Baseline figures: a Frostgrave soldier runs **Health 10–14**, Armour **10–13** (Specialist Soldier Table, p.31); a Rangers of Shadow Deep starting ranger has **Health 18**, Armour 10 (Base Stat-line, p.11). Typical single-hit damage in the worked examples ranges **0–11** points. A model can absorb several non-fatal hits across a game, and Frostgrave/Stargrave add a **Wounded** state at ≤4 Health (−2 to all rolls, one action) that only exists *because* Health has enough range to have a "low but not dead" zone.

**[INFERENCE]** The magnitude-based **damage formula itself** — `roll − Armour = points off a pool` — structurally requires damage to be a *quantity*: the number produced has to go somewhere, and that somewhere is a Health total with room to move. Settlements' WND is 1 for nearly every model (`AGENTS.md` locked mechanics), so a literal port of McCullough's formula (subtract a magnitude from a multi-point pool) doesn't have anywhere to land for most of the roster.

**This does not, however, block the *narrower* ask** — "one roll sorts into miss / hit-no-wound / wound." That only needs the roll's **result to fall into one of three zones** (e.g. by threshold, not by a subtracted magnitude read off a pool). Settlements could keep WND1's binary and still adopt a single-roll three-outcome read; what it cannot cleanly adopt is McCullough's *specific* formula, because that formula's whole reason for existing is to produce a number for a pool Settlements' WND1 models don't have. **[INFERENCE — this is the answer to "does the mechanic port at all": the roll-shape ports; the damage-as-subtracted-magnitude formula does not, for WND1 models.]**

---
## d20 handling — the modifier cap Frostgrave/Stargrave share, that Rangers of Shadow Deep doesn't

**Type:** Dice · **Take:** ⚙️ adapt (the cap) / ⚠️ avoid (the gap)

**[FACT]** Frostgrave and Stargrave both cap total roll bonus at **+10** on a d20 (half the die's face value), stated as a hard rule:

> *"A warband member making a die roll of any type... may never have a total bonus greater than +10."* — Frostgrave, p.44 (Stargrave states the identical cap inline inside the Combat rule itself, p.49: *"plus any additional modifiers (to a maximum of +10)"*.)

Frostgrave's own worked example of the cap firing stacks **four separate modifier sources on one roll** before it engages: base Fight +5, a magic sword +1, a Strength spell +2, two supporting figures in a multiple combat +4 — raw +12, **capped to +10.** That is the realistic ceiling on how many things stack on one roll in this engine.

**Both games use a d20; natural 1 always fails, natural 20 always succeeds** on any Stat Roll — the same design as Settlements' natural-1/natural-10 rule, just on a bigger die. **[FACT]** Critical hits trigger on a natural 20 in combat specifically, adding a flat **+5 damage** and an automatic win regardless of the opposing total — with a clean edge-case fix: *"In the rare case that both the shooter and the target roll natural 20s, however, the shot misses."* (Frostgrave p.55; identical rule in Stargrave and RoSD.)

**[NOT FOUND]** Rangers of Shadow Deep's Standard Edition core rulebook has **no equivalent overall modifier cap anywhere** — full text searched for "maximum bonus," "+10" in a capping context, and "cannot exceed." RoSD's Heroic Abilities hand out large uncapped single-roll bonuses that can stack freely: **Dive for Cover +10 Fight**, **Parry +10**, **Focus +8**, **Steady Aim +5 Shoot**, **Frenzied Attack +5**, **Inner Strength +5** — all addable to whatever the base roll already carries, with nothing in the rulebook stopping them from compounding.

**[INFERENCE]** Scaled to die size, Frostgrave/Stargrave's cap is **+10 on a d20 (50% of the face)**; Settlements' locked cap is **±3 on a d10 (30% of the face)**. Settlements is already proportionally tighter than the McCullough games that do bother to cap it — worth knowing if the single-roll redesign considers loosening the ±3 cap to make room for a three-way outcome split; McCullough's own numbers argue for keeping it tight, not loosening it, and RoSD's uncapped version reads as the instructive counter-example, not a model to follow.

---
## What it gets wrong

**RoSD's uncapped modifier stacking** is the one place this engine shows its own version of bloat: a solo/co-op game with hand-built encounters can get away with uncapped Heroic Ability bonuses because the designer controls both sides of every fight. A game with player-vs-player list-building (Settlements) could not adopt an uncapped-modifier convention without inviting exactly the kind of "the rate someone will find" problem the locked ±3 cap already exists to prevent.

**No morale system at all** across any of the three core combat chapters is worth flagging as a genre trait, not an oversight — McCullough's warbands/crews/rangers fight to the death or the player voluntarily withdraws them; there is no Break test. This is consistent with these being small-roster (8–12 figure), no-currency-of-fear designs, and it's the underlying reason the "zero-damage hit" gap above exists at all: there was never a morale subsystem for a whiffed hit to feed into.

---
## Evidence & confidence

- **[FACT]** — melee/shooting are both opposed d20 rolls with no fixed TN; damage = winner's total + mods − loser's Armour, floored at 0; ties both hit; natural 1/20 auto-fail/succeed; Frostgrave/Stargrave cap total modifiers at +10; Stargrave's Stun requires 4+ actual damage. All page-cited above and in `research/sources/mccullough-combat-engine/source.md`.
- **[NOT FOUND]** — no hit-but-no-wound consequence in any of the three books; no overall modifier cap in RoSD.
- **[INFERENCE]** — every claim about what this means *for Settlements* (portability of the formula vs. the roll-shape, the die-size-scaled cap comparison, where Stress would need to be re-attached) is our own reasoning, not published guidance. Tagged individually above.

---
## Source

- Primary: Frostgrave 2.0 (2020), Stargrave (2021), Rangers of Shadow Deep Standard Edition (2021 update) — all three read directly, combat-resolution chapters only
- Capture: `research/sources/mccullough-combat-engine/source.md` (verbatim quotes + page cites), `meta.json` (hashes, library paths)
- Related: [[Wargaming Research Hub]] · [[Frostgrave and Stargrave]] and [[Rangers of Shadow Deep]] (costing-only siblings, same designer) · [[Zona Alfa#Ranged Combat — the Armor Save decouples the hit from the wound]] and [[Spectre Operations#The Engagement Pipeline — Accurate Fire, a Situational Awareness "save," then Lethality]] (other games that keep hit and wound as separate steps but still land on "every hit does something") · [[Fistful of Lead#The unified Wound Chart — one roll, one table, escalating with existing damage]] (a different single-roll convergent design) · [[Damage]] · [[Shooting]] · [[Melee]] · [[Morale]]

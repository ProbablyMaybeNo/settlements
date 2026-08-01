# Settlements — The Global Points Table

**v0.2** · Scale: **1000 = standard Crew Rating** · Supersedes `GLOBAL-POINTS-SYSTEM.md` (v0.1)

Everything in the game costs points derived from one atom. Build anything by summing its parts from the tables below. Players see only final prices; the derivation is for the designer.

> **The atom.** `1 TICK = 10 points` = **+1 on a single core test** (`1d10 + mod vs 7+` → +10% success, bounded 10–90%).

**What changed from v0.1** — the five defects found on review:
1. **Skills were free.** Fixed by a non-linear stat ladder (§2).
2. **Short Range under-refunded.** Fixed by banding (§6).
3. **No multiplier.** Deliberately still additive — see §9 for the trade and the open decision.
4. **No LIMIT dial.** Added (§8).
5. **Conditional discounts were ad hoc.** Now derived (§5).

---

## 1 · Reading the system

| Layer | Priced by | Rule |
|---|---|---|
| **Additive core** | how well one action lands | damage, to-hit, range, payloads, armour — these add |
| **Gated, never sold** | how *often* a model acts | extra attacks, extra Orders — **rank gates these, no price exists** |
| **Thresholds** | — | 24" range, Damage +4, Armour −2, ±3 modifier — **capped, not priced** |

A unit's cost **is** its Crew Rating. You pay it once to hire and equip; that same number is what it occupies against the battle cap. Stashed, unequipped gear counts **0**.

---

## 2 · Stats — the non-linear ladder

**This is the fix for the free-skills hole.** `Unit Design.md:112` — every stat grants a skill at each tier it reaches (**+2 = T1 · +4 = T2 · +6 = T3**). So the skill is not a separate purchase; it rides the 2nd, 4th and 6th point. Those points therefore cost more.

Skill values are the game's own Advance prices: **T1 = 20 · T2 = 35 · T3 = 55**.

| Stat value | Marginal cost | Running total | Why |
|:---:|:---:|:---:|---|
| **+1** | 15 | **15** | a dabble — no tier, no skill |
| **+2** | **35** | **50** | 15 for the point + **20 for the T1 skill** |
| **+3** | 15 | **65** | no tier |
| **+4** | **50** | **115** | 15 + **35 for the T2 skill** |
| **+5** | 15 | **130** | no tier |
| **+6** | **70** | **200** | 15 + **55 for the T3 skill** |

Cost a fighter's stat line by summing the running total of each stat. `STR+4 / DEX+2 / AGI+1` = 115 + 50 + 15 = **180**.

> **Consequence worth understanding.** Two Fighters no longer cost the same. A spiked `+2/+2/+1` costs 115; a spread `+1/+1/+1/+1/+1` costs 75. That is correct — the first one owns two skills and the second owns none. Rank stops being a price and becomes a **gate**.

---

## 3 · Rank — a gate, not a price

Rank sets what you may buy. It no longer carries a flat cost.

| Rank | Stat pts | Tier caps | Orders | Body base | Max-value build | Cost at that build |
|---|:---:|---|:---:|:---:|---|:---:|
| **Recruit** | 3 | none (no tiers) | 0 | 20 | +1/+1/+1 | **65** |
| **Fighter** | 5 | 2× T1 | 0 | 20 | +2/+2/+1 | **135** |
| **Specialist** | 7 | 1× T2 · 2× T1 | 1 | 20 | +4/+2/+1 | **240** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | 2 | 20 | +6/+2/+1 | **375** |

`body = 20 + stat-line cost + order premium`

| Orders | Premium |
|:---:|:---:|
| 1 (Specialist) | **40** |
| 2 (Leader) | **90** — super-linear on purpose |

**Ladder shape:** 65 / 135 / 240 / 375 → **1 : 2.1 : 3.7 : 5.8**. Steeper than v0.1's 1 : 1.5 : 2.5 : 3.8, because v0.1 was giving away 40–165 points of skills per fighter.

---

## 4 · Weapon classes

| Class | Cost | Damage | Range | Hands | Slots | Min rank |
|---|:--:|:--:|:--:|:--:|:--:|---|
| Unarmed | 0 | +0 | melee | — | 0 | Any |
| Light Melee | **0** | +1 | melee | 1 | 2 | Recruit |
| One-Handed Melee | **40** | +2 | melee | 1 | 2 | Fighter |
| Heavy Melee | **80** | +3 | melee | 2 | 3 | Specialist |
| Thrown | **20** | +1 | 6" | 1 | 2 | Any |
| Sidearm | **40** | +2 | 8" | 1 | 2 | Recruit |
| Standard Ranged | **100** | +3 | 18" | 2 | 3 | Fighter |
| Heavy Ranged | **140** | +3 | 24" | 2 | 4 | Specialist |

### 4.1 · Range is banded, never per-inch

**Range is priced by which threshold a weapon clears.** A per-inch rate is wrong because the same 6" is worth far more at the top of the ladder than at the bottom.

| Band | Range | Clears | Classes |
|---|:--:|---|---|
| melee | 0" | — | Unarmed, Light/One-Handed/Heavy Melee |
| thrown | 6" | neither threshold | Thrown |
| close | 8" | neither threshold | Sidearm |
| **effective** | **18"** | the **12"** threshold | Standard Ranged |
| **deployment** | **24"** | the **24"** ceiling | Heavy Ranged |

### 4.2 · The two thresholds — preconditions, not priced features

Neither threshold is something you buy. They are the structural facts that make the band values mean anything, and they belong with the caps in §11.

- **12" — the turn-one firing threshold.** Deployment zones sit 24" apart and MOV is 6". A rifle at 18" closes 6" and fires on turn one (`24 − 6 = 18`). A pistol at 8" must cross 16" and cannot. 12" is where that flips.
- **24" — the deployment distance.** A 24" weapon fires on turn one without moving at all. Nothing is priced above it; 24" is a hard ceiling.

### 4.3 · What is actually derived

**18" → 24" = 60**, derived twice independently and checked by `verify.verify_structural()`:

1. `Long Range` costs **60** for exactly that +6".
2. Heavy Ranged = Standard + 6" + built-in Cumbersome: `100 + 60 − 20 = 140` ✓

**The lower steps are unpriced.** Not zero, not estimated — unpriced. They cannot be read off the class table without also splitting out Damage and Hands from the same figure. Sidearm 40 (Damage +2, 8") → Standard Ranged 100 (Damage +3, 18") is a gap of 60 containing one Damage step *and* one range step *and* a Hands step.

> ⚠️ **A number that died in M1.** The old figure "8"→18" is worth ~20" was `60 − 40`, computed when Damage cost 40. With the measured Damage atom of **15** the same subtraction leaves **45** for range-plus-Hands. Neither 20 nor 45 is a measurement of the range step alone, so `ticks.py` records this step as `RANGE_STEP_UNPRICED`. **Do not carry the 20 forward.**

---

## 5 · Characteristics

### 5.1 · The measured atoms **[measured 2026-07-30]**

There is no single "unconditional baseline" any more. A +1 is worth different amounts depending on *which roll* it lands on, and the difference was measured, not assumed.

Source: `test-bench/balance/realistic.py`, re-run and reproduced 2026-07-30. A free +1 given to one side; win-rate delta divided by models buffed; averaged over the all-armed lists (Gunline 4 / Fireteam 6 / Squad 8) at medium and dense density.

| Primitive | medium | dense | mean | relative to +1 Damage | **Credits** |
|---|:--:|:--:|:--:|:--:|:--:|
| **+1 to-hit** | +1.4367 | +1.8667 | 1.6517 | **1.4769×** | **22** |
| **+1 Damage** | +1.1733 | +1.0633 | 1.1183 | **1.0000×** *(anchor)* | **15** |
| +1 Armour | +0.9833 | +1.2733 | 1.1283 | 1.0089× | *(15.13 — see §7)* |
| **+1 Stress** | +0.5700 | +0.4400 | 0.5050 | **0.4516×** | **7** |

Anchoring +1 Damage = 15 Credits yields **22.15 / 15.00 / 15.13 / 6.77** → 22 / 15 / 15 / 7.

**Why to-hit beats damage.** Average cover is ≈ −1.1, so the hit roll (~49%) is the bottleneck against the injury roll (~70%). `P(kill) = P(hit) × P(injure)` — a multiplicative engine rewards fixing the bottleneck.

> ⚠️ **Provenance caveat.** `realistic.py` runs on `crew_sim.py`, which documents itself as a **1D board**, and it does not swap sides. The 2.5D engine has not reproduced these four exchange rates. §7 records a case where a 1D armour result was later shown to be an artefact — so the 1D provenance of the anchor is a live risk, not a settled fact.

### 5.2 · The conditional ladder

> **`L = (1 − f) / f`**, where **f** = the fraction of activations the condition is met. Net multiplier = **f**.

The multiplier applies to whichever atom the trait grants — a conditional to-hit trait divides down from 22, a conditional injury trait from 15.

| Condition holds | f | Multiplier | from the **22** to-hit atom | from the **15** damage atom |
|---|:--:|:--:|:--:|:--:|
| always | 1.00 | ×1.00 | 22 | 15 |
| most activations | 0.80 | ×0.80 | **18** | 12 |
| two in three | 0.67 | ×0.67 | 15 | 10 |
| about half | 0.50 | ×0.50 | 11 | 8 |
| one in three | 0.33 | ×0.33 | 7 | 5 |

**`f` is not yet measured for any trait.** Every `f` below is a judgement band. Instrumenting each trait and counting is Milestone 4 of the completion plan; until then the conditional column is provisional and only the `f = 0.8` row has been applied.

### 5.3 · The table

| Characteristic | Cost | f | Basis | Effect |
|---|:--:|:--:|:--:|---|
| **Brutal** | **15** | 1.0 | **[measured]** | +1 Damage (max +4) |
| **Armour Piercing** | **9** | *f(armour)* | **[measured M4]** | Target armour −1 on Injury — **exactly +1 Damage against an armoured target, exactly nothing against a bare one.** 9 is the blend over two bare lists and one armoured one; in an armoured meta it is worth the full 15 |
| **Accurate** | **18** | 0.8 | **[measured, provisional f]** | +1 hit if you did not Move/Sprint/Climb |
| **Spread** | **18** | 0.8 | **[measured, provisional f]** | +1 hit at ≤ half range, −1 beyond |
| **Rate of Fire 2** | **50** | 1.0 | **[measured]** | 2 hit dice; each extra hit = **+1 Stress** (§10) |
| **Bleeding** | **46** | 1.0 | **[measured M4]** | Payload: **Bleed** — a death clock at WND 1 |
| **Suppressive** | **17** | 1.0 | **[measured M4]** | Target may not clear the Pin with its Move |
| **Blast** | **43** | 1.0 | **[measured M4]** | Resolve against every model within 2" |
| Cleaving | 50 | 1.0 | legacy | Injury vs every Engaged enemy on a melee win |
| **Incendiary** | **22** | 1.0 | **[measured M4]** | Payload: **Fire** |
| **Shocking** | **16** | 1.0 | **[measured M4]** | Payload: **Shocked** |
| **Toxic** | **9** | 1.0 | **[measured M4]** | Payload: **Poison** |
| **Blinding** | **4** | 1.0 | **[measured M4]** | Payload: **Blind** |
| Concussive / Crippling | 30 | — | **⚠ measures zero** | Payload: Off-Balance / Hobbled — see §5.5 |
| **Heavy Impact** | **15** | 1.0 | **[measured M4]** | Push 2" |
| Smoke | 30 | 0.8 | legacy | Place 3" Dense Smoke instead of attacking |
| Breaching | 30 | 0.8 | legacy | +2 STR vs Breachable |
| **Long Range** | **60** | — | derived ×2 (§4) | +6" to the 24" ceiling — **threshold premium, not a rate** |
| Defensive | 20 | 0.5 | legacy | +1 opposed melee when not attacker and didn't Move |
| Balanced | 20 | 0.5 | legacy | Use AGI for melee |
| Hook | 20 | 0.5 | legacy | Pull 1" (melee) |
| Concealable | 20 | 0.5 | legacy | May start Hidden / smuggle |
| Quiet | 20 | 0.5 | legacy | No reveal, no alarms |
| Compact | 20 | 0.5 | legacy | Counts as one-handed |

**Rate of Fire 3 is unpriced.** Not "roughly 75", not "about double" — **unpriced**. The third die is superlinear and there is deliberately no entry in `ticks.py`.

**The remaining legacy rows are not derived from anything** — Hook, Smoke, Long Range, Balanced, Defensive, Cleaving, Breaching, Concealable, Quiet, Compact are still inherited from the old hand-set table.

### 5.4 · What M4 moved — every payload measured on its own **[2026-08-01]**

The flat 30 was a *grouping*, and the group turned out to span **46 : 1**. Source: `balance/conditions2d.py`, 1200 games/cell, sides swapped, on the 2.5D engine with the condition layer implemented (`engine2d/engine.py`; behaviour verified by `engine2d/test_conditions.py`, 21/21 passing).

**Two passes were run and they disagree — read the mirror.**

| Pass | Design | Verdict |
|---|---|---|
| **Asymmetric** | Buffed list vs a fixed opponent, as `primitives2d.py` does it | **Discarded as primary.** Hold baselines sit at **8%** (Gunline) and **92%** (Squad), so a buff has almost no room to move the number. Every delta is compressed toward zero |
| **Mirror** | Identical crews, one side buffed | **Used.** Baseline is exactly 50% by symmetry — maximum sensitivity, no clipping, and deployment/activation asymmetries cancel exactly |

Every low-value trait rose between the two passes, which is the signature of exactly the clipping the mirror pass was built to remove.

| Characteristic | mirror | asym | was | ×Damage | catalogue effect |
|---|:--:|:--:|:--:|:--:|---|
| **Bleeding** | **46** | 54 | 40 | 3.05× | Nailgun **140 → 146**, the only weapon that went **up** |
| **Blast** | **43** | 46 | 40 | 2.89× | unchanged in practice |
| **Incendiary** | **22** | 24 | 30 | 1.48× | Molotov 90 → 85, Flamethrower 150 → 135 |
| **Suppressive** | **17** | 5 | 40 | 1.11× | Squad MG 220 → 186 |
| **Heavy Impact** | **15** | 22 | 30 | 0.99× | Sledgehammer 140 → 125 |
| **Shocking** | **13** | 1 | 30 | 0.84× | — |
| **Armour Piercing** | **9** | 1 | 15 | 0.59× | conditional on armour — see §5.3 |
| **Toxic** | **9** | 2 | 30 | 0.58× | — |
| **Blinding** | **7** | −1 | 30 | 0.43× | — |

Nine of sixteen catalogue weapons moved, **−143 Credits** across the sample armoury.

### 5.5 · Two traits measure at zero — that is a rules defect, not a price

| Trait | Condition | Measured |
|---|---|:--:|
| **Concussive** | Off-Balance — no Sprint or Charge | **1** |
| **Crippling** | Hobbled — −2" MOV | **−2** |

Both sit inside the noise floor. **They are deliberately left at 30 in `ticks.py` and flagged by `points.verify` rather than repriced to nothing** — selling a player a trait that does nothing is worse than selling it at the wrong price.

### 5.6 · The duration experiment — run, and it mostly failed

All four low-measuring conditions were strengthened in the vault and re-measured on the same harness.

| Change | | |
|---|---|---|
| Blind · Shocked | clear in the End Phase | → ends at the end of its **next activation** |
| Off-Balance · Hobbled | expire after one activation | → **persist until cleared** with the Move slot, like Pinned |

| Trait | before | after | Verdict |
|---|:--:|:--:|---|
| Shocking | 13 | **16** | helped |
| Blinding | 7 | **4** | no better — both inside noise (≈ ±2) |
| Concussive | 1 | **−1** | still zero |
| Crippling | −2 | **1** | still zero |

**How strong the Hobbled test actually was:** nothing in the simulator ever spends a Move to shed it, so what was measured is a **permanent −2" MOV for the rest of the game** — and it is *still* worth nothing. Movement debuffs do not pay on a 36" board over six rounds. Two caveats keep this a lower bound: the AI does not kite or focus slowed targets, and it never chooses to shed the condition.

**The duration changes were kept anyway**, on design grounds rather than measured value: a payload that cleared in the End Phase did nothing at all if the target had already activated, and an invisible coin-flip the player cannot read off the card is worse than a small effect.

**The remaining options for Concussive and Crippling are: strengthen much harder, or cut them.** A third re-measure of the same shape is not worth running.

### 5.7 · Why every payload measures lower than it feels — the wounding gate

A payload only lands on a hit that **fails to wound**. A rifle (+3) into no armour wounds ~70% of the time, so only ~30% of hits deliver their payload at all.

**Payload value therefore rises with target armour**, and it is visible in the data: in the `ARMOURED6` mirror column almost every payload measures higher than in the bare-list columns. Pricing a payload against bare targets *understates* it in an armoured meta and *overstates* it in a naked one. This is the strongest argument for settling the armour level (M2) before the payload prices are re-locked.

A related timing finding, which is a rules question and not a costing one: **Blind and Shocked clear in the End Phase**, so a payload delivered mid-round only bites a target that has not yet activated. Roughly half the time they do nothing at all, which is most of why they measure at 7 and 13 rather than near Bleed. Moving them to *"until the end of its next activation"* (the Hobbled/Off-Balance clock) would make them worth carrying. **No price can fix a duration problem.**

### 5.4 · What M1 moved

Repricing the injury and to-hit atoms moved **5 of 16** catalogue weapons, all downward, for a total of **−111 Credits** across the sample armoury.

| Weapon | was | now | Δ | why |
|---|:--:|:--:|:--:|---|
| Fire Axe | 160 | **135** | −25 | Brutal 40→15 |
| Pipe Shotgun | 120 | **83** | −37 | Brutal 40→15, Spread 30→18 |
| Assault Rifle | 130 | **118** | −12 | Accurate 30→18 |
| Grandpa's Hunting Rifle | 190 | **178** | −12 | Accurate 30→18 |
| Squad Machine Gun | 220 | **195** | −25 | Armour Piercing 40→15 |

The other 11 are unchanged because they carry no repriced characteristic. Nothing was adjusted to compensate.

---

## 6 · Drawbacks — refunds

**A drawback must bite no matter how you play** (`Weapons.md:120`). A drawback dodgeable by playstyle is a discount, and does not belong here.

| Drawback | Refund | Effect |
|---|:--:|---|
| **Short Range** — Sidearm / Thrown | **−20** | Halve max range |
| **Short Range** — Standard Ranged | **−30** | 18" → 9" |
| **Short Range** — Heavy Ranged | **−70** | 24" → 12": **loses the 24" threshold entirely** |
| **Slow** | −30 | May not Charge. *Melee only* |
| **Limited** | −30 | One use per battle |
| **Unstable** | −20 | Nat 1 to hit → weapon destroyed |
| **Cumbersome** | −20 | −1 MOV while carried |

**Fix from v0.1:** Short Range was a flat −30, which on a Heavy Ranged handed back a 24"→12" collapse for the same refund as an 18"→9" one. It now scales with what is actually lost. Max **2 drawbacks** per weapon.

**Implemented 2026-07-30 (M3).** This banding was doc-only until now — `ticks.py` still charged a flat −30. It is now `SHORT_RANGE_REFUND`, keyed by class, and it is wired into `weapon_cost`. Two guards came with it: Short Range on a **melee** class is now an error (there is no range to halve), and `verify_structural()` checks the refunds stay negative, never exceed the class cost, and stay **monotonic** in range — a longer-ranged class can never get back less than a shorter-ranged one.

The one catalogue price this moved: **Makeshift Flamethrower 150 → 110** (Heavy Ranged short range −30 → −70).

---

## 7 · Armour & equipment

**Armour carries no drawbacks** *(decision 2026-07-30)*. The old table taxed it twice — Improvised −1 AGI, Heavy −1 MOV / −1 AGI / Loud — and **neither simulator modelled AGI meaningfully**: the 1D board never reads it at all, and the 2.5D engine uses it only for the Dodge reaction. So every armour measurement taken to date priced those penalties at **zero**. The real items were worse than anything measured.

The ladder is now linear in what armour does. `Injury = 1d10 + Damage − Armour vs 7+`, so each point is a flat **−10%** on being hurt: **−2 is worth exactly twice −1, and Heavy costs exactly twice Light.**

| Armour | Cost | Injury |
|---|:--:|:--:|
| None / Thick clothing | 0 | 0 |
| **Light** | **30** | −1 |
| **Heavy** | **60** | −2 |

**Improvised is cut.** With its −1 AGI penalty removed it was Light armour under a second name at the same price — a redundant row. Scavenged-versus-bought is a settlement-economy distinction and does not need its own catalogue entry.

**The level is measured** *(`balance/armourprice.py`, every crew rebuilt to 100 pts)*: the three melee builds cluster tightest between 20 and 30 per armour point, and fan out badly at 60 — bare 73% / light 51% / heavy 42%. Parity sits near 25; **30** is the integral value inside that bracket.

This also largely closes the anchor dispute: the primitive method implied ~15/point and the body-trade now says ~25–30. The old **60 was the outlier**, and it was only ever defensible because it was paying for drawbacks that neither simulator modelled.

> ⚠️ **The absolute level is still unresolved.** Both engines agree armour is worth about the same *per point* as +1 Damage (1D 1.0089×, 2.5D 0.9756×). But the two costing methods disagree on the level: the **primitive** method implies ~15/point, the **body-trade** method breaks even nearer 60/point. That gap is the **body-vs-damage scale problem**, not an armour problem — the weapon *class* costs are still legacy and unmeasured, so comparing a measured characteristic against an inherited class price gives a nonsense ratio. The table holds 60 pending measurement of the classes.

| Equipment | Cost |
|---|:--:|
| Med-Kit | 40 |
| Breach Kit | 40 |
| Exploit Suite | 80 |


## 8 · The LIMIT dial

Price answers *"how strong is this?"*. It cannot also answer *"how many should exist?"*. Trench Crusade tunes the two separately, and a **player-built armoury generates combinations nobody costed in advance** — so a cap is cheap insurance where a price is a guess.

Every catalogue entry may carry:

| Dial | Meaning |
|---|---|
| **Cost** | points, from this table |
| **LIMIT: N** | max N of this item per crew, ever |
| **0-N** | max N on the roster at once |
| **Rank gate** | minimum rank to carry it |

Suggested starting limits: **Blast LIMIT 2 · Rate of Fire 3 LIMIT 1 · Cleaving LIMIT 2.**

---

## 9 · The open decision — additive or multiplicative?

The engine is multiplicative: `P(kill) = P(hit) × P(injure)`. So a 100-point rifle delivers ~33% more kill probability on a DEX+4 Leader than a DEX+2 Fighter, and costs the same. **Elite crews are therefore slightly undercosted for their gear, swarms slightly overcosted.**

| Option | Gains | Costs |
|---|---|---|
| **A — stay additive** *(current)* | one price per item; a single table you can sum | elite gear undercosted |
| **B — multiply gear by carrier stat** (the OPR method) | correct coupling, automatically | **a gun no longer has one price** — the catalogue becomes carrier-dependent |

**A is assumed here**, because a single summable table was the requirement. Two things bound the error: the **±3 modifier cap** keeps builds near the diagonal where additive pricing is valid, and **rank gates** already stop Recruits carrying the best guns.

**The test that settles it:** run the 4-model Cadre against the 11-model Pyramid at 1000 points. If the elite list drifts up, option A is leaking and B is needed.

---

> 🚦 **DECISION GATE (M7) — evidence only. Nothing has been changed.**

**The test was run** (`balance/suite.py`, 8 crews × 5 scenarios, 200 games/pairing, sides swapped, 2.5D) and **the elite list does not drift up. It drifts down.**

| Crew | models | pts | mean win% |
|---|:--:|:--:|:--:|
| Mob 11 | 11 | 97 | **67** |
| Armoured 7 | 7 | 95 | 65 |
| Horde 12 | 12 | 97 | 63 |
| Redline 6 | 6 | 98 | 55 |
| Skirmish 6 | 6 | 94 | 46 |
| Turret 5 | 5 | 97 | 36 |
| Elite 3 | 3 | 92 | 36 |
| **Gunline 4** | 4 | 96 | **32** |

Model count explains most of it: **r = 0.841, r² = 0.708**, slope **+3.78 win-points per extra model**. At equal points the elite crews are the *worst* in the game, not the best.

**The coupling the section predicts is nonetheless real and large.** Per model buffed (`primitives2d.py`, 2000 games/cell):

| Primitive | Gunline 4 | Squad 8 | elite advantage |
|---|:--:|:--:|:--:|
| +1 to-hit (Hold) | +1.56 | +0.26 | **6.0×** |
| +1 to-hit (Annihilate) | +3.62 | +1.33 | **2.7×** |
| +1 Damage (Annihilate) | +1.97 | +0.83 | **2.4×** |

So a point of offence really is worth 2.4–6.0× more on an elite model — **and it still is not enough to make elite lists competitive.** Body count swamps it.

**A caveat that weakens the case for B further.** Annihilate is the one scenario where elites lead (Gunline 71%, Elite 70%), and its scoring is **not normalised by crew size** — VP is a raw count of enemy models removed. Gunline 4 vs Mob 11 scores **4.75 vs 1.53** VP; as a *fraction of the enemy crew destroyed* that is **43.2% vs 38.1%** — nearly even. Much of the elite lead in Annihilate is a scoring artefact, not lethality.

**Scenario scoring remains the dominant lever**, as the completion plan already found. Per-scenario spread in this run: Hold **65**, Breakthrough **64**, Loot **60** — against Hold+Claim **37** and Annihilate **36**.

---

## 10 · Rate of Fire — measured, not guessed

> **RoF (N).** Roll **N dice to hit**. The first hit resolves in full (Injury roll, or payload/Pin if it fails to wound). **Each additional hit inflicts +1 Stress** on the same target. Extra hits are wasted if the first one Downs it. No extra Injury rolls — RoF can never raise lethality.

**Measured 2026-07-28** by rebuilding the list to pay for the upgrade rather than granting it free:

| Variant | gave up | vs Pyramid | vs Horde | vs Standard |
|---|:--:|:--:|:--:|:--:|
| baseline | — | 64 | 64 | 68 |
| RoF 2, nothing given up | 0 | 79 (+15) | 81 (+17) | 69 (+2) |
| **RoF 2, dropped a Fighter** | **12** | **61 (−3)** | **62 (−2)** | **62 (−6)** |
| RoF 2, no armour + fists | 20 | 48 (−16) | 55 (−9) | 56 (−12) |

RoF 2 on two rifles ≈ 12 points at the 100-scale, slightly under → **~50 at the 1000-scale.** No to-hit penalty required; the cost carries it.

**Reproduced 2026-07-30** — `balance/rof_cost.py` re-run returned the identical row: *RoF 2, dropped a Fighter* = **61 (−3) / 62 (−2) / 62 (−6)**. `rate_of_fire_2 = 50` is now in `ticks.py`. Note this measurement, like the primitives in §5.1, comes from the **1D** `crew_sim.py`.

**RoF 3 is unpriced.** The third die adds little hit chance (84%→94%) but much more Stress (0.36→0.86 extra per attack), so it is superlinear. Run the same test before it ships.

---

## 11 · Caps — preconditions, not patches

These are **part of the costing system**. Additive pricing is only valid because they pin builds near the `hit ≈ damage` diagonal.

- Damage ≤ **+4** · Armour ≥ **−2** · modifiers **±3** · range ≤ **24"**
- **WND = 1** · MOV = 6" (raised only by named skills)
- Legal board **9–12** large features
- Extra attacks and Orders: **rank-gated, never sold**
- Max **2 drawbacks** per weapon

---

## 12 · Worked examples

**Weapons** — `class + characteristics − drawbacks`

| Build | Math | Cost |
|---|---|:--:|
| Assault Rifle | Standard 100 + Accurate **18** | **118** |
| Auto Rifle | Standard 100 + RoF 2 50 | **150** |
| Pipe Shotgun | Standard 100 + Brutal **15** + Spread **18** − Short 30 − Unstable 20 | **83** |
| Hunting Rifle | Standard 100 + Accurate **18** + Long Range 60 | **178** |
| Squad MG | Heavy 140 + Suppressive 40 + AP **15** | **195** |
| Flamethrower | Heavy 140 + Incendiary 30 + Blast 40 − Short **70** − Limited 30 | **110** |
| Fire Axe | Heavy Melee 80 + Brutal **15** + Bleeding 40 | **135** |

*Every bolded figure moved in Milestone 1 (atoms) or Milestone 3 (Short Range banding). All verified against `py -3.13 -m points`.*

**A fighter** — `20 + stat line + orders + gear`

| Leader | Math | Cost |
|---|---|:--:|
| body | 20 + (DEX+6 = 200) + (STR+2 = 50) + (NRV+1 = 15) + 2 Orders 90 | **375** |
| gear | Assault Rifle **118** + Light armour 60 + Med-Kit 40 | 218 |
| **total** | | **593** |

| Fighter | Math | Cost |
|---|---|:--:|
| body | 20 + (STR+2 = 50) + (INT+2 = 50) + (AGI+1 = 15) | **135** |
| gear | Sidearm 40 | 40 |
| **total** | | **175** |

| Recruit | Math | Cost |
|---|---|:--:|
| body | 20 + (STR+1 15) + (AGI+1 15) + (NRV+1 15) | **65** |
| gear | Light Melee 0 | 0 |
| **total** | | **65** |

A 1000-point crew: that Leader (**593**) + Fighter (175) + Recruit (65) + Recruit (65) = **898**, 102 spare.

---

## 13 · Still open

- [ ] **Armour** — resolve the pricing and the two-note contradiction before locking
- [ ] **Additive vs multiplicative** (§9) — run the elite-vs-swarm test
- [ ] **RoF 3** — price by the same rebuild method
- [ ] **Measure `f`** for every conditional trait rather than banding by judgement
- [ ] **Skills as Advances** — the +20/35/55 ladder must match §2, or creation and progression diverge
- [ ] **The pyramid after founding** — at 65/Recruit, 15 Recruits = 975 is a legal 1000-point crew with no Leader
- [ ] **Deployables, structures, the 2051 arsenal** — not yet costed from this spine
- [ ] Re-run the full crew sim against these numbers; the 5/8/16/24 ladder was never validly validated

---
*v0.2 · 2026-07-28. Every number here is provisional until simmed. Where a figure is measured rather than reasoned, it says so.*

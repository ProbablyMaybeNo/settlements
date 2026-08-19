# Settlements — The Points Catalogue

**v1.0 · 2026-08-13 · scale 1000 = standard Crew Rating**

Every price in this game, what it is worth, and where the number came from.
Machine-readable source: `test-bench/points/ticks.py`. Measurements:
`test-bench/balance/results/`, engine `e2b861d61` / harness `hf20a47e3`.

This supersedes nothing — `POINTS-TABLE.md` remains the design document and
`POINTS-REBUILD-TRACKING.md` remains the working board. **This is the shipping
artefact: the list a player's costs actually resolve through.**

---

## How to read a price

Every number carries a confidence tier. **No number ships untagged.**

| Tier | Means | How to treat it |
|:--:|---|---|
| **A** | Measured, current, statistically significant | Trust it for play |
| **B** | Measured, but wide CI or single-scenario coverage only | Usable; expect movement |
| **C** | **Derived by rule** from an A/B atom, never measured directly | Placeholder — the first thing table data corrects |

A C-tier price is fine. An **untagged** price is not: that is the exact defect
this rebuild existed to eliminate. Every C entry below states its derivation. If
you cannot read how a number was reached, that is a bug — report it.

---

## ⚠ Read this before using any number in this document

### 1. The list-context ceiling — this bounds the whole catalogue

An 18″ gun measures **~39% more valuable in an all-melee crew** than the
decomposition through a gun-carrying crew predicts — direct **+10.930** vs
composed **+7.870**, a gap of **3.060 ± 1.460**, significant.

Every price here is per-item, set independently of the list it goes into. That
assumption is measurably wrong by about a third. **No flat per-item catalogue is
accurate past this bound, and no amount of better measurement raises it** —
tighter CIs, more scenarios and a better AI all improve the numbers *inside* the
ceiling and none of them move the ceiling itself.

This is a property of points systems generally, not a defect in this one. It is
stated first because it is the largest single caveat on the document.

**And it operates INSIDE the payload table, not only at the catalogue's edges.**
Every payload price is **net of Pinned** — a payload lands *in place of* the
ordinary non-wounding result. But **value(Pinned) is itself list-dependent**:

| Chassis | value(Pinned) |
|---|---|
| Mixed rosters (Fireteam / Squad / Armoured) | **+0.510**, significant |
| Uniform rifle crew | **+0.086**, not significant |

So the quantity every payload price is measured *against* moves by roughly 6×
with the composition of the crew. The consequence is specific and it matters:

> **Payload prices are structurally noisier than their confidence tiers imply.**
> A B-tier payload row carries the uncertainty of its own measurement *plus* the
> uncertainty of a subtrahend that is not a constant. The tier describes the
> former only.

Treat the payload table's *ordering* as far more reliable than its *levels*, and
expect table testing to move the levels more than the tiers suggest.

### 2. Single-scenario coverage

Everything is priced on **`hold_claim` — Take a Hold, 1 of 5 shipped scenarios,
and the most static one.**

| Shipped scenario | Shape | Modelled |
|---|---|---|
| Take a Hold | Control, VP accrual | ✅ |
| Escort | Mobile, asymmetric | ❌ blocked — no model defends anything |
| Raid | Retrieve, enemy's half | built, passes verification, not yet priced from |
| Sabotage | Timer, sudden death | built, passes on 2 of 3 crews |
| Power Supply | Network, sudden death | ❌ |

**Expect static and defensive atoms — range, damage, armour — to read HIGH, and
mobility, tempo, stealth and objective-running to read LOW.**

### 3. Known policy residuals

- **Sprint overcorrection.** The AI runs across open ground where a slower
  advance would shoot, costing ~40–46% head-to-head in 3 of 9 cells. Symmetric,
  so it skews no mirror — but mobility-adjacent atoms may read low.
- **Nobody defends.** Every model's goal is the enemy's objective. Blocks Escort
  entirely and leaves a planted charge never defused.
- **Melee models charge rather than press objectives.** The one remaining
  Sabotage verification failure.
- **Orders** carry a standing AI-limitation caveat: never measured as an Order on
  any engine.

### 4. The anchor is PROVISIONAL

**+1 Damage = 0.606 wp/model**, and this is the **fifth value in a row to reject
its predecessor**:

| Anchor | Rejected by | Cause — invisible from inside the number that carried it |
|---|---|---|
| 1.150 | 1.332 | the AI shot instead of advancing |
| 1.332 | 0.786 | Annihilate averaged into a price |
| 0.786 | 0.3432 | half its weight was `hold`, which models no shipped scenario |
| 0.3432 | 0.606 | the AI never Sprinted and never took an objective Interact |
| **0.606** | — | *unknown* |

Every one of those runs was internally clean — paired estimator, tight CI, sane
spread. It has now been **corroborated once** (rosters 0.606 vs probe chassis
0.712, gap 0.106 ± 0.164), but **within the same instrument**: both routes share
an engine, a policy and single-scenario coverage. That rules out derivation error
in one path. It does **not** touch the failure class that has actually bitten
this project four times out of four.

---

## The scale

| | |
|---|---|
| **+1 Damage** | **0.606 win-points per model**, CI [0.436, 0.776] · **[B]** |
| **The peg** | +1 Damage ≡ **15 Credits**. A **choice**, not a measurement |
| **Conversion** | **24.77 Credits per win-point** |
| **Shape** | **FLAT — settled.** Density sweep moved it +0.176 ± 0.184 across 9/11/12 features. Flat-vs-curve is **closed** |

---

## 1 · Stats — the measured ladder

**The flat 15/point was wrong in both directions.** This is the largest single
correction in the rebuild.

| Rung | DEX *(one-sided)* | STR *(opposed)* |
|:--:|:--:|:--:|
| 0→1 | **37 Cr** | 25 Cr |
| 1→2 | **26 Cr** | 25 Cr |
| 2→3 | **27 Cr** | 25 Cr |
| 3→4 | **18 Cr** | 25 Cr |
| 4→5 | **15 Cr** | 25 Cr |
| 5→6 | **10 Cr** | 25 Cr |

**[B]** `stat-ladder-n3000`. Every rung significant.

**Why the two shapes differ, and why that is the placement rule for every other
stat.** A one-sided stat is tested against a **fixed TN**, so it *saturates* —
the sixth point improves a roll that is already passing. An opposed stat is
tested against another model's stat, where `P(X+a > Y+b)` depends only on `b−a`,
so it **cannot** saturate. STR measured flat to four decimals at every rung; the
structure predicted that before it was measured.

| Stat | Ladder | Tier | Derivation |
|---|---|:--:|---|
| **DEX** | one-sided | **B** | Measured. Shooting, vs a fixed TN |
| **STR** | opposed | **B** | Measured. Melee, opposed by the target's STR |
| **INT** | one-sided × 0.8 | **C** | Interact is `1d10+INT vs 7+` — a fixed TN, so one-sided like DEX. Discounted because it fires only on activations spent interacting, where DEX fires on nearly all. All five scenarios score through an Interact, so it is never dead |
| **NRV** | one-sided × 0.8 | **C** | Morale/Stress vs a fixed TN — one-sided. Discounted: fires only under pressure |
| **AGI** | opposed × 0.8 | **C** | **Engine-blocked** — read only inside the Dodge reaction, and `DODGE_ON` is False, so it measures exactly zero *by construction*. Priced by analogy: Dodge is an **opposed reaction**, so it takes the opposed ladder, discounted because it fires only when someone shoots you |

---

## 2 · Gear

### Weapons

### Weapon classes — the hard gate, closed 2026-08-14

**These were `# Weapon classes — legacy ×10` from the start of the project until
today.** They are the reason the rebuild exists: a rifle cost **100** and the
Fighter carrying it cost **95**.

**The old blocker was invalid.** The stated reason for leaving them was that the
lower range steps couldn't be separated from Damage and Hands — an argument that
ran algebra on the `sidearm 40` / `standard_ranged 100` gap. *Those are the
known-bad legacy numbers the rebuild exists to replace.* Solving for an unknown
with untrusted inputs gives an untrusted output. The table could never have been
fixed from inside itself.

So classes are now **built from atoms**, like bodies and armour: damage at the
measured 15/step counted above the free floor weapon, plus a ruled range term.

| Class | Damage | Range | **Cr** | Cheapest carrier | Ratio |
|---|:--:|:--:|:--:|---|:--:|
| unarmed | 0 | — | **0** | — | — |
| light_melee | 1 | — | **0** | recruit 65 | free floor |
| thrown | 1 | 6″ | **5** | recruit 65 | 8% |
| one_handed_melee | 2 | — | **15** | fighter 95 | 16% |
| sidearm | 2 | 8″ | **20** | recruit 65 | 31% ✅ |
| heavy_melee | 3 | — | **30** | specialist 165 | 18% ✅ |
| **standard_ranged** | 3 | 18″ | **35** | **fighter 95** | **37%** ⚠ |
| heavy_ranged | 3 | 24″ | **50** | specialist 165 | 30% ✅ |

**A rifle now costs 35 against a 95-Credit Fighter.** That single line is what
the rebuild was commissioned to fix.

Knock-on across the sample armoury: Assault Rifle **130 → 53**, Hunting Rifle
**190 → 68**, Pistol **40 → 20**. Fourteen of sixteen weapons moved; the armoury
total fell **1780 → 897**.

> **The one row still above the target band, stated rather than tuned away.**
> `standard_ranged` sits at 37% — under the 40% hard cap, over the 33% target. It
> **cannot** be brought down by pricing range lower: its Damage 3 alone is 2 steps
> × 15 = 30 Cr, already 32% of a 95-Credit Fighter. **The constrained side is the
> body scale, not the weapon.** Bodies still use the flat legacy `TICK_STAT = 15`;
> on the *measured* stat ladder a Fighter is ~183 Cr and the same rifle lands at
> **19%**, comfortably in band. That re-derivation changes every crew cost in the
> game, so it is a live open box and Ross's call — not smuggled in here.

### Weapon atoms

| Atom | Value | Tier | Source |
|---|---|:--:|---|
| +1 Damage | **15 Cr** | **A** | the anchor itself |
| +1 Damage *(probe chassis)* | 0.712 wp ≈ 18 Cr | **B** | `weapon-class-atoms-objective-n5000` |
| Range 8″ / 12″ / 18″ / 24″ | 5.75 / 5.17 / 5.34 / 4.68 wp | **B** | **The curve is FLAT.** Whole spread 1.07 sits inside one SE (~0.81) |
| +1 to-hit | 22 Cr *(scalar fallback)* | **B** | Superseded by the DEX ladder — to-hit *is* a DEX rung, and the ladder is not flat |
| +1 Stress | 7 Cr | **C** | No 2.5D measurement isolates Stress. Bounded above by Pinned (13 Cr = "+1 Stress **and** the pin"), so 7 sits inside the bound |
| Rate of Fire 2 | 50 Cr | **C** | 1D rebuild test, never reproduced on the 2.5D engine |
| Rate of Fire 3 | **unpriced** | — | Deliberately absent. The third die is superlinear; do not infer it from RoF 2 |

> ### ⚠ OVERRIDE — `long_range` deliberately contradicts its own measurement
>
> **A fourth tag beside A/B/C, and it exists so nobody "fixes" this to match the
> data.** An override is the one kind of entry a careful reader is most likely to
> break: check the price against the artefact, find a mismatch, helpfully correct
> the wrong one.
>
> | | |
> |---|---|
> | **Measured** | the 8″–24″ curve is **flat** — whole spread 1.07 inside one SE of ~0.81, which prices `long_range` at **~0** |
> | **Shipped** | **60** |
> | **Why** | The flat curve measures **a policy that does not exploit range**, not a rule that does not matter. Two opposite biases bracket it — single-scenario coverage overvalues reach, the sprint overcorrection undervalues it — and a free 24″ is a **known degenerate**: the sim measured a **13–30 point edge** for a list that can fire from its own deployment on turn one |
> | **Retires when** | Scenario coverage lands, or a range-exploiting policy makes the curve measurable honestly |
>
> Shipping 0 here would be following a number off a cliff. Machine-readable at
> `ticks.OVERRIDES_MEASUREMENT`; an override is legitimate **only** with all three
> of measured value, why it is not trusted, and what would retire it.

### Armour

| Level | Injury | Price | Tier |
|---|:--:|:--:|:--:|
| None / Thick clothing | 0 | **0** | — |
| **Light** | −1 | **24 Cr** | **B** |
| **Heavy** | −2 | **41 Cr** | **B** |

`armour-level-n2500`, measured with **zero prior** — the old 30/60 was tagged
`[measured]` citing `balance/armourprice.py`, **a file that has never existed in
any commit on any branch.**

**Corroborated by rebuild-to-pay**, which prices armour in weapons surrendered:

| Package | Result |
|---|---|
| light + (rifle→pistol) | **+0.140 ± 0.200 — fair trade, parity** |
| heavy + (rifle→pistol) | +1.110 — armour worth **more** than the payment |
| heavy + (rifle→bat) | −3.400 — armour worth **less** than the payment |

So **Light ≈ exactly one rifle→pistol downgrade**, and Heavy is bracketed on both
sides. First time an armour price here has been denominated in a measured
quantity rather than a prior.

> **Heavy is NOT twice Light, and the ratio question is closed.** The old rule
> argued each armour point is a flat −10% on the injury roll so −2 must cost 2×
> −1. That is the *wrong quantity*: linear in injury **probability** does not
> imply linear in **win-points**, because the second point buys survival on a
> model already surviving more often. Measured **1.745 ± 0.416**. Separating 2.0
> from 1.667 needs N≈66,000 / N≈194,000, and if the truth sits between them no
> sample size ever resolves it. **The individual values are what get used.**
>
> **Two biases, opposite directions:** armour's own drawbacks (Improvised −1 AGI,
> Heavy −1 MOV / −1 AGI / Loud) are priced at **zero**, so these *overstate*
> armour; and light armour's value **moves with terrain density** (0.140 at 11
> features, 0.508 at 9), so the level is board-dependent.

### Payloads

Every payload price is **net of Pinned**. A payload lands *in place of* the
ordinary non-wounding result, and on a ranged hit that result is **Pinned
(+0.510 wp = 13 Cr, significant)**. So a payload's price is what it is worth
**minus what it displaces** — and a trait can be a perfectly good condition and
still price at or below zero purely because Pinned is strong.

| Trait | Net value | Price | Was | Tier |
|---|:--:|:--:|:--:|:--:|
| **Suppressive** | +1.546 wp | **38 Cr** | 17 | **B** |
| **Bleeding** | +1.410 wp | **35 Cr** | 46 | **B** |
| **Blast** | +1.256 wp | **31 Cr** | 43 | **B** |
| **Incendiary** | +0.942 wp | **23 Cr** | 22 | **B** |
| **Armour-piercing** | +0.392 wp | **10 Cr** | 9 | **B** |
| Shocking | +0.217 wp *(n.s.)* | 5 Cr | 16 | **B** ⚠ |
| Heavy impact | +0.090 wp *(n.s.)* | 2 Cr | 15 | **B** ⚠ |

**Suppressive is now the dearest payload** — the Pin costing the whole activation
is worth far more than the old table thought. **AP at 10 vs the old 9 is the
closest agreement between a measured atom and a shipped price anywhere in this
rebuild.**

⚠ **Shocking and Heavy impact measure positive but inside the noise floor.**
Shipped at measured value per the shipping standard, and flagged: a trait this
cheap gets taken on everything. If table data shows either being auto-included,
the fix is mechanical, not a reprice. **This is the one judgment call in the
payload table.**

### 🚫 Blocked — redesign. These do NOT ship.

**Five traits measure at or below zero net.** The game currently sells five
things that make an attack **worse than not buying them**.

| Trait | Net | |
|---|:--:|---|
| **Crippling** | **−0.613** | significantly negative |
| **Concussive** | **−0.592** | significantly negative |
| **Blinding** | **−0.317** | significantly negative |
| Hook | −0.230 | negative point estimate; SE 0.858, unmeasurably noisy |
| Toxic | −0.080 | negative point estimate, not significant |

**No price fixes this.** Repricing a trait whose whole effect is to replace a
good default with a worse one sells the player a downgrade at any number.

**The mechanism was measured, not assumed** (`condition-values-n3000`):

| | |
|---|---|
| value(Off-Balance) | **+0.000 — exactly. Bit-identical games** |
| value(Hobbled) | +0.078, not significant |
| value(Blind) | **+0.369, significant and POSITIVE** |

So these are **not one problem**. Off-Balance and Hobbled are worth nothing, and
the reason was counted rather than inferred: they are applied in quantity
(**89,498 times**) but land on models that have **already arrived and will not
move again**. Afflicted models account for **0.8% of all movement**, and the
reduced cap actually binds in **0.8% of those**. *A movement debuff that lands
after movement has finished binds on nothing.* Blind is the opposite — a
genuinely valuable condition that still prices negative because what it replaces
is worth more.

> **Escalated to Ross as a RULES question, not a pricing one.**
> **Replace-not-stack was designed when Pinned was believed to be worth ~zero.**
> Pinned measures **+0.510 and significant**. If the default result is strong,
> every trait that replaces it starts in a hole. That is plausibly **one
> miscalibrated rule, not five broken traits.**
>
> *One further complication, logged not chased:* value(Pinned) is itself
> **list-dependent** — +0.510 on the mixed rosters, +0.086 (n.s.) on a uniform
> rifle chassis. Since every payload price is net of it, the subtrahend moves with
> the crew. That is the list-context ceiling operating on the payload table.

### Other gear — all C-tier

| Item | Price | Derivation |
|---|:--:|---|
| Defensive | 30 | Nearest measured neighbour is light armour (24) — same shape of effect. Within rounding |
| Cleaving | 50 | Blast (31) as a multi-target effect + one damage step (15) = 46 |
| **Long range** | **60** | **⚠ OVERRIDE — not measured, not derived.** Deliberately overrides its own measurement; see below |
| Smoke | 30 | Retained. No LOS-denial atom measured; nearest neighbour (Blind) is itself blocked |
| Balanced | 20 | Retained; no measured neighbour |
| Breaching | 30 | Retained; no measured neighbour |
| Concealable | 20 | Retained; stealth unmodelled — no noise system |
| Quiet | 20 | Retained; Loud/Quiet engine-blocked entirely |
| Compact | 20 | Retained; hands/slots inert in the engine |
| Accurate / Spread | 18 | Conditional to-hit at f = 0.8 |

---

## 3 · Body

| Atom | Price | Tier | Derivation |
|---|:--:|:--:|---|
| Bare body | 20 | **C** | Unchanged. No measurement isolates a model with no gear and no stats — every harness roster is built from equipped models. A floor, not a priced atom |
| **+1 WND** | **41** | **C** | **Was 45 with no derivation at all** — the ruleset called it "a judgment call, not a measurement" in three separate places. Now derived from the nearest measured survivability atom: **heavy armour, −2 injury, 41 Cr**. Still C — it is an analogy, not a measurement. **Propagated to the vault 2026-08-13**: all nine references updated, and the full Level track total moves **+245 → +241** |
| Orders (1 / 2) | 40 / 90 | **C** | **The weakest number in the catalogue.** Never measured as an Order on any engine, and no measured neighbour is close enough to derive from. Tolerable only because Orders are **rank-gated and never sold à la carte**, so a list-builder cannot arbitrage them |

---

## 4 · Skills — a three-band scheme

~150 skills exist; **9** are wired into the engine. Individually pricing the rest
is not achievable on any timeline, so they are **banded**, each band derived from
a measured atom of comparable effect size. **Deliberately coarse — it is the only
version that ships.**

| Band | Price | Derivation | Tier |
|:--:|:--:|---|:--:|
| **T1** | **20** | One mid-ladder DEX rung (18), rounded | **C** |
| **T2** | **35** | The first DEX rung (37) — the value of a point that is always live | **C** |
| **T3** | **55** | The dearest measured payload (suppressive, 38) + a mid-ladder rung (18) = 56 | **C** |

**The bands survive derivation unchanged from the legacy table.** That is the one
piece of luck in this write-back: the numbers were right, they simply had nothing
behind them.

### Placement rule — how to band a skill

| Band | Test |
|:--:|---|
| **T1** | It improves one roll, **in a named situation** |
| **T2** | It improves one roll **always**, or improves one roll **by 2** in a situation |
| **T3** | It **removes a restriction, grants an action, or affects another model** |

**When a skill straddles two bands, take the lower and note it.** A cheap skill
that turns out strong is a table-testing correction; an expensive one that turns
out weak never gets taken and is never observed.

---

## 5 · What is still engine-blocked

Not unmeasured — **unmeasurable on the engine as built.** No price should be
inferred for these beyond the C-tier analogies above.

| | Why |
|---|---|
| Hands / slots | `Unit` carries one weapon string; `two_handed` is inert |
| Rank-as-weapon-gate | `CLASS_META.min_rank` is read by nothing |
| Loud / Quiet | No noise or alarm system exists |
| Fire-while-Engaged | `take_action()` forces melee for any engaged unit |
| AGI | Read only inside Dodge; `DODGE_ON` is False |
| ~141 of ~150 skills | Each needs engine work per subsystem |
| Materials axis | Base gatherer rate is **not computable** — D23 prices structures by payback and the denominator is stated nowhere |

---

## 6 · A note on the two cost tables

`points/ticks.py` (this catalogue, 1000-scale) and `engine2d/data.py` (100-scale)
**are deliberately not reconciled.**

`data.py`'s costs exist only so the harness can build **equal-cost rosters inside
the sim**. They are not player-facing prices, and nothing player-facing reads them.

**Reconciling them would close a loop.** Measure → price → rebuild the sim's crews
from those prices → measure again. The second measurement is then no longer
independent of the first, and the apparatus converges on whatever it started with
while every confidence interval stays reassuringly tight.

**This project has already eaten that exact failure once.** T12 set
`BATTLE_CREDITS = RECRUIT_CR` and then printed the ratio back as confirmation — a
result that could not have come out any other way. It sits in the tracking doc's
contaminated-findings list. Reconciling these two tables would rebuild the same
loop at project scale instead of inside one script.

**They differ on purpose. The divergence is the safeguard, not the bug.** If they
ever must agree, the way to do it is to derive `data.py` **from** the catalogue and
then re-measure *knowing the rosters changed* — never to quietly sync the numbers.

---

## 7 · One structural consequence of shipping

Writing measured prices into `ticks.py` marks **every artefact that produced
them** stale on the `cost_table` fingerprint — and re-running reproduces them
exactly, because **nothing in a measurement reads `ticks.py`**. The engine costs
crews from `data.py`; the harness measures win-points and never touches Credits.

So the write-back cannot be performed without appearing to invalidate its own
inputs. `provenance.staleness()` now reports a moved cost table **separately**
from engine and harness changes, marked *downstream — not a reason to re-run*. A
guard that fires when nothing is wrong is worse than no guard.

---

## 8 · End-to-end validation — do equal-points crews play even?

**The first test the points system has ever had of the only question it exists to
answer.** Every earlier measurement priced an *atom* in isolation; none asked
whether two lists costing the same actually win the same.

Four archetypes built from *this catalogue* (not a harness roster), each spent up
to the same Crew Rating, played as side-alternated matchups on `hold_claim`,
N=1500. `catalogue-validation-n1500`.

| | Legacy bodies | **Measured bodies (shipped)** |
|---|:--:|:--:|
| Win-rate spread | **31% – 70%** | **41% – 61%** |
| Worst skew | 20.1% off parity | **11.2%** |
| BROKEN (>10% off) | 4 of 6 | **1 of 6** |

**Re-deriving bodies halved the spread.** That is the evidence the body-scale
ruling rests on, and it is *corroborated* rather than single-sourced: the gear:body
ratio check said bodies were too cheap relative to gear, and the sim independently
said more cheap bodies win. Two different instruments, same direction.

### What is still skewed, and it is one thing

| Matchup | A share |
|---|:--:|
| Armoured vs **Assault** | **61.2%** ⚠ |
| Horde vs **Assault** | 58.9% |
| Elite vs **Assault** | 55.8% |
| Elite vs Armoured | 40.8% |
| Elite vs Horde | 42.2% |
| Horde vs Armoured | 45.6% ✅ |

**Assault — the melee archetype — loses every matchup.** That is the single
remaining structural skew, and it is coherent with the catalogue's known biases:
melee gets no value from the flat range curve, and `hold_claim` rewards holding
ground over closing. Whether melee weapons are overpriced or the scenario
undervalues them **cannot be separated at 1-of-5 scenario coverage** — Raid and
Sabotage, both built and passing, are where a melee crew should show its worth.

**This is a table-testing question now, not a measurement one.** It is the first
thing to watch when the game hits a table.

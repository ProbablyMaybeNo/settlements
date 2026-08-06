# Campaign Start @ 500 — deep 2.5D simulation report

**Run 2026-08-06** · harnesses `test-bench/balance/campaign500_fixes.py` (new), `campaign500_growth.py` (new), `campaign500.py rebuild` (existing)
**Engine:** `test-bench/engine2d/` — layered 2.5D: see-over LOS, height advantage, falls, true geometric cover, objective hold/contest scoring, swappable AI
**Volume:** ~**5.9 million games**. 7 archetypes × 4 scenarios, every pairing, sides swapped; 67k–126k games per configuration; 78 configurations.

---

## Verdict

**Keep 500. It survives, and it does not need the cap raised to 625–750.**

The previous pass concluded *"the 500 cap is the problem, not the rank ladder"* and offered raising the cap as the cheapest fix. That conclusion was measured under a price the project has since **rejected**, and it tested 500 as a **permanent format**, which is not what the rules describe. Re-run properly, three things are true:

1. **The published 46-point spread was inflated.** ~10 of those points were an armour price the project already ruled wrong. The honest baseline is **35**.
2. **The remaining damage has one dominant cause, and it is not the cap — it is the rifle.** `standard_ranged` at 100 Credits is flagged *"legacy ×10"* and unmeasured in the costing engine's own source. Correcting it improves balance at 500 **and** at 1000.
3. **There is one thing about 500 that genuinely cannot be saved: freezing it.** A static 500 cap does not become unbalanced over a campaign — it becomes **arithmetically impossible**. That is the real finding of this report, and the fix is something §16 already promises and never wrote.

Nothing here requires going back to 1000. The one place 1000 reappears is as the *destination* of a ramp that starts at 500 — which is your stated design goal expressed as a rule.

---

## What changed in the method

Three corrections to how this was measured, each of which moved the answer:

| | Previous run | This run | Why it matters |
|---|---|---|---|
| **Armour price** | 30 / 100 from `ticks.py` | **60 / 100** (the adopted price) | `campaign500.py`'s own `armour` mode measured 30/60 as wrong (Armoured 64% → 51%, spread 46 → 37). `FULL-RULES-SYSTEM-V1` §15 and the vault both print 60/100. Every published 500-cap number used the rejected price. |
| **Verticality** | Every crew on the ground | **A Rooftop archetype** under the `ROOF` policy | The engine is 2.5D but no 500-cap crew had ever used height, so verticality was absent from the question entirely. |
| **Metric** | Spread only | Spread + **floor** (worst archetype) + **min models** | A 35-point spread caused by one archetype at 26% is a different disease from the same spread shared evenly. The floor is what tells you whether a player can build what they want. |

---

## 1 · The honest baseline at 500

Doc ladder (R65/F75/S125/L170), armour corrected, 84,000 games:

| | Swarm | Line | Elite | Gunline | Rooftop | Armoured | Mixed | **Spread** | **Floor** |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| win % | 60 | 60 | 55 | **26** | 36 | 52 | 61 | **35** | **26%** |
| models | 4 | 3 | 3 | **2** | **2** | **2** | 3 | | |

Compare the same harness at **1000** Credits: spread **28–31**. So 500 is worse than 1000 — but by 4–7 points, not by the 18 the earlier figure implied.

---

## 2 · The problem at 500 is *legality*, and it costs ten Credits

The mechanism is pure arithmetic, not dice. With a mandatory Leader and a 3-model minimum:

```
Gunline:   Leader+rifle 270  +  Fighter+rifle 175  +  Recruit 65  =  510   ✗ over by 10
Armoured:  Leader+sledge+light 330  +  Fighter+bat+light 135  +  Recruit 65  =  530   ✗
Melee:     Leader+sledge 250  +  Recruit 65 ×3  =  445   ✓  (4 models, fine)
```

**A shooting crew is ten Credits short of its third body.** So the fine cap sweep predicted a cliff at 510, and found one (126,000 games per cap):

| Cap | 500 | **510** | 520 | 530 | 540 | 550 | 575 | 600 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Spread** | 35 | **23** | 23 | 22 | 23 | **19** | 21 | 24 |
| **Floor** | 26% | **37%** | 37% | 36% | 35% | 38% | 38% | 34% |
| **Min models** | **2** | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

**+10 Credits takes the spread from 35 to 23 and the floor from 26% to 37%.** This is a threshold, not a curve — there is nothing gradual about 500, it is simply one body short.

> **Honest caveat.** The sim's crews are built by rigid greedy fill. A real player at 500 *can* build a legal shooting crew by putting the Leader on a pistol (210 + 175 + 65 = 450, 3 models) — so the archetype is **weakened and forced into a compromise**, not literally unbuildable. The 26% floor is measured on the un-compromised list. Either way the cause is the same: the rifle.

---

## 3 · The rifle is the dominant lever — and its price was never measured

`points/ticks.py` marks the whole class table **`# Weapon classes — legacy ×10`**. `standard_ranged` 100 is inherited from the old 10-point value; unlike the characteristics bolted onto it, it has never been measured. At 1000 a rifle is 10% of a crew; at 500 it is **20%**.

Three independent lines of evidence, all landing in the same band:

**a) The rebuild test** (`campaign500.py rebuild` — two identical crews, one pays for a better rifle in bodies; no archetype opinion involved): parity for a +3 Damage 18" rifle sits in **65–95**, and it is clearly overpriced at **110+** (39% win). Coarse, because model count quantizes at a 500 cap.

**b) Derivation from the measured atoms:** `sidearm` (8", +2 Damage) = 40 · one Damage step = 15 *[measured]* · the 18" chassis premium measured at ~15–30 over 8". That gives **40 + 15 + 25 ≈ 80**, built entirely from numbers that were measured, with no legacy value in the chain.

**c) The surface sweep** — 18 configurations, cap × rifle price, 67,200 games each. **Judge a row by its mean and worst cell, not its best:**

| rifle | 500 | 510 | 525 | 550 | 575 | 600 | **mean** | **worst** |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **100** | **35** | 24 | 23 | 20 | 20 | 25 | 24.3 | **35** |
| **85** | 12 | 23 | 15 | 17 | 34 | 26 | 21.0 | 34 |
| **70** | 10 | 16 | 15 | 26 | 26 | 24 | **19.5** | **26** |

Floor surface (higher is better), same grid: **100 → 34.9% mean / 26% worst · 85 → 37.3% / 28% · 70 → 38.1% / 31%**.

Two things this surface establishes, and one it kills:

- **(rifle 100, cap 500) is the single worst cell on the entire surface** — and it is exactly the shipped configuration. That is a robust result.
- **A cheaper rifle is better on average *and* in the worst case.** Mean spread 24.3 → 19.5; worst-case 35 → 26.
- **It kills the headline I nearly reported.** A single run showed "rifle 70 at cap 500 = spread 9", which looked like a total fix. The grid shows the same price scoring **26** at cap 550. That 9 was a **quantization coincidence** — greedy crews land on lucky model counts at particular (cap, price) pairs. Spread from any single configuration at these caps is not a reliable design target; only the surface is. **I am not recommending a number that only works in one cell.**

**Does a cheaper rifle break the 1000-Credit Match Play game it has to coexist with?** No — it slightly helps: spread **31** at rifle 100, **32** at 85, **28** at 70.

> **Cascade to flag:** `ticks.py` derives `heavy_ranged` 160 as `standard_ranged` 100 + `long_range` 60. Repricing the standard class to ~80 makes heavy ranged ~140 by the same identity. That is a consequence of the correction, not a separate decision, but it should be applied deliberately rather than discovered later.

---

## 4 · The finding that actually matters: a *frozen* 500 cannot host a campaign

§16 says a Campaign Start crew *"Begins at **500 Crew Rating**, **growing over the campaign** (§25.5, §29)."* But **no rule anywhere defines that growth**, and §25.5 — the only place that sets a cap at battle time — lists only *"standard 1000, raid 750, pitched 1500."* The ramp is promised and unwritten, so **every simulation to date, including the last one, has tested a static 500 that the rules never described.**

Tested properly, a static 500 does not degrade — it collapses. Levels cost Credits (§26.1: +245 for a full track), and those Credits ride on the fighter. **Crew size vs Level at a fixed cap** (pure arithmetic, no dice):

| Level | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **cap 500** — Line | 3 | 2 | 2 | 2 | 2 | 2 | **1** | 1 | 1 | 1 | 1 |
| **cap 500** — Swarm | 4 | 3 | 3 | 2 | 2 | 2 | **1** | 1 | 1 | 1 | 1 |
| **cap 500** — Gunline | 2 | 2 | 3 | 2 | 2 | 2 | **1** | 1 | 1 | 1 | 1 |
| **cap 500** — Armoured | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **cap 1000** — Line | 6 | 6 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 2 | 2 |
| **cap 1000** — Swarm | 12 | 10 | 8 | 7 | 6 | 5 | 4 | 3 | 3 | 3 | 2 |

**At a frozen 500, every archetype is a single model by Level 6, and below the 3-model legal minimum from Level 1–3 onward.** One fully-levelled fighter costs +245 — **49% of the entire budget** for one fighter's growth. Confirmed in the engine (90,000 games): by L7 every matchup is a 1-model duel.

This is not a balance problem that tuning fixes. **The very growth arc the 500 cap exists to deliver is what destroys the format** — the more successful your campaign, the less of a game you have. At 1000 the same track degrades gracefully (6 → 3 models), which is the anti-snowball valve working as designed rather than a crew evaporating.

### The ramp, derived rather than invented

The cap that keeps a crew the **same size** as it levels, measured per archetype and taken at the maximum:

| Level | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **cap needed** | 500 | 525 | 575 | 650 | 725 | 775 | 925 | 1100 | 1150 | 1225 | **1425** |

Spread at those rungs stays healthy — L0 500 → 36 · L2 575 → 34 · **L5 775 → 16** · L7 1100 → 31 · L10 1425 → 30. The mid-campaign game is the best-balanced point on the whole curve.

Note where this lands: a mature campaign crew needs **~1000–1425**, which is the already-validated standard/pitched band. **The 1000 cap is not the alternative to your 500 — it is where your 500 is supposed to arrive.**

---

## 5 · What does *not* work (tested, rejected)

| Candidate fix | Spread | Floor | Verdict |
|---|:--:|:--:|---|
| **Drop the mandatory Leader** at Campaign Start | **40** *(worse than 35)* | 26% | **Reject.** Swarm balloons to 7 models and Armoured to 4; removing the one expensive compulsory model hands the budget straight to body-count, which is the dominant win driver. |
| **Free founding kit — melee** (scavenged crowbars/sledges) | **54** | 19% | **Reject, emphatically.** It widens the exact gap it was meant to close: Line goes to 5 models and **73%** while Gunline stays at 2 and falls to **19%**. Melee lists convert the saving into bodies; shooters cannot. |
| **Free founding kit — everything incl. rifles** | 24 | 39% | Works, but it is a large power grant that achieves less than simply pricing the rifle correctly. |
| **Stacking the fixes** (Founder + free kit + rifle 70) | **53** | 21% | **Reject.** The levers are **not additive.** Each fix moves the body:gear ratio; stacking three overshoots and re-breaks the game from the other side. |
| **Raise the cap to 625–750** (the previous recommendation) | 25 / 28 | 35% / 32% | **Unnecessary.** No better than 510–550, and it costs more of the small-crew feel for nothing. |

**A cheap "Founder" rank does work** as a Campaign-Start-only alternative if you would rather not touch a global weapon price: Founder at 140 with **1 Order** instead of 2 gives spread **22** / floor **36%** with every archetype legal at a literal 500. Interestingly the *Orders* matter more than the stat points — 9 stat points at 1 Order (22) beat 7 points at 1 Order (25). It is also narratively apt: a founding crew's boss has not earned two Orders yet. Kept as **Option B** below.

---

## 6 · The 2.5D-specific finding: height is compensation for being outnumbered

Rooftop fields the **identical list** to Gunline and differs only in seeking the objective rooftops. The delta:

| | rifle 100 | rifle 85 | rifle 70 | rifle 55 | rifle 40 |
|---|:--:|:--:|:--:|:--:|:--:|
| Gunline | 26 | 43 | 47 | 36 | 39 |
| Rooftop | 36 | 52 | 45 | 47 | 52 |
| **delta** | **+10** | **+9** | **−2** | +11 | +13 |

By cap: **+10** at 500 · +2 at 560 · +8 at 625 · +2 at 750 · +5 at 1000.

**Height is worth roughly +5 to +10 points to a shooting crew, and the benefit is largest exactly when the crew is body-starved.** When the list can afford enough bodies (rifle 70 at 500), roof-camping goes slightly *negative* — standing on a roof costs objective presence, and objectives are how you win. That is the terrain pillar behaving correctly: verticality is a lever for the outnumbered, not a dominant strategy. It is consistent with the engine's earlier finding that roofs net to ~even via exposure.

The delta is **not monotonic** in rifle price (−2 at 70, +11 at 55), which I cannot explain from the data — most likely a crew-size threshold changing what the roof policy does with its activation. Flagged rather than smoothed over.

---

## 7 · Recommendation

### Required — two changes, neither of which is "go to 1000"

**R1 · Write the cap ramp that §16 already promises.** This is the one non-optional change: a frozen 500 cannot host a campaign at any set of prices. The measured curve rounds to a single line of arithmetic:

> **Campaign Start Crew Rating = 500 + 100 × (the highest Level in your crew)**, to a ceiling of 1500.

Check against the derived need: L2 → 700 (needs 575) · L5 → 1000 (needs 775) · L7 → 1200 (needs 1100) · L10 → 1500 (needs 1425). Always ≥ the requirement, monotone, and one subtraction at the table. It runs slightly generous early, which is a feature: the crew grows in **numbers** as well as quality, which is the *"becoming something bigger"* feel doing real mechanical work. **This is also the fix that best serves the stated design goal** — the arc stops being flavour text and becomes the rule that carries the campaign.

**R2 · Reprice `standard_ranged` from 100 to the 70–85 band; suggest 80.** Justified three independent ways (rebuild test 65–95 · derivation from measured atoms ≈80 · the surface sweep, where both 70 and 85 beat 100 on mean spread, mean floor and worst case). It is a **correction to an admittedly unmeasured legacy number**, not a crutch for 500 — which is why it also helps the 1000 game (31 → 28). Apply the `heavy_ranged` cascade (160 → ~140) in the same change, and **re-run the grid at the chosen value** before locking, since 80 is interpolated between two tested points rather than measured at 80.

### Recommended

**R3 · Open at 510–550 rather than exactly 500.** Ten Credits buys a legal three-model shooting crew; 550 measured the best floor (38%) in the fine sweep. If R2 lands, this is optional polish — but it is nearly free and it removes the "one body short" cliff regardless of what happens to the rifle. A founding crew at 550 is still 3–5 models: the feel is intact.

**R4 · Correct `points/ticks.py` armour to 60 / 100.** Already ruled adopted (§15, `List Building`), never applied. It is worth ~10 points of the original 46 on its own, and every future sim inherits the error until it is fixed. One-line change; I did not apply it because it also means editing a `[measured]` annotation, which is your call.

### Option B — if you would rather not touch a global weapon price

**A Campaign-Start-only "Founder" rank: 140 Credits, 9 stat points, 1 Order** (spread 22, floor 36%, every archetype legal at a literal 500). Your founding boss earns their second Order by promotion (§26.5) instead of starting with it. This keeps 500 exactly, changes nothing in Match Play, and is arguably the better *story* — but it leaves the rifle mispriced, which is a real defect independent of the cap.

**Do not combine Option B with R2.** Tested: Founder 120 + rifle 70 at 500 scores **34** — barely better than doing nothing. The levers are not additive.

---

## What this cannot see

Unchanged from the previous pass, and it bounds every number above:

- **Skills are not implemented beyond Tier 1.** `knockback`, `stare_down`, `keep_moving`, `hacker` — all T1. A Specialist's T2 and a Leader's T3 cost Credits here and deliver nothing, so the sim **undervalues** the top two ranks. Any Founder price it endorses is a **floor**, not a final price. It also means levelled crews in §4 were charged full price for part of their power, so those veteran results are **lower bounds**.
- **Greedy crews, not optimised lists.** Every archetype's ceiling is understated, and the quantization documented in §3 is a direct consequence. This is the single biggest methodological weakness in the whole harness; a list *optimiser* rather than a greedy filler would make spread numbers far more trustworthy at small caps.
- **Deployables are excluded** — the costing engine has no price for them.
- **One board, one scenario family.** All four scenarios run on the mirror-symmetric Take-a-Hold board. Terrain density is the most powerful dial in the game (66-point swing) and it is held constant here.
- **Spread is not comparable across harnesses.** ~20–35 here is not the 11-point figure in `Crew Sim — Findings` — different archetypes, builder and scenario mix. Only compare rows within these tables.
- `PACKET-TEST-RESULTS.md`, cited by the master note for T1–T14, **is still not in the repo**; nothing above depends on it.

---

## Reproduce

```
cd test-bench/balance
py -3.13 campaign500_fixes.py 1000 baseline    # the honest 500 baseline
py -3.13 campaign500_fixes.py 1500 capfine     # the 510 legality cliff
py -3.13 campaign500_fixes.py 1000 rifle       # rifle price at a 500 cap
py -3.13 campaign500_fixes.py  800 grid        # the cap x rifle surface (the one that matters)
py -3.13 campaign500_fixes.py 1000 founder     # the Founder rank sweep
py -3.13 campaign500_fixes.py 1000 noleader    # dropping the mandatory Leader
py -3.13 campaign500_fixes.py 1000 freegear    # founding kit allowance
py -3.13 campaign500_fixes.py 1500 combo2      # survivors stacked + the 1000 coexistence check
py -3.13 campaign500_growth.py 3000            # the growth arc: shrink, collapse, ramp
py -3.13 campaign500.py        800 rebuild     # independent rifle pricing
```

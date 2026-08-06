# Review — `Full Rules System v1`

**Reviewed 2026-08-05** against the live vault (`Rules System/`), the costing engine (`test-bench/points/`), `docs/POINTS-DECISIONS.md`, and a fresh sim run (`docs/CAMPAIGN-START-500-FINDINGS.md`).

**Verdict: adopt it.** It is the first document in this project that holds the whole game in one place, it is honest about its own provenance (`[NEW]` / `[DRAFTED]` / `[SIM-CONFIRMED]` / `[SIM FLAG]` tagging is doing real work), and it closes several gaps that had been open for weeks — Downtime existed nowhere before §25.5, and the Fate table had pointed at scar content that had never been written since it was drafted.

The findings below are things to fix inside it, not reasons to hold it back. Ordered by how much they'd cost to get wrong.

---

## A · Blocking — a rule was verbally changed and the document still carries the old version

**§14 vs §16, on whether a skill needs a matching stat.**

§14 states the core rule unchanged: *"A stat hands you a skill every time it reaches a tier… a stat at +4 grants both its T1 and T2 skill; at +6, T1+T2+T3."* §16's Campaign Start table hands each rank a flat skill at its tier — Leader **1× T3**.

Those cannot both hold. Under §14, a T3 skill requires a **+6** stat, which spends **6 of a Leader's 9 points**. Every Campaign Start Leader would be forced into +6/+2/+1, and every Specialist into +4/+2/+1 — build variety at the top two ranks disappears entirely, and it would be a silent, load-bearing constraint that neither section states.

You already ruled on this directly: *"skills don't need a matching stat anymore… Players can give their starting crew whatever stats they want."* **The document was not updated to match.** §14 needs the decoupling written into it, or §16 needs the stat gate spelled out.

Two consequences that follow from your ruling and are also unwritten:
- **§13's tier caps** (Fighter 2×T1, Specialist 1×T2·2×T1, Leader 1×T3·2×T2·4×T1) exist to force stat spread. If stats are now free, say whether the caps survive. Your answer says free; §13 says capped.
- **§26.1's Secondary** is defined as *one* named stat — "the next-highest" — and Levels 1/4/8 all feed it. Your phrasing was *"everything else are secondary stats."* One Secondary makes a narrow fighter; any-secondary makes a broad one. That is a real difference over ten Levels.

---

## B · The Campaign Start prices refund a cost that was never charged

§16 derives the Campaign Start column by subtracting skill values (T1 20 / T2 35 / T3 55) from the Match Play column. But the Match Play column never contained a skill charge. Every entry is exactly the body formula in `points/ticks.py`:

```
body = 20 (base) + 15 per stat point + Order premium (0 / 0 / 40 / 90)

Recruit     20 + 45 +  0 =  65 ✓      Specialist  20 + 105 + 40 = 165 ✓
Fighter     20 + 75 +  0 =  95 ✓      Leader      20 + 135 + 90 = 245 ✓
```

Skills contribute **zero**, which is correct and deliberate — `POINTS-DECISIONS` **D22** ("skills are measured but never charged") and **D27** ("a skill carries no separate cost of its own, in the same way a scar carries no rebate"). Subtracting a skill's value from a price that never included it discounts the same fighter twice.

Read strictly against your own decisions, a Campaign Start crew should cost **65 / 95 / 165 / 245** and simply be *worse* — fewer skills as a pure nerf, exactly how Scars were ruled. If instead skills should be priced into the rank bundle now that they no longer ride the stat line, the ladder is **65 / 115 / 200 / 300**. Both are defensible. The current column is neither.

**The Leader also fails the document's own arithmetic.** §16 lists Match Play Leader skills as *"~4 (1×T3 + 2×T2 + rest T1)"*. Keeping only the T3 removes 2×35 + 20 = **90**, so 245 − 90 = **155**, not the **170** printed. Fighter (95−20=75 ✓) and Specialist (165−40=125 ✓) both reconcile; the Leader is 15 Credits adrift.

---

## C · The sim disagrees with the 500 cap — and the ladder isn't the fix

Full data in `docs/CAMPAIGN-START-500-FINDINGS.md`. Six rank ladders spanning a 4× range in body cost, 30,000 games each:

- **No ladder balances at 500.** Spread never fell below 21 points, and the only ladder that reached it did so by shrinking every crew to two models.
- **A shooting list cannot be built.** Gunline wins **18%**. Leader+rifle (270) + Fighter+rifle (175) = 445, and the cheapest third body is 65 — **a rifle-armed Leader puts the crew below §16's own three-model minimum.**
- **The cap is the lever, not the prices.** Holding the ladder fixed: 500 → 46-point spread · **625 → 32** · 750 → 32 · 875 → 37 · 1000 → 36. The penalty is specific to 500 and gone by 625.
- **The mandatory Leader is 34%** of a 500 crew, against 24% at Match Play. Halving the budget while keeping one compulsory copy of the most expensive model in the game is what breaks it.

Recommendation: raise the Campaign Start cap to **625–750**, or cut the Leader's price specifically. Both untested as fixes.

---

## D · Armour — the document is right and the engine is wrong

§15 prints Light **60** / Heavy **100**. `points/ticks.py` carries **30 / 60**, marked *[measured]*. A 2× gap on every armoured fighter, and unresolvable on paper: `POINTS-COMPLETION-PLAN.md` M2 records that `balance/armourprice.py` — cited as the source by both `ticks.py` and `POINTS-TABLE.md` §7 — **does not exist in the repo**.

Swapping only these two numbers, 30,000 games per side: at **30/60** the Armoured crew wins **64%** and is the best list in the game; at **60/100** it wins **51%** and the whole field tightens by 9 points. **The document's number is better. `ticks.py` is owed the correction.** Caveat: measured at a 500 cap only, and at 60 the Armoured crew drops to two models, so some of the fall is affordability. Repeat at 1000 before locking.

---

## E · Smaller price conflicts with the engine

§15's class table was described as *"reconciled to the 1000-Credit scale"* but two rows track the older vault table rather than the engine:

| Row | §15 | `points/ticks.py` | Note |
|---|:--:|:--:|---|
| **Thrown** class | 20 | **40** | straight disagreement, unexplained |
| **Heavy Ranged** class | 140 | **160** | engine removed the welded-on Cumbersome drawback (2026-07-30) — §15's 140 predates that and still nets the −20 refund |

Neither is large, but both feed every built weapon in those classes.

---

## F · Things the document gets right that are worth not losing

- **The Match Play / Campaign Start split is the right idea.** A one-off crew and a crew built to grow genuinely are different fighters, and pricing them from one table was always going to distort one of them.
- **§26.1's fixed Level track** is a real improvement on freeform Advances: it removes the optimise-every-advance homework without removing choice (roll-3-choose-1 on skills keeps the interesting part).
- **Flagging its own weak numbers is doing its job.** The +1 WND price at 45 Credits is called out as having zero data behind it; the stat-point underprice (16–34 measured vs 15 charged) is carried forward rather than quietly dropped. Keep that discipline.
- **Closing Downtime (§25.5) is the biggest single gap closed.** Three other sections had been referring to a "Settlement Phase" that was never written.

---

## G · Owed follow-up work

1. Resolve **A** — it is a rules contradiction, not a wording problem.
2. Pick a Campaign Start ladder on one consistent principle (**B**), then re-run `campaign500.py`.
3. Rule the cap (**C**) — 500, or 625–750.
4. Correct `ticks.py` armour to 60/100 (**D**) and rebuild `balance/armourprice.py` so the number can be re-derived by someone other than the person who set it.
5. Rule Thrown and Heavy Ranged (**E**), then rewrite the vault's `Weapons.md` cost tables — they are still entirely on the retired 100-point scale and currently carry a ×10 conversion banner instead of real numbers.
6. **§24 Factions** claims to supersede the vault's `Factions.md`, but the two rosters only partly overlap and the vault's version is your own writing. It is flagged in-place rather than overwritten; it needs your call on which roster is canon.
7. **Milestone 5 (skills) is still the keystone and still blocked.** Only four skills are implemented in the engine, all Tier 1, so 20/35/55 remain estimates — and those three numbers are load-bearing for every calculation in **B**.

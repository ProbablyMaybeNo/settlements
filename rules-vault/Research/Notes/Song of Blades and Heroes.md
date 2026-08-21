---
type: research-note
title: Song of Blades and Heroes
game: Song of Blades and Heroes
publisher: Ganesha Games
designer: Andrea Sfiligoi
depth: official cost chart, formula derived and verified 34/34
tags: [settlements/research]
---
# 🎲 Song of Blades and Heroes

> [!abstract] In one breath
> A small-model-count skirmish game whose entire unit costing is a **published two-axis lookup table** — and whose underlying formula is fully recoverable from it. **The closest published analogue to Settlements**, and the cleanest solution anywhere to "the same ability is worth more on a better model."

| | |
|---|---|
| **Designer · publisher** | Andrea Sfiligoi · Ganesha Games |
| **Status** | Cost chart published as an official PDF; the formula is **not** stated but is fully recoverable |
| **Depth of read** | Formula derived, **validated 34/34** against transcribed cells *and* all three publisher worked examples |
| **Long-form** | `docs/POINTS-RESEARCH.md` §1.2 |

---
## The Quality multiplier

**Type:** Costing · **Take:** ⭐ steal — the highest-value transfer in the corpus

```
Cost = round( (5 × Combat + Σ SpecialAbilityPoints) × (7 − Quality) / 2 ),  minimum 1
```

**[FACT — chart published; formula derived and validated]** The publisher's own examples all reproduce exactly:

| Publisher's example | Computation | Result |
|---|---|---|
| *"Q5, C2, no Special Abilities = 10 points"* | (10 + 0) × 1.0 | **10** ✓ |
| *"Q3, C3 with 7 points of Special Abilities = 44 points"* | (15 + 7) × 2.0 | **44** ✓ |
| *"Q2, C2 with 15 points of Special Abilities = 63 points"* | (10 + 15) × 2.5 → 62.5 | **63** ✓ |

The Quality multiplier is exactly `(7 − Q)/2`: **Q5 → ×1.0 · Q4 → ×1.5 · Q3 → ×2.0 · Q2 → ×2.5.**

**Why this structure is right.** In SoBH, **Quality is the activation roll — it governs how many actions you get.** Because actions multiply everything a model can do, Quality multiplies **the entire cost, including every special ability.** A Stealth ability (3 SA points) costs **3 on a Q5 militia and 7.5 on a Q2 hero, automatically, with no separate table.**

> **This is the cleanest published solution anywhere to "the same ability is worth more on a better model."** A Board Game Designers Forum thread states exactly this problem — *"Regular troops and hero units often have access to the same power-up, but have to pay different amounts for it"* — with no solution offered. SoBH solved it with one multiplier.

**The Special Ability list is flat and published** (selected) **[FACT]**: Slow −5 · Animal, Short Move −3 · Coward, Dogged, Greedy, Protect, Stubborn −2 · Bodyguard, Evil, Solar Force, Standard Bearer, Were **0** · Shieldwall 1 · Ghost Blade, Mountaineer, Paladin, Shooter (Short) 2 · a large 3-point band (Acrobat, Fearless, Heavy Armor, Lethal, Poison, Stealth, Swarm, Undead…) · Berserk, Sharpshooter, Shooter (Medium) 4 · Huge, Magic Resistance, Reckless 5 · Mounted 6 · Shooter (Long) 7 · Beastmaster, Drain, Running Blow 8 · Champion, Gargantuan 9 · Bard, Combat Master, Flying, Long Move, Shield-Mage 10 · Distract, Teleport 12 · a 15-point band (Assassin, Blast, Hero, Leader, Magic-User, Terror, Tough…) · Immortal 20.

Three decisions visible in that list:

- **Ranged reach is a stepped, accelerating ladder** — Shooter Short **2** / Medium **4** / Long **7**. The steps accelerate (2 → +2 → +3), correctly reflecting that reach compounds with mobility.
- **Pure-flavour abilities are explicitly priced at 0** (Evil, Standard Bearer, Were, Solar Force). **A zero price is a legitimate, published answer** for things that are narrative rather than mechanical.
- **Negative traits refund**, with the biggest refund (−5, Slow) on the one that costs you tempo.

**For Settlements — what to take.**

1. **`(additive core) × (activation multiplier)`** as the top-level shape. Our own arithmetic agrees this is required: at a baseline model, **one extra attack per turn is worth 81% of everything else the model could ever buy** (`docs/POINTS-RESEARCH.md` §4.5), and our `Skill Sim — Findings` independently measured **Quick Shot at +24 win%** — the largest single-skill swing in the game. **[INFERENCE + our own measured result, in agreement.]** Note that our answer so far is to **gate** extra actions by rank rather than price them — which is the safer version of the same finding.
2. **Ability prices as a single flat list**, scaled automatically — so we never maintain per-rank ability tables in [[Skill Paths]].
3. **A stepped, accelerating price ladder for range**, not a linear per-inch price. Directly relevant to [[Weapons]] range bands and the 24" ceiling.
4. **Zero-cost flavour traits as an explicit category.** We have nowhere to put a trait that's pure character. This is where it goes.

**The known weakness** **[INFERENCE from the list structure — no published critique quantifies it]**: a 3-point band lumps together things of quite different value (Stealth, Heavy Armor and Poison are not really equal). **The granularity of the ability list is coarser than the formula deserves** — which is an argument for our 1000-point scale, not against the structure.

**Verdict** **[CONSENSUS]**: well regarded as light and fast, and the formula is why it supports thousands of user-created warbands across dozens of settings. The publisher ships a warband-builder app — **a strong signal that a formula this simple still wants tooling**, which is what `test-bench/points/` is for.

---
## Source

- Primary: official SoBH cost chart PDF + publisher worked examples
- Long-form: `docs/POINTS-RESEARCH.md` §1.2, §1.4, §4.5
- Related: [[Wargaming Research Hub]] · [[One Page Rules]] (the same insight, different implementation) · [[BattleTech]] · [[Skill Paths]] · [[Weapons]]

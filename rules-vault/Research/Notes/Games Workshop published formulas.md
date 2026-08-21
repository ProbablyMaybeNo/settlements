---
type: research-note
title: Games Workshop published formulas
game: Rogue Trader / 40k VDR / Warhammer Fantasy / Battlefleet Gothic / Epic
publisher: Games Workshop
depth: archive scans; one modifier graphic unreadable in both OCR passes
tags: [settlements/research]
---
# 🎲 Games Workshop's published formulas

> [!abstract] In one breath
> **GW's public "we don't use a formula" line is false twice over.** They published two complete atomic costing engines — both as *player-facing construction kits*, never as an account of their own internal costing — plus a semi-official third. The oldest of them identified and patched the super-linearity problem **in 1987**.

| | |
|---|---|
| **Publisher** | Games Workshop |
| **Depth of read** | Archive scans, verified verbatim where legible |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.9 |

---
## Rogue Trader, 1987

**Type:** Costing · **Take:** ⭐ steal the fix

A published formula, **verified verbatim against two archive scans**: additive per-characteristic deltas from a human baseline (**human = 5 points**), then a non-linear multiplier band, then flat equipment. **[FACT]**

The crucial admission, in GW's own words:

> *"Values worked out from the formula given above tend to **undervalue the larger creatures**. To compensate for this a modifier is applied to any creature whose points value works out greater than 10."*

Bands: 11–15 **×1½** · 16–20 **×2** · 21–30 **×3** · 31–40 **×4** … 91–100 **×10**.

> **Games Workshop identified and patched the super-linearity problem in 1987 and printed the fix.**

⚠️ **[CONSENSUS, not FACT]** The per-characteristic modifier table is a graphic **destroyed in both OCR passes**; the circulating community transcription could not be verified. **The method is published fact; the individual modifier numbers are not.**

**For Settlements.** The failure mode is real and universal — a purely additive system undervalues a model that stacks many small advantages, because the advantages interact. Three independent systems reach for the same fix: this band, [[One Page Rules#The stat ladder doubles at the top]]'s 8→16 doubling, and [[The Walking Dead All Out War#The published formula, and its confession]]'s escalating per-die ladder. **Ours is the ±3 modifier cap and the stat max of +6 — a hard cap where they used a rising price.** Worth knowing that both work and that ours is the cheaper one to explain.

---
## The Vehicle Design Rules

**Type:** Costing · **Take:** ⭐ steal

*(Jervis Johnson, White Dwarf 251 / Chapter Approved 2001.)* A full published formula **[FACT]**:

1. Buy armour per facing.
2. **The sum of all four facings becomes a scalar budget (36–56) that simultaneously gates hull class, speed class, and the open-top modifier.**
3. Add weapons from **race-specific** charts.
4. Apply percentage upgrades — Gun Battery **+50%**, Shorter Barrel **−25%**, Slower Rate of Fire **−25%**, Titan-Killer **+50%**.

**And weapons are priced by race AND by Ballistic Skill**: Heavy Bolter **+20 at BS4 / +15 at BS3**; Lascannon **+35 / +25**.

> **The same gun costs more on a better shooter. That is the cleanest published solution to platform-dependence found anywhere.**

Step 2 is the underrated one: **one number derived from your defensive spend then gates three unrelated things.** It stops the "heavily armoured *and* fast *and* open-topped" build without a single restriction rule.

**For Settlements.** Platform-scaling is the same finding as [[Infinity#SWC — the derived second budget]] (SWC rises with the carrier) and [[One Page Rules#Quality adds, then multiplies]] (weapon cost × Quality). **Three systems, three implementations, one conclusion: DEX should scale the weapon's price in our engine, not sit beside it.** See `test-bench/points/` and [[Weapons]].

---
## Abuse priced in painting labour

**Type:** Production · **Take:** ⭐ steal — the funniest thing in the corpus, and it works

The VDR's anti-abuse governor is **not mathematical** **[FACT]**:

> *"It is VITAL that people using the VDR obey 'The Most Important Rule', which is that in order to use a vehicle created with the VDR it MUST be represented by a **PAINTED WYSIWYG MODEL**."*
>
> *"Almost all of the arguments I've seen for unlikely 'game-winning' vehicles fall down on the fact that the author is clearly never going to be able to produce a painted wysiwyg model."*

> **Jervis Johnson priced abuse in painting labour.**

It was still exploitable ("Gatling Lascannon Skimmers"), and when GW revived VDR in 2018 it was restricted to **Open Play only** — the same quarantine move as [[The Walking Dead All Out War#The published formula, and its confession]].

**For Settlements.** We are **miniatures-agnostic**, so WYSIWYG isn't available to us as a governor — but the *principle* transfers: **a construction kit needs a non-mathematical brake somewhere.** Ours are the rank gates and the hard caps. Worth being explicit that they're doing this job, and worth noting that **quarantining the kit to friendly play is a shipped, respectable answer** if the maths can't close.

---
## Warhammer Fantasy — GW ran a formula while denying it

**Type:** Costing · **Take:** 📎 reference

No published formula, but a community reconstruction that **validates**: it ships a **16-row residuals table** of GW-published versus computed values — Goblin 2.5/2.5 · Orc 5.5/5.5 · Minotaurs 40/40 · Clanrats 6/6 · Chaos Warrior 24/24.5 · Trolls 65/66.5 · Black Orc 9/10 — **most exact, worst error ~7%.** Structure: human baseline PV 5, per-characteristic deltas, **M > 6 doubles the whole value**, characters = base **×5 (Champion) / ×13 (Hero) / ×20 (Lord)**. **[CONSENSUS — but the strongest evidence anywhere that GW was running an internal formula while denying it.]**

**For Settlements.** The **residuals table** is the transferable artefact, not the formula. **Publishing computed-vs-adopted side by side is how you prove a derivation is real** — and it makes every deliberate deviation visible as a deviation rather than an error. Directly applicable to `docs/POINTS-TABLE.md` and the costing engine.

---
## Battlefleet Gothic

**Type:** Costing · **Take:** ⚙️ adapt

GW's non-use is explicitly documented in the community formula's own introduction: *"Games Workshop themselves used absolutely no 'points formula' for creating their ships."* The semi-official **Smotherman Formula** (published in GW's own *BFG Magazine #2* but *"never made official"*) is purely linear-additive — Hits 5 · Shields 10 · Turrets 5 · Weapons Battery at 30/45/60cm = **1.5 / 3 / 4.5** per Strength (exactly ×1/×2/×3).

**The interesting part is faction identity as override layers**: Eldar **double** their Hits cost, **double** their speed cost, and pay a **+15 *"too many weapons on too small a ship"*** surcharge. **[FACT]**

**For Settlements.** A fourth place to write [[Factions]] identity — one shared formula, per-faction multipliers on top. Cheap to implement in `test-bench/points/`, and it means a faction's flavour is enforced by the price list rather than by rules text.

---
## Epic — the negative result

**Type:** Costing · **Take:** ⚠️ the clearest argument against atomic costing anywhere

**[FACT]**

> *"Applying points costs in Epic is more of an art than a science."*
>
> *"It's to do with the way the attributes of a unit fits in **both with any formation it belongs to and with that formation's place in an army**."*

Points attach to **formations in army context**, so unit cost is **not separable** from what it's bundled with.

> **If your units are only meaningful inside a container, cost the container.**

**For Settlements — the honest self-check.** Our units are *mostly* separable — a fighter is a fighter regardless of the crew around it. But three things push toward container-costing and are worth watching: **Orders** (a Leader's value depends on who can receive them), the **rank pyramid** (a Specialist requires two lower-rank bodies, so its real cost includes theirs), and **crew synergy** generally. If a costing pass keeps producing residuals that only make sense at the crew level, that's this finding arriving — see [[Balance]] and `docs/POINTS-AUDIT.md`.

---
## Source

- Primary: Rogue Trader (1987) archive scans; WD251 / Chapter Approved 2001 VDR; *BFG Magazine #2*; NetEA statements
- Long-form: `docs/POINTS-RESEARCH.md` §7.9
- Related: [[Wargaming Research Hub]] · [[Warhammer 40000]] · [[Kill Team]] · [[One Page Rules]] · [[Infinity]]

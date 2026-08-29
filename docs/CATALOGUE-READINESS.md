# Settlements — Catalogue Readiness

*What each catalogue needs before it can go on a board. Built 2026-08-29 from
`docs/CATALOGUE-MASTER.md` and the shipping standard in `docs/POINTS-CATALOGUE.md`.*

Every catalogue is checked on the same four axes:

| | Check | Passes when |
|:--:|---|---|
| **D** | **Drafted** | The rules text is complete — no TBD, no "parked", no forward reference to a note that doesn't exist. |
| **N** | **Enough items** | Enough entries that a player has a real choice, and the archetypes the game claims to support can actually be built. |
| **$** | **Costed** | Every entry has a price **and a confidence tier**. Per `POINTS-CATALOGUE`: *"No number ships untagged."* A C-tier price is fine; an untagged one is the defect the rebuild existed to remove. |
| **B** | **Board-ready** | The thing has a defined physical representation — a token, a card, a footprint, a marker — in `Board Representation`. |

> **The costing bar, verbatim.** **A** = measured, current, significant · **B** = measured
> but wide CI or single-scenario · **C** = derived by rule from an A/B atom, with the
> derivation written down. Untagged is not a tier, it's a bug.

---

## The matrix

| Catalogue | Items | D | N | $ | B |
|---|:--:|:--:|:--:|:--:|:--:|
| Weapon classes | 8 | ✅ | ✅ | ⚠️ | ✅ |
| Weapon characteristics | 18 | ✅ | ✅ | ✅ | ✅ |
| Weapon drawbacks | 5 | ✅ | ✅ | ❌ | ✅ |
| Attack Dice | 3 | ✅ | ✅ | ⚠️ | ✅ |
| Armour | 3 | ✅ | ✅ | ✅ | ✅ |
| Hacking gear | 2 | ✅ | ⚠️ | ✅ | ✅ |
| Equipment | 4 | ✅ | ❌ | ✅ | ⚠️ |
| Deployables | 24 | ✅ | ✅ | ❌ | ✅ |
| Structures | 23 | ✅ | ✅ | ❌ | ✅ |
| Skills | 150 | ✅ | ⚠️ | n/a | ✅ |
| Conditions | 29 | ✅ | ✅ | n/a | ✅ |
| Terrain | 6 + 6 | ✅ | ✅ | n/a | ✅ |
| Scenarios | 5 | ✅ | ✅ | n/a | ⚠️ |
| Faction rules | 0 | ❌ | ❌ | ❌ | n/a |
| Chems | 0 | ❌ | ❌ | ❌ | ❌ |
| Drones | 0 | ❌ | ❌ | ❌ | ❌ |
| Ambush | — | ❌ | n/a | n/a | n/a |

✅ ready · ⚠️ gap worth closing · ❌ blocking · n/a not costed by design

**The headline: costing is the weakest axis, not drafting.** Four catalogues are
fully drafted and completely untagged — and two of them, Deployables and
Structures, don't even have a Tier column to put a tag in.

---

# 🔴 Blocking — a catalogue you cannot put on a table

## Deployables — 24 entries, 15 with no price at all, 0 with a tier

The single worst-costed catalogue in the game. It has **no Tier column**, so even
the nine entries that *do* have a price are shipping untagged.

- [ ] **Add a Tier column** to all four family tables (Turrets, Chassis, Payload, Traps, Beacons). **[Build] S**
- [ ] **Tag the 9 priced entries** — Autoturret and Sniper Turret are engine rows so they can carry a real tier; the rest are derivations and need theirs written down. **[Build] S**
- [ ] **Price the 4 remaining traps** — Spike Strip, Covered Pit, Leg Clamp, Razor Barrier. **[Build] S** — derivable now by the engine's own stated rule, blocked on nothing.
- [ ] **Price the 5 remaining beacons** — Targeting, Aegis, Cover, Cleansing, Dread. **[Build] S** — an aura prices at the atom it grants, held under the gear:body cap.
- [ ] **Price the Remote chassis + 5 mine payloads.** **[Build] S** — *blocked behind the payload ruling in Gate A.* Three mine payloads mirror traits that currently measure ≤0, so pricing them first bakes the defect into a second catalogue.

## Structures — 23 entries, and the axis they're priced on is not computable

No confidence-tier column either. *(`Structures.md` does use the word "Tier", but
for **HQ upgrade tiers** — a different axis entirely. Don't mistake one for the
other when adding the column.)* Worse, `POINTS-CATALOGUE` §5 lists the **Materials
axis as engine-blocked**: D23 prices structures by payback, and *the denominator — the base
gatherer rate — is stated nowhere.* Every Materials number rests on it.

- [ ] **State the base gatherer rate.** **[Ross] S** — this is one number and it unblocks the whole axis. Until it exists, no structure price can be tiered above C, and the payback derivation cannot be written down.
- [ ] **Add a confidence-tier column** and tag all 23. **[Build] S** — after the rate exists. Name it distinctly (`Conf.`) so it cannot be read as an HQ upgrade tier.
- [ ] **Confirm the provisional numbers** flagged first-draft: HQ tiers (110/195), Med-bay, Mess Hall. **[Ross] S**

## Faction rules — the framework forbids things but nothing fills it

- [ ] **Write one playstyle-defining rule per faction, with numbers.** **[Ross + Build] M** — "Improved Build test for field deployables" doesn't say by how much. The framework already bars flat stat bonuses, matched drawbacks and exclusive unlocks, so the shape is constrained; what's missing is the content.
- [ ] **Lock the faction names.** **[Ross] S** — the `Ideas Inbox` set (The Veterans · First Responders · The Watch · The Union · The Syndicate · The Wyrm) is flagged in `Factions.md` itself as the strongest candidate.
- [ ] **Decide the count.** **[Ross] S** — the superseded interview script said 5 factions + 10 locations. That number has never been re-confirmed against the current framework.

## Chems — a mechanic with maths and no content

- [ ] **Write the catalogue.** **[Build] S** — the Dependence maths is sim-confirmed (1.55 clean uses at NRV +0, 3.02 at NRV +4). There is no list, no prices, no effects.
- [ ] **Agree a target count.** **[Ross] S** — *proposed, needs your tick:* **6–8**, one per axis the game already tests (a combat stim, a nerve steadier, a movement boost, a pain-killer that ignores Shaken, a focus drug for INT, a stealth suppressant). Every entry modifies a roll that already exists — no new subsystem.
- [ ] **Price them off the measured stat ladder.** **[Build] S** — a temporary +1 to a stat is a fraction of the permanent rung, so these derive C-tier cleanly.
- [ ] **Give them a token or card.** **[Build] S** — nothing in `Board Representation` covers a consumable.

## Drones — Bandwidth is ruled, the Drone Bay is built, the unit doesn't exist

- [ ] **Write drone profiles.** **[Build] M** — this is the 2051 setting's signature unit type and it has one paragraph.
- [ ] **Agree a target count and shape.** **[Ross] S** — *proposed:* **3–4** (a recon spotter, an attack drone, a protective swarm, a carrier/relay). Bandwidth already gates how many you can run.
- [ ] **Decide whether a drone is a unit, a deployable, or equipment.** **[Ross] S** — this decides which catalogue it lives in, which costing path it takes, and whether it activates. Nothing downstream can start until it's answered.
- [ ] **Board representation.** **[Build] S**

## Ambush — resolution is fully tuned and nothing can trigger it

- [ ] **Define the action, skill or gear that attempts an Ambush.** **[Ross + Build] M** — the mechanic cannot be tested because it cannot be reached. It also gives **Quiet** a job; Quiet currently prices C-tier and is explicitly engine-blocked for want of a noise system.

---

# 🟠 Gaps worth closing before the table

## Equipment — four lines, and one of them is a pointer

The weakest catalogue by breadth. Med-Kit, Breach Kit, Exploit Suite, and "a
deployable". Everything else a fighter carries is a weapon.

- [ ] **Widen to 12–16 entries.** **[Build] M** — the rule that keeps it honest: every entry must modify a roll you already make, apply a condition you already define, or open a terrain verb you already have. Your own note points the way — *armour sets that stop conditions: "fireproof", "hazmat"*.
- [ ] **Confirm the carry limit still works at that size.** **[Ross] S** — two equipment slots for everyone. If the catalogue triples, two slots is a much tighter choice than it is today. The rank-slot idea (Leader 4 / Specialist 3 / Fighter 2 / Recruit 1) is already on the table and would land naturally here.
- [ ] **Board representation for carried gear.** **[Build] S** — `Board Representation` has no entry for equipment.

## Weapon classes — 8 classes, no Tier column

The class row's "cheapest build" is a real price and carries no tier.

- [ ] **Tag the 8 class floors.** **[Build] S** — these derive from the measured damage step, so the derivation is short and they land B or C honestly.

## Weapon drawbacks — 5 refunds, none tiered

A refund is a price with a minus sign. Short Range, Slow, Unstable, Cumbersome and
Single-Use all shift a weapon's cost and none carries a tier.

- [ ] **Add a Tier column to the drawbacks table and tag all 5.** **[Build] S**
- [ ] **Re-derive Slow if you take the "attacks last" rewrite.** **[Ross] S** — "attacks last" bites in every melee where "cannot charge" only bites if you wanted to charge, so the refund would have to grow.

## Attack Dice — priced in the rules, invisible to the engine

- [ ] **Add Attack Dice to the costing engine.** **[Build] M** — 40/65 exists in two notes and nowhere in `test-bench/points/`. No sim can validate it and no costed roster can legally include it. *Weigh the known trap first:* `ticks.py` is downstream of the harness, so a write-back marks every artefact stale on `cost_table` while changing nothing measured.
- [ ] **Re-run the auto-include check against real catalogue weapons.** **[Build] S** — the original benchmark used a Heavy Ranged at its **+3 floor** against the **draft** price. Corrected, the margin is +24%, not +51%.

## Hacking gear — two entries, both C-tier and both flagged

- [ ] **Decide whether two is enough.** **[Ross] S** — Breach Kit +1 and Exploit Suite +2 is a ladder with no third rung and no sidegrade. Hacking is one of the three pillars; it has less gear than armour.
- [ ] **Measure the INT ladder.** **[Build] M** — both prices are explicitly *"retained pending a measured INT ladder"*, and INT is worth nothing in a scenario with no claim step.

## Skills — 150 entries, ~141 unmeasurable

Skills are **never charged Credits** (D22/D27), so the `$` axis genuinely doesn't
apply — rank buys the tier slots. But the breadth is a lookup problem.

- [ ] **Cull toward 6–8 verbs per tier.** **[Ross + Build] M** — 10 per tier per stat, perfectly even, is a sign of filling quotas rather than finding verbs. Merge the known twins first: Knockback / Heavy Impact, Ghost Blade / Balanced.
- [ ] **Resolve the three flagged conflicts.** **[Ross] S** — Long Barrel is dead, and the two overlaps above.
- [ ] **Fix the Wrecking Crew / Trapper collision.** **[Ross] S** — each is both a Deed and a skill.

## Scenarios — five exist, one carries the whole catalogue

- [ ] **Re-measure at least one atom on a non-`hold_claim` scenario.** **[Build] M** — every price in the game was measured on the most static of the five. Static and defensive atoms will read high; mobility, tempo and stealth will read low. You do not need all five — one mobile scenario tells you which way the bias runs.
- [ ] **Write the three scenario sheets.** **[Build] M** — Take a Hold, Raid, Sabotage.

---

# 🟢 Ready, or nearly

- **Weapon characteristics (18)** — every entry tier-tagged, five explicitly BLOCKED and correctly marked as not legal to buy. This is the catalogue every other one should look like.
- **Armour (3)** — tiered B, measured directly with zero prior, drawbacks cut.
- **Conditions (29)** — complete and grouped by clock. Needs the summary sheet, not more content.
- **Terrain (6 types + 6 hazards)** — complete, and the density band is the game's most validated number.
- **Structures, Deployables, Terrain, Objectives, Conditions** all have board representation defined.

---

## What I'd do first

**One number, then two columns, then the empty shelves.**

1. **The base gatherer rate** — one ruling from you that unblocks the entire Materials axis and 23 structure prices.
2. **Tier columns on Deployables and Structures**, then tag everything. Mechanical, and it moves two catalogues from "untagged" to "shipping standard" without a single new price.
3. **The 9 derivable deployable prices** — traps and beacons, blocked on nothing.
4. **Equipment to 12–16** — the biggest single gain in player choice per hour spent.
5. **Chems and Drones** — but decide the drone's *category* first, because it changes which costing path it takes.

Everything above is drafting and costing work. The one item that is genuinely a
design question is **Ambush**, and it is worth doing because it is the only thing
that turns Quiet, Hidden and the whole stealth axis from prose into play.

---

*Counts pulled from `docs/CATALOGUE-MASTER.md`, regenerable with
`py -3.13 scripts/build_catalogue_master.py`. Costing standard from
`docs/POINTS-CATALOGUE.md` §"How to read a price" and §5.*

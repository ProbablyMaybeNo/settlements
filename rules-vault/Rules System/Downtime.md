---
type: rule-phase
phase: "22"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 22
depends_on: ["Campaign", "Settlement"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s4]
---
# 22 · Downtime
> **S4 Settlement & Campaign** · status **Drafted** · build order **22**

**Depends on:** [[Campaign]], [[Settlement]]
**Feeds into:** —
**Raw dependency (from Notion):** Campaign, Settlement

## Focus
Between-battle actions that turn the campaign into meaningful decisions — scout, train, craft, build.

The Rules column should nail down:
- The downtime action menu and how many actions a crew gets per cycle.
- Each action's effect: scout (intel / pick next scenario), train (XP/skills), craft (gear/tech), build (settlement), heal/recover.
- How downtime sequences against the campaign turn, plus any costs or risks.
- How solo and co-op players resolve downtime.

## Working rules / decisions

*Drafted 2026-08-05 in [[Full Rules System v1]] §25.5. Everything in [[Structures]], [[Settlement]] and [[Progression]] that referred to a "Settlement Phase" was assuming this sequence existed before it was ever written.*

Every cycle between battles runs three phases, **in order**. Nothing in Workers or campaign persistence happens outside this sequence.

### Phase 1 — Post-Battle
Resolved the moment a battle ends, before anything else.
1. **Survival.** Check every fighter against the **Safe** rule ([[Campaign]]): still standing with the crew, left via a friendly edge, or ending in base contact with a friendly needs **no roll**. Everyone else rolls the Fate table, resolving Captured or Hardened on the spot.
2. **Level-ups.** Apply every qualifying trigger from the battle just played — kills, Glorious Deeds, surviving, objectives held — to each survivor, subject to the **6-source soft cap**. Anyone crossing a Level resolves it now ([[Progression]]).
3. **Bank Resources.** Add the battle's Credits and Materials, capped by storage.

### Phase 2 — Settlement
Follows immediately once Phase 1 is fully resolved. This is where the settlement itself moves.
- **Build & upgrade structures** against the catalogue ([[Structures]]).
- **Assign or reassign workers.** Reassigning ends the old benefit *immediately*; the new one starts producing next Settlement Phase, never retroactively.
- **Assign Power** across powered structures, respecting each one's draw. Anything left unpowered is **Disabled** until covered.
- **Resolve worker Proficiency gains** for every assigned worker.
- **Resolve pending Captured decisions** — Ransom or Brainwash attempts due this phase.
- **Resolve third-Scar retirement decisions.**
- **Dispatch actions** — one per HQ tier (HQ I = 1 · II = 2 · III = 3). Two types exist in v1:
	- **Scout** — reveal a chosen territory's Twist or hidden Side Objective before a battle is fought there.
	- **Scavenge** — roll that territory's Loot table for a small Credits/Materials gain, no battle needed.

	*Sabotage-by-dispatch is deliberately **not** in v1: wrecking a specific structure needs the planted-charge mechanic, which needs a raid. Dispatch stays light and non-combat, and the interesting sabotage decision stays on the table, literally.*

### Phase 3 — Battle Prep
Immediately before the next battle.
1. **Choose the territory**, and therefore the scenario from its card ([[Territory]]).
2. **Set the Crew Rating cap** for the format — standard 1000 · raid 750 · pitched 1500 ([[List Building]]).
3. **Build the roster** — which owned fighters to field within housing, equipped within the Rating cap.
4. **Resolve setup-time bonuses** — Faction battlefield rules, Location founding benefits, territory-card modifiers.
5. **Roll the Twist** once deployment is set.

### Still open
- **Train is cut** as a downtime action — growth comes only from post-battle Levels ([[Progression]]).
- Craft/repair sit inside the Workbench/Workshop, not as a separate downtime menu entry.
- **Solo & co-op downtime is not drafted** — see [[Solo & Co-op]], still `Not Started`.
- Worker Proficiency gain rate (+5–10/phase) is a **placeholder** awaiting campaign-length data.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

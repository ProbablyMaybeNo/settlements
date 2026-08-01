# Settlements — Rules System Audit + Completion Plan
*2026-07-23 · full consistency audit (rules-auditor) + ordered path to a complete, book-ready rules system.*

> **One-line state of the union:** the **battle engine is essentially built and now verified-consistent**; the two real bodies of remaining work are (1) **proving it on a physical table** to convert sim-truth into locked-truth, and (2) **authoring the Settlement meta-game the game is named after**. Everything downstream (factions, production) is well-scoped by the existing [[Rules System — Master Roadmap]] and hangs off those two.

---

## 1 · Where the system actually stands

| Layer | Notes | Status | Real remaining work |
|---|---|---|---|
| **S1 Foundation** | Game Vision, Core Game Format, Rules Engine | ✅ Drafted, consistent | Reconcile the 2 pillar lists (Vision vs MOC); lock dice |
| **S2 Core Combat** | Unit Design, Init & Activation, Movement, Shooting, Melee, Damage, Conditions, Morale | ✅ Drafted, sim-validated, audit-clean | A handful of unticked Focus items; **table playtest**; Lock |
| **S3 Battle Layer** | Terrain, Terrain Interaction, Hacking, Infrastructure, Deployables, List Building, Scenarios | ✅ Drafted, sim-validated | Crew-integration table play; Lock |
| **S4 Settlement & Campaign** | Settlement, Economy, Territory, Downtime, Events, Narrative, Diplomacy, Solo & Co-op | 🟡 Campaign + Progression *thin*; **rest empty** | **Author from scratch** — the base-building heart |
| **🎯 Final Alpha** | thin vertical slice of #1–20 | ⬜ gate | Assemble slice once Settlement drafted |
| **S5 Content** | Factions | ⬜ empty | 1 faction for alpha; spread later |
| **S6 Production** | Balance, Components, Rulebook, Edge Cases, Playtesting | ⬜ empty | Downstream of locked systems |

**Two truths that shape the whole plan:**
- **Nothing is "Locked."** Every rule is `Drafted`. All balance numbers are **sim-derived, never table-derived** — the roadmap says so explicitly. The table playtest is the single highest-leverage validation left.
- **The audit found the drafted core sound.** 1 Critical, 6 Standard, 7 Minor — and every one is a small, surgical fix. See §2.

---

## 2 · Audit findings (fix before they compound)

Full evidence in the audit run 2026-07-23. Severity + smallest fix:

### 🔴 CRITICAL (1)
- **Disengage cost contradiction.** `core-001 Movement.md:22` + `Master Roadmap:110` say Disengage costs **both slots**; the resolved rule (`Movement.md:67-72`, dated 2026-07-13) is **Move slot only, keep your Action**. A rulebook built from the ledger would ship the *rejected* rule. → Edit the two stale citations to match the phase note.

### 🟠 STANDARD (6)
1. **"Dodge" names two mechanics.** New BLKOUT reaction (opposed AGI vs DEX, 5+ core refs) collides with the pre-existing **Dodge skill** (`Skill Paths.md:130`, melee −1). → **Rename the skill** (e.g. *Weave* / *Slip*) — 2 refs vs 5. *(Do before playtest.)*
2. **Board Representation clears Ready every End Phase**, but Ready **persists across rounds** (`Initiative:47`). The play-sheet would silently break the validated Ready-banking balance. → Split the token: Ready persists; Order-used clears. *(Do before playtest.)*
3. **`core-007 Casualties` flattens the Down/Out split** and over-generalises "auto-hit" — contradicts `Damage.md` (melee→Out; Down auto-hit by *melee only*, ranged resolves normally). Down/Out is load-bearing (Revive Beacon, Infrastructure). → Restore the split in the card.
4. **Trap arming stat:** `Terrain.md:131` says **DEX** lays/arms; everywhere else **INT** builds/deploys, DEX only disarms. → Split the table row.
5. **"Difficult" redefined** inside Foul Weather twist (`Scenarios.md:86`, "−2" MOV") vs universal **double-cost**. → Use double-cost wording.
6. **Remote-mine detonation** doesn't map onto the Reaction trigger rules (Ready token? forward-arc? end-of-move?). → One-line carve-out mirroring Hacking's Interrupt.

### 🟢 MINOR (7)
Dodge missing from 2 reaction *summaries* (`Rules Engine:78`, `Master Roadmap:101`) · `core-006` Stress trigger omits "Out" · Fall wording "full 2\"" vs "round up" · Engine one-liner doesn't tag melee→Out · "Overwatch" vocab drift (should be "Ready", `Deployables:83`) · `core-003` melee compresses out the wound branch · Reinforcements twist returns an "Out" model. → Batch-fix in one pass.

**BLKOUT propagation verdict:** ✅ Return Fire cleanly cut (no dangling refs), Snap Shot distance-gate consistent everywhere, Dodge correctly specified in all rules notes. The *only* propagation miss that bites a table is the **Dodge name collision (#2.1)**.

---

## 3 · The completion path (ordered)

### Phase 0 — Consolidate + Lock the battle layer *(fast; do now)*
The engine is done and consistent — cash that in.
- [ ] Apply the audit fixes (§2) in the **real vault**. Critical + #2.1 + #2.2 are the must-do-before-playtest set; the rest batch in one pass.
- [ ] Reconcile the **5 pillars** into one canonical list (Vision vs MOC).
- [ ] Close the cheap open Focus items that need a *decision*, not a system: Shooting target-priority, Melee positional mods (or "none at launch"), forced-movement ownership (Movement vs skill), crew-wide bottling in Morale.
- [ ] **Lock the BLKOUT changes** — they propagated clean; promote Dodge / distance-gated Snap Shot from Drafted to a locked reaction set.
- **Gate G1/G2/G3 (engine + skirmish + board):** already effectively met — this phase just makes them airtight.

### Phase 1 — Table playtest the battle engine *(highest leverage; parallel with Phase 2)*
Everything is sim-validated but **table-unproven**. This is the gate that converts the whole core from "sim says" to "Locked." The `playtest-kit/` already exists (crew sheets, capture sheet, how-to-play, reference tables).
- [ ] Run the skirmish half of the Final Alpha slice on a real table (2 crews, 9–12-feature board, the 5 scenario shapes).
- [ ] Measure: game length (~6 turns / ~90 min?), lethality *feel* vs the "super-deadly" pillar, bottling rate, and how often Dodge / Snap Shot / cover actually get used.
- [ ] Feed breakages back; **Lock** Damage (lethality) and the core loop. These are the two headline opens the roadmap says must move from Recommended → Locked.
- **Risk to monitor:** table results diverge from sim. Mitigant: the sims are thorough and the audit confirms internal consistency, so expect *validation*, not *discovery* — but the table is the authority.

### Phase 2 — Author the Settlement meta-game *(the heart — Ross writes this)*
This is what makes it *Settlements*, and it's the biggest greenfield. Gated by the 8 forks in `docs/SETTLEMENT-DESIGN-QUESTIONS.md`.
- [ ] **Resolve the 8 pivotal forks** — that's the unblock. (Settlement sits *on top of* point-buy; 9–12 terrain density stays sacred.)
- [ ] Draft **Settlement** (map + buildings-become-boards + build/upgrade + collapse) → then **Economy** (resources, sinks, upkeep, anti-snowball) → then **Territory** (claim/contest/supply/raids).
- [ ] Flesh **Campaign** + **Progression** from thin → full (drop-in/out, carry-over list, advance award rates, scar tables).
- **Gate G4 — Campaign loop:** Settlement + Campaign thin slice; crews and bases persist between games.

### Phase 3 — Assemble the Final Alpha slice 🎯
- [ ] The vertical slice: **1 faction, 10 units, 10 buildings, 5 resources, 3 scenarios, one of each core system.** Don't deepen anything until this slice plays end-to-end.
- **Gate: 🎯 Final Alpha** — first public playtest gate.

### Phase 4 — Widen content
- [ ] **Factions (S5):** template (identity + unique units + signature + buffs *and* nerfs, hooking existing systems); ship 1 for alpha, plan a small spread.
- [ ] The campaign-support notes: **Downtime, Events, Narrative, Diplomacy, Solo & Co-op** — each reuses the core loop, no parallel rulesets.

### Phase 5 — Production (S6) → book-ready
- [ ] **Edge Cases** — the systematic collision audit (this audit was a preview; do the full pass over forced-movement + falling + collapse, suppression + morale, etc.).
- [ ] **Balance** — costing formulas + the tuning spreadsheet, once factions exist.
- [ ] **Components** — token/card/sheet list (don't finalise a component until its system is Locked).
- [ ] **Rulebook** — write the chapters (the roadmap's target ToC is ready); a chapter can only be written from a Locked phase.
- [ ] **Playtesting** — continuous, with gate criteria and a coverage matrix.
- **Gates G5 (content complete) → G6 (book-ready).**

---

## 4 · Definition of complete (from the roadmap)
- [ ] Every S1–S4 phase ≥ **Drafted**; every *core* system **Playtested → Locked**.
- [ ] The two headline opens (**dice, lethality**) are **Locked**, not recommended.
- [ ] One faction plays a **full campaign loop end-to-end** with no rules gap.
- [ ] Every ledger card has real text, a category, and a locked status *(the audit shows 3 cards currently drift — fix in Phase 0)*.
- [ ] **Edge Cases** audit passed — no unresolved collisions.
- [ ] **Rulebook** chapters all backed by a Locked phase.

---

## 5 · Recommended immediate next action
**Two things, in parallel:**
1. **Green-light Phase 0** — I apply the audit fixes to the vault (Critical + the two before-playtest Standards first). Small, safe, surgical.
2. **Pick the fork resolution session** — the 8 Settlement design questions are the true critical path to everything after the skirmish. Nothing in S4 moves until those are answered.

The battle game is ready to hit a table *now*. The Settlement meta-game is the real remaining design work. Everything else is execution against a roadmap that already exists.

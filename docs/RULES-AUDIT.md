# Settlements — Rules System Audit (authorship & scope)
*2026-07-20 · a note-by-note read to separate your core intent from accumulated agent-drafted work.*

> [!success] Resolved 2026-07-20 — Ross's call
> **The current system is battle rules only.** One thing was pulled: the **Doctrine** layer (a campaign / list-building identity mechanic Claude Code added — 8 archetypes) is now out of the battle ruleset and flagged for the campaign phase.
> **Everything else stays** — all of it was built with Ross's guidance and oversight, including **weapon construction** (the class + characteristics + drawbacks *equip* system: battle kit, not a campaign mechanic — the name was just new to him). §2 below is the pre-decision analysis, kept for the record; the flags in it that guessed "you never mentioned this" were **my inference and were wrong** for everything except Doctrines.

## Method, and what I can't prove
- **Git only sees back to 2026-07-08**, when the vault was first mirrored into the repo. Most notes already existed then, so git **cannot see their original authorship** — anything written before 07-08 is invisible to me.
- **The tell is the commit language.** A burst of substantive commits **2026-07-13 → 07-15** reads like an automated pipeline, not a person: *"sim-validated," "propagate hacking-v1 through the whole system," "close auditor regressions — re-roll, terminal lockout, interrupt scope."* That's the vocabulary of agent workflows (sim + rules-auditor + propagation). Three entire notes — **Hacking (07-13), Infrastructure (07-14), Deployables (07-15)** — are net-new from that window.
- **So these flags are a reasoned read, not proof.** They combine git dates + scope + which systems you've actually engaged with in our work. You confirm; I don't assert authorship as fact.
- **Nothing here is formally "Locked."** Every rule note is `Drafted` or `Not Started`. "Locked" has only ever meant "we agreed it in conversation."

**Status key:** `CORE` = your game's foundation, keep · `REVIEW` = agent-drafted, decide keep/simplify/cut · `DEFER` = empty stub, nothing to prune yet · `META` = tooling · `MINE` = written by me this month.

---

## 1 · CORE ENGINE — your game (keep)
The foundation you've engaged with directly, and that we re-worked and sim-tested this month. This *is* your real ruleset.

| Note | Vault status | Note |
|---|---|---|
| Game Vision | Drafted | pitch + 5 pillars — we reconciled to 5 this month |
| Core Game Format | Drafted | board, turns, win-on-objectives — we rewrote scoring |
| Rules Engine | Drafted | the 1d10+stat≥7 core test, turn structure |
| Unit Design | Drafted | stats + ranks — **we just locked the new stat system here** |
| Initiative & Activation | Drafted | alternating activation, priority, orders |
| Movement · Shooting · Melee · Damage | Drafted | the combat spine, sim-validated |
| Conditions | Drafted | the status-effect list used every game |
| Morale | Drafted | stress / break / **bottling (we wrote this)** |
| Terrain | Drafted | cover, LOS, verticality — your #1 pillar |

**Recommendation:** confirm these as your core. They're what the first playtest actually tests.

---

## 2 · ADVANCED SUBSYSTEMS — the agent burst (REVIEW each)
This is the heart of it — elaborate, "sim-validated" systems from the 07-13→15 window, most of which you never mentioned and two of which you flat-out didn't recognize.

| System | Origin | My read |
|---|---|---|
| **Weapon construction** (Weapons.md — classes × characteristics × drawbacks) | 07-13 "sim-validated" | ✅ **KEPT.** This is the *equip* system — buy a class, add trait characteristics (each costs points + a slot), optional drawbacks refund points. Battle kit, built with Ross's oversight; he just never called it "weapon construction." Untouched. |
| **Doctrines** (8-archetype layer in List Building) | 07-13 | ❌ **REMOVED** from the battle ruleset — Claude-invented, and a campaign / list-building mechanic. Section + all references pulled 2026-07-20; flagged in the roadmap for the campaign phase. |
| **Skill Paths catalogue** (~150 skills, 10 per path per tier) | 07-08+, likely elaborated in burst | The *tier system* is good (we locked it). The **150-skill catalogue is agent-thorough** — **curate** it down to a starter set rather than shipping all 150. |
| **Terrain Interaction** (Force/Lift/Search/Repair + a loot economy) | Drafted | **Review.** Basic bits (force a door, climb) belong to Terrain; the search/loot economy is extra — you already cut it from the scenario. |
| **Hacking** (terminal system, range bands, interrupt) | **new 07-13** | You cut it from the first game. **Decide** if hacking is a pillar of *your* vision — it does tie to the INT stat we just built, so a *light* version has an argument. |
| **Infrastructure** (operable cranes/doors/bridges/floodlights) | **new 07-14** | Elaborate, never mentioned by you. **Strong cut/park candidate.** |
| **Deployables** (turrets/mines/beacons families) | **new 07-15** | Cool but advanced gear system. **Park** for post-alpha. |

**Resolution (2026-07-20):** only **Doctrines** were pulled (campaign mechanic). The other six — **weapon construction, the skill catalogue, Terrain Interaction, Hacking, Infrastructure, Deployables** — all **stay**: Ross confirmed they were authored with his guidance and oversight. My "park because you never mentioned it" defaults were a wrong inference for these; corrected above.

---

## 3 · CAMPAIGN & CONTENT — mostly empty stubs (defer)
Roadmap placeholders — a focus statement and an empty body. **Nothing to prune** (there's no content yet); tackle when you reach that phase.

`Settlement` · `Economy` · `Territory` · `Downtime` · `Events` · `Narrative` · `Diplomacy` · `Solo & Co-op` · `Factions` · `Balance` · `Components` · `Rulebook` · `Edge Cases` · `Playtesting` — all **Not Started**.
`Campaign` · `Progression` — Drafted but *thin*. `Final Alpha` — the milestone gate.

**Recommendation:** leave untouched. Note: **Settlement / Economy / Territory** are the base-building layer that makes it *Settlements* — those are the ones *you'll* want to author yourself rather than let an agent fill.

---

## 4 · META / SCAFFOLDING — tooling, keep
`Master Roadmap` · `Rules System MOC` · `Open Decisions` (dashboard) · `Ideas Inbox` · `Out of Scope — What Settlements is NOT` · `Obsidian Guide` · `Quick Reference — Writing Rules`. These organize the vault; keep them. `Out of Scope` in particular reads as *your* voice — a good anchor for this pruning.

`Board Representation` — **MINE** (I wrote it 07-16, proxy/token guide). Keep or cut, your call.

---

## 5 · SIM FINDINGS — agent analysis (reference only)
`Crew Sim` · `Dice Mechanic` · `Skill Sim` · `Deployables Sim` · `Terrain-Hacking Cover` findings + test plan. Agent-generated balance analysis — useful *evidence*, not rules. Note that **Deployables Sim** and **Terrain-Hacking** exist only to validate the subsystems in §2, so they rise or fall with those decisions.

---

## 6 · LEDGER CARDS (Rules Ledger/, 14 cards)
`core-000` … `core-008` — short citation-form summaries of the core rules; agent-graduated (the "fix drifted ledger cards" commit). **Keep** as the clean reference form, but they must be re-checked against the core notes.
`adv-001…005` (Vehicles, Drones, Civilians, Weather, Campaign) — **parking-lot stubs** for future systems. **Review** — these are speculative placeholders.

---

## Recommended next actions
1. **Confirm the CORE 12** (§1) as your foundation.
2. **Rule on the seven subsystems** (§2) — keep / simplify / cut each. (My defaults above.)
3. On your calls, I'll: **write a real `status:` on every note** (`core` / `drafted` / `parked` / `cut`), **move parked systems** to a `_Parked/` folder so they're preserved but out of the active ruleset, and **delete** anything you kill.
4. Then the vault reflects *your* deliberate game — and the first playtest is built on rules you actually chose.

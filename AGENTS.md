# AGENTS.md — Settlements

*Corrected 2026-08-09 against the vault's `Full Rules System v1` (adopted 2026-08-05,
audit fixes integrated 2026-08-08). Several facts below were stale by a whole rules
generation — see "Superseded facts" at the bottom so the old versions don't creep back.*

## Learned User Preferences

- Keep all stat tests binary pass/fail against the flat TN 7+ mechanic. Do not add per-task difficulty modifiers — trivial actions (pushing a button) auto-pass, everything else is a straight 7+ test. Ross has pushed back on added test complexity repeatedly.
- Avoid flat unconditional "+1 to hit" bonuses when designing skills or rules; any to-hit bonus must be conditional (e.g. +1 vs units in the open).
- Core anti-bloat tenet: prefer cutting or merging subsystems over adding parallel ones. Things actually cut so far: Water upkeep, per-head upkeep, the Heat/Attention track, HP-based structure damage, worker Proficiency, the Seeker mine chassis. Don't propose new resource tracks or difficulty tiers without strong justification.
- Preferred design workflow: agent presents a numbered question list, Ross answers inline in chat, then the agent drafts the rules into the vault notes. Format questions so they're easy to answer in-chat.
- After drafting or changing rules, keep the Build Roadmap checkboxes and the rules ledger up to date.
- **One economy only.** A unit or piece of equipment's **Credits** cost IS its battle-roster cost — you buy with Credits and the Credits you field are your Crew Rating. Never introduce a second parallel currency. The internal global points costing system (`docs/GLOBAL-POINTS-SYSTEM.md`) is a designer-side tool — players should never see it.
- **Propagate, don't strand.** A rule change must drip through every note that references it before commit; grep the old vocabulary first. Satellite notes contradicting the master is the project's lowest-scoring quality axis.

## Learned Workspace Facts

- Settlements is a pre-alpha tabletop skirmish wargame — **near-future 2051 America, second civil war**, with a base-building campaign layer. Grounded mil-tech: directed energy, drones, robots, exosuits, EW (`docs/SETTING-TECH-2051.md`). Rules are markdown notes, not code.
- **Source of truth is the single master note** `Rules System/Full Rules System v1.md` in Ross's Obsidian vault (`Documents/Obsidian Vault/Settlements/`). Where any phase note disagrees with it, **the master wins** and that note is owed an edit. Phase notes keep the long-form reasoning; the master keeps the ruling.
- The repo's `rules-vault/` folder is a **one-way mirror**, refreshed every 15 min by the "Settlements Rules Sync" scheduled task (`scripts/sync-and-push.ps1`). **NEVER hand-edit `rules-vault/`** — it gets overwritten. Edit the real vault; run `scripts/sync-rules.ps1` to mirror immediately (robocopy exits 1 on "files copied" — that is success).
- `_Rules Catalogue.md` is a generated lens holding **live block embeds of every rules table** in one note, for design review. Regenerate with `py -3.13 scripts/build_catalogue.py`; it reports any table it could not place.
- Roadmap and trackers live in Notion (Build Roadmap page + Settlements hub DBs); `TRACKERS/` CSVs sync via `py -3.13 scripts/notion_sync.py sync-all`.
- Balance simulations live in `test-bench/`: `balance/` for subsystem sims, `engine2d/` for the **2.5D battle engine** that plays whole games (true LOS, height advantage, falls), `points/` for the costing engine. Run with `py -3.13`.
- `tts/` holds the Tabletop Simulator integration: a live socket to a running TTS (`tts_api.py`), a table generated from the validated sim board (`build_table.py`), and a rules layer in `Global.lua`.

## Locked mechanics — do not contradict these

- **Core resolution:** `1d10 + Stat + Modifiers` vs **7+**. Natural 1 always fails, natural 10 always succeeds. To-injure is `1d10 + Damage − Armour` vs 7+. **No second dice type exists anywhere in the game.**
- **Opposed tests** use the same roll for both sides; **ties go to the defender**.
- **Modifier cap ±3** on any single roll, however many conditions are carried.
- **Five stats:** STR (melee, force, hauling) · DEX (ranged, throwing, fine work) · AGI (climbing, jumping, dodging) · INT (hacking, crafting, medicine, searching) · NRV (nerve, Stress, Break tests). Max **+6**.
- **Ranks and stat points:** Recruit **3** · Fighter **5** · Specialist **7** · Leader **9**. Orders: 0 / 0 / 1 / 2. Tier caps at creation: Recruit none · Fighter 2×T1 · Specialist 1×T2 + 2×T1 · Leader 1×T3 + 2×T2 + 4×T1.
- **Skills ride the stat, one per tier a stat reaches** — +2 unlocks T1, +4 unlocks T2, +6 unlocks T3. Counts are **exact, not approximate**. There is no separate skill pool and skills are never charged Credits (`POINTS-DECISIONS` D22/D27).
- **Crew Rating caps:** Match Play **1000** · raid 750 · pitched 1500 · Campaign Start **500**. Rank bodies: Match Play 65/95/165/245, Campaign Start 65/75/125/170.
- **WND is 1 for everyone.** Campaign veterans reach WND 2 (Level 7) and at most **WND 3** (Level 7 + Tough) — a hard ceiling, logged as a deliberate tenet exception in `Out of Scope` §4. Nothing may push past 3.
- **Terrain density is the single most powerful balance dial: 9–12 large features, one per each of the nine 12"×12" squares, 12 is a hard ceiling.** Density alone swung win rate 66 points in simulation — more than any points cost can.
- **You win on objectives, never on kills.** Resources are banked by both crews regardless of who won.
- **Every hit does something:** a hit wounds *or* delivers its payload, never both, and a failed wound becomes Stress — which is the entire fear/suppression system.
- **The Level track (§26.1):** 10 levels. **Primary** is derived from the highest investment at creation and never changes; **there is no declared Secondary** — levels 1/4/8 add +1 to *any* stat, chosen when earned. Levels 2/5/9 are forced +1 Primary. Skill slots at 3/6/10 let you declare any path at any tier **that path's stat has unlocked**.
- **Fate:** a natural 1 is always Dead, a natural 10 always Hardened, and total Fate modifiers are **capped at +2**.

## Superseded facts — the old versions, so they don't creep back

| Stale claim | Current truth | Changed |
|---|---|---|
| "Leaders 6 stat points, Champions 4, fighters 2" | Recruit 3 / Fighter 5 / Specialist 7 / Leader 9 | rank rework |
| "Champion" as a rank name | **Specialist** | rank rename |
| "A free skill per 2 stat points spent" | One skill per **tier** a stat reaches (+2/+4/+6) | supersedes points÷2 |
| "Goods" as the currency | **Credits** | 2026-08-01, D24 |
| 100-point budget, 5/8/16/24 ladder | 1000-Credit scale | 2026-08-05 |
| Freeform Advance spend | The fixed 10-Level track | 2026-08-05 |
| Declared Primary *and* Secondary, fixed for life | Primary derived and permanent; secondaries float | 2026-08-08 |
| Generator +3 | **+5**, draws T1 −1 / T2 −2 / T3 −3 | D9 |
| HQ 10 housing | **12**, +6 per Bunkhouse | D10 |
| Armour 30 / 60 | **60 / 100** *(`points/ticks.py` still carries the old pair — a known, unfixed defect)* | 2026-08-05 |
| 25 structures | **23** — Water Reclaimer and Cistern went with Water | 2026-08-01 |
| Worker Proficiency 0–100 track | Cut. A worker is assigned or not; ten benefits ship, ten parked | 2026-08-05/08 |

## Known open defects

- `test-bench/points/ticks.py` carries armour at **30/60** and marks it `[measured]`, but the cited source file `balance/armourprice.py` **does not exist in the repo**, and a 500-cap sim measured 60/100 as the better price. The engine and the rules disagree.
- `PACKET-TEST-RESULTS.md` is cited by the master note for its **T1–T14** sim findings and **is not in the repo**. Those figures are quoted, not reproducible.
- `docs/SETTLEMENTS-WHOLE-SYSTEM-AUDIT.md` has an **unapproved** approval sheet — do not act on its recommendations without Ross's ticks.

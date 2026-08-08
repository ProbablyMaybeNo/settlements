# Settlements — Full Rules Audit & Proposed Fixes

**Date:** 2026-08-06 · **Against:** `Full Rules System v1.md` (vault copy, adopted 2026-08-05)
**Status:** PROPOSED — nothing here is applied. Review each fix, mark ✅ approve / ❌ reject / ✏️ amend, then integrate approved items into the Full Rules System in one pass.

Every fix below is written as **ready-to-paste rule text** with its target section. Numbers marked *(provisional)* are first-draft dials for Phase 2 to tune — the structure is the proposal, not the specific value.

---

## 0 · Reconciliation — RESOLVED, no action needed

Diffed the exported `Settlements-Full-Rules-System-v1.md` (1056 lines) against the vault's `Full Rules System v1.md` (1098 lines). The only difference is the vault copy's YAML frontmatter + the "Source of Truth" banner (23 lines + spacing). **Content is identical. The vault copy is canonical.** The download is a clean export — archive or delete it.

---

## PART A — Hard blockers (fixes 1–6)

### FIX 1 · Fate table death immunity **[BUG — must fix before any campaign test]**

**Problem.** Med-bay grants +1 to the Fate roll, +2 with a worker (§21, §22). Dead only occurs on a result of 1 (§26.3). A staffed Med-bay makes the minimum result 3 — death becomes impossible, gutting "combat is brutal and final."

**Fix — add to §26.3, directly under the roll instruction:**

> **A natural 1 on the Fate die is always Dead, regardless of modifiers** — the same rule the core engine already uses for every test (§2). Likewise, **a natural 10 is always Hardened**. Fate modifiers (Med-bay, workers, future sources) shift every other result but never overwrite the die's own extremes. **Total Fate modifiers are capped at +2** from all sources combined.

**Effect.** Every fighter who rolls Fate carries a flat 10% death risk forever, Med-bay or not. The Med-bay still meaningfully upgrades the middle of the table (scars → recovery, captured → scar). Matches the engine's existing nat-1/nat-10 grammar — zero new rules vocabulary.

---

### FIX 2 · WND creep vs the "no superhero" anti-goal **[TENET EXCEPTION — write it down as a decision]**

**Problem.** List Building's anti-hero argument is "WND is fixed at 1." The Level track grants +1 WND at Level 7 (§26.1), stackable with Tough to WND 3, and §26.1 says a Level 10 fighter reads "as close to a superhero as a civilian-scale game allows" — nearly quoting the hard anti-goal in `Out of Scope — What Settlements is NOT.md`. Currently reads as drift, not decision.

**Fix 2a — add to Out of Scope §4 (rejected/allowed log):**

> | Idea | Ruling | Why | Date |
> |---|---|---|---|
> | Veteran WND above 1 | **ALLOWED, hard-capped at WND 3** | Campaign survival must be mechanically felt or "scars tell the story" is flavour text. WND 2 costs a fighter ~10 battles of survival (Level 7); WND 3 additionally costs a T3 skill slot (Tough). Both are visible on the card, priced into Crew Rating, and every hit still does *something* (§9) — a WND 3 legend still dies in one bad round. **No current or future source may push WND past 3, and no source below Level 7 / Tier 3 may grant WND.** | 2026-08-06 |

**Fix 2b — replace the "superhero" sentence in §26.1 with:**

> Reaching Level 10 at all should be rare — surviving that long takes real luck. A Level 10 fighter is a **legend by civilian standards** — feared, storied, and still one bad round from the dirt. This game never makes anyone unkillable (see the WND ruling in *Out of Scope*, §4).

**Fix 2c — add one line to §9 (Damage), after "Every unit has WND 1":**

> Campaign veterans can reach WND 2 (Level 7) and at most WND 3 (Level 7 + the Tough skill) — the hard ceiling, logged in *Out of Scope* §4.

---

### FIX 3 · Campaign Start pyramid degenerate corner

**Problem.** "One Leader, minimum three models, no ratio" at 500 CR legally allows Leader + 2 Specialists in heavy armour — three elite bodies, no chaff, zero validation behind it, and exactly what every min-maxer will field.

**Fix — replace the Campaign Start pyramid paragraph in §16 with:**

> **[Campaign Start variant]** **Exactly one Leader. Every Specialist still requires two fighters of lower rank. Minimum three models.** Only the Recruit ratio is waived — a green crew hasn't built a chain of command, but a Leader still doesn't hire lieutenants before troops. *(At 500 CR this makes Leader + Specialist + 2 Fighters the most elite legal start — the all-Specialist door is closed.)*

**Effect.** Worst-case elite start becomes Leader (170) + Specialist (125) + 2 Fighters (150) = 445 naked — bodies on the board, and the Specialist ratio the sim validated stays intact. Recruit-swarm starts remain legal.

---

### FIX 4 · Level track — Primary is derived, direction is chosen in play, **skill tier is gated by the stat** *(revised ×3, 2026-08-06 — final shape agreed in discussion)*

**Problem.** §26.1 currently reads "At creation, declare a Primary stat and a Secondary stat… Both, and the skill path tied to the Primary, stay fixed for that fighter's whole career." That's not the intended design. The track exists to let units **focus into secondary stats as they level**, opening layered playstyles — the quick melee fighter (STR→AGI), the intelligent shooter (DEX→INT), the agile hacker who reaches terminals first (INT→AGI). Locking a single Secondary and a single skill path at hire kills exactly that. But fully floating skill slots create the opposite failure: a two-point splash buying a Tier 3 capstone (Tough on STR +2 → cheap WND). The resolution is the tier logic creation **already uses**: skill tier rides the stat — **+2 unlocks Tier 1, +4 unlocks Tier 2, +6 unlocks Tier 3.**

**Fix — replace §26.1's declaration paragraph, the three skill rows of the track table, and the skill-choice rule with:**

> **Primary** is the stat carrying the fighter's highest point investment at creation (player's choice on ties). It never changes — it's who they were when they signed on, and it names their Primary skill path.
>
> **There is no declared Secondary. Every other stat is a secondary stat.** At the track's **floating stat levels (1, 4, 8)**, add +1 to **any stat, chosen when the level is earned** (Primary included) — a fighter's direction emerges from play, not from a box ticked at hire. Levels 2, 5, 9 remain forced **+1 Primary** — the fighter's identity keeps growing regardless of direction. Only the **campaign stat cap (+6)** limits track growth; **rank tier caps are creation-time caps and do not constrain leveling.**
>
> **Skill slots (Levels 3, 6, 10):** declare any path, and roll on any tier that path's stat has **unlocked: +2 → Tier 1, +4 → Tier 2, +6 → Tier 3** — the same thresholds creation already uses (§14). Roll 3 on the declared tier's chart, choose 1, reroll duplicates. The Level no longer fixes the tier — **the stat does.** A fighter's Primary path always counts as unlocked at Tier 1, so a slot is never dead.

**Track table change:** rows 3, 6, 10 become simply **"Skill slot"** (Credits unchanged: 20 / 35 / 55). The Level 10 row keeps its capstone note — for a committed fighter that slot *is* their Tier 3 pick, because they've reached +6 by then.

**Why this works:**
- **Tough is solved structurally, not with an exception.** T3 needs the stat at +6 — start +3 and take all three forced Primary levels, or start +2 and spend floaters on it too. Only fighters who *are* bruisers get the bruiser capstone. No skill-specific carve-out needed.
- **One grammar everywhere.** Creation skills (§14, FIX 6) and leveled skills now use the identical +2/+4/+6 thresholds — nothing new to learn, nothing to cross-reference.
- **The layered builds still land.** The agile hacker (INT primary) pushes AGI with floaters to +4 by Level 8 and can take Fleet at the Level 10 slot — *at the real cost of forgoing their INT Tier 3 capstone.* Every cross-path pick is a genuine trade now, not a freebie.
- **Floaters into Primary are legal and self-limiting** — the +6 cap makes overflow wasted, so total specialists pay for their capstone with breadth.

**Effect.** Careers are unpredictable at hire and player-steered throughout; the 4-skill lifetime total, cadence, Credits, and bookkeeping are unchanged. Anti-freeform holds: the menu is only ever "tiers you've genuinely paid for in stat points."

**Playtest flag:** the one build to watch is the all-in Primary rush (floaters into Primary → +6 by Level 8, T3 available at Level 10 for any rank). That's intended — a total specialist with zero breadth — but verify in Phase 2 that a +6 single-stat Fighter doesn't outperform a rounded Specialist at equal Credits.

---

### FIX 5 · Dodge is over-loaded

**Problem.** Dodge (§3) both negates a hit *and* repositions up to full MOV out of LOS, drawing no reactions, for the cost of Pinned. On an AGI+Fleet build that's an 8" defensive teleport. It's the only reaction that cancels damage and moves.

**Fix — replace the Dodge row in §3 with:**

> | **Dodge** | When targeted by a ranged attack (any angle): opposed `1d10+AGI` vs shooter's `1d10+DEX`, ties to you. **Win** → the shot misses and you may move up to **half MOV"** (round down); the move draws no reactions; then gain **Pinned**. **Lose** → the shot hits, resolve Injury normally. |

**Sim spec (run before Phase 2):** add Dodge to `test-bench/` crew sim; AGI-stacked crew (2× AGI+4, Fleet) vs the 8 archetypes; three variants — full MOV / half MOV / full MOV + Prone. **Acceptance: the Dodge carrier gains ≤ +8 win-points over its no-Dodge baseline.** If half-MOV still breaks it, fall back to Prone-on-dodge.

---

### FIX 6 · Tildes in the Match Play rank table

**Problem.** "~2 / ~3 / ~4" starting skills — approximation marks in the core build table block crew creation at the table.

**Fix — replace the Match Play "Starting skills" column and add this footnote to §16:**

> | Rank | Stat pts | Starting skills | Orders | Credits |
> |---|:--:|:--:|:--:|:--:|
> | Recruit | 3 | **0** | 0 | 65 |
> | Fighter | 5 | **exactly the tiers your stats reach (max 2)** | 0 | 95 |
> | Specialist | 7 | **max 3** | 1 | 165 |
> | Leader | 9 | **max 4** | 2 | 245 |
>
> **Skills are never approximate: a fighter has exactly one skill per tier its stats reach** (§14). The listed value is the maximum, hit only when every point lands in tiered stats — e.g. Fighter `+2/+2/+1` = 2 skills; Specialist `+4/+2/+1` = 3; Leader `+6/+2/+1` = 4. A fighter who spreads into +1 "dabbles" trades skills for breadth — that's a legal, priced choice, not an error.

*(Campaign Start column is already exact — 1 skill per rank — no change.)*

---

## PART B — Removals & trims

### TRIM 1 · Worker benefits: ship 10, park 10

**Keep in v1** (they carry the loop): Processor · Salvage Yard · Generator · Med-bay · Storehouse · Equipment Shed/Armory · Trader's Kiosk/Trade House · Workbench/Workshop · HQ · Mess Hall.

**Park** (move into the §22 collapsed supplement appendix, beside Proficiency): Fabricator ladder · Scout Post · Comms Mast · Server Core · Drone Bay · Holding Cells · Gatehouse · Watchtower · Turret Mount · EW Mast.

**Replacement line for §22:** "Structures not listed accept no worker in v1 — their base effect is their whole effect. The parked benefits live in the supplement appendix below."

**Why these ten parked:** all are either battle-facing micro-buffs that complicate raids (Watchtower, Turret Mount, Gatehouse, EW Mast) or intel/unlock effects serving systems that are themselves thin in v1 (Scout Post, Comms Mast, Server Core, Drone Bay, Fabricator, Holding Cells). Zero loop damage; ~50% less rules surface.

### TRIM 2 · Seeker mine — park it

Remove from the §12.6 mine chassis list. **Add to the §15 rejected log:**

> | Seeker mine (self-moving munition) | Parked, not rejected — a moving munition on a 3'×3' board is an edge-case factory (does it draw Reactions? trigger traps? get shot as a Feature? what's its facing?). Revisit after the Edge Cases audit exists. | 2026-08-06 |

Proximity and Remote chassis carry the family fine; Remote's bluff kit is the interesting one anyway.

### TRIM 3 · Battlefield Event 3 (Trader's caravan)

Every other event modifies board state; this one opens a shop menu mid-battle. **Replace entry 3 in §27 with:**

> | 3 | Burst main | A water main lets go — a 3" zone centred on the board's midpoint becomes **Difficult ground** for the rest of the game. |

### TRIM 4 · Loot table entry 7 (Chems)

Chems are deliberately Workshop-gated (§28.2); loot handing out free doses bypasses a gate someone paid Materials for. **Replace entry 7 in §23 with:**

> | 7 | **+15 Credits** |

*(Credits ladder becomes 5/10/15/20 across entries 2/4/7/8 — clean.)*

---

## PART C — Missing pieces (drafted, provisional numbers)

### ADD 1 · Campaign end condition — "the Season" *(new §29.5 or end of §25.5)*

> ## The Season
> A campaign is played as a **Season**. A Season ends immediately when either player **Controls 4 territories** at the end of any Settlement Phase — that player wins outright. Otherwise it ends after **each player has fought 10 battles**, and the higher **Season Score** wins:
>
> | Source | Points |
> |---|:--:|
> | Per Controlled territory | 3 |
> | Per Functional structure (built after founding) | 1 |
> | Per fighter at Level 5+ still on the roster | 1 |
>
> Tiebreak: total banked Credits + Materials. *(All values provisional — the point is that campaign pacing now has an end to pace toward. Post-season, players may continue into a new Season keeping settlement and roster — fresh Season Score, fresh battle count.)*

### ADD 2 · Storage cap numbers *(replaces the prose in §20)*

> | Store | Capacity *(provisional)* | Raidable? |
> |---|---|---|
> | HQ | **150 Credits + 150 Materials** | Yes |
> | Gatherer buffer (each) | **30 of its own resource** | Yes — and first to go |
> | Storehouse (each) | **+250 combined**, any mix | Yes — the raid target |
> | Vault | **150 combined** | **No** — Sabotage/hack only, never raid loot |
>
> **Over cap:** caps are checked **once, at the end of the Settlement Phase** — resources may sit over cap freely between banking and spending inside the same phase; whatever still exceeds cap when the phase closes is lost. Spend it or lose it. *(Timing rule added 2026-08-07 — the ADD 5 worked example banks 215 Cr against a 180 cap mid-phase, spends down to 175 before phase end, and is legal.)* *(This is also the first real economy sink — a wealthy settlement must build Storehouses/Vaults or bleed surplus, which partially answers the §29 sink problem.)*

### ADD 3 · Trader conversion rate *(add to §21 Trader's Kiosk / Trade House entries)*

> **Kiosk:** sell **2 Materials → 1 Credit** · buy **2 Credits → 1 Material**. **Trade House:** **3 Materials → 2 Credits** · **3 Credits → 2 Materials**. Worker: +10% yield, round down. Convert in one direction only per Settlement Phase. *(The spread means no conversion loop is ever profitable; rates provisional.)*

### ADD 4 · Raid loot — what winning actually takes *(add to §21 raid rules / §12.7)*

> **If the attacker wins a raid** they carry off **25% (round down) of the defender's stored Credits and 25% of stored Materials** — Vault contents excluded — **capped at 100 Credits + 100 Materials per raid**, plus whatever they looted/sabotaged in-battle. **If the defender wins**, the attacker keeps only what they physically looted during the battle.
> **Floor:** raid theft never reduces a defender below **50 Credits + 50 Materials** combined stores — a settlement can be hurt, not deleted. *(Cap + floor are the anti-death-spiral pair; both provisional.)*

### ADD 5 · Worked example — founding + first campaign turn *(new appendix §28.6)*

> **Founding.** Rosa picks **Fire Station** (free Bunkhouse). She starts with HQ, Generator (+5), Processor, Salvage Yard, + the Bunkhouse. Founding budget 250 Materials + 150 Credits: she builds a **Med-bay** (120 Mat), banking 130 Mat + 150 Cr. Power draw: HQ 1 + Processor 1 + Salvage 1 + Med-bay 1 = 4 of 5 — one spare.
> **Crew (Campaign Start, 500 CR).** Leader **Marisol** (170) + Assault Rifle (130) = 300 · Fighter **Deke** (75) + Sidearm (40) = 115 · Fighter **Junie** (75) + free bat = 75. **Total 490/500.** Pyramid legal: one Leader, no Specialists, 3 models.
> **Battle 1** — Take a Hold on a neutral territory. Marisol claims two terminals; Junie goes Down in round 5 and the crew can't reach her. **Win.** Rewards: 65 Cr + 33 Mat.
> **Post-Battle.** Junie rolls Fate +1 (Med-bay): rolls a 6 → 7, **Lasting scar — Broken arm** (−1 STR next battle only). Marisol survived + held an objective → **Level 1: +1 Secondary stat**. Deke survived → **Level 1**.
> **Settlement Phase.** Bank to 215 Cr + 163 Mat — **215 is over the 180 Cr mid-phase store (HQ 150 + Salvage buffer 30), which is legal**: caps bite only at phase end (ADD 2). Assign the crew's one worker to the **Processor** (+1 Materials per gather). Buy Junie a Sidearm (40 Cr → 175 Cr). Scavenge dispatch (HQ I): loot roll 6, +15 Materials. Phase closes at **175 Cr + 178 Mat** — both under cap.
> **Battle Prep.** Choose the next territory; cap stays 500 CR; Junie fields with her scar. Roll the Twist at deployment.

---

## PART D — Phase 2 test plan (formalized)

| # | Test | Method | Pass criteria |
|---|---|---|---|
| 1 | **Full campaign turn loop** — 3-battle mini campaign, 2 players, §25.5 end to end | Table | Loop completes without a rules gap; Settlement Phase ≤ 15 min; every banked number has a place to go |
| 2 | **Campaign Start @ 500 CR** — fixed pyramid (FIX 3), lean kits, Level pacing | Table + `crew_sim` variant | No start archetype > 60% across the scenario set; a fighter reaches ~Level 3 by battle 3 |
| 3 | **Raid** — density fill, defender tie-break, charge timing, loot cap/floor (ADD 4) | Table | Attacker win rate 35–50%; charges armed by round 3 matter; post-raid defender still functional |
| 4 | **Dodge/Ambush/Hidden AGI economy** | `crew_sim` first (FIX 5 spec), then table | Dodge carrier ≤ +8 win-points; Ambush stays within its sim envelope (+1 to +13) |
| 5 | **Economy pacing over 5+ battles** — income vs 23-structure catalogue, storage-cap sink (ADD 2) | Spreadsheet sim + campaign from test 1 | A settlement always has a purchase it *wants* by battle 5; surplus loss actually bites at least once |
| 6 | **Captured/brainwash thread** across 3 Settlement Phases | Table (inject via test 1) | Thread resolves without ambiguity; both players report the decision felt real |

§29's open dials (hold radius, Burst Turret, Revive Beacon, CRUSH lethality, conveyor distances) ride along inside tests 1–3 — no separate slots.

### Part D sim results — 2026-08-07 (post-approval run)

Harnesses live in `test-bench/balance/audit_*.py`. Table tests 1 / 3 / 6 still need a human.

| # | Sim | Result | Notes |
|---|---|---|---|
| FIX 1 | `audit_fate.py` | **PASS** | Death flat 10% at every mod; old rule confirmed zero-death at +2; Med-bay still upgrades the middle |
| FIX 3 / D2 | `audit_pyramid.py` (300/pair) | **PASS** | Legal field best 50% (Armoured); OldElite (closed) at 71%. Level-3-by-battle-3: yes (1.3–2.1 battles) |
| FIX 4 gate | `audit_tier_gate.py` | **PASS** | No T3 below +6. Fighter all-in unlocks T3 at L6; Fighter who spreads never reaches T3 on Primary |
| FIX 4 rush | `audit_track.py` (400/pair) | **PASS mean / FAIL Annihilate** | RUSH vs ROUNDED mean 63% (inside 35–65). **Annihilate 90–91%** — WND-3 wall dominates kill missions. RUSH loses to SPECIAL (41%). Flag for Phase 2 table: either scenario mix absorbs this, or Tough / L7 WND needs a second look on pure-kill missions |
| FIX 5 | `audit_dodge.py` (200/pair) | **PASS acceptance, weak signal** | All variants ≤ +8 (full −6.4 / half −5.4 / prone −4.7). Dodge is a *trap* under the fisher AI (opposed-loss = auto-hit), so the sim does **not** reproduce the over-load worry — half-MOV barely differs from full. **Table test still required** to settle FIX 5 |
| D5 / ADD 2–4 | `audit_economy.py` (2000×12) | **PASS** | Builder wishlist never exhausted; hoarder bleeds 100%; post-raid rebuy in 1.4 phases. Trader round-trips unprofitable |
| ADD 4 | `audit_raid_loot.py` | **PASS** | Cap, per-resource 50+50 floor, Vault immune. Economy sim floor corrected to per-resource (was combined-100) |
| ADD 5 | `audit_add5_example.py` | **PASS** | 215→175 Cr under phase-end timing; counterfactual cap-at-bank would have lost 35 Cr |

**New sims added from the verdict:** `audit_tier_gate.py` (the T3-without-+6 bug Ross named), `audit_raid_loot.py` (ADD 4 floor/cap exact), `audit_add5_example.py` (cap-timing reconciliation).

**Open from this run (not blockers for integrate, but Phase 2 must carry):**
1. FIX 4 Annihilate skew — WND 3 vs WND 2 on kill missions is a 90%+ wipe.
2. FIX 5 needs a table pass; the engine AI cannot currently stress the escape-LOS case that motivated the nerf.

---

## PART E — Vault hygiene & the DRAFTED commit

**E1 · Reconciliation** — ✅ done (Part 0). Vault copy is canonical.

**E2 · Propagate the monolith into the phase notes** (stamp-or-edit each — a one-line banner is enough):

| Note | Action |
|---|---|
| `List Building.md` | Banner: "Superseded by Full Rules System v1 §16 — the 5/8/16/24 ladder is deprecated; Credits scale is canonical." |
| `Factions.md` | Banner: "Superseded by §24 — stat-bonus/nerf placeholder replaced by one-rule + affinity model." |
| `Downtime.md` | Banner: "Drafted as §25.5 (the Campaign Turn)." Status → Drafted. |
| `Progression.md` | Banner: "Superseded by §26.1 (10-Level track) — freeform Advance spend is dead." |
| `Unit Design.md` | Add the exact-skill-count footnote (FIX 6); point costs to §16. |
| `Campaign.md` | Point Fate at §26.3 (incl. FIX 1's nat-1/nat-10 rule). |
| `Out of Scope — What Settlements is NOT.md` | Add FIX 2a (WND ruling) + TRIM 2 (Seeker) log entries. |
| `Settlement.md` / `Structures.md` | Point at §17–§22; fold ADD 2/ADD 4 numbers in. |

**E3 · Master Roadmap updates:** Settlement, Economy, Downtime, Events, Territory, Factions → **Drafted**; Progression → Drafted (Level track); fix the S4 stage line ("rest empty" is false); log the Season (ADD 1) as Campaign's end-condition checkbox.

**E4 · The commit.** After approvals are integrated (edit in **Obsidian**, never `rules-vault/` directly — one-way sync):
1. Integrate approved fixes into `Full Rules System v1.md` + the E2 banners in Obsidian.
2. Let the sync task mirror (or run `scripts\sync-rules.ps1`).
3. Single commit: `Full Rules System v1 — audit fixes integrated; S4 DRAFTED milestone; ready for Phase 2 testing`.

---

## Approval sheet

*Ross verdict 2026-08-07 — approve everything as written; FIX 4 with the T3-without-+6 bug-fix context; ADD 5 contingent on the ADD 2 phase-end timing line (now in both).*

| Item | Fix | Approve? |
|---|---|---|
| FIX 1 | Fate nat-1 always Dead / nat-10 always Hardened / +2 mod cap | ✅ |
| FIX 2 | WND exception logged in Out of Scope; WND 3 hard ceiling; wording swap | ✅ |
| FIX 3 | Campaign Start keeps the Specialist ratio | ✅ |
| FIX 4 | Primary derived; floating secondaries; skill tier gated by stat (+2/+4/+6) | ✅ |
| FIX 5 | Dodge move → half MOV + sim spec | ✅ |
| FIX 6 | Exact skill counts (tiers-reached rule) | ✅ |
| TRIM 1 | Ship 10 worker benefits, park 10 | ✅ |
| TRIM 2 | Park Seeker mine + log entry | ✅ |
| TRIM 3 | Trader's caravan → Burst main | ✅ |
| TRIM 4 | Loot Chems → +15 Credits | ✅ |
| ADD 1 | The Season (campaign end + scoring) | ✅ |
| ADD 2 | Storage caps + spend-it-or-lose-it sink + **phase-end timing** | ✅ |
| ADD 3 | Trader conversion rates | ✅ |
| ADD 4 | Raid loot: 25% / cap 100+100 / floor 50+50 / Vault immune | ✅ |
| ADD 5 | Worked example appendix (numbers reconciled to phase-end caps) | ✅ |
| E2–E4 | Propagation banners + roadmap + single DRAFTED commit | ✅ *(pending integrate)* |

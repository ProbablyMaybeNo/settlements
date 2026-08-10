# Settlements — Whole-System Tenet Audit

**Date:** 2026-08-08 · **Against:** Obsidian `Full Rules System v1.md` (revised 2026-08-08, prior hard-blocker audit integrated)  
**Lens:** identity fidelity — not bug-hunting. Does the *whole game* still feel like Settlements?  
**Status:** OPINIONATED AUDIT — recommendations only. Nothing here is applied.

---

## 0 · The bar (your ask, mapped to Vision)

| You said | Vision pillar it answers |
|---|---|
| Terrain first | **1 · Battlefield is the weapon** |
| Battles quick, tactical, bloody | **2 · Combat is brutal and final** |
| Win with all tools, not just kills | Anti-goal: not annihilation-driven · Signature: terrain mastery |
| Terrain interactions natural & impactful | Pillar 1 + "not static battlefields" |
| Crews feel like *yours* | **4 · Scars tell the story** · Signature: crews as characters |
| Simple but never boring | **5 · Simple rules, complex outcomes** |
| No rules for rules' sake | Out of Scope: no bloat · Complexity ceiling |
| Growth feels natural | Pillar 4 + Level track |
| Every battle → meaningful crew *and* settlement change | Pillar 4 + §25.5 Campaign Turn |
| Rules clear, systems mesh | Pillar 5 + one-dice / three-lever contracts |
| Online hub carries bookkeeping | Out of Scope tension: tabletop-first, hub as convenience |

**Canonical ranking** for this audit: **Game Vision's five pillars** (1→5). Out of Scope aliases ("We are only human", "Crunchy not Concrete") are treated as the same spirit under different names — the Roadmap's "two tenet lists" debt is still open and should be closed in a five-minute rename pass.

---

## 1 · Scorecard (0–5)

| # | Tenet / ask | Score | One-line verdict |
|---|---|:---:|---|
| T1 | Terrain first | **4.5** | Identity is locked in rules text; density is the proven balance dial. Risk is *layer pile-on* (Infra + Deployables + Hack) diluting one grammar. |
| T2 | Quick / tactical / bloody | **4.0** | Bloody yes. Tactical yes. "Quick" is the soft spot — Ready/Reactions + condition zoo + mid-battle Events can inflate a round. |
| T3 | Tools > kills | **4.5** | Five objective shapes; kills bank resources but never win. Strongest anti-annihilation stance in the doc. |
| T4 | Terrain interactions feel natural | **4.0** | Verb/stat Interact is clean. Feature damage + "no structural collapse" + Structural Collapse *skill* is the one honesty gap. |
| T5 | Meaningful customization | **4.5** | Emergent roles, weapon construction, floating secondary growth — ownership fantasy is real. Catalogue size is the tax. |
| T6 | Simple ≠ boring | **3.5** | Combat spine earns "complex outcomes." Campaign layer is where boredom-prevention starts to look like *more systems*. |
| T7 | Anti-bloat discipline | **4.0** | Culture is excellent (Water, Proficiency, upkeep, Seeker all cut). Live surface still too wide in skills + board machines. |
| T8 | Crew growth natural | **4.5** | Post-FIX-4 track is the best version you've had. Annihilate/WND-3 skew is a Phase 2 table question, not a tenet fail. |
| T9 | Post-battle meaningful choices | **4.0** | §25.5 sequence is the right shape. Economy sink + thin structure wishlist late-game can make Settlement Phase *feel* empty. |
| T10 | Clarity & meshing | **3.0** | Master is coherent; satellite notes still lie (Progression, List Building, Events, Territory loot). Hub cannot fix contradictory paper. |
| T11 | Hub-ready bookkeeping | **4.0** | Data shapes are hub-native. Explicitly resolve "not app-dependent" vs hub: **paper-complete, hub-preferred**. |

**Overall identity health: 4.0 / 5 — still Settlements.** The spine is true. The risk is *campaign + board-machine mass* quietly turning Pillar 5 into "complex rules, complex outcomes."

---

## 2 · Per-tenet deep dives

### T1 · Terrain first — **KEEP / sharpen**

**What's working**
- §5 density (9–12) is SIM-CONFIRMED as the largest win swing in the project (~66 pts). That is Pillar 1 made measurable.
- §6 Interact verbs ride the one dice mechanic — no second resolution language.
- §12.7 scenario philosophy literally says a scenario playable on a bare table is a failed scenario.
- Settlement raids use the canvas as the board — home base *is* terrain.

**What's drifting**
- **Four board-machine layers** now sit beside "terrain": Terrain profiles · Infrastructure verbs · Deployables · Hacking. INT glues them, but a new player experiences four catalogues, not one "use the board" instinct.
- Setup-time load (declare every profile, mark every interactive tag, place infrastructure tokens) fights "activation under a minute" if the first ten minutes of every game are labeling.

**Recommendations**
1. **Publish a one-page "Board Grammar"** — Movement × Cover × Tags → Interact → (optional) Operate/Hack/Deploy. Everything else is an instance of that sentence.
2. **Cap active board machines per scenario** in the scenario sheet (e.g. Take a Hold: terminals + optional 1 infrastructure family; Power Supply is the INT showcase). Don't fire every subsystem every game.
3. Keep density as the sacred dial — never let list-building "fix" sparse boards.

---

### T2 · Quick, tactical, bloody — **KEEP bloody / watch clock**

**What's working**
- WND 1 default, melee-to-Out, Down bleed-out, Stress→Break→BugOut — lethality is structural.
- ±3 modifier cap, one attack/activation, ~2 activations/fighter — complexity ceiling is real in combat.
- Objective end conditions + 6-round hard stop prevent grind-to-table.

**What's drifting**
- **Reaction economy** (Snap Shot / Dodge / Charge / Interact / Trigger) is tactically rich and clock-expensive. Dodge alone is an opposed roll inside someone else's activation.
- **Condition + token zoo** (§10 + §28.5): Pinned, Down, Prone, Hidden, Ready, Stress beads, persistent rings, Offline features — correct, but "under a minute" dies when three tokens need updating after every shot.
- **WND 3 veterans** (L7 + Tough) on Annihilate skew ~90% in sim — doesn't break Pillar 2 on objective missions, but *does* soften "brutal and final" on kill-shaped fights. Carry into Phase 2; don't silently accept legends who shrug rounds.
- Mid-battle **Events (exactly two)** + **Twist** are fine individually; stacked with dense reactions they add "stuff happens" overhead.

**Recommendations**
1. Phase 2 table clock: target **≤90 min** including setup; if mean >100, cut one of: Events frequency, Reaction menu size, or condition markers that don't change decisions.
2. Keep Annihilate as a *stress test*, not a Season staple — Season Score already rewards territory/structures/levels, not kills.
3. Do **not** add more mid-activation opposed rolls.

---

### T3 · Tools, not just kills — **STRONG — protect this**

**What's working**
- Five shapes, all objective-primary; bottling rules; resources earned by both sides.
- INT/AGI/NRV builds are justified by scenarios (Power Supply, Hold claim, Break tests) — T6 sim already showed utility crews die on Annihilate but live on Hold.
- Terrain Search, sabotage charges, hacking Interrupt, deployables as denial — multiple win paths.

**Watch**
- If Season scoring or raid loot ever pays *more* for kills than objectives, the anti-annihilation stance erodes. Current Season Score does not — keep it that way.
- Glorious Deeds that are kill-flavored need the existing once/fighter/battle cap forever.

**Recommendation:** When writing new scenarios, require a one-line proof: "the higher-kill crew can still lose." If you can't write it, the scenario is wrong.

---

### T4 · Terrain interactions natural & impactful — **GOOD with one honesty fix**

**What's working**
- Trivial auto-pass / else 7+ is the right binary (matches your locked preference — no difficulty tiers).
- Feature Online→Offline→Destroyed is impactful without HP bookkeeping.
- Raid sabotage reuses Sabotage's charge timer — one mechanic, two contexts.

**Honesty gap**
- §6: **no structural collapse** of buildings/cover.
- §14 STR T3: **Structural Collapse** destroys 4" of Breachable terrain.
- Players will ask which walls are "features" vs "buildings." If the answer is "ask your opponent," it doesn't feel natural.

**Recommendation:** One clarifying sentence in §6: *Breachable terrain pieces and tagged Features can be destroyed; load-bearing building shells and Cover values of bulk terrain cannot.* Put Structural Collapse firmly in the first bucket.

---

### T5 · Customization without boredom — **STRONG**

**What's working**
- Roles emerge (Brawler/Techie/Medic) — never locked classes.
- Weapon construction + characteristics + one payload = toys with teeth.
- Level track: derived Primary, floating secondaries, stat-gated skill tiers — direction chosen in play (your FIX 4 intent, now in master).
- Match Play vs Campaign Start kits correctly split "showcase build" vs "grow into it."

**Tax**
- ~10 skills × 3 tiers × 5 paths ≈ **~150 skills**. That is customization *content*, but at the table it is a lookup tax unless the hub (or a printed path card) owns it.
- Roll-3-choose-1 is the anti-min-max hero — keep it; never replace with free pick from the full tier.

**Recommendations**
1. Ship **path cards** (physical or hub) as the skill UI — never expect players to browse §14 mid-battle.
2. Before Final Alpha, run a **skill cull**: merge near-duplicates called out in §29 (Knockback/Heavy Impact, Ghost Blade/Balanced, etc.). Target: each tier feels like 6–8 distinct verbs, not 10 near-twins.
3. Do **not** add crafted/manufactured weapon-origin tiers until the existing construction system has been played — Inbox desire, Pillar 5 risk.

---

### T6 / T7 · Simple-not-boring vs anti-bloat — **the central tension**

**Discipline already proven**
Cuts that protected identity: Water · per-head upkeep · Heat/Attention · HP structures · Worker Proficiency · Seeker mine · Freak-as-default · freeform Advance spend.

**Still smells like "rules for rules"**

| System | Why it might be bloat | Keep if… | Park/cut if… |
|---|---|---|---|
| **Captured / Brainwash** | Multi-phase side quest on a rare Fate band | Rescue-raid and ransom show up in real campaigns and feel like stories | First 3 Season tests never produce a meaningful Captured thread |
| **Drones + Chems (§28)** | Explicit "advanced modules"; bandwidth + dependence tracks | They create distinct INT/NRV fantasy in playtests | They only appear because the catalogue has them |
| **10 parked worker benefits** | Already parked — good | Stay parked until their host systems thicken | Someone "helpfully" unparks them for completeness |
| **Faction × Location × Territory setup stack** | Easy to forget three small bonuses | Hub auto-applies them in Battle Prep | Paper play regularly skips them → they aren't earning their words |
| **Events + Twist** | Two RNGs around one battle | Both create stories players retell | Players start ignoring one of them |

**Recommendation — Hub doctrine (resolves Out of Scope tension):**

> **The game must be paper-complete. The hub is the preferred way to carry persistence.**  
> No rule may *require* the hub to resolve. Any rule whose only comfortable home is a spreadsheet is a cut candidate.

That single sentence should go in Out of Scope §1 as a clarifying bullet under "Not app-dependent," and in the hub product brief as the design contract.

---

### T8 · Crew growth — **STRONG**

**What's working**
- Fixed track removes analysis paralysis; floating levels restore authorship.
- Stat-gated tiers unify creation and leveling (one grammar).
- Levels raise Crew Rating — growth taxes itself (anti-snowball).
- Scars / third-Scar retirement / Hardened free Level — persistence has teeth and gifts.

**Watch**
- Stat-point Level pricing still SIM-FLAGGED underpriced (esp. STR) — economic, not tenet, but cheap levels accelerate WND-3 walls.
- Campaign Start 500 CR still has list-building friction for gunlines (prior sim); if green crews can't field the fantasy, growth fantasy starts bitter.

**Recommendation:** Treat 500 CR and Level Credits as **one dial pair** in Phase 2 — don't raise one without re-checking the other.

---

### T9 · Every battle → meaningful crew *and* settlement change — **GOOD shape, soft settlement half**

**Crew half — strong:** Fate → Levels → scars almost always fire. Rosa example proves the loop in one page (§28.7).

**Settlement half — softer:**
- Early game: Med-bay / Storehouse / weapons = real choices.
- Mid/late: economy sink (§29) means Settlement Phase can become "assign the same worker, bank numbers." Storage overflow is a *partial* sink, not a decision engine.
- Structures that unlock thin systems (Scout Post, Server Core, Fabricator→arsenal, Holding Cells after worker trim) are **promises**, not toys.

**Recommendations**
1. Every shipped structure must answer: **what new decision does this create next Settlement Phase or next battle?** If the answer is only "+1 to a number," park it.
2. Add **one** expensive, exciting sink before Season end (examples to choose later — not design them now): second Generator tier · rare Fabricator blueprint · territory "fortify" spend · roster training that isn't a Level. Pick *one*.
3. Dispatch (Scout/Scavenge) is the right light touch — don't add Sabotage-by-dispatch in v1 (master already refused; keep that).

---

### T10 · Clarity & meshing — **WEAKEST score — fix before marketing the hub**

The master document is largely self-consistent after the 08-08 integrate. The **vault constellation is not**:

| Drift | Master says | Satellite still says |
|---|---|---|
| Level track | Floating stats, stat-gated skills | `Progression.md` — declared Secondary, fixed path |
| Campaign Start pyramid | Specialist ratio kept | `List Building.md` — "no ratio" |
| Events #3 | Burst main | `Events.md` — Trader's caravan |
| Loot #7 | +15 Credits | `Territory.md` — Chem dose |
| Cross-refs | promotion §26.5 | §13 still points at §27 (Events) |
| Tenet names | Vision 1–5 | Out of Scope uses different labels for 4/5 |
| AGENTS.md | — | Obsolete Leader 6 / Champion 4 / fighter 2 |

**Meshing wins already in master:** one dice · three combat levers · growth≠unpriced power · Interact breaks Hidden · raid Priority one lever · sabotage timer reused.

**Recommendation:** A single **vault hygiene sprint** (Part E of the prior audit, still pending) before any hub build that reads phase notes. Hub should ingest **only** the master + structured catalogues, never Ideas Inbox.

---

### T11 · Hub readiness — **architecturally yes**

What the hub should own (and the rules already shape as data):

| Hub module | Rules substrate | Bookkeeping it removes from the table |
|---|---|---|
| List builder | §13–16 ranks, skills, weapons, CR | Pyramid validation, exact skill counts, field cost |
| Crew tracker | §26 Levels, scars, Fate, Captured clocks | Track position, scar list, Hardened, retirement options |
| Settlement tracker | §17–22 canvas, Power, storage, workers | Caps, overflow, worker assignment, structure state |
| Campaign manager | §23–25.5, §28.6 Season | Territory states, Season Score, dispatch uses, Battle Prep bonuses |
| Battle helper (optional) | §2–12 | Reference cards, Twist/Events rolls — never required |

**Do not put in the hub as *rules*:** AI that auto-plays fighters, hidden information the opponent can't verify, or timers that replace table timing. Helper ≠ referee.

**Product contract:** if a player prints sheets from the hub and leaves the laptop home, the Season must still resolve.

---

## 3 · Systems that mesh well (protect these contracts)

1. **One dice, everywhere** — including Fate extremes (nat 1 / nat 10).
2. **Stats / Weapons / Skills** — three levers, never blurred.
3. **Growth increases decisions, never unpriced power** — territory benefits = access.
4. **Density as balance dial** — board prices what points can't.
5. **Objective > kills** — scenarios + Season Score.
6. **Same Interact grammar** for objectives, search, sabotage, hack operate.
7. **Rank gates weapons; tiers gate skills; Levels raise CR** — three anti-snowball gears that turn together.

---

## 4 · Systems that fight each other (resolve or park)

| Tension | Why it hurts identity | Proposed resolution |
|---|---|---|
| No structural collapse vs Structural Collapse skill | Feels like a gotcha | Clarify Breachable/Feature vs shell (§T4) |
| "Not app-dependent" vs hub ambition | Designers will write spreadsheet rules | Hub doctrine sentence in Out of Scope |
| Skill catalogue vs activation-under-a-minute | Lookup kills pace | Path cards + cull |
| Captured thread vs rare Fate band | High rules weight, low fire rate | Keep for Season 1 table; cut if unused |
| Campaign Start 500 vs gunline fantasy | Growth starts feeling unfair | Phase 2 dial with Level pricing |
| WND 3 vs Pillar 2 on kill missions | Legends soften brutality | Scenario mix + possible Tough/Primary-only if table confirms |
| Four board-machine catalogues | Pillar 1 becomes "INT homework" | Per-scenario subsystem budget |
| Phase notes vs master | Confusion is a rules bug | Hygiene sprint |

---

## 5 · Priority actions (ordered)

### P0 — before calling S4 "locked for hub build"
1. **Vault hygiene sprint** — banners/edits on Progression, List Building, Events, Territory, Unit Design cross-refs, Out of Scope tenet aliases, AGENTS.md rank points.
2. **Hub doctrine sentence** in Out of Scope + hub brief.
3. **Breachable vs building-shell** one-liner in §6.

### P1 — Phase 2 table (identity tests, not just balance)
4. Clock a real 6-round game with density 9–12 + Reactions + one Event. Pass: ≤90 min feel.
5. 3-battle mini-Season: every Settlement Phase must produce at least one *excited* spend (structure, gear, or dispatch that changes the next battle). If not, sink problem is confirmed in play.
6. Annihilate vs Hold with a WND-3 crew — confirm whether Season scenario weighting already solves the sim skew.
7. Dodge at the table (engine could not stress escape-LOS).

### P2 — content discipline (anti-bloat)
8. Skill cull pass (merge twins).
9. Per-scenario board-machine budget.
10. Keep Drones/Chems marked **advanced / optional** until core Season plays clean.
11. One real late-game sink — only after P1 #5 fails.

### Explicitly do **not** do next
- Unpark the ten worker benefits.
- Add crafted/manufactured weapon tiers.
- Add Sabotage-by-dispatch.
- Add difficulty tiers to tests.
- Add a second points currency.
- Deepen Captured before seeing it fire in a real Season.

---

## 6 · What to celebrate (so you don't "fix" the soul)

- Pillar 1 is not a slogan — density sims and scenario philosophy back it.
- Anti-bloat culture is rare and you're actually executing cuts.
- The three-lever combat sentence is teachable in one breath.
- Campaign Turn (§25.5) finally exists as a real loop, not a gesture.
- FIX 4 closed a real tenet bug (T3 without +6) and improved authorship.
- Objective-primary design means customization toward hackers, runners, and medics is *rational*, not cosplay.

---

## 7 · Bottom line

Settlements still reads as the game Vision describes. The combat spine and terrain-first identity are healthy. The danger is not "losing Pillar 1" — it's **winning Pillar 1 four different ways at once** while the campaign layer asks for a spreadsheet Season.

If you do only three things from this audit:

1. **Hygiene** — make every note agree with the master.  
2. **Hub doctrine** — paper-complete, hub-preferred.  
3. **Board grammar + scenario budgets** — one instinct for using the table, not four catalogues every game.

Then Phase 2 table time will stress the real remaining identity questions (clock, settlement excitement, WND-3, Dodge) instead of fighting documentation drift.

---

## Approval sheet (optional next pass)

| # | Recommendation | Do it? |
|---|---|---|
| R1 | Vault hygiene sprint (satellites → master) | ☐ |
| R2 | Hub doctrine sentence in Out of Scope | ☐ |
| R3 | §6 Breachable vs shell clarification | ☐ |
| R4 | Skill cull target (6–8 verbs/tier) before Final Alpha | ☐ |
| R5 | Per-scenario board-machine budget | ☐ |
| R6 | Keep Captured; kill only if Season 1 never uses it | ☐ |
| R7 | Keep Drones/Chems optional until core Season clean | ☐ |
| R8 | One late-game sink — only if table confirms empty Settlement Phases | ☐ |
| R9 | Phase 2 identity table pack (clock / settlement spend / WND-3 / Dodge) | ☐ |
| R10 | Reconcile tenet naming (Vision wins; Out of Scope aliases) | ☐ |

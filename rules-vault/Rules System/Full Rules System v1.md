---
type: master
title: Full Rules System v1
status: Source of Truth
adopted: 2026-08-05
revised: 2026-08-05
tags:
  - settlements/master
---
> [!success] This note is the source of truth
> Adopted **2026-08-05**. Where any other note in `Rules System/` disagrees with this
> document, **this document wins** and the other note is owed an edit. It is the draft
> that becomes the rulebook. Individual phase notes remain useful for the long-form
> reasoning behind a rule; this is the ruling.
>
> **Revised 2026-08-05** — §22 Workers: the 0–100 **Proficiency** track is **cut**. A worker
> is assigned or not, one flat benefit per structure, nothing to level. The full three-tier
> version is parked in §22 as future-supplement content. Ripples through §25.5 (no
> Proficiency-gain step), §26.4 (Reassign carries no Proficiency) and §29.
>
> **Revised 2026-08-08 — the full-rules audit is integrated.** All 15 approved items from
> `docs/SETTLEMENTS-FULL-RULES-AUDIT.md` (Ross verdict 2026-08-07, "approve everything as
> written"):
> - **§26.3 Fate:** natural 1 is always Dead, natural 10 always Hardened, modifiers capped
>   at **+2**. Fixes a real bug — a staffed Med-bay made death impossible.
> - **§26.1 Levels:** Primary is derived and permanent; **no declared Secondary** (levels
>   1/4/8 float to any stat); **skill tier is gated by the stat**, +2/+4/+6 → T1/T2/T3.
> - **§9 / Out of Scope §4:** WND is capped at **3**, logged as a deliberate tenet exception.
> - **§3 Dodge:** the winning move is **half MOV**, not full.
> - **§16:** Match Play skill counts are **exact** (one per tier reached); Campaign Start
>   keeps the Specialist ratio.
> - **§22:** ten worker benefits ship, ten are parked.
> - **§12.6:** the Seeker mine chassis is parked. **§27:** Trader's caravan → Burst main.
>   **§23:** loot entry 7 → +15 Credits.
> - **New:** §20 storage caps with a phase-end "spend it or lose it" sink · §21 trader
>   conversion rates and raid-loot 25%/cap/floor · **§28.6 The Season** (campaign end) ·
>   **§28.7** a worked founding-and-first-turn example.
>
> Sim-verified where possible: `test-bench/balance/audit_*.py`. Two items ride into Phase 2
> table testing — the FIX 4 Annihilate skew (WND 3 dominates pure-kill missions) and FIX 5,
> which the engine AI cannot currently stress.
>
> **Revised 2026-08-27 — the whole rules system is reconciled onto one scale.**
> Every price in this document now comes from the **850-Credit shipping catalogue**
> (`test-bench/points/ticks.py`, `costs/catalogue_v0.json`), and every satellite note in
> `Rules System/` was propagated in the same pass. What moved:
> - **Crew Rating is 850 / 425.** The 1000 and 500 figures are retired everywhere,
>   including the two places this document contradicted itself.
> - **Weapons run on class *bands*, not one fixed value per class** (§15) — the
>   2026-08-14 rework, which this document had never received. Damage ceiling **+4 → +5**;
>   range reaches **36"** behind four gates instead of a hard 24" wall; **Concealable is cut**.
> - **All prices reconciled** — weapons, armour, hack gear, deployables, structures,
>   Level track. A rifle is **35 Credits**, not 130; an Autoturret is **10**, not 120;
>   the HQ is **70 Materials**, not 130.
> - **Stat levels read off the measured ladder**, which is non-flat *and* stat-dependent.
>   The flat 15/point is gone, and the contaminated "16–34" underprice flag with it.
> - **Five weapon payloads are BLOCKED** (§15) — Crippling, Concussive, Blinding, Hook,
>   Toxic all measure ≤0 net because they replace Pinned, which measures +0.510. This is a
>   **rules question** (replace-not-stack), not a pricing one, and it is open.
> - **Fifteen of twenty-four deployables are marked [UNPRICED]** (§12.6) rather than
>   carrying invented numbers.
> - **Mess Hall** was the only structure with no derived cost anywhere; it is now in the
>   costing engine at **75 Materials**.
> - The **§28.7 worked example** is rebuilt on the new scale — and now shows the founding
>   Power draw correctly (the free Location structure eats the whole margin).
>
> Costing engine: `test-bench/points/` · sim harnesses: `test-bench/balance/` ·
> shipping prices: `docs/POINTS-CATALOGUE.md` · decisions log: `docs/POINTS-DECISIONS.md`.
> Consistency guard: `py -3.13 scripts/check_rules_consistency.py`.

# Settlements — Full Rules System v1

*The complete ruleset: core game format, the combat spine, fighter construction, weapons, skills, and the settlement/campaign layer, all in one document. Supersedes the earlier `Settlement-Rules-System-v1.md`, which only covered the settlement half. Built from the vault (`rules-vault/Rules System/`), the Systems and Mechanics Packet, `PACKET-TEST-RESULTS.md` sim data, and this project's working decisions.*

*Tags: **[DRAFTED]** = existing vault rule, tested at the table only informally, not "locked" until playtested for real. **[PACKET]** = packet content formally adopted. **[NEW]** = written here to close a confirmed gap. **[SIM-CONFIRMED]** / **[SIM FLAG]** = validated or flagged by `PACKET-TEST-RESULTS.md`. Section numbers include decimal insertions (12.5–12.7, 28.5) from integrating content in later passes rather than renumbering the whole document each time — sequence, not the exact number, is what matters.*

---

## 0 · The one rule everything else answers to

**Settlement growth increases decisions. It never grants unpriced power.** Every structure, worker benefit, or territory bonus earns its place by widening what a settlement can *choose to do* — never by making a fighter flatly stronger just for existing. **[DRAFTED — Game Vision]**

**Stats decide if you land it. Weapons decide how bad it is. Skills decide what else happens.** This is the combat engine's own version of the same discipline — three separate levers, never blurred into each other. **[DRAFTED — Rules Engine]**

**One dice mechanic for everything:** `1d10 + Stat + Modifiers` vs **7+**. Natural 1 always fails, natural 10 always succeeds. No second dice type exists anywhere in this game. **[DRAFTED]**

---

# PART I — CORE GAME & COMBAT

## 1 · Core Game Format **[DRAFTED]**

- **Board:** standard 3'×3'. Scenarios may vary this.
- **Deployment:** scenario-defined; default is within 6" of opposite board edges (~24" apart).
- **Player count:** 1v1 PvP is the standard format.
- **Game length:** 6 rounds, ~1.5 hours. Ends after round 6 or immediately on a scenario objective being completed.
- **Victory:** objective-driven, never on kills. The crew ahead on objectives at game end wins.
- **Resources are earned, not the win metric.** Both crews bank resources from scenario-defined sources (objectives, kills, control, Glorious Deeds — §26) regardless of who won the battle. Killing pays even when it doesn't win.
- **Miniatures:** any 28mm-scale range; larger units may use 40–50mm bases.
- **Terrain:** dense and interactive by design — see §5.

---

## 2 · The Core Test **[DRAFTED]**

```
1d10 + Stat + Modifiers  vs  7+
Natural 1 = automatic failure. Natural 10 = automatic success.
```

Used for every attack, skill test, and terrain/objective interaction in the game. Each **+1** on a stat is worth roughly **+10%** on this test, bounded 10–90% by the natural-1/10 floor and ceiling.

**Opposed tests** use the same roll for both sides — highest total wins, **ties go to the defender**.

**Armor never affects the hit** — it only reduces the Injury roll (§9). Cover protects against *being hit*; armor protects against *being hurt*.

### House conventions
- Pre-measuring is always allowed. Measurements are base edge to base edge.
- Every model has a **180° forward arc**, set by how the miniature is physically placed — no facing notches. Ranged attacks, Ready triggers, and shoot-based Reactions need the target in that arc **and** true LOS.
- **Melee ignores facing entirely** — once Engaged, either fighter attacks regardless of orientation.
- A unit is **Engaged** within **1"** of an enemy.
- Standard movement/range increments are built around 6". Always round down.

---

## 3 · Turn Structure & Activation **[DRAFTED]**

### Round structure
1. **Priority Phase** — both players roll 1d10, **+1 if you have fewer surviving models**. Highest chooses to activate first or second this round. Ties re-roll.
2. **Alternating Activations** — players alternate, activating one unit at a time.
3. **End Phase** — in order: refresh Actions/Orders/Reactions → resolve persistent conditions (Fire, Poison, etc.) → **Break tests** for every unit at 2+ Stress → score objectives/VP.

### The activation
Each activation = **one Move slot + one Action slot**.

| Slot | What it buys |
|---|---|
| **Move** | Up to MOV" (baseline 6"), any direction. Never split around the Action. Never forced. |
| **Action** | Shoot, Fight, Interact, Hide, Stabilize, etc. Not a second Move. At most **one attack per activation**. |
| **Sprint** *(both slots)* | Move up to 2× MOV", nothing else — no Shoot, no Ready. |
| **Charge** *(both slots)* | Move up to 2× MOV" into base contact, then a free melee attack at the charge bonus (§8). |

### Orders
Recruits/Fighters get none. **Specialists get 1, Leaders get 2.** An Order grants a free Action or Reaction to the issuing unit or a friendly. Orders can't chain. **Orders are issued only during the issuing unit's own activation** — a Leader can't hold one in reserve. Each unit may receive only **one Order per round**.

### Ready & Reactions
- Spend your Action on **Ready**, or receive Ready from an Order.
- At most **one Ready token** at a time. Persists across rounds until spent or cancelled.
- **Cancelled** by taking any other Action, or by being hit by an attack, hostile hack, or terrain/hazard effect.
- A Ready unit may react **once**, after an enemy finishes a Move or Action in the reactor's forward 180° + true LOS, if the trigger is: a Move **> half MOV"** ending in that arc · a finished Shoot · a finished Interact · a resolved Charge · a sprung visible trap.

| Reaction | Effect |
|---|---|
| **Snap Shot** | Normal ranged attack at the trigger, no extra penalty. Resolves *after* the enemy's action — a shooter who Downs its target first denies the reply. |
| **Charge** | Move up to MOV" into Engagement, free melee at no bonus. |
| **Throw** | Normal thrown attack, no penalty. |
| **Interact/Operate** | Doors, Lift-block/clear, buttons, reachable Infrastructure, or Interrupt an enemy hack. No Search, Repair, or Stabilize as a Reaction. |
| **Trigger** | Only your own **Remote Detonation** traps. |
| **Dodge** | When targeted by a ranged attack (any angle): opposed `1d10+AGI` vs shooter's `1d10+DEX`, ties to you. **Win** → the shot misses and you may move up to **half MOV"** (round down); the move draws no reactions; then gain **Pinned**. **Lose** → the shot hits, resolve Injury normally. |

**Catch-up:** underdog gets **+1 Priority** only — no free-hold surge. This is deliberate compensation, not an exploit: swarms out-produce elites on raw output (WND is fixed at 1 for everyone), so fewer models *should* go first.

---

## 4 · Movement **[DRAFTED]**

Basic Move: up to MOV" (baseline 6"), any direction. **Movement draws fire** — a Move covering more than half MOV" that ends in an enemy's LOS can be reacted to; a short shuffle (≤half MOV) doesn't.

**Sprint:** both slots, up to 2× MOV", nothing else. **Charge:** both slots, up to 2× MOV" into base contact, then a free melee attack at +1 (§8).

### Terrain movement
Open ground and clear paths: no test. **Low leap** (obstacle under 2" tall): no test, flat **−2" Move cost**. Everything else is an **AGI test** (`1d10+AGI` vs 7+), paid from the Move slot:

| Maneuver | Trigger | On fail |
|---|---|---|
| **Climb** | Ascending/descending Climbable terrain | Stop at last safe level; mid-climb fail = fall |
| **Jump/Leap** | Horizontal gap, or obstacle 2"+ | Fall short at the near edge, or fall if committed past it |
| **Vault** | Waist-high obstacle | Bounce off, end short |
| **Swim** | Deep water | End in the water, gain Pinned |

Difficult ground costs double movement. No job-difficulty modifiers — only skills and conditions apply.

### Disengaging
Uses your Move slot (not the whole activation): move up to MOV" out of the enemy's 1" zone. **Every enemy you were Engaged with gets a free swing at −2.** You keep your Action but **cannot Charge** afterward.

---

## 5 · Terrain **[DRAFTED]**

**Terrain is the primary weapon.** Every piece has three independent properties:

| Property | Values |
|---|---|
| **Movement** | Open · Difficult (double cost) · Impassable |
| **Cover** | Open (0) · Light (−1) · Heavy (−2) · Hidden (−3, earned not passive) · Blocked (can't be targeted) |
| **Tags** | Openable, Climbable, Searchable, Hackable, etc. |

**Terrain types** set defaults for these axes: Building, Ruin, Scatter, Environmental, Feature, Deployed — each with a typical Movement/Cover/tag profile (full table in the original vault note). Every floor of a Building needs at least one no-test route (stairs/ladder).

**Hazards** (the Dangerous overlay, triggered by ending a Move/activation inside): Fire/burning → Fire condition. Acid → Poison. Ice → AGI test or Off-Balance. Electrified → Shocked. Deep water → Swim test. Dense smoke → Blind while inside, counts as Concealing.

### Verticality
- A ranged attacker 2"+ above target ignores Light cover from the target's level (Heavy still counts).
- **Falling:** under 3" = no effect. 3"+ = Prone. 6"+ = also an Injury roll at +1 Damage per full 2" fallen, ignoring Armor. A voluntary drop may test AGI 7+ to land clean.

### Setup procedure — the single most powerful balance dial in the game
1. **Density first — 9 to 12 large features**, minimum one per each of the nine 12"×12" board squares, filled with smaller scatter until no clear firing lane crosses the board. **Twelve is a hard ceiling.**
2. Pick Type, accept/adjust Movement and Cover defaults, add Tags, mark hazards.
3. At least 2 Buildings/Ruins and real interactive pieces.
4. Check elevated-area access.

> **[SIM-CONFIRMED — `Crew Sim — Findings`]** Terrain density alone produced a **66-point swing** in win rate — bigger than any points cost could ever produce. A 4-model elite crew beats a 14-model horde 81% of the time on a sparse board and 15% on a crowded one. Parity sits at **9–12** exactly. Density is chosen *after* lists are locked and must never be open-ended.

**Settlement boards:** when a battle is fought at someone's settlement, the defender's placed structures fill the back three of the nine density squares automatically as their large features; the attacker's remaining six squares fill with neutral terrain until the board hits 9–12 total. A settlement never buys board advantage — it changes *what* fills the squares, never *how many*.

> **[NEW — raid fairness, resolved]** Raids are not meant to be fair — the defender is fighting on home ground and should have a genuine edge; that's what makes attacking risky. **The defender automatically wins all Priority ties** during a raid (normal ties re-roll per §3; in a raid, the defender simply takes it). No other asymmetry is added — the terrain/density rule above already gives the defender their built structures' tags, turrets, and Infrastructure for free, which is edge enough on top of the Priority tiebreak. Deliberately a single small lever, not a stacked pile of raid-only exceptions.

---

## 6 · Terrain Interaction **[DRAFTED]**

A unit spends its Action to Interact with adjacent terrain, stat determined by the verb:

| Verb | Stat | Resolution |
|---|---|---|
| Force door / Smash | STR | 7+, Loud |
| Lockpick / disarm trap | DEX | 7+, Quiet |
| Hack / build / repair / Search | INT | 7+ (Hacking has its own range rules, §12) |
| Steady in a hazard | NRV | 7+ |
| Climb / vault / leap / swim | AGI | Move-slot test, not an Interact |

**Auto-pass** for trivial actions with no consequence (open an unlocked door). Direct interaction needs base contact.

**Searching:** any fighter in base contact with a Searchable piece, not Engaged, not Down. INT 7+. Places a Searched token after the attempt (pass or fail) — that piece can't be searched again this battle.

| d10 | Search result |
|---|---|
| 1 | Hazard — trap/alarm/collapse, searcher Pinned, Loud |
| 2–4 | Nothing |
| 5–7 | Supply cache — roll on the default Loot table (§23) |
| 8–9 | Gear — roll on the default Loot table (§23) |
| 10 | Jackpot — 1 Resource + one gear item |

**Structural integrity of buildings/cover is out of scope** — no damaging walls or collapse. **Feature damage** (turrets, traps, cameras, alarms only) has its own mini-system: WND 1, Armor −2, Heavy cover unless attacker within 6", a successful hit takes it **Offline** (still on board, non-functional), a second hit **Destroys** it. Repair = adjacent INT 7+.

**Traps:** deploy via INT Interact (pass = armed & concealed, fail = armed & visible, nat 1 = triggers on placer). Disarm via DEX 7+ (nat 1 = boom), or hack a Linked trap via INT instead.

---

## 7 · Shooting **[DRAFTED]**

1. Declare a target in range, true LOS, forward 180°.
2. Measure range.
3. **Attack roll:** `1d10 + DEX + modifiers` vs 7+. **One roll per Attack Die** (§15) — default 1, all at full stats, all for the same Action.
4. Hit → Injury roll (§9). Miss → nothing.

**Modifiers:** Cover Light −1 / Heavy −2 / Hidden −3. Weapons rarely add to hit — only via a conditional trait like Accurate.

**A Ready enemy may Dodge** (opposed AGI vs DEX, §3) or **Snap Shot back** after your shot resolves. **Most ranged weapons can't fire while Engaged** — a Sidearm is the exception, using DEX, targeting only the Engaged enemy.

---

## 8 · Melee **[DRAFTED]**

**Engagement:** move into an enemy's 1" zone (no LOS needed) then Fight with your Action, no bonus — or **Charge** (both slots, LOS required, 2× MOV") for a free attack at **+1**.

**Melee attack (opposed):** `1d10+STR` (attacker) vs `1d10+STR` (defender), highest wins, **ties to the defender**. Some weapons/skills swap in AGI. **Facing doesn't apply** — either fighter attacks regardless of orientation.

**Losing a melee:** the loser takes the Injury roll (§9). A charged/just-engaged unit gets no charge bonus of its own.

---

## 9 · Damage **[DRAFTED]**

After a hit lands, the attacker makes one **Injury roll**: `1d10 + Weapon Damage − Armor` vs 7+.

- **Pass** → target loses 1 WND. At 0 WND: **Down** if the wound was ranged/hazard, straight to **Out of Action** if melee.
- **Fail** → no wound, but the hit still tells: **Ranged** → Pinned (+1 Stress). **Melee** → +1 Stress (Shaken) but stays Engaged, no Pinned.

Every hit does *something*. No wasted hits.

**Multi-die weapons (Attack Dice, §15):** a weapon with Attack Dice 2 or 3 rolls one attack and one Injury die *per die*, all at once, and the attacker applies **one** Injury result. **A burst inflicts at most 1 WND however many of its dice pass** — surplus passes are discarded, not banked against a multi-wound target. Every *other* hit that failed to injure still Pins. Full rule and costs in §15.

**Weapon Damage** is a small class: +0 unarmed · +1 light · +2 medium · +3 heavy (see Weapons, §16, for the full construction system and reconciled Credit pricing). **Armor** reduces Injury only: 0 none · −1 light · −2 heavy.

**Melee is decisive** — a melee kill goes straight to Out of Action, no bleed-out. **Ranged/hazard kills leave a fighter Down** (alive, prone, counts as Heavy cover vs ranged unless in the open; a melee/engaged attack auto-hits to finish it, ranged resolves normally). A Down unit must be Stabilized by the end of its **next** activation or bleeds out. Stabilize = Action + INT 7+ (−2 without a Med-Kit; a Medic skill auto-succeeds).

**A Down unit keeps its Stress** *(drafted 2026-08-29 — §11)*. It takes no Break tests while Down and sheds nothing, then returns carrying every point. Stabilized at **2+ Stress** means a Break test in the next End Phase; at **4+**, a failure removes it. **You can patch the body faster than the nerve.**

**Every unit has WND 1**, raised only by a specific skill (Tough, §14). Campaign veterans can reach **WND 2** (Level 7) and at most **WND 3** (Level 7 + the Tough skill) — the hard ceiling, logged in *Out of Scope* §4.

---

## 10 · Conditions **[DRAFTED]**

A condition is a status token. **No stacking** — reapplying refreshes duration, doesn't deepen effect. **Modifier cap: ±3** on any single roll, however many conditions are carried. Gaining a negative condition gives +1 Stress the *first* time (not on refresh); Pinned/Shaken's own +1 already counts as this, don't double it.

> **Payload rule:** a weapon characteristic that applies a condition does so **in place of** the normal non-wound result (Pinned/Shaken), never in addition. A hit does exactly one thing.

**Core combat conditions:**
- **Pinned** (ranged non-wound) — can't Move/Charge/Sprint/Disengage; must spend Move to clear; may still Shoot/Interact.
- **Down** — prone, out of the fight; ranged-only origin; Stabilize or bleed out. **Keeps its Stress and takes no Break tests while Down**, resuming them on recovery (§11).
- **Prone** — knocked flat, not an injury; can't Shoot/Charge/Sprint; standing costs the whole activation.
- **Hidden** — −3 to be hit; earned via Hide in Concealing terrain or gear/skill; lost on moving, shooting, **interacting** (any Action that resolves an Interact test — claim/loot/hack/arm/defuse, §6, §12.7), or being revealed. *(See §25 for the ruling on holding an objective while Hidden.)*

**Control conditions:** Grappled, Suppressed (counts as Pinned + can't React), Off-Balance (can't Sprint/Charge, persists until cleared), Hobbled (−2" MOV, persists until cleared), Blind (−2 on sight-based rolls, clears end of next activation), Shocked (−2 all rolls + can't React, clears end of next activation), Provoked, Snared.

**Persistent conditions** (resolve in End Phase): **Fire** (Injury roll at +1 Damage ignoring Armor each End Phase; extinguish with an Action). **Bleed** (lose 1 WND each End Phase unless treated — at WND 1 this is a two-round death clock, the harshest condition in the game). **Poison** (−1 all rolls; STR 7+ each End Phase to end).

**Nerve states** (from Morale, §11): Shaken, Bolt, Broken, BugOut, and the skill-induced **Fight** state.

**Marker/device states** (not conditions, no Stress, don't count toward the modifier cap): Spotted, Jammed, Overloaded, Compromised, Linked.

---

## 11 · Morale **[DRAFTED]**

Every hit that fails to wound generates **Stress** instead — this is the entire fear/suppression system, all running through one number.

- **1+ Stress = Shaken:** flat −1 to all rolls, always-on, doesn't stack, no test. Carries into your next turn — Stress never clears on the round you gained it.
- **2+ Stress:** a **Break test** in the End Phase: `1d10 + NRV − (Stress−1)` vs 7+. Shaken's −1 does **not** double-apply here.

| Fail margin | Result |
|---|---|
| 2 | **Bolt** — flees toward nearest board edge, hugging cover |
| 3 | **Broken** — freezes, cannot act |
| 4+ | **BugOut** — routs off the board, removed from play |

**Bottling** (voluntary concession) and full Recovery timing rules live in the vault note; the short version: a unit at exactly 1 Stress sheds it in the End Phase only on a round it took no new Stress. BugOut can't be rallied — only prevented at the moment of failure by specific skills.

### Stress and Down — persistence **[DRAFTED 2026-08-29 · pending playtest]**

**Stress persists through Down.** A unit reduced to 0 WND keeps every point it had; going Down is not a rest.

- **A Down unit does not take Break tests** — it is out of the fight, so it cannot Bolt, freeze or rout while lying there. Its Stress freezes with it, and it sheds nothing either.
- **Stabilize returns the fighter with its Stress intact** (§9), and it tests normally from then on. Recovered at **2+ Stress** → Break test the next End Phase. At **4+**, a failure removes it.
- **No new test, no new trigger, no new token.** The End Phase Break test already does all of it. This rule is the *absence* of a clearing step, which is exactly why it is free.

> **Why it was ruled in.** The rules had never said either way, and this was never an Attack Dice question — with **no** Attack Dice in the game a downed model already carries **0.66 Stress** and sits in Break-test range **15.5%** of the time. A single shot that Downs you carries none (its one pass *is* the wound); all of it comes from everything that missed or failed first. Measured in `Stress Persistence — Sim Findings`.
>
> Cost at NRV +2: **8.8%** of revived fighters fail their first Break test, **1.9%** BugOut immediately — about **one revival in fifty-three**. Story frequency. It also makes Stabilize a real decision rather than an automatic yes.
>
> **Watch the stacking, not the rule.** If Attack Dice later also converts surplus injury passes into Stress (§29), a downed model's Stress roughly **2.2×** and wasted revivals go from ~1-in-11 to nearly **1-in-4**. Adopt one at a time, this one first. It also compounds the death-spiral risk flagged in `Dice Mechanic — Sim Findings` §7. **Valve held in reserve, deliberately not pre-applied:** *"a Stabilised fighter returns Shaken, however much Stress it had."*

> **[Vision-doc note, preserved for the record]** The original design notes for this project proposed two additional nerve states beyond Bolt/Broken — a "Freak" (attack nearest friend or foe) and a forced "Fight" (berserk charge). Two similar softeners to the current three-tier system were sim-tested and **both broke the game**. The current system's skill-gated **Fight** state (Fanatic and similar Tier-3 skills only) is the surviving, safe version of that idea — never a routine morale outcome.

---

## 12 · Hacking **[DRAFTED — fully drafted in the vault, no changes]**

v1 is deliberately small: hack a terminal to control its Linked features; an enemy at another terminal can Interrupt you at the cost of Overloading their own.

1. **Declare** the terminal and the Linked feature (must be in a legal range band, max 24").
2. **Roll** `1d10 + INT − range band` vs 7+.

**Interrupt:** an enemy in base contact with another live terminal may Interrupt as it happens (not after) — ignores the forward-arc/LOS requirement, costs no Ready token. Pass → jams the one attempt, interrupter's terminal goes Overloaded (down till start of next turn). A different unit can still hack the same target terminal again.

No hacker-vs-hacker minigame in v1 — a deeper system is drafted and parked for later.

---

## 12.5 · Infrastructure **[DRAFTED — new integration]**

The operable machines built into the city — cranes, doors, bridges, shutters, lights, vents. **Infrastructure reshapes the board. It does not exist to hurt people** — that job belongs to Deployables (§12.6). Any harm infrastructure causes is a rare, secondary effect of a board change.

**Infrastructure vs. Deployables:**

| | Infrastructure | Deployables |
|---|---|---|
| What | Fixed board parts (crane, door, bridge, generator) | Gear a unit carries (turret, mine, tripwire) |
| Job | Reshape the battlefield | Deal or deny damage |

Turrets, mines, and traps are always Deployables, never Infrastructure.

### The five categories, eight verbs
Every feature is [category] + one or two of eight board verbs + an optional damage keyword:

**Mobility** (Create/Remove Route, Change Elevation) · **Access** (Open/Close Path) · **Visibility** (Block/Clear LOS) · **Manipulation** (Shift Terrain, Create/Remove Cover, Displace) · **Utilities** (Field a Zone).

Each verb is a toggle with a defined "caught in the change" clause (e.g. Open/Close Path: a model caught in a closing gap is Displaced 1"; a heavy blast door prints CRUSH instead).

### Damage — exactly two keywords, nothing else
- **FALL** — resolve per the normal fall rules (§5): under 3" nothing, 3"+ Prone, 6"+ Injury roll.
- **CRUSH** — a hazard Injury roll: `1d10+3` vs 7+, ignoring Armor; a wound → Down (never straight Out — the board maims, it doesn't execute).

Everything else a feature does is pure repositioning or an existing condition (Deep water, Dense Smoke, etc.) — never a new one invented here.

### Operating a feature — three ways
1. **Remote hack:** `1d10+INT−range band` vs 7+ (same range bands as §12). Can be Interrupted.
2. **Manual operation:** base contact, DEX Interact 7+ (STR for heavy manual mechanisms). **Cannot be Interrupted** — the payoff for exposing yourself.
3. **As a Reaction:** a Readied unit may operate one reachable feature as its Reaction when an enemy's move/action triggers the moment.

**Feature state:** everything starts Powered Down (inert). Operating it sets or flips its state; either crew may flip it back — that back-and-forth *is* the contest. Terminals/controls can never be destroyed — only Overloaded via an Interrupt.

### Feature catalogue (representative, not exhaustive)
Cargo Crane (Shift Terrain/Cover/Displace — CRUSH or Displace) · Blast Door (Open/Close Path — CRUSH or Displace) · Roller/Security Gate (lighter door, Displace only) · Retractable Bridge (Create/Remove Route — FALL if retracted under someone) · Elevator/Cargo Lift (Change Elevation) · Conveyor Belt (carries a model +4"/round while on it) · Window Shutters (Block/Clear LOS) · Floodlights (strip Hidden in the lit zone) · Flood Gates (Field a Zone — Deep water/Difficult) · HVAC/Gas Vent (Displace + Dense Smoke) · Trash Compactor (the one overt hazard — CRUSH, always scenario-flagged) · Power Generator/Junction (macro-toggle — powers a whole zone on/off; can't be destroyed, only Overloaded).

### Setup
**Standard battles:** fixed by the scenario. **Custom battles:** one feature per building guideline, assigned alternately/mirrored, on roughly half the eligible buildings (matches the terrain density band). **Settlement battles:** the defender's built structures carry their own printed tags as their feature — no separate assignment; the attacker's six squares assign normally.

---

## 12.6 · Deployables **[DRAFTED — new integration]**

The gear a crew **builds and plants on the board** to deal or deny damage — turrets, mines, traps, and beacons. Bought like a weapon, carried by a fighter, set up with an INT test. This is where INT's combat role lives now that v1 hacking only flips switches.

**Design contract:** inherits the weapon contract (§15) — a deployable applies conditions, never defines them; a deployable attack does exactly one thing, wounds or delivers its payload, never both; obeys the same +4 Damage ceiling and ±3 modifier cap as everything else. **One deploy = one Action.** **INT builds and repairs; DEX disarms.**

- **Bought like equipment**, taken against a fighter's equipment allowance in List Building. **Persists across the campaign** like a weapon — spent or destroyed only for the rest of the *current* battle, returns intact next battle.
- **Two shapes:** spent-on-trigger (mines, traps — fires once, then gone) and standing hardware (turrets, beacons — works every round until destroyed, repairable once).

### Deploying
`1d10 + INT + Build rating` vs 7+. **Pass** → active (armed & concealed, or online). **Fail** → placed but exposed/inert. **Nat 1** → backfires on the deployer, or standing hardware is Destroyed outright.

**Build rating** (printed on the item, intrinsic — not table-assigned difficulty): Simple +1 · Standard 0 · Complex −1 (most turrets/beacons) · Intricate −2 (flagship hardware).

**Destruction/repair** reuses the Feature-damage engine (§6): WND 1, Armor −2, Heavy cover unless attacker within 6". One hit → Offline (repairable, INT 7+ adjacent). Second hit while Offline → Destroyed for the battle.

> **[REPRICED 2026-08-27 — the gear scale, at last]** The ×10 conversion these costs used to carry priced deployables against the **body** scale, which is why a Burst Turret cost 189% of the Fighter deploying it. They are now derived the way the costing engine states: **a deployable prices at the weapon class it mounts** — the persistence premium and the immobility/destructibility discounts cancel — and every entry is held under the gear:body cap. Source: `test-bench/points/ticks.py` · `DEPLOYABLE_CREDITS`.
>
> **Nine of twenty-four entries are priced.** The rest are marked **[UNPRICED]** and are *not legal to field* until the engine carries them. That is deliberate: an untagged number is the exact defect the points rebuild exists to remove, and inventing fifteen of them here would reintroduce it. The derivation rule above is written down, so pricing them is a short job — it just has to happen in the engine, not in this document.

### Family A — Turrets *(standing, repairable, both equipment slots)*
Holds a Ready reaction; auto-fires once/round at the first enemy that Moves/acts in range+LOS, no facing (360°), never moves. An enemy hacker can hijack, deactivate, or turn one against its own side.

| Turret | Build | Range | Credits | Profile |
|---|---|---|:--:|---|
| Autoturret | Complex −1 | 18" | **10** | 1 shot/round, Damage +3 — a sidearm on a tripod |
| Sniper Turret | Intricate −2 | 24" | **25** | 1 shot/round, Damage +3, +1 to hit — a rifle on a tripod |
| Burst Turret | Intricate −2 | 18" | **20** | 2 shots/round, Damage +2 each |
| Blast Turret | Complex −1 | 12" | **15** | 1 shot/round, Damage +3, Blast 2" |
| Reinforced Turret | Complex −1 | 18" | **15** | 1 shot/round, Damage +3, always Heavy cover (the within-6" Open clause doesn't apply) |

### Family B — Mines *(spent-on-trigger, concealed, one slot)*
Built like a weapon: chassis + one payload.

**Chassis:** Proximity (**5 Cr**, 3" template, triggers on enemy Move inside) · Remote (**[UNPRICED]**, 6" trigger radius, owner command-detonates as a Reaction — buying one grants 1 live + 3 dummy markers as a bluff kit). *(The **Seeker** chassis is parked — see the rejected log in §15.)*

**Payload (buy exactly one) — all five [UNPRICED].** Explosion (Damage +3, Blast) · Fire (Blast Damage +2 + Fire hazard) · Poison (3" Poison hazard, no direct Injury) · Shock (Blast, no Injury — Shocked+Blind) · Smoke (no damage, 3" Dense Smoke).

> **Why the payloads are held rather than guessed.** A mine payload's natural neighbour is the weapon characteristic it mirrors — and three of those five characteristics (Toxic, and the Blast/Shock pair's partners) sit inside the **blocked-payload problem** in §15. Pricing a mine off a trait that measures negative would bake the same defect into a second catalogue. These unlock the moment the payload rule is ruled on.

### Family C — Traps *(spent-on-trigger, concealed, one slot — deny movement, not kill)*
Trip Wire (30 Cr, 1" trigger → Prone) · Spike Strip (40 Cr, 3" area, Difficult + Hobbled) · Covered Pit (50 Cr, concealed 2" hole → FALL + Snared) · Leg Clamp (50 Cr, 1" trigger → Snared) · Razor Barrier (40 Cr, 3" Impassable wall, Force STR 7+ to break through, Hobbled on success).

### Family D — Beacons *(standing, repairable, both slots — 6" aura)*
**Two rules keep beacon-stacking honest:** an aura obeys the ±3 cap and doesn't stack with itself; **a model benefits from at most two friendly beacon auras at once.**

Munitions Beacon (80 Cr, +1 Injury for allies) · Targeting Beacon (80 Cr, +1 ranged hit for allies) · Aegis Beacon (80 Cr, −1 on enemy Injury rolls against allies) · Cover Beacon (60 Cr, allies count as Light cover) · Cleansing Beacon (80 Cr, clear one condition/round, acts as a Med-Kit) · Revive Beacon (120 Cr, recovers one Down ally to Prone/round — Down only, a melee kill stays dead) · Dread Beacon (70 Cr, the one enemy-facing aura — +1 Stress on entry, −1 Break tests while inside).

---

## 12.7 · Scenarios **[DRAFTED — new integration]**

**You win by objectives, never by kills.** A wiped or BugOut crew can no longer contest or score, so combat is the *tool*; the objective is the *win*.

**Design philosophy:** objective-primary (every scenario below can be lost by the side that killed more models) · terrain is mandatory, not scenery — a scenario playable on a bare table is a failed scenario · objectives are interactive terrain, using the same core test and verbs as everything else · five shapes, not five maps — future scenarios reskin a shape rather than invent new resolution mechanics.

### Shared rules
- **Objectives are Interacts** — base contact, costs the Action, resolves as `1d10+Stat` vs 7+. Claim/activate/connect → INT. Loot/search → INT + a spent Searched token. Arm/defuse → INT to arm, DEX to defuse. Open a route → STR/DEX/INT per the lock type.
- **A Down, Out, or Broken unit cannot hold, claim, or score.** Shaken units act normally at their −1.
- **Holding:** a standing friendly within 3" and no enemy within 3". **Contested** (both within 3") → nobody holds it that round.
- **Scoring happens in the End Phase** — no scoring in Round 1.
- **Wipe:** a crew at zero standing models can no longer contest/score; the opponent plays on to bank objectives. Both wiped same round → whoever's ahead on objectives at that moment wins.
- **Bottling** (voluntary concession): Rounds 1–3, only a fighting withdrawal off your own edge or an accepted surrender ends it early. **Round 4+, a declared bottle ends the game immediately as the opponent's win**, regardless of score.
- **The Twist** — roll 1d6 at setup: 1 Blackout (LOS capped 12") · 2 Live Board (one hazard active from setup) · 3 Reinforcements (Round 3 End Phase, each crew returns one Down model) · 4 Scavengers (neutral bonus objective, centre) · 5 Foul Weather (open ground is Difficult) · 6 Clean (no twist).

### The five scenarios

1. **Take a Hold** *(Control)* — 3 terminals on the centreline, claimed via INT 7+. Score 1 VP/held terminal each End Phase, Rounds 2–6 (15 VP ceiling). Most VP after Round 6 wins.
2. **Escort** *(Mobile, asymmetric)* — Attacker moves a Caravan (no activation of its own, indestructible, only delayable) 6"/Action toward the far edge; Defender gates a chokepoint they can close and the Attacker must force/hack back open. Attacker wins on exit; Defender wins if it hasn't exited by Round 6.
3. **Raid** *(Retrieve)* — each side hides 3 loot caches in their own half (one secretly a 2-VP Jackpot); score by looting the *enemy's*, not defending your own. Most enemy loot value by Round 6 wins.
4. **Sabotage** *(Timer, sudden death)* — each side nominates a target building; the enemy arms a charge (INT 7+) that detonates after surviving 3 End Phases armed unless defused (DEX 7+, nat 1 = it goes off now). Detonating the enemy's building wins immediately.
5. **Power Supply** *(Network, INT-primary)* — a central Transformer hub + 4 Power Supply nodes; claim the hub (INT 7+), then run lines outward to uncontrolled nodes within 8" (INT 7+), or sever an enemy's line (DEX 7+ or damage it as a Feature). First to hold hub + 2 connected supplies at an End Phase wins.

Full scoring-clock math (why each scenario resolves inside 6 rounds) and the exact objective/deployment/twist tables live in the source note; the shapes above are complete enough to run a game.

---



---

# PART II — BUILDING A FIGHTER

## 13 · Unit Design — the stat line **[DRAFTED]**

Five path-stats, plus two fixed values:

| Stat | Governs |
|---|---|
| **WND** | How many serious hits before Down/Out. Fixed at **1** for everyone; raised only by the **Tough** skill. |
| **MOV** | Inches per Move. Fixed at **6"**; raised only by the **Fleet** skill. |
| **STR** | Melee, breaching, hauling, lifting, carrying |
| **AGI** | Climbing, jumping, dodging, escaping, repositioning |
| **DEX** | Ranged combat, throwing, lockpicking, trap work, delicate equipment |
| **INT** | Hacking, crafting, repairing, medicine, searching, terrain ID |
| **NRV** | Mental state under pressure — Stress and Break tests |

Each **+1** ≈ +10% on a core test, bounded 10–90%. **Max is +6.**

| Value | Meaning | Tier |
|---|---|:---:|
| −1 | Impaired | — |
| 0 | Civilian baseline | — |
| +1 | Capable (a "dabble" — no tier, no skill) | — |
| +2 | Skilled | **T1** |
| +4 | Veteran | **T2** |
| +6 | Peak/master | **T3** |

### Rank vs Role
**Rank** = command slot, restricted, sets stat points/skills/Orders/caps. **Role** (Brawler, Techie, Medic…) is **emergent** from stats/skills/gear — unlimited, narrative, never restricts fielding.

### Ranks

| Rank | Stat pts | Tier caps | Orders |
|---|:---:|---|:---:|
| **Recruit** | 3 | none — no tiered stat | 0 |
| **Fighter** | 5 | 2× T1 | 0 |
| **Specialist** | 7 | 1× T2 · 2× T1 | 1 |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | 2 |

**Starting skill count now depends on which game you're building for, not rank alone** — a richer kit for a one-off Match Play crew, a leaner one for a fresh Campaign Start crew that's meant to grow. Full breakdown and Credits costs for both in §16.

A rank grants **more points than can spike into one stat** — tier caps force the spread, so a Fighter (5 pts, max 2×T1) builds something like `STR+2 / INT+2 / AGI+1`, not one giant number. Only a **Leader** ever reaches T3. Recruits get no tiered stat and no skills — pure chaff/screen bodies, not a melee force. **Rank is also a weapon gate** (§16) — a Recruit physically cannot hold a rifle. **Rank rises only via deliberate promotion into an open slot** (§27), never automatically.

**Fielding costs live in §16 (List Building), on the 850-Credit scale — the old 5/8/16/24 ladder is deprecated, and so is the 1000-Credit scale that replaced it.**

---

## 14 · Skill Paths **[DRAFTED — full catalogue]**

Skills are the **third lever**: stats decide if you hit, weapons decide how bad, **skills decide what else happens**. A skill is a verb or a conditional exception, never a flat stat bump.

**A stat hands you a skill every time it reaches a tier.** No separate skill pool. A stat at +4 grants both its T1 and T2 skill; at +6, T1+T2+T3. You choose the specific skill from that stat's path at that tier (may take a lower tier if preferred). Picked at crew-build, and again in campaign whenever an Advance tips a stat into a new tier.

| Stat | Path | Covers |
|---|---|---|
| **STR** | Combat / Muscle | melee, force, grappling, breaking, hauling |
| **DEX** | Shooting / Perception | ranged, aim, spotting, trick shots |
| **AGI** | Movement / Acrobatics | climbing, dodging, repositioning, escaping |
| **INT** | Expertise / Knowledge | hacking, traps, medicine, tech, terrain |
| **NRV** | Bravery / Morale | rallying, resisting fear, reckless aggression |

**Design contract:** T1 = reliable options and narrow exceptions. T2 = role-defining actions. T3 = campaign-earned, fight-swinging. Any modifier from a skill is conditional, capped at ±3. Difficulty is always a modifier on 7+, never a raised target number. At most one attack per activation unless a skill explicitly overrides it.

### Combat / Muscle (STR)
**T1 — Good:** Heavy Hands (+1 melee vs Pinned/Grappled) · Knockback (push 2" after a melee win) · Breakdown (auto-open/destroy adjacent Breachable) · Deadlift (carry Movable terrain at half MOV) · Strong Arm (2× thrown range) · Grapple (opposed STR replaces attack) · Bodyguard (redirect an attack to yourself once/round) · Rooted (ignore forced movement on a STR test) · Pack Mule (carry without Move penalty, can Sprint not Charge) · Doorstop (contest a door with opposed STR).

**T2 — Great:** Muscle Override (force a powered/locked door, Loud) · Human Shield (grappled enemy blocks LOS as Heavy cover) · Super Slam (failed-injury Charge → Suppressed not Shaken) · Squeeze (auto-hit a Grappled target) · Come Along (drag a Grappled enemy at full MOV) · Disarm (forgo Injury to strip a held item) · Breach and Clear (move 3" through a door you just opened) · Power Position (move/rotate adjacent Movable terrain 3") · Fireman's Carry (carry + Stabilize a Down friendly at full MOV) · Clinch (stop a Disengage you hit).

**T3 — Amazing:** Tough (**+1 WND** — the only way to raise it) · The Muscle (+2 Injury on first Charge hit) · Slam & Throw (place a Grappled enemy anywhere within 5", Pinned) · Falcon Punch (push 4" on Charge hit, Pinned on contact) · Wrecking Crew (bonus −2 melee attack if Charge downs the target) · Juggernaut (Charge through a door, destroying it) · Crushing Hold (failed Grapple escape → Pinned + Bleed) · Living Barricade (redirect a saved shot to yourself) · Structural Collapse (destroy 4" of Breachable terrain, Pin everyone within 2") · Too Angry to Drop (ignore a Pin for 1 Stress).

### Shooting / Perception (DEX)
**T1 — Good:** Long Barrel (+5" rifle range if stationary — *superseded by Long Range characteristic, needs a rewrite*) · Ready to React (pre-emptive Ready vs Charges) · Bank Shot (miss-by-1 vs cover → target Pinned) · Sharp Eyes (Spot at 18") · Muzzle Flash (auto-Spot a shooter within 24") · Covering Fire (lane suppression) · Called Shot (forgo Injury to disarm/Hobble) · Shoot and Shift (2" repositioning after firing) · Crossfire (Pinned target that fails Injury → Suppressed) · Tripwire Eye (shoot a trigger from range).

**T2 — Great:** Sniper (12"+ miss-by-1, stationary → Pinned) · I See You (Hidden penalty −3→−2 vs Spotted targets) · Lookout (Spot for allies too) · One in a Million (shoot a trigger at max range) · Kill Lane (3"-wide reaction lane) · Relocation Drill (3" move after firing from cover) · Pin Them Down (failed Injury → Suppressed) · Breach Window (auto-Spot on ally-opened terrain) · Running Read (auto-Spot after a 5"+ move) · Calm Under Fire (Pinned doesn't block Ready/Spot/trigger Actions) · Last Known Position (softer Hidden penalty against tracked targets) · Controlled Burst (forgo Injury for Suppressed + 2" push).

**T3 — Amazing:** Dead Eye (+1 hit if stationary, no cover on target) · Quick Shot (second attack at −2, no Reactions that round — *the single biggest DPS lever in the game per sim*) · Gunslinger (two targets, dual pistols, at −2 each) · Counter-Sniper (free Spot + Ready vs 18"+ attackers) · Patient Overwatch (Ready an area, not a target) · Thread the Gap (reduce cover penalty through a narrow gap) · Forward Observer (Spot for the whole crew within 12") · Shoot the Supports (destroy terrain via shooting).

### Movement / Acrobatics (AGI)
**T1 — Good:** Sure-Footed (auto-pass unstable-ground tests) · Like a Cat (reduce fall distance by 3") · Weave (−1 to melee attacks against you after moving) · Leaper (3" gap for free, +2 on longer jumps) · Vault (waist-high obstacles free) · Low Profile (3" move while Hidden without breaking it) · Quick Hands (interact during your Move) · Break Contact (extra 3" after Disengage) · Rescue Grip (carry a Down friendly without Move penalty) · Scramble (2" free move on becoming Pinned).

**T2 — Great:** Houdini (evade a 12"+ shot, become Hidden if LOS breaks) · Sidestep (evade a Charge) · Water Walker (treat shallow water as open) · Slide (pass through an enemy's space mid-move) · Double Dash (Sprint on Action slot only) · Fleet (**MOV 8" instead of 6"** — the only way to raise it) · Parkour Route (combine terrain maneuvers into one test) · Grab and Go (3" move after grabbing an objective/friendly) · Feint (+2 melee after a 3"+ approach from outside LOS) · Leg Sweep (forgo Injury for Off-Balance).

**T3 — Amazing:** Ghost Blade (**use AGI instead of STR for melee**) · Dual Wield (attack with both one-handers, second at −2) · Trading Spaces (swap positions after a melee win) · In-N-Out (free Disengage + 3" after a Charge hit) · Vanishing Point (become Hidden after a concealed Sprint) · Extraction Drill (Sprint while carrying a Down friendly) · Wall Runner (cross a 3"-high obstacle free) · Cornering Charge (ignore Difficult ground on a Charge) · Reversal (3" free move after an enemy misses in melee) · Action on the Run (an Action mid-Move).

### Expertise / Knowledge (INT)
**T1 — Good:** Hacker (basic terminal access) · Locksmith (lock/unlock without damage) · Trapper (arm/disarm/reposition traps) · Medic (auto-Stabilize, remove Bleed/Poison) · Camouflage Drill (extend Hide to an adjacent ally) · Loop Camera (blind a camera to your crew) · Jury-Rig (temp-restore a damaged Powered device) · Threat Scan (reveal Hidden hazards in a 6" area) · Jam Signals (Jam a device/trap) · Read the Objective (learn an objective's defenses).

**T2 — Great:** Computer Whiz (hack a Linked device remotely) · Turret Tamer (hack and fire a Linked turret) · Lockdown (lock up to 3 Linked doors) · Field Surgeon (restore a Down fighter to 1 WND at −2) · Counter-Hack (Interrupt without Overloading) · Trap Relay (chain up to 3 linked traps) · Power Broker (disable one Linked system, overcharge another) · Forensic Sweep (identify last interaction at a site) · Tactical Uplink (grant 2 allies immunity to Blind/Shaken for one Action) · Shepherd Alarm (suppress/redirect one alarm trigger).

**T3 — Amazing:** Mastermind (operate 2 device functions on one test) · Kaboom (weaponize a hazard) · Blackout Protocol (disable a whole Linked zone at −2) · Rewrite Killbox (turn enemy turrets against them) · Trauma Reset (full Down recovery at −3) · Ghost the Network (invisible to cameras/alarms/logs) · Fortify Objective (arm an objective's defenses) · Minefield Conductor (control up to 3 electronic mines) · Predictive Model (pre-emptive Stress removal or Pin) · Camo King (Hide a group even while observed).

### Bravery / Morale (NRV)
**T1 — Good:** Steady (remove 1 Stress/activation) · Rattle-Proof (ignore first Stress/round) · Battle Cry (+1 Stress on a melee-engaged enemy) · Dig In (stay still → Braced) · Keep Moving (move an ally 3" as an Action) · Stare Down (opposed NRV → enemy Stress + Cowed) · Feed the Anger (+1 Stress for +1 melee, ignore Shaken) · Drag Clear (reduce Stress from a nearby Down event) · Count Breaths (remove 2 Stress for a passive activation) · Buddy Check (remove 1 Stress for standing together, passive).

**T2 — Great:** Rally (remove 2 Stress or end Bolt/Broken) · Fearless (no Stress from seeing an ally Down) · Bloodlust (remove 3 Stress on a melee kill) · Talk Them Down (soften a failed Break by one step, +2 Stress to you) · Snap Out of It (end a condition on an ally, +1 Stress to them) · Take It on Me (absorb up to 2 Stress from an ally) · Dare Me (Provoke an enemy) · No One Left (carry a Down ally without a free-swing Disengage penalty) · Hard Case (first condition/round costs no Stress) · Lead from the Front (Order recipient also removes 1 Stress).

**T3 — Amazing:** Iron Will (auto-pass one Break test/game) · Fanatic (a failed Break → Fight instead of Bolt/Broken) · Unbreakable (reduce first Stress/round for the whole crew within 6") · Last Command (issue an Order the instant you go Down, once/game) · Stand Your Ground (save an ally from a failed Break, once/game) · Terrify (opposed NRV → enemy Stress + Frightened) · Master the Moment (one Order affects two allies, once/game) · Walk into Fire (redirect a ranged shot to yourself) · Red Mist (+3 Stress for +2 melee, ignore Shaken, can't Rally/receive Orders that activation) · Clear Heads (a natural-10 Break test clears Stress for the whole crew within 6").

---

## 15 · Weapons — Construction System **[DRAFTED mechanics · prices from the 850-Credit shipping catalogue]**

Weapons are **built, not bought off a shelf**: pick a Class, spend Credits on Characteristics, name the result.

> **Design contract:** (1) a weapon never grants an effect a skill grants — weapons do damage/range/armor/conditions/noise/concealment, skills do extra actions/reactions/exceptions/positioning. (2) Weapons apply conditions, never define them (§10). (3) A hit does exactly one thing — wounds, or delivers its payload, never both. **This contract is per DIE, not per Action:** a multi-die burst (Attack Dice, below) rolls the contract once per die, and a whole burst still inflicts at most **one wound**.

### Weapon classes — the class is an ENVELOPE, not a value

**The class sets the Damage and Range *bands*; the weapon picks inside them and pays for what it picked.**

```
weapon cost = class base (slots) + Damage steps + range + characteristics − drawbacks
```

| Class | Damage | Range | Cheapest build | Min rank | Always has |
|---|:--:|:--:|:--:|---|---|
| Unarmed | +0 | melee | **0** | Any | — |
| Light Melee | +1 | melee | **0** | Any | the free basic loadout |
| One-Handed Melee | **+1 to +3** | melee | **0** | Any | — |
| Heavy Melee | **+2 to +4** | melee | **10** | Specialist | Two-Handed |
| Thrown | **+1 to +2** | 8" | **5** | Any | usable in melee too; not Loud; exclusive to Blast/Smoke |
| Sidearm | **+1 to +3** | 6"–12" | **5** | Any | may fire while Engaged, Loud |
| Standard Ranged | **+2 to +4** | 12"–36" | **15** | Fighter | Two-Handed, Loud |
| Heavy Ranged | **+3 to +5** | 12"–36" | **25** | Specialist | Two-Handed, Loud |

> **Why bands, and why this replaced one fixed value per class (2026-08-14).** A fixed value made weapon class a global damage tier: a .22 and a Magnum could not both be One-Handed, and a snub-nose and a long-barrel could not both be Sidearms. It also crushed the damage axis flat — Standard Ranged, Heavy Melee and Heavy Ranged all sat at +3 against a +4 cap, so a basic rifle, a great axe and a machine gun shared a tier with one step of headroom.
>
> The bands **overlap deliberately**: Heavy Melee overlaps the top of One-Handed and reaches higher; nothing shoulder-fired is a .22, so Standard Ranged floors at +2; Heavy Ranged floors at +3.

**Damage stops at +5.** Armour only runs to −2, and the ceiling is what stops the armour ladder becoming decorative. **Only Heavy Ranged reaches +5.**

**Range reaches 36", and everything past 24" is GATED, never priced.** Deployment zones sit 24" apart, so a 24" weapon fires from its own deployment zone on turn one and a **36"** weapon fires from **12" behind it**, covering the whole board from a square the enemy needs a round of sprinting to threaten. That is a **threshold**, and no points cost can balance a threshold — the sim found an uncapped long-range crew beating every other list by **13–30 points**, larger than any single atom in the catalogue. So past 24" a weapon must clear **four gates**:

| Gate | Rule |
|---|---|
| **Manufactured only** | Cannot be crafted at **any** Workshop tier. Loot and raid spoils only. |
| **Limit 1 per crew** | The finding was a *list archetype*; this destroys the archetype rather than taxing it. |
| **Specialist or above** | The carrier is an expensive body in its own right. |
| **Steep price** | The cost step accelerates sharply across 24". |

A 36" rifle is a **rare, expensive, found weapon a crew builds a plan around** — never standard kit. All four gates are enforced in the costing engine, not merely written here.

**Rank gates the class:** Recruit → Unarmed / Light Melee / **One-Handed Melee** / Sidearm / Thrown. Fighter adds **Standard Ranged**. Specialist adds Heavy Melee + Heavy Ranged. Leader → everything. **A Recruit still physically cannot hold a rifle** — that is the gate doing the load-bearing work; a machete is not.

### Attack Dice — the multi-shot axis **[RULED 2026-08-29 · sim-priced]**

Every weapon has an **Attack Dice** value, **default 1**. Unlisted on a weapon card means 1; it needs no catalogue line. A weapon with Attack Dice 2 or 3 fires that many shots for **one Action**.

**Resolution — roll the whole burst at once, then apply ONE result:**

1. Roll **one attack roll per Attack Die**, all together. Each is the normal `1d10 + DEX + modifiers` vs 7+, at **full stats** — no diminishing to-hit, no recoil penalty.
2. Every die that **hit** rolls its **Injury die** (§9). Roll them together.
3. The **attacker chooses one** of those Injury results to apply. A pass means the target loses **1 WND**; a fail means **Pinned (+1 Stress)**.
4. **Every other hit that failed to injure also applies Pinned (+1 Stress).** A burst that lands and does not wound still suppresses. *(Sub-ruling flagged in §29 — see below.)*
5. **One Action, whatever the dice count.**

> **A burst can only ever inflict one wound.** However many dice hit and pass, the Action takes the target down **1 WND** — never more. This is the load-bearing half of the rule: it caps overkill at zero on a WND-1 body, and it means **no burst can shortcut a Leader**. A 3-die weapon cannot take a WND-2 or WND-3 veteran from full to Down in a single Action — measured at exactly **0%**, by construction, against **29.5%** (WND 2) and **4.7%** (WND 3) if surplus wounds were allowed to stack. Attack Dice **shred rank-and-file and do not melt characters.**

*Worked example.* A 3-die weapon fires. All three hit. The target's three Injury rolls come up **one pass, two fails**. The attacker takes the pass: the target goes **Down**. The two fails would have Pinned, but a Down model cannot be Pinned, so they are discarded. — *Had all three failed, the target would take **3 Stress** in one Action and go straight to a Break test (§11).*

> **When is the choice in step 3 a real choice?** With a vanilla weapon against a WND-1 body, never: **Down strictly dominates Pinned** on every axis — a Down model cannot Shoot, cannot clear itself, and costs its crew an Action to Stabilize or it bleeds out. Always take the wound. The pick becomes live in exactly two cases, and they are the same case: **when one wound is not decisive.** (a) A **payload** weapon, where the alternative to a wound is Bleeding or Fire rather than a bare Pin — against a WND-3 target, a two-round death clock can beat 1 of 3 WND. (b) Any **multi-wound** target, for the same reason. Do not read step 3 as a decision the player owes on every burst.

**Cost — measured, not estimated:**

| Attack Dice | Marginal Cr | Cumulative over baseline |
|:--:|:--:|:--:|
| 1 (baseline) | — | 0 |
| **2** | **+40** | **+40** |
| **3** | **+25** | **+65** |

**The step runs downward, and that is not a typo.** Because a burst caps at one wound, each extra die is worth only the chance the previous dice *all missed or failed* — so **die 2 is the expensive one** and die 3 is worth barely half of it. Priced at the catalogue's own offensive exchange rate (10 Cr per +1 Damage = 167 Cr per 1.0 wounds/Action), the marginal wound gain is **+0.230** for die 2 and **+0.148** for die 3 on the standard open target. An evenly-stepped or rising price sells die 3 at a premium to die 2 while delivering less.

> [!warning] **Attack Dice break the stat ceiling — this is why they need a gate, not just a price.**
> A **DEX +6 marksman** — the hard stat cap — with a medium weapon tops out at **54.0%** wound per Action, and cannot go higher: the natural-1 rule caps to-hit at 90%. A plain **DEX +2 Fighter with Attack Dice 2** reaches **59.0%**, and with **Attack Dice 3, 73.8% — +37% over the best marksman the game permits.** A **DEX +0 Recruit** with three dice beats him too (56.1%).
>
> That directly contradicts this section's own first tenet — *stats decide if you land it, weapons decide how bad it is.* No price repairs it, exactly as no price repaired the 36" range threshold: a purchase that outperforms four stat points at the cap has stopped being a weapon axis and started being a stat replacement.

> [!tip] **Proposed gates — NOT yet law, pending Ross's tick (§29)**
> The Phase 15b brief pre-authorised gating *if* the auto-include flag fired. It fired: at these prices a 3-die rifle is the most Credit-efficient way to put a body down on the board, beating the **Heavy Gunner** benchmark by **+51%** on identical fielded Credits (175 vs 175). Same treatment as the 24" line — gate the archetype rather than tax it:
> - **Attack Dice 2 → Fighter or above. Attack Dice 3 → Specialist or above.**
> - **Limit one Attack Dice 3 weapon per crew.**
> - **Attack Dice 3 is manufactured-only** — loot and raid spoils, never craftable.

*Full measured basis: `Attack Dice — Sim Findings`, harnesses `test-bench/attack_dice_sim.py` and `test-bench/attack_dice_rules_compare.py`, both stamped.*

### Characteristics (one slot each; ~30 Credits typical, scaled from the vault's point costs)

| Group | Characteristic | Effect |
|---|---|---|
| Damage/Armor | **Brutal** | +1 Damage (max +4). Melee only, or ranged + Short Range. |
| | **Armour Piercing** | Target Armor −1 on Injury. |
| To hit | **Accurate** | +1 hit if stationary this activation. |
| | **Spread** | +1 hit at half range or less, −1 beyond. |
| Payload *(replaces the non-wound result)* | **Concussive** → Off-Balance · **Crippling** → Hobbled · **Blinding** → Blind · **Shocking** → Shocked · **Toxic** → Poison · **Incendiary** → Fire · **Bleeding** → Bleed *(priciest — the deadliest payload)* · **Heavy Impact** → push 2" · **Hook** → pull 1" (melee only) · **Suppressive** → target must spend its whole activation to clear the Pin (ranged only) |
| Area | **Blast** | Resolve vs every model within 2" (Thrown/Heavy Ranged only). |
| | **Smoke** | Place 3" Dense Smoke instead of attacking (Thrown only). |
| Handling | **Long Range** | +6" range, to the 24" ceiling. |
| | **Balanced** | Use AGI instead of STR for melee (Light/One-Handed only). |
| | **Defensive** | +1 opposed melee when not attacker and didn't Move (melee only). |
| | **Cleaving** | Injury vs every Engaged enemy on a melee win (Heavy Melee only). |
| | **Breaching** | +2 STR vs Breachable terrain. |
| | **Concealable** | May start Hidden / smuggle past a search. |
| | **Quiet** | No reveal, no noise/alarm trip. |
| | **Compact** | Counts as one-handed despite class (heavy classes only). |

### Drawbacks — refund Credits, take no slot (max 2 per weapon)

| Drawback | Effect |
|---|---|
| **Short Range** | Halve max range (ranged only). |
| **Slow** | Can't Charge with this weapon (melee only). |
| **Unstable** | Natural-1 to hit destroys the weapon. |
| **Cumbersome** | −1 MOV while carried. |
| **Single-Use** | One use per battle. |

> **The rule that governs this list:** a drawback must bite no matter how you play. (E.g. "Slow" on a rifle would be free points — a rifleman never Charges anyway — so Slow is melee-only. "Awkward," no-Move-and-attack, was cut entirely because it synergizes with Accurate and is free on a sniper who never moves anyway.)

### Armor

Armor reduces the Injury roll only, never the hit. **Carries no drawbacks** — a drawback you opt into for a discount is a deal; a drawback welded onto something you want is a tax.

| Armor | Injury | Cost |
|---|:--:|:--:|
| None / Thick clothing | 0 | **0** |
| Light | −1 | **10** |
| Heavy | −2 | **20** |

*Measured, not derived — `armour-level-n2500`, with zero prior. **Heavy is not twice Light**: linear in injury probability does not imply linear in win-points, because the second point buys survival on a model already surviving more often. Measured ratio **1.745 ± 0.416**; the individual values are what get used.*

*(Improvised armor is cut — with its drawback gone it was just Light armor under another name.)*

### Hacking gear

| Gear | Modifier | Cost |
|---|:--:|:--:|
| Bare-handed | +0 | **0** |
| Breach Kit | +1 | **20** |
| Exploit Suite | +2 | **40** |

### Sample armoury *(generated from the costing engine, 850 scale — `py -3.13 -m points`)*

| Name | Build | Cr |
|---|---|:--:|
| Baseball Bat | Light Melee | **0** |
| Kitchen Knife | Light Melee · Balanced | **10** |
| Machete | One-Handed Melee | **10** |
| Crowbar | One-Handed Melee · Breaching | **25** |
| Magnum | Sidearm · Brutal · *Short Range* | **30** |
| Great Axe | Heavy Melee | **20** |
| Sledgehammer | Heavy Melee · Heavy Impact · Breaching | **50** |
| Fire Axe | Heavy Melee · Brutal · Bleeding | **50** |
| Reaping Hook | Heavy Melee · Cleaving · Defensive | **50** |
| Pistol | Sidearm | **15** |
| Snub Revolver | Sidearm | **15** |
| Pipe Shotgun | Standard Ranged · Brutal · Spread · *Short Range* · *Unstable* | **35** |
| Assault Rifle | Standard Ranged · Accurate | **35** |
| Nailgun | Standard Ranged · Bleeding | **35** |
| Grandpa's Hunting Rifle | Standard Ranged · Accurate · Long Range | **40** |
| Squad Machine Gun | Heavy Ranged · Suppressive · Armour Piercing | **55** |
| Makeshift Flamethrower | Standard Ranged · Incendiary · Blast · *Short Range* · *Single-Use* | **20** |
| Molotov | Thrown · Incendiary · Blast · *Single-Use* | **10** |
| Smoke Grenade | Thrown · Smoke · *Single-Use* | **15** |
| Ranger's Long Rifle | Heavy Ranged · 36" *(manufactured, limit 1)* | **55** |

*Nineteen of twenty moved when the rebuild landed — the armoury total fell **1950 → 575**. A rifle now costs 35 against a 100-Credit Fighter; it used to cost 100 against 95, which is the single line the rebuild was commissioned to fix.*

> ### ⛔ Five payloads are BLOCKED — they do not ship
> **Crippling, Concussive, Blinding, Hook and Toxic all measure at or below zero net value**, three of them significantly. The game would be selling a player a downgrade at any price.
>
> The cause was measured, not assumed. A payload lands **in place of** the ordinary non-wounding result, and on a ranged hit that result is **Pinned — worth +0.510 and significant**. So a payload's value is what it does *minus what it displaces*. Blind is the tell: it measures **+0.369 and positive** and still prices negative, purely because Pinned is worth more.
>
> **This is a RULES decision, not a pricing one.** Replace-not-stack was designed when Pinned was believed to be worth roughly zero. It is one miscalibrated rule, not five broken traits — and until it is ruled on, these five are not legal to buy.

> **[SIM-CONFIRMED — `PACKET-TEST-RESULTS.md` T5]** The one-payload-per-weapon cap is worth keeping, but **not because stacking is explosive** — it isn't. A second payload measured +3.3 win-points (real but sharply diminishing against the first payload's +15.5); a third measured zero (a known rules defect in how Crippling/Concussive price, not evidence the cap doesn't matter). **This is a readability/bookkeeping choice, not a balance emergency** — keep the cap, but justify it that way.

### Cut, and why (kept so it doesn't creep back)

Seeker mine (self-moving munition) — parked, not rejected. A moving munition on a 3'×3' board is an edge-case factory: does it draw Reactions? trigger traps? get shot as a Feature? what is its facing? Revisit once the Edge Cases audit exists; Proximity and Remote carry the family fine, and Remote's bluff kit is the interesting one anyway. Rapid (extra attack) — it *is* Quick Shot, a T3 skill; selling it as a cheap characteristic destroys the skill economy. Precision (flat +1 hit) — strictly better than Dead Eye; replaced by conditional Accurate. Reliable (re-roll) — no re-roll mechanic exists anywhere else in the game. Quick Draw (fire after Sprinting) — Sprint uses both slots, there's no Action left. Crushing (ignore cover on Injury) — cover never touches Injury, that's load-bearing. Awkward — free points on a static shooter. Intimidating (Stress aura) — parked, too volatile given Stress-cascade findings. **Concealable** (may start Hidden / smuggle past a search) — **cut 2026-08-14**: both halves are edge cases that do nothing in a typical battle, and it breaks the design contract at the top of this section, because "may start Hidden" is *positioning*, which is skill territory (Vanishing Point and Camouflage Drill already do it properly). **Quiet is NOT cut** — no-reveal / no-alarm-trip is a real mechanical axis that interacts with Hidden and with sensor deployables.

---

## 16 · List Building **[DRAFTED shape · 850-Credit scale]**

> **The core claim:** points buy **bodies and guns**. Stats and skills are free — rank already caps them, so pricing them again would double-count. The board prices stats (terrain density, not points, decides whether a Shooter or a Grabber wins); points price the only two things whose value doesn't depend on the mission — a body, and the weapon in its hands.

### Crew Rating

**Standard cap: 850 Credits** *(Match Play)* · **425** *(Campaign Start)*.

| Format | Cap |
|---|:--:|
| **Match Play** — a one-off game, no campaign attached | **850** |
| Raid variant *(75%)* | **640** |
| Pitched variant *(150%)* | **1275** |
| **Campaign Start** — a fresh crew entering the settlement layer | **425** |

*The 1000/500 pair is **retired**. The scale rebased 1000 → 1700 when bodies moved onto the measured stat ladder, then halved to **850** on 2026-08-20 so a standard crew is still six models rather than four.*

```
crew_rating = sum(body + equipped weapons + armour + equipment) for each fielded fighter
crew_rating ≤ agreed cap
```

**Stashed/unequipped gear counts 0 toward rating** — you paid Credits to own it, it only occupies Rating when fielded. Ownership and fielding are orthogonal: Credits/Materials buy what you own, Crew Rating gates what you field.

### Rank bodies (Credits) — two starting tiers

> **[NEW — Match Play vs. Campaign Start split]** These are genuinely different fighters, not the same table at two prices. A **Match Play** crew is built once for a single game with no persistence — it gets the richer starting kit because there's no other chance for those fighters to develop. A **Campaign Start** crew is meant to grow through the Level track (§26.1), so it starts leaner and earns its way to the same place over real play.

**Match Play** — one-off games, no campaign attached. Standard **850** Crew Rating cap. Rank bodies are identical in both tiers; the tiers differ only in the **cap** and the **starting skill count**.

| Rank | Stat pts | Starting skills | Orders | Credits |
|---|:--:|:--:|:--:|:--:|
| **Recruit** | 3 | **0** | 0 | **70** |
| **Fighter** | 5 | **exactly the tiers your stats reach (max 2)** | 0 | **100** |
| **Specialist** | 7 | **max 3** | 1 | **145** |
| **Leader** | 9 | **max 4** | 2 | **185** |

> **Skills are never approximate: a fighter has exactly one skill per tier its
> stats reach** (§14). The listed value is the maximum, hit only when every point
> lands in tiered stats — e.g. Fighter `+2/+2/+1` = 2 skills; Specialist
> `+4/+2/+1` = 3; Leader `+6/+2/+1` = 4. A fighter who spreads into +1 "dabbles"
> trades skills for breadth — a legal, priced choice, not an error.

**Campaign Start** — a fresh crew entering the persistent Settlements layer. Begins at **425 Crew Rating**, growing over the campaign (§25.5, §29).

| Rank | Stat pts | Starting skills | Orders | Credits |
|---|:--:|:--:|:--:|:--:|
| **Recruit** | 3 | 0 | 0 | **70** |
| **Fighter** | 5 | 1× T1 | 0 | **100** |
| **Specialist** | 7 | 1× T2 | 1 | **145** |
| **Leader** | 9 | 1× T3 | 2 | **185** |

> **[RE-DERIVED 2026-08-19]** Rank bodies are no longer backed out by hand — they are computed from the measured stat ladder plus the body base and Orders premium, re-derived 2026-08-19 onto the **measured stat ladder** (20/15/15/10/10/5 across the six rungs — a one-sided stat saturates, so the flat 15/point was wrong in both directions). The **Crew Rating scale rebased 1000 → 1700, then halved to 850 on 2026-08-20** at the same time so a standard crew is still six models rather than four; Campaign Start moves 500 → **425**. Validated end-to-end: at equal Crew Rating the win-rate spread across four archetypes tightened from 31–70% to **41–61%** (`catalogue-validation-n1500`).

### The pyramid — two versions

**Match Play (standard 850 CR):** **Exactly one Leader.** Every Specialist requires two fighters of lower rank. Every Recruit requires one Fighter or better. Minimum four fighters.

> **[NEW — Campaign Start variant]** **Exactly one Leader. Minimum three models. Every Specialist still requires two fighters of lower rank** — the Recruit-per-Fighter rule is the only part dropped, so a green crew can be all bodies but cannot be an all-Specialist elite. Otherwise pick any mix within the **425** Crew Rating cap. This is deliberately looser than the Match Play pyramid: a green crew hasn't built a chain of command yet, it's just whoever the founding Leader could recruit. Worth checking the same way the standard pyramid's model-count question was checked (`Crew Sim — Findings`) once this is played — dropping the ratio changes which body-count-vs-power-tier mixes are reachable at this budget, and that's untested.

**The roster you own is capped separately by housing** (§21) — base 12 slots from the HQ, +6 per Bunkhouse. No per-head upkeep. **Housing is the only population brake.** Veterans get more expensive as they Advance (§26), which is the real anti-snowball valve: the longer a campaign runs, the smaller your crew gets, because your best fighters crowd out rookies on the Rating cap.

### Loadout

Free to every fighter: fists, one Light Melee weapon, thick clothing. **Carry limits:** one armor · two hands · up to two equipment items. Weapons are built per §15 and rank-gated — a Recruit physically cannot hold a rifle.

| Equipment | Effect | Credits |
|---|---|:--:|
| Med-Kit | Cancels the −2 on Stabilize/treating Bleed & Poison | 40 |
| Breach Kit | +1 hack test | 40 |
| Exploit Suite | +2 hack test | 80 |
| Deployable | Turret/mine/trap/beacon — see Deployables catalogue | varies |

> **[SIM-CONFIRMED — `PACKET-TEST-RESULTS.md` T6]** The concern that non-combat-primary builds (INT/NRV-heavy) might be unfieldable is real but narrow: an INT or NRV-primary crew runs ~12 points below a STR-primary crew overall, but is **fully competitive (47–49%) on Hold and Hold+Claim scenarios** and only collapses on pure Annihilate (14–17%). **The scenario, not the stat line, decides whether INT/NRV is worth building** — this is a reason to keep scenario variety high, not a reason to think these builds are broken.

---

# PART III — SETTLEMENT & CAMPAIGN

## 17 · Founding a settlement

### 17.1 · Choosing a location **[NEW]**

At founding, choose one **Location**, granting one free structure or upgrade at zero Materials cost:

| Location | Grants |
|---|---|
| Hospital | Free Med-bay |
| Police Station | Free Holding Cells |
| Scrapyard | Salvage Yard upgraded one tier |
| Fire Station | Free Bunkhouse |
| National Guard Armory | Free Armory (Equipment Shed pre-upgraded) |
| High School/University | Free Comms Mast |
| Auto Shop/Garage | Free Workshop (Workbench pre-upgraded) |
| Radio/TV Station | Free Server Core |
| Farm/Ranch | +50 Materials to founding budget |
| Strip Mall/Shopping Center | Free Trade House (Trader's Kiosk pre-upgraded) |

### 17.2 · Starting structures **[DRAFTED]**

Every settlement begins with, free: **HQ** (command, 12 housing) · **Generator** (+5 Power) · **Processor** (Materials gatherer) · **Salvage Yard** (Credits gatherer). Starting footprint: 95/432 squares.

### 17.3 · Founding budget **[NEW]**

**125 Materials + 75 Credits.** 125 Materials is still ≈ **two Tier-1 structures** on the 850 scale — the stated design intent, preserved through the rescale. Full 23-structure catalogue open from turn one, no prerequisites.

*(Was 250 + 150. Materials halved along with Credits on 2026-08-20; leaving the budget at 250 against halved structure costs would have quietly doubled a founding player's buying power.)*

> **[SIM-CONFIRMED — T12, rescaled]** A normal battle reward of **70 Credits + 15 Materials** funds **~1 Recruit**, and a Tier I structure takes **~3 battles**. Those two ratios are the finding; the raw numbers moved with the 850 rescale and were re-derived to preserve them. A fighter is an impulse buy, a building is a campaign-scale commitment.

---

## 18 · The settlement canvas **[DRAFTED]**

12" × 36" strip, 1" grid, 432 squares — exactly the defender's back three 12"×12" density squares on a 3'×3' board. **A raid always uses the whole canvas.** Groundworks I: 18"×36" (648 sq). Groundworks II (4'×4' play): 18"×48" (864 sq).

**Footprint classes:** Building (6×6 min, enclosed) · Plant (~3×3, no interior) · Station (3×1 min, open-air).

---

## 19 · Power **[DRAFTED, reconciled]**

Generator produces **+5**. Draw scales by tier: T1=1 · T2=2 · T3=3. Unpowered = Disabled for the round. Starting draw: HQ 1 + Processor 1 + Salvage Yard 1 = 3 against +5 — two spare.

---

## 20 · Storage & caps **[DRAFTED]**

HQ (a little of everything) · Gatherer buffer (a little of its own resource, easy pickings) · Storehouse (bulk, the raid loot target) · Vault (small, secure — Sabotage/hack only). **Housing:** HQ base 12, +6/Bunkhouse. **Equipment:** start 30 slots, +30/Armory tier.

| Store | Capacity *(provisional)* | Raidable? |
|---|---|---|
| HQ | **75 Credits + 75 Materials** | Yes |
| Gatherer buffer (each) | **15 of its own resource** | Yes — and first to go |
| Storehouse (each) | **+125 combined**, any mix | Yes — the raid target |
| Vault | **75 combined** | **No** — Sabotage/hack only, never raid loot |

*(Halved with the rest of the economy on the 850 rescale. Still provisional — these are the numbers §29 lists as genuinely open.)*

^tbl-storage-caps

**Over cap:** caps are checked **once, at the end of the Settlement Phase** — resources may sit over cap freely between banking and spending inside the same phase; whatever still exceeds cap when the phase closes is **lost. Spend it or lose it.** *(This is also the first real economy sink — a wealthy settlement must build Storehouses/Vaults or bleed surplus, which partially answers the §29 sink problem.)*

---

## 21 · The structure catalogue — 23 entries **[DRAFTED shape, NEW costs]**

**A structure is always Functional or Disabled — nothing in between.** No HP, no partial damage. Destruction only via Sabotage; repair is a flat Materials cost.

> **[NEW — closes the Water gap for good]** During any raid, an attacker may target **any** of the defender's structures with the same charge mechanic already drafted for the Sabotage scenario (§12.7): a fighter in base contact spends an Action + INT 7+ to **arm** a charge; it detonates after surviving **3 End Phases armed** unless a defender spends an Action + DEX 7+ to **defuse** it first (nat 1 = it goes off immediately). A detonated structure goes **Disabled** until repaired at its normal flat Materials cost (§21) — it doesn't need to be looted, and it was never a special "Water tank" or any other bespoke destroy-only target. Any generator, processor, trader's kiosk, or storehouse is a legitimate sabotage target under this rule. This was the vault's own flagged gap — "you cannot carry a tank away, but you can hole it" — closed using a mechanic that already existed rather than inventing a new resource to create the target.

### Sustain
| Structure | Class | Size | Pwr | Materials | Effect |
|---|---|---|---|:--:|---|
| Generator ★ | Plant | 3×3 | +5 | **20** | Power |
| Bunkhouse | Building | 6×9 | −1 | **60** | +6 housing |
| Storehouse *(repeatable)* | Building | 6×6 | −1 | **50** | Bulk storage; raid target |
| Equipment Shed→Armory | Station→Building | 3×2→6×6 | −1→−2 | **25 → 96** | Unequipped-gear cap |

### Convert
| Structure | Class | Size | Pwr | Materials | Effect |
|---|---|---|---|:--:|---|
| Processor ★ | Plant | 3×5 | −1 | **45** | Materials gatherer |
| Salvage Yard ★ | Yard | 5×7 | −1 | **45** | Credits gatherer |
| Trader's Kiosk→Trade House | Station→Building | 3×2→6×6 | −1→−2 | **45 → 128** | Sell gear; convert resources (below) |
| Workbench→Workshop | Station→Building | 3×2→6×8 | −1→−2 | **45 → 128** | Craft/repair; unlocks weapon/armour/chem branches |
| Fabricator→Robotics Workshop→Advanced Weapons Lab | Building | 6×6→6×8→6×10 | −1/−2/−3 | **70 → 110 → 195** | Research tiers; T3 unlocks the 2051 arsenal |

*The Fabricator's two upper tiers are **[C-tier, derived]** — the engine carries the T1 entry and the ladder's own `UPGRADE_MULT` (×1.60, ×1.75); it does not yet carry the named T2/T3 forms as rows.*

### Operate
| Structure | Class | Size | Pwr | Materials | Effect |
|---|---|---|---|:--:|---|
| HQ ★ | Building | 6×6 | −1 | **70** | Campaign actions, 12 housing, dispatch |
| Vault *(HQ add-on)* | Plant | 3×3 | −1 | **50** | Secure storage |
| Scout Post | Plant | 3×3 | −1 | **50** | Pre-battle info |
| Comms Mast | Plant | 3×3 | −1 | **50** | Mission-quality rerolls |
| Server Core | Building | 6×6 | −2 | **128** | Rival intel; friendly terminals Linked |
| Drone Bay | Building | 6×8 | −2 | **144** | Drone deployables; free recon mission |

### Recover
| Structure | Class | Size | Pwr | Materials | Effect |
|---|---|---|---|:--:|---|
| Med-bay | Building | 6×6 | −1 | **65** | **+1 to Fate roll**; T2 heals scars |
| Holding Cells | Building | 6×6 | −1 | **65** | Prisoner capacity |
| Mess Hall | Building | 6×8 | −1 | **75** | **Once/battle, one fighter clears 1 Stress free** |

*Mess Hall was the only one of the 23 structures with **no derived cost anywhere** — it carried "~120", flagged as a guess. It is now in the costing engine and priced by the same formula as every peer (2026-08-27).*

### Defend
| Structure | Class | Size | Pwr | Materials | Effect |
|---|---|---|---|---|---|
| Perimeter Wall | Line | 6" segments | −1 | **50**/seg | Shapes the raid board |
| Gatehouse | Building | 6×6 | −1 | **75** | Chokepoint |
| Watchtower | Plant | 3×3 | −1 | **55** | Defender starts a model in it |
| Turret Mount | Plant | 2×2 | −2 | **104** | Auto-deploy turret hardpoint (still costs Credits to field) |
| EW Mast | Plant | 3×3 | −2 | **104** | Counter-hack/drone |

**Trader conversion** *(NEW)*: **Kiosk** sells 2 Materials → 1 Credit and buys 2 Credits → 1 Material. **Trade House** does 3 Materials → 2 Credits and 3 Credits → 2 Materials. An assigned worker adds +10% yield, round down. **Convert in one direction only per Settlement Phase** — the spread means no conversion loop is ever profitable. *(Rates provisional.)*

**Repair: flat 15 Materials/structure.** **HQ tiers** *(**[C-tier, derived]** from HQ I and the ladder's own `UPGRADE_MULT`)*: HQ I (starter, 1 dispatch / 12 housing) → **HQ II (110 Mat**, 2 dispatch / 18 housing, unlocks Vault) → **HQ III (195 Mat**, 3 dispatch / 24 housing). **Groundworks I: 60 Mat. Groundworks II: 100 Mat.**

### What winning a raid actually takes **[NEW]**

**If the attacker wins a raid** they carry off **25% (round down) of the defender's stored Credits and 25% of stored Materials** — Vault contents excluded — **capped at 50 Credits + 50 Materials per raid**, plus whatever they looted or sabotaged in-battle. **If the defender wins,** the attacker keeps only what they physically looted during the battle.

**Floor:** raid theft never reduces a defender below **25 Credits and 25 Materials** — a settlement can be hurt, not deleted. *(The cap and the floor are the anti-death-spiral pair; both provisional, and both halved with the 850 rescale.)*

---

## 22 · Workers **[PACKET shape, simplified per direct instruction]**

> **Proficiency tiers are cut from v1.** The 0–100 track with three unlocking bands was real bookkeeping — a number to track per worker, per structure, that grows over time — for a mechanic that's ultimately still just "a structure works better with a person in it." That's the kind of layered complexity this project has consistently cut everywhere else (per-head upkeep, the Heat/Attention track, HP-based structure damage), and worker progression didn't earn an exception just by arriving later. **A worker is either assigned or not.** The listed benefit applies while assigned, stops the moment they're reassigned, full stop. No number to track, nothing to level.
>
> The full three-tier version isn't thrown away — it's genuinely good content, just scoped wrong for a core rule. It's parked below as a candidate for a future Settlements supplement focused on expanding the settlement layer, where a slower, more granular sub-system is a reasonable thing to offer to players who specifically want more settlement-management depth, without forcing that bookkeeping on everyone else.

One worker slot per structure that accepts one.

**v1 ships ten worker benefits** — the ones that carry the campaign loop:

**Processor:** +1 Materials per gather. **Salvage Yard:** +1 Credits per gather. **Generator:** +1 Power output. **Med-bay:** +1 further to the Fate roll (stacks with the structure's own +1, total +2 — which is also the cap, §26.3). **Storehouse:** +10% effective storage cap. **Equipment Shed / Armory:** +10 equipment slots on top of the structure's own. **Trader's Kiosk / Trade House:** sell rate +10%. **Workbench / Workshop:** crafted item Materials cost −10%. **HQ:** +1 dispatch action per cycle, on top of the tier's base rate (§21). **Mess Hall:** the free Stress-clear (§21) triggers on two fighters instead of one.

**Structures not listed accept no worker in v1 — their base effect is their whole effect.** The other ten (Fabricator ladder · Scout Post · Comms Mast · Server Core · Drone Bay · Holding Cells · Gatehouse · Watchtower · Turret Mount · EW Mast) are parked in the supplement appendix below. They are either battle-facing micro-buffs that complicate a raid, or intel and unlock effects serving systems that are themselves thin in v1 — no loop damage, roughly half the rules surface.

*(Bunkhouse, Vault, and Perimeter Wall stay excluded — passive amenities/board shaping with no operational job for a worker to hold.)*

All of these are first-draft, same flag as everything else content-shaped in this document.

<details>
<summary><b>Parked — the full three-tier Proficiency system, for a future supplement</b></summary>

Proficiency 0–100, tied to the current job: 0–32 base only · 33–65 T1 bonus · 66–99 T2 bonus · 100 T3 ceiling. The flat effects above are each drawn from what was previously this system's T1 or T2 tier. The full tiered text, including every T3 once-per-campaign ceiling effect that got cut along with the tracking, is preserved in this document's revision history rather than reproduced here — reintroduce wholesale if a supplement wants the deeper version rather than rewriting it from scratch.

</details>

---



## 23 · Territory & the campaign map **[PACKET]**

**Territory card — 11 required fields:** terrain recipe · scenario weighting · Side Objective(s) · infrastructure · Events · Loot table · control benefit (access, never power) · supply requirement · control state · adjacent territories · raid profile.

### The default loot table **[NEW]**

Every territory needs a Loot table (per the card fields above); this is the base table any territory uses unless its own card overrides specific entries to fit its flavor (an industrial territory might swap "found jewelry" for "found tools," etc.). This is also what §6's Search result "Gear" and "Supply cache" outcomes roll on, and what the Raid scenario (§12.7) and a Scavenge dispatch (§25.5) draw from.

Roll **1d10** whenever a Search, Raid loot, or Scavenge action calls for it:

| d10 | Result |
|:--:|---|
| 1 | Nothing usable — spoiled, broken, or already picked clean |
| 2 | **+5 Credits** |
| 3 | **+10 Materials** |
| 4 | **+10 Credits** |
| 5 | A basic Light Melee or Sidearm weapon, unbuilt (player picks the class, no characteristics) |
| 6 | **+15 Materials** |
| 7 | **+15 Credits** |
| 8 | **+20 Credits** |
| 9 | One piece of equipment (Med-Kit, Breach Kit, or a basic Trap/Mine, player's choice) |
| 10 | **Jackpot** — roll twice more on this table, ignoring further 10s |

Small, fast, and deliberately low-stakes — this is meant to make searching worth doing even when a battle's going badly, not to be a second economy. First-draft, same flag as everything else content-shaped in this document — the specific values haven't been checked against the economy-sink problem already flagged in §29, and probably shouldn't be tuned until that's addressed, since loot is one of the few natural places to route a sink fix through if the economy needs one.

### Control states

**Claimed** (win a battle here, no benefit yet) → **Controlled** (assign a worker or pay Materials, benefit active) → **Isolated** (cut off by an enemy-held adjacent territory, benefit suspended).

---

## 24 · Factions **[PACKET framework + this project's roster]**

One battlefield rule + one settlement affinity each. No flat stat bonus, no matched drawback, no exclusive unlock. Balanced peer-to-peer, not against a paired nerf. *(Supersedes the vault's own unstarted `Factions.md` placeholder, which still uses flat stat bonuses/nerfs.)*

| Faction | Battlefield rule | Settlement affinity |
|---|---|---|
| **Military** | Ready token survives a failed Reaction attempt | +1 free Bunkhouse tier at founding |
| **First Responders** | Improved Build test for field deployables | Med-bay costs −10% Materials |
| **Labor** | Re-attempt one failed Search/battle, free | Gatherers +1 flat/Settlement Phase |
| **Residents** | +1 Break test within 3" of another Resident | Bunkhouse costs 1 fewer Materials-tier |
| **Tech Workers** | Hack range bands read one step closer | Fabricator ladder −10% Materials |
| **Criminals** | Hide in Light cover (not just Concealing), never within 6" of an objective | Trade House sell rates +10% |

None touch a hard ceiling (modifier cap, damage cap, range cap, re-rolls, extra attacks) — every rule is a discount, a conditional modifier, an action-economy nudge, or a terrain-verb exception.

---

## 25 · Stealth & Ambush **[NEW — sim-tuned]**

*700–2000 games/cell, paired mirrors. Full data: `PACKET-TEST-RESULTS.md` T1–T3.*

**Ambush attacks off AGI instead of STR/DEX**, and this must be printed explicitly on the card — a DEX carrier running Ambush measured **−30 to −33 win-points** (attacking on its worst stat); an AGI carrier measured **+1.0 to +12.7**.

**The failed-Ambush free Attack Back is load-bearing — keep it unchanged.** It removes 4.1 of the mechanic's 12.1 win-points and fires on 47.5% of attempts. This is confirmed, not just designed — don't soften it later.

**RULED — a Hidden fighter may hold an objective, but claiming/scoring one breaks Hidden.** Holding just means sitting within 3" with no enemy within 3" (§12.7) — that costs nothing and doesn't touch Hidden at all. But *claiming* a terminal, *looting* a cache, *arming* or *defusing* a charge is always an Interact test, and Interacting now explicitly breaks Hidden (§10, fixed above). In practice this makes the sim's "may/may not hold" question close to moot for objective types that require an active claim — a Hidden fighter can sit on an unclaimed objective all day, but the instant they do the thing that scores it, they're not Hidden anymore. **Take a Hold** is the one scenario where this matters most cleanly: a terminal has to be claimed (INT 7+, breaks Hidden) before it can ever be *held* for score, so the "hold" state a Hidden fighter benefits from only ever applies *after* the reveal already happened. The sim's measured **+12.7 / −5.2** swing was run against a simplified "can this fighter contribute to score while Hidden" toggle — with Interact-breaks-Hidden as a hard rule, the practical answer lands close to the sim's "No" case for anything requiring a claim, and close to "Yes" for a scenario that only needs bodies standing still (a pure territorial-control read). This is the resolution going forward; if a future scenario type introduces a hold-only objective with no claim step, revisit this specific interaction then.

**If Hidden ever moves from a −3 modifier to "not a legal target," a skill-stacking cap is required in the same change** — stacking three specific concealment skills under the untargetable reading produced a fighter shot **zero times per game**; under the current −3 reading the same stack gets shot ~12 times and dies normally.

---

## 25.5 · The Campaign Turn **[NEW — this is `Downtime.md`'s actual content; that file was `status: Not Started` in the vault, and §17/§22/§26 all assumed this sequence existed without it ever being written]**

Every cycle between battles runs through three phases, in order. Nothing in §22 (Workers) or §26 (Campaign persistence) happens outside this sequence — this section is what ties them together.

### Phase 1 — Post-Battle
Happens the moment a battle ends, before anything else.

1. **Survival.** Check every fighter against the Safe rule (§26.3) — still standing, left via a friendly edge, or in base contact with a friendly needs no roll. Everyone else rolls the Fate table (§26.3), including resolving any Captured or Hardened result on the spot where the immediate part applies (§26.3a step 1, §26.3b).
2. **Level-ups.** Apply every qualifying trigger from the battle just played (kills, Glorious Deeds, surviving, objectives held) to each surviving fighter, subject to the 6-source soft cap. Any fighter who crosses into a new Level resolves it now — choose the stat, or roll-3-choose-1 the skill, per §26.1.
3. **Bank Resources.** Add the battle's earned Credits and Materials to the settlement's totals, capped by storage (§20).

### Phase 2 — Settlement
Follows immediately once Phase 1 is fully resolved. This is where the settlement itself moves.

- **Build & upgrade structures** — spend Materials against the catalogue (§21).
- **Assign or reassign workers** to structures (§22). Reassigning ends the old benefit immediately; the new assignment starts producing next Settlement Phase, not retroactively.
- **Assign Power** — allocate the Generator's output across powered structures, respecting each structure's draw (§19). A structure left unpowered this phase is Disabled until it's covered.
- **Resolve pending Captured decisions** — Ransom or Brainwash attempts due this phase (§26.3a steps 3–4).
- **Resolve third-Scar retirement decisions** for any fighter who crossed that threshold (§26.4).
- **Dispatch actions.** Send fighters or workers out against the Territory map. A settlement gets one dispatch action per HQ tier's rating (HQ I = 1, II = 2, III = 3 — §21). Two dispatch types exist in v1:
  - **Scout** — reveal a chosen territory's Twist or hidden Side Objective ahead of a battle fought there.
  - **Scavenge** — roll on that territory's Loot table (§23) for a small Materials/Credits gain, no battle required.
  
  *(Sabotage-by-dispatch, without physically raiding, is not in v1 — sabotaging a specific structure requires the planted-charge mechanic below, which needs a raid. This keeps dispatch actions light and non-combat, and keeps the interesting sabotage decision on the table, literally.)*

### Phase 3 — Battle Prep
Immediately before the next battle. Once a player has done everything they intend to in the Settlement Phase, they move here.

1. **Choose the territory** (and therefore the scenario, per that territory's card, §23) for the next battle.
2. **Set the Crew Rating cap** for the format being played (Match Play 850, raid 640, pitched 1275, Campaign Start 425 — §16).
3. **Build the roster.** Choose which owned fighters to field within housing (§20) and equip them within the Rating cap — weapons, armor, equipment, all per §15–16.
4. **Resolve setup-time bonuses** — Faction battlefield rules (§24), Location founding benefits if still relevant, any territory-card modifiers.
5. **Roll the Twist** (§12.7) once deployment is set, per standard Scenario setup.

---



## 26 · Campaign persistence

### 26.1 · Levels — fixed advancement track **[NEW — replaces the previous freeform Advance-spend model per direct instruction; finalized after several rounds of iteration]**

> **This supersedes the earlier draft's direct-choice Advance system.** The old model let a player spend any earned Advance on any of stat/skill/scar-heal, freely, up to a flat +6 cap. This one fixes *what* each Advance buys, in a set order, folding in a version of the packet's controlled-random skill selection — narrowed, after discussion, to a single fixed path per fighter rather than any path at any tier.

**Earning a Level-up** uses the same triggers as before — kills, Glorious Deeds (§26.2), surviving, objectives held — one qualifying trigger advances a fighter to their next Level. The same **soft cap of 6 distinct sources/fighter/battle** still applies **[SIM-CONFIRMED — T8]**.

**Primary** is the stat carrying the fighter's highest point investment at creation (player's choice on ties). It never changes — it is who they were when they signed on, and it names their Primary skill path.

**There is no declared Secondary. Every other stat is a secondary stat.** At the track's **floating stat levels (1, 4, 8)**, add +1 to **any stat, chosen when the level is earned** (Primary included) — a fighter's direction emerges from play, not from a box ticked at hire. Levels 2, 5 and 9 remain forced **+1 Primary**, so identity keeps growing regardless of direction. Only the **campaign stat cap (+6)** limits track growth; **rank tier caps are creation-time caps and do not constrain leveling.**

**Skill slots (Levels 3, 6, 10):** declare any path, and roll on any tier that path's stat has **unlocked: +2 → Tier 1, +4 → Tier 2, +6 → Tier 3** — the same thresholds creation already uses (§14). The Level no longer fixes the tier; **the stat does.** A fighter's Primary path always counts as unlocked at Tier 1, so a slot is never dead.

**The track — ten Levels, fixed contents:**

| Level | Grants | Credits |
|:--:|---|:--:|
| **1** | +1 **any stat** (floating) | *ladder* |
| **2** | +1 **Primary** stat | *ladder* |
| **3** | **Skill slot** | **10** |
| **4** | +1 **any stat** (floating) | *ladder* |
| **5** | +1 **Primary** stat | *ladder* |
| **6** | **Skill slot** | **20** |
| **7** | **+1 WND** | **20** |
| **8** | +1 **any stat** (floating) | *ladder* |
| **9** | +1 **Primary** stat | *ladder* |
| **10** | **Skill slot** — the capstone for a committed fighter | **30** |

**A stat level is priced off the measured ladder, not a flat rate** — this replaced the flat 15/point, which was wrong in *both* directions:

| Rung | One-sided stat *(DEX, INT, NRV)* | Opposed stat *(STR, AGI)* |
|:--:|:--:|:--:|
| 0→1 | **20** | 15 |
| 1→2 | **15** | 15 |
| 2→3 | **15** | 15 |
| 3→4 | **10** | 15 |
| 4→5 | **10** | 15 |
| 5→6 | **5** | 15 |

*A one-sided stat is tested against a fixed TN, so it **saturates** — the sixth point improves a roll that is already passing. An opposed stat is tested against another model's stat, where the odds depend only on the gap, so it **cannot** saturate: STR measured flat to four decimals at every rung, and the structure predicted that before it was measured. INT and NRV take the one-sided ladder at ×0.8; AGI takes the opposed ladder at ×0.8 and is **engine-blocked**, priced by analogy only.*

**A fully-levelled fighter costs roughly +140 Credits** on top of their Rank body, depending on which stats they grew — a Primary-DEX fighter who spends every floating level on DEX pays less at the top of the track than one spreading into STR. **A fighter caps at Level 10** — further kills/Deeds/etc. still bank Resources and count for Glorious Deeds, but no longer advance the fighter further. Reaching Level 10 at all should be rare — surviving that long takes real luck. A Level 10 fighter is a **legend by civilian standards** — feared, storied, and still one bad round from the dirt. This game never makes anyone unkillable (see the WND ruling in *Out of Scope*, §4).

**MOV is not part of this track.** It stays exactly where it already was — Fleet (T2 AGI skill) is the only way to raise it. No collision, no separate MOV-swap option; keeping it purely skill-gated is cleaner narratively and avoids any interaction with Sprint/Charge distances at the top of the track.

**Choosing the skill at Levels 3, 6 and 10:** declare a path, pick any tier that path's stat has unlocked (+2/+4/+6), roll **3 times** on that tier's chart (reroll duplicates), then **choose one of the three.** Cross-path picks are legal and cost you your own path's capstone — a genuine trade, not a freebie.

**Lifetime totals for a fully-leveled fighter:** **6 stat points** (3 Secondary + 3 Primary) on top of whatever Rank already gave them, **4 skills total** (1 starting — see the updated Rank table in §13 — plus 3 from leveling: T1/T2/T3, all one consistent path), and **one WND bump.**

> **[Flagged, not blocking]** A fighter who also picks **Tough** (T3 STR skill) as their Level 6 or 10 skill choice can stack it with the Level 7 WND bump — base 1 + Tough's +1 + Level 7's +1 = **WND 3** at the absolute ceiling. This was walked through directly and landed on as acceptable (down from an earlier version that would have reached WND 4) — flagged here so the stacking is visible in the rules text, not just in the design conversation that produced it.

**Scar-healing is not part of this track.** It lives in two dedicated places instead: the Med-bay's T2 worker benefit (§22) and the one-per-career Special Treatment option on a fighter's third Scar (§26.4).

> **[CLOSED 2026-08-27]** This entry used to flag a "16–34 Credits" measured stat value against a flat 15 charged. **That figure was contaminated** — measured before the 2026-08-13 policy fix and averaged across scenarios since dropped. The flat 15 is gone; stat levels now read off the measured ladder above, which is non-flat *and* stat-dependent. The residual risk moved: it is no longer an underprice, it is that **AGI has never been measured at all** (`DODGE_ON` is False in the engine, so it reads exactly zero by construction) and is priced purely by analogy.

> **[DERIVED — no longer a judgment call, but not measured either]** The +1 WND price was **45 Credits with no sim data behind it at all**, priced by position (above a T2 skill, below a T3). It is now **20** on the 850 scale, derived from the measured value of **heavy armour** (−2 on the injury roll, the same 20 Cr) — both buy the same thing, the model staying on the table longer. That makes it a **C-tier price** in `docs/POINTS-CATALOGUE.md`: derived by rule from a measured atom, never measured directly. An analogy is not a measurement — but unlike the 45, it is correctable from table data, because the derivation is written down.

### 26.2 · Glorious Deeds **[NEW]**

Once per fighter per battle: **Daredevil** (gap leap) · **Wrecking Crew** (terrain-verb kill) · **Duelist** (win a head-to-head) · **Last One Standing** · **Medic** (revive a Down friendly) · **Steady Hand** (Rally/Talk Down) · **Ghost** (never targeted) · **Ambush Predator** (land an Ambush) · **Trapper** (trap/deployable kill) · **Against the Odds** (win at 2+ Stress). Plus 1–5 **Territory Deeds** per territory card, themed to that location.

### 26.3 · The Fate table **[DRAFTED pre-check + categories, NEW per-injury effects, NEW Captured/Hardened mechanics]**

**First, who rolls at all.** A unit is **Safe** — no roll — if at battle's end it: is still standing with its crew, **or** left the board via a friendly edge, **or** ends in base contact with a friendly. *(This exemption exists in the vault and was missing from the previous draft of this section — restored here.)*

Any unit that ends the battle **Down and alone**, or that bled out during it, rolls **1d10**, +1 with a Med-bay (+2 with an assigned worker):

> **A natural 1 on the Fate die is always Dead, regardless of modifiers** — the same rule the core engine already uses for every test (§2). Likewise, **a natural 10 is always Hardened**. Fate modifiers shift every other result but never overwrite the die's own extremes. **Total Fate modifiers are capped at +2** from all sources combined.

| d10 | Category *(vault)* | Specific result *(new, closes the vault's flagged gap — "no scar effect table has ever been written")* | Effect |
|---|---|---|---|
| 1 | Dead | Death | Removed from the roster permanently |
| 2–3 | Grievous injury | Severed leg *or* severed arm (player/GM choice, or split the range) | Severed leg: permanent −2 MOV. Severed arm: permanent −1 STR, no two-handed weapons |
| 4–5 | Captured | Captured — **Recruits and Fighters only** (see below) | Full mechanic in §26.3a |
| 6–8 | Lasting scar | Gouged eye · Broken leg (heals) · Broken arm (heals) · Concussion · Deep scar (roll or choose one) | Gouged eye: permanent −1 ranged to-hit. Broken leg/arm: −1 MOV or STR, **next battle only**. Concussion: −1 all rolls, next battle only. Deep scar: cosmetic only |
| 9 | Full recovery | Shaken loose | No lasting injury; starts next battle at 1 Stress |
| 10 | Hardened | Hardened | Full mechanic in §26.3b |

**Specialists and Leaders cannot roll Captured** — if the die comes up 4–5 for one of them, re-roll onto the Lasting Scar band (6–8) instead. Ranked fighters are too dangerous, too well-protected, or too valuable to bag cleanly; only Recruits and Fighters get taken alive.

Entries **2–3 and 6–8** are **Scars** for the retirement rule below. **Captured (4–5) is not a Scar** — it's a separate campaign thread. Scars never touch Crew Rating — pure rules penalties.

#### 26.3a · Captured — full resolution **[NEW, drafted from your sketch]**

1. **The fighter is held by the capturing crew**, unavailable to their owner for their owner's **next battle**.
2. **Rescue window.** Before that next battle, the owning player may declare a **Raid** against the capturing settlement specifically to free the prisoner. This raid must be played before any other non-raid battle the owner takes. **If the capturing player cannot or will not accept the raid within that window, they must release the prisoner immediately, for free.** Win the raid → the fighter returns unharmed. Lose it → the fighter stays captive and the sequence below proceeds as normal.
3. **If no rescue happens**, then in the capturing player's **Settlement Phase following their own next battle**, they must choose exactly one, no stalling:
   - **Ransom.** Offer the fighter back for **half their Credits cost.** The owner may pay to recover them (returns at full health, no new Scar). If the owner won't or can't pay, the fighter is lost permanently, same as Dead.
   - **Brainwash attempt** *(requires an upgraded Holding Cells — see §21)*. Opposed `1d10+INT`: capturing Leader vs. the captive fighter. **Win** → mark one success; nothing changes yet. **Lose** → the fighter breaks free immediately and returns to their owner's settlement, unharmed, and the whole Captured thread ends.
4. **A marked first success carries into the capturing player's next Settlement Phase**, where they attempt the opposed INT test a second time. **Win again** → the fighter **permanently defects** — added to the capturing crew's roster at their current Level and stats, Credits cost recalculated normally against the new owner's Crew Rating. **Lose** → same as any lost brainwash roll: the fighter escapes home unharmed, thread over.

So a captor gets three real choices at the point of decision: take a guaranteed half-price payday (Ransom), or gamble up to two Settlement Phases for a permanent free recruit (Brainwash) with a real chance of getting nothing at all. This is a first-draft sequence — flagged for playtesting like everything else in this document, but it's concrete enough to run at a table as written.

#### 26.3b · Hardened **[NEW]**

A fighter who rolls Hardened suffers no injury and receives **one free Level-up immediately**, at zero Credits cost, following the normal Level track (§26.1) in sequence — whichever Level they'd reach next. This is on top of, not instead of, any Levels they'd otherwise earn from that battle's kills/Deeds/objectives.


### 26.4 · The third Scar — forced retirement **[DRAFTED shape, NEW options]**

Choose one: **Reassign** to Worker (§22) · **One last mission** then retire regardless of outcome · **Special treatment** (T2 Med-bay, significant cost, heals one Scar — **once per career, full stop**) · **Retire outright**.

> **[SIM-CONFIRMED — T9]** Uncapped, Special Treatment gets bought **3.98 times per 20-battle campaign** — routine, not exceptional. Capping at once/career brings it to 1.00. **Do not ship this uncapped.**

### 26.5 · Promotion **[DRAFTED]**

Separate from leveling; requires an open rank slot and an explicit in-fiction action, never automatic.

---

## 27 · Battlefield Events **[PACKET structure, NEW table]**

Exactly two rolls: start of Round 1, start of the midpoint round. No running clock.

| d10 | Event | Effect |
|---|---|---|
| 1 | Clear skies | No effect |
| 2 | Rain rolls in | Ranged range −3", Hide test +1 |
| 3 | Burst main | A water main lets go — a 3" zone centred on the board's midpoint becomes **Difficult ground** for the rest of the game |
| 4 | Pack on the move | Neutral hostile token attacks nearest model in 12" |
| 5 | Power flicker | Powered terrain within 12" of center Disabled this round |
| 6 | Distant gunfire | Everyone within 12" of center gains 1 Stress |
| 7 | Scavenger's luck | Extra loot token at an unclaimed Side Objective |
| 8 | Structural failure | One Building piece within 12" becomes Difficult |
| 9 | Radio chatter | Both players reroll one failed Spot this round |
| 10 | All quiet | No effect |

First-draft 10 entries; expand toward 15–20 once the rhythm is confirmed.

---

## 28 · Drones & Chems — advanced modules

### 28.1 · Drones **[PACKET, reasoning revised per sim]**

Drone Operator (INT-primary), hard **Bandwidth** cap: 1/Operator, one drone action per the Operator's own activation. **Bandwidth is a fixed fighter stat, not a settlement resource** — the Drone Bay grants access, not more Bandwidth.

> **[SIM FLAG — T13]** The packet's "super-linear" justification for the cap didn't reproduce at crew scale — extra actions measured **linear** (~2.2–2.6 win-points/fighter, 1–4 fighters, comparable to +2 DEX). **Keep the cap anyway**, justified as bounded risk: the vault's own single-duel sim measured a comparable skill (Quick Shot) at +24%, an order of magnitude larger, in a context this crew-scale test doesn't cover.

### 28.2 · Chems **[PACKET]**

Single-use, Workshop-gated. Stat boost for one battle. **Dependence** counter 0–3; each use past the first rolls an escalating resistance test (`1d10+NRV−Dependence` vs 7+), harder each time. Never touches Crew Rating.

> **[SIM-CONFIRMED — T14]** Math is correct and runs the right direction. Expected clean uses before failure: 1.55 (NRV+0) to 3.02 (NRV+4) — even an iron-nerved fighter cracks inside three uses. Reads as a short-term gamble, exactly as intended.

---

## 28.5 · Appendix — Board Representation & Tokens **[DRAFTED — new integration]**

How to physically show every game element at the table; any collection (DIY, 3D-printed, bought) plugs in the same way.

- **Terrain:** represent however you like, declare the one-line profile at setup (`Type · Movement · Cover · tags`).
- **Structures:** follow the same terrain rules; footprint sizes are sheet bookkeeping, not a strict model-size requirement (±1–2" tolerance). Every interactive tag (Openable, Lockable, Hackable, Searchable) must be **visibly** marked on the table — nothing interactive is invisible. Disabled structures get a face-down/flipped marker.
- **Infrastructure:** a labelled token on or beside the structure; show current state via the token's orientation (open/closed, on/off). Triggers/terminals are permanent — leave the token in place all game.
- **Objectives:** a chip/disc/coin per marker; a held objective is just "bodies within 3"" in this first pass.
- **Conditions:** one token per condition beside the model — Stress as a die/bead count, persistent conditions as coloured rings, Pinned/Down/Prone by laying the model down, Hidden as a "?" token or removed to a sheet, Ready as a die/arrow that persists across rounds.
- **Deployables:** place the actual model plus a small owner marker; track Online→Offline→Destroyed by turning or removing it.

---

## 28.6 · The Season — how a campaign ends **[NEW]**

A campaign is played as a **Season**. A Season ends immediately when either player **Controls 4 territories** at the end of any Settlement Phase — that player wins outright. Otherwise it ends after **each player has fought 10 battles**, and the higher **Season Score** wins:

| Source | Points |
|---|:--:|
| Per Controlled territory | 3 |
| Per Functional structure built after founding | 1 |
| Per fighter at Level 5+ still on the roster | 1 |

^tbl-season-score

Tiebreak: total banked Credits + Materials. *(All values provisional — the point is that campaign pacing now has an end to pace toward.)* After a Season, players may continue into a new one keeping settlement and roster: fresh Season Score, fresh battle count.

---

## 28.7 · Appendix — a worked founding and first campaign turn **[NEW]**

**Founding.** Rosa picks **Fire Station** (free Bunkhouse). She starts with HQ, Generator (+5), Processor, Salvage Yard and the Bunkhouse. Founding budget **125 Materials + 75 Credits**: she builds a **Med-bay** (65 Mat), banking **60 Mat + 75 Cr**.

Power draw: HQ 1 + Processor 1 + Salvage Yard 1 + **Bunkhouse 1** + Med-bay 1 = **5 of 5 — nothing spare.** Her free Location structure cost her the whole margin, and her next build needs a second Generator first. *(That is the tension §19 says should arrive on the second build, arriving exactly on schedule.)*

**Crew (Campaign Start, 425 CR).** Leader **Marisol** (185) + Assault Rifle (35) = **220** · Fighter **Deke** (100) + Pistol (15) = **115** · Recruit **Junie** (70) + the free bat = **70**. **Total 405 / 425**, 20 Credits spare. Pyramid legal: exactly one Leader, three models, no Specialists to ratio against.

**Battle 1** — Take a Hold on a neutral territory. Marisol claims two terminals; Junie goes Down in round 5 and the crew cannot reach her. **Win.** Rewards: **70 Cr + 15 Mat**.

**Post-Battle.** Junie rolls Fate at +1 (Med-bay): a 6 becomes 7 → **Lasting scar, broken arm** (−1 STR next battle only). Marisol survived and held an objective → **Level 1: +1 to any stat.** Deke survived → **Level 1**.

**Settlement Phase.** Bank to **145 Cr + 75 Mat** — 145 is over the **90 Cr store** (HQ 75 + Salvage buffer 15), **which is legal**: caps bite only at phase end (§20). Assign the crew's one worker to the **Processor** (+1 Materials per gather). Buy Junie a Pistol (15 Cr → 130 Cr). Scavenge dispatch (HQ I): loot roll 6 → **+15 Materials** → 90 Mat.

The phase closes at **130 Cr + 90 Mat**. Her Materials cap is HQ 75 + Processor buffer 15 = **90** — exactly at cap, nothing lost. Her Credits cap is HQ 75 + Salvage buffer 15 = **90**, and she is holding **130**. **40 Credits spoil.** Rosa's first real lesson: she needed a Storehouse (50 Mat) more than she needed the Med-bay.

**Battle Prep.** Choose the next territory; the cap stays 425 CR; Junie fields with her scar. Roll the Twist once deployment is set.

---

## 29 · What's still genuinely open

**Two terms you asked about, in plain English:**
- **"Economy sink"** means: settlements pile up Credits/Materials faster than they have anything worth spending them on, so the number just sits there unused. It's not a balance danger (nobody's winning unfairly) — it's closer to a design *waste*: a wealthy settlement's surplus isn't buying interesting decisions, it's idling. The fix is more expensive high-tier things to build, or ongoing costs, so a rich settlement's wealth is actually doing something. Not addressed by this turn's changes — still open.
- **"D21"** is a specific numbered decision in `POINTS-DECISIONS.md`, the vault's own log of settled pricing calls — it's about whether weapon costs should add together or multiply together as you stack characteristics onto a weapon (additive vs. multiplicative pricing). It's outside this document's scope (it's a Weapons/List Building pricing question), but the sim data flagged that the test used to justify D21's answer might have a bug in it, so it's worth someone re-checking before treating D21 as bedrock. Not something you need to solve — just flagging it exists.

**Resolved most recently:** Worker Proficiency's 0–100 tiered tracking system was cut entirely from v1 (§22) — a worker is now assigned or not, full stop, one flat benefit, no number to grow. This was flagged as verging on rules bloat relative to its payoff, and it's a fair catch: it's the same category of cut this project has made repeatedly elsewhere (per-head upkeep, Heat/Attention, HP-based structure damage). The full three-tier version wasn't discarded — it's preserved as a collapsed appendix in §22, explicitly scoped as future-supplement content rather than a core rule.

**Resolved this turn, by direct instruction:**
- Deployables costs converted to the 1000-Credit scale (§12.6, ×10 conversion off the vault's own stated anchor).
- Captured and Hardened both fully drafted (§26.3a, §26.3b) — Captured gated to Recruits/Fighters only, with a rescue-raid escape valve, ransom, and a two-stage brainwash path; Hardened grants a free Level.
- The entire post-battle → Settlement Phase → Battle Prep sequence drafted (§25.5) — this was `Downtime.md`, confirmed `Not Started` in the vault, and everything else in this document that referenced a "Settlement Phase" was assuming content that didn't exist until now.
- Advancement finalized as a **10-Level track** (§26.1) after several rounds of iteration — 6 lifetime stat points, 4 total skills (1 starting + 3 leveled, all one fixed path), one WND bump at Level 7. This applies to **Campaign Start** crews specifically — the Level track is what a persistent campaign fighter grows through. **List Building now runs two separate starting tiers, not one** (§16): **Match Play** crews (one-off games, no persistence) keep the original richer starting kit (~2/~3/~4 skills, Credits 95/165/245), because those fighters never get a second chance to develop. **Campaign Start** crews begin lean (1 skill per rank, Credits 75/125/170) at **425 Crew Rating**, with a **loosened pyramid** (one Leader, minimum three models, no ratio requirement) — deliberately, since a green crew hasn't built a chain of command yet. The Campaign Start Credits and the loosened pyramid are both first-draft and untested — worth checking the same way the standard pyramid's model-count balance was checked (`Crew Sim — Findings`) once played. The +1 WND price used to be the one number in this whole area with zero validation behind it; as of 2026-08-13 it is **41 Credits**, derived from the measured value of heavy armour (-2 on the injury roll, 41 Credits, `armour-level-n2500` 2026-08-13) - both buy the same thing, the model staying on the table longer (§26.1). The Campaign Start Credits and the loosened pyramid are now the untested numbers here.
- Hidden + objectives resolved (§25, §10): holding costs nothing and doesn't break Hidden; claiming/scoring always requires an Interact, which now explicitly breaks Hidden. Closes the sim's 17.9-point open question in practice.
- Water killed for good (§21): any structure can be sabotage-charged during any raid using the mechanic the Sabotage scenario already had, no bespoke Water target needed.
- Raid fairness resolved (§5): defender wins all Priority ties during a raid. One small lever, not a stacked pile of exceptions.

**Resolved earlier, still holding:** per-head upkeep (confirmed unneeded and harmful), Deeds cap (6, measured), Attack Back (confirmed load-bearing), payload cap (readability not balance), Scar-treatment cap (confirmed necessary), Bandwidth's super-linear justification (reframed), Chems math (confirmed).

**Every "Open dials" list from Scenarios/Deployables/Infrastructure is still real and unresolved — these are playtest questions, not design gaps, and none of this turn's changes touched them:**
- *Scenarios:* hold radius/no-Round-1-scoring as the Control-game pace levers · Caravan speed and a possible symmetric two-caravan variant · Sabotage's 3-round fuse (now doing double duty as the general structure-sabotage timer too, per this turn's Water fix — worth extra attention) · Power Supply's node count/line range need table validation.
- *Deployables:* Burst Turret's two-shot pricing · Revive Beacon's Down-recovery swing · turret auto-fire frequency · the two-aura cap actually biting at the table · Seeker mine movement on a small board.
- *Infrastructure:* CRUSH lethality · Blast Door's CRUSH-vs-Displace choice · conveyor/vent distances · one-vs-two features per building · the Generator macro-toggle's off-by-default.

**Confirmed genuinely not started anywhere in the vault — a gap in the game, not in this document:** Diplomacy, Edge Cases, Solo & Co-op, Balance, Components, Narrative, Rulebook. All carry `status: Not Started` in the source. *(Downtime is no longer on this list — drafted this turn.)*

**Drafted this turn — Stress persistence (§9, §10, §11), 2026-08-29:**
- **Stress now survives being Downed**, and a Down unit takes no Break tests until Stabilized. Drafted rather than locked: **pending playtest**, on the grounds that only the table can say whether losing a just-rescued fighter reads as brutal-good or brutal-bad. Measured in `Stress Persistence — Sim Findings`; costs ~1 revival in 53 walking off at today's rates.
- **Still to decide:** whether **surplus Attack Dice injury passes convert to +1 Stress each**. Measured and ready (`attack-dice-15b-surplus`), deliberately NOT adopted alongside persistence — together they roughly **2.2×** the Stress on a downed model and take wasted revivals from ~1-in-11 to nearly 1-in-4. **Test persistence alone first**, then decide. Note the conversion does nothing at all at WND 1 unless persistence is in force, so this ordering is the only one that makes either rule legible.
- **Valve on standby, not applied:** *"a Stabilised fighter returns Shaken, however much Stress it had."* One clause if persistence plays too punishing.
- **Watch for:** the death-spiral risk in `Dice Mechanic — Sim Findings` §7 — many triggers × a compounding −1 — which persistence directly compounds.

**Opened this turn — Attack Dice (§15), ruled 2026-08-29 but with live sub-decisions:**
- **Do surplus whiffed dice Pin?** §15 step 4 says yes, and that is the **only** thing separating the two candidate resolutions — they are otherwise **the same weapon**, with identical P(Down) at every dice count. Saying *no* (apply strictly one result and discard the rest) cuts effective suppression by **14–40%** and caps a burst at **one** Stress, so a 3-die burst would suppress exactly as hard as a pistol. That deletes the mechanic's stated second identity rather than trimming it, which is why step 4 reads as it does — **but it was not explicitly ruled, and Ross's worked example does not disambiguate it** (both readings give the same answer in that example, because the target went Down). Wants a tick.
- **The gates in §15 are PROPOSED, not law.** Rank gate, one-per-crew on AD 3, manufactured-only on AD 3. The brief pre-authorised gating if the auto-include flag fired and it fired hard: AD 3 beats the Heavy Gunner benchmark by **+51%** on identical fielded Credits, and a DEX +0 Recruit with 3 dice out-shoots a DEX +6 marksman. Price alone cannot fix a stat-ceiling breach — same shape of problem as the 24" range threshold, which was solved with gates.
- **Split fire is still unruled.** §15 assumes all dice go at the declared target. Allowing a burst to split across targets would change the maths materially — surplus dice would stop being wasted, which is the assumption the one-wound cap and the whole cost table rest on.
- **Is 3 the ceiling?** Nothing in the maths breaks past 3, but the auto-include gap widens with each die. Reserving 4+ for turrets and vehicles is untested either way.
- **A defect this pass turned up in a neighbouring harness, unrelated to Attack Dice:** `test-bench/sim_report.py` applies Stress on a *successful* wound as well as a failed one, which contradicts §9 and §10. Invisible at WND 1 (a wound ends the fight), but at WND 3 it roughly **doubles** the break rate — the published "~1.75 breaks/fight" in `Dice Mechanic — Sim Findings` §7 measures **0.744** rules-correct. The qualitative claim that morale is a duration mechanic probably survives; the number does not. Needs its own pass.

**Still open, unchanged by this turn:**
- The economy sink (explained above).
- **AGI is unpriced by construction.** The engine reads it only inside the Dodge reaction and `DODGE_ON` is False, so it measures exactly zero. One of five stats has never been priced; it currently rides the opposed ladder at ×0.8 by analogy. *(The old "16–34 vs 15" underprice flag is closed — that figure was contaminated and the flat rate is gone.)*
- **Five weapon payloads are blocked** (§15) — Crippling, Concussive, Blinding, Hook, Toxic all measure ≤0 net because they replace Pinned, which measures +0.510. Needs a rules ruling on replace-not-stack, not a reprice.
- **Fifteen of twenty-four deployables are unpriced** (§12.6) — the four traps beyond Trip Wire, five of seven beacons, the Remote chassis and all five mine payloads.
- D21's methodology flag (explained above).
- Territory terrain-type → pre-built terrain list mapping.
- Loot markers vs. the 9–12 terrain-density budget — confirm they're counted separately. *(The default Loot table itself is now drafted, §23 — this remaining item is specifically about physical loot-marker footprint on the board, a separate question.)*
- Crafted vs. manufactured weapon-origin tiers, including the conditions-asymmetry hook — dropped by the packet, never replaced.
- HQ tier costs, Med-bay/Mess Hall numbers — first-draft guesses, untested.
- Worker benefit numbers (§22) are first-draft, untested — the same flag as everything else content-shaped in this document, now simpler to check since there's no Proficiency curve to validate alongside them.
- BUILDER-type on-table construction units — mentioned in original vision notes, never built anywhere.
- A worked example of objective-completion → specific settlement benefit.
- Scale note: `List Building.md`'s old 5/8/16/24 ladder is superseded everywhere in this document by the 1000-Credit scale; worth a one-line flag in that file itself.
- Three flagged-but-unfixed skill/characteristic conflicts from `Weapons.md` §7: Long Barrel is dead, Knockback vs. Heavy Impact and Ghost Blade vs. Balanced are thin overlaps.

This is the Tier 4/5 list from the last review, minus everything Tier 1–3 just closed. Ready for more context whenever you want to tackle it.

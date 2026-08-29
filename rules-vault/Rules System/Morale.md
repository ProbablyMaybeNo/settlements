---
type: rule-phase
phase: "17"
stage: S2 Core Combat
status: Drafted
build_order: 11
depends_on: ["Damage"]
feeds_into: ["Scenarios", "Final Alpha", "Solo & Co-op", "Factions", "Edge Cases"]
tags: [settlements/phase, settlements/stage/s2]
---
# 17 · Morale
> **S2 Core Combat** · status **Drafted** · build order **11**

**Depends on:** [[Damage]]
**Feeds into:** [[Scenarios]], [[Final Alpha]], [[Solo & Co-op]], [[Factions]], [[Edge Cases]]
**Raw dependency (from Notion):** Damage

## Focus
When crews break — fear, insanity, bottling, rout, surrender. ✅ After this you have a playable combat skirmish.

The Rules column should nail down:
- Morale / Fear / Insanity tests: what triggers them, the stat used (Morale), and target numbers.
- Bottling: when a crew tests to flee the field — design it to be the NORM, not the exception.
- Individual vs crew-wide effects (a single fighter pinned/fleeing vs the whole crew bottling).
- Insanity and Fear mechanics and how they alter behaviour and tie back to the initiative phase.
- Recovery / rally rules and how leaders steady nearby fighters.

## Inherits from the engine
> [!info] This note **is** the source of the Stress system. The engine only reserves it: [[Rules Engine#Nerve / Stress]] (Stress does not affect Priority). Everything else lives below.

## Working rules / decisions

### Stress
Stress represents fear, panic, suppression and shock. It is tracked as points on a unit and tested against **NRV**. Stress does **two separate jobs** — a small always-on penalty, and a break test once it piles up.

**A unit gains +1 Stress when it:**
- Takes a **non-wounding hit** — the **Pinned** (ranged) or **Shaken** (melee) result of a failed Injury roll. *(Every hit does exactly one thing — it **wounds** or it **stresses**, never both; a clean **miss** does nothing.)*
- Gains a negative condition (Fire, Poison, Blind, Shocked)
- Has a friendly go **Down** or **Out of Action** within line of sight
- Suffers a hazard, skill, or scenario effect that says so

**Environmental Stress** = Stress from the board itself — hazards, weather, fire, smoke, cold — as opposed to *combat* Stress (being shot or fought). Some gear ignores the first Environmental Stress each game (e.g. Thick clothing, [[Weapons]]).

> [!info] More triggers are coming
> The sim shows Stress from combat alone barely fires in a 1v1 ([[Dice Mechanic — Sim Findings]]). That's expected — most Stress will come from **skills, hazards, terrain and scenario events**, which stack far faster at crew scale. Tune trigger *frequency* before touching the numbers below.

### Shaken — the always-on penalty
Any unit with **1+ Stress is Shaken: −1 to all rolls.** Flat, passive, no test — it does **not** grow with more Stress. This is the reliable "under fire, rattled, shooting worse" effect, and it is the *only* thing 1 Stress does. You risk actually breaking only once Stress reaches 2. **Shaken carries into your next turn** — a point of Stress never clears on the same round you gain it (see Recovery), so hitting a unit in melee is never wasted: it fights its next activation at −1.

### Break test — End Phase, 2+ Stress
Every End Phase, each unit with **2+ Stress** tests:

`1d10 + NRV − (Stress − 1)` vs **7+**

- The first Stress point is a free buffer — it costs you the −1, not the test.
- The **Shaken −1 does not apply to this roll.** Stress is already in the formula; don't double-count it.
- **Natural 10 →** auto-pass. **Natural 1 →** auto-fail.

- **Pass →** the unit steadies: remove **all** Stress.
- **Fail →** the unit **breaks** into the state set by its Stress level, then removes **1** Stress:

| Stress | Break state |
|:---:|---|
| 2 | **Bolt** |
| 3 | **Broken** |
| 4+ | **BugOut** |

^tbl-break-test-end-phase-2-stress

**Chance of breaking** on a failed roll (`1 − pass%`):

| NRV | 2 → Bolt | 3 → Broken | 4 → BugOut |
|:---:|:---:|:---:|:---:|
| +0 | 70% | 80% | 90% |
| +2 | 50% | 60% | 70% |
| +4 | 30% | 40% | 50% |

^tbl-break-test-end-phase-2-stress-2

### Nerve states
Full status entries in [[Conditions]]. A state governs the unit's **next activation**; it clears when the unit passes its next Break test or is steadied by Rally/Interact.
- **Bolt** — flees toward the nearest board edge, hugging cover.
- **Broken** — freezes; cannot act.
- **BugOut** — routs: moves full speed off the nearest board edge and is **removed from play** (a casualty).

> [!question] BugOut replaces the old "Insanity"
> The worst state is now a clean **rout off the table**, not attack-nearest-model. Fits the name and the gritty-realism pillar better than berserk-attacks-allies. Flag to revisit if you want the chaos option back.

> [!success] Validated at crew scale — **do not touch these numbers** (2026-07-13)
> The friendly-Down trigger looked, on paper, like it would wipe crews: three casualties in LOS is 3 Stress, and a Break test at NRV 0 / Stress 3 fails **80%** of the time. [[Crew Sim — Findings|The crew sim]] says leave it alone. On a legal board ([[Terrain#Setup procedure|9–12 features]]) the cascade is mild — **0.6 BugOuts per battle**, versus 5.3 on an illegally sparse one. Two proposed softeners were tested and **both broke the game**:
> - *"Ignore Stress from friendly Downs while bunched"* → took a 14-model horde to **93–96% win rate at every terrain density.**
> - *"Cap Stress from friendly Downs at 1 per round"* → flipped a sparse board from 19% to **60%** for the horde.
>
> **The cascade is not a bug — it is the only thing keeping a swarm honest.** A mob of civilians crossing open ground under rifle fire *should* shatter. Dense terrain is the mitigation, and it already works.

### Bottling — voluntary concession
Breaking happens *to* a crew (the Nerve states above); **bottling** is a crew *choosing* to quit the field. Any player may bottle — but **when** decides **how**:

- **Rounds 1–3 — an early bottle is never free.** You may not simply lift your crew off the table. Either:
	- **Fighting withdrawal** — walk every model off your **own** board edge by normal movement. They stay in play, and exposed, until they physically leave. A crew that clears the board this way has quit (it can no longer contest or score), but its survivors live to fight another day — see [[Campaign]]. *Or*
	- **Surrender** — offer it; if your **opponent accepts**, the game **ends immediately** as *their* victory.
- **Round 4 onward — a clean bottle.** Declare it during your activation; **all your models are removed from play at once and the game ends.** This is a **concession: the opponent wins**, whatever the objective score at that moment — an empty board holds nothing.

Scoring stops the instant you bottle or clear the board — see [[Scenarios#Concession, bottling & the wipe]].

> [!question] Alpha rule — campaign may soften it
> Under [[Campaign]] rules a bottle may become a *withdrawal* (save the roster for a resource/territory cost) rather than a flat loss. Test the flat version first.

### Stress and Down — persistence **[DRAFTED 2026-08-29 · pending playtest]**
> Measured in [[Stress Persistence — Sim Findings]]. Being Downed was never ruled either way; this closes that gap.

**Stress persists through Down.** A unit reduced to **0 WND** keeps every point of Stress it had. Going Down is not a rest.

- **A Down unit does not take Break tests.** It is out of the fight — it doesn't activate, so it can't Bolt, freeze or rout while lying there. Its Stress simply sits frozen with it. (It also can't shed Stress, since shedding requires a clean round or a passed test.)
- **Stabilize brings the fighter back with its Stress intact** ([[Damage#Down & bleeding out]]). From that moment it tests normally again — so a fighter recovered at **2+ Stress** faces a **Break test in the next End Phase**, and a failure at **4+** removes it outright.
- **No new test and no new trigger.** The End Phase Break test above already does all of this. The rule is the *absence* of a clearing step, which is why it costs nothing to write.

> [!warning] What this actually feels like at the table
> Someone spends an **Action and an INT test** to drag a friend up, and the friend may immediately bolt — or, at 4+ Stress, rout straight off the board. That is the intended beat: **you can patch the body faster than the nerve.** It also makes Stabilize a real decision instead of an automatic yes.
>
> Measured cost, NRV +2: **8.8%** of revived fighters fail their first Break test and **1.9%** BugOut immediately — roughly **one revival in fifty-three**. Story frequency, not a pattern to play around.

> [!question] Watch the stacking, not the rule
> If [[15b · Attack Dice|Attack Dice]] later also converts **surplus injury passes into Stress**, a downed model's Stress roughly **2.2×** (0.66 → 1.44 mean) and wasted revivals go from ~1-in-11 to nearly **1-in-4**. Both rules are defensible; adopt them **one at a time**, this one first. Note also that this compounds the **death-spiral risk** flagged in [[Dice Mechanic — Sim Findings]] §7.
>
> **Valve, held in reserve and deliberately not pre-applied:** *"a Stabilised fighter returns Shaken, however much Stress it had."* One clause, kills the bad beat, also kills the beat. Only the table can say which way it plays.

### Recovery
- **Passing a Break test** (2+ Stress) clears **all** Stress; a **natural 10** always clears all.
- **Being Downed clears nothing** — see *Stress and Down* above. A Down unit neither tests nor sheds; its Stress waits for it.
- **A point of Stress never clears on the round you gain it — it carries to your next turn.** A unit at **exactly 1 Stress** sheds it in the End Phase **only on a round where it took no new Stress.** So a fighter tagged in melee **stays Shaken (−1) right through its next turn** and only shrugs it off after a *clean* round — do **not** reduce it to 0 at the end of the turn it was hit. (At 2+ Stress you can't passively drain a real panic at all; you must pass a Break test.)
- **Everything else is a skill.** Removing Stress before/without a test, shedding it faster, or ending a **Bolt/Broken** state early comes from the **Bravery path** ([[Skill Paths]]) — *Steady, Count Breaths, Rally, Talk Them Down, Iron Will*, and the rest. Deliberately: composure is a build choice, not free.
- **BugOut can't be rallied** — the unit has already routed. It can only be stopped *at the moment of failure* by *Talk Them Down* or *Stand Your Ground*.

## Rule ledger
- [[core-006 Morale and suppression]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

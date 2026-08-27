---
type: rule-phase
phase: "35"
stage: S3 Battle Layer
build_order: 16
status: Drafted
depends_on:
  - Weapons
  - Conditions
  - Terrain Interaction
  - Damage
feeds_into:
  - List Building
  - Skill Paths
  - Scenarios
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 35 · Deployables
> **S3 Battle Layer** · status **Drafted** · build order **16**

**Depends on:** [[Weapons]], [[Conditions]], [[Terrain Interaction]], [[Damage]]
**Feeds into:** [[List Building]], [[Skill Paths]], [[Scenarios]]

## Focus
The gear a crew **builds and plants on the board** to deal or deny damage — turrets, mines, traps, and support beacons. [[Infrastructure]] reshapes the battlefield and deliberately *doesn't* hurt people; **that job lives here.** A deployable is bought like a weapon, carried by a fighter, and set up with an **INT test**.

> [!info] Why this note exists — two gaps the [[Hacking]] rework opened
> 1. **INT lost a job.** When hacking could injure a rival hacker, INT was a combat stat. v1 hacking only flips terrain switches, so INT needed a second battlefield role. **Deploying and repairing hardware is that role** — an INT-heavy crew is now the *engineer / sapper*, not just the door-opener.
> 2. **Terrain stopped dealing damage.** [[Infrastructure]] routes all harm through two rare keywords and says plainly: *"a thing that exists only to hurt people belongs in gear, not in the walls"* ([[Infrastructure#Infrastructure vs Deployables]]). Deployables are where that damage went — you carry your killbox now, you don't find it bolted to the scenery.

## Design contract — the five rules that keep this honest
Deployables inherit the [[Weapons|weapon contract]] and add two of their own.

1. **Deployables deal or deny damage; Infrastructure reshapes the board.** If a piece exists to hurt or lock down the enemy, it is a deployable. If it exists to move routes, sight, cover or elevation, it is [[Infrastructure]].
2. **A deployable applies conditions — it never defines them.** Every condition it inflicts is written in [[Conditions]].
3. **A deployable attack does exactly one thing: it wounds, or it delivers its payload — never both** ([[Damage]]). A deployable attack is a normal **Injury roll** (`1d10 + Damage − Armor` vs **7+**); it invents no new damage maths, and it obeys the same **+5 Damage ceiling** and **±3 modifier cap** as everything else.
4. **One deploy is your Action.** Setting a deployable up costs the fighter's Action for that activation. Once placed, standing hardware acts **on its own** — that is what you paid for.
5. **INT builds and repairs; DEX disarms.** Assembling and arming a device is technical work (**INT**). Defusing someone else's is fine-motor work under pressure (**DEX**). See [[Terrain Interaction#Stat ownership]].

## What a deployable is
- **Bought like equipment.** Each deployable has a points cost and is taken in [[List Building]] against a fighter's equipment allowance. It is **kit**, not a stat or a skill.
- **One use per battle — kept on the roster.** A deployable is a physical thing your crew owns. Once it is **spent** (a mine detonates) or **destroyed** (a turret is wrecked) it is gone **for the rest of that battle** — but it returns, re-armed and repaired, for the **next** battle. Deployables are **never a per-game consumable**; you buy them once and they persist across the campaign like any weapon.
- **Two shapes:**
  - **Spent-on-trigger** (mines, traps) — waits concealed, fires once at the first enemy that meets its condition, then it is spent.
  - **Standing hardware** (turrets, beacons) — sits on the board and works every round until it is destroyed. **Repairable once** (below).

## Deploying — the INT test
> [!info] Recall — deploying is **one core test**: `1d10 + INT + Build vs 7+`, the same engine as everything else.

1. **Declare & place.** Spend your **Action**; place the deployable within **1"** (base contact for standing hardware). One Action = one deploy.
2. **Roll** `1d10 + INT + Build rating` vs **7+**.
3. **Pass** → the deployable is **active**: a mine/trap is **armed and concealed**; standing hardware is **online**.
4. **Fail** → it is **placed but exposed and inert**: a mine/trap is **armed but visible** (the enemy can see it, avoid it, disarm or shoot it); standing hardware sits **Offline** until a fighter gets it running (a **repair**, below).
5. **Nat 1** → **backfire.** A mine/trap **triggers on the deployer** (resolve its effect against them); standing hardware is **Destroyed** for this battle. **Nat 10** auto-succeeds as normal.

Pre-placed **settlement** deployables (a [[Terrain Interaction#In-battle repair / settlement hook|Trap stockpile]], or a turret on a built [[Structures|Turret Mount]]) skip the roll — they **deploy armed and concealed / online** during setup.

> [!warning] Auto-deploy is all that ownership buys
> Owning the structure removes the **INT test**, nothing else. The deployable still **costs Credits against your Crew Rating** in [[List Building]], still occupies a slot inside the sacred **9–12** density band ([[Terrain#Settlement boards — the same procedure, one square-set pre-filled|settlement boards]]), and keeps **full fragility** — `WND−1`, repairable once, hijackable, destroyable. A bigger settlement never means a bigger army.

### Build rating — some things are harder to build
The **Build rating** is a modifier on the deploy test, printed on the item. It is **intrinsic to the device**, not a difficulty the table assigns — a sentry gun is genuinely fiddlier than a tripwire. It obeys the global **±3** cap alongside skills, conditions and **Shaken**.

| Build | Modifier | Feel |
|---|:---:|---|
| **Simple** | **+1** | wire, spikes — anyone can lay one |
| **Standard** | **0** | a straight 7+ |
| **Complex** | **−1** | most turrets & beacons — a Specialist's job |
| **Intricate** | **−2** | the flagship hardware (sniper / burst turret) |

^tbl-build-rating-some-things-are-harder-to-build

A low-INT fighter can *carry* a Sentry Gun; reliably **standing it up under fire** is what INT buys.

## Destruction & repair — reuse the Feature-damage engine
Nothing new here: deployables that sit on the board are **Features**, and they take damage exactly like every other interactive feature ([[Terrain Interaction#Feature damage]]).

- **Standing hardware** (turrets, beacons): **WND 1**, **Armour −2**, cover **Heavy (−2)** to be hit unless the attacker is within **6"** (then **Open**). One successful Injury → **Offline** (dead weight, still blocks LOS). **Repair once**: a fighter adjacent passes an **INT test (7+)** to bring it back **online** (**Jury-Rig** may auto-succeed). A **second** Injury while Offline → **Destroyed**, gone for the battle. *This is the "repaired one time before it's lost" rule — it already existed; deployables just use it.*
- **Mines & traps**: **concealed** on a passed deploy (found by **Threat Scan** or an opposed INT test). While **untriggered** they can be **shot** (Feature damage) or **disarmed** — **DEX 7+**, nat 1 = boom; or, if the device is electronic (**Remote**), **Jammed** or hacked instead (**Jam Signals** / **Minefield Conductor**, [[Hacking]] · [[Skill Paths]]). Once a trap **triggers**, it is spent — you cannot Offline a boom mid-trigger.

---

## Family A · Turrets
Standing hardware · **repairable** · takes **both** equipment slots.

A deployed turret holds a **Ready** reaction. **Once per round**, as a **Reaction**, it auto-fires one shot at the **first enemy that Moves or acts within its range and LOS**. It has **no facing** (360°) and never moves. The shot is a normal ranged attack — hit, then Injury — using the profile below. A turret fires at a fixed **+0 gunnery** (a crude auto-mount) plus the target's cover; the **Sniper Turret's +1** is on top of that.

> [!note] Turrets are yours; hijacking them is the counterplay
> A deployed turret **auto-fires for its owner** — that is what the points and the one-hit fragility buy. There are **no board-built turrets**; *every* turret is a deployable. An enemy **hacker can hijack one** — deactivate it, lock it off their squad (**Rewrite Killbox**), or fire it at its own side (**Turret Tamer**) — see [[Hacking#Linked functions (what a successful hack controls)]].

| Turret | Build | Credits | Range | Auto-fire profile |
|---|:---:|:---:|:---:|---|
| **Autoturret** | Complex −1 | **10** | 18" | One shot / round, Injury **Damage +3**. The baseline — a sidearm on a tripod. |
| **Sniper Turret** | Intricate −2 | **25** | 24" | One shot / round, **Damage +3**, **+1 to hit** (it never moves, so it is always braced). Reaches from its own deployment zone. A rifle on a tripod. |
| **Burst Turret** | Intricate −2 | **20** | 18" | **Two** shots / round at **Damage +2** each (same or split targets). Volume of fire — priced up because multi-shot is the game's biggest DPS lever. |
| **Blast Turret** | Complex −1 | **15** | 12" | One shot / round, **Damage +3**, **Blast** (2" — resolve against every model within 2" of the target). |
| **Reinforced Turret** | Complex −1 | **15** | 18" | One shot / round, **Damage +3**. **Hardened:** always counts as **Heavy (−2) cover** to be hit — the within-6" *Open* clause does **not** apply, so it can't be walked up to and wrecked. |

^tbl-family-a-turrets

## Family B · Mines
Spent-on-trigger · **concealed** · **one** equipment slot each. **Built like a weapon:** pick a **chassis** (how it reaches the target), then buy **one payload** (what it does). Cost = chassis + payload.

### Chassis — how it delivers
| Chassis | Credits | Delivery |
|---|:---:|---|
| **Proximity** | **5** | Place a **3" template**. Detonates the instant an enemy **ends a Move** inside it. |
| **Remote** | **[UNPRICED]** | Place a hidden marker with a **6" trigger radius**; the **owner command-detonates** it while any enemy is inside the radius (a **Reaction** costing a Ready token; it ignores the forward-arc / end-of-move requirement, like the Hacking Interrupt). **Bluff kit:** buying a Remote gives you **4 markers — 1 live, 3 dummy**. The carrier may spend an activation to place a dummy; only the live marker ever detonates. The enemy can't tell which is which without a **Threat Scan** or a disarm. |
| ~~**Seeker**~~ | **PARKED** | **Not in v1** — a self-moving munition on a 3'×3' board is an edge-case factory (does it draw Reactions? trigger traps? get shot as a Feature? what is its facing?). Parked, not rejected; revisit once [[Edge Cases]] exists. Proximity and Remote carry the family, and Remote's bluff kit is the interesting one anyway. ([[Out of Scope — What Settlements is NOT#4 · Rejected-ideas log]]) |

^tbl-chassis-how-it-delivers

### Payload — what it does on detonation
Buy exactly one. All effects route to rules you already have.
| Payload | Credits | Effect |
|---|:---:|---|
| **Explosion** | **[UNPRICED]** | Injury **Damage +3**, **Blast** (2"). The default killer. |
| **Fire** | **[UNPRICED]** | **Blast** Injury **Damage +2**, sets **Fire**, leaves a **3" Fire** hazard for one round ([[Terrain#Hazards (the Dangerous overlay)]]). |
| **Poison** | **[UNPRICED]** | Places a **3" Poison** hazard for two rounds ([[Conditions#Persistent conditions (resolve in the End Phase)|Poison]] to anyone inside or entering). |
| **Shock** | **[UNPRICED]** | **Blast**, no Injury: **Shocked + Blind** on every model in radius ([[Conditions#Control conditions (from skills, weapons and terrain)]]). |
| **Smoke** | **[UNPRICED]** | No damage — places a **3" Dense Smoke** ([[Weapons]] Smoke). A trap that screens instead of kills. |

> [!warning] Why the payloads are held rather than guessed
> A mine payload's natural neighbour is the **weapon characteristic it mirrors** — and Poison mirrors **Toxic**, Shock mirrors **Shocking**, and both sit inside the **blocked-payload problem** ([[Weapons#Payload — *replaces* the non-wounding result]]). Pricing a mine off a trait that measures negative would bake the same defect into a second catalogue. These unlock the moment the replace-not-stack rule is ruled on.

^tbl-payload-what-it-does-on-detonation

*Examples:* a mine costs **chassis + payload**. With only the Proximity chassis priced, no complete mine has a shipping cost yet — Proximity is **5** and every payload is held.

## Family C · Traps
Spent-on-trigger · **concealed** · **one** equipment slot each. **Traps deny movement** — that is their whole job. Mines kill; [[Infrastructure]] reshapes; traps **stop, channel and wall off** the enemy. Almost none deal damage.

| Trap | Build | Credits | Trigger & effect |
|---|:---:|:---:|---|
| **Trip Wire** | Simple +1 | **5** | Within **1"** → the model is knocked **Prone**. Stops a rush cold. |
| **Spike Strip** | Simple +1 | **[UNPRICED]** | A **3" area**; enemies entering treat it as **Difficult** ground and gain **Hobbled**. Persists until cleared. |
| **Covered Pit** | Standard 0 | **[UNPRICED]** | A concealed **2" hole** that reads as normal floor. A model entering **FALLs** ([[Terrain]] verticality — **Prone**) and is **Snared** (stuck until it climbs out). |
| **Leg Clamp** | Standard 0 | **[UNPRICED]** | Within **1"** → the model is **Snared** (cannot move; Action + **STR 7+** to break free). A hard single-model stop. |
| **Razor Barrier** | Standard 0 | **[UNPRICED]** | Deploy a **3" barrier**: **Impassable** without **Forcing** it (STR 7+, and you take **Hobbled** shoving through). A pure movement wall — blocks bodies, not sight. |

^tbl-family-c-traps

## Family D · Beacons
Standing hardware · **repairable** · takes **both** equipment slots. A beacon projects a **6" aura** that persists until the beacon is destroyed. Auras are the **modifiers the engine already uses** — friendly buffs or enemy debuffs.

> [!warning] Two rules keep beacon-stacking honest
> - An aura **obeys the global ±3 cap** and **does not stack with itself** (two Munitions Beacons ≠ +2).
> - **A model benefits from at most two friendly beacon auras at once.** Pick the two if more overlap. This is the brake on a death-star stack.

| Beacon | Build | Credits | Aura (within 6") |
|---|:---:|:---:|---|
| **Munitions Beacon** | Complex −1 | **5** | *Allies:* **+1 to the Injury roll** (a damage buff — capped by ±3; never lifts a weapon past its class band's ceiling). |
| **Targeting Beacon** | Complex −1 | **[UNPRICED]** | *Allies:* **+1 to ranged hit rolls.** |
| **Aegis Beacon** | Complex −1 | **[UNPRICED]** | *Allies:* enemy **Injury rolls against them suffer −1** (the "+1 armour" aura, as a capped modifier). |
| **Cover Beacon** | Standard 0 | **[UNPRICED]** | *Allies:* count as in **Light cover** (−1 to be hit) if not already in better cover. |
| **Cleansing Beacon** | Standard 0 | **[UNPRICED]** | *Allies:* each **End Phase**, one friendly in range **clears one negative condition** (Fire, Poison, Blind, Shocked, Pinned); also acts as a **Med-Kit** for Stabilize / Bleed. |
| **Revive Beacon** | Intricate −2 | **10** | *Allies:* each **End Phase**, one friendly **Down** unit in range **recovers to Prone** (stands next activation). **Down only — a melee kill (Out) stays dead.** |
| **Dread Beacon** | Standard 0 | **[UNPRICED]** | *Enemies:* a model that **enters** the aura gains **+1 Stress**; while inside, **−1 on Break tests**. The one negative-aura beacon. |

^tbl-family-d-beacons

## How INT gets its job back
Deployables hand a technical crew a full battlefield loop — and every step is INT:

- **Build** it (deploy test), **Repair** it (**Jury-Rig**), **Find** the enemy's (**Threat Scan**, **Forensic Sweep**).
- **Seize or suppress** the enemy's: **Trapper** (arm/disarm/reposition), **Jam Signals** ([[Hacking]]), **Turret Tamer**, **Minefield Conductor**, **Trap Relay**, **Kaboom** — the whole INT-path *Trapper / Engineer / Hacker* families now have real targets ([[Skill Paths]]).

That is the design payoff: an INT specialist is no longer *only* a door-opener. They plant the killbox, keep it running, and turn the enemy's own devices against them.

## Open dials
> [!warning] Nine of twenty-four entries are priced. The rest are **[UNPRICED]** and not legal to field.
> **Repriced onto the gear scale 2026-08-27.** The old ×10 conversion priced deployables against the **body** scale, which is why a Burst Turret cost **189% of the Fighter deploying it**. They are now derived the way the costing engine states: **a deployable prices at the weapon class it mounts** — the persistence premium and the immobility/destructibility discounts cancel — and every entry is held under the gear:body cap. Source: `test-bench/points/ticks.py` · `DEPLOYABLE_CREDITS`.
>
> **Priced:** all five turrets · Proximity chassis · Trip Wire · Munitions and Revive Beacons.
> **Unpriced:** the Remote chassis · all five mine payloads · four of five traps · five of seven beacons.
>
> Marking them rather than guessing is deliberate — **an untagged number is the exact defect the points rebuild exists to remove.** The derivation rule is written down, so this is a short job; it just has to happen in the engine, not in this note.

- [ ] **Burst Turret's two shots.** Multi-attack is the biggest DPS lever in the game ([[Skill Sim — Findings]]). +2×2 is priced high and gated (Intricate −2) — first item to watch. Fallback: one shot with **Spread**.
- [ ] **Revive Beacon.** Returning Down units in a **WND-1** game is a huge swing — bounded to *one unit, to Prone, Down-only*. If it warps games, cut it to a flat Med/Cleansing effect.
- [ ] **Turret auto-fire.** One Reaction shot / round is the lever. If a free static gun proves oppressive, drop it to **fire only when operated**.
- [ ] **Slot weight.** Standing hardware eating **both** slots + the **two-auras-per-model** cap are the anti-stack brakes — confirm they bite at the table.
- [ ] **Price the fifteen held entries** — the Remote chassis, five mine payloads, four traps and five beacons. Blocked behind the replace-not-stack ruling for the payloads; the traps and beacons are derivable now.
- [x] ~~**Seeker movement.**~~ Parked with the chassis — revisit only if [[Edge Cases]] resolves the moving-munition questions.

## Rule ledger
_none yet — graduate a `core-00X Deployables` card after the first deployables sim / playtest._

---
See [[Rules System MOC]] · deals damage through [[Damage]] · conditions in [[Conditions]] · costed in [[List Building]] · skills in [[Skill Paths]] · sim in [[Deployables Sim — Findings]] · not to be confused with [[Infrastructure]].

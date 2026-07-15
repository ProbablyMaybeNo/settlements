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
Deployables inherit the [[Weapons#Design contract — the three rules that keep this honest|weapon contract]] and add two of their own.

1. **Deployables deal or deny damage; Infrastructure reshapes the board.** If a piece exists to hurt or lock down the enemy, it is a deployable. If it exists to move routes, sight, cover or elevation, it is [[Infrastructure]].
2. **A deployable applies conditions — it never defines them.** Every condition it inflicts is written in [[Conditions]].
3. **A deployable attack does exactly one thing: it wounds, or it delivers its payload — never both** ([[Damage]]). A deployable attack is a normal **Injury roll** (`1d10 + Damage − Armor` vs **7+**); it invents no new damage maths.
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

Pre-placed **settlement** deployables (a [[Terrain Interaction#In-battle repair / settlement hook|Trap stockpile]] or turret emplacement, or the **Wire & Sandbag** doctrine) skip the roll — they **deploy armed and concealed / online** during setup.

### Build rating — some things are harder to build
The **Build rating** is a modifier on the deploy test, printed on the item. It is **intrinsic to the device**, not a difficulty the table assigns — a sentry gun is genuinely fiddlier than a tripwire. It obeys the global **±3** cap alongside skills, conditions and **Shaken**.

| Build | Modifier | Feel |
|---|:---:|---|
| **Simple** | **+1** | wire, spikes — anyone can lay one |
| **Standard** | **0** | a straight 7+ |
| **Complex** | **−1** | turrets, beacons — a Specialist's job |

A low-INT fighter can *carry* a Sentry Gun; reliably **standing it up under fire** is what INT buys.

## Destruction & repair — reuse the Feature-damage engine
Nothing new here: deployables that sit on the board are **Features**, and they take damage exactly like every other interactive feature ([[Terrain Interaction#Feature damage]]).

- **Standing hardware** (turrets, beacons): **WND 1**, **Armour −2**, cover **Heavy (−2)** to be hit unless the attacker is within **6"** (then **Open**). One successful Injury → **Offline** (dead weight, still blocks LOS). **Repair once**: a fighter adjacent passes an **INT test (7+)** to bring it back **online** (**Jury-Rig** may auto-succeed). A **second** Injury while Offline → **Destroyed**, gone for the battle. *This is the "repaired one time before it's lost" rule — it already existed; deployables just use it.*
- **Mines & traps**: **concealed** on a passed deploy (found by **Threat Scan** or an opposed INT test). While **untriggered** they can be **shot** (Feature damage) or **disarmed** — **DEX 7+**, nat 1 = boom; or, if the device is electronic/Linked, **Jammed** or hacked instead (**Jam Signals**, [[Hacking]]). Once a trap **triggers**, it is spent — you cannot Offline a boom mid-trigger.

## The four families
> [!warning] Costs below are a **first pass**, anchored to comparable gear in [[Weapons#5 · Sample armoury|the armoury]] (Trap 4 · Med-Kit 4 · Molotov 9 · Assault Rifle 13). They are **not sim-validated yet** — treat them as the starting ladder for a deployables sim, exactly as the weapon costs were before [[Crew Sim — Findings]].

**Carry weight:** a **mine or trap** takes **one** of a fighter's two equipment slots. **Standing hardware** (a turret or beacon) is bulky — it takes **both** slots, so a fighter carrying one carries nothing else.

### A · Emplacements — turrets (standing hardware · repairable · both slots)
A deployed turret holds **Overwatch**. **Once per round**, as a **Reaction**, it auto-fires one shot at the **first enemy that Moves or acts within its range and LOS**. It has **no facing** (360°) and never moves.

| Turret | Build | Cost | Auto-fire |
|---|:---:|:---:|---|
| **Sentry Gun** | Complex −1 | **14** | One Reaction shot / round, **18"** + LOS, Injury **Damage +3**. |
| **Scrap Autogun** | Complex −1 | **10** | One Reaction shot / round, **9"** only, Injury **Damage +4** (Brutal). Cheaper, deadlier, short-sighted. |

> [!note] Deployable turrets **auto-fire**; board turrets do **not**. A **settlement / [[Infrastructure]] turret** is *controlled only* — someone must hack or operate it to fire ([[Hacking#Linked functions (what a successful hack controls)]]). A **deployable** turret you paid points for, that dies to a single hit, earns its automatic shot. The two are deliberately different objects, not a contradiction.

### B · Mines — proximity charges (spent on trigger · concealed · one slot)
Trigger on the **first enemy** to enter the listed range, resolve once, then **spent**.

| Mine | Build | Cost | Trigger & effect |
|---|:---:|:---:|---|
| **Frag Mine** | Standard 0 | **8** | Within **2"** → Injury **Damage +3**, **Blast** (every model within 2"). |
| **Shaped Charge** | Standard 0 | **7** | Within **1"** → single target, Injury **Damage +3**, **Armour Piercing** (−1 Armor). Anti-armour. |
| **Incendiary Charge** | Standard 0 | **8** | Within **2"** → **Blast** Injury **Damage +2**, sets **Fire**, and leaves a **3" Fire** hazard for one round ([[Terrain#Hazards (the Dangerous overlay)]]). |

### C · Traps — control devices (spent on trigger · concealed · one slot)
Mostly **no Injury** — they exist to stop, blind or choke a route, not to kill. Trigger once, then spent (an **area** trap persists until cleared or destroyed).

| Trap | Build | Cost | Trigger & effect |
|---|:---:|:---:|---|
| **Snare Wire** | Simple +1 | **4** | Within **1"** → the model is **Prone** + **Hobbled**. No Injury. |
| **Spike Strip** | Simple +1 | **4** | A **3" area**; enemies entering it treat it as **Difficult** ground and gain **Hobbled**. Persists. |
| **Flash Charge** | Standard 0 | **5** | Within **2"** → **Blast**, no Injury: **Blind + Shocked** on every model in radius. |
| **Gas Canister** | Standard 0 | **6** | Within **2"** → places a **3" Poison** hazard for two rounds ([[Conditions#Persistent conditions|Poison]] to anyone inside or entering). |

### D · Beacons — support auras (standing hardware · repairable · both slots)
A beacon projects a **friendly aura** in a radius (default **6"**). The aura is one of the **modifiers the engine already uses** — it obeys the global **±3** cap and **does not stack with itself** (two Munitions Beacons ≠ +2).

| Beacon | Build | Cost | Aura (friendly, within 6") |
|---|:---:|:---:|---|
| **Munitions Beacon** | Complex −1 | **8** | **+1 to the Injury roll** (a damage buff — capped by ±3; never lifts a weapon past the +4 Damage ceiling). |
| **Targeting Beacon** | Complex −1 | **8** | **+1 to ranged hit rolls.** |
| **Med-Station** | Standard 0 | **6** | Acts as a **[[List Building#Armour & equipment|Med-Kit]]** for everyone in range — cancels the −2 on Stabilize / treating Bleed & Poison. |
| **Bulwark** | Standard 0 | **5** | Deploys a **3" barricade**: a line of **Light cover** that **Blocks LOS** through it ([[Terrain#Cover]]). A carried version of the **Wire & Sandbag** Deployed piece. |

## How INT gets its job back
Deployables hand a technical crew a full battlefield loop — and every step is INT:

- **Build** it (deploy test), **Repair** it (**Jury-Rig**), **Find** the enemy's (**Threat Scan**, **Forensic Sweep**).
- **Seize or suppress** the enemy's: **Trapper** (arm/disarm/reposition), **Jam Signals** ([[Hacking]]), **Turret Tamer**, **Minefield Conductor**, **Trap Relay**, **Kaboom** — the whole INT-path *Trapper / Engineer / Hacker* families now have real targets ([[Skill Paths]]).

That is the design payoff: an INT specialist is no longer *only* a door-opener. They plant the killbox, keep it running, and turn the enemy's own devices against them.

## Open dials
- [ ] **Every cost is first-pass** — anchored to the armoury, not yet run through a deployables sim.
- [ ] **Turret auto-fire.** One Reaction shot/round is the lever. If a static gun that shoots for free proves oppressive, drop it to **fire only when operated** (an INT/DEX Interact), matching the board turret.
- [ ] **Slot weight.** Standing hardware taking **both** equipment slots is the main brake on beacon/turret stacking — confirm it bites at the table.
- [ ] **Build ratings.** −1 for all Complex hardware is a placeholder; a −2 tier is reserved if the flagship turret should demand a true specialist.
- [ ] **Aura radius.** 6" default across all beacons — may want to shrink the damage aura specifically.

## Rule ledger
_none yet — graduate a `core-00X Deployables` card after the first deployables sim / playtest._

---
See [[Rules System MOC]] · deals damage through [[Damage]] · conditions in [[Conditions]] · costed in [[List Building]] · skills in [[Skill Paths]] · not to be confused with [[Infrastructure]].

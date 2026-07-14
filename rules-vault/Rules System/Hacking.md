---
type: rule-phase
phase: "33"
stage: S3 Battle Layer
status: Drafted
build_order: 14
depends_on:
  - Terrain
  - Terrain Interaction
  - Rules Engine
feeds_into:
  - Settlement
  - Scenarios
  - Skill Paths
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 33 · Hacking
> **S3 Battle Layer** · status **Drafted** · build order **14**

**Depends on:** [[Terrain]], [[Terrain Interaction]], [[Rules Engine]]
**Feeds into:** [[Settlement]], [[Scenarios]], [[Skill Paths]]

## Focus
Terminals, Linked networks, range-banded control, and hacker-vs-hacker duels. Physical Interacts (Lift, Force, Search, traps) stay in [[Terrain Interaction]] — this note is the digital layer.

The Rules column nails down:
- How a fighter operates a terminal (declare → range → **Access roll**; a **Breach roll** follows only in a hacker duel).
- Range bands as modifiers on the core **7+** test (max 24").
- What a breach does, **graded by the roll total** (Shut Out → Power Surge → Take Over → Brain Hack).
- Contested control when two operators share a network.
- Hacker-vs-hacker as a **Head-to-Head** access, then a breach.
- How turrets, cameras, doors, and alarms plug in without a second dice mechanic.

## Inherits from the engine
> [!info] Recall — hacking reuses combat's rolls: an **Access roll** (the to-hit) and, **only when a rival hacker defends**, a **Breach roll** (the injury). A **solo** hack is a single Access; a **duel** is Access → Breach. Range is a **modifier**, not a new target number. **Program** and **Firewall** are hacking's **Damage** and **Armor**. Feature **Offline** / **Destroyed** and device states (**Jammed**, **Linked**, **Compromised**) live in [[Terrain Interaction#Feature damage]] and [[Conditions]].

![[core-000 Core Test#Text]]

## Working rules / decisions

### Terminals & Linked features
- A **terminal** is terrain a fighter can Interact with while in **base contact**.
- Features are **Linked** only when the scenario or settlement says so — range alone never makes something Linked.
- Operating a terminal spends the unit's **Action** slot.
- One Action = one hack = **one Access** (plus **one Breach** if a rival hacker defends) = at most **one** Linked function, unless a skill says otherwise ([[Skill Paths]]).

### One roll, or two — depends on whether anyone's home
A hack resolves like an attack. **How many rolls you make depends on whether a rival hacker is defending the network.**

**Solo hack** — no rival hacker in base contact with a linked terminal. **One roll:**
- **Access roll** → `1d10 + INT + range − Firewall` vs **7+**. *Firewall* here is the system's **static hardening** (unhardened terminal = **0**; military/settlement systems buy it up).
- **Pass** → immediately activate **one** Linked feature within the range band you rolled at — open the door, loop the camera, fire the turret, cycle the compactor. **That is the whole hack.**
- **Fail** → you leave a **foothold**: the system becomes **Compromised** ([[Conditions]]) — **+2** to your next Access against it. **Nat 1** → not even that.
- **No Breach roll** — there's no rival system to breach into, and nothing to injure.

**Hacker duel** — a **rival hacker** is in base contact with a linked terminal on the same network. **Two rolls:**

**1 · Access roll** — the *to-hit*, now a **Head-to-Head**: both roll `1d10 + INT + mods`, highest wins, **ties → defender**. This is the race to seize the wire. (Static Firewall does **not** modify this — the rival's live opposed roll *is* the defence.) Winning earns you the Breach; the loser gets nothing.

**2 · Breach roll** — the *injury*: `1d10 + Program − Firewall` — read the **total**. **Tiers do not stack — resolve only the highest tier you reach.** Every result targets the **rival and their terminal**:

| Breach total | Effect                                                                                                                                                                                                                                                                                                                    |
| :----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    **7+**    | **Shut Out** — the rival's feature goes **Jammed / Offline** until the end of their next activation. You've locked them out.                                                                                                                                                                                              |
|    **8+**    | **Power Surge** — the **rival's terminal** blows: **Destroyed**, unusable for the rest of the game. Any fighter in **base contact with it** (the rival hacker included) gains **+1 Stress**. They've lost their way in.                                                                                                    |
|    **9+**    | **Take Over** — you seize the network and become its **controller**. **Either** take control — immediately activate **one** Linked feature within the range band (turret fire is your **one attack** for the activation) — **or** overload it (resolve as **Power Surge**).                                                 |
|   **10+**    | **Brain Hack** — you upload into the rival's synapse-link and puppet their unit: **activate it now** under your control, acting exactly as a normal activation except **you** choose its actions. **This is that unit's activation this round** — it does not act again.                                                    |

- Below **7** → you won the wire but can't get deep. You leave a **foothold**: the rival's system is **Compromised** — **+2** to your next Access against it.
- **Nat 1** → a **1 never breaches**: nothing happens, not even a foothold.
- **Nat 10** → a **10 always breaches** (never a mere foothold), but read the **total** as written — **Firewall still gates which tier you reach**.

### Program & Firewall — Examples of hacking's Damage & Armor. Granted as benefits of Equipment + Skills.
- **Program** (= +DMG) is your breach power in a **duel**, from hacking **gear or skills** (a breach kit, an exploit suite). Default **+0** bare-handed — but a real hacker carries one, just as a fighter carries a weapon. (In a **solo** hack there's no Breach, so Program does nothing — it's your weapon for hacker fights.)
- **Firewall** (= Armor) is a system's hardening, from hardened terminals, security software, or a defender's gear/skills. Default **0**; military and settlement systems buy it up. It works in **both** modes without double-dipping: a **penalty to a solo Access roll** (harder to crack), and a **reduction to the attacker's Breach total** in a duel.
- *Example values (TBD in playtest):* Breach Kit **Program +1** · Exploit Suite **+2** · Firewall Node **Firewall −1** · Military ICE **−2**. Several INT skills grant or beat these — see [[Skill Paths]].
  
> [!question] These are either two examples of a range of breach roll modifers or the categories that all the other breach equipment, skills, etc, fall under.

### Range bands
Measure **terminal → feature** (or **attacking terminal → defending terminal** for a duel). Max **24"**. Applies to the **Access roll**.

| Band | Distance | Mod |
|---|---|:---:|
| Close | 0–6" | 0 |
| Short | 6–12" | −1 |
| Medium | 12–18" | −2 |
| Long | 18–24" | −3 |
| Out | 24"+ | illegal |

Other modifiers (skills, **Shaken**, conditions) stack normally; the global **±3** cap applies to the Access roll.

### Linked functions (what a successful hack resolves)
The **one** function a solo Access or a duel **Take Over** grants — one per Action unless a skill says otherwise:
- Doors — lock / unlock / open / close
- Cameras — loop / reveal / ignore named fighters
- Alarms — suppress next trigger / trip now
- Power — toggle a Powered system or printed hazard
- Turrets — rotate / deactivate / **fire once** (counts as your attack)
- Electronic traps — arm / disarm / trigger if legal

**Turrets are controlled only** — no auto-sentry.

### Network control
- A duel **Take Over (9+)** makes that fighter (or their crew) the network's **controller** until someone beats them in a Head-to-Head or takes a terminal another way. A **controller** hacks their own network **solo** (no defender); a rival must win a **Head-to-Head** against them to act on it.
- **Compromised** ([[Conditions]]) — from a **foothold** (a failed solo Access or a sub-7 Breach) or a skill (e.g. **Counter-Hack**) — doesn't change the TN; it hands the next Access **+2** as written.

### Action economy
One hack Action per activation. A Linked function that deals damage (turret fire, a triggered hazard) — whether from a **solo** hack or a duel **Take Over** — is your **one attack** for the activation; you may not also make a separate attack. A **Brain Hack** spends its Action on seizing the rival and puppeting them; the puppet acts on the rival's own profile, not yours.

### Skills
INT-path skills ([[Skill Paths]]) are exceptions and payoffs on top of these rules (**Hacker**, **Computer Whiz**, **Turret Tamer**, **Counter-Hack**, **Jam Signals**, **Kaboom**, **Mastermind**, etc.). They never replace the core rolls — they change what one Action can do, grant Program/Firewall, or change when you may React. **Counter-Hack** is what *turns a solo hack into a duel*: a defender Readied at a terminal reacts to a hostile hack, forcing the Head-to-Head and Breach that wouldn't otherwise happen.

> [!question] Playtest dials
> - **Solo vs duel split:** Breach fires *only* against a live rival hacker. Confirm defenders actually contest terminals often enough that duels happen — if hackers just avoid each other, the whole Breach table goes unused. **Counter-Hack** availability is the lever.
> - **Contested feature is harder:** a solo pass (7+) grants the feature; in a duel you need **Take Over (9+)** for it. That's deliberate (someone's fighting you for it) — watch that it doesn't make defended networks feel un-hackable.
> - **Breach tiers** 7/8/9/10 — exclusive (highest reached only). The 9+ **choice** (control *or* overload) keeps Take Over dominant over Power Surge; confirm it reads cleanly.
> - **Brain Hack (10+):** consumes the puppet's activation. Because Breach only happens in duels it *always* has a valid target now. Check the land-rate (see sim) isn't oppressive; if so, gate harder with Firewall or cap nat-10 at Take Over.
> - **Firewall's two jobs:** penalty to solo Access **and** −Breach in a duel. Set one number per system and see if it feels right in both modes.
> - **Program/Firewall ladder:** set the gear values once first playtests show how reliable breaches feel.

## Rule ledger
_none yet — graduate a `core-00X Hacking` stub after first playtest_

---
*See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*

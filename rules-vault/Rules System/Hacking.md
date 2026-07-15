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
Terminals, Linked features, and range-banded control of terrain. Physical Interacts (Lift, Force, Search, traps) stay in [[Terrain Interaction]] — this note is the digital layer.

**v1 is deliberately small:** you hack a terminal to control its Linked features, and an enemy at another terminal can **interrupt** you — Overloading their own terminal for the turn to jam one hack. One roll, one clean decision. A deeper hacker-vs-hacker system is drafted and **parked** at the bottom for a later version.

The Rules column nails down:
- How a fighter operates a terminal (declare → range → **INT test**).
- Range bands as modifiers on the core **7+** test (max 24").
- **Interrupt** — how an opponent at another terminal contests your hack, at the cost of their own.
- How turrets, cameras, doors, and alarms plug in without a second dice mechanic.

## Inherits from the engine
> [!info] Recall — a hack is **one core test**: `1d10 + INT − range` vs **7+**, the same engine as everything else. Range is a **modifier**, not a new target number. Device states (**Jammed**, **Linked**, **Overloaded**, **Compromised**) live in [[Conditions#Marker & device states]].

![[core-000 Core Test#Text]]

## Working rules / decisions

### Terminals & Linked features
- A **terminal** is terrain a fighter can Interact with while in **base contact**.
- Features are **Linked** only when the scenario or settlement says so — range alone never makes something Linked.
- Operating a terminal spends the unit's **Action** slot.
- One Action = one hack = at most **one** Linked function, unless a skill says otherwise ([[Skill Paths]]).
- **Access doesn't wear a terminal out.** A terminal used only to **access** features stays live all turn — different units may each hack it — but a **single unit may not access the same terminal twice in one turn.**
- **Interrupting does.** A terminal used to **interrupt** (below) becomes **Overloaded** and powers down until the **start of next turn**. So each turn a terminal is either your reusable access point *or* a one-shot interrupt — never both.

### Hacking a terminal — the core test
1. **Declare** the terminal and the Linked feature you want. The feature must be within a legal **range band** (below).
2. **Roll** `1d10 + INT − range band` vs **7+**.
3. **Pass** → activate that Linked feature now (open the door, fire the turret, trip the hazard, loop the camera).
4. **Fail** → nothing happens this activation.
5. **Nat 1 / Nat 10** = auto-fail / auto-succeed.

That's the whole hack. No damage roll, no second mechanic — controlling the feature *is* the reward.

### Range bands
Measure **terminal → feature**. Max **24"**. Applies to the hack test.

| Band | Distance | Mod |
|---|---|:---:|
| Close | 0–6" | 0 |
| Short | 6–12" | −1 |
| Medium | 12–18" | −2 |
| Long | 18–24" | −3 |
| Out | 24"+ | illegal |

Other modifiers (skills, gear, **Shaken**, conditions) stack normally; the global **±3** cap applies.

### Interrupt — contesting a hack
An enemy in base contact with another **live** (non-Overloaded) terminal on the network may **Interrupt** a declared hack. It's a **Reaction** — the *interrupt Interact* option ([[Initiative & Activation#Reaction options]]), and the one Reaction declared *as* the enemy acts rather than after they finish.

**Declare early, pay only if it lands:**
1. The hacker declares the terminal and the feature.
2. The enemy declares **Interrupt** — *before* the access roll.
3. The hacker rolls `1d10 + INT − range` vs **7+**.
   - **Fail** → the hack fails on its own. The interrupt is **not spent** — the interrupter's terminal stays **live**.
   - **Pass** → the interrupt **jams it**: the feature does **not** activate, and the interrupter's terminal becomes **Overloaded** (down till the start of next turn).

There's no opposed roll — the only die is the hacker's access. A declared interrupt automatically jams a hack that *would* have landed, and costs nothing against one that fails anyway.

**What it does and doesn't do:**
- It stops **one** access attempt — **not** the terminal for the turn. A *different* unit can hack the same target terminal again; and once an interrupter has Overloaded their terminal, they can't stop that second attempt. **Bait the interrupt with one unit, land the hack with the next.**
- Each interrupter terminal absorbs exactly **one** successful hack per turn. To push a feature through a defended network, bring bodies (see sim).

**The decision:** an interrupt spends your terminal for the turn to deny one enemy feature. Worth it to jam the turret about to shoot your squad; rarely worth it to stop a door.

### Linked functions (what a successful hack controls)
The **one** function a passed hack grants — one per Action unless a skill says otherwise:
- Doors — lock / unlock / open / close
- Cameras — loop / reveal / ignore named fighters
- Alarms — suppress next trigger / trip now
- Power — toggle a Powered system or printed hazard
- Turrets — rotate / deactivate / **fire once** (counts as your attack)
- Electronic traps — arm / disarm / trigger if legal

**Turrets are controlled only** — no auto-sentry.

> The full catalogue of operable features — cranes, bridges, shutters, vents, flood gates — and exactly what each does to the board (with every crush/fall/push routed to an existing rule) lives in [[Infrastructure]]. Hacking is *how* you operate them; Infrastructure is *what happens*.

### Modifiers — from gear & skills, not a hardening stat
A hack test takes **+/− modifiers** like any other roll: hacking **gear** (Breach Kit, Exploit Suite — [[Weapons]] / [[List Building]]), INT **skills** ([[Skill Paths]]), **conditions**, and **Shaken**. Difficulty is the same in reverse — a defender's gear/skill or a scenario may impose a **penalty** on enemy hacks against a device. There is **no separate "hardened systems" stat**; toughness is just a modifier, and the global **±3** cap applies.

### Action economy
One hack per activation. A feature that deals damage (turret fire, a triggered hazard) is your **one attack** for the activation — you may not also make a separate attack.

### Skills
INT-path skills ([[Skill Paths]]) are exceptions and payoffs on top of these rules (**Hacker**, **Computer Whiz**, **Turret Tamer**, **Counter-Hack**, etc.). They modify the hack test, change what one Action can do, or change how the **interrupt** works — e.g. **Counter-Hack** lets a fighter Interrupt *without* Overloading their own terminal.

> [!question] Playtest dials
> - **Interrupt is a hard counter** — automatic against a *successful* hack, no opposed roll. Because it only spends when the hack would land, one interrupter reliably eats one feature per turn. A lone hacker can't beat an interrupter alone — the sim shows you need **two** successful hacks to push one through. If that's too strong, let a hacker's **nat 10** punch through, or add an opposed INT test.
> - **Bait dynamic** — Overload (not turn-long lockout) + multi-use terminals means a second unit beats a spent interrupter. The **Overloaded-till-next-turn** duration is the lever if interrupts feel too weak or too strong.
> - **Hack-modifier ladder** — set the gear/skill +/− values once first playtests show how reliable an unmodified hack feels.

## Rule ledger
_none yet — graduate a `core-00X Hacking` stub after first playtest_

---

> [!note]- Parked — deeper hacking (a later version, do not build yet)
> A two-roll **breach** system was drafted then set aside to keep v1 simple. Recorded here so the design isn't lost; the full drafted text lives in git history (see commits around the `hacking_sim.py` two-roll work).
>
> **Shape:** a hack is *Access* (the to-hit) then, **only against a live rival hacker**, a *Breach* roll (the injury) — `1d10 + Program − Firewall`, exclusive tiers:
> - **7+ Shut Out** — deny the feature for a turn.
> - **8+ Power Surge** — destroy the contested terminal (symmetric denial).
> - **9+ Take Over** — seize control of the network + activate a feature.
> - **10+ System Shock** — brick the rival hacker's unit (forfeits its next activation). *A full "puppet the unit into a hazard" version exists but is quarantined to opt-in hacker duels only — never off a normal terminal Interact.*
>
> **Key decisions already made (so we don't re-litigate):**
> - Breach targets **terrain control**, not the fighter's body — losing a breach costs you the terminal, not your model. This is what keeps hacking from *dissuading* terrain interaction.
> - The catastrophic "steal the unit and walk it into lava" outcome is a **tail you can't out-reward** — bound it (System Shock) or quarantine it to duels; don't try to make features juicy enough to justify it.
> - **Program** = breach damage, **Firewall** = armor / static hardening. In v1 **neither is a stat** — gear and skills grant flat +/− modifiers to the hack test instead ([[Weapons]]). When this system is revived those modifiers would land mostly on the **breach** roll.
> - Graduate this only if v1 hacking proves too thin at the table.

*See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*

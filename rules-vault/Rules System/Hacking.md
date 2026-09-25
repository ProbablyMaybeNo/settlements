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
  - Skills
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 33 · Hacking
> **S3 Battle Layer** · status **Drafted** · build order **14**

**Depends on:** [[Terrain]], [[Terrain Interaction]], [[Rules Engine]]
**Feeds into:** [[Settlement]], [[Scenarios]], [[Skills]]

## Focus
Terminals, Linked features, and range-banded control of terrain. Physical Interacts (Lift, Force, Search, traps) stay in [[Terrain Interaction]] — this note is the digital layer.



The Rules column nails down:
- How a fighter operates a terminal (declare → range → **INT test**).
- Range bands as modifiers on the core **7+** test (max 24").
- **Interrupt** — how an opponent at another terminal contests your hack, at the cost of their own.
- How turrets, cameras, doors, and alarms plug in without a second dice mechanic.

## Inherits from the engine
> [!info] Recall — a hack is **one core test**: `1d20 + INT − range` vs **7+**, the same engine as everything else. Range is a **modifier**, not a new target number. Device states (**Jammed**, **Linked**, **Frozen**) live in [[Conditions#Marker & device states (not conditions on units)]].

![[core-000 Core Test#Text]]

## Working rules / decisions

### Terminals & Linked features
- A **terminal** is terrain a fighter can Interact with while in **base contact**.
- Features are **Linked** only when the scenario or settlement says so — range alone never makes something Linked.
- Operating a terminal spends the unit's **Action** slot.
- One Action = one hack = at most **one** Linked function, unless a skill says otherwise ([[Skills]]).
- **Access doesn't wear a terminal out.** A terminal used only to **access** features stays live all turn — different units may each hack it — but a **single unit may not access the same terminal twice in one turn.**


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
| Close | up to 6" | 0 |
| Short | over 6", up to 12" | −1 |
| Medium | over 12", up to 18" | −2 |
| Long | over 18", up to 24" | −3 |
| Out | over 24" | illegal |

^tbl-range-bands

Other modifiers (skills, gear, **Shaken**, conditions) stack normally; the global **±3** cap applies.

### Interrupt
Interrupt is the INT skill in [[Skills#INT]]. It requires contact with an active terminal and an enemy terminal interaction within 12 inches. Resolve opposed INT; success cancels that interaction and FREEZEs the enemy terminal until the end of the next turn. It may be used after the source has activated. No automatic veto or self-Overload applies. See [[Skill Integration Decisions]] for unresolved frequency/network details.

### Linked functions (what a successful hack controls)
The **one** function a passed hack grants — one per Action unless a skill says otherwise:
- Doors — lock / unlock / open / close
- Cameras — loop / reveal / ignore named fighters
- Alarms — suppress next trigger / trip now
- Power — toggle a Powered system or printed hazard
- Turrets — rotate / deactivate / **fire once** (counts as your attack)
- Electronic traps — arm / disarm / trigger if legal

**Turrets are [[Deployables]].** There are **no board-built turrets** — every turret is a deployable that **auto-fires for its owner**. Hacking one **hijacks** it: deactivate it, turn it, or fire it once at its own side (your Action).

> The full catalogue of operable features — cranes, bridges, shutters, vents, flood gates — and exactly what each does to the board (with every crush/fall/push routed to an existing rule) lives in [[Infrastructure]]. Hacking is *how* you operate them; Infrastructure is *what happens*.

### Modifiers — from gear & skills, not a hardening stat
A hack test takes **+/− modifiers** like any other roll: hacking **gear** (Breach Kit, Exploit Suite — [[Weapons]] / [[List Building]]), INT **skills** ([[Skills]]), **conditions**, and **Shaken**. Difficulty is the same in reverse — a defender's gear/skill or a scenario may impose a **penalty** on enemy hacks against a device. There is **no separate "hardened systems" stat**; toughness is just a modifier, and the global **±3** cap applies.

### Action economy
One hack per activation. A feature that deals damage (turret fire, a triggered hazard) is your **one attack** for the activation — you may not also make a separate attack.

### Skills


> [!question] Playtest dials


> - **Hack-modifier ladder** — set the gear/skill +/− values once first playtests show how reliable an unmodified hack feels.

## Rule ledger
_none yet — graduate a `core-00X Hacking` stub after first playtest_

---

> [!note]- Parked — deeper hacking (a later version, do not build yet)
> A two-roll **breach** system was drafted then set aside to keep v1 simple. Recorded here so the design isn't lost; the full drafted text lives in git history (see commits around the `hacking_sim.py` two-roll work).
>

## Current skills
Neural Uplink adds +4 to HACKING tests. Trojan operates an enemy ELECTRIC deployable. Interrupt contests terminal interactions. Full effects: [[Skills#INT]].

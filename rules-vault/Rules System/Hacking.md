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
Terminals, Linked networks, range-banded control, and hacker-vs-hacker shut-outs. Physical Interacts (Lift, Force, Search, traps) stay in [[Terrain Interaction]] — this note is the digital layer.

The Rules column should nail down:
- How a fighter operates a terminal (declare → range → roll).
- Range bands as modifiers on the core **7+** test (max 24").
- What one successful hack can do (one Linked function).
- Contested control when two operators share a network.
- Hacker-vs-hacker shut-outs: opposed INT → Effect roll → Shut-out table.
- How turrets, cameras, doors, and alarms plug in without a second dice mechanic.

## Inherits from the engine
> [!info] Recall — hacking reuses the [[Rules Engine#Universal Resolution Mechanic|core test]] and [[Rules Engine#Opposed Tests|opposed tests]]. Range is a **modifier**, not a new target number. Feature **Offline** / **Destroyed** and device states (**Jammed**, **Linked**, **Compromised**) live in [[Terrain Interaction#Feature damage]] and [[Conditions]].

![[core-000 Core Test#Text]]

## Working rules / decisions

### Terminals & Linked features
- A **terminal** is terrain a fighter can Interact with while in **base contact**.
- Features are **Linked** only when the scenario or settlement says so — range alone never makes something Linked.
- Operating a terminal spends the unit's **Action** slot.
- One Action = **one** Linked function, unless a skill says otherwise ([[Skill Paths]]).

### Range bands
Measure **terminal → feature** (or **terminal → defending terminal** for shut-outs). Max **24"**.

| Band | Distance | Mod |
|---|---|:---:|
| Close | 0–6" | 0 |
| Short | 6–12" | −1 |
| Medium | 12–18" | −2 |
| Long | 18–24" | −3 |
| Out | 24"+ | illegal |

Other modifiers (skills, **Shaken**, conditions) stack normally. The global **±3** modifier cap still applies.

### Terminal Interact (feature control)
1. Base contact with a **terminal**.
2. Declare one **Linked** function within 24".
3. Apply the range modifier.
4. **Uncontested** → `1d10 + INT + mods` vs **7+**.  
   **Contested** → opposed **INT** (same mods; **ties to the current controller**).
5. Pass / win → that one function resolves. Fail / lose → nothing.

**Natural 1** / **Natural 10** still auto-fail / auto-succeed on uncontested tests.

### Example Linked functions
One per Action unless a skill says otherwise:
- Doors — lock / unlock / open / close
- Cameras — loop / reveal / ignore named fighters
- Alarms — suppress next trigger / trip now
- Power — toggle a Powered system or printed hazard
- Turrets — rotate / deactivate / **fire once**
- Electronic traps — arm / disarm / trigger if legal

**Turrets are controlled only** — no auto-sentry. Firing a turret from a terminal **counts as your attack** for the activation.

### Network control
- The first successful hack on a network this battle makes that fighter (or their crew) the **controller** until someone beats them in an opposed hack or takes the terminal another way.
- **Compromised** ([[Conditions]]) may apply from skills (e.g. **Counter-Hack**) — it does not change the TN; it modifies the next opposed hack as written.

### Hacker vs hacker (shut-out)
Use this when you want to attack another operator instead of a terrain feature.

1. Attacker is in base contact with a terminal.
2. Target a fighter who is in base contact with a **terminal** (defending terminal may be the same network or another — measure **attacking terminal → defending terminal**).
3. Both roll opposed **INT** with range and other mods. Highest wins; **ties → defender** (nothing happens).
4. If the **attacker** wins → make an **Effect roll**: `1d10` vs **7+** (no weapon Damage).
   - **Fail** → **Nothing** (won the duel, payload didn't land).
   - **Pass** → roll on the **Shut-out table**.

### Shut-out table
| d10 | Effect |
|:---:|---|
| 1–2 | **Glitch** — nothing extra |
| 3–5 | **Shut down** — defending terminal is **Jammed** / offline until the end of the defender's **next activation** |
| 6–7 | **Destroyed** — defending terminal goes **Offline** (see [[Terrain Interaction#Feature damage]]; Repairable; second hit = removed) |
| 8–9 | **Take Over** — attacker becomes controller of that terminal **this activation** and may immediately resolve **one** Linked function measured from *that* terminal's range bands (turret fire still counts as the attack) |
| 10 | **Overload** — terminal goes **Offline** + defending hacker takes an automatic hit: Injury `1d10 + 0 − Armor` vs **7+** |

> [!question] Playtest dials
> - **Take Over** on 8–9 may snowball — consider **10 only** if games swing too hard.
> - **Overload:** Injury +0 vs auto-**Pinned** vs auto-**Down** — tune at the table.
> - **Shut down** duration: end of next activation (current) vs end of next round.

### Action economy
One hack Action per activation — either a **feature function** or a **shut-out**, not both (unless **Take Over** grants the follow-up function).

### Skills
INT-path skills ([[Skill Paths]]) are exceptions and payoffs on top of these rules (**Hacker**, **Computer Whiz**, **Turret Tamer**, **Counter-Hack**, **Jam Signals**, **Kaboom**, **Mastermind**, etc.). They never replace the core test — they change what one Action can do or when you may React.

## Rule ledger
_none yet — graduate a `core-00X Hacking` stub after first playtest_

---
_See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

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
- How a fighter operates a terminal (declare → range → **Access roll → Breach roll**).
- Range bands as modifiers on the core **7+** test (max 24").
- What a breach does, **graded by the roll total** (Shut Out → Power Surge → Take Over → Brain Hack).
- Contested control when two operators share a network.
- Hacker-vs-hacker as a **Head-to-Head** access, then a breach.
- How turrets, cameras, doors, and alarms plug in without a second dice mechanic.

## Inherits from the engine
> [!info] Recall — hacking is **the same two rolls as combat**: an **Access roll** (the to-hit) then a **Breach roll** (the injury). Range is a **modifier**, not a new target number. **Program** and **Firewall** are hacking's **Damage** and **Armor**. Feature **Offline** / **Destroyed** and device states (**Jammed**, **Linked**, **Compromised**) live in [[Terrain Interaction#Feature damage]] and [[Conditions]].

![[core-000 Core Test#Text]]

## Working rules / decisions

### Terminals & Linked features
- A **terminal** is terrain a fighter can Interact with while in **base contact**.
- Features are **Linked** only when the scenario or settlement says so — range alone never makes something Linked.
- Operating a terminal spends the unit's **Action** slot.
- One Action = one hack (**one Access + one Breach**) = **one** Linked function, unless a skill says otherwise ([[Skill Paths]]).

### Two rolls — same as combat
A hack resolves exactly like an attack: **Access roll** (did you get in?) → **Breach roll** (how deep?).

**1 · Access roll** — the *to-hit*:
- **Undefended** system → `1d10 + INT + range` vs **7+**.
- **Defended** system, or a **rival hacker** at a terminal → **Head-to-Head**: both roll `1d10 + INT + mods`, highest wins, **ties → defender**.
- **Nat 1 / Nat 10** = auto-fail / auto-succeed. Fail → nothing happens.

**2 · Breach roll** — the *injury*, only on a successful Access:
`1d10 + Program − Firewall` — read the **total** (each tier includes the ones below):

| Breach total | Effect                                                                                                                                                                                                                                        |
| :----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    **7+**    | **Shut Out** — the feature is **Jammed / Offline** until the end of the target's next activation (denial).                                                                                                                                    |
|    **8+**    | **Power Surge** — **Terminal** **explodes** due to a **power surge**, it cannot be used for the rest of the game and a **hacker** in base to base contact becomes **shaken**. until the end of their next turn.                               |
|    **9+**    | **Take Over** — Attacker takes control of defenders terminal. Immediately gains 1 free terrain feature activation at the same range band as the initial successful access roll.                                                               |
|   **10+**    | **Brain Hack** — Attacker takes complete control of defenders unit. Immediately activate (or re-activate) defender under opponents control. Acts exactly as it would under a normal activation except actions are determined by the opponent. |

- Below **7** → you got in but achieve **nothing** this activation (a glitch).
- **Nat 1 / Nat 10** on the Breach = auto-fail / auto-succeed (a natural 10 always reaches **Brain Hack**).

### Program & Firewall — Examples of hacking's Damage & Armor. Granted as benefits of Equipment + Skills.
- **Virus** (= +DMG) is your breach power, from hacking **gear or skills** (a breach kit, an exploit suite). Default **+0** bare-handed — but a real hacker carries one, just as a fighter carries a weapon.
- **Firewall** (= Armor) reduces the attacker's Breach total, from hardened terminals, security software, or a defender's gear/skills. Default **0**; military and settlement systems buy it up.
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

### Linked functions (what Take Over resolves)
One per Action unless a skill says otherwise:
- Doors — lock / unlock / open / close
- Cameras — loop / reveal / ignore named fighters
- Alarms — suppress next trigger / trip now
- Power — toggle a Powered system or printed hazard
- Turrets — rotate / deactivate / **fire once** (counts as your attack)
- Electronic traps — arm / disarm / trigger if legal

**Turrets are controlled only** — no auto-sentry.

### Network control
- The first successful breach on a network this battle makes that fighter (or their crew) the **controller** until someone beats them in a Head-to-Head or takes the terminal another way.
- **Compromised** ([[Conditions]]) from skills (e.g. **Counter-Hack**) doesn't change the TN — it modifies the next Access roll as written.

### Action economy
One hack Action per activation = one **Access + Breach**. A **Take Over** / **Brain Hack** function (e.g. turret fire) is your **one attack** for the activation — you may not also make a separate attack.

### Skills
INT-path skills ([[Skill Paths]]) are exceptions and payoffs on top of these rules (**Hacker**, **Computer Whiz**, **Turret Tamer**, **Counter-Hack**, **Jam Signals**, **Kaboom**, **Mastermind**, etc.). They never replace the two rolls — they change what one Action can do, grant Program/Firewall, or change when you may React.

> [!question] Playtest dials
> - **Breach tiers** 7/8/9/10 — check Power Surge (8+) isn't strictly better than Take Over (9+) in play.
> - **Brain Hack duel auto-hit:** `+Program` damage vs auto-**Pinned** vs auto-**Down** — tune at the table.
> - **Program/Firewall ladder:** set the gear values once first playtests show how reliable breaches feel.

## Rule ledger
_none yet — graduate a `core-00X Hacking` stub after first playtest_

---
*See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*

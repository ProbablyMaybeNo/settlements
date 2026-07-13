---
type: reference
title: Weapons
tags: [settlements/reference]
---
# 🔫 Weapons

The catalogue of weapon profiles and traits. The *rules* that govern them live in [[Damage]] and [[Shooting]] / [[Melee]] — this note is the reference they point to.

> [!info] Weapon design principle
> **Stats decide if you land the hit. Weapons decide how dangerous, loud, reliable, and situational it is.** Most weapons do **not** add to hit — they set **Damage** and carry **traits**. Only rare weapons grant a conditional **+1 to hit**.

## Damage classes
Damage feeds the **Injury roll** (`1d10 + Damage − Armor vs 7+`, see [[Damage]]).

| Class | Damage | Examples |
|---|:---:|---|
| Unarmed | +0 | fists |
| Light | +1 | knife, bat, pipe |
| Medium | +2 | pistol, heavy tool, sledgehammer |
| Heavy | +3 | rifle, shotgun (close) |

## Armor
Armor reduces the **Injury roll only** — never the hit.

| Armor | Injury | Drawback |
|---|:---:|---|
| None | 0 | — |
| Thick clothing | 0 | ignore the first Environmental Stress once per game |
| Light | −1 | — |
| Improvised | −1 | −1 AGI |
| Heavy | −2 | −1 MOV, −1 AGI, counts as **Loud** |

## Hacking gear
Hacking mirrors combat: **Program** is its Damage (adds to the **Breach roll**), **Firewall** is its Armor (subtracts from an incoming breach). Both come from gear or skills — see [[Hacking]].

| Program (breach) | +DMG | Notes |
|---|:---:|---|
| Bare-handed | +0 | improvising at a terminal |
| Breach Kit | +1 | standard hacker loadout |
| Exploit Suite | +2 | specialist kit |

| Firewall (defence) | Armor | Notes |
|---|:---:|---|
| Open system | 0 | civilian terminal |
| Firewall Node | −1 | hardened terminal / basic ICE |
| Military ICE | −2 | settlement / military security |

*(Values TBD in playtest — set the ladder once breach reliability is confirmed.)*

## Trait glossary
- **Sidearm** — may fire while Engaged, using DEX, against the Engaged enemy only.
- **Accurate** — +1 to hit if the unit didn't Move / Sprint / Climb and isn't Shaken this activation.
- **Quiet / Loud** — noise level (feeds Heat and detection).
- **Concealable** — may start Hidden / be smuggled.
- **Two-Handed** — occupies both hands.
- **Knockback** — the target is pushed on a wound.
- **Breach** — auto-succeeds against Breachable terrain.
- **Brutal** — +1 on the Injury roll. *(rare)*
- **Spread · Blast · Fire · Unstable · Slow · Awkward · Limited · Ammo Check · Illegal** — *area, hazard, and reliability traits — values TBD in playtest.*

## Example profiles
- **Fists** — Melee · +0 · *Quiet, Always Available*
- **Knife** — Melee · +1 · *Quiet, Concealable, STR or AGI*
- **Bat / Pipe** — Melee · +1 · *Knockback*
- **Sledgehammer** — Melee · +2 · *Breach, Slow, Two-Handed*
- **Pistol** — 8" · +2 · *Sidearm, Loud, Concealable*
- **Shotgun** — 10" · +3 close / +1 long · *Brutal, Loud, Spread, Two-Handed*
- **Rifle** — 18" · +3 · *Accurate, Loud, Awkward, Two-Handed*
- **Molotov** — 6" · +1 · *Fire, Blast, Loud, Unstable*

---
See [[Rules System MOC]] · governed by [[Damage]] · [[Shooting]] · [[Melee]].

---
type: reference
title: Weapons
tags: [settlements/reference]
---
# 🔫 Weapons — Construction System

Weapons are **built, not bought off a shelf.** Pick a **Class**, then spend points on **Characteristics**. Name the result after your miniature.

> [!info] Design contract — the three rules that keep this honest
> 1. **Stats decide if you land it · Weapons decide how bad it is · Skills decide what else happens.** A weapon **never** grants an effect a **[[Skill Paths|skill]]** grants. Weapons do damage, range, armour, conditions, noise and concealment. Skills do extra actions, reactions, exceptions and positioning.
> 2. **Weapons apply conditions — they never define them.** Every condition below is written in **[[Conditions]]**.
> 3. **A hit does exactly one thing: it wounds, or it delivers its payload.** Never both ([[Damage]]).

```
Fire Axe         Heavy Melee · Brutal · Bleeding                             16 pts
Pipe Shotgun     Standard Ranged · Brutal · Spread · Short Range · Unstable  12 pts
Grandpa's Rifle  Standard Ranged · Accurate · Long Range                     19 pts
```

---
## 1 · Weapon classes

| Class | Cost | Damage | Range | Hands | Min. rank | Slots | Always has |
|---|:--:|:--:|:--:|:--:|---|:--:|---|
| **Unarmed** | 0 | +0 | melee | — | Any | 0 | — |
| **Light Melee** | 0 | +1 | melee | 1 | Recruit | 2 | *(the free basic loadout)* |
| **One-Handed Melee** | 4 | +2 | melee | 1 | Fighter | 2 | — |
| **Heavy Melee** | 8 | +3 | melee | 2 | Specialist | 3 | Two-Handed |
| **Thrown** | 2 | +1 | 6" | 1 | Any | 2 | **Limited** (one use) |
| **Sidearm** | 4 | +2 | 8" | 1 | Recruit | 2 | **Sidearm** (may fire while Engaged), Loud |
| **Standard Ranged** | 10 | +3 | 18" | 2 | Fighter | 3 | Two-Handed, Loud |
| **Heavy Ranged** | **16** | +3 | 24" | 2 | Specialist | 4 | Two-Handed, Loud |

Damage feeds the **Injury roll** — `1d10 + Damage − Armor` vs **7+** ([[Damage]]).

> [!warning] Two hard ceilings. Both are load-bearing.
> **Damage stops at +4, and only Brutal reaches it.** Armour only runs to −2; if weapons ran past +4 the armour ladder would be decorative. Base classes stop at **+3**. On a ranged weapon, Brutal is gated behind **Short Range** — which encodes the finding from [[Terrain Hacking Cover — Sim Findings]]: *keep Brutal off any longer-ranged weapon.*
>
> **Range stops at 24".** Deployment zones sit **24" apart** ([[Core Game Format]]), so a weapon that reaches 24" can fire from its own deployment zone on turn one. That is a **threshold**, not a linear advantage, and no points cost can balance a threshold — the sim found an uncapped long-range crew beating every other list by 13–30 points. Only **Heavy Ranged** (Specialist rank, Cumbersome) reaches 24" cleanly.

### Rank gates the class
The hard lock that makes the ladder in [[List Building]] real — **a Recruit cannot hold a rifle.**

| Rank | May carry |
|---|---|
| **Recruit** | Unarmed · Light Melee · Sidearm · Thrown |
| **Fighter** | + One-Handed Melee · Standard Ranged |
| **Specialist** | + Heavy Melee · Heavy Ranged |
| **Leader** | everything |

---
## 2 · Characteristics
Each takes **one slot**. Restrictions in *italics*.

### Damage & armour
| Characteristic | Cost | Effect |
|---|:--:|---|
| **Brutal** | 4 | **+1 Damage**, to a maximum of **+4**. *Melee only — or a ranged weapon that also takes **Short Range**.* |
| **Armour Piercing** | 4 | Reduce the target's **Armor by 1** on the Injury roll. |

### To hit
| Characteristic | Cost | Effect |
|---|:--:|---|
| **Accurate** | 3 | **+1 to hit** if you did not Move, Sprint or Climb this activation. |
| **Spread** | 3 | **+1 to hit** at half range or less; **−1** beyond it. *Ranged only.* |

### Payload — *replaces* the non-wounding result
> A payload lands **in place of Pinned** (ranged) **or Shaken** (melee) when a hit fails to wound. Its **+1 Stress** applies once, exactly as Pinned's would ([[Conditions#General rules]]) — never both.
>
> This is what makes conditions work in a **WND-1** game. Wounding is binary and terminal, so there is no headroom to "add damage" — a weapon's extra bite has to land on the *hit that didn't kill you*.

| Characteristic | Cost | Payload |
|---|:--:|---|
| **Concussive** | 3 | **Off-Balance** |
| **Crippling** | 3 | **Hobbled** |
| **Blinding** | 3 | **Blind** |
| **Shocking** | 3 | **Shocked** |
| **Toxic** | 3 | **Poison** |
| **Incendiary** | 3 | **Fire** |
| **Bleeding** | 4 | **Bleed** — *at WND 1 this is a two-round death clock unless treated. The deadliest payload; priced for it.* |
| **Heavy Impact** | 3 | Push the target **2"** directly away. Falls and hazards resolve normally ([[Terrain]]). |
| **Hook** | 2 | Pull the target **1"** toward you. *Melee only.* |
| **Suppressive** | 4 | The target **may not clear the Pin with its Move** — it must spend its **entire activation**. *Ranged only.* |

### Area
| Characteristic | Cost | Effect |
|---|:--:|---|
| **Blast** | 4 | Resolve the attack separately against **every model within 2"** of the target. *Thrown / Heavy Ranged only.* |
| **Smoke** | 3 | Instead of attacking, place a **3" Dense Smoke** area ([[Terrain#Hazards (the Dangerous overlay)]]). *Thrown only.* |

### Handling
| Characteristic | Cost | Effect |
|---|:--:|---|
| **Long Range** | 6 | **+6"** maximum range, to the **24" ceiling**. *Ranged only.* |
| **Balanced** | 2 | May use **AGI** instead of STR for melee attacks with this weapon. *Light / One-Handed Melee only.* |
| **Defensive** | 3 | **+1** on opposed melee rolls when you are **not** the attacker and did **not Move** this activation. *Melee only.* |
| **Cleaving** | 5 | When you **win** a melee clash, make the Injury roll against **every** enemy Engaged with you. *Heavy Melee only.* |
| **Breaching** | 3 | **+2** on STR tests to Force or break **Breachable** terrain ([[Terrain Interaction]]). |
| **Concealable** | 2 | May start **Hidden**, or be smuggled past a search. |
| **Quiet** | 2 | Attacks don't reveal you from **Hidden** and don't trip noise or alarms. |
| **Compact** | 2 | Counts as **one-handed** despite its class. *Heavy classes only.* |

### Drawbacks — refund points, take **no** slot (max 2 per weapon)
The DIY layer. This is how you build a pipe shotgun that might blow up in your hand.

| Drawback | Refund | Effect |
|---|:--:|---|
| **Short Range** | −3 | **Halve** the weapon's maximum range. *Ranged only.* |
| **Slow** | −3 | You may not **Charge** with this weapon. *Melee only.* |
| **Unstable** | −2 | On a **natural 1** to hit, the weapon is **destroyed**. |
| **Cumbersome** | −2 | **−1 MOV** while carried. |
| **Limited** | −3 | **One use** per battle. |

> [!danger] The rule that governs this list: **a drawback must bite no matter how you play**
> The sim caught the same bug twice, and it is the one to guard against:
> - **Slow on a rifle is free points** — a rifleman never Charges anyway. *(Hence: melee only.)*
> - **Awkward** *(may not Move and attack)* **is free points on a sniper** — he never moves anyway, and it *synergises* with **Accurate**, which pays you for standing still. **Awkward is cut.**
>
> A drawback you can dodge by how you play is just a discount. If a proposed drawback can be sidestepped by a legitimate playstyle, it does not belong on this table.

---
## 3 · Armor
Armor reduces the **Injury roll only** — never the hit. Cover protects against *being hit*; armor protects against *being hurt* ([[Rules Engine]]).

> [!info] Armour carries no drawbacks *(2026-07-30)*
> A drawback you **opt into** for a discount is a deal — that is the DIY weapon layer below, and it stays. A drawback **welded onto something you want** is a tax, and armour had two of them. They are gone.
>
> The ladder is now linear in what armour actually does: the Injury roll is `1d10 + Damage − Armor` vs **7+**, so each point of armour is a flat **−10%** on being hurt. **−2 is worth exactly twice −1, so Heavy costs exactly twice Light.**
>
> **Improvised armour is cut.** With its penalty gone it was Light armour under another name. Whether a suit was **scavenged and welded together** or **bought from a trader** is a settlement-economy distinction — it does not need a second row on this table.

| Armor | Injury | Drawback | Cost |
|---|:---:|---|:--:|
| None | 0 | — | **0** |
| Thick clothing | 0 | ignore the first Environmental Stress once per game | **0** |
| Light | −1 | — | **3** |
| Heavy | −2 | — | **6** |

---
## 4 · Hacking gear
A hack is one INT test ([[Hacking]]). Gear grants a flat **+/− modifier to hacking rolls** — the v1 hack test today, and mostly the **breach roll** if the parked deeper system is ever built ([[Hacking]]).

| Hack gear | Modifier | Cost | Notes |
|---|:---:|:--:|---|
| Bare-handed | +0 | 0 | improvising at a terminal |
| Breach Kit | +1 | 4 | standard hacker loadout |
| Exploit Suite | +2 | 8 | specialist kit |

Defence is the same in reverse: a defender's gear/skill or a scenario may impose a **penalty** on enemy hacks against a device. There is no separate hardening stat — toughness is just a modifier like any other.

---
## 5 · Sample armoury
Every one of these is a legal build. Copy or rename freely.

| Name | Build | Profile | Cost |
|---|---|---|:--:|
| **Baseball Bat** | Light Melee | +1 melee | **0** |
| **Kitchen Knife** | Light Melee · Balanced · Concealable | +1, AGI, hidden | **4** |
| **Crowbar** | One-Handed Melee · Breaching | +2, breaches | **7** |
| **Great Axe** | Heavy Melee | +3 melee | **8** |
| **Sledgehammer** | Heavy Melee · Heavy Impact · Breaching | +3, push 2" | **14** |
| **Fire Axe** | Heavy Melee · Brutal · Bleeding | **+4**, Bleed | **16** |
| **Reaping Hook** | Heavy Melee · Cleaving · Defensive | +3, hits everyone Engaged | **16** |
| **Pistol** | Sidearm | 8", +2, fires while Engaged | **4** |
| **Pipe Shotgun** | Standard Ranged · Brutal · Spread · *Short Range* · *Unstable* | 9", **+4**, Spread | **12** |
| **Assault Rifle** | Standard Ranged · Accurate | 18", +3 | **13** |
| **Nailgun** | Standard Ranged · Bleeding | 18", +3, **Bleed** | **14** |
| **Grandpa's Hunting Rifle** | Standard Ranged · Accurate · Long Range | **24"**, +3 | **19** |
| **Squad Machine Gun** | Heavy Ranged · Suppressive · Armour Piercing | 24", +3, locks you down | **22** |
| **Makeshift Flamethrower** | Heavy Ranged · Incendiary · Blast · *Short Range* · *Limited* | 12", +3, **Fire**, Blast | **15** |
| **Molotov** | Thrown · Incendiary · Blast | 6", +1, **Fire**, Blast, one use | **9** |
| **Smoke Grenade** | Thrown · Smoke | 6", places 3" smoke | **5** |

---
## 6 · Cut, and why
Kept so it doesn't creep back in a new costume ([[Out of Scope — What Settlements is NOT#4 · Rejected-ideas log]]).

| Proposed | Why it's out |
|---|---|
| **Rapid** *(extra attack at −2)* | It **is** **Quick Shot** — a **Tier 3** skill needing a stat of +6, i.e. campaign-earned. [[Skill Sim — Findings]] measured multi-attack as *the biggest DPS lever in the game* (+67% output). Selling it to a Fighter for 4 points destroys the entire skill economy. |
| **Precision** *(flat +1 hit)* | Strictly stronger than **Dead Eye** (T3, which is conditional). Replaced by **Accurate** — conditional, and already a locked trait. |
| **Reliable** *(re-roll)* | Introduces **re-rolls**, a dice mechanic that exists nowhere in Settlements. Breaks the one-mechanic ceiling. |
| **Quick Draw** *(fire after Sprinting)* | Sprint consumes **both slots** — there is no Action left to fire with. It silently invents a new action economy. |
| **Crushing** *(ignore cover on the Wound Roll)* | **Cover never touches the Injury roll.** That is the load-bearing line of the entire engine. (Shields also don't exist.) |
| **Awkward** *(no Move + attack)* | Free points on a static shooter, and it *synergises* with Accurate. A drawback must bite regardless of playstyle. |
| **Intimidating** *(Stress aura)* | A free, always-on Stress aura is far too volatile given the Stress-cascade findings in [[Crew Sim — Findings]]. **Parked**, not rejected. |
| **Area Effect** | Merged into **Blast**. |

---
## 7 · Conflicts flagged in [[Skill Paths]]
Three skills are now out-competed by a characteristic. Flagged, not changed.

- **Long Barrel** (T1 DEX) — *"+5" rifle range if you don't Move."* **Long Range** gives +6" unconditionally for 6 points, and the 24" ceiling makes the skill's extra reach unusable anyway. The skill is dead and wants a rewrite.
- **Knockback** (T1 STR) vs **Heavy Impact** — different triggers (the skill fires on a melee *win* and allows a follow-up; the characteristic fires on a *non-wounding* hit). Distinct enough to keep both — but watch them.
- **Ghost Blade** (T3 AGI) vs **Balanced** — the skill covers *all* melee including Heavy (+3); the characteristic caps at One-Handed (+2). Distinct, but the margin is thin.

---
See [[Rules System MOC]] · governed by [[Damage]] · [[Shooting]] · [[Melee]] · costed in [[List Building]] · conditions in [[Conditions]].

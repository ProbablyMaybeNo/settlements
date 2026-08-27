---
type: reference
title: Weapons
tags: [settlements/reference]
---
# 🔫 Weapons — Construction System

Weapons are **built, not bought off a shelf.** Pick a **Class**, then spend Credits on **Characteristics**. Name the result after your miniature.

> [!success] Prices reconciled 2026-08-27 — this note, the master and the engine now agree
> Every number below is the **850-Credit shipping catalogue**, generated from `test-bench/points/ticks.py`. The old ×10 conversion warning is retired, and so are the three disagreements it tracked: **armour is 10 / 20** (measured with zero prior, `armour-level-n2500`), **Thrown is 5**, **Heavy Ranged is 25**. Regenerate with `py -3.13 -m points` from `test-bench/`.
>
> Confidence tiers travel with the numbers — see `docs/POINTS-CATALOGUE.md`. **[A]** measured and current · **[B]** measured, wide CI or single-scenario · **[C]** derived by rule from a measured atom, never measured directly. **No number here is untagged**, and a C-tier price is fine — it is simply the first thing table data corrects.

> [!info] Design contract — the three rules that keep this honest
> 1. **Stats decide if you land it · Weapons decide how bad it is · Skills decide what else happens.** A weapon **never** grants an effect a **[[Skill Paths|skill]]** grants. Weapons do damage, range, armour, conditions, noise and concealment. Skills do extra actions, reactions, exceptions and positioning.
> 2. **Weapons apply conditions — they never define them.** Every condition below is written in **[[Conditions]]**.
> 3. **A hit does exactly one thing: it wounds, or it delivers its payload.** Never both ([[Damage]]).

```
Fire Axe         Heavy Melee · Brutal · Bleeding                             50 Cr
Pipe Shotgun     Standard Ranged · Brutal · Spread · Short Range · Unstable  35 Cr
Grandpa's Rifle  Standard Ranged · Accurate · Long Range                     40 Cr
```

---
## 1 · Weapon classes

| Class | Cheapest build | Damage | Range | Hands | Min. rank | Slots | Always has |
|---|:--:|:--:|:--:|:--:|---|:--:|---|
| **Unarmed** | **0** | +0 | — | — | Any | 0 | — |
| **Light Melee** | **0** | **+1 only** | melee | 1 | Recruit | 2 | *(the free floor weapon)* |
| **One-Handed Melee** | **0** | **+1 to +3** | melee | 1 | Recruit | 2 | spans a shiv to a Magnum |
| **Heavy Melee** | **10** | **+2 to +4** | melee | 2 | Specialist | 3 | Two-Handed |
| **Thrown** | **5** | **+1 to +2** | 8" flat | 1 | Any | 2 | may also be used in **melee** |
| **Sidearm** | **5** | **+1 to +3** | **6"–12"** | 1 | Recruit | 2 | **Sidearm** (may fire while Engaged), Loud |
| **Standard Ranged** | **15** | **+2 to +4** | **12"–36"** | 2 | Fighter | 3 | Two-Handed, Loud |
| **Heavy Ranged** | **25** | **+3 to +5** | **12"–36"** | 2 | Specialist | 4 | Two-Handed, Loud |

*"Cheapest build" is the class at its **floor** Damage and **floor** range with no characteristics. Every step up the band costs **+10 per Damage point**; range is priced separately (below).*

> ### The class is an ENVELOPE, not a value — reworked 2026-08-14
>
> **Each class used to have one fixed Damage and one fixed range**, which made
> weapon class a global damage tier: a .22 pistol and a Magnum could not both be
> One-Handed, and a snub-nose and a long-barrel could not both be Sidearms. It
> also crushed the damage axis — Standard Ranged, Heavy Melee and Heavy Ranged
> all sat at +3 against a +4 cap, so a basic rifle, a great axe and a machine gun
> shared a tier with one step of headroom.
>
> **Now the class sets the BANDS and the weapon picks inside them**, paying for
> what it picked:
>
> `cost = class base (slots) + Damage steps + range + characteristics`
>
> The bands **overlap deliberately**. Heavy Melee overlaps the top of One-Handed
> and reaches higher. Nothing shoulder-fired is a .22, so Standard Ranged floors
> at +2. Heavy Ranged is inherently powerful and floors at +3.
>
> **The Damage cap moves +4 → +5** to accommodate Heavy Ranged's ceiling.

^tbl-1-weapon-classes

Damage feeds the **Injury roll** — `1d10 + Damage − Armor` vs **7+** ([[Damage]]).

> [!info] Thrown weapons are not automatically one-use *(2026-07-31)*
> **One-use is a tag, not a class.** `Single-Use` is an ordinary drawback that a build may take for its refund — so a **molotov** takes it (you cannot un-throw a burning bottle) while a **javelin**, **hatchet** or **throwing knife** does not, and is simply thrown again next turn.
>
> To keep a reusable thrown weapon from being a worse Sidearm, the class carries two edges no other ranged class has: it is **not Loud**, and it **may also be used as a melee weapon** at its own Damage — a javelin is a spear. It also holds exclusive access to **Blast** and **Smoke**.
>
> On the 850 scale a **Molotov** (Thrown · Incendiary · Blast · *Single-Use*) is **10 Cr** and a **Smoke Grenade** (Thrown · Smoke · *Single-Use*) is **15 Cr** — the smoke costs more than the firebomb, because Smoke is a placed-area effect and Incendiary is a payload riding a hit that already happened.

> [!warning] Two hard ceilings. Both are load-bearing.
> **Damage stops at +4, and only Brutal reaches it.** Armour only runs to −2; if weapons ran past +4 the armour ladder would be decorative. Base classes stop at **+3**. On a ranged weapon, Brutal is gated behind **Short Range** — which encodes the finding from [[Terrain Hacking Cover — Sim Findings]]: *keep Brutal off any longer-ranged weapon.*
>
> **Range reaches 36", and everything past 24" is GATED.** Deployment zones sit **24" apart** ([[Core Game Format]]), so a 24" weapon fires from its own deployment zone on turn one, and a **36"** weapon fires from **12" behind** it — covering the whole board from a square the enemy needs a round of sprinting to threaten. That is a **threshold**, not a linear advantage, and no points cost can balance a threshold on its own: the sim found an uncapped long-range crew beating every other list by **13–30 points**, larger than any single atom in the catalogue.
>
> So the ceiling is no longer a hard 24". It is **24" for anything you can build**, and past that a weapon must clear **four gates**:
>
> | Gate | Rule |
> |---|---|
> | **Manufactured only** | Cannot be crafted at **any** Workshop tier. Loot and raid spoils only. |
> | **Limit 1 per crew** | The 13–30 point finding was a *list archetype*; this is the gate that destroys the archetype rather than taxing it. |
> | **Specialist or above** | The carrier is an expensive body in its own right. |
> | **Steep price** | The cost step across 24" accelerates sharply — 18"→24" is +6, 24"→30" is +12, 30"→36" is +15. |
>
> The intent: a 36" rifle is a **rare, expensive, found weapon that a crew builds a plan around** — never standard kit. All four gates are enforced in code, not merely written here.

### Rank gates the class
The hard lock that makes the ladder in [[List Building]] real — **a Recruit cannot hold a rifle.**

| Rank           | May carry                                |
| -------------- | ---------------------------------------- |
| **Recruit**    | Unarmed · Light Melee · Sidearm · Thrown |
| **Fighter**    | + One-Handed Melee · Standard Ranged     |
| **Specialist** | + Heavy Melee · Heavy Ranged             |
| **Leader**     | everything                               |

^tbl-rank-gates-the-class

---
## 2 · Characteristics
Each takes **one slot**. Restrictions in *italics*.

### Damage & armour
| Characteristic | Cr | Tier | Effect |
|---|:--:|:--:|---|
| **Brutal** | **10** | **A** | **+1 Damage**, to the class band's ceiling (max **+5**). *Melee only — or a ranged weapon that also takes **Short Range**.* |
| **Armour Piercing** | **5** | **B** | Reduce the target's **Armor by 1** on the Injury roll. *The closest agreement between a measured atom and its old shipped price anywhere in the rebuild.* |

^tbl-damage-armour

### To hit
| Characteristic | Cr | Tier | Effect |
|---|:--:|:--:|---|
| **Accurate** | **10** | **B** | **+1 to hit** if you did not Move, Sprint or Climb this activation. |
| **Spread** | **10** | **B** | **+1 to hit** at half range or less; **−1** beyond it. *Ranged only.* |

^tbl-to-hit

### Payload — *replaces* the non-wounding result
> A payload lands **in place of Pinned** (ranged) **or Shaken** (melee) when a hit fails to wound. Its **+1 Stress** applies once, exactly as Pinned's would ([[Conditions#General rules]]) — never both.
>
> This is what makes conditions work in a **WND-1** game. Wounding is binary and terminal, so there is no headroom to "add damage" — a weapon's extra bite has to land on the *hit that didn't kill you*.

**Every payload price is net of Pinned.** A payload lands *in place of* the ordinary non-wounding result, and on a ranged hit that result is **Pinned — measured at +0.510 and significant**. So a payload's price is what it is worth **minus what it displaces**.

| Characteristic | Cr | Tier | Payload |
|---|:--:|:--:|---|
| **Suppressive** | **20** | **B** | The target **may not clear the Pin with its Move** — it must spend its **entire activation**. *Ranged only. Now the dearest payload: the Pin costing a whole activation is worth far more than the old table thought.* |
| **Bleeding** | **20** | **B** | **Bleed** — *at WND 1 this is a two-round death clock unless treated.* |
| **Incendiary** | **10** | **B** | **Fire** |
| **Shocking** | **5** | **B** ⚠ | **Shocked** — *measures positive but inside the noise floor.* |
| **Heavy Impact** | **5** | **B** ⚠ | Push the target **2"** directly away. Falls and hazards resolve normally ([[Terrain]]). *Also inside the noise floor.* |

> [!danger] ⛔ Five payloads are BLOCKED — they do **not** ship
> **Concussive · Crippling · Blinding · Hook · Toxic.** All five measure at or below **zero net value**, three of them significantly. No price fixes this: repricing a trait whose whole effect is to replace a good default with a worse one sells the player a downgrade at any number.
>
> | Trait | Net | |
> |---|:--:|---|
> | **Crippling** | **−0.613** | significantly negative |
> | **Concussive** | **−0.592** | significantly negative |
> | **Blinding** | **−0.317** | significantly negative |
> | Hook | −0.230 | negative point estimate, unmeasurably noisy |
> | Toxic | −0.080 | negative point estimate, not significant |
>
> **The mechanism was counted, not inferred** (`condition-values-n3000`): value(Off-Balance) = **0.000 exactly — bit-identical games**; value(Hobbled) = +0.078 (n.s.); value(Blind) = **+0.369, significant and POSITIVE**. Blind is the tell — a genuinely valuable condition that still prices negative purely because what it replaces is worth more. Off-Balance and Hobbled fail differently: applied **89,498 times**, they land on models that have *already arrived and will not move again*.
>
> **This is a RULES question, not a pricing one.** Replace-not-stack was designed when Pinned was believed worth ~zero. That is plausibly **one miscalibrated rule, not five broken traits** — and it is open. Until it is ruled on, these five are not legal to buy.

^tbl-payload-replaces-the-non-wounding-result

### Area
| Characteristic | Cr | Tier | Effect |
|---|:--:|:--:|---|
| **Blast** | **15** | **B** | Resolve the attack separately against **every model within 2"** of the target. *Thrown / Heavy Ranged only.* |
| **Smoke** | **15** | **C** | Instead of attacking, place a **3" Dense Smoke** area ([[Terrain#Hazards (the Dangerous overlay)]]). *Thrown only. No LOS-denial atom has been measured; its nearest neighbour (Blind) is itself blocked.* |

^tbl-area

### Handling
| Characteristic | Cr | Tier | Effect |
|---|:--:|:--:|---|
| **Long Range** | **5**/step | **⚠ OVERRIDE** | Moves the weapon up one range band. Past **24"** the four gates above apply. *Ranged only.* |
| **Balanced** | **10** | **C** | May use **AGI** instead of STR for melee attacks with this weapon. *Light / One-Handed Melee only.* |
| **Defensive** | **15** | **C** | **+1** on opposed melee rolls when you are **not** the attacker and did **not Move** this activation. *Melee only. Derived from light armour, the nearest measured neighbour.* |
| **Cleaving** | **25** | **C** | When you **win** a melee clash, make the Injury roll against **every** enemy Engaged with you. *Heavy Melee only. Derived: Blast (multi-target) + one damage step.* |
| **Breaching** | **15** | **C** | **+2** on STR tests to Force or break **Breachable** terrain ([[Terrain Interaction]]). |
| **Quiet** | **10** | **C** | Attacks don't reveal you from **Hidden** and don't trip noise or alarms. *Engine-blocked — no noise or alarm system exists in the sim.* |
| **Compact** | **10** | **C** | Counts as **one-handed** despite its class. *Heavy classes only. Engine-blocked — hands and slots are inert in the sim.* |

> [!warning] ⚠ `Long Range` deliberately contradicts its own measurement
> **Measured:** the 8"–24" range curve is **flat** — the whole spread sits inside one standard error, which prices Long Range at **~0**. **Shipped:** a real price, accelerating steeply across 24".
>
> **Why:** the flat curve measures *a policy that does not exploit range*, not a rule that does not matter. Two opposite biases bracket it, and a free 24" is a **known degenerate** — the sim measured a **13–30 point edge** for a list that can fire from its own deployment zone on turn one. Shipping 0 here would be following a number off a cliff.
>
> **Retires when:** scenario coverage lands, or a range-exploiting policy makes the curve measurable honestly. Machine-readable at `ticks.OVERRIDES_MEASUREMENT`.

^tbl-handling

### Drawbacks — refund points, take **no** slot (max 2 per weapon)
The DIY layer. This is how you build a pipe shotgun that might blow up in your hand.

| Drawback | Refund | Effect |
|---|:--:|---|
| **Short Range** | **−5** *(−10 on Heavy Ranged)* | **Halve** the weapon's maximum range. *Ranged only. Heavy Ranged refunds double because halving takes it out of the 24" deployment band entirely.* |
| **Slow** | **−5** | You may not **Charge** with this weapon. *Melee only.* |
| **Unstable** | **−5** | On a **natural 1** to hit, the weapon is **destroyed**. |
| **Cumbersome** | **−5** | **−1 MOV** while carried. |
| **Single-Use** | **−5** | **One use** per battle — the weapon is expended when thrown or fired. |

^tbl-drawbacks-refund-points-take-no-slot-max-2-p

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

| Armor | Injury | Drawback | Cr | Tier |
|---|:---:|---|:--:|:--:|
| None | 0 | — | **0** | — |
| Thick clothing | 0 | ignore the first Environmental Stress once per game | **0** | — |
| Light | −1 | — | **10** | **B** |
| Heavy | −2 | — | **20** | **B** |

> [!info] **Heavy is NOT twice Light, and that question is closed**
> The old rule argued each armour point is a flat −10% on the injury roll, so −2 must cost 2× −1. That is the **wrong quantity**: linear in injury *probability* does not imply linear in *win-points*, because the second point buys survival on a model that is already surviving more often. **Measured ratio: 1.745 ± 0.416.**
>
> Measured with **zero prior** (`armour-level-n2500`) — the old 30/60 pair was tagged `[measured]` citing `balance/armourprice.py`, **a file that has never existed in any commit on any branch.** Corroborated by rebuild-to-pay: **Light armour ≈ exactly one rifle→pistol downgrade** (+0.140 ± 0.200, parity), with Heavy bracketed on both sides.
>
> Two known biases, opposite directions: armour's own historical drawbacks price at **zero** here, so these overstate it slightly; and light armour's value **moves with terrain density** (0.140 at 11 features, 0.508 at 9), so the level is board-dependent.

^tbl-3-armor

---
## 4 · Hacking gear
A hack is one INT test ([[Hacking]]). Gear grants a flat **+/− modifier to hacking rolls** — the v1 hack test today, and mostly the **breach roll** if the parked deeper system is ever built ([[Hacking]]).

| Hack gear | Modifier | Cr | Tier | Notes |
|---|:---:|:--:|:--:|---|
| Bare-handed | +0 | **0** | — | improvising at a terminal |
| Breach Kit | +1 | **20** | **C** | standard hacker loadout |
| Exploit Suite | +2 | **40** | **C** | specialist kit |

*Both are **C-tier and flagged**: they sell +1 / +2 on the Interact test, which prices high against the measured to-hit atom, and INT is worth nothing in a scenario with no claim step. Retained pending a measured INT ladder.*

^tbl-4-hacking-gear

Defence is the same in reverse: a defender's gear/skill or a scenario may impose a **penalty** on enemy hacks against a device. There is no separate hardening stat — toughness is just a modifier like any other.

---
## 5 · Sample armoury
Every one of these is a legal build. Copy or rename freely.

*Generated from the costing engine — `py -3.13 -m points` from `test-bench/`.*

| Name | Build | Profile | Cr |
|---|---|---|:--:|
| **Baseball Bat** | Light Melee | +1 melee | **0** |
| **Kitchen Knife** | Light Melee · Balanced | +1, AGI | **10** |
| **Machete** | One-Handed Melee | +2 melee | **10** |
| **Crowbar** | One-Handed Melee · Breaching | +2, breaches | **25** |
| **Magnum** | Sidearm · Brutal · *Short Range* | 4", +3, fires while Engaged | **30** |
| **Great Axe** | Heavy Melee | +3 melee | **20** |
| **Sledgehammer** | Heavy Melee · Heavy Impact · Breaching | +3, push 2" | **50** |
| **Fire Axe** | Heavy Melee · Brutal · Bleeding | **+4**, Bleed | **50** |
| **Reaping Hook** | Heavy Melee · Cleaving · Defensive | +3, hits everyone Engaged | **50** |
| **Pistol** | Sidearm | 8", +2, fires while Engaged | **15** |
| **Snub Revolver** | Sidearm | 6", +2, fires while Engaged | **15** |
| **Pipe Shotgun** | Standard Ranged · Brutal · Spread · *Short Range* · *Unstable* | 9", **+4**, Spread | **35** |
| **Assault Rifle** | Standard Ranged · Accurate | 18", +3 | **35** |
| **Nailgun** | Standard Ranged · Bleeding | 18", +3, **Bleed** | **35** |
| **Grandpa's Hunting Rifle** | Standard Ranged · Accurate · Long Range | **24"**, +3 | **40** |
| **Squad Machine Gun** | Heavy Ranged · Suppressive · Armour Piercing | 24", +3, locks you down | **55** |
| **Makeshift Flamethrower** | Standard Ranged · Incendiary · Blast · *Short Range* · *Single-Use* | 9", +3, **Fire**, Blast | **20** |
| **Molotov** | Thrown · Incendiary · Blast · *Single-Use* | 8", +1, **Fire**, Blast, one use | **10** |
| **Javelin** | Thrown | 8", +1, throw it or stab with it, **reusable** | **5** |
| **Smoke Grenade** | Thrown · Smoke · *Single-Use* | 8", places 3" smoke | **15** |
| **Ranger's Long Rifle** | Heavy Ranged · 36" *(manufactured, limit 1, Specialist+)* | **36"**, +3 | **55** |

*Nineteen of twenty moved when the rebuild landed. The armoury total fell **1950 → 575** — **a rifle now costs 35 against a 100-Credit Fighter**, where it used to cost 100 against a 95-Credit one. That single line is what the rebuild was commissioned to fix.*

^tbl-5-sample-armoury

---
## 6 · Cut, and why
Kept so it doesn't creep back in a new costume ([[Out of Scope — What Settlements is NOT#4 · Rejected-ideas log]]).

| Proposed | Why it's out |
|---|---|
| **Rapid** *(extra attack at −2)* | It **is** **Quick Shot** — a **Tier 3** skill needing a stat of +6, i.e. campaign-earned. [[Skill Sim — Findings]] measured multi-attack as *the biggest DPS lever in the game* (+67% output). Selling it to a Fighter for 4 points destroys the entire skill economy. |
| **Precision** *(flat +1 hit)* | Strictly stronger than **Dead Eye** (T3, which is conditional). Replaced by **Accurate** — conditional, and already a locked trait. |
| **Reliable** *(re-roll)* | Introduces **re-rolls**, a dice mechanic that exists nowhere in Settlements. Breaks the one-mechanic ceiling. |
| **Concealable** *(may start Hidden / smuggle past a search)* | **Cut 2026-08-14.** Both halves are edge cases that do nothing in a typical battle, and it **breaks the weapon design contract stated in §1**: weapons do damage / range / armour / conditions / noise, and **skills** do positioning exceptions. "May start Hidden" is skill territory — [[Skill Paths]]' **Vanishing Point** and **Camouflage Drill** already do it properly. **Quiet is NOT cut**: no-reveal / no-alarm-trip is a real mechanical axis that interacts with Hidden and the Sensor deployables. *(Propagated to [[Full Rules System v1]] §15 on 2026-08-27 — the master still listed it as live.)* |
| **Quick Draw** *(fire after Sprinting)* | Sprint consumes **both slots** — there is no Action left to fire with. It silently invents a new action economy. |
| **Crushing** *(ignore cover on the Wound Roll)* | **Cover never touches the Injury roll.** That is the load-bearing line of the entire engine. (Shields also don't exist.) |
| **Awkward** *(no Move + attack)* | Free points on a static shooter, and it *synergises* with Accurate. A drawback must bite regardless of playstyle. |
| **Intimidating** *(Stress aura)* | A free, always-on Stress aura is far too volatile given the Stress-cascade findings in [[Crew Sim — Findings]]. **Parked**, not rejected. |
| **Area Effect** | Merged into **Blast**. |

^tbl-6-cut-and-why

---
## 7 · Conflicts flagged in [[Skill Paths]]
Three skills are now out-competed by a characteristic. Flagged, not changed.

- **Long Barrel** (T1 DEX) — *"+5" rifle range if you don't Move."* **Long Range** gives +6" unconditionally for 6 points, and the 24" ceiling makes the skill's extra reach unusable anyway. The skill is dead and wants a rewrite.
- **Knockback** (T1 STR) vs **Heavy Impact** — different triggers (the skill fires on a melee *win* and allows a follow-up; the characteristic fires on a *non-wounding* hit). Distinct enough to keep both — but watch them.
- **Ghost Blade** (T3 AGI) vs **Balanced** — the skill covers *all* melee including Heavy (+3); the characteristic caps at One-Handed (+2). Distinct, but the margin is thin.

---
See [[Rules System MOC]] · governed by [[Damage]] · [[Shooting]] · [[Melee]] · costed in [[List Building]] · conditions in [[Conditions]].

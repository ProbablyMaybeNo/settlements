---
type: reference
title: Terrain · Hacking · Cover — Test Plan
tags: [settlements/reference, settlements/analysis]
---
# 🧪 Terrain · Hacking · Cover — Test Plan

Review + test list for the new S3 Battle Layer rules ([[Terrain]], [[Terrain Interaction]], [[Hacking]], [[Movement]], cover, hazards, verticality). Covers what's **already broken** (P0 — fix these first), what to **sim** (P1 — dice-testable now), and what needs a **ruling/playtest** (P2 — logic, not probability).

> [!warning] Hacking sections superseded by v1
> The **hacker-vs-hacker shut-out** tests below (T6, T11, and related) target the pre-v1 breach system, now **parked** — v1 hacking is a single INT test + **Interrupt/Overload** ([[Hacking]]). The cover / terrain / fall / disengage tests still apply.

---
## P0 · Consistency bugs found in review — fix before testing
These are live contradictions between notes; a player would get two different answers.

- [ ] **1. Search / Scavenge stat conflict.** [[Terrain#Interact]] table says **Scavenge → DEX**; but [[Unit Design]] ("searching" under INT) and [[Terrain Interaction#Searching and looting]] ("Search, INT, 7+") say **INT**. → **Fix Terrain.md to INT.**
- [ ] **2. Repair stat conflict.** [[Terrain#Interact]] table says **repair → DEX**; [[Unit Design]] ("repairing" under INT) and [[Terrain Interaction#Feature damage]] ("Repair, INT, 7+") say **INT**. → **Fix Terrain.md to INT.**
- [ ] **3. "Accurate if Braced" (Rifle) vs the Accurate trait.** [[Weapons]] rifle profile says *Accurate if Braced*, but the **Accurate** trait is defined as *+1 if you didn't Move/Sprint/Climb and aren't Shaken*. **Braced** is a *morale condition* (from **Dig In**, [[Conditions]]). Two different triggers wearing one word. → Pick one: rename the rifle clause to the Accurate condition, **or** make "Braced-the-firing-stance" a distinct stationary state (not the morale Braced).
- [ ] **4. "Down" means two things.** Unit **Down** (prone, bleeding out) vs feature **Down** (offline, [[Terrain Interaction#Feature damage]]). Same keyword, different rules. → Consider **"Offline"** for features to kill the ambiguity.
- [ ] **5. "Build/Deploy → INT" vs trap Place = DEX.** [[Terrain#Interact]] lists **Build/Deploy → INT**, but [[Terrain Interaction#Traps and deployable defences]] places traps with a **DEX** Interact. → Split: **Build** (structures) = INT, **Deploy trap** = DEX; say so explicitly.
- [ ] **6. "Environmental Stress" is undefined.** [[Weapons]] "Thick clothing" ignores *the first Environmental Stress once per game*, but no note defines that category. → Define it (Stress from hazards/weather) in [[Morale]] or [[Conditions]], or reword.

---
## P1 · Dice / sim tests — runnable now (bench + `skills_sim.py`-style script)
Each: **setup → measure → pass criteria.** 10k samples, seeded.

- [ ] **T1 · Cover ladder (revalidate with Hidden = −3).** Shooter DEX+2, med weapon, vs Open/Light/Heavy/Hidden. *Measure:* to-hit, wound/shot, shots-to-Down. *Pass:* clean −10%/step; Hidden ≈ 30% hit (already matches [[Dice Mechanic — Sim Findings]] §3 — confirm no drift).
- [ ] **T2 · ⭐ Cover × the ±3 cap — the decision test.** Does **cover count toward the same ±3 modifier cap as conditions**, or is it a separate axis? *Run:* Shaken shooter (−1) into Heavy (−2) and into Hidden (−3), under (a) one shared cap vs (b) cover-separate-from-conditions. *Measure:* the to-hit divergence. *Why it matters:* under a shared cap, **Shaken does nothing when shooting into Heavy/Hidden** (already at −3) — stacked penalties go free. **Ross must rule this**; the sim just quantifies the gap.
- [ ] **T3 · Fall damage vs WND 1 / WND 2.** Falls of 2"/4"/6" → Injury `1d10 + (1 per 2") − 0, ignore Armor`, lands Pinned. *Measure:* P(Down) per height. *Pass:* a 2" drop isn't a ~coin-flip kill on a WND-1 fighter (Terrain flags this dial explicitly).
- [ ] **T4 · Height advantage value.** Shooter 2"+ above (ignores Light cover) vs a ground shooter, target in **Light** cover. *Measure:* to-hit + shots-to-Down uplift. *Pass / flag:* if the elevated shooter's shots-to-Down drops hard, "roof camping" is real — feeds the Terrain dial.
- [ ] **T5 · Hacking success curve.** `1d10 + INT + range ≥ 7`, INT 0–6 × Close(0)/Short(−1)/Medium(−2)/Long(−3). *Measure:* success%. *Pass:* clean ladder; Long band unusable for low-INT (e.g. INT+2 @ Long = 30%), rewarding the specialist.
- [ ] **T6 · ⭐ Hacker-vs-hacker shut-out, full chain.** Opposed INT (ties→defender) → **Effect roll 7+** → **Shut-out table**. *Measure:* P(payload lands) for INT Δ −2…+2, and the outcome spread (Glitch/Shutdown/Destroyed/TakeOver/Overload). *Flag:* even-INT lands only ≈ win% × 50% — is the shut-out too weak to bother? And does **Take Over (8–9)** snowball (the note's own dial)?
- [ ] **T7 · Search EV.** Default find table (1 Hazard / 2–4 Nothing / 5–7 Resource / 8–9 Gear / 10 Jackpot). *Measure:* E[Resource], E[gear], P(hazard). *Pass:* worth an Action but the 10% self-Pin hazard is a real deterrent (not free loot).
- [ ] **T8 · Disengage cost.** Expected wounds from **free swings at −2** when leaving 1 vs 2 engagers, plus losing the whole activation. *Measure:* net swing damage taken. *Decision:* is Disengage a dead option (Movement flags this) — is the −2 swing alone enough without also costing both slots?
- [ ] **T9 · AGI traversal + armour drag.** Climb/Jump/Vault/Swim at 7+, AGI 0–6, then repeat with **Heavy armour −1 AGI**. *Measure:* pass%, fall-on-fail frequency. *Pass:* heavies are meaningfully worse across terrain — this is the mechanism that makes **terrain the balancer** for the Heavy Gunner ([[Dice Mechanic — Sim Findings]] §6).
- [ ] **T10 · Brutal / shotgun-close lethality.** Shotgun close = **+3 + Brutal(+1) = +4 injury**. vs Armor 0/−1/−2. *Measure:* wound/hit. *Flag:* +4 = 80% wound at Armor 0 — is Brutal-on-a-heavy-weapon too swingy? Check the stacking rule.
- [ ] **T11 · Overload injury frequency.** Shut-out roll 10 → `1d10 + 0 − Armor ≥ 7` on the defending hacker. *Measure:* how often the worst result actually injures (and whether it should be auto-Pinned/Down instead — the note's dial).

---
## P2 · Edge-case & interaction rulings — decide or playtest (not dice)
- [ ] **Hidden stacking.** Does earned **Hidden (−3)** *replace* passive cover or *add* to it? (The −3 cap hides the math, but state it: **Hidden replaces**, it's the best single state.)
- [ ] **Height vs Hidden.** Does 2"+ height strip a **Hidden** target? Height only negates *Light cover from pieces at target's level* — Hidden is earned concealment, so **no**. Confirm in text.
- [ ] **Take Over → turret fire = two attacks?** The shut-out spent the hack Action; Take Over then grants **one Linked function** which could be **turret fire ("counts as your attack")**. Does that let one activation both shut-out *and* fire a turret? Rule it.
- [ ] **Feature cover "Heavy unless attacker within 6" → Open."** A 6" gun-line trivially deletes terminals/turrets (WND1, then Down). Intended? Points/placement counter?
- [ ] **Low-leap edges.** Low leap with <2" Move left; two low leaps in one activation (−4"); low leap **on** Difficult ground (does the double-cost stack with the flat −2"?).
- [ ] **Turret weapon profile is missing.** [[Weapons]] has no turret entry — **T7-turret and any turret DPS test is blocked** until one exists. Add a profile.
- [ ] **Smoke double-effect.** Dense smoke = **Blind** (−2 your own sighted attacks) **+ Concealing** (can Hide). Confirm a unit can Hide inside but shoots out at −2.
- [ ] **Disengage double-cost dial** (both slots **and** −2 swings) — Movement's own open question.
- [ ] **Ladder cost dial** (free vs −2" Move) — Terrain's open question; pick one before it forks playtests.

---
## What I can run right now
**T1–T11 are all dice-testable** with a new `terrain_hacking_sim.py` (same harness as `skills_sim.py`). **T2 and T6 are the high-value ones** — the cover/cap ruling and the shut-out chain are where the new rules are most likely to be silently broken. P0 bugs 1–2 (Search/Repair stat) I can fix in a one-line edit right now.

See [[Terrain]] · [[Terrain Interaction]] · [[Hacking]] · [[Movement]] · [[Conditions]] · [[Dice Mechanic — Sim Findings]] · [[Skill Sim — Findings]].

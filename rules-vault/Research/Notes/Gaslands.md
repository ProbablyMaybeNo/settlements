---
type: research-note
title: Gaslands
game: Gaslands Refuelled
publisher: Osprey Games
designer: Mike Hutchinson
depth: official QRS v3
tags: [settlements/research]
---
# 🎲 Gaslands

> [!abstract] In one breath
> Post-apocalyptic car combat with **two currencies where the second one cannot be bought**. Everything costs **cans** (points) *and* **build slots**; slots are fixed by the chassis. Its biggest gun costs **one can** — because the whole price is in the drawbacks.

| | |
|---|---|
| **Designer · publisher** | Mike Hutchinson · Osprey |
| **Currencies** | **Cans** (points, ~50 per team) + **build slots** (fixed, unbuyable) |
| **Depth of read** | Official Osprey QRS v3 |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.6 |

---
## Points plus an unbuyable capacity

**Type:** List · **Take:** ⭐ steal

Everything costs cans **and** slots; slots come from the chassis and **cannot be purchased at any price** **[FACT]**:

| Chassis | Cans / Slots | | Weapon | Cans / Slots |
|---|---|---|---|---|
| Bike | 5 / 1 | | Machine Gun | 2 / 1 |
| Car | 12 / 2 | | Minigun | 5 / 1 |
| Truck | 15 / 3 | | Rockets | 5 / 2 |
| Bus | 30 / 3 | | 125mm Cannon | 6 / 3 |
| Tank | 40 / 4 | | **BFG** | **1 / 3** |
| War Rig | 40 / 5 | | Armour Plating (+2 Hull) | 4 / 1 |

Extra Crewmember 4 cans / **0 slots** (capped at 2× starting Crew) · Nitro Booster 6 / 0 · **Turret mounting = ×3 the weapon's cost** · **Crew-fired weapons cost 0 slots.**

**Why it works.** Slots **decouple "how strong" from "how much fits"**, and because they can't be bought, they cannot be points-optimised around. A rich player still only has four slots on a tank. Note the two pressure valves: a **zero-slot category** (crew, nitro) that lets you keep spending cans once slots run out, and a **multiplicative mount** (Turret ×3) that stays proportionate on a 2-can MG and a 6-can cannon alike.

**For Settlements.** Our [[Weapons]] classes already carry a **slot count** (Light Melee 2, etc.) — this is the same family, and Gaslands is the argument for leaning on it harder rather than relying on price alone. Same shape as [[Last Days Zombie Apocalypse#Empty Spaces is the real constraint]] and [[Kill Team#Slots instead of prices for the long tail]].

---
## Price the drawback, not the number

**Type:** Combat · **Take:** ⭐ steal

**The BFG is the biggest gun in the game and costs 1 can.** **[FACT]** Because it eats **3 slots**, has **Ammo 1**, and firing it **shoves you backwards, drops you to Gear 1, and adds 3 Hazard tokens**.

**Why it works.** **[INFERENCE]** The gun's raw output is enormous and its *expected contribution* is small, because the drawbacks tax the thing the game is actually about — momentum and control. **That is how you put a spectacular toy in a game without distorting the economy: don't discount the number, charge for the number and hand back the difference in consequences.**

**For Settlements.** This is the design pattern behind our own **Unstable**, **Cumbersome** and **Heavy Ranged** entries in [[Weapons]] — and it's the answer to the [[Ideas Inbox]] want for rare near-future tech that's *better* without being an auto-take. A microwave launcher can be devastating and still cost little, if firing it lights you up, locks you in place, or empties in one shot. **Price the drawback.**

---
## Publish the inverse

**Type:** Costing · **Take:** ⭐ steal

One exchange rate is derivable from two published facts **[INFERENCE from FACT]**: Armour Plating = **+2 Hull for 4 cans**, and the Prison Car errata reads *"Reduce the cost of this vehicle by 4 Cans… Reduce the hull value of this vehicle by 2."*

→ **1 Hull ≈ 2 cans, applied consistently in both directions.**

**Why it works.** **Stating a rate forwards *and* backwards makes it self-auditing.** Anyone can check it. It's the cheapest possible form of published derivation and it costs a designer nothing but discipline.

**And the permission it grants:** the rate does **not** govern chassis costs. **Chassis and add-ons sit on different price scales, and the game is fine.** You do not have to reconcile every price scale in your game to each other.

**For Settlements.** Directly relevant to `docs/GLOBAL-POINTS-SYSTEM.md` and `test-bench/points/`. Our locked atomic unit (**10 points per +1 on any single test**) should be published with its inverse — *removing* a +1 refunds 10 — and any refund rule should be checked against the anti-exploit note that **refunds must be smaller than purchases**, or negative traits become an arbitrage. Compare [[Bolt Action#The implicit unit of account]] and [[Song of Blades and Heroes#The Quality multiplier]] (negative-cost traits, done well).

**[NOT FOUND]** No formula anywhere — not on Hutchinson's studio site, not in his 160-episode *Rule of Carnage* design podcast, not in BGG designer threads. Balance came from an iterative community beta; he calls Refuelled *"a sort of 1.5 version… nothing's been fundamentally changed, it's just rebalanced and tweaked."*

---
## Source

- Primary: official Osprey Gaslands Refuelled QRS v3
- Long-form: `docs/POINTS-RESEARCH.md` §7.6
- Related: [[Wargaming Research Hub]] · [[Kill Team]] · [[Last Days Zombie Apocalypse]] · [[Weapons]]

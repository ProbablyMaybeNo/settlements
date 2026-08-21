---
type: research-note
title: Trench Crusade
game: Trench Crusade
publisher: Trench Crusade (open playtest)
designer: Tuomas Pirinen · Mike Franchina · James Sherriff
depth: primary — playtest PDFs + BattleScribe catalogue
tags: [settlements/research]
---
# 🎲 Trench Crusade

> [!abstract] In one breath
> A grimdark WW1-flavoured skirmish campaign game by **the lead designer of Mordheim**, built around a **Gold Ducat** warband economy with a **published fixed power-curve schedule**, a second currency (**Glory**) you can only earn by playing dramatically, and a `LIMIT: N` cap printed beside every price. The most transferable campaign architecture found anywhere.

| | |
|---|---|
| **Designers** | Tuomas Pirinen (Mordheim), Mike Franchina, James Sherriff |
| **Build currency** | **Gold Ducats** — campaign warband starts at **700** |
| **Second currency** | **Glory Points** — earned by named deeds, never purchasable |
| **Depth of read** | **Primary** — v1.6.3 PDFs + the community BattleScribe `.cat`, cross-checked and in agreement on every item |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.10 |

> [!warning] Version warning
> Trench Crusade is in **open playtest** and every page of v1.6.3 is stamped PLAYTEST RULES. Two revisions were read and **they disagree on several numbers**. Pirinen's own foreword: *"these are not the final rules… there are bound to be mistakes as well as plenty of rules that are going to change."* **Treat the structure as the finding and every individual number as provisional.**

---
## Why it's here

It is the closest thing to a modern, complete answer to the question Settlements is actually asking: *how do you run a persistent warband economy that doesn't snowball, doesn't punish the loser out of the campaign, and doesn't require the designer to defend a global formula?* Its answer is **more dials, each doing one job** — price, cap, force-value gate, headcount ceiling, and a separate uncapped glory axis — rather than one price trying to do everything.

---
## Two dials per item — price and LIMIT

**Type:** List · **Take:** ⭐ steal

Every catalogue entry carries a **price in ducats** *and* a **`LIMIT: N`** cap, side by side. Sample from the New Antioch armoury **[FACT — v1.6.3, agrees with the `.cat`]**:

| Ranged | Ducats | LIMIT |
|---|---:|---|
| Molotov Cocktail | 5 | — |
| Bolt Action Rifle · Shotgun | 10 | — |
| Sniper Rifle | 35 | 3 |
| Automatic Rifle | 40 | **1** |
| Machine Gun | 50 | 2 |
| Heavy Flamethrower | 55 | **1** |

**The errata prove they're independent dials.** The same patch adjusts prices and caps as separate levers **[FACT — V1.4 Change List]**: *"Viscera Cannon: Cost reduced to 50 ducats"* (price) · *"Grenade Launcher: New **LIMIT: 2**"* (cap) · *"Black Grail Musician's Instrument: Cost 15 ducats. **LIMIT: 1**"* (both, together).

**Why it works.** **Two orthogonal dials mean a designer can fix "too strong" without making it unaffordable, and fix "too common" without making it weak.** A single price has to do both jobs at once and does neither well.

**And the cap is on *purchasing*, not possession** **[FACT — two verbatim statements]**:

> *"**LIMIT (X):** You can only purchase as many of this piece of equipment… as indicated by the number in parenthesis **for your warband**. **If you find more via looting/exploration, you can break this limit.**"*

So it persists across the whole campaign, allies are exempt, and **loot can exceed it**. That is a genuinely clever middle path: it constrains list-building without forbidding the narrative moment where you take the enemy's machine gun off the field.

**For Settlements.** [[List Building]] currently gates by **rank**, which is a legitimate equivalent and needs no extra bookkeeping. The addition worth considering is a **printed cap column** on the [[Weapons]] catalogue for the handful of entries where rank alone isn't enough — and the loot exemption is a direct fit for the [[Ideas Inbox]] want of loot tables that can hand you gear you couldn't buy.

---
## Caps keyed to force value

**Type:** Economy · **Take:** ⚙️ adapt

> *"You may include 0-2 Artillery Witches in a warband worth more than 1000 ducats."* **[FACT]**

**A roster cap gated on total force value is a third dial beyond price and LIMIT.** It lets a capability exist at high budgets without distorting small games — the thing exists in the world, it just isn't available to a starting warband.

**For Settlements.** Directly relevant to the **Campaign Start 500** vs **Match Play 1000** split. Anything that breaks a 500-point game but is fine at 1000 can be gated this way instead of being priced out of reach or cut.

---
## The published threshold ladder

**Type:** Campaign · **Take:** ⭐ steal

The campaign power curve is a **published fixed schedule, not an emergent one** **[FACT]**:

| Battle | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Threshold (ducats)** | 700 | 800 | 900 | 1000 | 1100 | 1200 | 1300 | 1400 | 1500 | 1600 | 1700 | 1800 |
| **Max Field Strength** | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 22 |

⚠️ *An earlier revision accelerates instead — 1250 / 1400 / 1550 / 1750 / 1950 / 2200 over 11 battles. The revisions disagree; the shape is the finding.*

**The Max Field Strength track is the underrated half.** A separate published ceiling on **model count** rises alongside the budget, so **a player cannot convert a rising budget purely into bodies.** Budget and headcount are capped independently — a direct structural answer to the horde-vs-elite problem.

**Everyone's ceiling rises on the same schedule regardless of who is winning.** Resupply scales with battles fought, not with performance.

**For Settlements.** [[Campaign]] and [[Progression]]. A printed ladder is enormously better than "you keep what you earn" for a game that must stay playable between players with different play frequencies — which is exactly the failure mode measured in [[Necromunda and Mordheim#Play frequency beats skill]].

---
## The rubber band you choose

**Type:** Campaign · **Take:** ⭐ steal

To rebuild a mauled warband back up to the threshold you must **[FACT]**:

- *"Forego Exploration Phase completely"*
- *"Give up/Sell all Weapons, Armour and Equipment that is not assigned to any of your models"*
- *"Empty your Warband treasury of all ducats"*
- *"Do not keep any leftover ducats"*

**Catching up is always available and always costs you the upside phase.** That is a far better anti-snowball design than a win-rate-scaled handicap, **because the losing player chooses it.** No one is being handed charity, and no one is being punished for winning.

**For Settlements.** The cleanest available answer to the catch-up problem in [[Campaign]], and it composes with our [[Downtime]] three-phase turn — foregoing a phase is a cost we can already express.

---
## Cap the veterans, don't tax them

**Type:** Campaign · **Take:** ⭐ steal — **and this is a live fork for us**

**Trench Crusade never re-prices veterans.** The post-battle sequence defines warband value verbatim as *"the total cost in Ducats of **all your models and their weapons, armour and equipment**."* **Experience, Skill Advancements and ELITE promotion are not in that formula.** **[FACT — unambiguous]** A Lieutenant with 18 XP and six skills counts against the 700-ducat ceiling at exactly the 70 ducats he cost on day one.

Inflation is capped **structurally** instead **[FACT]**:

- A warband may have **a maximum of 6 ELITE models** (7 with Bad Company).
- ELITE models have **exactly two Battle Scar slots and die on the third**.
- Promotion is a dice pool — 1 die if you lost, 2 if you won, +1 per Glorious Deed, promote on a 6, **max one promotion per battle**.
- Some models carry **Limited Potential** (hard cap of 3 Skill Advancements) or *"cannot be promoted"* at all.

The consequences are deliberate: **advancement is free power**; two models at identical ducat cost are **not equal**, and the veteran is worth more for free — *which is the campaign-attachment mechanism.* Your veterans are precious **because** the ledger doesn't tax them. Injuries drain ducats without inflating value (*"deduct 10 ducats from your Paychest… This payment does not count towards your Warband's Threshold Value"*), and **Glory purchases dodge the ceiling entirely** because Threshold is measured in ducats.

**For Settlements — the fork.** Our current design is the opposite: *"each Advance a fighter carries adds +2 points to its cost"* — taxing veterans so they crowd out rookies, an anti-snowball valve. Compare [[The Walking Dead All Out War#Re-pricing veterans]], which taxes survival directly, and [[Last Days Zombie Apocalypse]], which never touches a veteran's cost. **Both shipped, neither is reported broken.**

> **The rule that matters: pick the valve — price *or* cap — and let the other axis run. What you must not do is half of each.** See [[Progression]].

---
## Glory

**Type:** Campaign · **Take:** ⭐ steal

A second currency that **cannot be bought** **[FACT]**:

> *"Glory Points… can be used to purchase powerful troops and famous warriors known as Allies… **They cannot be purchased with ducats** – the only way to attract their services is to perform glorious deeds on the battlefield!"*

Earned by named **Glorious Deeds** — Sniper, Sharpshooter, Lord of War, Blood Sacrifice, Suicidal Bravery, King of the Hill, Kill their Leaders, ~20 more — and **claimed first-come-first-served**: *"Victory Points for these can only be gained once – whichever player completes them first gets the Glory!"*

Glory buys effects with no ducat equivalent anywhere: armour that defeats armour-ignoring attacks (Damascus Armour, 5), a weapon that chains between targets (Locust Spitter, 6), one that removes a model from the game outright (Beelzebub's Embrace, 20).

**Why it works.** **Glory is a currency you earn by playing dramatically rather than efficiently**, and because deeds are claimed once per campaign it is **inherently self-limiting** — the second player to do a thing gets nothing. The designers give exactly one exchange data point (*"sell the book for either 150 ducats or 5 Glory Points"* → 1 Glory ≈ 30 ducats) and otherwise deliberately avoid a general conversion.

**For Settlements.** This is the mechanical shape the [[Ideas Inbox]] "glorious deeds" want has been reaching for — leaping between buildings, downing an enemy with terrain, reviving a downed friendly, winning a hack-off. **The first-come-first-served claim is the piece that makes it self-limiting**, and it's free to add. See [[Progression]] and [[Economy]].

---
## Faction rules that edit the economy

**Type:** Faction · **Take:** ⭐ steal

Knights of Avarice **[FACT]**: *"Your force may have no models that cost less than 80 ducats (including their equipment)"* — a **minimum model cost as faction identity**. Plus banned keywords (*"No weapon with the Keyword FIRE or SHRAPNEL"*), a cross-faction unlock (one weapon/armour/equipment type from two other lists), and a hard exclusion (*"may include no Death Commandos"*).

**Why it works.** Faction identity written as a constraint on **the price list** rather than on the stat line. A minimum model cost produces an elite, few-bodies force *automatically*, with no special rules to balance.

**For Settlements.** A third place to write [[Factions]] identity, alongside BLKOUT's one-playstyle-rule and Malifaux's hiring tax. This one costs nothing to balance because it only removes options.

---
## Melee is built, ranged is eyeballed

**Type:** Costing · **Take:** 📎 reference

Taking **Trench Club** (3 ducats, one-handed, no modifiers) as baseline and deriving increments from controlled pairs — CRITICAL **+1** (Sword/Axe 4), Ignore Shield **+1** (Shotel 5), anti-charge **≈+4** (Polearm 7) — then predicting two weapons *not* used to fit anything **[INFERENCE, working shown]**:

- **Great Sword/Axe** = Great Hammer 10 + CRITICAL 1 + "+1D Injury" 1 = **12**. Published: **12** ✔
- **Lochaber Axe** = Great Hammer 10 + CRITICAL 1 + anti-charge 4 = **15**. Published: **15** ✔

Two exact out-of-sample hits, with the anti-charge increment derived from a *different* weapon pair. **Melee costs are built, not eyeballed. Ranged costs do not reconstruct.**

**For Settlements.** Half a published formula is still evidence that atomic melee costing works in a game of this shape — relevant to `test-bench/points/` and [[Weapons]].

---
## Source

- Primary: Trench Crusade v1.6.3 playtest PDFs + community BattleScribe `.cat`, read directly
- Long-form: `docs/POINTS-RESEARCH.md` §7.10, §8.11
- Related: [[Wargaming Research Hub]] · [[Necromunda and Mordheim]] (same designer lineage) · [[Last Days Zombie Apocalypse]] · [[The Walking Dead All Out War]] · [[Campaign]] · [[Progression]]

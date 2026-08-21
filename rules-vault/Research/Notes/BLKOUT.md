---
type: research-note
title: BLKOUT
game: BLKOUT
publisher: Enemy Spotted Studios & Mr. Mystery Studios
depth: primary — full rulebook + supplement
retrieved: 2026-07-22
tags: [settlements/research]
---
# 🎲 BLKOUT

> [!abstract] In one breath
> A **high-lethality tactical skirmish game** on the colony planet ABOL in 2110, where war is multi-domain — firefights *plus* cyberspace, combat AI, drones and mechs. Small **Group** of 32mm minis, **D10s**, objectives, dense terrain, 30–45 minutes. Miniatures-agnostic. It is the game Settlements battles are explicitly aimed at feeling like.

| | |
|---|---|
| **Publisher** | Enemy Spotted Studios & Mr. Mystery Studios (ESS) |
| **Scale / format** | 8–12 models a side (scaling to 32+), 2×2 to 4×4 ft, objective-driven |
| **Core resolution** | `2D10` vs **Skill**, count successes — one success passes |
| **Depth of read** | **Primary** — Print 2nd Edition digital rulebook (23pp) + Supplemental Packet April 2026 (9pp) |
| **Long-form** | `docs/BLKOUT-RULES-ANALYSIS.md` — full 420-line read-through, framed against our own taxonomy |

---
## Why it's here

It is the **battle-feel target on record** for Settlements: highly tactical, super-deadly, fast-paced, multi-dimensional. It shares most of our DNA already — objective-primary victory, alternating activation, dice-off priority, one-hit lethality, "cover protects being hit, armour protects being hurt" — which makes the places it *differs* unusually informative. Its reaction system is the best thing in it. Its absent morale layer is the gap we deliberately fill.

---
## The Skill Check — one test, and cover is dice

**Type:** Dice · **Take:** 📎 reference (⚙️ for the cover idea)

Roll **2D10** against the model's **Skill** (lower Skill = better trained). Each die **≥ Skill** is a **Success**. **At least one Success passes.** A natural **10** is an **Ace** and counts as **two** Successes.

Adjustment happens in the dice pool, never the target number:

- Bonuses and penalties **add or remove whole D10s**.
- You can never roll **fewer than 1D10**.
- A check flagged **Hard** caps you at **1D10** maximum, however many bonuses you're holding.

Shooting, close combat, hacking, securing objectives, running someone over — all of it is a Skill Check with dice added or subtracted. Master that loop and you understand 80% of the game.

**Why it works.** *Cover literally removes dice thrown at you.* That is more viscerally legible at the table than a number written on a chart, and it makes the fiction and the maths the same gesture.

**For Settlements.** Ours is `1d10 + Stat + mods vs 7+` — one die, modifiers shift the total ([[Rules Engine]]). Same design goal, one universal test, opposite implementation. **Ours is faster to read and less swingy; theirs is more visceral.** We are not changing engines — the locked tenet is that no second dice type exists anywhere in the game. What's worth borrowing is the *framing*: "Hard" as a ceiling expressed inside the resolution economy is a cleaner idea than a bolted-on cap, and it's a lens on our own **±3 modifier cap**.

---
## Reactions — the beating heart

**Type:** Reactions · **Take:** ⭐ steal — and we already have

On the **enemy's** activation your models can act. A model may React if it hasn't activated yet this round, **or** holds a **Ready Token**. Reacting costs an **Engaged Token**, which replaces any Ready Token — and a model with an Engaged Token can neither act nor react again that round. **Reactions are a finite, budgeted resource.**

Three reactions:

| Reaction | What it does |
|---|---|
| **Overwatch** | Shoot an enemy that ends an Action, **or ends a Move longer than half its Movement Value**, in your LOS |
| **Return Fire** | Shoot back the instant you're targeted. **Both roll simultaneously**; more Successes applies damage first, and **a destroyed model deals no damage** |
| **Juke** | Spend an Engaged Token to count as in Cover. Matched play: shooter rolls **−1D10**, and a survivor may move up to half its Move |

**Why it works.** You are never just watching your opponent's turn. You're deciding which of a small number of reactions to spend, and they're sequencing activations to bait or dodge yours. **Return Fire in particular makes every trigger-pull a gamble** — you might kill them, or you might trade, and a dead man shoots nobody.

**Move-half-to-dodge-Overwatch** deserves separate credit: it converts movement *distance* into a tactical dial for one sentence of rules. Creep and stay safe; dash and expose yourself.

**For Settlements — status.** Drafted into the vault 2026-07-23, not merely proposed:

- **Return Fire was cut.** Sequential shoot-back already exists as **[[Shooting|Snap Shot]]** (resolves *after* the enemy's shot, so the attacker keeps a first-mover incentive). The simultaneous version was rejected as too swingy and anti-shooter. **[INFERENCE — a design call, not a measured result.]**
- **Juke became [[Movement|Dodge]]** — an opposed **AGI vs DEX** evasion; win = the shot misses and you move full MOV out of LOS, then Pinned. A resourced exception to the "can't dodge a bullet" tenet.
- **Overwatch** = a distance-gated Snap Shot: only a Move greater than half MOV, ending in enemy LOS, triggers it.

---
## Lean Out

**Type:** Movement · **Take:** ⭐ steal

Spend **half your Move** to place a **Lean Out Marker** and peek. Enemies who can only see the *marker* (not the model) treat the marker as the model, and the leaning model has **Cover** from them. The marker is removed before the model moves. **If you only Lean Out and don't move, it doesn't count as "moving"** for special rules — which makes it excellent for static shooters.

**Why it works.** It models the single most common real infantry action — exposing the minimum of yourself to see and shoot — with one marker and one sentence. It also creates a genuine positional decision that costs tempo rather than dice.

**For Settlements.** Directly compatible with [[Terrain Interaction]] and our [[Movement]] economy. The "lean-only doesn't count as moving" clause is the load-bearing half — without it, it's just a worse move.

---
## Verticality is gated by scenery

**Type:** Movement · **Take:** ⚙️ adapt

- Obstacles ≤1" tall: infantry cross for **−2" of movement**.
- Up and down needs stairs or ladders, and you must **end fully flat on a surface**.
- Per FAQ you **cannot free-climb** — you need an obvious means (ladder, crates) — and **cannot come down from height without Jump**. Find the stairs.
- **Jump (X)** places a model anywhere within X" horizontally and X" vertically, without passing through terrain.

**Why it works.** No climbing test exists, so no climbing test can be argued about. The terrain piece itself is the permission.

**For Settlements.** Ours resolves climbing through **AGI** ([[Movement]]), which is the right call for a game where AGI is a purchased stat — but the *no free descent* rule is worth a look. It makes rooftops a commitment rather than a free vantage, which is a cheap way to make our nine-feature board matter more.

---
## Morale, deleted

**Type:** Morale · **Take:** ⚠️ instructive failure

BLKOUT has **no break tests, no fear, no rout, and no suppression-from-fire.** The only morale-adjacent mechanic is the **Pinned Marker**: a Pinned unit spends its Reposition step removing the marker instead of moving. Pins come from **Data Attacks** (hacking) and from being aboard a destroyed vehicle — **not** from taking fire.

So a firefight never suppresses heads down. Models die instead of flinching.

**Why it's here.** It is a *defensible* choice — deleting morale is a large part of why the game runs 30–45 minutes — but it is also the game's biggest gap, and it's the axis where Settlements is deliberately deeper. Our **Stress/Nerve** system (1 Stress = Shaken, −1 to everything; 2+ = a Break test in the End Phase) is lean by design and should stay that way. See [[Morale]].

**The tension to hold consciously.** BLKOUT is fast *partly because* it deleted morale and kept conditions thin. Settlements carries Stress **and** a conditions ladder **and** hacking/terrain/deployables **and** a campaign. **Depth and a 30-minute pace trade off directly** — the realistic target is 45–75 minutes, paid for with ruthless bookkeeping discipline. Every new status token is a tax on the exact feel we're chasing.

---
## Slot currency — there is no costing system

**Type:** List · **Take:** ⚠️ the road not taken

The publisher states it outright: *"Forget the tedious task of point-counting; in BLKOUT, you simply choose a force and pick three units."* **[FACT — blkoutgame.com/pages/the-game]**

A **Group** = **1 Force Card + 3 Unit Cards** from that force. Matched Play adds a **Handler** (one of eight archetypes) and allows one unit to be swapped for a **BLKLIST** mercenary. **Control Points** (3 per game) are an *in-game* resource for Battle Drills and chained activations — not a list-building currency.

Balance is carried entirely by **card design and access restrictions**: BLKLIST units *"cannot use Battle Drills, Armory Items, or Force Special Rules"*; Power Cards are *"intentionally less potent than standard force cards, but they open the door for highly thematic and flexible force-building."*

**The objection is exact, and it's in the canonical design literature.** Gutschera: *"'Everyone gets to bring 16 pieces to the table' is a costing system for choose-your-own-army chess (each piece you bring costs you 1 of your 16 slots) but it's not robust, since players will choose nothing but queens."* **[FACT]** That is precisely why BLKOUT has to lean so hard on card design and access tiers.

**For Settlements.** Nothing to steal on costing — we chose the other trade deliberately, and a player-built armoury is a pillar. The value here is the **negative** result: a slot system removes costing risk entirely at the price of customisation. Related: [[Kill Team#Slots instead of prices for the long tail]] reaches a smarter middle — slots for the long tail, real prices for what carries the game.

**[NOT FOUND]** No unit card face was obtained, so it cannot be stated as fact that *no number* is printed on a card — only that the publisher disclaims point-counting and every force-building rule found is slot-and-restriction based. There is essentially **zero public discussion of BLKOUT costing** because there is nothing to discuss.

---
## Force Rules — one rule, one playstyle

**Type:** Faction · **Take:** ⭐ steal

BLKOUT's strategic variety comes almost entirely from **one Force Special Rule per faction** — Harlow gets sprint/assault aggression, Impisi gets recruit-recursion attrition, Boone gets shoot-in-reposition gunline.

**Why it works.** It is the cheapest possible lever for "players choose different strategies," and it is the thing reviewers actually *feel* and write about. One strong, legible rule beats twelve small modifiers, because a player can hold it in their head while making every decision.

**For Settlements.** [[Factions]] is drafted as a framework with a six-faction roster adopted and the names still open. **Give each faction one strong rule that dictates a playstyle** before adding anything else. Compare [[Malifaux#The keyword tax]] and [[Trench Crusade#Faction rules that edit the economy]] — three different places to write faction identity: the rules, the hiring price, or the price list itself.

---
## What it gets wrong

**Type:** Production · **Take:** ⚠️

- **Fragmentation is the #1 community complaint** — rules spread across 6+ documents. **[CONSENSUS]** Our single-vault, single-master-note approach ([[Full Rules System v1]]) is the thing we're already doing right; don't lose it.
- **Token clutter** gets flagged even with a *thin* ruleset. Settlements carries Stress + conditions + hacking + terrain states — **marker load is our biggest silent threat to the pace goal.**
- **Cover changes between books.** The core rule is binary (terrain blocks >half of you = Cover); matched play patches in a graded Full/Partial chart. A newcomer who learns the base book then plays matched finds the cover rules meaningfully different. We bake graded cover (Light −1 / Heavy −2) into the core engine from the start — better.

---
## Source

- Primary: `z:/Downloads/BLKOUT-DIGITAL-RULE-BOOK.pdf` (Print 2nd Ed.) + `z:/Downloads/BLKOUT_Supplemental_4-26.pdf`, read 2026-07-22
- Long-form analysis: `docs/BLKOUT-RULES-ANALYSIS.md` (§19 is the Settlements convergence plan)
- Costing profile: `docs/POINTS-RESEARCH.md` §7.0
- Related: [[Wargaming Research]] · [[Kill Team]] · [[Rules Engine]] · [[Morale]]

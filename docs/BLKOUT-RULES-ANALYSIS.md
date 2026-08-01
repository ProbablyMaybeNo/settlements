# BLKOUT — Complete Rules & Systems Analysis

*Reference read-through of **BLKOUT Print Second Edition** (digital rulebook, 23pp) + **BLKOUT Supplemental Packet, April 2026** (9pp). A game by Enemy Spotted Studios & Mr. Mystery Studios (ESS).*

Framed against the wargame-component taxonomy used in the Settlements vault (`rules-vault/Rules System/`) so the two designs can be compared directly. Written so someone who has never played can understand exactly how a game runs.

---

## 0 · What BLKOUT is, in one breath

A **high-lethality tactical skirmish wargame** set on the colony planet **ABOL** in 2110, where war is "multi-domain" — physical firefights *plus* cyberspace (**Data Attacks**), **Combat AI**, drones, and giant armoured mechs called **Dusters**. You control a small **Group** of 32mm miniatures, roll **D10s**, and fight over **objectives** on a dense, terrain-heavy 2×2 to 4×4 ft board. Games are short, brutal, and decided by positioning, cover, and who reacts fastest. Miniatures-agnostic; a print-at-home supplement exists.

**The single most important thing to understand:** every action in the game is one dice test — the **Skill Check** — and *cover literally adds or removes dice*. Master that one loop and you understand 80% of BLKOUT.

---

## 1 · The core dice engine (the one mechanic everything reuses)

**The Skill Check.** Roll **2D10** and compare each die to the model's **Skill** value (lower Skill = better trained).

- Each die **≥ Skill** = a **Success**.
- **At least one Success** = the check **Passes**.
- A natural **10** is an **Ace** = counts as **two Successes** (this is where big swings and drama come from).

**Adjusting the dice pool** (this is the clever part):
- You can never roll **fewer than 1D10**.
- A **"Hard"** check caps you at **1D10** maximum.
- Bonuses/penalties are applied by **adding or removing whole D10s**, not by modifying the target number.

That's the entire resolution system. Shooting, close combat, hacking, securing objectives, running someone over — all of it is a Skill Check with dice added or subtracted for circumstances.

> **Settlements contrast:** Settlements uses `1d10 + Stat + mods vs 7+` (one die, modifiers shift the total). BLKOUT uses `2D10 vs Skill, count successes` (a dice pool, modifiers add/remove dice). Same design goal — one universal test — but BLKOUT's "cover = fewer dice thrown at you" is more viscerally intuitive at the table, while Settlements' single modified die is faster to read and less swingy.

---

## 2 · The building blocks (army/force structure)

BLKOUT nests four layers. Learn them bottom-up.

| Layer | What it is |
|---|---|
| **Model** | One miniature. Either **Infantry** (human-sized, on a 25mm/1" base) or a **Vehicle** (larger, may have no base). |
| **Unit** | A **Unit Card** + its models: **Grunts** (identical, use only the card's stats) and **Specialists** (extra models with their own weapons/rules, sometimes their own Skill/Movement). Each Specialist must be a visually distinct model. |
| **Force** | A **Force Document/Card** = your faction. Provides a **Force Special Rule**, a **Force Armory** (weapons/abilities Grunts can borrow), and **Battle Drills** (special abilities units can trigger). |
| **Group** | Your whole army for the game = **1 Force Card + 3 Unit Cards** from that force. |

### What's printed on a Unit Card
- **Unit Name** and **Unit Special Rules** (some are limited-use — you tick a box each time).
- **Skill**, **Movement Value** (inches), **Armor** (written `X/Y` — see §7).
- **Number of Grunts**, **number of Specialists**.
- **Weapon** — the primary weapon every model in the unit carries: its **Range / Damage** and any **Special Rules**.
- **Combat Loads** — triangles in the card corner. Each is one "charge" a Grunt can spend to pull a weapon/ability from the Force **Armory**. Tick one per use.

### Game size = number of Groups
- **1 Group** → small game, 2×2 to 3×3 ft.
- **2 Groups** → medium, 3×3 ft.
- **3 Groups** → large, 4×4 ft.

### Matched Play adds two things (the "tournament" build)
A **Matched Play Group** = **1 Handler + 1 Force Card + 3 different Units**, where **one unit may be swapped for a BLKLIST mercenary unit**.
- **Handler** = a commander model. Pick one of eight archetypes: **Agent, Assault, Covert, Cyber, Keres, Marksman, Melee, Siege**. Handlers can't use Battle Drills, Armory, or the Force Rule — they're their own thing.
- **BLKLIST units** (mercenaries): Banak Dust Element, Exterminator Drone, Gull Drones, Hired Killers, Nomads, Rebel Miners, Szabla Element, Whistler Drone. They also can't use the force's Drills/Armory/Rule.

> **Settlements contrast:** Structurally very close cousins — both are objective-driven, miniatures-agnostic skirmish games with a small force and a faction identity layer. Settlements builds its crew from a point-buy; BLKOUT hands you **fixed pre-costed Unit Cards** and you assemble a Group from them (no points in the base game — balance is by card design and the "both players agree" social contract).

---

## 3 · Game setup

1. **Pick game size** (number of Groups) and build your Group(s).
2. **Pick a Scenario** (several in the book; more online). The scenario sets table size, objectives, and special rules.
3. **Arrange terrain** — thematic and balanced, dense with structures and line-of-sight blockers.
4. **Choose Deployment Edges** — roll a D10 each (reroll ties); higher chooses their edge (and usually becomes the **Attacker**), opponent takes the opposite edge. Attacker typically deploys up to 2" on and **activates first in Round 1**.
5. **Insert** — models not starting on the table use their first Move to come on from their Deployment Edge.

---

## 4 · Round structure

A game is a series of **Rounds**. Each Round has two parts: **Operations**, then **Execution**. Scenarios cap the game (all printed ones end after **5 Rounds**; whoever's ahead on the objective wins, and some scenarios end early on a points lead).

### Operations (housekeeping + who goes first)
1. **Pick Up** — remove all Activation Markers, Ready Tokens, Engaged Tokens.
2. **Determine Initiative** — both players roll **1D10**, reroll ties. Higher activates first this Round. (You may spend a **Control Point** to add a D10 to this roll.)
3. Smoke dissipation and persistent effects are also resolved around here.

### Execution (the actual game)
- Players **alternate activating one Unit at a time**, starting with the initiative winner.
- The Round **ends when both players have activated all their Units**. Then a new Round begins.

> **Settlements contrast:** Nearly identical skeleton — dice-off for priority, alternating activations, an end/upkeep step. Settlements folds Break tests and condition resolution into an explicit **End Phase**; BLKOUT has no morale step to resolve (see §9), so its round is lighter.

---

## 5 · Activating a Unit (a unit's turn)

When you activate a Unit, you do **two steps in order**:

1. **Reposition** — **every model** in the Unit may **Move** (up to its Movement Value).
2. **Actions** — after all models have moved, **each model makes exactly one Action**, resolved one at a time:
   - **Shoot** — attack a target (see §6).
   - **Ready** — take a **Ready Token** (lets the model **React** later, even after activating — see §8).
   - **Sprint** — **Move again** (this is why a model can effectively move twice: once in Reposition, once as a Sprint Action).

At the start you may **choose one Battle Drill** for the unit (costs a Control Point). When finished, the unit gets an **Activation Marker** (it can't activate again this round). You may spend a Control Point to immediately **chain into activating another unit**; otherwise your opponent activates.

**Enemy models can interrupt you** — every Action can trigger **Reactions** (§8). This back-and-forth is the tactical heart of the game.

> **No unit coherency** — the FAQ confirms models in a unit don't have to stay near each other. They spread out freely.

---

## 6 · Movement

- Measure from the base; move up to the Movement Value; **can't pass through enemies or terrain**.
- **Obstacles** (terrain ≤1" tall): infantry cross by paying **−2" of movement**.
- **Up/down**: use stairs/ladders; you must **end fully flat on a surface**. Per FAQ you **cannot free-climb** — you need an obvious means (ladder, crates), and you **cannot come down from a height without Jump** — find the stairs.
- **Leaning Out**: spend **half your Move** to place a **Lean Out Marker** and peek. Enemies who can only see the *marker* (not the model) treat the marker as the model, and the leaning model has **Cover** from them. Removed before the model moves. If you *only* Lean Out (don't move), it doesn't count as "moving" for special rules — great for static shooters.
- **Jump (X)**: a Jump special rule lets a model be placed anywhere within X" horizontally and X" vertically, without passing through terrain.

---

## 7 · Combat — shooting, wounds, and saves

### Shooting: the 5-step loop
1. Pick a target you have **Line of Sight** to and is **within Weapon Range**.
2. Determine if the target is **in Cover**.
3. Roll a **Skill Check**, **+1D10 if the target is NOT in cover**, **−1D10 if it IS in cover**. (Dice in a shooting check are called **Shots**.)
4. **Each Success** deals the **Weapon's Damage**. **Aces (10) double** that weapon's Damage.
5. The target makes an **Armor Check**.

### Wounds, saves, and the Damage Track
- **Armor is written `X/Y`.** The target rolls **X D10** and blocks **one point of Damage per die that rolls ≥ Y**.
- You can only block up to **X points total** — if you suffer more Damage than your Armor dice, the excess can't be stopped.
- Damage that isn't blocked is **marked on the model's Damage Track**. When the track fills, the model is **Destroyed**. **Models with no Damage Track die to a single point of Damage** — so most infantry are effectively one-hit.

> **Settlements contrast:** BLKOUT uses a **separate save roll** (the Armor Check dice pool, `X/Y`), where Settlements folds defence into a single **Injury roll** (`1d10 + Damage − Armor vs 7+`) with **no separate save**. Both keep the load-bearing principle **"cover protects against being *hit*, armor protects against being *hurt*"** — cover never touches the wound/armor step in either game.

### Close Quarters Combat (CQC) — the automatic melee
After a model finishes an Action while **base-to-base with an enemy infantry model**, **CQC happens automatically**:
- Both models roll a **Skill Check**; **each Success = 1 Damage, ignoring Armor**.
- The model with **more Successes applies its Damage first** — if that destroys the loser, the winner takes **no** damage back.
- Ties → highest single die wins; still tied → reroll.
- CQC **repeats each round of rolls until one model is destroyed.**

### Melee (the weapon rule) is a *different thing* from CQC
This trips everyone up (the FAQ addresses it directly): **Melee** is a **weapon Special Rule** resolved as a **modified Shoot Action** (you place the attacker base-to-base first, it ignores cover, and the target may only Return Fire with a Melee weapon or Juke). **CQC** is the separate automatic base-to-base roll-off above. A melee attack can *lead into* a CQC.

### Explosives / Blast — a parallel resolution path
Blast weapons **cannot target infantry directly**. Instead you **place a 25mm Blast Marker** you can see, make a Skill Check, and every infantry model within X" makes an **Armor Check** rolling dice equal to your Successes (a point of Damage per failed die). Blast ignores LoS/cover to models in the radius (subject to "agree it's realistic").

The supplement splits Blast into **two firing modes**:
- **HE (High Explosive)** → the marker/AoE method above, vs infantry.
- **AP (Armor Piercing)** → normal single-target shooting vs **Vehicles/Dusters** (choose a damage track).

---

## 8 · Reactions (the interactive layer — this is the game's beating heart)

On the **enemy's** activation, your models can act. A model may React if it **hasn't activated yet this round** *or* has a **Ready Token**. Reacting costs an **Engaged Token** (which replaces any Ready Token). **A model with an Engaged Token can't Act or React** again this round — so reactions are a finite, precious resource.

Three reactions:
- **Overwatch** — Shoot an enemy that **ends an Action**, or **ends a Move that took it farther than half its Movement Value**, in your Line of Sight. (Moving *slowly* — half your move or less — dodges Overwatch. Big deal tactically.)
- **Return Fire** — one model shoots back the instant it's targeted by a Shoot Action. **Both roll simultaneously**; more Successes applies Damage first, and **a destroyed model deals no Damage** — so every shot you take is a gamble.
- **Juke** — when targeted by shooting, spend an Engaged Token to **count as in Cover**. (Matched play makes it stronger: shooter rolls **−1D10**, and if you survive you may move up to half your Move.)

> This system is the reason BLKOUT feels tactical rather than passive. You are never just watching your opponent's turn — you're deciding which of your limited reactions to spend, and they're sequencing their activations to bait or dodge yours.

> **Settlements contrast:** Settlements has a comparable **Ready → React** economy (Snap Shot / Charge / Throw / Interact / Trigger) with a 180° forward arc. BLKOUT's version is richer at the point of contact (Return Fire's simultaneous roll-off, Juke as an active dodge) but has no facing arc — LoS is omnidirectional.

---

## 9 · Morale / suppression — almost none (a defining choice)

BLKOUT has **no break tests, no fear, no rout, and no suppression-from-fire.** The only morale-adjacent mechanic is the **Pinned Marker**:
- A Pinned unit must **spend its Reposition step removing the marker instead of moving** any models.
- Pins come from **Data Attacks** (hacking) and from **being aboard a destroyed vehicle** — *not* from taking fire.

So a firefight never "suppresses heads down." This is a deliberate lethality-first design: models die instead of flinching.

> **Settlements contrast:** This is the single biggest philosophical divergence. Settlements runs a full **Stress/Nerve** system — 1 Stress = Shaken (−1 to everything), 2+ = a Break test — so suppression and morale are core pressure. BLKOUT deletes that entire axis in favour of raw lethality and cyber-pinning.

---

## 10 · Terrain, cover & line of sight

- **Line of Sight**: an unobstructed straight line from **any point** of your model/base to **any point** of the target's model/base (or marker).
- **Cover (core rule)**: a model has Cover if terrain (or, per errata, a vehicle) **blocks more than half** of it. Binary — you're in cover or you're not.
- **Vertical combat**: a model on terrain **≥3" tall** gets **Cover from models below it**.
- **Structures**: buildings with clear boundaries; models inside have Cover from outside, and you can't draw LoS *through* a structure.

### Matched Play refines cover (a bolt-on fix — important)
The core binary cover is too swingy for competitive play, so matched play adds a **Full/Partial** chart:
- **Full Cover** (−1D10 to the shooter): target is ≥50% obscured **and within 1" of the terrain** giving cover.
- **Partial Cover** (no change): obscured but **not within 1"** of the terrain.
- **Open** (+1D10 to the shooter): not 50% obscured.
- **Smoke**: blocks LoS within 3"; a model fully inside gets Full Cover, partially inside gets Partial. Smoke **dissipates on a 6+** each round (then leaves weaker "Light Smoke").

> **Settlements contrast:** Settlements bakes graded cover (Light −1 / Heavy −2) into the core engine from the start; BLKOUT ships a binary core rule and patches it to graded cover only in the matched-play layer. A newcomer who learns the base book and then plays matched will find the cover rules meaningfully different.

---

## 11 · Weapons & equipment — how they're structured

This is the section most relevant to a designer. **BLKOUT weapons are a base profile + a trait list**, exactly the "base value + trait" shape:

```
WEAPON NAME  |  RANGE / DAMAGE  |  Special Rule(s)
FAL-32C      |  24" / 1         |  CQB
Micro Launcher | 4-16" / 2      |  Blast (1), Heavy
Grenade Launcher | 24" / 2      |  Blast (1)
```

- **Base values** = **Range** (single like `24"`, or a **min–max band** like `4-16"`) and **Damage** (a flat number of hits applied per Success).
- **Hitting** is done by the model's **Skill**; **saving** by its **Armor `X/Y`**. The weapon itself only carries Range, Damage, and traits.
- **Traits** = **Universal Special Rules (USRs)** — a shared library. This is where all the texture lives. Highlights:

| USR | What it does |
|---|---|
| **AP (X)** | Worsens the target's Armor threshold by +X for that hit. |
| **Auto (X)** | After shooting, make up to X extra shots at *different* models within 4" (can't be Reacted to). |
| **Cyclic** | After shooting, immediately make one more Shoot or Ready Action. |
| **Heavy** | +1D10 if you didn't move this turn (reactions always get the bonus). |
| **Deployed** | Only 1D10 if you moved this turn. |
| **CQB** | Re-roll failed Shots within half range. |
| **Medium** | Re-roll one failed Shot. |
| **Seeking** | Ignores the cover −1D10 penalty. |
| **Sustained (X)** | Target must re-roll up to X successful Armor dice. |
| **Blast (X)** | The explosive AoE path (§7). |
| **Indirect** | Fire using another friendly model's LoS. |
| **Melee** | Resolved as a modified Shoot Action, ignores cover (§7). |
| **Lethal** | Roll 3D10 for CQC checks. |
| **Smoke Grenade \| X"** | Place a Smoke Token before repositioning. |
| **EMP / Data Knife / Data Spike** | Cyber-warfare payloads (§12). |
| **Shield / Spotter / Team Leader / Controller / Reinforcements** | Support/utility traits on models and units. |

**Conditions** in BLKOUT are thin and delivered *through* these traits/actions rather than a standalone status system: **Pinned** (Data Spike / wreck), armor-degradation (AP, Sustained), and hard control mostly via cyber and Blast. There's no bleed/fire/poison/stun ladder.

> **Settlements contrast — the key design divergence:** BLKOUT weapons are **designer-authored fixed cards** — the player never builds a weapon, they pick a unit and get its printed profile. Settlements weapons are **player-built** (choose a Class, then spend points on priced Characteristics), which is a fundamentally different authorship model. Same "base + trait" DNA; opposite control. BLKOUT's approach is faster to onboard and easier to balance centrally; Settlements' is more expressive and customization-driven. Notably, several BLKOUT USRs map almost 1:1 onto Settlements characteristics (AP↔Armour Piercing, Seeking↔ignore-cover which Settlements deliberately *bans*, Sustained↔re-roll-armour which Settlements deliberately *bans* to keep one dice mechanic). Worth a side-by-side if you ever want to sanity-check your trait list against a shipped commercial one.

---

## 12 · The "multi-domain" systems (what makes BLKOUT itself)

- **Data Attacks / cyber**: a model with a **Data Spike** makes a Data Attack (Skill Check, **no LoS needed**, range only if listed) to **Pin** an enemy unit or **un-Pin** a friendly one. A **Data Knife** instead deals **1 Damage to an AI/Powered model, ignoring armor**. **Counter EWAR** (matched play) lets a friendly Data Spike nullify an incoming Data Attack by winning a Skill Check.
- **Vehicles**: two damage tracks — **Chassis** and **Mobility** (shooter picks which to target; kill Mobility to immobilize, fill Chassis to destroy). Move in **straight lines** (2" to rotate 90°), **can't React**, can **run over** infantry (Skill Check or destroyed), can **Transport (X)** models (embark/disembark within 2"). Destroyed by a **Blast** weapon → **Explodes**, killing everyone aboard.
- **Dusters** (giant mechs): vehicles that rotate 360°, can **Fight** in CQC, can **Juke**, have **front/rear arcs** (weapons get **+1 Damage** in the rear), and their **Mobility is always Hard** to hit (1D10). Core rules are superseded by the **Impact Expansion** for full "Front Line" Duster rules.
- **Control Points**: **3 per game, never regained.** Spend one to: add a D10 to Initiative, let a unit use a **Battle Drill**, or **chain-activate** another unit. In matched play, also to give a **Handler** a bonus activation.
- **Burn Cards**: draw **3 from a shared 8-card deck**; powerful **one-time** abilities playable any time.
- **Skirmish mode** (activate individual models, one unit per group) and **Larger games** (move-all-then-act-all) are alternate scales.

---

## 13 · Scenarios & victory

BLKOUT is **objective-driven — you win on objectives, not body count** (though kills help). The recurring currency is the **Overrun Point**, earned for:
- **Destroying an enemy Unit**, and
- **Locking Down / Securing Points of Interest** (having a model within 4" with LoS and no enemy within 6"), or **holding quadrants** (matched play).

Each Round, after Initiative, you check the score: in most scenarios, **being 2–3 Overrun Points ahead ends the game instantly**; otherwise the **most points after Round 5 wins**. Scenarios layer on **Hardpoints** (secure them for an extra Initiative D10 or a drone-swarm strike), **Attacker/Defender** asymmetry, and one-off special rules (drop-in Dusters, movable objectives, dome shields).

> **Settlements contrast:** Same win-philosophy exactly — *objectives primary, killing optional but conflict inevitable, tactical withdrawal valid.* Both games explicitly reward you for playing the mission, not the kill count.

---

## 14 · List building — and how you "choose a tactic"

You don't tune a tactic with points; you **choose it by selection**, in four decisions:

1. **Pick a Force (faction) — this IS your strategy.** The Force Rule + Armory + Battle Drills encode a playstyle. Examples from the books:
   - **Harlow 1st Reaction Force** → +2 Movement when Sprinting, plus **Stims** (+2 Move), **Assaulters** (immune to Overwatch on a full move), **Chaff** (drop smoke before activating) → a **fast, reaction-denying assault** force.
   - **Impisi Insurgents** → spend a Control Point to **return a dead Grunt** to the unit → an **attrition / board-control grind**.
   - **Boone Recon** → **shoot during Reposition instead of moving** → a **gunline / overwatch** identity.
2. **Pick 3 Units** from that Force and kit their **Specialists** — this sets your firepower/mobility/cyber mix.
3. **(Matched play) Pick a Handler archetype** — Assault / Marksman / Melee / Siege / Covert / Cyber / Keres / Agent — a second, personal tactical lean for your commander.
4. **(Matched play) Splash one BLKLIST merc unit** to cover a capability your Force lacks (drones, killers, dust elements).

Then in-game, your tactical levers are **Control Points** (3, precious), **Battle Drills**, **Burn Cards**, and above all **how you manage Reactions and objectives**. So "choosing a tactic" is really: *faction identity → unit mix → handler → merc splash*, and the game rewards you for building a Group whose Force Rule and units all pull the same direction.

---

## 15 · Critique

### What BLKOUT does really well
- **One elegant engine that carries huge weight.** The 2D10-vs-Skill Skill Check with **cover = ±a die** is intuitive, fast, and makes positioning *tangible* — you can literally see fewer dice being thrown at a well-covered model. Aces (double damage) inject drama without a separate crit table.
- **Best-in-class interactivity.** The Overwatch / Return Fire / Juke system means the opponent's turn is a decision-rich phase for you, and every shot is a genuine risk (Return Fire's simultaneous roll-off is a standout — you can die by pulling the trigger). This is the game's biggest strength and the reason it plays *tactical*.
- **Cyber is real, not flavour.** Data Attacks, Counter-EWAR, EMP, Data Knives, and Pinning give the "multi-domain 2110" pitch actual mechanical teeth — a hacker meaningfully shapes a firefight.
- **Lethality delivers on its promise.** Low armour + direct damage + one-hit infantry means "every decision is life or death" is true, and games stay short and sharp.
- **Accessible footprint.** Miniatures-agnostic, low model count, small tables, print-at-home supplement, alternating activation that keeps both players engaged the whole game.
- **Verticality and positioning are richly rewarded** (Lean Out, 3"+ cover-from-below, structures, half-move-to-dodge-Overwatch).

### Weaker mechanics & friction points
- **The core relies heavily on "players agree."** Terrain effects, what counts as a structure, Blast LoS, vehicles crossing terrain — all deferred to table consensus. Lovely for a narrative group; a problem for consistency and tournaments. The **entire matched-play cover system is a bolt-on fix** for exactly this, which tells you the base cover rule is under-specified and swingy.
- **The full ruleset is fragmented across four+ documents** — rulebook, supplemental, a separate Universal Special Rules card, an FAQ, errata, and paid expansions (you need the **Impact Expansion** for real Duster rules; the supplement even *removed* its own Quick Reference and Expansion sections). A newcomer **cannot learn the complete game from one file**, which is a real onboarding tax.
- **No suppression-from-fire is a notable gap for a "tactical firefight" game.** With morale essentially deleted, combat can't pin heads down, so the game skews toward **alpha-strike snowballing** — remove models first and the activation/dice advantage compounds with no morale friction to slow it. It's an intentional lethality choice, but it costs the "suppressed under fire" texture that defines the genre it's evoking.
- **Two overlapping close-combat systems (CQC vs Melee)** are genuinely confusing — the FAQ leads with "what's the difference?" for a reason. Elegant once learned, opaque on first read.
- **Emergent rules-lawyering.** Auto+Cyclic needs a 4-step FAQ ordering; simultaneous multiple reactions can be "wasted"; Blast has dual HE/AP modes; Duster/Mobility + Smoke targeting has fiddly caveats. These are the edge cases that *require* the FAQ, meaning table disputes are likely without it to hand.
- **Marker/token bookkeeping is heavy for a "fast" game** — Ready, Engaged, Activation, Pinned, Lean Out, Smoke/Light Smoke, Combat Loads, Overrun Points, Control Points, Burn Cards all in play at once.
- **Swinginess.** One-hit infantry + Aces (doubling) + whole-die pool swings mean single rolls can decide a lot. Fun and cinematic; punishing if you want a controllable, grind-it-out experience.
- **Balance is partly outsourced to the social contract** (Dusters require mutual agreement; power is gated by Handler/BLKLIST rules) rather than a points economy.

### Tactical or narrative?
**Fundamentally a tactical engine wearing a narrative skin.** The mechanical meat — cover-dice, reactions, activation sequencing, LoS, verticality, objective control — is pure tactics, and **matched play deliberately strips the fuzz to push it toward competitive play**. But the *presentation* is strongly narrative: scenario fiction, Burn Cards, "agree with your opponent" resolution, and gentleman's-agreement terrain. So: **tactical core, narrative wrapper, with narrative-flavoured fuzziness in the base rules that matched play cleans up.**

### How you actually win (winning tactics)
1. **Play the objective, use kills to enable it.** You win on Overrun Points — but destroying enemy units both scores *and* removes their ability to contest. The tension is control vs tempo.
2. **Weaponize activation order & initiative.** Win Initiative, then use Control Points to **chain activations** — grab or double-contest an objective before the enemy can react.
3. **Cover discipline is everything.** Always fight *from* cover (fewer Shots at you) and catch enemies *in the open* (more Shots from you). **Lean Out** to shoot without exposure; **Juke** to survive being targeted.
4. **Deny reactions.** Move at **half speed or less to dodge Overwatch**; use **Chaff/Smoke** to cut LoS; bait the enemy into spending **Engaged Tokens** (wasting reactions) before your key unit commits; run **Assaulters** to ignore Overwatch outright.
5. **Bank Ready Tokens** to threaten fields of fire on the enemy's turn.
6. **Focus fire.** Fragile models + doubling Aces mean concentrated Shots snowball the model/activation advantage fast.
7. **Take the high ground** — 3"+ elevation for cover-from-below and cleaner LoS.
8. **Use cyber for tempo** — Data-Spike **Pin** an enemy unit to steal its Reposition move at the decisive moment; Counter-EWAR to protect your own.
9. **Spend your 3 Control Points where they swing the game** — usually a pivotal-round Initiative re-roll, a chain-activation on an objective, or a Battle Drill at the perfect beat.

---

## 16 · BLKOUT vs Settlements — one-page cheat sheet

| Component | BLKOUT | Settlements |
|---|---|---|
| **Core test** | 2D10 vs Skill, count Successes; 10 = Ace (2 successes) | 1d10 + Stat + mods vs 7+ |
| **Cover** | Adds/removes a whole D10 (Shot) | Flat −1 (Light) / −2 (Heavy) modifier |
| **Wounding** | Successes × Damage, then separate **Armor Check** save (`X/Y` dice pool) | Single **Injury roll** `1d10 + Dmg − Armor vs 7+`, no separate save |
| **Weapons** | Fixed designer-authored profile: **Range/Damage + USR traits** | Player-built: **Class + priced Characteristics** |
| **Morale** | Essentially none (Pinned only, from cyber/wrecks) | Full **Stress/Nerve** + Break tests |
| **Reactions** | Overwatch / Return Fire / Juke, no facing | Ready → Snap Shot/Charge/etc., 180° arc |
| **Round** | Operations (initiative) + Execution (alternating), ~5 rounds | Priority + alternating activations + End Phase, 6 rounds |
| **Activation** | Reposition (all move) → Actions (each: Shoot/Ready/Sprint) | 1 Move slot + 1 Action slot, Orders/Ready |
| **Victory** | Objective-driven (Overrun Points), kills optional | Objective-driven, kills optional |
| **Signature system** | Cyber / Data Attacks / Dusters | Settlement-building meta-layer + Stress |

The two games are close genre cousins — same objective-primary, terrain-dense, alternating-activation, miniatures-agnostic skeleton. Where they part ways is instructive: BLKOUT bets on **lethality + cyber + reactions** and skips morale; Settlements bets on **morale/Stress + player-built weapons + a persistent settlement campaign**. BLKOUT is the useful sanity-check for "here's how a shipped commercial game solved the same problems you're solving."

---

## 17 · Rules rating (scorecard)

Rated against what BLKOUT is *trying to be* — a fast, lethal, tactical modern-skirmish game — not against a 400-page ruleset it never wanted to be.

| Dimension | Score | Why |
|---|:--:|---|
| **Core dice engine** | 8.5 / 10 | One mechanic (2D10 vs Skill), cover = ± a die. Elegant, legible, does a lot with little. |
| **Reactions / interactivity** | 9 / 10 | The standout. Overwatch / simultaneous Return Fire / Juke make the enemy turn yours too. |
| **In-battle tactical depth** | 8 / 10 | Positioning, LoS, verticality, half-move-dodge, reaction sequencing all carry real weight. |
| **Lethality & pace** | 9 / 10 | Nails the brief — one-hit infantry, 30–45 min games, brutal decisions. |
| **Multi-dimensional systems** | 7.5 / 10 | Cyber/vehicles/mechs have genuine mechanical teeth, but full Dusters are gated behind a paid expansion. |
| **Strategic variety / list-building** | 6.5 / 10 | Factions have distinct identities, but customization is shallow (fixed cards), the meta is young, and balance leans on "both players agree." |
| **Completeness / organization** | 5.5 / 10 | Weakest area — real ruleset is scattered across rulebook + supplement + USR card + FAQ + errata + expansions; base book reads as incomplete. |
| **Accessibility / onboarding** | 7.5 / 10 | 30-minute read, free rules — undercut by the "internet scavenger hunt" for the rest. |
| **Overall** | **~8 / 10** | As a delivery vehicle for *fast, super-deadly, highly-tactical, multi-dimensional skirmish*, it genuinely succeeds. The rough edges are polish and completeness, not the core loop. |

**One-line verdict:** the *engine* is a 9; the *packaging of the full ruleset* is a 5.5; the product averages to a strong, rough-edged 8.

## 18 · What people say online (community reception)

**Caveat first:** BLKOUT is a young, small-studio game (Gamefound Nov 2023, Print 2nd Ed. + supplement 2026). The community is small and enthusiast-skewed, so this is impressions and early reviews, not a mature tournament consensus. There isn't much deep Reddit/competitive-meta discussion yet.

**The consensus is broadly positive**, and remarkably consistent on the core:

- **Fast and brutal — universally.** Iron Dice: *"plays fast, and is brutal,"* rules *"tight and concise."* OnTableTop members: *"incredibly lethal,"* *"one unsaved hit kills most models,"* and that lethality *"forces careful tactical play rather than reckless advancement."*
- **Genuinely tactical, minimalist by design.** Repeated praise that stripped-down rules push *real military tactics over rules-combos*. The designer's ethos, quoted approvingly: *"If there are no rules, you cannot bend them, and you use what you have."* The reaction system is singled out as *"simple but effective."*
- **Veteran-made authenticity** comes up a lot as a selling point that people feel in how it plays.
- **Distinct faction playstyles** are recognized (elite clones vs. criminal gangs vs. insurgents), so people do feel the strategic identities.
- **Model quality** praised by several as crisp 3D prints; CCGwinkel floated it as a possible *"Spectre killer"* and *"the future of wargaming."*

**The criticisms are real and cluster tightly:**

- **Incompleteness / rules fragmentation** — the loudest complaint. An RPG Pub moderator (E-Rocker): the printed rules are *"incomplete,"* with undefined Unit Special Rules, missing Burn Card abilities, and no templates — *"when I buy a game, I'm expecting a complete game, not an internet scavenger hunt."* This matches my own §15 critique exactly.
- **Thin narrative flavor in the book** — despite atmospheric marketing, the rulebook has *"only two short paragraphs"* of fluff; one reviewer: if you want the promised sci-fi flavor, *"look elsewhere."*
- **Inconsistent model QC** — praised as crisp by some, but at least one player reported minis becoming *"horrible and super fragile"* after a few months. So QC appears uneven.
- **Cost of the full kit** — free rules and a cheap ($12.99) print rulebook, but the full boxed set runs ~€120, and terrain isn't included.

**Do people like it? Yes** — the people who've played it are enthusiastic, and the praise centres on precisely the things you want (fast, deadly, tactical). **Is the tactical gameplay good? The community says yes**, strongly, especially the reaction system and cover/positioning play. **Does it support different strategies, and does that system work?** Faction identities clearly land, but the *depth* of strategic diversity is unproven at scale — the customization is shallow and the meta is young, and the "both players agree" fuzziness is the thing most likely to undercut consistent strategic expression (which is exactly why they bolted on the matched-play layer).

## 19 · Designing Settlements toward the BLKOUT feel

*Goal on record: Settlements battles should feel like BLKOUT — highly tactical, super-deadly, fast-paced, multi-dimensional.* Good news: **Settlements already shares most of BLKOUT's DNA**, and in several places is aiming deeper. Here's the honest map of where to converge, where to diverge, and what to steal.

### Where they're already the same (you're on-genre)
- **Objective-primary victory, kills optional but conflict inevitable.** Identical philosophy.
- **Alternating activation, dice-off priority, ~6-round envelope, miniatures-agnostic, dense interactive terrain.** Same skeleton.
- **Super-deadly wounding.** Both are effectively **WND-1 / one-hit** games. You already have the lethality BLKOUT is praised for.
- **"Cover protects being hit, armor protects being hurt."** Both hold this exact line. It's load-bearing in both engines.
- **Cover/positioning is the primary skill expression.** Same design bet.

### Where they differ (and which way to lean)
| Axis | BLKOUT | Settlements | Recommendation |
|---|---|---|---|
| **Morale/suppression** | None (Pinned only, from cyber) | Full Stress/Nerve + Break | **Keep yours — it's your edge.** BLKOUT's biggest *gap* is no suppression-from-fire. Just keep it lightweight (see below). |
| **Reactions** | Overwatch / **simultaneous Return Fire** / **active Juke** | Ready → Snap Shot/Charge, 180° arc | **Steal from BLKOUT.** This is their best system and the engine of the "tactical feel" you want. |
| **Cover math** | ± a whole D10 (swingy, visceral) | Flat −1/−2 modifier (clean) | **Keep yours** — it fits your single-die engine and is less swingy. |
| **Weapons** | Fixed designer cards | Player-built (Class + Characteristics) | **Keep yours** — more strategic expression at list-building than BLKOUT offers. |
| **Multi-dimensional** | Cyber + vehicles + mechs | Hacking, Deployables, Terrain Interaction, Infrastructure, + campaign | **You're already deeper.** The lesson is *delivery*, not scope (see steal #5). |
| **Rules packaging** | Fragmented across 6+ docs | Single Obsidian vault, one source | **Keep yours** — their #1 complaint is exactly the thing you're doing right. |
| **Pace** | 30–45 min | Targeting ~1.5 hr | **Tighten toward ~45–75 min** if BLKOUT pace is the goal (see the tension below). |

### Steal these five things (highest-value, lowest-cost)
1. **Simultaneous Return Fire.** The single best mechanic in BLKOUT: when you're shot, you can shoot back *at the same time*, and a killed model deals no damage. It makes **every trigger-pull a gamble** — instantly more tactical and more deadly, with zero new subsystems. Your Ready→React already has the hooks; add a simultaneous-resolution reaction and you've imported the feel.
2. **Active dodge (Juke).** Let a targeted model spend its reaction to gain cover / roll the attacker down. Gives the defender agency *on the enemy turn* — the thing that makes BLKOUT's opponent-turn engaging rather than passive.
3. **Move-half-to-dodge-Overwatch.** Turning movement *distance* into a tactical dial (creep to stay safe, dash to close and expose yourself) is a huge amount of tactical texture for one sentence of rules. Trivial to graft onto your Ready/overwatch triggers.
4. **One playstyle-defining rule per faction.** BLKOUT's strategic variety comes almost entirely from **Force Rules** — Harlow = +sprint/assault (aggro), Impisi = recruit-recursion (attrition), Boone = shoot-in-reposition (gunline). When you build Factions (S5), give each **one strong, legible rule that dictates a playstyle**. It's the cheapest possible lever for "players choose different strategies," and it's the thing reviewers actually feel.
5. **Keep multi-dimensional systems as a single core Action, not a subsystem.** BLKOUT's cyber works because a Data Attack is *one Skill Check that Pins a unit* — it lives inside the normal action loop. Your Hacking/Deployables/Terrain-Interaction risk becoming pace-killing subsystems. Pressure-test each one: **can it be one Action = one test = one clear effect?** If yes, it stays fast *and* multi-dimensional. If it needs its own mini-phase, it's fighting your BLKOUT-pace goal.

### The one real tension to decide consciously
**Suppression-texture vs. raw speed.** BLKOUT is fast *partly because it deleted morale and kept conditions thin.* Settlements deliberately has a Stress system **and** a conditions ladder **and** hacking/terrain/deployables **and** a settlement campaign. That depth is your differentiator — but **depth and BLKOUT's 30-minute pace trade off directly.** You can't have both extremes.

The resolvable path: **keep the depth, pay for it with ruthless bookkeeping discipline.** BLKOUT gets dinged for token clutter even with a *thin* ruleset; Settlements carries Stress + conditions + hacking + terrain states, so the marker load is your biggest silent threat to the "fast-paced" goal. Your current Stress design is actually already lean (1 Stress = Shaken −1 always-on; 2+ = one Break test in the End Phase) — that's the right instinct. Guard it. Every new status token or mid-activation subsystem is a tax against the exact feel you're chasing.

**Net:** aim for a game that is **as deadly and reaction-driven as BLKOUT, plus the suppression layer BLKOUT lacks, minus the fragmentation and bookkeeping** — landing around 45–75 minutes. That's not a copy of BLKOUT; it's BLKOUT's best ideas (reactions, lethality, faction identity) fused with your genuine advantages (Stress/suppression, player-built weapons, single-source rules, persistent campaign). If you hit it, Settlements is *more* tactical than BLKOUT, not just as tactical.

> **Implementation status (updated 2026-07-23).** Drafted into the Obsidian vault (`Rules System/`), not just proposed. **Return Fire was cut** — sequential shoot-back already exists as Settlements' **Snap Shot** (resolves after the enemy's shot, so the attacker keeps a first-mover incentive); the simultaneous version was rejected as too swingy / anti-shooter. **Juke became "Dodge"** — an opposed **AGI vs DEX** evasion (win = shot misses + move full MOV out of LOS, then Pinned), a resourced exception to the "can't dodge a bullet" tenet. **Overwatch** = a distance-gated Snap Shot (only a Move > half MOV ending in enemy LOS triggers it). **Orders** were already Specialist/Leader-only. Factions still deferred.

---

*Sources for §18: [Iron Dice — "Operation Bone Scraper" spool-up](https://irondice.org/2025/04/05/operation-bone-scraper-a-blkout-spool-up/) · [OnTableTop / Beasts of War forum thread](https://www.ontabletop.com/forums/topic/blkout-near-future-sci-fi-by-enemy-spotted-studios/) · [RPG Pub thread](https://www.rpgpub.com/threads/blkout-minis-game.12751/) · [CCGwinkel unboxing review](https://ccgwinkel.com/2026/04/26/blkout-the-new-modern-skirmish-sensation-set-foot-in-europe/) · [Gamefound campaign page](https://gamefound.com/en/projects/enemy-spotted-studios/blackout) · [blkoutgame.com](https://www.blkoutgame.com/). (BoardGameGeek thread 3375078 was inaccessible — 403 — so not cited.)*

---

*Source: `z:/Downloads/BLKOUT-DIGITAL-RULE-BOOK.pdf` (Print 2nd Ed.) + `z:/Downloads/BLKOUT_Supplemental_4-26.pdf`. Read-through and analysis, 2026-07-22.*

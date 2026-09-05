# Equipment, Weapons & Armour — How the Research Corpus Does It

**A cross-game breakdown of every gear system in `research/`, `rules-vault/Research/`, `docs/POINTS-RESEARCH.md` and `docs/BLKOUT-RULES-ANALYSIS.md`.**

Compiled 2026-08-31. Covers **30 games**, of which **15 have a full equipment-layer breakdown** and 15 are shorter because their gear layer is genuinely thin or structural rather than under-read.

---

## 0 · How to read this

**Evidence tags carry through from the source notes.** `[FACT]` = quoted or closely paraphrased from a primary rulebook read; `[CONSENSUS]` = repeated community opinion, not a published number; `[INFERENCE]` = our own derivation; `[NOT FOUND]` = searched, absent — a real result, not a gap.

**Where the material came from.** The corpus splits three ways:

| Layer | Holds | Depth |
|---|---|---|
| `research/sources/<slug>/source.md` | Verbatim rulebook extractions — 12 games, ~2.2 MB | Primary; actual weapon/armour tables |
| `rules-vault/Research/Notes/*.md` | 32 curated analysis notes | Mechanism-level, cross-linked |
| `docs/POINTS-RESEARCH.md` §7 | ~25 games' costing profiles, 2,050 lines | Costing-first; the richest source for *pricing* gear |

**The known ceiling on this report.** Three named holes, stated up front rather than papered over:

- **Necromunda's Weapon Traits catalogue and Close Combat rules were never fetched** — the capture session hit a rate limit (`meta-core.json` → `pages_not_yet_fetched_for_core`). The Trading Post *structure* is fully captured; the per-trait effects are not. **[NOT FOUND]**
- **Trench Crusade's armoury is sourced from `POINTS-RESEARCH.md` §7.10, not a `source.md` capture** — it was read directly from the PDFs + BattleScribe `.cat` before the capture convention existed. Numbers are cross-checked between two sources but the raw extraction isn't in the repo.
- **Every Trench Crusade number is playtest-stamped.** Two revisions disagree. Treat the *structure* as the finding.

---

# PART ONE — THE CROSS-GAME MAP

## 1 · Six answers to "should gear cost anything?"

Every game in the corpus lands in one of six buckets. This is the single most useful frame in the report, because **the bucket a game picks determines almost everything else about its equipment layer.**

| # | Model | Games | What it buys | What it costs |
|---|---|---|---|---|
| **1** | **Full atomic pricing** — every item has a price, bought per model | Necromunda, Mordheim, Trench Crusade, Spectre Operations, Zona Alfa, Judge Dredd, Mad Dogs, Kill Team 2018, 40k 3rd–7th, Fallout (Caps), Bolt Action | Maximum expressiveness; a real armoury; loot has somewhere to go | Every item is a balance surface; context-dependence breaks the atom (§7.1) |
| **2** | **Slot capacity, no price** | Fistful of Lead, Kill Team 2024, Zona Alfa (slots *on top of* price), Gaslands (slots *and* price) | Unbreakable — slots can't be points-optimised; instantly learnable | Can't express "this model is kitted differently" at fine grain |
| **3** | **Free by default, priced at outliers** | 40k 11th ed (June 2026) | Removes the arithmetic without homogenising everything | Needs a live patch channel to keep working |
| **4** | **All free, fixed loadouts** | 40k 10th ed, Kill Team 2021 (models) | Zero arithmetic; no auto-take problem because there's no choice | You pay in **flavour** — profiles homogenise |
| **5** | **Baked into the unit's cost, never itemised** | Oathmark, Frostgrave/Stargrave, Rangers of Shadow Deep, Malifaux (mostly), Horizon Wars, BLKOUT | Nothing to balance at the item layer at all | The armoury stops being a game |
| **6** | **Two currencies, gear on the scarce one** | Infinity (SWC), Kill Team 2021 (10 Equipment Points), Trench Crusade (Glory items), Gaslands (build slots) | Force-multipliers can be cheap in points *and* rare | A second economy to teach and track |

### The load-bearing quotes

> **GW's stated reason for making wargear free was never fairness.** Robin Cruddace: per-item costs *"added to the complexity of working out your army, **for little gain regarding the actual output of the unit on the battlefield**."* **[FACT]**
>
> **The question is not "can we cost gear correctly?" but "is the cost of costing it worth what it buys?"**

> **And the price of free.** Goonhammer on 10th-ed Death Guard: *"flails and cleavers and maces are all just boring plague weapons/heavy plague weapons… **a bunch of the options don't matter any more**."* **[FACT]**
>
> **To make N options cost the same you must make them *worth* the same — so you homogenise the profiles. You cannot escape paying for differentiation: you pay in points arithmetic, or you pay in flavour.**

> **Kill Team states the sidegrade dependency plainly** **[CONSENSUS]**: *"If your operative has the choice between only a bolt pistol and plasma pistol, **there's no reason to ever not pick the plasma pistol** — the stronger option just always wins with no cost involved."* GW's answer was to remove the *choice* as well as the cost.
>
> **If you make something free, make it mandatory.**

---

## 2 · The acquisition matrix — how equipment actually gets into a player's hands

Nine distinct routes appear across the corpus. Most games use three or four.

| Route | Games | Mechanism |
|---|---|---|
| **Bought with the list-building currency** | Necromunda, Mordheim, Trench Crusade, Spectre, Judge Dredd, Mad Dogs, Bolt Action, Kill Team 2018 | Straight purchase at list-building or post-battle |
| **Bought with a *separate* campaign currency** | Zona Alfa (Zone Script ≠ Khrabrost'), Fallout (Caps ≠ Resources), Necromunda (Credits from Stash) | The battle-budget currency and the shopping currency are different numbers |
| **Rolled for — an availability gate, not a price gate** | Necromunda (Rare/Illegal `R#`/`I#`), Mordheim (Rare-item search + camp modifiers), Necromunda homebrew (rotating Trading Post generator) | You can afford it; can you *find* it? |
| **Capped per warband, breakable by loot** | Trench Crusade (`LIMIT: N`) | *"If you find more via looting/exploration, **you can break this limit**."* **[FACT]** |
| **Faction signing bonus + permanent discount** | Zona Alfa (six factions), Trench Crusade (faction economy rewrites) | Joining a faction hands you free starting gear and a standing % discount |
| **Looted off the board mid-scenario** | Zona Alfa (Hot Spot Salvage + Artifacts), Mordheim (Exploration chart), Necromunda (scenario rewards), Mad Dogs (Smash-and-Grab Loot objectives), Judge Dredd (cache markers) | Gear as an in-battle objective |
| **Unlocked by a settlement structure** | Fallout Homestead, Last Days (Refuge Perks), Necromunda (Outlander Structures), Oathmark (territory rarity gate) | Own the building → gain access to the gear tier |
| **Drawn as a card, not chosen** | Judge Dredd (Armoury cards, 6 dealt / keep 3), Fallout (Item deck draws) | Equipment is a hand of cards, not a shopping list |
| **Free, mandatory, or slot-allocated** | BLKOUT (Force Armory Combat Loads), Kill Team 2024 (4 slots), Fistful of Lead (2/3/4 slots), Oathmark (baked into unit cost) | No purchase step exists |

### Three acquisition mechanics worth naming separately

**Necromunda's Availability roll — access as a dice gate, not a count cap.** **[FACT]** Every Trading Post item carries an Availability Level: `C` Common (always buyable) · `R#` Rare · `I#` Illegal · `E` Exclusive (gang list only, never at the Trading Post). A **Seek Rare & Illegal Equipment** post-battle action rolls `2D6 + Leader Trading (+2) + each Champion Trading (+1) + 1 per full 10 Reputation`. Law Abiding gangs need ≥ Rare(X) for Rare and ≥ Illegal(X)+4 for Illegal; Outlaw gangs need ≥ X for either. **A successful roll opens the whole tier for that visit — no printed cap on how many copies you then buy.** The gate is *can you reach the tier at all this visit*, not *how many exist*.

**Trench Crusade's `LIMIT: N` — a purchasing cap that loot can exceed.** **[FACT, verbatim]** *"**LIMIT (X):** You can only purchase as many of this piece of equipment… as indicated by the number in parenthesis **for your warband**. **If you find more via looting/exploration, you can break this limit.**"* Persists across the whole campaign; **allies are exempt** (*"a mercenary's equipment never counts toward the LIMIT"*). This is the single cleverest access mechanic in the corpus: it constrains list-building without forbidding the narrative moment where you take the enemy's machine gun off the field.

**Judge Dredd's Armoury cards — equipment as a random hand.** **[FACT]** Deal **six** Armoury cards per player at game start; keep **three**, discard the rest. Cards are played on *any* friendly model, not assigned in advance. They cover grenades, special ammunition, respirators, Stealth Suits, BOING®, Mantraps and Seeker rounds. The design rationale is explicit: rather than ruling that Judges are simply immune to gas (they all have helmet respirators), the game requires an Armoury card to *use* a respirator — modelling "did you get the mask on in time" as a draw. **You cannot buy hand bombs at all; they exist only as single-use Armoury cards.**

---

## 3 · The gating matrix — who is allowed to take what

Nine distinct gating mechanisms, and most games stack two or three.

| Gate | Games | Example |
|---|---|---|
| **Rank / experience tier** | Zona Alfa, Spectre, Fistful of Lead, Necromunda, Settlements | Zona Alfa: Rookie 1 slot · Hardened 2 · Veteran 3 |
| **Faction list** | Necromunda (`E` Exclusive), Trench Crusade, Spectre (Militia vs Task Force), Judge Dredd, Infinity | Necromunda's `E` items never appear at the Trading Post at all |
| **Per-item purchase cap** | Trench Crusade (`LIMIT: N`), Warmachine (Field Allowance) | Automatic Rifle `LIMIT: 1`; Machine Gun `LIMIT: 2` |
| **Roster-slot cap (`0-N`)** | Trench Crusade, Warmachine, 40k Force Org | *"0-1 Death Commando"* |
| **Ratio cap (X in Y)** | Spectre Operations | *"Up to 1 in 3: may choose additional Weapons (MG, Launcher, Shotgun or Marksman Armoury)"* |
| **Force-value gate** | Trench Crusade | *"You may include 0-2 Artillery Witches in a warband worth more than 1000 ducats"* **[FACT]** |
| **Derived second budget** | Infinity (SWC), Kill Team 2021 (10 EP) | *"Each 50 Army Points will provide 1 point of SWC"* **[FACT]** |
| **Hands / slots / carrying capacity** | Judge Dredd (3 "hands", Judges get 4), Necromunda (3 weapons, `*` = 2 slots), Zona Alfa, Fistful of Lead, Gaslands | Physical capacity, unbuyable |
| **Skill/perk prerequisite** | Fallout Homestead, Zona Alfa (Bone Doc doubles Med-Kits per slot) | Armor Workbench *"Requires: Armorer perk"* |

### The three sharpest gating findings

**Infinity — the same weapon costs more SWC on a better platform.** **[FACT — N3 rulebook]**

| HMG carrier | SWC | Points |
|---|:--:|---:|
| Fusilier (line infantry) | 1 | 18 |
| Moblot / Govad | 1.5 | 29 |
| Janissary (Heavy Infantry) | 2 | 40 |
| Hsien (HI) | 2 | 61 |
| Squalo (TAG), MULTI HMG | 2 | 93 |

*Honest counter-example: the Missile Launcher is flat 1.5 on both a 15-point Fusilier and a 49-point Father-Knight. **Platform scaling is a strong designer habit, not a stated rule.*** And some profiles *grant* SWC rather than costing it — a Ghulam HMG is SWC 1, the Ghulam *Lieutenant* HMG is SWC 0.5, and **Joan of Arc as Lieutenant is +1 SWC: she pays you.** A negative price in a scarce currency is a sharper lever than any discount in the abundant one.

**Spectre Operations — the elite tier is gated by catalogue access, not by a bigger multiplier.** **[FACT — p.110]** *"Although the capability of Tier 2 and Tier 1 Elements are extremely high, **the access to some equipment is more limited than Veteran or Enlisted Elements**… This is intended to represent the roles these highly specialised units take in real life."* The observed effect: cheaper Veteran/Enlisted Elements crew the heavy weapons and vehicles, while expensive Tier 1 riflemen do the objective work. **Militia and Task Force share one Resources economy and one price ladder; what differs is which armoury page they can open.**

**Judge Dredd — signature weapons are free, everything else is priced.** **[FACT]** *"A Judge's primary personal weapons are their Lawgiver Mk2 Pistol, a Day Stick and, as a last resort, their Boot Knife. The Notoriety costs for Judges given above **includes the cost of these weapons**."* Judges also carry **four hands** of weapons instead of the standard three. Non-Judge factions start with *no* weapons at all and buy every one. **Faction identity is written as "what comes in the box price," not as a stat difference.**

---

## 4 · What armour actually does — nine different answers

This is where the corpus diverges most sharply. **Armour is emphatically not "just survivability" in half these games.**

| Game | Mechanism | Beyond survival? |
|---|---|---|
| **Zona Alfa** | Armor is a **stat** (0–7); the defender rolls `D10 ≤ Armor − Weapon Damage` to save. A passed save is a **Deflected Hit** — no wound, but a forced Will check that can leave a Pin. | **Yes.** Nearly every armour type also confers **Obscured Target** (a flat −1 to the shooter's Combat Ability, cumulative with cover). Advanced Armour and Exo Suits grant **an extra Armor Save die, choose best**. Mimetic Camo gives concealment in melee *and* ranged. Exo Suit gives **+2" Move** and **immunity to the Will check on Deflected Hits**. |
| **Spectre Operations** | Body armour **reduces the Lethality of a weapon by 1**, to a minimum of 10+. | **Yes, and it cuts both ways.** Wearing Body Armour **adds +1 die to an enemy's Scrutinise roll** against you when Covert, and a Trained searcher auto-detects any Covert model carrying armour. Heavy Body Armour reduces Frag Lethality by a further 1. An **EOD Suit** reduces Frag Lethality by **−3** but costs **−2 Movement**. **Ballistic Shields** reduce Lethality by −1 from the front only, and a Full Shield at 1-in-3 density grants the whole Element **+2 Situational Awareness**. |
| **Fallout: Wasteland Warfare** | Three **separate** Armor Ratings per model — physical / energy / radiation. Roll the red d12 Armor Dice (results 1–4); roll ≤ your rating and that much damage is blocked. Roll over and **nothing** is blocked. | **Yes, richly.** `3+1` notation = **Strong Armor**: the `+1` is always blocked regardless of the roll. **Armor Boost tokens** add temporary Strong Armor that burns off one icon per hit. **Armor Reduction icons** on the blue Effect Dice ignore rating points for that attack (but never the Strong Armor bonus). **Power Armor** has its own damage pool and a two-stage degrade. |
| **Judge Dredd** | Ballistic shell armour = **+1 Resist for +2 Notoriety**. Flat, one rung, one price. | No — but the game puts its texture in **Armoury cards** instead (Stealth Suit: +1 Evade and immunity to being spotted or Overwatched until you first attack). |
| **Mordheim** | Flat D6 save thresholds: **Light 6+ · Heavy 5+ · Ithilmar 5+ · Gromril 4+**, shield/buckler **+1**. Modified by attacker Strength (S4 −1 … S9+ −6). | Partly — Helmet (10gc) is a separate item that saves against stunning; a natural 6 to wound is a critical that often ignores armour entirely. |
| **Necromunda** | A **Save roll** in a four-roll chain (Hit → Wound → Save → Injury dice). **AP cancels it outright. One save only, regardless of how many armour types are worn.** | Yes — **Field armour** is a separate category that cover bonuses explicitly do *not* apply to. |
| **Trench Crusade** | Priced items in the same catalogue as weapons: Trench Shield 10 · Standard Armour 15 · **Reinforced Armour 40 (ELITE only)** · **Machine Armour 50 (`LIMIT: 1`, ELITE only)**. | Yes — the Glory tier holds armour that no ducat price can buy: **Damascus Armour (5 Glory) defeats armour-ignoring attacks.** |
| **Infected** *(RPG, thin source)* | **Hardness Rating**, an ordinal 0–5 ladder (Soft → Annihilating). The **margin between attacker and defender tier** decides everything: defender 2+ tiers above → **the attacker cannot deal damage at all**; attacker 2+ above → **the defender cannot absorb at all**. | It's the most aggressive armour design in the corpus: *"Handgun (HR 2) vs Humvee (HR 4) — The handgun can shoot at the humvee all day… **No damage is possible**."* **[FACT]** |
| **Fistful of Lead · Mad Dogs with Guns** | **There is none.** **[NOT FOUND — checked]** FoL's only "Armored" entry is a *mount* trait ("the mount is not taken Out of Action by the first hit"). Mad Dogs armours **cars** (+$500 Bulletproofing) and nothing else. | Two full commercial skirmish games with a persistent campaign and **no personal armour layer at all.** That is itself a finding. |
| **Oathmark** | Light/Heavy Armour appear in the `Equipment:` line of every profile, **with the cost already baked into the unit's points.** Defence is expressed through the **Shielding (X)** special ability (discard X of the attacker's Combat Dice). | Shielding cannot be used against flank/rear attacks — armour that is *directional* without a facing subsystem. |

### The two armour patterns worth stealing

**Armour that also hides you.** Zona Alfa's *Obscured Target* clause welds concealment onto nearly every armour tier, so buying armour buys **both** "harder to hurt" and "harder to hit" — normally two separate purchases. Spectre inverts the same idea: armour makes you **more** detectable when you're trying to pass as a civilian. Both are cheap, one-clause additions that stop armour being a pure survivability tax.

**Armour that trades a stat for protection.** Zona Alfa's Advanced Body Armour is `Armor 7 / −1" Move`; the Exo Suit is `Armor 7 / +2" Move` at a much higher price. Spectre's EOD Suit is `−3 Frag Lethality / −2 Movement`. **[INFERENCE]** In both games the drawback is what stops the top tier being an auto-take — the same "price the drawback" pattern Gaslands runs on weapons (§6).

---

## 5 · Consumables, one-shots, chems and drugs

Nine games have a genuine consumable layer. These are the mechanics most often missing from a corpus survey and they matter a lot for a scavenger-economy game.

| Game | Consumables | How they're limited |
|---|---|---|
| **Zona Alfa** | **Electric Juice** (meth + vodka: +2 Actions immediately, then only 1 Action next turn) · **Med-Kit** (replace 1 Wound with 2 Pins) · **Hot Load Ammo** (+1 Weapon Damage, one mission) · grenades (Frag/Smoke/Flash/Molotov/Satchel) | Grenades: **two free, no slot**; further pairs cost a slot. Med-Kits stack in slots. Fuse Cutter skill raises the grenade cap to three; Bone Doc doubles Med-Kits per slot. |
| **Fallout: WW** | **Chems**, **Alcohol**, **Food & Drink** (cooked variants are stronger and strip radiation), **Stimpaks** | Three **operational durations** — *Instant* / *Fixed* / *Diminishing* (the card physically slides under the unit card one step per activation until its bonuses are covered). **Only one diminishing effect per unit at a time.** **Addiction:** when an Addictive item's effect ends, roll a Special Effect die — on a match the card flips to its red side and the penalty is **permanent until cured**. |
| **Spectre Operations** | **Narcotics — Numbing** (never take Stress Tests, but at Stress 10 the Element collapses and is removed; no Reactions, no Rally, Awareness counts as 10) and **Stimulants** (+1 Awareness, +1 Move, free Assault Actions, reroll failed Stress dice — for 3 turns, then **+2 Stress**). **Cocktail:** taking both forces an **8+ Lethality roll per model**. Cost: **5r**. | Self-limiting by the downside; campaign rules carry lasting effects. |
| **Judge Dredd** | Every hand bomb (Hi-Ex, Incendiary, Concussion), special ammunition (Ricochet, Seeker, Hot Shot), Stealth Suit, respirator, BOING®, Mantrap | **Cannot be purchased at all.** They exist only as single-use Armoury cards, 3 held per game. |
| **Trench Crusade** | Molotov Cocktail 5 · Grenades 7 · Incendiary Grenades / Satchel Charge 15 · Medi-Kit 5 · **Martyrdom Pills (1 Glory, `LIMIT: 2`)** | `LIMIT: N` on the potent ones; Glory pricing on the ones that dodge the ducat ceiling. |
| **Fistful of Lead** | Dynamite (`d10+3"` throw, 3" Blast, detonates in hand on a natural 1) and the Gatling Gun | **Neither is purchasable.** *"The following weapons are not available for players to equip their Gangs with… but may be found during scenarios."* **[FACT]** |
| **Mad Dogs with Guns** | Grenades at **$25 each** | Priced like anything else; no separate consumable layer. |
| **Necromunda** | **Chems** are a first-class Trading Post category alongside Grenades and Booby Traps. **Out of Ammo attaches to the weapon, not the fighter** — a two-gun fighter can have one gun offline and keep fighting on the other. **[FACT]** | Availability roll; the Firepower dice forces an Ammo test on *every* ranged attack. |
| **Last Days** | **Ammo Tokens** accumulate per Rate-of-Fire point spent and check against the weapon's Reload Number; **they persist until the gun is actually reloaded.** Separately, **Noise Tokens** from the same trigger can summon a zombie on a 7+. | *"Unlike Noise Tokens, Ammo Tokens are only removed once a gun is reloaded."* **[FACT — p.53]** One action produces two consequences off one bookkeeping step. |

### The ammunition designs worth separating out

- **Spectre's specialist ammunition is bought per weapon and swapped per Engagement.** Incendiary (**10r**, AMR/HMG only — every glancing hit becomes a Crew Hit, +1 Stress) · Hollowpoint (**10r**, pistols/SMGs only — **+1 Lethality, but only if the target has no Body Armour**) · Shotgun **Slug** (10r — reroll a failed Lethality in CQB, reroll a failed Breaching roll) · Shotgun **Flechette** (15r — gains the Armour Piercing rule). *"Trained Elements with the appropriate weapons may choose to use Specialist Ammunition in any Engagement using that Weapon."* **[FACT]**
- **Zona Alfa's Hot Load Ammo is 350 ZS for +1 Damage, for one mission.** A pure consumable stat bump, priced roughly at the cost of a Med-Kit.
- **Zona Alfa's designer note on energy weapons is a whole balance philosophy in four lines** **[FACT]**: *"My solution to keep the game balanced is to grant powered versions of weapons increased Damage ratings but offset that by requiring a **Reload Action between each shot**… we have found it best to make such weapons **extremely rare and experimental**."*

---

## 6 · Weapon design — base profile + trait list, and where the texture lives

**Every game in the corpus that lets you distinguish weapons at all uses the same shape: a small base profile, plus a shared library of named traits.** What differs is who authors the combination.

| Game | Base profile | Trait library | Authored by |
|---|---|---|---|
| **BLKOUT** | `RANGE / DAMAGE` only. Hitting is the model's Skill; saving is the model's Armor `X/Y`. | ~20 USRs: AP(X), Auto(X), Cyclic, Heavy, Deployed, CQB, Medium, Seeking, Sustained(X), Blast(X), Indirect, Melee, Lethal, Smoke, EMP/Data Knife/Data Spike | **Designer.** Fixed unit cards; the player never builds a weapon. |
| **Spectre Operations** | Three range bands, each with `Range / Ballistics Modifier / Lethality / AP`. | Automatic, Suppressing, Sustained(X), Heavy, Deployed, Compact, Covert, Marksman, Single Fire, One Shot, Silent, Breaching(+X), AoE | Designer, with a **player-side build layer** (below). |
| **Zona Alfa** | `Range / Firepower / Damage`. Firepower = number of D10s. | Indirect Fire, Reload, Limited Ammo (5 rounds), Support Weapon (−1" Move), Crew Served (stationary), SBT/LBT, Flame Template, Burn | Designer, with an explicit **"tweak it if the other players agree"** clause. |
| **Judge Dredd** | `Short Range / Modifier / Long Range / Modifier / Power`. | Blast(X), Seeker, Ricochet, BOING®, Mantrap, Stun Pulse, Armour Piercing, Special Rounds | Designer + the Armoury card deck. |
| **Fistful of Lead** | `Short / Long` range and a Notes column. | Splatter, Blast, Burst, Entangle, Reload-after-every-shot, "out of weapon on a 1 or 2" | Designer. |
| **Trench Crusade** | Ducats + `LIMIT` + keywords (FIRE, SHRAPNEL, ASSAULT, CRITICAL, Ignore Shield) | Keywords double as **faction ban targets** (*"No weapon with the Keyword FIRE or SHRAPNEL"*) | Designer. |
| **Fallout: WW** | Damage value + colour-coded range bar + a **skill icon** (Pistol/Rifle/Heavy/Throw/Melee) that must match the model's card. | Slow Firing, Unique, Primed(X), Walked Fire, Area Effect (diameter = colour of the damage value), Mines, plus per-card **Special Effects** driven by the blue Effect Dice | Designer, plus a **Mod** layer the player attaches. |
| **Settlements** *(for contrast)* | Class sets **bands** (Damage floor/ceiling, range, hands, slots, min. rank); the weapon picks inside them. | Priced Characteristics | **Player.** `cost = class base + Damage steps + range + characteristics` |

### Spectre's Specialist Builds — the one player-side weapon-customisation layer in the corpus that isn't a full point-buy

**[FACT — pp.57]** *"A weapon may have up to **two (2) Build Options**… Builds must be chosen **before the mission begins**… Only **one** Build effect may be applied per Engagement."*

| Build | Eligible | Effect | Trade-off |
|---|---|---|---|
| **CQB** | Sidearms, Subguns, Shotguns, Assault LMGs, PDW/Short Rifles, Short Battle Rifles, .50 Rifles | Within CQB range: reroll one failed Accurate Fire **or** Lethality | None |
| **Mid-Range** | All Rifles except PDW, Machine Guns, DMR | Same, within Engagement range | None |
| **Long Range** | Long Rifles, Marksman Rifles, Machine Guns | Same, within Extreme range | None |
| **Night Fighter** | All ranged weapons | Ignore all NVG/Darkness penalties on Engagement | If the target *also* has NVGs, **they gain +1 Situational Awareness against you** |

**Cost: 10r each, Tier 1/2 only.** **[FACT — Task Force Armoury]**

**Why it's the best-shaped customisation layer here.** **[INFERENCE]** Builds don't stack, are locked before the game, and are **situational rather than static** — they buy a reroll in one range band, not a permanent modifier. That means a build cannot be stacked into an auto-take, and it makes the *same* weapon play differently on two models in the same squad without a second profile. It's a player-facing armoury with almost none of the combinatorial balance surface a full point-buy carries.

### Gaslands' BFG — price the drawback, not the number

**[FACT]** **The biggest gun in the game costs 1 can.** Because it eats **3 build slots**, has **Ammo 1**, and firing it **shoves you backwards, drops you to Gear 1, and adds 3 Hazard tokens**.

| Chassis | Cans / Slots | | Weapon | Cans / Slots |
|---|---|---|---|---|
| Bike | 5 / 1 | | Machine Gun | 2 / 1 |
| Car | 12 / 2 | | Minigun | 5 / 1 |
| Truck | 15 / 3 | | Rockets | 5 / 2 |
| Bus | 30 / 3 | | 125mm Cannon | 6 / 3 |
| Tank | 40 / 4 | | **BFG** | **1 / 3** |
| War Rig | 40 / 5 | | Armour Plating (+2 Hull) | 4 / 1 |

Plus two pressure valves: a **zero-slot category** (Extra Crewmember 4 cans / 0 slots, capped at 2× starting Crew; Nitro Booster 6 / 0) so you can keep spending cans after slots run out, and a **multiplicative mount** — **Turret = ×3 the weapon's cost** — which stays proportionate on a 2-can MG and a 6-can cannon alike. **Crew-fired weapons cost 0 slots.**

**And the published inverse.** **[INFERENCE from FACT]** Armour Plating = +2 Hull for 4 cans; the Prison Car errata reads *"Reduce the cost of this vehicle by 4 Cans… Reduce the hull value of this vehicle by 2."* → **1 Hull ≈ 2 cans, stated consistently in both directions.** Notably, that rate does **not** govern chassis costs — **chassis and add-ons sit on different price scales and the game is fine.**

---

## 7 · Drones, turrets, deployables and vehicles

The corpus is thinner here than on weapons, but five games have real material.

| Game | Drones / robots | Turrets & emplacements | Vehicles |
|---|---|---|---|
| **Spectre Operations** | **M-UAV** (M8/B7/A4/**S0**) and **UGV** (M7/B6/A7/**S0**) are full Elements — they generate Momentum, Manoeuvre and Engage like anyone else, with **one exception: *"Drones do not gain Stress or confer any Stress to their Parent Element."*** **[FACT — p.80]** Engaging an M-UAV always counts as **Extreme Range** unless using an Anti-Drone Weapon. When rolling Lethality against Drones, the drone benefits from the **Body Armour** rule. | **Emplaced Weapons** are a separate armoury page requiring a 2-model Element: SPG9 HEAT/HE **90r**, M40 HEAT **120r**, Light Guided AT Launcher **120r**. The **Deployed** trait costs 1 Momentum to pack down and 1 to deploy, and needs 2 models to carry. | Full vehicle armoury with **base cost + weapon mount slots**: Technical 75r (1× Light/Med/Heavy), Armoured Pickup 100r, MRAP 200r (0–2 mounts), HMV 120r, Dagger 120r. Light/Heavy **RWS mount systems** are priced separately. |
| **Fallout: WW** | **Automatrons** — *"an Automatron's Unit card consists of **3 cards: Head, Torso and Legs**"* laid side by side with S.P.E.C.I.A.L. rows aligned. **Pricing has no formula at all: *"The caps cost of an Automatron is the total of all the cards used to construct and equip it including weapons."*** AI is composited too — *"the AI card that matches the Automatron's Head,"* with one stated fallback. **[FACT]** **Clunky** robots take a flat **−20% Caps** and roll an extra activation die that can add a beneficial or harmful token. | **Turrets never activate.** They start each round with the Reaction Markers printed on their weapon card, are aware at **double Awareness range**, *"react to every Trigger they are aware of **regardless of faction**,"* count as no unit for objectives, and can never be moved once placed. **[FACT — p.52]** Adding a Turret to a Settlement costs **5× its Caps cost in a Force.** | Not covered in this capture. |
| **BLKOUT** | Force Armory pulls (Combat Loads), Exterminator/Gull/Whistler mercenary drones on the BLKLIST. | — | **Two damage tracks — Chassis and Mobility** (the shooter picks which to target; kill Mobility to immobilise, fill Chassis to destroy). Straight-line movement, can't React, can **run over** infantry, `Transport (X)`. Destroyed by a **Blast** weapon → **Explodes**, killing everyone aboard. **Dusters** (mechs) rotate 360°, can Fight in CQC, can Juke, and take **+1 Damage from the rear arc**. |
| **Judge Dredd** | Robots are a **keyword, not a subsystem**: *"Robots can only generate normal Action chips, never Star chips… Robots are also unaffected by Psi Skills."* That is the entire mechanical footprint, repeated verbatim on every robot profile. **[FACT — p.110]** | **Auto-Turret** upgrade: fixed **+3 Notoriety**, starts each turn in Overwatch, fires without a crew — and **malfunctions on a roll of 1 if a friendly model crosses its arc, firing on them anyway.** **[FACT]** **Placed Guns price their firing arc as a percentage surcharge on the weapon underneath**: Forward focused **+25%** · Forward **+50%** · All round **+100%**, rounded up. | Grav pod / Sky cycle 9–11, Ground pod / block buggy 16, Hover van 19 Notoriety. |
| **Zona Alfa** | No drone rules as such, but **suggested Armor Ratings** are published so you can field them: Small Drone or Robot **Armor 3** · human-sized robot **4** · truck/jeep **4–6** · Light Walker / Piloted Exo Suit / IFV **6–7**, possibly two Wounds. **[FACT]** | Crew Served weapons (HMG, Mortar) are **stationary positions with no movement possible**, min. 2 crew, 4,000 ZS. | Explicitly out of scope beyond light vehicles. |
| **Infinity** | **Repeaters and Deployable Repeaters** (`Disposable (3)`) — a network relay **either side can use**, at a printed **−3 Firewall** penalty. *"There can be no reaction against a Repeater that is being used by an enemy Hacker, only against the Hacker."* **[FACT]** | — | **TAGs** can be possessed outright via **Total Control**, guarded by four stacked constraints (TAG-only scope; a **generic, worse-than-native replacement profile** `MOV 4-4 / CC 13 / BS 12 / WIP 11`; **zero VP for either side**; and a 1-Command-Token unconditional cancel). |

### Spectre's counter-tech is priced as deliberately as the tech

**[FACT]** Both sides of the drone problem are named items with prices: **Anti-Drone gun 50r** (Militia Specialist Armoury) and **Cope Cage** — slat armour bolted to a vehicle roof *"to defend against drone attacks that usually crash into or detonate on the upper hull."* Electronic warfare stacks on top: an **IED Jammer (10r)** blocks detonation within 3"; a **Tactical EW System** blocks the enemy Commander's Escalation Requests and negates their Comms bonuses entirely; **Hardened Comms (10r)** is the priced immunity to all of it — *"Immune to the effects of Electronic Warfare Devices… Cannot have their Momentum, Escalation attempts, or communications disrupted by enemy EW actions or Hacking."*

---

## 8 · The five failure modes the corpus documents

Each of these is a *shipped, published* failure, not a hypothetical.

**1 · Context-dependence kills the atom.** **[FACT — 4th-ed Codex: Space Marines, read from archive scans]**

| Weapon | Tactical Squad | Command Squad | Spread |
|---|---|---|---|
| Heavy bolter | +5 | **+15** | **3×** |
| Multi-melta | +10 | **+20** | 2.5× |
| Lascannon | +15 | **+35** | 2.33× |

The same gun, in one book, at up to 3× the price — because the number was really pricing the **slot**, not the gun. Flamers and meltaguns were flat everywhere, so **the inconsistency wasn't even systematic**. 8th edition kept *principled* exceptions (heavy bolter 8 pts for BS4+ Guard vs 10 for BS3+ Marines), which proves the deeper point: **a weapon's value is a function of its platform, so a global weapon price list is a category error.** Once an atom needs context-dependent prices it has stopped being an atom — and has kept all the bookkeeping.

**2 · Flat weapon prices on quality-priced bodies create an arbitrage.** **[FACT/CONSENSUS — Bolt Action]** Bodies cost 7 / 10 / 13 by troop quality; weapons cost the same regardless of carrier. Result: *"You should never take anything other than Inexperienced mortars — you need 6s to hit anyway."* **When a weapon's performance is independent of the carrier's quality, paying the veteran body tax is pure waste.** 3rd edition's fix was **to change the rules, not the price** — giving veteran vehicles a mechanical benefit they previously lacked.

**3 · Coarse atoms in a tight budget is the worst combination.** **[FACT + INFERENCE]** Kill Team 2018 ran a **100-point cap with per-item wargear costs**. Every item was a large fraction of the budget, so a small mispricing was decisive. Contemporary verdict **[CONSENSUS]**: *"Despite the complex lists and fiddly point values the teams devised were terribly unbalanced, with certain factions dominating others."*

**4 · An upgrade written to patch a weak unit lands on auto-take by construction.** **[CONSENSUS — Malifaux designers on removing Emissary upgrades]** They *"were generally used as patches to sub-par Masters and were either **not impressive enough to see the table or so strong that they became mandatory hires**."* **[INFERENCE]** This is the atomic-costing failure mode in its purest form: a costed option collapses into "never taken" or "auto-taken," and the band between is narrow. **The real fix was structural — fold auto-take content into the base card so it stops being a purchase decision at all.**

**5 · Escalating per-item costs can price a unit out of its own identity.** **[FACT — Goonhammer on T'au, 9th ed]** *"It was very easy — especially with 9th's **escalating points costs for duplicating weapons on the same model** — to price a unit out of its usefulness."* Per-item costing had reached the point where equipping a unit with its own signature weapons made it unplayable.

**And the one nobody has solved with points at all.** **[FACT — BattleTech]** Weapons dealing 60+ damage get a flat **20% BV bonus** — so the AC/20 pays a threshold premium and the AC/10 pays nothing, with no gradation between. **Every game examined solves thresholds by hard cap, hard gate, or removal — never by charging more.**

---

## 9 · The eleven mechanics most worth stealing, ranked

1. **`LIMIT: N` printed beside the price, capping *purchase* not possession, breakable by loot** — Trench Crusade. Two orthogonal dials mean you can fix "too strong" without making it unaffordable, and "too common" without making it weak.
2. **Availability as a roll-gate that improves with reputation and rank** — Necromunda. Rewards an established gang for being established; the trade-off is table variance and a "not this visit" result.
3. **Slots for the long tail, real prices for what carries the game** — Kill Team 2024 + Gaslands + Zona Alfa. Slots can't be points-optimised and can't be bought.
4. **Price the drawback, not the number** — Gaslands' BFG. Put a spectacular toy in the game and charge for it in *consequences* rather than points.
5. **Free by default, priced only at proven outliers, rebased so the default is points-neutral** — 40k 11th ed. The compromise a company reached after trying both extremes.
6. **The same gun costs more on a better platform** — Infinity SWC, GW's VDR (Heavy Bolter +20 at BS4 / +15 at BS3), One Page Rules (`Weapon Cost × Quality`). Three implementations, one conclusion: **multiply the things that multiply.**
7. **Modular units priced as the plain sum of their parts** — Fallout's Automatron. Three interchangeable cards; no multiplier, no synergy tax, no new pricing machinery. Conditional on the parts being roughly commensurable.
8. **A named cheap-and-unreliable tier** — Fallout's **Clunky** (−20% Caps, one extra activation die that can help or hurt). *"Cheaper and worse" doesn't have to mean fewer stat points.*
9. **Two build options per weapon, situational not static, locked before the game** — Spectre's Specialist Builds. Player-facing customisation with almost no combinatorial balance surface.
10. **Capturability as a weapon property** — Judge Dredd's **Stun/Injury fork**. A knockout tagged Stun-only routes to arrest; any Injury marker routes to a death roll. **A crew can choose a no-kill loadout at list-building and the resolution honours it at the point of impact.**
11. **A settlement structure that owns its unlock** — Last Days: *"Stable (20 SP) unlocks 0–2 Horses at 15 SP each, and **losing the Stable removes the Horses from the roster**."* Fallout's Homestead does the same with Workbenches gated behind perks. **Capability is leased, not bought outright** — which is what gives raids on a settlement a target that isn't a body.

---
---

# PART TWO — PER-GAME BREAKDOWN

The fifteen games with a real equipment layer, longest first. Thin/structural systems follow in §25–30.

---

## 10 · Necromunda — the deepest armoury in the genre

*Games Workshop, 1995 Living Rulebook + N23 Core Rulebook. Read via NecroRAW, cross-checked page-for-page against both primary books.*

**Currency.** **Credits.** Campaign gangs start at **1,000 credits**; skirmish play is an agreed budget, guideline 1,250–2,000. If vehicles are used, **+400 credits ring-fenced** to Mounted-condition wargear, Crew, and vehicles — **unspent allowance from that pool is lost, not banked.** **[FACT]**

**The two-number ledger — and it holds across 28 years.** **[FACT — four independent statements]**

> N23: *"**Gang Rating** — the total cost of all of the fighters and vehicles in the gang, including the cost of all the equipment and Upgrades **they are equipped with**."*
> N23: *"**Wealth** — …plus the value of any credits or equipment they have in their **Stash**."*
> 1995: *"Any weaponry or other equipment that the gang keeps but does not give to a fighter is hoarded… **its value is not included in the gang rating**."*

**Ownership is wealth; rating is fielded power.** 1995 had one number with a stash carve-out; N23 promoted the excluded pile to its own tracked stat. This is what makes underdog banding work at all — a gang that loses fighters must not keep the rating of the gear those fighters carried.

**Carrying capacity.** 3 weapons per fighter on foot, 2 if Mounted. Weapons marked `*` take **2 of the 3 slots**. Vehicle Crew: 2 weapons max, gaining the Arc (Front) trait. **Tools of the Trade** lets one model have multiple "Equipment Sets" (alternate Fighter cards) at no extra cost — only one is used per battle, drawn at random if the scenario randomises.

**The Trading Post.** ~20 category pages: Basic / Pistol / Special / Heavy / Power Pack / Close Combat Weapons · Grenades · Booby Traps · **Armour** · **Field Armour** · **Bionics** · Gang / Personal / Spyrer Equipment · **Chems** · **Weapon Accessories** · Status Items · Vehicle Upgrades & Wargear · Special Terrain. Plus three book-specific Appendices (Badzones, Black Market, Book of Ruin).

**Access is a roll, not a cap.** Every item carries an **Availability Level**: `C` Common · `R#` Rare · `I#` Illegal · `E` **Exclusive** (gang list only, *never* purchasable at the Trading Post). The **Seek Rare & Illegal Equipment** post-battle action rolls `2D6 + Leader Trading(+2) + each Champion Trading(+1) + 1 per full 10 Reputation`. Law Abiding: ≥ Rare(X), or ≥ Illegal(X)+4. Outlaw: ≥ X for either. **One successful roll opens the whole tier for that visit, uncapped.**

**Four footnote symbols, which is itself a warning.** `*` two-slot weapon · `†` mutually exclusive with other `†` accessories on the same weapon · `♦` a different price applies via the fighter's own gang list (Trading Post price is reference-only) · `^` sourced from a book-specific appendix, arbitrator's discretion. **A notation that needs four symbols to stay navigable is a symptom of the fragmentation NecroRAW exists to fix.**

**Combat chain — four to five rolls to land one casualty.** Hit roll (BS test, stacking −1/−2 modifiers) → **Wound roll** (D6 against a five-row Strength-vs-Toughness table) → **Save roll** (armour-dependent; **AP can cancel it outright; one save only regardless of how many armour types are worn**) → **Injury dice** (three-symbol die: Out of Action / Serious Injury / Flesh Wound) → in campaign, the **Lasting Injury D66**. Cover grants a Save bonus (+1 partial / +2 full) that **does not apply to Field armour**. **[FACT]**

**The Firepower dice runs the ammo economy.** Rolled on *every* ranged attack regardless of the hit outcome; an Ammo symbol forces an immediate Ammo test or the weapon goes Out of Ammo.

**Conditions live on the item, not just the model.** **[FACT]** *"Unlike other Conditions, **Out of Ammo is applied to a weapon carried by a model rather than the model themselves**. It is therefore possible for a model to have multiple Out of Ammo markers on them at one time."* A two-weapon fighter can keep functioning on their sidearm while the primary is offline — no parallel "half-suppressed" model state required.

**Equipment through the campaign layer.** One of the five Territory **Boon** types is literally **Equipment** (added to Stash). *Archaeotech Device* / *Tech Bazaar* (Van Saar) grants **free weapon Traits** — Blaze, Rad-phage, Seismic, Shock, plus Unstable — and a **Haggle** post-battle action for cut-price Rare gear. A **Black Market** Structure in the Outlander settlement *"Reduce[s] Legality of all Black Market items by 2"* for `5 Power, 10 Salvage, Scrap Market`. **Alignment gates the shop**: Law Abiding gangs get free Trading Post access and restricted Black Market; Outlaw gangs get the exact mirror.

**Post-battle order matters.** Step 6 of the seven-step sequence runs **Clean House → Visit the Trading Post → Territory Boons → Distribute Equipment → Purchase Advancements → Update Gang Rating** — with the Rating update **deliberately last**, so every earlier decision reads a stable, frozen number.

> **[NOT FOUND]** The full Weapon Traits catalogue, the Skills catalogue and the Close Combat resolution pages were identified but not fetched (rate limit). This is the largest single hole in the corpus's equipment coverage.

---

## 11 · Trench Crusade — two dials on every line

*Tuomas Pirinen (Mordheim), Mike Franchina, James Sherriff. v1.6.3 playtest PDFs + the community BattleScribe `.cat`, in agreement on every item.* ⚠️ **Every page is stamped PLAYTEST. Two revisions disagree on numbers.**

**Currency.** **Gold Ducats** (campaign warband starts at **700**) + **Glory Points**, which *cannot be bought* — *"the only way to attract their services is to perform glorious deeds on the battlefield."* **[FACT]**

**The full New Antioch armoury** **[FACT — v1.6.3, agrees with the `.cat`]**

| Ranged | Ducats | LIMIT | | Melee | Ducats | LIMIT |
|---|---:|---|---|---|---:|---|
| Molotov Cocktail | 5 | — | | Trench Knife | 1 | — |
| Pistol | 6 | — | | Bayonet | 2 | — |
| Grenades | 7 | — | | Trench Club | 3 | — |
| Bolt Action Rifle · Shotgun | 10 | — | | Sword/Axe | 4 | — |
| Semi-Auto Rifle · Auto Shotgun | 15 | — / 2 | | Shotel | 5 | — |
| Incendiary Grenades · Satchel Charge | 15 | 2 / 3 | | Polearm | 7 | — |
| Heavy Shotgun · Automatic Pistol | 20 | 2 / 3 | | Great Hammer/Maul | 10 | — |
| SMG · Grenade Launcher · Flamethrower | 30 | 2 / 2 / 3 | | Great Sword/Axe | 12 | — |
| Sniper Rifle | 35 | 3 | | Lochaber Axe · Misericordia | 15 | — / 1 |
| Automatic Rifle | 40 | **1** | | Tank-Splitter Sword | 15 | 3 |
| Machine Gun | 50 | 2 | | | | |
| Heavy Flamethrower | 55 | **1** | | | | |

**Armour and kit.** Trench Shield 10 · Standard Armour 15 · **Reinforced Armour 40 (ELITE only)** · **Machine Armour 50 (`LIMIT: 1`, ELITE only)** · Gas Mask / Shovel / Medi-Kit / Helmet **5 each** · Musician's Instrument 15 (`LIMIT: 1`). **Glory-only:** Troop Flag 1 · **Martyrdom Pills 1 (`LIMIT: 2`)** · Field Shrine 2 · **Damascus Armour 5 (defeats armour-ignoring attacks)** · Locust Spitter 6 (chains between targets) · **Beelzebub's Embrace 20 (removes a model from the game outright)**.

**The errata prove price and cap are independent dials.** **[FACT — V1.4 Change List]** *"Viscera Cannon: **Cost** reduced to 50 ducats"* (price) · *"Grenade Launcher: New **LIMIT: 2**"* (cap) · *"Black Grail Musician's Instrument: **Cost 15 ducats. LIMIT: 1**"* (both, together).

**Four gating dials in total**, all running at once: **price** · **`LIMIT: N`** (per-warband purchase cap) · **`0-N`** (roster slots) · **value-gated caps** (*"0-2 Artillery Witches in a warband worth more than 1000 ducats"*).

**Melee costs are built; ranged costs are eyeballed.** **[INFERENCE, working shown]** Taking Trench Club (3, one-handed, no modifiers) as baseline: CRITICAL **+1** (Sword/Axe 4), Ignore Shield **+1** (Shotel 5), anti-charge **≈+4** (Polearm 7). Two out-of-sample predictions, both exact:

- **Great Sword/Axe** = Great Hammer 10 + CRITICAL 1 + "+1D Injury" 1 = **12**. Published: **12** ✔
- **Lochaber Axe** = Great Hammer 10 + CRITICAL 1 + anti-charge 4 = **15**. Published: **15** ✔

Ranged has exactly one clean increment (**ASSAULT = +5**, on two independent pairs) and then collapses: the second attack costs **+25**, the third about **+15** — *decreasing* marginal cost, which no additive formula produces. **Range isn't priced at all** — the Flamethrower (8") is 30 and the Sniper Rifle (48") is 35. **The variable that actually predicts ranged cost is `LIMIT`**: every weapon at 30+ ducats carries one; nothing at 15 or below does.

**And the clincher against any universal formula.** **[FACT]** *The same profile is priced in different currencies for different factions.* Automatic Rifle = **40 ducats (`LIMIT: 1`)** for New Antioch and **2 Glory (`LIMIT: 2`)** for the Heretic Legion. Submachine Gun = 30 ducats / 2 Glory / 25 ducats depending on faction and variant. Martyrdom Pills = 1 Glory (New Antioch) or 20 ducats (Trench Pilgrims). **No function of range, dice and keywords outputs both "40 ducats" and "2 Glory" for one identical profile. Currency choice *is* the balancing lever.**

**Faction rules rewrite the price list itself.** **[FACT]**

| Variant | Economic rule |
|---|---|
| Knights of Avarice | *"no models that cost less than **80 ducats** (including their equipment)"* — a **minimum** model cost; plus banned keywords (*"No weapon with the Keyword FIRE or SHRAPNEL"*) and a cross-faction unlock of one weapon/armour/equipment type from two other lists |
| Papal States | Recruited with *"**500 ducats and 11 Glory Points**"*; Threshold at −200 ducats; +4 Glory on every Reinforcement |
| Procession of the Sacred Affliction | Holy Icon Shields become **20 ducats and universal** instead of 2 Glory and ELITE-only |
| House of Wisdom | *"treats Alchemist Armour as if they had a **LIMIT of 2**"* |
| Heretic Wretched | *"None of their weapons, armour or equipment can cost more than **10 ducats** each"* — a per-model spend ceiling; uniquely, they sell back at **full** value |

**Universal floor rules.** Sale value is **half base, rounding up**, *"including Glory Items."* **Death destroys gear** — *"It is not possible to reallocate fallen warriors' weapons or equipment once they die."* Loot income is **10 × Exploration Score in ducats**. To rebuild to Threshold you must *"Give up/Sell **all Weapons, Armour and Equipment that is not assigned to any of your models**"* — so the rubber-band explicitly liquidates your armoury.

---

## 12 · Spectre Operations — the deepest modern-military kit list in the corpus

*Stephen May, Spectre Miniatures. 3rd Ed Revised 07-25 (143pp) + Errata (5pp) + Solo Rules (5pp), all read in full.*

**Currency.** **Resources (r)**, one economy shared by Militia and Task Force. Model cost by training tier: Militia rifleman **20r** · Enlisted **30r** · Veteran **40r** · Tier 2 **50r** · Tier 1 **60r**, up to **80r** for a Tier 1 Support specialist. Sergeant upgrade **+10r**.

**Weapon profile.** Three range bands (CQB / Engagement / Extreme), each carrying `Range / Ballistics Modifier / Lethality / AP`. CQB is a fixed 6" for every weapon. **A blank Extreme value means unlimited range** (sniper rifles). Example **[FACT — p.37]**:

```
Pistol         6"/+1/7+/1   ·  10"/0/8+/1    ·  16"/-2/10+/0   Compact, Covert
Heavy Pistol   6"/0/4+/1    ·  10"/-1/7+/1   ·  16"/-3/8+/0    Compact
Machine Pistol 6"/+1/6+/1   ·  8"/-1/9+/1    ·  16"/-3/10+/0   Automatic
```

**Militia Armoury (selected)** **[FACT]**

| Rifles | | Marksman | | Machine Guns | | Launchers | |
|---|---:|---|---:|---|---:|---|---:|
| Medium Rifle | 10r | DMR | 30r | Assault LMG | 24r | Grenade Launcher | 25r |
| Bolt Action Rifle | 20r | Medium Sniper | 40r | LMG | 30r | RPG HEAT | 28r |
| Short Rifle | 25r | Heavy Sniper | 50r | MMG / Pack Fed LMG | 35r | RPG Frag | 36r |
| Long Rifle | 28r | | | Medium MG | 38r | RPG Thermobaric | 45r |
| Battle Rifle | 30r | | | HMG | 50r | RPG Tandem | 70r |

| Sidearms | | SMGs | | Shotguns | | Thrown | |
|---|---:|---|---:|---|---:|---|---:|
| Pistol | 5r | Compact SMG | 20r | Sawn-Off | 5r | Smoke Grenade | 5r |
| Heavy Pistol | 8r | SMG | 25r | Shotgun | 12r | Flash Grenade | 15r |
| Machine Pistol | 10r | | | Combat Shotgun | 16r | Molotov | 20r |
| Close Combat Weapon | 5r | | | Automatic Shotgun | 24r | Frag Grenade | 30r |

**Specialist Armoury:** Flamethrower 60r · **Anti-Drone gun 50r** · **Anti-Personnel/Armour Drone 50r** · Multi-Grenade Launcher 50r · Light Recoilless Rifle 40r · Unguided AT Launcher 80r · Anti-Material Rifle 75r · Short Battle Rifle 25r. **Emplaced (2-model Element required):** SPG9 90r · M40 HEAT 120r · Light Guided AT 120r.

**Equipment prices** **[FACT]**

| Militia | | Task Force adds | | Tier 1/2 only | |
|---|---:|---|---:|---|---:|
| **Body Armour** | **10r** | Heavy Body Armour | 28r | Augmented Reality | 15r |
| Narcotics | 5r | Suppressor | 10r | Night Vision MK3 | 15r |
| Lock Pick | 4r | Night Vision MK1 / MK2 | 5r / 10r | **Hyper-Aware Operator Suite** | **40r** |
| IED Switch | 12r | Thermal Optic | 32r | Hybrid NVG+Thermal Goggles | 20r |
| Ballistic Shield Half/Full | 12r / 25r | Range Finder | 15r | **CQB / Mid / Long Rifle Build** | **10r each** |
| Breaching Hard/Explosive/Electronic | 8r / 10r / 15r | Ghillie Suit | 30r | Covert Body Armour | 15r |
| CBRN Suit | 10r | Gunfire Detector | 10r | **Exoskeleton** | **30r** |
| Respirator Short / Long | 10r / 18r | Hardened Comms | 10r | **Thermal Camo** | **40r** |
| Bomb Vest | 20r | IED Jammer | 10r | | |
| Trained Dog | 30r | K9 Advanced Command | 10r | | |
| Long Range Comms | 20r | Laser Designator | 5r | Spotter Scope | 10r |

**Night vision is a three-rung ladder with explicit costs on every rung.** **[FACT]**

| NVG | Darkness removed | Limitations while equipped |
|---|---|---|
| **MK1** | LoS/Detection limits in Darkness | Max **1** Momentum for Manoeuvre · Engagements **−1 Ballistics** · reduced FoF (45°) remains |
| **MK2** | as MK1 | Max **2** Momentum · −1 Ballistics · reduced FoF remains |
| **MK3** | **all** Darkness penalties | −1 Ballistics · **full FoF (90°) restored** |

**Thermal Optics** ignore all Cover bonuses to Situational Awareness, grant **+3 Awareness** to detect Hidden/Undetected/Covert Elements or locate Traps/IEDs, and function in Pitch Black or Dense Smoke — but **do not remove Darkness movement/engagement penalties on their own**. **AR devices** give +1 Awareness on Engagements, +3 on detecting Hidden/IEDs, +2 on Scrutinising Covert Elements, and ignore all Cover modifiers to SA. The **A.I. Target Recognition Suite** gives **+4 Awareness on a Scrutinise action, replacing the usual modifiers**. The **Hyper-Aware Operator Suite** bundles AR + AI + Thermal + Comms + Smart Optic, sets **Field of Fire to 180° regardless of light**, and explicitly *"does not stack beyond its listed bonuses, even if other gear is present."*

**Stacking rules are printed, which most games skip.** **[FACT]** *"Thermal + NVGs: May stack, but only one 'type' of vision bonus may apply to each individual test. Awareness modifiers from optics and build options **do** stack. Engagement modifiers from NVGs and weapon builds **do not** stack unless specifically allowed."*

**Suppressors are the sharpest single item in the corpus.** **[FACT — p.87]** *"If an **Unsuppressed** Weapon is used: **All enemy Elements become Alert immediately. No Awareness Test required.**"* Suppressed weapons instead give nearby Elements a *chance* to hear, scaled by range (CQB +3 / Engagement +2 / Extreme +1 to the listening roll), and reduce the target's Situational Awareness by −1. **Integrally Suppressed** weapons *"suffer no penalty to detection."* A **10r** purchase converts a binary auto-fail into a roll.

**Breaching tools price noise against effectiveness.** **[FACT]** Hard Entry (sledgehammer, bolt cutters, saw) **+4** to Breaching, **Alerts everyone within 8"** · Explosive Entry **+6**, Alerts within **12"** · Electronic Entry **+5** to Breaching *or* Hacking, and *"if the test is failed and a 1 is rolled a system alert is activated"* · **Lock Pick** **+2** on the first attempt, **+1 per extra Momentum**, and *"this method of entry is **silent** and will not require a test for Detection."*

**Camouflage counters optics directly.** Ghillie Suit (30r): while entirely within scenery, **reduce a Detecting Element's Awareness by −2**. **Thermal Camo** (40r): *"When attempting to Detect or make an Engagement Action against the wearer of Thermal Camo, **benefits for Thermal Imagers are negated**."*

**Explosives are a two-part system.** An **IED Device** is hidden in a named scenery item (the player marks it, photographs it, or places a model). An **IED Switch (12r)** — *"often as simple as a cell phone"* — triggers it as an Action (1 Momentum) or as a Reaction when an enemy moves within 3". A **Bomb Vest (20r)** uses the same switch; if detonated, *"that model is automatically removed as a Casualty."*

**Dogs are a costed, statted unit with three actions.** Trained Dog **30r** (`M7 B0 A5* S3`), Untrained (`M7 B0 A6* S5`). One of Manoeuvre (never >12" from the Handler), **Investigate** (Awareness test — success detects all undetected Elements within 9"), or **Attack** (*"If the Model is killed, roll a D10, on a 6+ the attack was silent"*). **K9 Advanced Command (10r)** removes the leash distance entirely. Untrained dogs must pass a Stress Test to act at all and on a roll of 1 *"attack the closest model within their Movement value, friend or foe."*

---

## 13 · Zona Alfa — the cleanest complete scavenger armoury

*Patrick Todoroff, Osprey 2020. Full 65-page rulebook read.*

**Two economies that never touch.** Force-building uses **Khrabrost' (K)** = the sum of Actions across the crew (Veteran 3 / Hardened 2 / Rookie 1); a starting crew has 12 K. Shopping uses **Zone Script (ZS)**, converted from Salvage at a **10% Trader cut**. *"The Zone's economy is set at the 'AK Standard': the fixed exchange rate for a working AK-47."* **[FACT]**

> **⚠️ And this is the system's own admitted hole.** **[INFERENCE — read directly from the recruitment rules; no gear-cost adjustment is stated anywhere]** **Khrabrost' is gear-blind.** *A Veteran with an RPG, NODs and Kevlar costs exactly the same 3 K as a Veteran with a knife.* It's the same "everyone gets N slots" trap Kill Team 2018 hit; Zona Alfa simply never tries to solve it, because a 12–16 K pickup game is too short for anyone to optimise that hard. **It would not survive a campaign-length gear gap.**

**Weapons — deliberately coarse categories, WYSIWYG-statted.** *"Zona Alfa does not differentiate between types of Assault Rifles (AK74 vs Vintorez VSS) or handguns… Weapon and Armor types are broad, catch-all categories."* Stats are `Range / Firepower (number of D10s) / Damage`.

| Melee & Sidearm | Range | FP | Dmg | | Support | Range | FP | Dmg | Special |
|---|---|:--:|:--:|---|---|---|:--:|---|---|
| Knife, Claws/Teeth | Melee | 1 | 0 | | Flamethrower | Flame Template | — | 3/model | Limited Ammo, Support, **Burn** |
| Machete | Melee | 1 | 1 | | 40mm GL | 4–24" | 1 | 1/model SBT | Indirect, Reload, Limited, Support |
| Pistol | Melee–12" | 1 | 0 | | Squad LMG | 1–48" | 4 | 1 | Support |
| Magnum Pistol | Melee–12" | 1 | 1 | | RPG (AT) | 4–48" | 1 | **4** | Reload, Limited, Support |
| Shotgun | Melee–12" | 3 | 3 ≤6" / 2 >6" | | RPG (AP) | 4–48" | 1 | 2/model SBT | Reload, Limited, Support, SBT |
| SMG | Melee–18" | 4 | 0 | | Sniper Rifle | 1–60" | 1 | **4** | Support |
| Assault Rifle | 1–36" | 3 | 1 | | HMG | 1–60" | 4 | 3 | **Crew Served** |
| Battle Rifle | 1–48" | 2 | 2 | | Mortar | 6–60" | 1 | 2/model LBT | Crew Served, Indirect, Reload, Limited |

**Weapon special rules, in full.** **Reload** = one Action after each shot · **Limited Ammo** = **5 rounds per load-out** · **Support Weapon** = **−1" Movement per Action** · **Crew Served** = stationary, no movement, min. 2 crew · **SBT/LBT** = 3"/5" diameter blast · **Flame Template** = 8" long teardrop, **no Combat Ability roll needed — just place it** · **Burn** = affected models keep rolling Armor Saves until they go Out of Action or pass one · and **a flat −2 Combat Ability for using any non-Melee-tagged ranged weapon in melee**. Pistols, SMGs and shotguns are exempt because they carry the `Melee` range tag.

**Grenades and explosives** — Molotov (SBT 1/model, BURN) · Flash Bang (SBT, auto 1 Pin/model) · Smoke (LBT, blocks LOS, **Will check −2** for anyone caught in it) · Hand Grenade (SBT 2/model) · Satchel Charge (2–12", LBT 3/model). **All are Indirect Fire capable.** *"Crew members can carry up to two (2) grenades of any type **for free**… the first set does not use an Equipment Slot."* **[FACT]**

**Cover blocks blast.** *"Models caught in an Area Effect Template but behind Soft Cover receive a **+2 bonus to the Armor Save** roll. **Hard and Hardened Cover will completely block the blast effect.**"*

**Body armour — seven tiers, and every one buys concealment too.**

| Type | Armor | Extra |
|---|:--:|---|
| Basic BDU / Foul Weather Gear | — (save only on a natural 1) | Obscured Target in Cover |
| Salvaged / Improvised | 3 | Obscured Target in Cover |
| Civilian / Commercial | 5 | Obscured Target in Cover |
| Military | 6 | Obscured Target in Cover |
| Advanced | 7 | **−1" Move**; Obscured Target; **+1 Armor Save die, choose best** |
| Mimetic Camo | 4 | **Obscured Target for melee *and* ranged**, cumulative with cover |
| **Military Exo Suit** | 7 | **+2" Move**; Obscured Target; **no Will check for Deflected Hits**; +1 Armor Save die |

**Obscured Target** is *"a −1 penalty to a Ranged Attacker's Combat Ability… additional to and cumulative with standard Cover modifiers."*

**Armour pricing is perfectly linear and published in both directions.** **[FACT]** *"The cost to upgrade your personal protection is simple: **1,000 Zone Script per level of Armor Rating**. So that Military Body Armor will run you 6,000 ZS. The good news is you can **trade in your current armor at 50% of cost**."*

**Equipment Slots.** Rookie **1** · Hardened **2** · Veteran **3**. One item per slot; multiples allowed. Crew Leaders start with **three** items from the Basic list, everyone else **two**. Grenades don't use a slot for the first pair. **A backpack for Salvage is assumed and has no limit** — slots represent *"specific items that are readily available and used in the course of a mission."*

**Three equipment tiers.**

| Basic | Effect | Value | | Advanced | Effect | Value |
|---|---|---:|---|---|---|---:|
| Binoculars | +12" Inspect range | 200 | | Detector | +2 Will when Searching an Anomaly | 500 |
| **Electric Juice** | **+2 Actions now; only 1 Action next turn** | 100 | | Tool Kit | +2 Mechanical checks, −1 Action cost | 600 |
| Gas Mask | No Will check for Smoke/Fumes | 200 | | NODs | Negates Dark/Low-Light penalties | 750 |
| Med-Kit | Replace 1 Wound with 2 Pins | 250 | | Hot Load Ammo | **+1 Weapon Damage, one mission** | 350 |
| Red Dot Sight | +1 Ranged CA **at ≤ half range** | 400 | | Scope | +1 Ranged CA **at > half range** | 750 |

| Special Items *(do not use an Equipment Slot)* | Effect | Value |
|---|---|---:|
| Chest Rig | +1 Grenade, **+1 Equipment Slot** | 1,000 |
| Load Bearing Vest | +2 Grenades, **+2 Equipment Slots** | 1,500 |
| Under Barrel Grenade Launcher | Assault Rifles only — adds a 40mm GL option to the weapon | 1,800 |
| Kevlar Plates | **+1 Armor Rating. Can be added twice per crew member.** | 1,800 |
| Heavy Weapon Reload | +5 ammo of one Limited Ammo weapon type | 2,000 |

*Note the Red Dot / Scope pair: one optic is priced for close work and one for long, at different prices, on mutually exclusive range bands. **That is a sidegrade by construction, not by hope.***

**Weapon prices at the Stalls** (buy price; the "Value" column above is the *resale* figure). Combat Knife 100 · Machete 150 · Chainsaw 250 · Pistol 200 · Magnum 300 · Shotgun 350 · Flamethrower 400 · SMG 400 · **Assault Rifle 500** · Battle Rifle 650 · Grenade Launcher 1,000 · Squad LMG 2,000 · RPG 2,000 · **HMG / Mortar / Sniper Rifle 4,000 each**. *Weapons come with 5 rounds; more ammo is bought separately.* **Weapons and armour trade in at 50%; equipment, artifacts and salvage sell at 90% (the 10% Trader cut).**

**Faction membership is an equipment system in its own right.** **[FACT]** Each of six factions gives a **signing bonus of free gear**, a **permanent % discount at the Stalls**, and cheaper recruitment — paid for by **Faction Dues of 10% of all Salvage after every run, successful or not** (and if you took no salvage, 10% of your cash reserve *including the retirement fund*).

| Faction | Free starting gear | Standing discount |
|---|---|---|
| **Military** | 2× Red Dot Sight, 1× Hot Load Ammo | **20% off Weapons**; Rookies −25% |
| **Scientists** | Detector, Med-Kit, Tool Kit | **25% off Med-Kits, Tool Kits, Gas Masks, Binoculars**; 2 Hardened at 50% |
| **Bandits** | 2× Electric Juice, Chest Rig | **1 free Molotov per visit**; 1 Veteran −25%, Rookies always 50% |
| **Independents** | Gas Mask, Med-Kit, Scope | **20% off Basic Equipment**; Hardened always −30% |
| **Cultists** | NODs, 2× Med-Kit | **20% off Advanced Equipment**; first Veteran and Rookie free |
| **Traders** | **None** | **40% off everything, permanently**; Veterans −25% |

> ⚠️ **The note's own verdict on this:** *"Traders get a flat, permanent 40% discount on everything plus 25% off Veteran hires; Bandits get 'one free Molotov Cocktail' as their recurring perk."* **[INFERENCE — the book states no balancing methodology between factions.]** Thematically defensible, mechanically uneven. **Copy the shape, not the numbers.**

**Suggested armour for drones and light vehicles** (so you can field them without new rules): Small Drone/Robot **3** · human-sized robot **4** · truck or jeep **4–6** · Light Walker / Piloted Exo Suit / IFV **6–7**, possibly two Wounds.

---

## 14 · Fallout: Wasteland Warfare — the richest item-card taxonomy

*Modiphius, lead designer James Sheahan. Rules of Play (60pp) + Into the Wasteland (24pp) + Homestead v2 (34pp) + Automatron (2pp) read in full; the Robots faction list has unconfirmed provenance.*

**Currency.** **Caps** buys everything in a Force and every Structure. **Resources** (Homestead only) pays *only* for upkeep-shaped actions — repair, reinforce, extend, move a Small Structure — and *"can only be kept between each Settlement Use if there is appropriate storage… in a new type of Structure called **Resource Sheds**."* **[FACT]**

**Ten item types, each with printed rules.** **[FACT — p.32]**

| Type | Rule |
|---|---|
| **Weapons** | The main offensive power. Carry a skill icon (Pistol/Rifle/Heavy/Throw/Melee) the model must match. |
| **Armor** | Sets or modifies Armor Ratings. **One card sets the values, plus up to one card of each type that modifies them; the model chooses which cards it's using at the start of its activation.** |
| **Power Armor** | *"A model may equip up to one Power Armor Item."* Its own damage pool and degrade state. |
| **Mods** | *"Up to one Mod card can be attached to an item **which is of the same type**, i.e. Rifles can only be fitted with Mods showing the Rifle weapon type icon. **Mods cannot be fitted or changed during a battle.**"* |
| **Chems** | Powerful mind/body effects with an **addiction downside**. |
| **Alcohol** | As Chems, also addictive. |
| **Food and Drink** | Heal, raise stats, add resistances. **Cooked variants are stronger and strip radiation** — usable only if the card was equipped by a model in your force at the start of the battle. |
| **Clothing** | Raises attributes, grants abilities. **Max one clothing item per model.** |
| **Gear** | The oddities — Stealth Boy (near-invisibility), Stuffed Monkey (warns of enemy activity). |
| **Junk** | *"Serves no other use than its value in Caps"* — pure settlement currency. |
| **Grenades and Mines** | Their own icon class. |

**Limited Use items and sharing.** *"A model may use up to one Limited Use Item each Action."* Multiple copies are one card plus counting tokens. And the sharing rule is unusually generous: *"A model has access to any Limited Use items **its unit is equipped with, and/or any Limited Use item possessed by any unengaged friendly model within Yellow range and Line of Sight**, as if they were equipped with it themselves… ('Hey, Nate! Throw me a stimpak!')."* **[FACT]**

**Three operational durations, tracked physically.** **Instant** (resolve and discard) · **Fixed** (same effect for a period) · **Diminishing** — the item card slides one step further under the unit card **each time the model activates**, and as each column of bonuses is covered, that bonus stops applying. *"A unit may only have one item with a diminishing effect in progress at any time… A unit cannot choose to end a diminishing effect early."* **[FACT]**

**Addiction.** *"When the effect of an item card with the Addictive icon ends, a Special Effect Dice is rolled. If the result matches the icon shown next to the Addicted face, the model has become addicted; instead of discarding the card, **the card is turned 180 degrees and slid under the unit card, with the red section showing the effects of this addiction. These effects remain until the addiction is cured**; the effects do not degrade over time."* **[FACT]**

**Armour — three types, a d12 die, and two bonus mechanics.** Each model has separate physical / energy / radiation ratings. Roll the red **d12 Armor Dice** (results 1–4): **≤ your rating** blocks that much damage; **> your rating** blocks nothing. **Strong Armor** (`3+1`) always blocks the `+1` regardless of the roll. **Armor Boost Tokens** add a temporary Strong Armor bonus and **burn one icon per hit, whether or not damage was caused** — but *"cannot be applied to other sources of armor for a model, such as Power Armor."* **Armor Reduction icons** on the blue Effect Dice ignore one rating point each for that attack only, and **never touch the Strong Armor bonus**.

**Power Armor's two-stage degrade.** *"Damage Tokens are placed **beside** the Power Armor card until the total equals the armor's End bonus."* At threshold the card **rotates 180° to its yellow side** — weaker, but *"even when degraded, Power Armor continues to give benefits such as increased strength, negating falling damage."* **One armor roll only, regardless of anything worn beneath.** Repairable only by items that specifically name Power Armor. **Power Armor always negates ALL falling damage.**

**Advanced weapon categories.** **Mines** are placed by a Move Action up to Orange away, become active at the start of the placer's next turn, trigger only on *enemy* models entering or ending in the proximity area, and the blast diameter is the colour of the short-range bar. **Heavy Weapons** need their own skill icon on the unit card. **Slow Firing** weapons carry a Loaded/Empty marker and can fire once per activation cycle, and can only be equipped by single-model units. **Unique** weapons are one-per-force, single-model-units only. **Primed (X)** weapons need X tokens before use. **Walked Fire** fires multiple shots, each with a separate Skill Test.

**Automatrons — modular units priced as a plain sum.** **[FACT]** *"An Automatron's Unit card consists of **3 cards: Head, Torso and Legs** placed side-by-side to give the total attributes, skills and abilities just like a single Unit card."* **The caps cost is the total of all cards used, including weapons — no formula, no multiplier, no synergy tax.** The AI uses *"the AI card that matches the Automatron's Head,"* with a stated fallback for the mismatch case. **Clunky** robots are *"poorly built and therefore not totally reliable; however, they cost fewer Caps"* — **a flat −20% on the whole robot including all equipped cards**, plus an extra activation die that can add a beneficial *or* harmful token (discarded at the start of the next activation, so the swing never compounds).

**The Robot Controller.** *"To create a Robot faction, the Leader **must** be the Robot Controller (which cannot be a Dog, Creature, Robot, or Synth). Apart from the Leader, the force may only contain Robots."* In exchange the card grants nearby robots **Hold** and **Observer** for free and unlocks a dedicated **Robot Perks** pool — which *"have no further effect"* the instant the Leader is removed.

**Homestead — structures that own equipment acquisition.** This is the corpus's clearest "settlement unlocks gear" system. **[FACT]**

| Crafting Structure | Caps | What it does | Prerequisite |
|---|---:|---|---|
| Weapons Workbench | 100 | Draw and Keep 1 **Weapon Mod** of a type you can attach | Blacksmith or any Gun Nut perk |
| Armor Workbench | 100 | Draw and Keep 1 **Armor Mod** (exc. Power Armor) **OR** add 1 Armor Boost token to a model | **Armorer perk** |
| Power Armor Station | 100 | Draw and Keep 1 **Power Armor Mod**; **repair degraded Power Armor** | **Armorer perk** |
| Chemistry Station | 100 | Draw and Keep 1 **Chem** | — |
| Cooking Station | 100 | Draw 1 Food/Alcohol per Crop Field, keep 1 | — |
| Robot Workbench | 100 | Draw and Keep 1 **Robot Mod** | Robotics Expert perk |
| Creature Pen | 100 | Draw and Keep 1 Creature Mod per Pen | Creature Trainer perk |

**Item Structures** scale in three tiers — Scavenging **50/100/150** (draw 1/2/3, keep 1) and Trading / **Weapons** / **Armor** / Clothing / Drink / First Aid all at **100/150/200** for draw 1/2/3, keep 1. **Turrets cost 5× their in-Force Caps price to install in a Settlement.**

**Land is a slot cap that also sets the battle budget.** **[FACT]** Buying Land costs *"500 OR Complete 5 Quests"* and does three things at once: raises the Structure ceiling (*"Start with 15, and each new Land allows 10 more"*), widens the physical build grid (24×24 → 30×30 → 36×36), **and scales the Caps budget of both sides in a Settlement Attack Scenario** (defender `200 + 150 per Land`, attacker `200 + 200 per Land`, rising to `200+250` / `300+300` at Attack Rating 9+).

> **[NOT FOUND]** Whether an *ordinary away battle's* budget scales with settlement size is genuinely unanswered — that rule lives in the uncaptured Campaign Handbook, which Homestead explicitly requires.

---

## 15 · Judge Dredd Miniatures Game — priced weapons, drawn equipment

*Warlord Games 2020, Dylan Owen. Full 164-page read.*

**Currency.** **Notoriety** — one economy that buys models, weapons, base defences, campaign resources and Informers alike. Campaign phases cap it on a printed schedule (Early 25 / Mid 50 / Late 75) and *"Players with rosters that are below the requisite Notoriety get the difference to spend in each game, to make up any shortfall."*

**Weapons are priced per item, with an escalating cost for duplicates.** **[FACT]** *"Where Notoriety cost is expressed as x/x the first value is for the first weapon chosen and the second is for additional weapons of that type."* A Punk with 2 Pistols costs **+3** (1 for the first, 2 for the second).

| Class | Type | Notoriety |
|---|---|---|
| One-handed close combat | Close combat weapon / Knife / Chain | 0/+1 · +1/+2 · +1/+2 |
| Two-handed close combat | Baseball bat / Laz saw | +2 · +3 |
| One-handed ranged | Pistol / Spit pistol / Sawn-off stump gun / Hand cannon | +1/+2 · +2/+3 · +2/+3 · +3/+4 |
| Two-handed ranged | Combat rifle / Stump gun / Auto stump / Spit carbine / Sniper rifle | +2 · +2 · +3 · +3 · +4 |

**Weapon profile:** `Short Range / Modifier / Long Range / Modifier` plus **Power**, and Special Rules. Range modifiers are the differentiator — the Spit Pistol is `8"/+2, 16"/−1` (high volume, poor accuracy at range); the Hand Cannon `8"/+1, 16"/0`; the Laser Pistol `8"/+1…` and *"can cut through almost any material a target might attempt to use for protection"* but requires recharge time between shots.

**Carrying capacity is "hands."** *"A model can normally carry up to **three 'hands'** of weapons"* — three one-handed, or one two-handed plus one one-handed. **Judges get four.** Aliens, robots and mutants with extra appendages carry more per their own rules. **Firing two guns:** only one-handed weapons or Sawn-off Stump guns; **the model's fire arc becomes Focused Front**; **+1 Shoot per additional weapon**, use the **lowest Power** of the guns fired, and the target gains **a single +1 Resist** for the "quantity over quality" of it.

**Armour is one flat rung.** *"Any Citi-Def model can be upgraded with **ballistic shell armour** and gain **+1 Resist for +2 Notoriety**."*

**Faction identity is written into what's bundled.** Judges' Notoriety cost **includes** their Lawgiver Mk2, Day Stick and Boot Knife; every other faction's model cost *"includes no weaponry of any kind."* Judges may then buy faction-exclusive heavy kit: **M2000 Widowmaker +6** · **Lawrod Mk5 +5** · **Stub gun +10**.

**Armoury cards — the one-shot layer, and you can't shop for it.** Deal **6**, keep **3**. Playable on any friendly model. *"You **cannot buy** hand bombs; they are available as single use items provided by Armoury cards."* Covers: **Hi-Ex** · **Incendiary** · **Concussion** (any model in the radius is *immediately pinned*) · **Ricochet** (gains Blast 2", **needs no line of fire**, ignores cover Resist, and **+2 Power in a confined space**) · **Seeker** (adds 8" to long range, ignores range modifiers, needs no LoF, **−1 to the target's Evade and −1 to their cover Resist** — but on a miss it **automatically hits a different model within 3"**) · **Stealth Suit** (**+1 Evade**, and *"cannot be spotted in scenarios with guards or targeted by Overwatch attacks until it has made a ranged or close combat attack for the first time"*) · **BOING®** (immobilises with no Power-vs-Resist roll at all; *"BOINGed models cannot be harmed in any way"* and can only be freed with another BOING® card) · **Mantrap** (a Power-vs-Resist result table: −1 no effect / 0 stunned / 1+ stunned **and immobilised**, freed only by an ally spending a Hunker Down action within 1").

**Base defences price the field of fire.** **[FACT — p.149]** A Placed Gun's arc is a percentage surcharge on the weapon's own cost: **Forward focused +25% · Forward +50% · All round +100%**, rounded up. **Auto-Turret +3 Notoriety** starts each turn in Overwatch and fires without a crew — but *"malfunctions on a roll of 1 if a friendly model crosses its arc, firing on them anyway."* Other base upgrades: **Turf** (D6 bonus Notoriety per game, lost if unused), **Weapons Locker** (3D6 bonus Notoriety for one-off purchases per campaign phase), **Workshop** (repairs a robot per game), **Bolthole/Emergency Evac** (auto-saves a Subdued model).

**Robots are a keyword, not a subsystem** — see §7.

---

## 16 · Mordheim — the founding priced armoury

*Games Workshop 1999, Tuomas Pirinen. mordheimer.net wiki cross-checked against the 122pp Living Rulebook.*

**Currency.** **Gold crowns**; warbands start at **500 gc**.

**Mercenary Equipment List** **[FACT — living-rulebook.pdf p.52, cross-checked against the wiki's armour page]**

| Melee | gc | | Missile | gc | | Armour | gc |
|---|---:|---|---|---:|---|---|---:|
| Dagger | **1st free** / 2 | | Bow | 10 | | Shield | 5 |
| Mace / Hammer / Club | 3 | | Long bow | 15 | | Buckler | 5 |
| Axe | 5 | | Crossbow | 25 | | Helmet | 10 |
| Sword | 10 | | Pistol | 15 (30 brace) | | **Light armour (6+)** | 20 |
| Spear | 10 | | Duelling pistol | 25 (50 brace) | | **Heavy armour (5+)** | 50 |
| Halberd | 10 | | Blunderbuss | 30 | | **Ithilmar armour (5+)** | 90 |
| Morning star | 15 | | Handgun | 35 | | **Gromril armour (4+)** | 150 |
| Double-handed weapon | 15 | | **Hunting rifle** | **200** | | *(shield adds +1)* | |

> ⚠️ **A caution the capture logged on itself.** A bulk regex scrape of the wiki's `/docs/weapons-armour/close-combat` page (73k chars of per-warband weapon variants) produced clearly wrong numbers — Dagger "15gc", Kitchen Knife "40gc". **The table above comes from the Living Rulebook's actual price list.** Anyone extending this should not trust that wiki page's scraped figures.

**Armour saves are flat D6 thresholds, degraded by attacker Strength:** S1–3 no modifier, S4 **−1**, S5 **−2**, S6 **−3**, S7 **−4**, S8 **−5**, S9+ **−6**. **A natural 6 to wound is a critical**: 1-2 doubles the wound with the save taken *before* doubling; 3-4 doubles it and **ignores all armour saves**; 5-6 doubles it, ignores armour, **and adds +2 to the Injury roll.**

**Gear is destroyed and stolen by the injury table.** **[FACT]** D66 **11-15 Dead** — *"removed, all gear lost."* **36 Robbed** — *"survives, loses all gear."* **23 Arm Wound** on a 1 — *"amputated, one-handed weapons only"* permanently. **61 Captured** — the captor decides between ransom, prisoner swap, or sale to slavers.

**Rarity is a camp-gated search, not a price.** The three **Encampments** each modify equipment access differently: **Sigmarhaven** costs a **tithe of 2 wyrdstone shards per battle** and restricts who may live there · **Brigandsburg** charges nothing but **hired swords cost only 75%**, and **Rare-item searches risk ambush** (Initiative test or lose the search) · **Cutthroat's Den** makes goods cost **double** but finds them at **+2 easier**, and has a slaver and a fighting pit. The separate **Lustria** settlement rules (a different supplement, no shared mechanical grammar) add **Nuevo Luccini** (+2 to find goods at standard price) and **Skeggi** (discounted upkeep for five named Hired Sword types).

**Loot is one dice pool answering two questions.** The exploration pool (1 die per surviving Hero, +1 if you won, max 6) is **summed** for the wyrdstone count *and* **checked for matching pairs or better** against a **30-entry Exploration Chart** — Wells, Shops, a Smithy, a **Gunsmith**, a Graveyard, up to a six-of-a-kind Noble's Villa and a chance at **one of six named Magical Artefacts**. The rarity gradient is free: six-of-a-kind on 6 dice self-limits without any separate rarity roll.

**And the sale price falls twice, by design.** **[FACT]** Wyrdstone pays out on a table keyed to **both** the number of shards sold at once **and** the size of the selling warband:

| Shards | 1-3 warriors | 4-6 | 7-9 | 10-12 | 13-15 | 16+ |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 45 | 40 | 35 | 30 | 30 | 25 |
| 2 | 60 | 55 | 50 | 45 | 40 | 35 |
| 4 | 90 | 80 | 70 | 65 | 60 | 55 |
| 8+ | 155 | 140 | 130 | 120 | 110 | 100 |

**Two independent diminishing-returns curves compressed into one table, with no upkeep line item anywhere on the roster sheet — the maintenance tax is baked directly into the exchange rate.**

---

## 17 · Infinity — equipment as a printed capability menu

*Corvus Belli. Official N5.2 wiki + N3 rulebook figures; 16 hacking/EW pages read in full.*

**Two currencies.** **Army Points** (abundant, integers) + **SWC** (scarce, 0.5 granularity, values 0 → 3.5 plus `+1`/`+2`). *"Each 50 Army Points will provide 1 point of SWC"* — **so the scarce budget auto-scales with game size and needs no per-format table.** **Both Cost and SWC are Private Information** — your opponent may not ask what anything costs. Stacked alongside: **AVA** (per-unit availability caps), Combat Groups (max 10 order-generating troopers), exactly one Lieutenant, and in N5 a hard **15-trooper cap**.

**Why two currencies, stated as a mechanism.** **[INFERENCE, well-supported]** Infinity's order economy makes cheap bodies individually mandatory, so a single currency would force the designer to price HMGs so high nobody takes them. SWC lets them price the gun **cheaply in points** (a Fusilier HMG is only +8 points over a Combi) while **hard-capping how many exist**. **Points buy bodies and order count; SWC buys the right to have force-multipliers at all.**

**Hacking Devices — a device grants a fixed printed menu, not a bigger number.** **[FACT]**

| Device | Programs granted |
|---|---|
| **Hacking Device** | Carbonite, Spotlight, Total Control, Oblivion |
| **Hacking Device Plus** | + White Noise, Cybermask |
| **Killer Hacking Device** | Trinity, Cybermask — *nothing else*; a pure hacker-killer with no attack program that works on TAG/HI/REM |
| **EVO Hacking Device** | Assisted Fire, Enhanced Reaction, Fairy Dust, Controlled Jump — **pure support, no attack program at all** |

Plus named **Upgrade Programs** printed in brackets next to the model's name, exactly like a weapon option. **An EVO hacker is *mechanically incapable* of a killer attack — no restriction text needed, the capability is simply absent from that row.**

**Firewall is Cover, renamed.** **[FACT — designer-voice callout on the official wiki]** *"The Firewall in a Comms Attack is the equivalent of Cover in a BS Attack, it hinders the Attack and aids the target's Saving Roll."* Rather than invent a "hack resistance" stat, Corvus Belli reused an existing subsystem's shape.

**Optics are a three-rung priced counter-ladder.** **[FACT]** **Mimetism** is a flat negative MOD on enemy BS Attacks and Discover rolls. The **Multispectral Visor** answers it in graduated steps: **L1** takes Mimetism −3 → 0 and −6 → −3, gives LoF through Zero-Visibility Zones at a flat −6, and grants immunity to Smoke Ammunition FTF · **L2** zeroes *all* Mimetism and Visibility Zone MODs and gives free LoF through Visibility Zones · **L3** adds auto-succeed Discover vs Camouflaged targets, ignores Surprise Attack MODs, and **may BS Attack a Camo Marker directly** with no Discover roll first. **Sensor** is a one-Action area reveal (*"a Normal WIP +6 Roll… to simultaneously Discover all enemy Troopers in the Hidden Deployment or Camouflaged States inside the user's Zone of Control"*) that also denies re-Camouflaging in that zone.

**Counters exist at three price points instead of one hard wall.** **Non-Hackable** is a printed immunity tag, not a roll. **ECM** is Automatic Equipment imposing a flat negative MOD on a named attack type, value printed per profile. And **[CONSENSUS]** the meta answer is to hunt the network — bring an Engineer to repair Isolated/Immobilized troops, use a cheap disposable model to physically destroy the enemy's Repeaters, or assassinate the lynchpin hacker.

**Hackability is a printed Troop Type tag.** **[FACT]** The Hacking Programs Chart's Target column reads `TAG, HI, REM, VH, Hacker`. *"Which of my units can even be hacked"* is answered once, at the type level.

> **The instructive trend: Corvus Belli have been *pruning* this system, not growing it.** **[FACT — absence confirmed by direct page read]** N3 had **seven** device types (AHD, HD, HD+, KHD, DHD, WHD, EVO) and **five** program families (SWORD, SHIELD, CLAW, GADGET, UPGRADE), with SHIELD splitting further into Army Shields and Defense Protocols. **None of AHD, DHD, WHD, EXORCISM, U-TURN, HACK-TRANSPORT AIRCRAFT, BREAKWATER or COUNTERSTRIKE appear anywhere on the current N5.2 pages.** The current game has four devices and two labelled categories. **The one publisher with the resources to make a maximal EW subsystem work has spent three editions cutting it down.**

---

## 18 · Warhammer 40,000 — the 25-year controlled experiment

*Published editions 3rd → 11th plus designer statements. The single most decision-relevant profile in the corpus.*

**The arc.** Per-item costs on every entry (3rd–7th) → per-item costs **plus** a parallel coarse Power Level system (8th) → per-item costs quietly deleted faction-by-faction (9th) → **all wargear free** (10th) → **selective costs return on outlier weapons only** (11th, June 2026).

**The failure documented in print** — see §8.1 for the 3× spread table.

**8th edition's principled exception proves the deeper point.** **[FACT — parsed from BSData catalogues]** Heavy bolter **8 pts** for Astra Militarum vs **10** for Grey Knights/CSM; multi-melta **15** vs **22**. Guardsmen are BS4+, Marines BS3+, so the same gun genuinely delivers less. **[INFERENCE] A weapon's value is a function of its platform, so a global weapon price list is a category error. Any atomic system must either accept per-platform prices — losing the atomic benefit — or accept mispricing. There is no third option.**

**11th edition's settlement, and the worked example.** **[FACT]** *"Some weapon upgrades now cost points if they are **significantly more powerful or effective** than the other available options."* The macro plasma incinerator on a Redemptor Dreadnought costs **10 points**, but *"the basic cost of the Dreadnought **drops by 10**, so it nets out the same"* — it *"helps limit their impact when taken en masse, but doesn't overly punish players."* Plus **points steppers**: units cost more for your 2nd or 3rd copy, *"designed to discourage always spamming three of whatever is most efficient right now."*

**Goonhammer's verdict, and their fix is the useful part.** **[CONSENSUS]** *"**How well this works varies.** For big threats centred around a main weapon, it's generally pretty good… Where it feels more awkward is for some squad weapons like psycannons in Grey Knights, where each gun probably isn't 5pts better than the alternatives."* Their proposal: *"rather than 5pts per gun, do 10pts on the unit if you take any psycannons"* — **cost the decision, not the item.**

**The operational lesson, free to adopt.** **[FACT]** GW moved points **off the datasheet** in 2017 specifically so *"points for units could change without invalidating existing books."* **Every balance correction across three editions depended on that one packaging decision.** The maintenance cost is real, though: quarterly Munitorum Field Manual updates plus alternating Balance Dataslates, running **monthly** for 11th edition's first three months. **[INFERENCE] The 11th-edition model requires a live data feed and a patch channel.**

> ⚠️ **[UNVERIFIED]** No published dataset isolates free wargear's actual effect on balance. Nobody ran the counterfactual. **Every claim in either direction — including GW's — is argument, not measurement.**

---

## 19 · Kill Team — three equipment philosophies in six years

*Games Workshop, 2018 / 2021 / 2024. The cleanest natural experiment in the hobby: same company, same setting, same scale.*

**2018 — full atomic costing.** 100-point cap; *"each model **and each of their pieces of wargear** has an associated points cost."* Specialist progression itself was priced: Level 1 +0, Level 2 +4, Level 3 +8, Level 4 +12. **[FACT]** See §8.3 for why this combination is the worst available.

**2021 — points removed for models, retained for gear.** GW's own headline is the thesis: *"New Kill Team Replaces Points With a Fast, Finely Balanced List-building System."* Designers *"effectively **baked your operatives' points values into the way you pick your rosters**,"* with balance from *"restrictions on specialist numbers rather than point calculations."* **[FACT]**

> **But points survived for equipment, at a separate budget of 10 Equipment Points. GW did not abolish points in 2021 — they split the problem.** Models structural, gear costed, two budgets. **[INFERENCE] That is a dual-currency system arrived at from the opposite direction to Infinity's.**

**2024 — points removed entirely, including for gear.** **[FACT]**

> *"Each player instead may choose **up to four equipment options**… It is important to note that **equipment no longer corresponds to any individual operative**… Each option may only be taken **once per battle**, and players **alternate setting them up** prior to operative placement."*

The universal list is mostly battlefield furniture and consumables — **barricades, ladders, ammo cache, razor wire, comms device, mines, grenades.**

**Three separate wins in one move.** **[INFERENCE]** (1) Four slots, each item costs one slot — **no numbers to balance, unbreakable, instantly learnable.** (2) **Detaching equipment from operatives** kills the combinatorial interaction that made 2018 unbalanceable *and* removes the "key model dies, kit wasted" swing. (3) **Alternating placement** converts a list-building decision into an interactive pre-game one — you react to what they put down.

**The price paid:** equipment can no longer express "this specific model is kitted differently."

**The arc, in one line: atomic → structural → structural-with-slot-budget. GW ended up back at a resource system; they just made the resource unit-less.**

---

## 20 · BLKOUT — designer-authored cards and a shared Force Armory

*Enemy Spotted Studios. Print 2nd Edition digital rulebook (23pp) + Supplemental Packet (9pp). Full read-through at `docs/BLKOUT-RULES-ANALYSIS.md`.*

**There is no costing system at all.** **[FACT — blkoutgame.com]** *"Forget the tedious task of point-counting; in BLKOUT, you simply choose a force and pick three units."* A **Group** = 1 Force Card + 3 Unit Cards. Matched Play adds a **Handler** (one of eight archetypes) and allows one unit to be swapped for a **BLKLIST** mercenary.

**Weapons are a base profile plus a shared USR library.**

```
FAL-32C          |  24" / 1     |  CQB
Micro Launcher   |  4-16" / 2   |  Blast (1), Heavy
Grenade Launcher |  24" / 2     |  Blast (1)
```

The weapon carries **only Range and Damage**. Hitting is the model's **Skill**; saving is the model's **Armor `X/Y`**. Range can be a single value or a **min–max band**. All the texture is in the ~20 USRs: **AP (X)** worsens the target's Armor threshold · **Auto (X)** makes up to X extra shots at *different* models within 4", un-Reactable · **Cyclic** immediately grants one more Shoot or Ready Action · **Heavy** +1D10 if you didn't move (reactions always get it) · **Deployed** only 1D10 if you moved · **CQB** re-roll failed shots within half range · **Medium** re-roll one failed shot · **Seeking** ignores the cover −1D10 · **Sustained (X)** forces re-rolls of up to X *successful* Armor dice · **Blast (X)** · **Indirect** (fire using another friendly model's LoS) · **Lethal** (3D10 for CQC checks) · **EMP / Data Knife / Data Spike** for cyber payloads.

**The Force Armory + Combat Loads is the one acquisition mechanic.** **[FACT]** *"**Combat Loads** — triangles in the card corner. Each is one 'charge' a Grunt can spend to pull a weapon/ability from the Force **Armory**. Tick one per use."* The Armory is a faction-level pool of weapons and abilities that any Grunt can draw from, a finite number of times, mid-game. **Balance is carried entirely by card design and access restrictions:** BLKLIST mercenaries *"cannot use Battle Drills, **Armory Items**, or Force Special Rules,"* and neither can Handlers.

**Cyber is delivered through weapon traits, not a separate subsystem.** A **Data Spike** makes a Data Attack (Skill Check, **no LoS needed**) to **Pin** an enemy unit or un-Pin a friendly one; a **Data Knife** deals **1 Damage to an AI/Powered model, ignoring armor**. **Counter EWAR** lets a friendly Data Spike nullify an incoming Data Attack.

**Conditions are thin and delivered *through* the traits** — Pinned (from a Data Spike or a wrecked vehicle), armour degradation (AP, Sustained), and hard control via cyber and Blast. **There is no bleed/fire/poison/stun ladder.**

**The design objection is in the canonical literature.** **[FACT — Gutschera]** *"'Everyone gets to bring 16 pieces to the table' is a costing system for choose-your-own-army chess… but it's **not robust**, since players will choose nothing but queens."* Which is precisely why BLKOUT has to lean so hard on card design and access tiers.

---

## 21 · Fistful of Lead — slots and traits, one pool, no currency

*Jaye Wiley, Wiley Games 2024 (2nd ed.). Full 62-page read.*

**There is no costed force-build system anywhere in the book.** **[NOT FOUND — checked the full Building Your Gang, Traits, Negative Traits, Gang Traits and Weapons chapters.]** Roster size and composition are fixed role-slots: Leader / Sidekick / 3 Regulars, or a Rabble group in a Regular's place.

**Equipment Slots are the entire economy.** Leader **4** · Sidekick **3** · Regulars and Rabble **2**. Weapons take **1 or 2 slots**. And the key move: *"In this initial build part of creating your Gang, **each member may elect to 'trade' 2 equipment slots for a trait** for themselves."* **[FACT — p.30]** **Gear and character-flavour compete for literally the same pool, at a fixed published exchange rate.** A Leader who wants to be a walking arsenal gets no Traits; one who wants Traits shows up with a knife.

**Weapons** — `Short/Long` range plus a Notes column. Notably, **most of the differentiation is in ammunition and reload discipline, not damage.**

| Weapon | Range | Slots | Notes |
|---|---|:--:|---|
| Dagger/Knife | melee | 1 | **Wins ties in Close Combat** |
| Sword | melee | 1 | +1 to Close Combat rolls |
| Ax/Machete | melee | 1 | +1 to Wound rolls |
| Club | melee | 1 | **Additional Shock Marker added to the Wound roll** |
| Whip | 6" reach | 1 | **Entangle** — a Wound result means Helpless, not damage; and *"if the defender should win, the attacker cannot be harmed"* |
| Spear | 6"/12" | 1 | Thrown: lost on a Shoot roll of 1 or 2 |
| Bow | 8"/16" | 1 | **Reload: 1 Action** (not 2) |
| Throwing Knives/Axes | 3"/6" | 1 | **Out of weapon on a natural 1 or 2, for the rest of the game** |
| Single Shot Pistol | 6"/12" | 1 | Reload after every shot |
| Repeating Pistol | 6"/12" | 1 | — |
| Musket | 8"/16" | **2** | Reload after every shot |
| Carbine | 8"/16" | **2** | — |
| Rifle | 12"/24" | **2** | — |
| Buffalo Rifle | 18"/36" | **2** | Reload after every shot, **+1 to Wound** |
| Shotgun | 6"/12" | **2** | **Splatter**, +1 to Wound at short range, **ignores light cover** |
| Dynamite Stick | `d10+3"` | — | **Blast; not purchasable — found in scenarios only** |
| Gatling Gun | 18"/36" | — | **Burst; not purchasable — found in scenarios only** |

**Shotgun Splash, stated exactly:** *"If the weapon with Splash damage hits, any miniature within 1" of the target will also be rolled to hit (**friend or foe**). At Long range, this splash increases to 2", but extra targets are hit at a −1 modifier as well as a −1 on the Wound roll."*

**Dynamite has a self-inflicted failure state:** *"When rolling to hit, a roll of '1' causes the stick to **detonate in the model's hand**. BOOM! Roll with a +1 on the Wound chart."*

**Negative Traits buy Positive Traits — a slot swap, not a refund.** **[FACT — p.28]** *"Negative Traits let you pick another Positive trait for the miniature. **You may normally only take one Negative Trait.**"* The list is short and flavourful — Brittle, Coward, Drunkard (start Wounded), Greenhorn (d8 for all rolls), Slow, Small, Squeamish, Unlucky, Unskilled, Weakling — **with no point values attached to any of them.** Where Song of Blades and the Rampant line refund a *spendable point value*, Fistful of Lead has no points to refund into: a flaw **unlocks exactly one extra Trait slot**, capped at one use.

> ⚠️ **The trait list has no stated weighting, and it shows.** **[INFERENCE — read against the full ~50-entry list, pp.25-29]** Quick (+1" move) and **Two Gunned** (an entire second combat mode, Burst fire, near-immunity to Out of Ammo) sit in the same undifferentiated list with no price or tier separating them.

**There is no armour.** See §4.

---

## 22 · Mad Dogs with Guns — dollars, and a super-linear stat ladder

*Howard Whitehouse & Roderick Robertson, Osprey 2017. Full 116-page read.*

**Currency.** **Dollars.** The exchange rate is published: **1 point of Loot = $100** **[FACT — stated verbatim twice, pp.57 and 77]**.

**Punks are built on a super-linear stat ladder.** **[FACT]** A basic Punk costs **$25** with 2 across the board.

| Improvement | Cost |
|---|---:|
| Increase stat to 3 | +$10 |
| Increase stat to 4 | +$25 |
| Increase stat to 5 | +$50 |
| Increase stat to 6 | +$100 |
| Random Skill | +$25 |
| Chosen Skill | +$50 |

**A doubling at every rung.** Note also that a *chosen* skill costs exactly 2× a *random* one — a clean published price on removing variance.

**Weapons and equipment** **[FACT]**

| Item | Cost | | Item | Cost |
|---|---:|---|---|---:|
| **Hand to Hand Weapon** | **Free** | | Automobile or Truck | $200 |
| **Pistol** | **$20** *(1 free to figures with GATS 3+)* | | Fancy Automobile | $700 |
| Double-barreled Shotgun | $50 | | Souping up an auto | +$150 |
| Pump Shotgun | $75 | | Good Suspension | +$150 |
| Carbine | $100 | | **Bulletproofing** | **+$500** |
| Rifle | $150 | | Grenades | $25 each |
| Tommy Gun | $200 | | | |
| BAR / High-powered Rifle | $300 each | | | |

**Everyone has a free melee weapon and every competent shooter has a free pistol.** *"Every figure with a GATS of 3 or more automatically has a pistol and all figures have close combat weapons (fists, bats, pipes, flick knives, etc.)."* **The floor is free; only the escalation is priced.**

**Weapon profiles are `Short / Long / Dice` plus a note.** The Tommy Gun is `6"/24"`, **6 dice**, *"Blazing Away. −2 GATS at more than 3". **Jams if three 6s rolled**"* — a signature weapon with a signature failure mode. The BAR is `12"/48"`, 5 dice, −1 GATS beyond 3". Light MG (.30) `24"/60"`, 7 dice. Heavy MG (.50) `24"/72"`, 7 dice, **+1 on the Deadly Weapons Table**. High-Powered Rifle `24"/72"`, 1 die, **+1 on the Deadly Weapons Table**. **Small guns give −1 on the Deadly Weapons Table.**

**Reload discipline is per weapon type:** one action after rolling a 6 for a pistol/carbine/rifle/pump shotgun; **4–6 for machine gun bursts**; both barrels of a double-barrelled shotgun; or after Blazing Away with a pistol or shotgun.

**There is no personal armour.** Armour exists exclusively as **$500 Bulletproofing on a car**, which *"reduce[s] their Speeding"* — a mobility cost for protection, exactly the same trade Zona Alfa's Advanced Body Armour makes.

**Healing buys down your own risk of dying.** **[FACT — p.80]** Wounds cost total stat points (Light 6, Wound 12, "It's Serious" 24), recovered over months at a rate set by the purchased care tier:

| Care tier | Cost/month | Heals | **Cripple Roll Modifier** |
|---|---:|:--:|:--:|
| Self-Care | free | 4 | **+4** |
| Doctor Visits | $50 | 6 | +2 |
| Hospital | $500 | 8 | +1 |
| In-Home Doctor | $1,000 | 8 | **none** |

Every recovery month, roll `2D6 + Cripple Roll Modifier`: **11 or under is fine, 12+ permanently costs 1 point off a still-injured stat, and boxcars kill outright regardless of care tier.** **Spending more doesn't just heal faster — it directly buys down the flat probability of your gangster dying that month, off the same number.**

**Business defence is derived from business income.** **[FACT — p.94]** *"A business needs **2 guards per D6 Loot** that it produces."* A Paradise Brewery (5D6) defends itself with 10 free guards; a Bookies (1D6−1) with 2. **A richer site is automatically harder to take, with no second stat to hand-tune.**

---

## 23 · Last Days: Zombie Apocalypse — noise as an equipment attribute

*Ash Barker, Osprey. Core rulebook + Seasons supplement, both read in full, twice.*

**Currency.** **100 Scavenge Points**, spent once at group creation. **There is no per-game points limit after that at all.** **[FACT]** Levels are bought with **Experience**, a completely separate currency; *"you cannot buy a stat with SP, and you cannot buy a body with XP."*

**`Noisy X` is the standout equipment mechanic in the whole corpus for a scavenger game.** **[FACT — p.72]**

> *"**NOISY X** — A character, weapon, or piece of equipment with this attribute generates +X [Noise Tokens]."*

It's a first-class attribute that can sit on **a weapon, a piece of gear, or a Character**, stacking flat tokens onto the *same* shared counter that shooting already writes to. A **Motorcycle** carries `Noisy 3` just for existing each Menace Phase. In *Seasons*, the Gather Fuel job's Chainsaw option adds **+3 Fuel** but **−2 to the next Zombie Attack roll** for the racket it makes.

**Exactly one skill answers it — Stalker:** *"They do not generate Noise Tokens when they run."* **One attribute, one counter-skill, no parallel stealth subsystem.**

**Ammo is per-weapon and persists until you actually reload.** Every Rate-of-Fire point spent drops both a Noise Token *and* an Ammo Token; the Ammo Token checks against the weapon's **Reload Number** rather than the flat 7 that Noise checks against. *"Unlike Noise Tokens, **Ammo Tokens are only removed once a gun is reloaded**."* **[FACT — p.53]**

**Weapons carry a Knockback stat that only matters against zombies.** A hit on a zombie rolls 1D6: **5–6 destroys the brain**; **1–4 does nothing to Damage Capacity but adds Knockback Tokens equal to the weapon's Knockback stat**, each cutting 1 AP from that zombie's *next* activation (5+ and it can't move at all), discarded at the end of its activation. **[FACT]** **The horde's threat is resolved through tempo, not a hit-point race — which is what lets 20+ zombie models stay cheap at the table.**

**The Refuge and its Perks are the equipment-adjacent layer.** The base costs **zero points** and sits outside the creation budget entirely. Perks run **15–30 SP** and, crucially, **cannot be built without an Empty Space** — a slot cap that *"cannot be optimised around the way a price can."*

| Refuge | Max Group | Empty Spaces | Built-in Perks (free) |
|---|:--:|:--:|---|
| The Gun Shop | 6 | 3 | **Armoury**, Fortified Windows, Reinforced Doors |
| The Farm House | 8 | 5 | Fenced-Off Garden *or* Stable, Cold Cellar |
| The Church | 8 | 2 | Solid Structure, Watch Tower |
| The Police Station | 8 | 2 | Escape Vehicle, Radio Room |
| The Prison | 10 | 3 | Fences, Infirmary |
| The Mall | 12 | 8 | Store Room |
| Outdoor Campsite *(Seasons)* | 12 | 10 | **None** — and **Exposed**: every Perk costs **+5 SP** |
| Cabin in the Woods *(Seasons)* | 5 | 3 | Wood-Burning Stove |

The **Armoury** Perk is the direct gear link: *"If a Character works the Armoury, during the next Encounter their Group may **re-roll 3 failed Ammo Rolls**."* **[FACT]**

**And structures own their unlocks.** **[FACT]** *"Stable (20 SP) unlocks 0–2 Horses at 15 SP each, and **losing the Stable removes the Horses from the roster**."* **Capability is leased, not bought outright.**

**Context-priced construction, with an unresolved bug.** An **Engineer** assigned to Build cuts the cost **25%, rounding up**; an **Exposed** Refuge adds **+5 SP** to every Perk. ⚠️ **The book never states the order of operations.** 35 → 27, or 23 + 5 = 28? **Genuinely unresolved in print, confirmed still unresolved on the full read of both books.**

**The upkeep natural experiment.** The **core rulebook has no food, water or fuel economy at all** **[FACT — confirmed on the full read]**. The optional *Seasons* supplement bolts on four tracked Conditions (Hunger, Health, Thirst, Warmth) with a Suffering → Critical ladder where **any two Critical simultaneously kills the Character outright**, plus three new Jobs, a heating formula (`Starting Perks + Empty Spaces = Rooms to heat, 1 Fuel per Room`), and **three separate ordered feeding/warming/watering lists resolved after every Encounter for every Character.** **Same designer, same game: he shipped zero-upkeep as the default and sold the tracking as an opt-in hardcore module two years later.**

---

## 24 · Malifaux — Upgrade Cards, and the correction to a common belief

*Wyrd Miniatures, M3E Rules Manual, quotes verified.*

> **Correction on record: M3E did *not* remove upgrade-buying.** *"Upgrade Cards exist in M3E, carry Costs, and are purchased during hiring. What changed was their **scope and volume**."* **[FACT — verified against the Rules Manual]**

**One upgrade at hiring, unlimited in play.** **[FACT]**

> *"During hiring, **any model can pay for and Attach a single Upgrade**. This limit only applies during hiring; **there is no limit** to the number of Upgrades a model may Attach during gameplay."*

**[INFERENCE] The combinatorial explosion that makes upgrades unbalanceable happens at list-building, where a player can search the whole space offline. In play, upgrades are gated by tempo and circumstance. Cap where the search is free; open up where the game is already the constraint.**

**A three-word constraint vocabulary printed on the cards:** `Restricted (Name)` · `Special (Name)` (cannot be hired, only attached in-game) · `Plentiful (X)`. **That is less text than a paragraph of restrictions and does the same job.**

**The keyword tax gates access without banning anything.** **[FACT]** *"A player may hire any models that share one or more Keywords with their Leader… models that do not share a Keyword with their Crew's Leader have their **Cost increased by +1** during hiring. The exception… are models with the **Versatile** Characteristic."* One flat, tiny, universal modifier makes thematic lists cheaper than optimised ones, with a designer-controlled escape hatch for the units *meant* to travel between crews.

**Leftover budget converts, and the conversion is capped.** *"Any unspent points become Soulstones in your Crew's Soulstone Pool. A Crew's Soulstone Pool **cannot exceed 10 Soulstones** during hiring."* Nobody is punished for a list that doesn't spend to the last point, and hoarding is bounded.

**The upgrade failure mode, in the designers' own words.** **[CONSENSUS — quote surfaced via search, original URL unconfirmed; attribute cautiously]** Emissary upgrades *"were generally used as **patches to sub-par Masters** and were either not impressive enough to see the table or so strong that they became mandatory hires,"* and removing them let designers *"focus on making each Emissary good on its own merits."*

> **A standing test for any priced option: *is this a patch?* If it exists to make something weak playable, it belongs in the base profile, not on the price list.**

---
---

# PART THREE — THE THIN AND STRUCTURAL SYSTEMS

Seven games whose gear layer is deliberately minimal, plus the costing-formula sources that inform how gear *should* be priced.

## 25 · Oathmark — equipment baked into the profile

*Joseph A. McCullough, Osprey. Full core rulebook (194pp) + Battlesworn (81pp) + Bane of Kings (81pp).*

**There is no wargear purchase step.** **[FACT — p.15]** *"**Equipment**: The basic fighting equipment the figure carries, including weapons, armour, and shields. **All costs for a figure's equipment are already worked into their stats**; however, it is necessary to note which figures carry missile weapons, such as bows or slings, as only these figures may make shooting attacks."*

Profiles simply read `Equipment: Hand Weapon, Shield, Light Armour`. *"Note that hand weapon or two-handed weapon can refer to any type of weapon and can be represented by swords, axes, clubs, or flails on a model. **Spears are listed separately**, as these figures generally have the special ability Brace."*

**Defence is a special ability, not a stat.** **Shielding (X)**: the non-active unit discards X of the attacker's Combat Dice, but the attacker's unit must also discard one (to a minimum of 1). **Shielding may not be used if the attack targets the flank or rear** — directional armour with no facing subsystem to maintain.

**The only à-la-carte equipment in the game is Magic Items, and they are opt-in.** **[FACT — p.183]** *"**If you and your opponent agree**, you may include magic items in your armies. To purchase a magic item, you must simply pay the listed point cost and assign the item to a figure in your army that has the **special ability Magic Items**."* **Gated twice: by mutual consent, and by an ability only characters have.**

| Item | Pts | Effect |
|---|---:|---|
| Armour of Starsilver | 50 | Roll a die per point of damage; on a **7+**, ignore that point |
| Banner of Courage | 60 | The whole unit gains **Courage (1)**, or +1 level if it already has it |
| Boots of Striding | 30 | Grants **Nimble** |
| Crown of Regeneration | 50 | **Regeneration (1)**, not cumulative with other sources |
| Cloak of Discorporation | 100 | Grants **Discorporate** |
| Golden String Bow | 50 | A Champion may roll the **Champion Die on shooting attacks** — an explicit exception to the normal procedure |
| Ring of Shielding | 50 | **Shielding (1)** or +1 level — but *"only affects attacks directed at the figure itself, not at the figure's unit"* |
| Ring of Spellcasting | 30 | +1 known spell |
| Sceptre of Command | 75 | Activate other units at **9" instead of 6"** |
| Sword of Starsilver | 50 | **+1 to the Champion Die**; a 9 counts as a 10 for hits, **but not for striking a character** |
| Sword of Flames | 50 | Re-roll 1s on the Champion Die — **once only, so it can't stack with Wild Charge's reroll** |

**Note the discipline in that list.** Every entry either grants an *existing named ability* or bends *one existing rule*, and three of them carry an explicit anti-stacking clause. **No item invents a new mechanic.**

**And the whole kingdom layer never touches the budget.** **[FACT — p.82]** *"Every game you play has a **fixed number of points** you can spend to purchase figures for your army."* Growth is a **wider menu**, never a bigger army — which means new territory unlocks *access to units*, and by extension their bundled equipment, without ever inflating what you can field.

## 26 · Frostgrave & Stargrave — the wizard's gear is free

*Joseph A. McCullough, Osprey. Primary PDFs read directly.*

**Two economies with no exchange rate.** **[FACT]** **Gold buys bodies and items. XP buys stats, spells and powers.** Neither converts in either direction. **The wizard/captain is free, their gear is free, and spells and powers are free** — limited by slots and count, not by price. The 400gc budget covers only the apprentice (100gc) and the soldiers.

**Price ladders are deliberately coarse.** Frostgrave: **Free / 10 / 50 / 75 / 100 / 125**. Stargrave: **Free / 10 / 20 / 50 / 75 / 100 / 150**. **[INFERENCE]** The implied curve reads as roughly **25gc per meaningful stat step**, with a deliberately flat but playable free tier — *"a genuinely free, genuinely playable body means a player can always field a full warband no matter how badly the campaign has gone."*

**[NOT FOUND — a firm negative]** No derivation is published. The only justification is in-fiction: costs are *"retainers"*; specialists *"require larger retainers and positions of authority."* The "Why A Second Edition?" essay discusses spell rebalancing in detail (~20 of 80 spells were *"too weak or too situational"*) and **never mentions soldier pricing at all.**

## 27 · Rangers of Shadow Deep — no currency of any kind

*Joseph A. McCullough. Primary PDF read directly.*

**There is no currency.** **[FACT]** Treasure results of "Gold and Jewels" convert to **+10 XP or 1 companion Progression Point** — never to purchasing power.

A Ranger is **10 Build Points** on a fixed base, against sub-caps that deliberately total **16**:

| Purchase | Cost | Max BP in category | What 1 BP buys |
|---|:--:|:--:|---|
| Stats | 1 BP | **3** | +1 to one stat — **Armour can never be raised** |
| Heroic Abilities & Spells | 1 BP | **5** | one ability *or* one spell |
| Skills | 1 BP | **5** | **+1 to eight different skills** |
| Recruitment Points | 1 BP | **3** | +10 Base Recruitment Points |

**[INFERENCE] The build is deliberately over-subscribed by ~60%, which is what forces a real choice — you cannot max any two categories.** And note the hardest constraint in the corpus: **Armour is the one stat that simply cannot be bought at all.**

**Companions are hired with Recruitment Points, recalculated before every mission, and cannot be banked.** *"Nothing carries over, so nothing compounds."*

## 28 · The Walking Dead: All Out War — a published build formula with a printed confession

*Mantic Games, Anthology edition.*

**Characteristic dice are priced X / Y / Z** — pay X for the first die in that characteristic, Y each for a second, Z each for a third. **[FACT]**

| Die tier | Melee | Shoot | Defense |
|---|---|---|---|
| Best (blue) | 10 / 12 / **16** | 12 / 15 / **20** | 7 / 10 / 12 |
| Mid (white) | 5 / 6 / 7 | 6 / 7 / **8** | 3 / 4 / 5 |
| Worst (red) | 3 / 3 / 5 | 3 / 4 / 6 | 2 / 2 / 3 |

Confirmed by the book's own worked example: *"two white dice and one blue… for the Shoot value that would be a whopping total of 36 points – 8+8+20."* Plus **Nerve** (Low +0 / Medium +5 / High +15), **Health** (3 = +0 rising to 8 = +20), **Pack Slots** (1 = +0 to 4 = +5), up to two Special Rules (2–20 pts) and one Leader Ability (5–10 pts).

**Note that Pack Slots — carrying capacity — are an explicitly priced characteristic**, which almost no other game in the corpus does.

**And the designers admit in print that it doesn't quite work.** **[FACT — verbatim]**

> *"You'll notice that some of the Survivors in the game work out slightly different to the points values here would indicate. **As there's no way of accounting for every possible combination of characteristic and ability**, it's hard to truly gauge the effectiveness of a custom character, **so these rules include a slight premium**. As a result, it's best to only use custom characters in friendly games in which your opponent agrees to their use."*

**This is the most honest statement of the atomic-costing problem found anywhere in the research, and the mitigation is the instructive part: ship the formula, add a deliberate premium for the combinations you can't price, and quarantine the whole system to friendly play.**

**The neutral threat is costed against the game, not either player.** *"Walkers are **15 points each**, [chosen] to the same points limit as the game"* — so in a 50-point game you field 4, and in a 300-point game 20. **Nobody pays for the threat out of their own list, and both players get to aim it.**

## 29 · The costing-formula sources — how gear *should* be priced

Five systems in the corpus have little equipment texture but publish (or leak) the arithmetic that governs it.

**One Page Rules — the most complete atomic system in modern tabletop.** **[FACT — official "AoF: Point Calculator v1.10", verified 4/4 against OPR's own worked examples]**

```
Base Cost       = (Quality + Defense) × X          where X = Tough(X), else 1
Total Unit Cost = (Base + Weapons + Special Rules) × Models   → round to nearest 5

Weapon Cost = Range × Attacks × Special Rules
Total Cost  = Weapon Cost × Quality        ← the unit's Quality POINT VALUE
```

Range multipliers: Melee 0.25 · 6" 0.125 · 12" 0.25 · 18" 0.375 · **24" 0.5** · 30" 0.625 · 36" 0.75 · 42" 0.875 · **48" 1.0**. Weapon-rule multipliers: **AP(1) ×1.5 · AP(2) ×2 · AP(3) ×2.5 · AP(4) ×3 · Blast(X) ×X · Deadly(3) ×2 · Deadly(6) ×4 · Indirect ×1.25 · Poison ×1.25 · Rending ×1.5**.

**Because Quality is additive in the base but multiplicative on every weapon, while Defense enters only the base, a Quality step costs ~1.75× a Defense step — automatically, with no separate offence/defence budget.** And `Tough(X)` multiplies the whole base but **not** weapons, so durability compounds while guns stay linear.

The stat ladder: **2 / 4 / 6 / 8 / 16** for 6+ / 5+ / 4+ / 3+ / **2+** — *+2 per step, then a doubling at the top,* to make extreme stats self-limiting. Special rules mix flat, derived and multiplicative forms: Fear = 20 · Artillery = 15 · **Impact(X) = 3X** · **Regeneration = 6×Tough(X)** · **Stealth = 2×Tough(X)** · **Wizard(X) = 20X+5** · Flying/Fast/Scout/Ambush = Quality · **Slow = −Quality** · **Immobile = −3×Quality** · Strider = Quality/2 · **Hero = 0** · Fearless = recompute the base at Quality+1.

Two operational rules worth lifting: **price upgrades as deltas** — `cost(new) − cost(old)`, **rounded up**, which kills the "sidegrade costs 0" exploit dead — and **round once, at the end, to a coarse grid** (nearest 5).

And OPR ship a **second, orthogonal validator** **[FACT — patch notes, 26 Jan 2024]**: *"we use a simple system of comparing **how many potential wounds a unit can deal vs how many wounds the unit can take**."* **The formula sets the price; a damage-ratio cap catches what the formula misses.** Plus a written guideline where maths can't reach: *"**Avoid using Quality 2+ and 6+** because players feel like they are not very balanced, even if point costs compensate for the rolls."* — **costing the extremes correctly is not the same as making them fun.**

**Song of Blades and Heroes — the cleanest published answer to "the same ability is worth more on a better model."** **[FACT — chart published; formula derived and validated 34/34]**

```
Cost = round( (5 × Combat + Σ SpecialAbilityPoints) × (7 − Quality) / 2 ),  minimum 1
```

Quality multiplier: **Q5 ×1.0 · Q4 ×1.5 · Q3 ×2.0 · Q2 ×2.5**. Because Quality *is* the activation roll, it multiplies the entire cost including every special ability — **so Stealth (3 SA points) costs 3 on a Q5 militia and 7.5 on a Q2 hero, automatically, with no separate table.**

Three decisions visible in the published ability list: **ranged reach is a stepped, accelerating ladder** (Shooter Short **2** / Medium **4** / Long **7** — steps of 2 → +2 → +3) · **pure-flavour abilities are explicitly priced at 0** (Evil, Standard Bearer, Were, Solar Force) · **negative traits refund**, with the biggest refund (−5, Slow) on the one that costs you tempo.

⚠️ **The known weakness [INFERENCE]:** a 3-point band lumps Stealth, Heavy Armor and Poison together as equals. **The granularity of the ability list is coarser than the formula deserves.**

**BattleTech Battle Value 2 — the only fully public, machine-checkable derivation.** **[FACT]** `BV = (Defense × DefensiveFactor) + (Offense × SpeedFactor)`, then × pilot skill. `Defense = 2.5 × ArmorPoints + 1.5 × StructurePoints + 0.5 × Tonnage`. **Each term carries a type multiplier** — structure ×0.5 Industrial/Composite, ×2.0 Reinforced; engine ×1.0 standard, ×0.75 Clan XL, ×0.5 IS XL. **Defensive equipment (AMS = 32, ECM, probes, pods) is a flat additive block. Explosive ammo and Gauss criticals *subtract*.** Full floating-point precision is kept throughout and rounded **only at the very end**.

> **Multiply the things that multiply. Add the things that add.** Mobility and crew quality are multipliers; armour and weapons are addends. The same architecture appears independently in SoBH, One Page Rules, and Hero System — **four systems, no shared lineage.**

⚠️ **And the threshold bug is visible in print:** weapons dealing 60+ damage get a flat **20% BV bonus**, so the AC/20 pays a premium and the AC/10 pays nothing, with no gradation between.

**Games Workshop's own published formulas — two complete construction kits they later disowned.**

*Rogue Trader (1987)* **[FACT — verified verbatim against two archive scans]**: additive per-characteristic deltas from a human baseline (**human = 5 points**), then a non-linear multiplier band, then flat equipment. The admission is theirs: *"Values worked out from the formula given above tend to **undervalue the larger creatures**. To compensate for this a modifier is applied to any creature whose points value works out greater than 10."* Bands: 11–15 ×1½ · 16–20 ×2 · 21–30 ×3 · 31–40 ×4 … 91–100 ×10. **GW identified and patched the super-linearity problem in 1987 and printed the fix.**
⚠️ **[CONSENSUS, not FACT]** The per-characteristic modifier table is a graphic **destroyed in both OCR passes**; the circulating community transcription could not be verified. **The method is published fact; the individual numbers are not.**

*The Vehicle Design Rules* (Jervis Johnson, WD251 / Chapter Approved 2001) **[FACT]**: buy armour per facing → **the sum of all four facings becomes a scalar budget (36–56) that simultaneously gates hull class, speed class, and the open-top modifier** → add weapons from **race-specific** charts → apply percentage upgrades (**Gun Battery +50% · Shorter Barrel −25% · Slower Rate of Fire −25% · Titan-Killer +50%**).

> **And weapons are priced by race AND by Ballistic Skill: Heavy Bolter +20 at BS4 / +15 at BS3; Lascannon +35 / +25. The same gun costs more on a better shooter — the cleanest published solution to platform dependence found anywhere.**

Step 2 is the underrated one: **one number derived from your defensive spend then gates three unrelated things**, stopping "heavily armoured *and* fast *and* open-topped" without a single restriction rule.

And the anti-abuse governor is **not mathematical** **[FACT]**: *"It is VITAL that people using the VDR obey 'The Most Important Rule', which is that in order to use a vehicle created with the VDR it MUST be represented by a **PAINTED WYSIWYG MODEL**… Almost all of the arguments I've seen for unlikely 'game-winning' vehicles fall down on the fact that the author is clearly never going to be able to produce a painted wysiwyg model."* **Jervis Johnson priced abuse in painting labour.** It was still exploitable ("Gatling Lascannon Skimmers"), and when GW revived VDR in 2018 it was restricted to **Open Play only** — the same quarantine move The Walking Dead made.

*Battlefleet Gothic* **[FACT]**: the semi-official **Smotherman Formula** (published in GW's own *BFG Magazine #2*, *"never made official"*) is purely linear-additive — Hits 5 · Shields 10 · Turrets 5 · Weapons Battery at 30/45/60cm = **1.5 / 3 / 4.5** per Strength (exactly ×1/×2/×3). **The interesting part is faction identity as an override layer:** Eldar **double** their Hits cost, **double** their speed cost, and pay a **+15 *"too many weapons on too small a ship"*** surcharge.

*Epic* — **the clearest argument against atomic costing anywhere** **[FACT]**: *"Applying points costs in Epic is more of an art than a science… It's to do with the way the attributes of a unit fits in **both with any formation it belongs to and with that formation's place in an army**."* **If your units are only meaningful inside a container, cost the container.**

**Bolt Action, Warmachine, the Rampant line and Horizon Wars** contribute the remaining structural lessons: **flat weapon prices on quality-priced bodies create an arbitrage** (§8.2); **Field Allowance is a per-entry cap independent of points — and Theme Forces *raise* FA for thematically-appropriate units, repurposing a restriction as a flavour unlock**; **"Javelins are −1 on cavalry and +1 on foot" is defensible context-pricing because Mersey can say why in one sentence, where GW couldn't**; Dragon Rampant clamps every derived cost (*"no unit's cost may be boosted above 10 points or reduced below 1 point"*) — **a floor and a ceiling on a derived cost is a cheap universal guard against every stacking exploit at once**; and Horizon Wars collapses cost and stat into one number (**Presence is simultaneously the unit's points cost and its close-combat value**) with **point-buy reserved for mechs and aircraft, everything else on fixed pre-costed profiles.**

## 30 · Infected — the armour idea from the wrong kind of game

*Immersion Studios, Oliver R. Shead. Sampler (50pp) + GM-screen card + adventure module. **Never primary** — the ~300pp core rulebook is not in the capture, and this is an RPG, not a wargame.*

**Hardness Rating** is a 0–5 ordinal ladder — Soft (unarmoured humans, unarmed strikes) · Blunt · Sharp · Fatal · Destructive · Annihilating (artillery, main battle tanks). **[FACT — original.pdf p.29]** Combat compares **tiers, not numbers**, and the **margin** decides everything:

| Margin | Result |
|---|---|
| Defender 2+ HR above attacker | **Attacker cannot deal damage at all** |
| Defender 1 HR above | Attacker deals half damage |
| Equal | Normal — roll to absorb as usual |
| Attacker 1 HR above | Defender absorbs half |
| Attacker 2+ HR above | **Defender cannot absorb at all** |

> *"Handgun (HR 2) vs Humvee (HR 4) — The handgun can shoot at the humvee all day, but it's not going to do anything but make a few scratches. **No damage is possible.**"* **[FACT — p.30]**

**Why it's worth logging despite the source quality.** Most armour systems only ever *scale* a save — more AP means a worse save, but the roll stays live. This puts **a hard floor and a hard ceiling on a 6-rung ladder**: cross it by 2 tiers in either direction and the roll stops mattering entirely. A pistol is *narratively incapable* of hurting a tank, stated as a rule rather than left to GM fiat.

**The honest objection** is that it's a discrete tier system, so bolting it onto a continuous numeric armour value means either running two parallel armour systems or replacing the numeric one wholesale. **[INFERENCE]** File it as the working precedent for "should light weapons auto-fail against heavy armour" — not as a drop-in.

## 31 · Necromunda homebrew — what thirty years of players kept re-adding

*17 of ~94 community PDFs read. **[COMMUNITY]** throughout — none of this is official, none playtested at commercial scale.*

**The one equipment-layer finding: rotating, Arbitrator-curated availability.** Two unrelated documents independently built the same tool. `lost-zone.pdf`'s **Trading Post Generator** and **Unemployment Office**: once per campaign week, the Arbitrator generates a **limited, randomised list** of buyable rare items or hireable Hangers-On, with an optional **Auction System** capping some items to `D3` total copies **for the entire campaign, allocated lowest-gang-rating-first**. `expanded-campaign.pdf`'s **Tavern Mechanic** — explicitly credited as *"inspired by… Heroes of Might and Magic"* — has the Arbitrator pick from a pool of Hired Guns each week and post them for recruitment.

**Why it works.** A static, always-available shop list makes the meta-game solvable — whoever has the most credits just buys the best thing. **Rotating a small curated selection turns "what can I buy" into a weekly event, and rationing scarce items by gang rating (lowest first) is a free, built-in catch-up mechanic riding on the same tool.** The cost is that it needs *someone* to run the generator.

**Also relevant:** `settlement-events` gates a shopping trip twice — *"You may visit up to **D3 locations** each time your gang goes into town"* **and** a shared **D66 Settlement Events** roll for the whole travelling party before any location is chosen. **A settlement stops being a passive shop the moment it can roll something *at* you.**

---
---

# PART FOUR — WHAT THIS REPORT DOES NOT COVER

Stated plainly so the next pass knows where to go.

- **Necromunda's Weapon Traits catalogue, Skills catalogue and Close Combat resolution** — identified, not fetched (rate limit mid-session). **This is the single largest hole.** The Trading Post *structure* is fully captured; the per-trait effects are not.
- **Fallout's Campaign Handbook** — defines the base Settlement/Caps loop and the full AI Response system that Homestead's Land and Natural Behavior rules both depend on. Not captured. Also uncaptured: 13 further Battle-Mode faction lists and *Into The Vault*.
- **Spectre Operations' 13 uncaptured supplements** — Frontlines v3, Aftermath, Jungle, Outbreak, Cosmic Horror, Criminal Element, Law Enforcement, Russian Forces, EOD rules, Baba Yaga, Blackout Rifle, plus three scenario packs. All clean text, all in the library.
- **Trench Crusade beyond New Antioch and the Heretic Legion** — the other faction armouries are referenced but only sampled.
- **Judge Dredd's full Armoury card deck** — the special rules for named cards are captured; the complete card list is not.
- **Infinity's weapon and equipment catalogue** — only the hacking/EW subsystem and the SWC cost figures were read. The main weapon list, ammunition types (AP/DA/EXP/Shock/Viral/Nanotech) and the wider equipment list are **[NOT FOUND]** in this corpus.
- **Malifaux's actual Upgrade Card catalogue** — the *rules governing* upgrades are verified; the card list is not.
- **Every game's vehicle armoury** beyond Spectre's price table and BLKOUT's damage-track design.
- **No source in the corpus publishes a derivation for its equipment prices**, with four exceptions: One Page Rules (recovered, verified 4/4), Song of Blades (derived, verified 34/34), BattleTech BV2 (fully public), and GW's VDR/Rogue Trader (published then disowned). **Everything else is hand-set and iterated.** That is itself the most robust finding in the report.

---

## Sources

- `research/sources/` — verbatim captures: zona-alfa · spectre-operations · fallout-wasteland-warfare (5 docs) · judge-dredd · fistful-of-lead · mad-dogs-with-guns · mordheim · necromunda · necromunda-campaigns · necromunda-homebrew · oathmark (3 docs) · last-days · infinity-hacking · infected
- `rules-vault/Research/Notes/` — 32 curated notes (mirror of the Obsidian vault; **edit the vault, not the mirror**)
- `rules-vault/Research/Wargaming Research Hub.md` — 446 rows, the human view
- `research/index.json` — 32 sources, machine-readable, the join key
- `docs/POINTS-RESEARCH.md` — §1 derived systems · §2 dual-currency · §6 failure modes · §7 per-system profiles · §8 recommendations
- `docs/BLKOUT-RULES-ANALYSIS.md` — §11 weapons & equipment · §12 multi-domain systems

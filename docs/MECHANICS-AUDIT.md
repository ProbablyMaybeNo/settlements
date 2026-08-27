# Mechanics Audit — Reality & Gameplay

**Date:** 2026-08-22  
**Scope:** Full rules vault + research corpus (32 sources, 235 hub rows).  
**Not used:** `Shortlist — Best Mechanics`. This list is independent.

Rules source of truth: `Full Rules System v1.md`. Research notes in `rules-vault/Research/Notes/`.

---

## What I filtered against

A mechanic had to do one of two jobs:

1. **Reality** — the table feels like a 2051 neighborhood under civil war, not a points-balanced arena.
2. **Gameplay** — a better decision, less argument, or a hole closed, without a new subsystem.

Anything that broke a locked law was adapted or rejected. Locked: `1d10 vs 7+`, WND 1 (max 3), 9–12 density, Credits / Materials / Power only, equal Crew Rating, binary structures, no saves / generic rerolls / ignore-cover-on-Injury, no Water, skills ride rank, objective-primary.

---

## Already doing the job — do not restock

These are solved. Research keeps rediscovering them. Leave them alone.

| Settlements already has | Research keeps selling as a steal |
|---|---|
| Equal rating every battle; growth = menu | Oathmark kingdom |
| Stashed gear = 0 Rating | Necromunda Rating vs Wealth (the *split* is still worth *naming*) |
| Skills / stats not sold in Credits | Frostgrave two currencies |
| Binary Functional / Disabled structures | Fallout structure HP (we correctly cut this) |
| Fate table + scars, no price change | Mordheim / Necromunda injury charts |
| Dodge, Snap Shot, Hidden | BLKOUT Juke / FoL Hide |
| Power assigned each Settlement Phase | — this *is* the 2051 blackout |
| Housing + equipment slots | Last Days Empty Spaces, Gaslands unbuyable slots |
| Location founding grant | Necromunda location (they also cap categories — see below) |
| Sabotage fuse, 30 Materials repair | — |
| Objective scenarios, not annihilation | — |
| Isolated territory suspends benefit | Oathmark occupied-never-destroyed (push further) |

---

## Reality — my list

Ranked. Steal the mechanism, not the flavour.

### R1. Noise is an attribute. Shooting manufactures the threat.

**From:** Last Days Menace Phase + `Noisy X`. Confirmed independently by Zona Alfa Hot Spots and TWD walkers.

**Mechanism:** Every shot, explosion, and breach drops Noise on that square (or fighter). End Phase: `1d10 + Noise vs 7+` draws a Neutral Contact onto the nearest table edge, or pulls existing neutrals toward the noisiest square. `Noisy X` is a tag on weapons / vehicles / tools — one skill (Stalker-shape) cancels run-noise only.

**Why it feels real:** You do not empty a magazine on a residential street for free. The neighborhood hears you.

**Settlements fit:** End Phase already exists. Same TN 7+. Neutrals are not zombies — militia patrol, panicked civilians, a drone, a rival scout team. Needs a four-rule AI (see R3). Do **not** add ammo tokens; we have no ammo track and should not grow one.

**Cost:** One counter type + one End Phase check. Highest reality return in the whole corpus.

### R2. Three alert states. Not a stealth game.

**From:** Spectre Operations Unaware / Uneasy / Alert. FoL Hide/Spot is the cheap cousin.

**Mechanism:** Neutrals and raid-defenders start **Unaware** or **Uneasy**. Unsuppressed fire = auto Alert in range. Suppressed / melee = roll. Alert unlocks Reactions and full Orders. Player crews in a pitched battle start Alert — do not track this on both sides every game.

**Raid overlay (Fallout Watch Tower):** A powered Scout Post or Watchtower lets the defender start Alert and deploy knowing the attack is coming. None powered: defender starts Uneasy, attacker places second.

**Why it feels real:** Neighborhood fights start quiet. Intelligence is a building, not a buff.

**Do not take:** Spectre Cover Level (decaying disguise number). Too much tracking for WND-1 crews.

### R3. The board bites when you loot.

**From:** Zona Alfa 3″ Reaction Radius + Bolt Toss. Fallout Investigation → Searchable markers.

**Mechanism:** Interact (search / loot / breach) on a marked cache first activates anything in 3″. Clear it, then search once. A thrown object can trigger the radius remotely.

**Why it feels real:** Kicking in a pharmacy door is never quiet.

**Settlements fit:** We already have a Search table. This is the missing half — the table was a loot lottery with no consequence. Pair with R1: the Interact can also drop Noise.

**AI (Last Days / Zona / TWD all converged):** nearest visible → noisiest if none visible → retarget if blocked → idle. Four rules. Do not write a random AI table.

### R4. Infrastructure is two-way.

**From:** Infinity Repeaters. Candidate-games sweep found **no** published skirmish EW/jamming layer — if we want jamming, we invent it.

**Mechanism:** Comms Mast, Server Core, EW Mast, and scenario terminals extend *your* hack range. An enemy hacker inside the zone can use the same node at −2 (inside ±3). You stop a hack by interrupting the hacker, not by shooting the mast.

**Why it feels real:** You occupy the neighborhood grid. You do not own it.

**Do not take:** Infinity program families. Corvus Belli spent three editions shrinking that. Our v1 Interrupt is the right size.

### R5. Structures lease capability. Lose the building, lose the unlock.

**From:** Last Days — lose the Stable, horses leave the roster.

**Mechanism:** Disabled is not just “no worker bonus.”
- Workshop / Fabricator Disabled → in-progress craft is lost.
- Drone Bay Disabled → drones stay owned, cannot be fielded this Crew Rating window.
- Armory Disabled → equipment cap reverts to the previous tier until repaired.
- Generator Disabled → Power is reassigned; something else goes dark.

**Why it feels real:** Capability is rented from the lot. Sabotage becomes a reason to raid.

**Settlements fit:** Binary structures already. This gives sabotage a second sentence of teeth without structure HP.

### R6. Occupied, never deleted. Supply is a path.

**From:** Oathmark occupation. Necromunda Road Sections + Isolated. Our Isolated state is the seed.

**Mechanism:** Losing a territory flips it to Occupied / Contested. The card stays on the map. Benefit suspends until you hold a path of friendly or neutral territories back to HQ. No path → gatherer output halves and Dispatch cannot target that card.

**Why it feels real:** You do not erase a neighborhood by winning one fight. You also cannot eat a farm you cannot reach.

**Do not take:** Necromunda 3× kill-ratio to flip a territory. That makes kills the map engine. We are objective-primary.

### R7. Named landmarks, uneven, takeable not buyable.

**From:** Mad Dogs named sites (Gambling ×3, Protection ×0). Oathmark unique territories.

**Mechanism:** 4–6 city landmarks (substation, hospital, radio mast, scrap river, motorway junction, national-guard lockup). One copy each. Occupy then claim. Qualitative access only — a scenario weighting, a loot table, a legal Structure category for a Forward Position. Never +DEX, never extra Crew Rating.

**Why it feels real:** Not every block is the same empty tile.

### R8. Founding location also shapes the lot.

**From:** Necromunda Settlement Locations — one pick sets three category caps.

**Mechanism:** Keep the free structure. Add a **soft** category lean, not a lock. Hospital: Recover structures cost −20 Materials or you may build one extra Recover over the footprint comfort. Armory location: same for Defend. Scrapyard: Convert. Farm: Sustain.

**Why it feels real:** A hospital campus does not become a fortress as cheaply as a guard armory.

### R9. Capturability lives on the weapon.

**From:** Judge Dredd Stun / Injury fork.

**Mechanism:** A **Less-lethal** tag (sidearm beanbag, shock baton, smoke-into-capture). Down from that weapon never rolls Dead on Fate — Captured-eligible only. Live ammo uses the normal table. Holding Cells finally have a pipeline.

**Why it feels real:** This is a civil war among neighbors, not an extermination.

### R10. What you did writes the next event.

**From:** Judge Dredd Crime Ledger. (Heat/Attention was correctly cut as a *track*. This is not a track.)

**Mechanism:** After a raid, tally two flags: **Brutal** (2+ structures sabotaged, or a Downed fighter finished) and **Quiet** (loot only, no sabotage). Next Settlement Event — when that table is drafted — is drawn from the matching column. No running Heat number.

**Why it feels real:** The neighborhood remembers the last visit. Bookkeeping is two checkboxes.

### R11. Market price falls when everyone dumps.

**From:** Mordheim wyrdstone (price falls with batch size *and* warband size).

**Mechanism:** Trader conversion is not a fixed 2:1. If stored Materials at this settlement are over half the Storehouse, or if the table converted a lot last Phase, the rate worsens one step. Hoarding brake inside the exchange rate. No Water, no per-head tax.

**Why it feels real:** You flooded the only scrap buyer in the district.

**Also closes:** the open economy-sink question in `Economy.md`.

### R12. Weather and season sit before the game.

**From:** Last Days Seasons — 2D6 weather, LOS / difficult / fire line, never touches the combat engine.

**Mechanism:** Our Events table already rolls twice in battle. Keep weather as a pre-game Twist reskin. Do not add Hunger / Thirst / Warmth. Last Days *Seasons* is the natural experiment: the same designer shipped zero upkeep in core, then bolted four conditions into the supplement at real table-time cost. We already made that call.

---

## Gameplay — my list

Ranked. These make the campaign and the roster better to *play*.

### G1. Print two numbers: Rating and Wealth.

**From:** Necromunda, 1995 and 2023, same rule, four independent statements.

We already *behave* this way. We do not *name* it. The sheet needs **Crew Rating** (fielded Credits) and **Wealth** (banked Credits + stashed gear). Arguments die when the stash has a name.

### G2. Every catalogue line has a price *and* a LIMIT.

**From:** Trench Crusade. Kill Team slots are the cousin.

`LIMIT` caps **purchase**, not possession. Loot can break it. Apply to Heavy Ranged, Turret Mount, Exploit Suite, drones. Rank already gates class; LIMIT stops “everyone bought two.” Equipment Shed slots stay as the *stash* cap; LIMIT is the *type* cap.

### G3. Print the rating ladder. Kill the 850 / 1000 / 425 / 500 fight.

**From:** Trench Crusade threshold schedule. Judge Dredd Early / Mid / Late Notoriety.

Same number for both players, every battle, on a printed track. Suggested:

| Season battles played (per player) | Crew Rating |
|---|---|
| 1–3 | 500 |
| 4–6 | 750 |
| 7–10 | 1000 |

Match Play outside a Season: pick one row and both use it. Master note currently says 850 / 425. Phase notes say 1000 / 500. Pick one and propagate. The ladder is the design; the exact rungs can move after sim.

### G4. Catch-up is a choice with a price, not a +1 forever.

**From:** Trench Crusade rubber band (skip Exploration, sell unassigned, empty treasury). Necromunda House Patronage (gap → temporary spend).

Two tools, different jobs:

- **Rebuild (between battles):** after a lost raid or a 2-loss streak, skip Dispatch, empty the treasury, repair all Disabled, restock to the current ladder rung. The loser opts in.
- **Patronage (this battle only):** Rating gap ≥ 200 → 1 token per 200, cap 3. Spend on Ready / free Stabilize / one Search. Never +1 to hit. Expires End Phase of the game.

Underdog Priority +1 can stay as the tiny residual.

### G5. Post-battle sequence, Rating updated last.

**From:** Necromunda seven-step loop.

Write the order into Downtime: Fate → Levels → bank Resources → Settlement actions (build, workers, Power, Dispatch, hire) → **then** recalc Rating / Wealth. Hiring and rescue eligibility read a frozen number.

### G6. One job per structure.

**From:** Last Days three payoff channels — Capacity, Economy, Battle.

Audit the 23. Each entry is exactly one channel. HQ is the allowed exception (housing + Dispatch). Anything else that buffs the firefight *and* prints income is doing two jobs and will be auto-take.

This is also the Forward Position rule, restated: **one Active System per away battle.** Last Days keeps almost the entire Refuge off ordinary encounters. We should too.

### G7. One subplot deck. Deeds stay post-battle.

**From:** Necromunda Intrigues. Designer warning in the same book: do not stack a second subplot system.

Draw 2, claim 1 when the criterion is met. Texture for “why this block tonight.” Glorious Deeds stay a post-battle XP source. They are not a second in-game objective layer.

### G8. Unspent Rating becomes a capped kit, this game only.

**From:** Malifaux leftover Soulstones.

Unspent Crew Rating up to 40 converts to one-use kit for *this* battle (Med-Kit, smoke, extra less-lethal). Nothing wasted, hoarding bounded. Does not persist.

### G9. Cheap faction identity: out-of-theme costs more.

**From:** Malifaux keyword tax (+1 if no shared keyword). Trench Crusade faction-as-economy-edit.

+10 Credits on a weapon or structure that fights the Location / faction lean. No bans. No second price list. Hospital crew can still buy the turret. They just pay the tax.

### G10. Elevation drops cover one tier.

**From:** Zona Alfa.

One sentence. Replaces or absorbs “2″+ ignores Light.” High ground becomes a reason, not just a LOS trick.

### G11. WND 1 + Stress 2 = Bolt. Leaders still roll.

**From:** Fistful of Lead — Shock > remaining Wounds, no morale roll.

We already Break-test at 2+ Stress. For Recruits and Fighters (WND 1, 0 Orders) make it automatic. Specialists and Leaders still roll `1d10 + NRV`. Faster, more brutal, matches the WND-1 law. Crew-wide bottling stays parked.

### G12. Hiring comes back as a rotating board, not a shop.

**From:** Necromunda homebrew — two unrelated docs invented the same weekly curated pool. Official Recruiting Board was cut; the hole is still there.

Each Settlement Phase: roll 3 available hires (or 3 rare items). First claim. If nobody wants the cheapest, it attaches to the lowest-Wealth crew until they are no longer last. Catch-up rides inside the flavour.

### G13. Season awards, not one emperor.

**From:** Homebrew six-category Triumphs. Our Season Score is the seed.

Keep Control-4 as an instant win. After 10 battles, award Builder / Raider / Survivor / Controller from the same sheet. Several stories, one Season.

### G14. Chosen retirement is legal.

**From:** Zona Alfa 10,000 Ruble Plan. Fistful Renown 20 → Showdown.

If you want out: bank a printed Wealth threshold *and* hold 4 territories, declare the settlement stands down. It persists as an NPC lot. Sidesteps infinite snowball by giving a door.

---

## Rejected — looked good, I passed

| Mechanic | Why it dies here |
|---|---|
| Fallout Caps + Resources upkeep | Second maintain-currency. We cut this shape on purpose. |
| Last Days Seasons Hunger / Thirst / Warmth | Same designer’s own proof that earnest upkeep eats the evening. Water stays dead. |
| Mad Dogs Reputation from banked cash | Wealth-gates-wealth. The bribery system in the same book cannot save it. |
| Necromunda 3× OOA to flip territory | Makes kills the map. Objective-primary forbids it. |
| Oathmark Battle Honour rerolls | No generic rerolls. Honour-as-spendable-power is interesting; the reroll is not. |
| Spectre Cover Level | Third tracked number on a WND-1 model. |
| Infinity deep hacking / TAG possession | They spent three editions deleting it. |
| Fistful card deck + Quality Die | Second randomiser. Locked one-die-type. |
| Lost Zone Reputation-as-currency | Diagnoses a real problem, cures it with a second economy. |
| Per-fighter downtime action | Bookkeeping bomb at our crew sizes. Dispatch 1–3 by HQ is the right size. |
| Fallout Power Armor two-stage HP | Structure-HP we cut, moved onto a backpack. |
| Trench Crusade Glory as money | We have Deeds. Do not mint a second coin. |
| Crew-wide bottling as the default | Individual rout is enough until playtest says otherwise. |

---

## Holes the corpus cannot fill

The research is thick on settlement, campaign snowball, injury, and neutral threats. It is thin where Settlements is actually distinctive:

1. **Electronic warfare / jamming / signal denial.** The candidate-games sweep found no published skirmish implementation. EW Mast is ours to invent. Keep it one verb (jam a node / strip a Reaction / drop a drone’s Bandwidth) on the existing INT test.
2. **Civilians as a *place* cost, not a unit type.** Parked in Out of Scope — but R1 + R3 + R10 get most of the feel without fielding civilian models.
3. **Away-board player structures.** Research says keep the base off ordinary fights (Last Days) *or* scale a Settlement Attack budget with Land (Fallout). Our Forward Position / one Active System is the right hybrid. Nothing in the corpus solves provenance better than that.
4. **Diplomacy with teeth in 2-player.** Homebrew hidden betrayal needs a third party. For two players, stage betrayal as a scenario (The Meet) or use a non-reciprocal faction grid (Zona Alfa 6×6). Do not start Diplomacy with a reputation economy.

---

## Suggested first slice

If only five things move into the master note next:

1. **R1** Noise + Neutral Contact  
2. **G1 + G3** Name Wealth; print the rating ladder  
3. **G2** LIMIT on the catalogue  
4. **R5** Disabled strips the unlock  
5. **G4** Opt-in rebuild + patronage tokens  

That set makes raids feel like raids, makes the campaign sheet honest, and gives the economy a sink that is not Water.

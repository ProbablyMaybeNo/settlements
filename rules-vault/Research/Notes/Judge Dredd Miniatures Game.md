---
type: research-note
title: Judge Dredd Miniatures Game
game: Judge Dredd Miniatures Game
publisher: Warlord Games
designer: Dylan Owen
depth: primary — full 164-page rulebook read in full
retrieved: 2026-08-21
source_url:
capture: research/sources/judge-dredd/
tags: [settlements/research]
---
# 🎲 Judge Dredd Miniatures Game

> [!abstract] In one breath
> Judges vs perp gangs in Mega-City One, dice-pool skirmish with a chip-bag activation — genre-standard on the table, but its **campaign layer converts battlefield conduct directly into consequences**: a knockout is tagged **Stun** or **Injury** by the weapon that caused it, and that tag — not the roll, not the range — decides whether the loser goes to the **Iso-Cubes** (arrestable, held, campaign thread continues) or **Resyk** (a death roll). Sentences are itemised from an actual crime code keyed to in-game actions. Settlements already has a mature **Captured** thread on its own Fate table — this note is not "we have nothing," it's **the one clean idea that thread is still missing**: making capturability a *weapon property a player chooses*, not an accident of how the wound was rolled.

| | |
|---|---|
| **Publisher · designer** | Warlord Games · Dylan Owen (2020) |
| **Scale / format** | Objective-driven skirmish, Notoriety-budgeted (Small 10–25 / Medium 26–50 / Large 50+ Notoriety — roughly 3 to 15+ models a side depending on the roster) |
| **Core resolution** | Dice-pool: roll **N Combat dice** (a d6 with faces `[HIT]×3 / [ARMOUR]×2 / [SPECIAL]×1`) where **N = the relevant stat** (Shoot/Fight/Evade/Resist/Cool); count successes. A stat test needs at least one `[SPECIAL]` to pass |
| **Depth of read** | **Primary** — full 164-page rulebook read cover to cover |
| **Raw capture** | `research/sources/judge-dredd/` in the Settlements repo |
| **Source** | Warlord Games, 2020. Library master: `G:\My Drive\Wargaming\Judge dredd\Miniatures Games (Judge Dredd, Strontium Dog, Slaine)\` |

---
## Why it's here

Ross's probe flagged this book on keyword density — robot ×110, campaign ×73, perp ×54 — expecting a deep robot subsystem and a strong asymmetric Judges-vs-perps design. The robot count turned out to be a trap (see **What it gets wrong**, below), but the campaign and perp density was real, and it converges on exactly Settlements' declared want list: **non-lethal objectives**, **asymmetric scenario balancing**, and **persistent campaign stakes for a captured fighter**. It also independently re-derives two mechanics Settlements has already locked (fixed-schedule budget escalation with catch-up, and rating-gap-scaled underdog bonuses) — useful as corroborating precedent, not as new information.

---
## The Stun/Injury fork — capturability as a weapon property, not a coin-flip

**Type:** Damage/Campaign · **Take:** ⭐ steal

Every hit that reduces a model's `Cool` to zero takes it out of the fight, but **how** it got there is tracked separately and matters afterwards. Two marker types both drain `Cool`:

- **Stunned** — all stats (including Move) reduced by 1 per marker; removable in-game with a Shake It Off action. **[FACT — p.9]**
- **Injury** — all stats reduced by 1 per marker; removable in-game only with a Hunker Down double-action, and persists for the rest of the game. **[FACT — p.23]**

If `Cool` hits zero from **Stun markers only**, the model is **Subdued**. If **any Injury marker** contributed, it's **Incapacitated** instead:

> *"A model that is reduced to zero Cool by Stun markers only is said to [have] been subdued instead of incapacitated. This is important to note for when you need to sentence perps – the subdued ones have a better chance of ending up in iso‐cubes rather than in Resyk."* **[FACT — p.23]**

The type, not the severity, is what the post-game roll cares about: an **Incapacitated** model rolls Resist at game's end — fail, and it's Resyk (removed, permanently, from a campaign roster); a **Subdued** model instead rolls Cool to try to escape, and on a fail (with Judges present) it is simply arrested and proceeds to sentencing — **no death roll at all**. **[FACT — p.142]**

**Why it works.** This decouples "can this model be captured" from *how it was taken down mechanically* (range vs melee, which weapon type) and re-couples it to *what the weapon was tagged as*. A stun baton, a Stumm Gas grenade, or a beanbag round can take a target to zero Cool exactly as fatally-effective as a bullet, in exactly the same number of hits — the only difference is which marker they lay down. That means **a crew can choose, at list-building time, to run a "no-kill" loadout** and the game's own resolution honours that choice at the point of impact, not as a narrative gloss applied after the fact.

**For Settlements.** This is **not** a gap in Settlements' rules — [[Campaign#Post-battle — the Fate table]] already has a mature **Captured** result (Fate 4–5, Recruits/Fighters only, full ransom/rescue-raid/brainwash sequence). What Settlements' [[Damage]] currently lacks is the *lever* JDMG has: our Down/Out-of-Action split is keyed to **range vs melee** (`Damage.md`: *"Down if the wound was ranged/hazard, or straight to Out of Action if it was melee"*) — an accident of attack type, not a property either side chose. There is currently no way for a crew to deliberately field a **non-lethal weapon tag** that shifts a kill toward Captured regardless of range or melee. Adding one — a `[Non-Lethal]` weapon property that forces **Down** (never straight to **Out of Action**) even on a melee finish, feeding into the existing Fate table exactly as-is — would give "bring stun batons, we're doing a bounty job, not a hit" real mechanical teeth without touching the Fate table at all. Honest cost: one new weapon tag, one Damage.md exception clause, and a design call on whether `[Non-Lethal]` weapons should be cheaper, weaker, or otherwise balanced against lethal equivalents (JDMG doesn't answer this — Stumm Gas and a stub gun are priced on their stats, not on their tag). See [[Weapons]], [[Damage]], [[Campaign]].

---
## The Crime Ledger — sentences are built from actions taken, not from a single post-game roll

**Type:** Campaign/Scenarios · **Take:** ⭐ steal (structural pattern, not the literal table)

Sentencing is not a flat lookup on the Fate-style capture result. It's an itemised crime code — sixteen sections, from Homicide down to Public Nuisance — keyed directly to actions taken **during the game itself**:

> *"In game terms, inflicting an Injury marker is grievous bodily harm and stuns are actual bodily harm."* **[FACT — p.126]**
> *"In game terms any time a model is incapacitated there's a chance it will be murder. See scenario sentencing for survival rolls."* **[FACT — p.126]**
> *"Refusing to surrender when challenged is resisting arrest, fighting back is definitely obstructing a Judge in their duty."* **[FACT — p.127]**

Firing a gun at all is Criminal Damage; using an explosive or heavy weapon is *mandatory* Criminal Damage; gunfire itself can be charged as Noise Pollution. **[FACT — p.126–127]** Charges **stack** as separate counts — a perp caught with six stolen wallets is six counts, "possibly both" dunking and receiving. **[FACT — p.126]** Sentences resolve as fixed years, dice-rolled years (`D6+2`, `2D6+3`), or a variable range left to the arresting Judge's discretion.

**Why it works.** The consequence a captured model faces is **derived from what actually happened in the game**, not from a single die roll made after the fact. A perp who shot at a Judge, used an incendiary, and got caught fighting is objectively worse off than one who was simply present — the ledger reads that difference off the battle log instead of needing a bespoke severity table.

**Honest caution — don't import the table's actual weights.** *Judge Dredd* is a satire of totalitarian over-policing, and the table is written to be absurd on purpose: *"Boinging® in a public place: 20 years fixed"* sits next to *"Premeditated murder: 15 years to Life"* — a recreational activity carrying a **longer minimum** sentence than a killing. That's the joke, not a balance choice, and importing it wholesale would create bizarre incentives in a game that isn't trying to be satire.

**For Settlements.** The transferable idea is **"log what happened, don't just roll a result"** — directly serviceable for a future **arrest/bounty objective type** in [[Scenarios]] (none exists there today — checked, [NOT FOUND]). A scenario could score "clean capture" (subdued, no Injury markers on the target) above "captured but roughed up" above "killed," feeding a Territory or Deed reward scaled to *how* the objective was completed — reusing the Stun/Injury fork above as the input signal, rather than building a parallel tracking system. [[Scenarios]], [[Territory]].

---
## Sentencing, Iso-Cubes, and the jailbreak loop

**Type:** Campaign · **Take:** ⚙️ adapt (corroborates, doesn't replace, the existing Captured thread)

Once sentenced, a model sits in the Iso-Cubes, unavailable until its term is served, checked each missed game on a d6-style Custody roll: stay in custody, early release (possibly injured), or die in custody and get struck from the roster permanently. **[FACT — p.144]** The book explicitly floats jailbreak as an unbuilt extension, not a shipped scenario:

> *"Models sent to the cubes might be broken out using a variant of the Raid or Heist scenarios, with cache markers replaced by shackled prisoners."* **[FACT — p.151]**

Notably, the security-tier flavour text (*"A high security Iso‐Cube facility... is a very different prospect to a Cursed Earth penal farming colony under intermittent mutie raider attack"*, p.142) is **narrative colour only** — there is no mechanical tier table anywhere in the book. **[NOT FOUND]** — if Settlements ever wants graduated holding-security, JDMG doesn't hand you one, just the idea that it should exist.

**For Settlements.** This is close kin to the already-built [[Campaign#Captured — resolution]] rescue-raid/ransom/brainwash sequence, arrived at independently. The one thing JDMG's version has that ours doesn't: **the captor's own next-game absence risk** — a held prisoner can die in custody or escape *without either player initiating anything*, a small passive tension-clock our version doesn't currently have (ours only resolves on ransom/brainwash/rescue-raid, all player-initiated). Minor, but cheap if wanted: a d10 "did anything happen to the prisoner" check on the captor's own Settlement Phase, orthogonal to whether a rescue raid was attempted. [[Campaign]], [[Territory]].

---
## Deeds — the losing side still earns advancement currency

**Type:** Progression · **Take:** ⚙️ adapt

Deeds (the promotion-track currency) are earned for the expected things — incapacitating a stronger foe, surviving a scenario, winning the game — but also, explicitly, by the losing side:

> *"Being sentenced to 10 years or more in the cubes earns the model a Deed for each ten years or part thereof of its sentence."* **[FACT — p.146]**

**Why it works.** Getting caught is still, mechanically, *something happened to you that mattered* — a heavily-sentenced perp becomes a harder, more storied character even while off the roster serving time, rather than a pure write-off for their owner.

**For Settlements.** [[Progression]]'s current **Glorious Deed** table (Daredevil, Wrecking Crew, Duelist, etc., [[Campaign#Glorious Deeds]]) is earned entirely by things done *during* the battle — nothing rewards the fighter who ends up **Captured** afterward. A one-line addition — a captured fighter banks a small Level-trigger credit scaled to how long they're held, independent of whether the rescue/ransom/brainwash thread resolves in their favour — would close that gap cheaply, and slots directly into the existing 6-source soft cap rather than requiring a new track. [[Progression]], [[Campaign]].

---
## Underdog Big Meg Cards — a bonus resource that scales with the gap, not the scoreboard

**Type:** Balance/Scenarios · **Take:** 📎 reference (independent corroboration of an already-locked pattern)

> *"A faction with a lower starting Notoriety than their opponent may gain extra Big Meg cards at the start of the game to help balance their chances. For every full 10 points of Notoriety less than the other side, rounding up, the underdog gains an extra Big Meg card."* **[FACT — p.56]**

Big Meg cards are one-shot wildcard effects (extra Action chips, card-draw tricks, tactical reversals) drawn at Set Up and playable between activations. The underdog bonus scales the *hand size*, not the stat line.

**Why it works.** Same shape as the Necromunda/Mordheim rating-gap banding already logged in [[Necromunda and Mordheim#Underdog banding]] — self-adjusting, no tuning knob, and it disappears the moment the gap closes. JDMG independently reaches the identical structure (scale by *difference*, never by win/loss record) with a different resource type (cards, not a stat bonus).

**For Settlements.** No action needed — this is corroboration, not a new proposal, for an already-adopted design principle. Worth citing the next time that banding pattern needs a second published precedent. [[Balance]], [[Campaign]].

---
## Informers — paying a campaign resource to bias which scenario role you get

**Type:** Scenarios/Economy · **Take:** ⚙️ adapt

A base upgrade, bought like any other faction asset:

> *"Players may spend Notoriety to employ Informers. When determining which side takes which role in a scenario (i.e. attacker or defender), before rolling the dice, a faction may expend an Informer to add one to the roll... Factions secretly write down how many Informers they wish to use and reveal their intentions together."* **[FACT — p.150]**

**Why it works.** It's a cheap, secret-bid lever over an asymmetric decision (who attacks, who defends) that would otherwise be a flat coin-flip, without touching the scenario's actual objective design. The simultaneous-reveal bidding also adds a small bluffing layer for a single Notoriety-cost item.

**For Settlements.** Directly applicable if [[Scenarios]] ever gets role-asymmetric objectives (attacker/defender, raider/defender of a Territory) and wants a resource sink that isn't combat-facing. Cheap to add: a Territory upgrade or a Resource spend that nudges a d10 role-assignment roll. [[Scenarios]], [[Territory]], [[Economy]].

---
## The Notoriety phase ceiling — fixed schedule, catch-up top-up, never performance-tied

**Type:** Campaign/Economy · **Take:** 📎 reference (independent corroboration of an already-locked mechanic)

The campaign is split into Early/Mid/Late phases with hard Notoriety ceilings (25 / 50 / 75) that rise **on the printed schedule regardless of how any given faction is doing**:

> *"Players with rosters that are below the requisite Notoriety get the difference to spend in each game, to make up any shortfall."* **[FACT — p.141]**

**Why it works.** A faction that's lost fighters isn't punished twice — once for the losses, again by a lower budget ceiling than the schedule says they should have. The schedule escalates for everyone identically; only the roster you've actually built determines what you spend it on.

**For Settlements.** Confirms, independently, the same shape already committed to in [[Campaign]]/[[Progression]] — budget ceilings that escalate on a fixed calendar, not tied to who's winning. This is the same principle already logged from [[Trench Crusade#The published threshold ladder]] (*"Everyone's ceiling rises on the same printed ladder... regardless of who is winning"*); JDMG is a second independent data point for it, not a new one. No change proposed.

---
## Base Upgrades — one currency buys crew, base defences, and one-off campaign resources alike

**Type:** Economy/Territory · **Take:** ⚙️ adapt (the fire-arc costing formula), 📎 reference (the single-currency shape)

Notoriety — the same number that buys a model — also buys **Turf** (D6 bonus Notoriety per game, lost if unused that game), a **Weapons Locker** (3D6 bonus Notoriety for one-off purchases per campaign phase), a **Workshop** (repairs a robot per game), **Bolthole/Emergency Evac** (auto-saves a Subdued model from a Cool test), and fixed **Home Base Defences**. **[FACT — pp.148–150]**

Placed Guns price their firing arc as a percentage surcharge on the weapon's own cost:

> *"Forward focused... +25% · Forward... +50% · All round... +100%. Round up to the nearest point of Notoriety."* **[FACT — p.149]**

An Auto-Turret upgrade (fixed +3 Notoriety) starts each turn in Overwatch, fires without a crew, and — the honest risk — malfunctions on a roll of 1 if a *friendly* model crosses its arc, firing on them anyway. **[FACT — p.149]**

**Why it works.** No second currency exists for base-building — it's a genuine single-economy proof-of-concept at exactly the scale Settlements cares about (units *and* fixed defences *and* campaign-only resources, one pool). The fire-arc percentage formula is a clean, reusable costing pattern: field-of-fire is priced as a multiplier on the weapon underneath it, not as a flat tax.

**For Settlements.** Direct precedent for our own single-currency tenet — never propose a second player-facing currency — confirmed working at the base-defence layer specifically, which is exactly where a second currency is most tempting to reach for. If [[Structures]] or [[Territory]] ever prices a fixed defensive emplacement, the arc-based percentage surcharge (rather than a flat Credits cost per arc) is directly reusable, and the auto-turret's friendly-fire risk is a cheap, honest downside for an otherwise-free defensive asset. [[Structures]], [[Territory]], [[Economy]].

---
## Grudge Points — a two-faction nemesis track

**Type:** Campaign/Narrative · **Take:** 📎 reference

Gang/Citi‐Def Leaders (not Judges) accrue Grudge Points against a specific rival leader — for Deeds the rival earned, for the leader's own crew taking Serious/Acute wounds, and for defending against a Raid/Heist/Ambush — cashed in as a bonus the next time those two specific factions meet. **[FACT — p.150]**

**For Settlements.** Minor, campaign-flavour only — a persistent grudge/rivalry counter between two specific players (not the general campaign) is a cheap narrative hook for [[Narrative]] or [[Diplomacy]] if a nemesis system is ever wanted, but nothing here is load-bearing enough to prioritise. [[Narrative]], [[Diplomacy]].

---
## Robots — a keyword, not a subsystem (and a lesson about probe counts)

**Type:** List Building · **Take:** 📎 reference (correctly scoped — this is thin)

Every robot in the book (UtilBot, MediBot, Auto-Turret, etc.) is a normal roster entry costed in Notoriety like anything else, carrying exactly one recurring special rule:

> *"Robots can only generate normal Action chips, never Star chips (although a Star chip can be used to activate a robot). Robots are also unaffected by Psi Skills."* **[FACT — p.110, repeated verbatim on every robot profile]**

That's the entire mechanical footprint. The 110-hit word count that made this look like a priority was mostly repeated flavour text (the same one-line rule copy-pasted onto every profile, plus lore about the 2099 and 2021 Robot Wars) — not 110 distinct mechanical touchpoints.

**What it gets wrong (methodology, not the game).** A keyword-frequency probe measures *repetition*, not *density* — a rule stamped on fifteen unit profiles counts fifteen times but is one rule. Worth remembering the next time a probe count sets expectations before the read.

**For Settlements.** Doesn't feed the thin tech layer or the drone-operator want the way the brief hoped — there's no drone/robot control subsystem here, just a Notoriety-costed unit type with a narrow activation-economy carve-out. If anything it's a caution: **"Robot" here is a tag that removes access to two specific systems (a premium activation resource, Psi effects) rather than adding a new one** — a pattern (tag-gates-access-to-an-existing-system, rather than tag-adds-a-new-system) that's cheap to imitate if Settlements' own robot/drone entries need a similarly narrow carve-out instead of a parallel subsystem.

---
## What it gets wrong

- **The robot probe-count trap**, above — the single clearest lesson in this read for how *not* to scope a source before reading it.
- **Hacking and stealth, checked and closed.** Both flagged by the probe (3 hits each) and both thin on inspection: "hacking" is flavour text for one Armoury-card effect on a single named character (discard an opponent's Armoury card); "stealth" is a single Armoury card (Stealth Suit: +1 Evade, immune to detection/Overwatch while worn) with no supporting stealth/noise subsystem anywhere else in the book. **[NOT FOUND]** — neither is worth a dedicated hub row, and this closes the question of whether the rest of the 77-file Judge Dredd folder is worth digging into for stealth mechanics specifically: this book, at least, has none to find.
- **The Crime Ledger's actual numbers are satire, not balance** — see the caution in that section above. The structure is the steal; the weights are the joke.
- **Core resolution and activation are unremarkable, on purpose.** The Combat-dice pool (roll N dice sized by your stat, count `[SPECIAL]`/`[HIT]` successes) and the Action/Star-chip bag-pull (draw a chip, its owner picks which of their models acts) are both genre-standard — closest kin is a Rangers of Shadow Deep/Frostgrave-style chip-bag, with one small nuance worth a passing note: a Star chip returned to the bag on a `[SPECIAL]` "going for broke" test lets a high-Cool model reactivate later the same turn, at increasing statistical unlikelihood the more times it's chained. Not different enough from what's already logged elsewhere in the hub to warrant its own row.

---
## Source

- Primary: *Judge Dredd Miniatures Game* rulebook, Warlord Games, 2020 (Dylan Owen)
- Capture: `research/sources/judge-dredd/source.md` (full 164-page verbatim extraction), `research/sources/judge-dredd/meta.json`
- **Filing correction:** `research/sources/judge-dredd/block-war.pdf`, originally assumed to be this game's supplement, is a different, older, unrelated Judge Dredd miniatures game published by Mongoose Publishing (c.2009–2013) that happens to share a similar name and the same IP licence. It was **not** used as a source for this note — see `research/sources/judge-dredd/block-war-meta.json` for the full discovery writeup and a flagged-but-uncaptured Territory-control finding for a future, separate research pass.
- Related: [[Wargaming Research Hub]] · [[Necromunda and Mordheim]] (underdog banding, the closer analogue for genre lineage) · [[Trench Crusade]] (the fixed-threshold-schedule precedent this book independently confirms) · [[Campaign]] · [[Damage]] · [[Scenarios]] · [[Progression]] · [[Territory]] · [[Structures]] · [[Economy]]

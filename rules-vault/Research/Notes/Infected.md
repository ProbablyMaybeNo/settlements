---
type: research-note
title: Infected
game: Infected! (Immersion RPG system)
publisher: Immersion Studios
designer: Oliver R. Shead
depth: sampler / quickstart — 50pp preview + 1pp official GM-screen reference card + 15pp adventure module. No core rulebook sourced.
retrieved: 2026-08-21
source_url: www.immersion-rpg.com — full book listed as "Infected Zombie RPG" on DriveThruRPG (per sampler p.3, not independently verified)
capture: research/sources/infected/
tags: [settlements/research]
---
# 🎲 Infected

> [!abstract] In one breath
> **This is a tabletop RPG, not a miniatures wargame** — the sampler says so on page 4, in those words. It's a Storyteller-style 2D10 dice-pool (Attribute die + Skill die, count successes over 11) with Narrator/Player structure, Experience-bought stats, and a sanity-adjacent Morality meter. There is no basing, no measured movement, no unit roster — nothing a skirmish game could borrow at the resolution-mechanic level. One genuinely reusable idea survives the trip: a **6-tier ordinal "Hardness Rating" that hard-blocks damage outright when the margin between attacker and defender tier is 2+**, rather than just scaling a save.

> [!warning] Rank this down — read the caveats, don't spend more time here
> Two compounding depth problems. First, **this is an RPG** — the project has already established (Judge Dredd, 77 files) that RPG resolution mechanics don't transfer cleanly to skirmish, and this note doesn't relitigate that. Second, even within "what this RPG does," **all three files are partial**: a marketing sampler, one face of a GM screen, and one adventure module — never the ~300pp core rulebook the adventure itself cites ("page 188 of the Infected Rulebook"). Nothing here is `primary`. Treat every number as **provisional to a book we don't have.**

| | |
|---|---|
| **Publisher · designer** | Immersion Studios · Oliver R. Shead |
| **Format** | Tabletop RPG (Narrator + Players), not a miniatures game — no scale/basing applies |
| **Core resolution** | `1D10 + Attribute` and `1D10 + Skill` (2 dice, rolled together), target 11, count successes above target |
| **Depth of read** | **sampler / quickstart** (50pp) + **official GM-screen reference card, one face** (labelled "Core," 1pp) + **adventure module** (15pp). **Never primary** — the ~300pp core rulebook is not in this capture |
| **Raw capture** | `research/sources/infected/` in the Settlements repo |
| **Source** | Immersion Studios, 2016 sampler (2nd ed.); full book on DriveThruRPG |

---
## Why it's here

Ross's batch flagged this as a possible bust before I opened it, and the probe was right: **it is an RPG wearing a zombie-apocalypse skin, not a skirmish game.** The one thing worth carrying forward is a clean piece of combat math — the **Hardness Rating** table — which happens to answer a live Settlements want (equipment tiering) even though it comes from completely the wrong kind of game. Everything else genre-typical to zombie RPGs — a sanity/Morality meter, a called-shot table, burst-fire dice-pool math, a Luck/Resolve spend economy — is either generic to the RPG hobby or a direct analogue of mechanics Settlements has already looked at elsewhere with better sourcing, so none of it earns a second row. The one thing Ross explicitly asked me to look for — an infection/contagion track — turned out to be **a single opposed roll with no elaboration**, not a track at all; see **What it gets wrong**, below.

---
## Hardness Rating — an ordinal tier that can fully negate a hit, not just reduce it

**Type:** Combat · **Take:** ⚙️ adapt

Every object and creature has a **Hardness Rating (HR)** from 0-5 — Soft (0, unarmoured humans / unarmed strikes) through Blunt, Sharp, Fatal, Destructive, to Annihilating (5, artillery / main battle tanks). **[FACT — original.pdf p.29, narrator-screen.pdf]** Combat doesn't compare raw numbers; it compares **tiers**, and the *margin* between attacker HR and defender HR decides the entire outcome:

| Margin | Result |
|---|---|
| Defender 2+ HR above attacker | **Attacker cannot deal damage at all** |
| Defender 1 HR above | Attacker deals half damage |
| Equal HR | Normal — roll to absorb as usual |
| Attacker 1 HR above | Defender absorbs half |
| Attacker 2+ HR above | **Defender cannot absorb at all** |

*"Handgun (HR 2) vs Humvee (HR 4) — The handgun can shoot at the humvee all day, but it's not going to do anything but make a few scratches. No damage is possible."* **[FACT — original.pdf p.30]**

**Why it works.** Most armour-vs-weapon systems (including Settlements' own numeric armour ticks) only ever *scale* a save — more AP means a worse save, but the roll is always live. This system instead puts a **hard floor and a hard ceiling on a 6-rung ladder**: cross it by 2 tiers in either direction and the roll stops mattering entirely. A pistol is *narratively* incapable of hurting a tank, not just statistically unlikely to — and that's stated as a rule, not left to GM fiat. It's the same "small ordinal ladder, margin governs the effect" shape as [[Zona Alfa#Combat Experience — one tier gates Actions, Skills, and Equipment Slots together|Zona Alfa's Combat Experience tier]], independently arrived at from a completely different genre and dice system. **[INFERENCE — convergent design, not a stated cross-reference.]**

**For Settlements.** Touches [[Weapons]] and the open equipment-tiering/crafting question. The honest objection: Settlements prices armour as a **continuous numeric tick** (30/60 in the current test-bench), not a discrete tier ladder, and that choice is deliberate — it lets any two values be compared without a lookup table. Adopting a hard-block-at-margin-2 rule would mean either (a) bolting a second, parallel tier system onto the numeric one — exactly the kind of dual-track bloat the project avoids — or (b) replacing continuous armour pricing with an ordinal ladder, a much bigger rework for a benefit that hasn't been shown to matter at Settlements' scale. **This is a "wrong shape for us" idea, not a "do this" idea** — worth keeping on file the next time "should light weapons just auto-fail against heavy armour" comes up as a design question, since this is a working precedent for stating that as an explicit rule rather than an emergent one. Low confidence: single sampler, no community feedback located, no evidence of how it played at the table.

---
## What it gets wrong (or rather, what it doesn't have)

**Infection/contagion — the one thing Ross specifically wanted, and it isn't here.** The only infection rule in 66 pages is one sentence, inside a monster stat block, not a rules chapter: *"the victim must make a Brawn/Luck check, opposed by the amount of damage received... If they fail, they're infected, and only rapid medical attention will give them any chance of survival."* **[FACT — original.pdf p.46]** That's it — no incubation clock, no symptom stages, no track of any kind, and no rule for what "rapid medical attention" or "immune" actually means mechanically. **[NOT FOUND]** — whatever the real system is, it lives in the ~300pp core book this capture doesn't include. This is not a documented negative result (no design rationale is given for keeping it this thin) — it's simply outside what a sampler covers. **Do not treat "Infected has no real infection track" as a finding about the full game; treat it as a gap in this capture.**

**Noise/detection — searched, effectively absent.** Zero hits on `noise`, `detect`, `scavenge`, `stealth`, `scent`, `smell` across the 15-page adventure module; two hits on `sound`/`attract`, both flavour prose with no roll, no range, no table attached. **[NOT FOUND]**

**Generic-to-genre, correctly excluded from a row:** the Morality/sanity meter (a Call of Cthulhu-shaped corruption track, not a novel structure), the called-shot table (Head/Throat/Limb/Groin/Eyes — the same trope as a dozen other games already in this vault), the Luck/Resolve spend economy, and the burst-fire dice-pool math. All genre-conventional RPG furniture; restating any of them in Settlements' vocabulary produces nothing Settlements doesn't already have a better-sourced version of.

---
## Evidence & confidence

- **[FACT]** — Hardness Rating table and comparison rule, both files, cross-verified identical between `original.pdf` p.29-30 and `narrator-screen.pdf`.
- **[FACT]** — game-type determination ("a tabletop role playing game — also called an RPG"), `original.pdf` p.4.
- **[NOT FOUND]** — anything past "infected" in the infection check; any codified noise/detection system; what a failed Morality check does (text cuts off mid-sentence in the sampler).
- **[INFERENCE]** — the Hardness Rating's structural resemblance to Zona Alfa's tier-gates-multiple-things pattern is my own observation, not a stated design connection between the two games.

---
## Source

- Primary: Immersion Studios / Oliver R. Shead, *Infected!* 2nd-edition sampler (2016), GM-screen back face, and the *Lobster Problems* adventure module.
- Capture: `research/sources/infected/` (`source.md`, `meta.json`; PDFs gitignored, library masters at `G:\My Drive\Wargaming\Infected!\`).
- Related: [[Wargaming Research Hub]] · [[Zona Alfa#Combat Experience — one tier gates Actions, Skills, and Equipment Slots together]] · [[Horizon Wars]] (another thin/rank-down note, same "flag it and stop" treatment) · [[Weapons]]

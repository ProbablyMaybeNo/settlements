# Settlements — Phase 2 Readiness Checklist

*Built from a full audit of the Obsidian vault, the local repo and GitHub, 2026-08-29.
Supersedes nothing — it sits beside `LAUNCH-CHECKLIST.md` (2026-08-27) and carries the
items that checklist predates, plus everything the audit turned up.*

> **One numbering note.** `Project Roadmap/SETTLEMENTS PROJECT ROADMAP.md` (the newest
> source on phases, 2026-08-10) has **Phase 2 = Reference Materials & Cheat Sheets** and
> **Phase 3 = Testing**. This list is built for *"everything that has to be settled before
> real test games start"*, which spans both — the reference pack is a prerequisite for
> testing, not a detour around it. If you've renumbered, nothing here moves; only the
> label does.

**Legend** — **[Ross]** your ruling, nothing moves without it · **[Build]** mechanical,
I can execute · **[Table]** only real play answers it.
**S** one sitting · **M** a session · **L** a project.

---

## Platform sync — clean

| Check | Result |
|---|---|
| Obsidian vault ↔ repo `rules-vault/` | **Byte-identical**, every file, both directions |
| Local `main` ↔ `origin/main` | **Same commit**, 0 ahead / 0 behind |
| Worktree branch ↔ `main` | **Same commit** |
| `check_rules_consistency.py` | **PASS** (vault and mirror) |

Eight cross-note contradictions were found and fixed this pass — see *What changed* at
the bottom. Three housekeeping items remain, none of them blocking:

- [ ] **`TRACKERS/*.csv` and `.notion-sync-state.json` are frozen at 2026-05-18.** **[Build] S** — the Notion tracker sync (`scripts/notion_sync.py sync-all`) has not run in three and a half months. Either re-run it or stop citing Notion as a live tracker.
- [ ] **Today's sim work is uncommitted** — `test-bench/attack_dice_*.py` (4 harnesses), 14 result envelopes, `test-bench/explorer/`. **[Build] S** — and these harnesses sit **directly in `test-bench/`**, which `run_stamped.py` does not fingerprint. Commit them *before* the numbers get cited, or the only thing binding the Attack Dice results to their source is a dirty tree.
- [ ] **Six empty directories** in the repo root — `WORLD/ equipment/ ideas/ rules/ units/ weapons/`, 0 files each. **[Build] S** — delete or populate.

---

# 🔴 Gate A — rulings that block the first test game

*Eleven items. Nothing below Gate A is worth doing until these land, because a test game
played on an unruled mechanic measures the wrong thing.*

## A1 · Attack Dice — ruled 2026-08-29, but four sub-decisions are still open

The mechanic went into `Full Rules System v1` §15 and `Weapons` §1.5 today. It is the
newest thing in the game and the least settled. **All four of these change what a test
game measures.**

- [ ] **The gates are PROPOSED, not law.** **[Ross] S** — rank gate (AD 2 → Fighter+, AD 3 → Specialist+) · one AD 3 weapon per crew · AD 3 manufactured-only. The auto-include flag fired hard: **AD 3 beats the Heavy Gunner benchmark by +51%** on identical fielded Credits, and a **DEX +0 Recruit with three dice out-shoots a DEX +6 marksman** — the hard stat cap. That breaks §15's own first tenet (*stats decide if you land it*). **Ungated, the first six test games measure a solved meta**, exactly as the 24" range threshold did before it was gated.
- [ ] **Do surplus whiffed dice Pin?** **[Ross] S** — §15 step 4 says yes. It is the *only* thing separating the two candidate resolutions; P(Down) is identical at every dice count either way. Saying no cuts effective suppression **14–40%** and caps a burst at one Stress, so a 3-die burst suppresses exactly as hard as a pistol. Your worked example doesn't disambiguate it — both readings give the same answer there, because the target went Down.
- [ ] **Split fire.** **[Ross] S** — §15 assumes every die goes at the declared target. Allowing a split would stop surplus dice being wasted, and *that is the assumption the one-wound cap and the entire cost table rest on*. Ruling this after pricing means repricing.
- [ ] **Is 3 the ceiling?** **[Ross] S** — nothing in the maths breaks past 3, but the auto-include gap widens per die. Reserving 4+ for turrets and vehicles is untested either way.

## A2 · The payload block — five weapon effects are not legal to buy

- [ ] **Payload replace-vs-choose.** **[Ross] S** — Crippling, Concussive, Blinding, Hook and Toxic all measure **≤0 net value** because a payload lands *in place of* Pinned, and Pinned measures **+0.510 significant**. They are marked BLOCKED and cannot be fielded. **This is a rules decision, not a pricing one — do not fix it by repricing.** The recommendation on file: on a hit that fails to wound, the attacker **chooses** payload *or* the default result. Every payload becomes weakly positive by construction, "a hit does exactly one thing" survives, costs one clause, needs no reprice.
- [ ] **This also blocks the mine catalogue** — three mine payloads mirror traits that currently measure negative, so pricing them first bakes the defect into a second catalogue.

## A3 · Rulings carried over from 2026-08-27, still unticked

- [ ] **Wrecking Crew / Trapper name collision.** **[Ross] S** — each is both a Glorious Deed and a skill (T3 STR and T1 INT). A player asking *"did I earn Wrecking Crew?"* cannot tell which system is meant. Recommendation on file: rename the **Deeds** (→ Demolition Man, Sprung the Trap), because the skills are referenced from the stat ladder and the costing engine while the Deeds are referenced from one table.
- [ ] **Long Barrel (DEX T1).** **[Ross] S** — a dead skill: Long Range moves a whole range band unconditionally for 5/step, so the skill buys less *and* costs you a Move. Rewrite or cut. *(Its stated justification cited a retired 24" ceiling and a retired 6-point price — corrected this pass, but the verdict still needs your call.)*
- [ ] **Sign off the seven derived calls** from the reconciliation. **[Ross] S** — raid/pitched caps (640/1275), founding budget (125 + 75), repair (15), storage caps, HQ tiers (110/195), battle reward (70 Cr + 15 Mat), One-Handed Melee at Recruit. Listed in `docs/RULES-RECONCILIATION-2026-08-27.md`. Each applied a stated convention rather than leaving an actively-wrong number, but they are numeric design decisions and they are yours.
- [ ] **Long Range vs the 24" gate line.** **[Ross] S** — *new this pass.* §15 rules that range reaches 36" and everything past 24" clears four gates. The Long Range characteristic previously read *"to the 24" ceiling"*, which contradicted it. I repointed the line at the gates rather than rule it either way. **The open question: does buying Long Range carry a weapon across the gate line, or does it stop at 24" so that only gated weapons go further?**

---

# 🟠 Gate B — the mechanics a test game needs in order to be playable

*Nine items. These are not design questions — they are things that exist in prose but
cannot be used at a table.*

## B1 · The costing engine does not know about this month's rules

- [ ] **Attack Dice pricing (+40 / +65) exists in the rules and nowhere in the engine.** **[Build] M** — zero hits for `attack_dice` anywhere in `test-bench/points/` or `test-bench/engine2d/`. A brand-new, gated, priced weapon axis that no sim can validate and no costed roster can legally include. **Note the known trap first:** `points/ticks.py` is *downstream* of the harness, so a write-back marks every artefact stale on `cost_table` while changing nothing measured. Decide whether that staleness is worth paying before writing it in.
- [ ] **`test-bench/sim_report.py` applies Stress on a *successful* wound as well as a failed one.** **[Build] S** — verified in the source: both branches of the injury roll do `dfn['_st'] += 1`, contradicting §9 and §10 ("a hit wounds *or* stresses, never both"). Invisible at WND 1 where a wound ends the fight; at WND 3 it roughly **doubles** the break rate. **The published "~1.75 breaks/fight" in `Dice Mechanic — Sim Findings` §7 measures 0.744 rules-correct.** The qualitative claim that morale is a duration mechanic probably survives; the number does not.
- [ ] **AGI has never been measured.** **[Build] M** — the engine reads it only inside the Dodge reaction and `DODGE_ON` is `False`, so it prices at **exactly zero by construction** and rides the opposed ladder at ×0.8 by analogy. One of five stats is unpriced. Cheaper than it sounds: Dodge is fully implemented and `blkout_test.py` already A/Bs it — flip the toggle and run the stat-ladder measurement.
- [ ] **Fifteen of twenty-four deployables are `[UNPRICED]`.** **[Build] S–M** — the four traps beyond Trip Wire and five of seven beacons are derivable now by the engine's own stated rule. The Remote chassis and five mine payloads are blocked behind A2.
- [ ] **Fabricator T2/T3 are not engine rows.** **[Build] S** — currently C-tier derived in the note (110 / 195) from `UPGRADE_MULT`.

## B2 · Mechanics with no way to be used

- [ ] **Ambush has no action, skill or piece of gear anywhere.** **[Build] M** — the *resolution* is fully sim-tuned; there is no defined way for a player to attempt one. The mechanic cannot be tested because it cannot be triggered.
- [ ] **Equipment is four lines.** **[Build] M** — the weakest catalogue in the game and the safest to widen, because equipment modifies tests that already exist. Rule: every entry must modify a roll you already make, apply a condition you already define, or open a terrain verb you already have.
- [ ] **Chems have no catalogue.** **[Build] S** — the Dependence maths is sim-confirmed (1.55 clean uses at NRV +0, 3.02 at NRV +4). There is no list, no prices, no effects.
- [ ] **Drones have no profiles.** **[Build] M** — Bandwidth is ruled and the Drone Bay is built; there is one paragraph and no catalogue.

---

# 🟡 Gate C — the reference pack (Phase 2 proper)

*Six sheets. You cannot hand this to a stranger without them, and the audit found the
layer they were supposed to be generated from is not ready.*

- [ ] **The Rules Ledger only covers the battle core.** **[Build] M** — the MOC declares it *"the clean final wording for embeds / the eventual rulebook"*, i.e. the source for these sheets. It holds nine `core-*` cards and five parked `adv-*` cards. There is **no ledger card for list building, campaign, settlement, economy, progression, hacking, deployables, terrain or scenarios.** Roughly two-thirds of the reference pack has to be written from scratch rather than graduated. *(Three cards were brought current this pass — core-002, core-006, core-007. The other six are still v0.1 from July.)*
- [ ] **47 tables in the vault carry no block anchor — 37 of them in the master doc.** **[Build] S** — `build_catalogue.py` reports them as un-embeddable. Every one of those is a table a cheat sheet would want to pull.
- [ ] **Core test card** — the one mechanic, nat 1/10, the modifier cap, the probability table. **[Build] S**
- [ ] **Condition summary sheet** — **~29 conditions**, one line each, grouped by clock (persistent / activation / until cleared). **[Build] S** — *note the roster has grown; the 2026-08-27 estimate of 26 is out of date.*
- [ ] **Crew sheet** — with **Crew Rating and Wealth as two separate printed numbers**. **[Build] S**
- [ ] **Settlement sheet** — the 12″ × 36″ one-inch grid, Power sum, resource tracks, Functional/Disabled flags. **[Build] S**
- [ ] **Three scenario sheets** — Take a Hold, Raid, Sabotage. One spread each. **[Build] M**
- [ ] **Quick-reference turn sequence** — round structure, activation, reaction triggers, End Phase order. **[Build] S**

---

# 🟢 Gate D — decide *at* the table, not before it

*Do not try to close these first. They are the reason to test, and several are already
designed as experiments.*

- [ ] **Six real games with real people.** **[Table] L** — **nothing else on this page is worth more than this.** Roughly six million simulated games and zero human ones.
- [ ] **Stress persistence** (§§9–11, drafted 2026-08-29). **[Table]** — deliberately shipped as *drafted, pending playtest*: only the table can say whether losing a just-rescued fighter reads as brutal-good or brutal-bad. Costs about **1 revival in 53** walking off at current rates. **Valve held in reserve, not pre-applied:** *"a Stabilised fighter returns Shaken, however much Stress it had."*
- [ ] **Then, and only then, surplus Attack Dice passes → +1 Stress each.** **[Ross after Table] S** — measured and ready (`attack-dice-15b-surplus`), deliberately **not** adopted alongside persistence. Together they roughly **2.2×** the Stress on a downed model and take wasted revivals from ~1-in-11 to nearly **1-in-4**. The conversion does nothing at WND 1 unless persistence is in force, so this ordering is the only one that makes either rule legible.
- [ ] **Clock the games.** **[Table]** — target ≤90 min including setup at 9–12 density with reactions and one event. If mean >100, cut one of: event frequency, the reaction menu, or any marker that doesn't change a decision. *Decide by measurement, not taste.*
- [ ] **Watch the melee archetype.** **[Table]** — Assault loses every matchup in `catalogue-validation-n1500`, 61.2% against it at worst. Whether melee is overpriced or `hold_claim` just undervalues closing **cannot be separated at 1-of-5 scenario coverage**.
- [ ] **Watch Dodge.** **[Table]** — the engine AI cannot stress the escape-out-of-LOS case.
- [ ] **Watch WND 3 on kill-shaped missions.** **[Table]** — the FIX 4 skew the audit deferred, and the one place B1's `sim_report` defect actually bites.
- [ ] **Everything is priced on `hold_claim`** — one of five shipped scenarios and the most static. **[Table]** — expect static/defensive atoms to read HIGH and mobility/tempo/stealth to read LOW. Play the other four and see which way the bias runs.

---

## The order I'd run it

**A1 + A2 (six rulings, one sitting) → B1 (the engine catches up) → C (the pack) → D (the table).**

A1 and A2 are six small calls that between them unblock the newest mechanic in the game
and five weapon effects. B1's first two items are a morning's work and one of them
invalidates a published number, so it wants doing before anyone cites it again. The
reference pack is the long pole in Gate C — not because the sheets are hard, but because
two-thirds of the ledger they graduate from doesn't exist yet.

---

## What changed in this pass

Eight contradictions cleared, all verified by quoting the conflicting text. Committed as
`3e034c2` and pushed.

| Where | Was | Now |
|---|---|---|
| `Full Rules System v1` §12.6 | deployables obey "the same **+4** Damage ceiling as everything else" | **+5** — everything else is +5 |
| `Full Rules System v1` §15 char. table | Long Range "+6″ range, **to the 24″ ceiling**" | repointed at the four gates; the underlying question raised in A3 |
| `List Building` pyramid | Campaign Start has "**no ratio requirement**", all-Specialist lists legal | Specialist ratio holds; only Recruit-per-Fighter drops (master §16 wins) |
| `List Building` pyramid | "inside the **500** cap" | **425** |
| `List Building` max bodies | "at **1000 Credits** … about **11 fighters**" | **8** at 850 — recomputed off the 70/100/145/185 ladder |
| `Factions` | faction rules may not touch "the **+4** Damage cap, the **24″** range cap" | **+5**, and the **36″** ceiling with its four gates |
| `Unit Design` | "**Champions** and Leaders" | **Specialists** |
| `Weapons` §7 | Long Barrel is dead because of "the **24″** ceiling" and a **6**-point price | reasoning corrected to the band step at **5**/step; verdict kept |

Plus: `core-002` / `core-006` / `core-007` ledger cards taken to v0.2 (Attack Dice, the
one-wound burst cap, Stress persistence) · the `Interviews` script now carries a
SUPERSEDED banner because its "locked context every interview inherits" was three
generations stale (Cash, Water, the 100-point scale) and read as live ·
`check_rules_consistency.py` gained **eight guards** for exactly these strings, including
the master document, **which was previously its own blind spot** — it had rules for
catching `+4 Damage ceiling` in `Deployables.md` but not in the source of truth.

### Three things that looked broken and are not

- `[[15b · Attack Dice]]` — a **deliberate** dangling link, documented as such in the note.
- `[[Overwatch]]` — a worked example inside the Obsidian guide, not a real reference.
- `[[Wargaming Research Hub]]` — exists at `Research/Wargaming Research Hub.md`; Obsidian resolves it cross-folder.

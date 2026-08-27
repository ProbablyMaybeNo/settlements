# Settlements — Launch Checklist

Everything outstanding from the 2026-08-27 launch-readiness audit, ordered into three
gates. **Tick as you go.** This is the working list; the audit itself is the reasoning
behind it.

**Legend** — **[Ross]** needs your ruling before anything can move · **[Build]** I can
execute once unblocked · **[Table]** only real play answers it.
Sizes are relative, not hours: **S** one sitting · **M** a session · **L** a project.

---

## ✅ Closed 2026-08-27 — the reconciliation pass

Recorded so the remaining list reads honestly against what's already done.

- [x] Every price in the vault regenerated from the shipping catalogue (rifle 130 → 35, HQ 130 → 70 Mat, etc.)
- [x] Crew Rating settled — 850 / 640 / 1275 / 425, one rank ladder 70/100/145/185
- [x] Weapons moved onto the banded generation — ceiling +5, range 36" behind four gates, Concealable cut
- [x] Eleven satellite contradictions cleared (Dodge, loot 7, Progression track, armour drawbacks, Seeker, worker benefits, Factions roster…)
- [x] Mess Hall added to the costing engine — the one structure with no derived cost anywhere
- [x] The §28.7 worked example rebuilt, including the Power draw it had been getting wrong
- [x] `scripts/check_rules_consistency.py` — the guard against this whole class of drift
- [x] Vault and repo mirror verified identical; both pass the checker

---

# 🔴 Gate 1 — Final Alpha

*A thin slice you can hand to strangers: one faction, ten fighters, ten structures, three
scenarios, one of each core system. **Nothing in this gate requires new design** except
the four rulings at the top.*

## 1.1 · Rulings only you can make — everything else waits on these

- [ ] **Payload replace-vs-choose.** **[Ross] S** — Five payloads (Crippling, Concussive, Blinding, Hook, Toxic) measure ≤0 net because they replace Pinned, which measures **+0.510**. Currently marked BLOCKED and not legal to buy. My recommendation: on a hit that fails to wound, the attacker **chooses** payload *or* default result. Every payload becomes weakly positive by construction, "a hit does exactly one thing" survives, costs one clause, needs no reprice.
- [ ] **Wrecking Crew / Trapper name collision.** **[Ross] S** — Each is both a Glorious Deed and a skill. Suggested: rename the *Deeds* (→ Demolition Man, Sprung the Trap), because the skills are referenced from the stat ladder and the costing engine while the Deeds are referenced from one table.
- [ ] **Long Barrel** (DEX T1). **[Ross] S** — Dead skill: the Long Range characteristic does it better and unconditionally. Rewrite it or cut it.
- [ ] **Sign off the seven derived calls** from the reconciliation. **[Ross] S** — raid/pitched caps (640/1275), founding budget (125+75), repair (15), storage caps, HQ tiers (110/195), battle reward (70 Cr + 15 Mat), One-Handed Melee at Recruit. All listed in `docs/RULES-RECONCILIATION-2026-08-27.md`. Each applied a stated convention rather than leaving an actively-wrong number, but they're numeric design decisions and they're yours.

## 1.2 · Pricing — finish the catalogue

- [ ] **Price the 4 remaining traps** — Spike Strip, Covered Pit, Leg Clamp, Razor Barrier. **[Build] S** — derivable now by the engine's own stated rule; not blocked on anything.
- [ ] **Price the 5 remaining beacons** — Targeting, Aegis, Cover, Cleansing, Dread. **[Build] S** — same; an aura prices at the atom it grants, held under the gear:body cap.
- [ ] **Price the Remote chassis + 5 mine payloads.** **[Build] S** — *blocked behind 1.1's payload ruling*: three payloads mirror traits that currently measure negative, so pricing them now would bake the same defect into a second catalogue.
- [ ] **Add the Fabricator T2/T3 as engine rows.** **[Build] S** — currently C-tier derived in the note (110 / 195) from `UPGRADE_MULT`, but not present as rows.
- [ ] **Measure AGI.** **[Build] M** — *this is cheaper than the audit implied.* Dodge is fully implemented and `blkout_test.py` already A/Bs it. Flip `DODGE_ON = True` and run the stat-ladder measurement against AGI. One of five stats currently prices at exactly zero **by construction**, and it's a toggle away from being real.

## 1.3 · The reference pack — Phase 2 on the project roadmap

- [ ] **Core test card** — the one mechanic, nat 1/10, the modifier cap, the probability table. **[Build] S**
- [ ] **Condition summary sheet** — all 26, one line each, grouped by clock (persistent / activation / until cleared). **[Build] S**
- [ ] **Crew sheet** — with **Crew Rating and Wealth as two separate printed numbers** (see 3.2/G1). **[Build] S**
- [ ] **Settlement sheet** — the 12 × 36 one-inch grid, Power sum, resource tracks, Functional/Disabled flags. **[Build] S**
- [ ] **Three scenario sheets** — Take a Hold, Raid, Sabotage. One spread each. **[Build] M**
- [ ] **Quick-reference turn sequence** — round structure, activation, reaction triggers, End Phase order. **[Build] S**

## 1.4 · Put it on a table

- [ ] **Six real games with real people.** **[Table] L** — **nothing else on this page is worth more than this.** Every number in the game is sim-derived; six million simulated games and zero human ones.
- [ ] **Clock them.** **[Table]** — target ≤90 min including setup at 9–12 density with reactions and one event. If mean >100, cut one of: event frequency, the reaction menu, or any marker that doesn't change a decision. *Decide by measurement, not taste.*
- [ ] **Watch the melee archetype specifically.** **[Table]** — Assault loses every matchup in `catalogue-validation-n1500` (61.2% against it at worst). Whether melee is overpriced or `hold_claim` just undervalues closing **cannot be separated at 1-of-5 scenario coverage.**
- [ ] **Watch Dodge.** **[Table]** — the engine AI can't stress the escape-out-of-LOS case.
- [ ] **Watch WND 3 on kill-shaped missions.** **[Table]** — the FIX 4 skew the audit deferred.

---

# 🟡 Gate 2 — Closed Beta

*A full campaign season plays end to end without a gap.*

## 2.1 · The campaign holes

- [ ] **The regional map.** **[Ross + Build] L** — the territory *card* and control states exist; the **map graph does not**. Needs: how territories connect, supply paths, who can attack whom, how Isolated resolves and whether it chains. Named on the roadmap as a remaining design session.
- [ ] **Storage numbers.** **[Ross] S** — HQ base, gatherer buffer, Storehouse, Vault. Currently halved-and-provisional. Also: how much a successful raider actually takes from each container.
- [ ] **The economy sink.** **[Ross + Build] M** — the one genuinely unresolved economy problem. Cheapest fix that needs no new resource: **the trader's exchange rate worsens as you flood the district** (Mordheim's wyrdstone shape). The loot table is deliberately parked behind this — tune the sink first or you tune loot twice.
- [ ] **Settlement events + map events.** **[Build] M** — §27 covers the battlefield only. Ten entries each. Pair them with a two-checkbox **Brutal / Quiet** raid flag so the neighbourhood remembers your last visit — no running Heat track.
- [ ] **Side-objective content.** **[Build] M** — territory card field #3 exists with **nothing behind it**. Cheapest shape: one subplot deck, draw 2 claim 1. Glorious Deeds stay a *post-battle* XP source and do **not** become a second in-game objective layer.
- [ ] **Territory terrain-type → pre-built terrain lists.** **[Build] M** — each card's terrain recipe has to resolve to pieces a player actually owns.
- [ ] **Confirm loot markers count separately from the 9–12 density band.** **[Build] S** — so a loot-heavy territory doesn't quietly blow the sacred band.

## 2.2 · The thin catalogues

- [ ] **Equipment: 4 lines → 12–16.** **[Build] M** — the weakest catalogue in the game and the safest to widen, because equipment modifies tests that already exist. Rule: every entry must modify a roll you already make, apply a condition you already define, or open a terrain verb you already have. Your own note already points the way — *armour sets that stop conditions: "fireproof", "hazmat"*.
- [ ] **Chems: one paragraph → a real catalogue.** **[Build] S** — the Dependence maths is sim-confirmed (1.55 clean uses at NRV+0, 3.02 at NRV+4). There is no list of chems, no prices, no effects.
- [ ] **Drones: one paragraph → profiles.** **[Build] M** — Bandwidth is ruled and the Drone Bay is built. No drone catalogue exists.
- [ ] **Faction rules tightened to one strong sentence each, with numbers.** **[Ross + Build] S** — "Improved Build test for field deployables" doesn't say by how much. And BLKOUT's lesson: one **playstyle-defining** rule beats six conditional nudges.
- [ ] **Lock the faction names.** **[Ross] S** — the framework doesn't care which labels win. Your Ideas Inbox set (**The Veterans · First Responders · The Watch · The Union · The Syndicate · The Wyrm**) carries far more setting voice than Military / Tech Workers, and is built around free starting gear + category discounts.

## 2.3 · Your stated wants that aren't built

- [ ] **Stealth and noise.** **[Ross + Build] L** — Ambush *resolution* is fully sim-tuned, but **no Ambush action, skill or piece of gear is defined anywhere** — the mechanic has no way to be used. Recommended shape (three independent designers converged on it): every shot/breach drops Noise; End Phase `1d10 + Noise vs 7+` draws a neutral contact toward the noisiest square; four ordered AI rules, not a random table. Highest reality-per-rule in the whole corpus, and it gives **Quiet** a job.
- [ ] **Loot enemy bodies in battle.** **[Ross + Build] M** — your version: a downed model leaves a token, an enemy Interacts to take it, roll after the battle, a 6 means Captured. Puts agency where it belongs; Judge Dredd's Stun/Injury fork is the published shape.
- [ ] **Rank equipment slots — Leader 4 / Specialist 3 / Fighter 2 / Recruit 1.** **[Ross] S** — everyone currently gets a flat two. Free differentiation, one table row.
- [ ] **Slow → "attacks last", not "cannot charge".** **[Ross] S** — your version is better *and* survives the drawback rule: attacking last bites in every melee, where "cannot charge" only bites if you wanted to charge.
- [ ] **Rank-gating weapon type — you said "I don't love this".** **[Ross] S** — still locked and still load-bearing for the rank ladder. Worth a deliberate ruling rather than an objection sitting in the inbox. *(Note: the reconciliation already loosened One-Handed Melee to Recruit; the gate that matters is rifles.)*
- [ ] **The Vault — you said "we can remove this, unnecessary".** **[Ross] S** — still in the catalogue at 50 Materials with a full design argument written for it.
- [ ] **Aerial Attack.** **[Ross] S** — drafted in your notes, never adopted. Uses AGI, +2 Damage, unreactable.
- [ ] **BUILDER units.** **[Ross] M** — in the vision notes from the start; nothing anywhere.

---

# ⚪ Gate 3 — Release

*Everything currently at or near zero.*

- [ ] **Write the setting.** **[Ross] M** — `Narrative.md` is Not Started **and contains a detailed alien-invasion premise** (antimatter tests, a monolith in the Mojave) that is a completely different game from the 2051 civil war everything else is built on. **Archive that draft explicitly as rejected so it can't creep back**, then write one page: what broke, who's fighting, why a neighbourhood is worth a firefight. One page unblocks faction names, territory cards, event flavour and the loot table's voice.
- [ ] **Weapon origin tiers — crafted / manufactured / found.** **[Ross + Build] L** — your idea, dropped by the packet and never replaced. Does four jobs at once: makes the setting legible, makes the settlement matter to the *crew* not just the campaign sheet, gives loot a reason to excite, and creates an asymmetry axis with no new mechanics (crafted takes characteristics; manufactured has better base numbers but no slots; found tech does both and can't be bought or built). Pair with **capability is leased, not owned** — lose the Workshop, lose the tier.
- [ ] **Solo & co-op.** **[Build] L** — three separate games independently confirm the same trick: **reuse the alert-state tables as the bot** rather than building a parallel AI.
- [ ] **Diplomacy.** **[Build] M** — stage betrayal as a *scenario*, not a reputation economy. Two-player needs the hidden-break-check shape, not a standing.
- [ ] **Edge Cases audit.** **[Build] M** — also unblocks the parked Seeker chassis.
- [ ] **The rulebook.** **[Build] L**
- [ ] **Components** — tokens, cards, print-and-cut structure tiles at exact grid footprints. **[Build] L**
- [ ] **Playtesting plan** — stages, gate criteria, coverage matrix. **[Build] M**
- [ ] **Skill cull.** **[Ross + Build] M** — 150 is a lookup problem; target 6–8 verbs per tier. Merge the known twins first (Knockback/Heavy Impact, Ghost Blade/Balanced).
- [ ] **One targeted terrain research sweep.** **[Build] M** — terrain is the **first pillar** and has **1 of 235** catalogued mechanics. The candidates are already named: *Scrappers* (closest structural match, same publisher as Zona Alfa), *Across the Dead Earth*, *Combat Zone*.

---

# 💡 Backlog — the upside list

*Ranked by return against table-time cost. None adds a subsystem.*

- [ ] **1 · Noise + neutral contact** — see 2.3. Highest reality return in the corpus.
- [ ] **2 · Print the rating ladder** — both players climb the same printed schedule (500 → 750 → 1000 by battles played) regardless of who's winning. Kills the cap argument permanently and removes the **play-frequency** snowball, which is the biggest one measured (750 credits at one game/week vs 1,170 at two).
- [ ] **3 · Name Wealth** — two numbers on the crew sheet: **Crew Rating** (fielded) and **Wealth** (banked + stashed). You already behave this way; Necromunda states it verbatim 28 years apart. Arguments die when the stash has a name.
- [ ] **4 · A LIMIT column beside every price** — two independently-tuned dials per line. **LIMIT caps purchasing, not possession** — loot can break it, so taking the enemy's machine gun stays a prize.
- [ ] **5 · One subplot deck** — see 2.1.
- [ ] **6 · Alert states, scoped to raids only** — Unaware/Uneasy/Alert on the *defender* only. A powered Scout Post or Watchtower means they start Alert. Makes intelligence a **building**, not a buff. Don't take the decaying disguise number.
- [ ] **7 · Disabled strips the unlock** — a Disabled Workshop loses the in-progress craft, a Disabled Drone Bay grounds drones, a Disabled Armory reverts the equipment cap. Gives sabotage teeth with no structure HP.
- [ ] **8 · Elevation demotes cover one tier** — one sentence replacing "2"+ ignores Light". Makes density do more work without another board feature. Watch for roof camping; the sim already has a sweep.
- [ ] **9 · Automatic Bolt for the rank and file** — Recruits and Fighters (WND 1, no Orders) skip the Break roll at 2+ Stress. Specialists and Leaders still roll. Faster, more brutal, and rank finally means something where it currently means nothing.
- [ ] **10 · Opt-in rebuild + patronage tokens** — catch-up the loser *chooses* and *pays for*, rather than a handicap applied to them.

---

# ⛔ Not doing — the restraint list

*Keep these refused. The anti-bloat discipline is a competitive advantage and the easiest thing here to lose.*

- **No second currency.** Glory, Reputation, Renown — three names, one trap.
- **No unparking the ten worker benefits** or reviving the Proficiency track.
- **No difficulty tiers on tests.** Flat 7+ with modifiers has survived every challenge.
- **No deeper hacking.** Corvus Belli spent three editions shrinking Infinity's; Fallout's is one sentence.
- **No second randomiser.** Card activation and the quality die are good and structurally incompatible.
- **Don't fire every subsystem every game.** Budget board-machines per scenario.
- **Don't reconcile `ticks.py` with `data.py`.** The divergence is the safeguard — syncing them closes a self-confirming measurement loop this project has already eaten once.
- **Don't build the companion app before the table games.**

---

## Suggested first move

**1.1 (the four rulings) → 1.2 (finish pricing) → 1.3 (reference pack) → 1.4 (six games).**

The four rulings are small and everything else queues behind two of them. After that,
Gate 1 is mechanical work I can just do — and then the table tells us which half of this
list was worth writing.

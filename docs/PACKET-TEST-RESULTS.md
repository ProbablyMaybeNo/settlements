# Packet Design Review — Simulation Results

**Run 2026-08-02** against `Z:\Downloads\Packet-Design-Review.md`.
Engine: `test-bench/engine2d/` (2.5D). Harnesses: `test-bench/balance/stealth2d.py`,
`packet_battle.py`, `packet_campaign.py`. Every number below is a measurement on
this engine; nothing here is an estimate.

> **Read this first.** The file supplied is a **review of** the packet, not the
> packet. It states verdicts on §1–§10 but does not contain the packet's own text:
> no XP award values, no Level Surcharge numbers, only 4 of the 10 generic Deeds
> named, and the eight structure / eleven territory fields named but not filled.
> So where the packet proposes a value, these tests **derive** the value rather
> than validate it. If the packet's numbers differ, re-run against those.

## Method

All battle results are **paired mirrors**: for every configuration we measure
`(buffed crew vs plain crew) − (plain vs plain)` with sides swapped every game, so
residual harness bias subtracts out. Both sides always run the same AI policy, so
a delta is the value of the *mechanic* and never of a playstyle.

Prices are quoted against the anchor `conditions2d.py` established on this engine:
**+1 Damage = 1.12 win-points per model = 15 Credits.**

Harness controls (identical crews, no buff): DEX6 **48.9 / 50.4%**, AGI6
**49.2 / 49.4%**, STR6 **49.0 / 48.7%**. Clean.

---

## T1 / T4 — the stealth layer, and who it is for  (§2.6)

700 games/cell. `d mean` = points of win rate gained by the stealthy side.

| carrier | hidden mode | hidden holds | ambush payoff | d Hold | d Annih | d mean | per model | ≈Credits | ambushes/game |
|---|---|---|---|---|---|---|---|---|---|
| DEX6 | modifier | yes | +0 | −32.8 | −32.9 | **−32.8** | −5.47 | −73 | 0.56 |
| DEX6 | untargetable | yes | +2 | −31.0 | −29.5 | **−30.2** | −5.04 | −68 | 0.77 |
| AGI6 | modifier | yes | +0 | +1.1 | +0.9 | **+1.0** | 0.17 | +2 | 4.29 |
| AGI6 | modifier | yes | +2 | +13.0 | +12.4 | **+12.7** | 2.11 | +28 | 4.42 |
| AGI6 | modifier | **no** | +0 | −28.6 | +0.9 | **−13.8** | −2.30 | −31 | 4.29 |
| AGI6 | modifier | **no** | +2 | −22.8 | +12.4 | **−5.2** | −0.87 | −12 | 4.42 |

*(`untargetable` rows for AGI6 are identical to `modifier` to the decimal.)*

**Findings**

1. **Ambush-on-AGI works, but only for an AGI carrier.** Handing the same kit to a
   DEX crew costs **−30 to −33 points** — its fighters end up attacking on their
   worst stat. This is the strongest argument in the packet's favour for §3.2's
   "add a third worked archetype": without a worked AGI example, players will build
   the trap. It is also a warning that Ambush must be visibly flagged as AGI-driven
   on the card.
2. **The −3-modifier vs not-a-legal-target fork barely matters.** Identical results
   for the AGI carrier; ~2–3 points for the DEX one. **This is not the decision to
   agonise over** — but note it is currently unruled: the vault says Hidden is −3,
   while the packet's Spot action only earns its slot if Hidden means untargetable.
3. **The real lever is unruled in both documents: may a Hidden fighter hold an
   objective?** Yes → **+12.7**; no → **−5.2**. A **17.9-point swing**, larger than
   any other dial in the section. *Recommendation: rule it.* Allowing a Hidden
   fighter to score is what turns stealth from a flavour option into a strong one.
4. The ambush payoff (+0 vs +2 on the Injury roll) is worth ~11.7 points across the
   range — a genuine tuning knob, not a rounding error.

## T2 — the "un-targetable fighter" combo  (§2.6)

Vanishing Point + Ghost Step + Return to the Shadows stacked on one fighter,
**against the shooting crew** (against an all-melee mirror "never shot at" is true
by construction and measures nothing — the first run of this test made exactly that
mistake and had to be discarded).

| hidden mode | build | rounds hidden (of 6) | times shot at | survived |
|---|---|---|---|---|
| modifier | plain kit | 1.15 | 12.05 | 0.1% |
| modifier | **COMBO** | 1.20 | 11.84 | 0.3% |
| untargetable | plain kit | 1.48 | 10.93 | 2.1% |
| untargetable | **COMBO** | 2.55 | **0.00** | 7.4% |

**The review's worry is confirmed — but narrowly.** The combo fighter is shot at
**exactly zero times per game**, but *only* when Hidden is read as "not a legal
target" **and** all three skills are stacked. Under the vault's −3 reading the same
fighter is shot ~12 times a game and dies. Either reading alone is safe; it is the
**conjunction** that breaks.

*Recommendation:* if Hidden becomes untargetable, the three skills need a stacking
rule (one concealment skill per fighter, or Spot auto-succeeds at close range).

## T3 — does the free Attack Back bite?  (§2.6)

| hidden mode | attack back | d mean | ambushes/game | miss rate | ambush kills |
|---|---|---|---|---|---|
| modifier | **yes** | **+8.0** | 4.40 | 47.5% | 1.33 |
| modifier | no | **+12.1** | 4.46 | 46.2% | 1.45 |

**Yes — keep it, unchanged.** The Attack Back removes **4.1 points**, a third of
the mechanic's total value, and it fires often: **47.5% of ambushes miss**. The
review's instruction to protect this clause in playtesting is supported by the
measurement.

## T5 — is the one-payload cap load-bearing?  (§2.2)

2000 games/cell, cap lifted so every payload on the weapon lands.

| weapon | d mean | per model | ≈Credits |
|---|---|---|---|
| 1 payload (Bleed) | +15.5 | 2.58 | 35 |
| 2 payloads (Bleed+Shock) | +18.8 | 3.12 | 42 |
| 3 payloads (Bleed+Shock+Hobble) | +18.8 | 3.12 | 42 |

**The second payload is worth +3.3 points (~9 Credits) — real but strongly
diminishing** against the first payload's +15.5. The third adds **exactly zero**,
which is not evidence the cap is unnecessary: the third payload was Crippling, and
`ticks.py` already records Crippling and Concussive as measuring at zero (a known
rules defect, flagged in `POINTS-TABLE.md` §5.5).

**Verdict:** the cap is worth keeping for the reason the review gives — bookkeeping
and readability — but *not* on the grounds that stacking is explosive. It isn't.
This is a simplicity argument, not a balance emergency. Adopt the tightened wording
("capped at one, no exceptions"); do not expect it to move win rates much.

## T6 — is a non-combat-primary archetype viable?  (§3.2)

2000 games/cell. Identical ranks, weapons and points; only the stat line differs.

| crew | Hold | Hold+Claim | Annihilate | mean |
|---|---|---|---|---|
| STR6 (combat) | 84.5% | 57.0% | 15.1% | **52.2%** |
| DEX6 (combat) | 49.3% | 49.3% | 49.3% | **49.3%** |
| INT6 (technical) | 49.1% | 47.8% | 14.3% | **37.1%** |
| NRV6 (morale) | 48.2% | 47.2% | 16.7% | **37.4%** |

**The review's recommendation to add a third, non-combat-primary worked example is
sound — and the sim shows exactly why it is risky to ship without support.** An
INT- or NRV-primary crew runs **12 points below** a combat crew. Crucially they are
*competitive on objective scenarios* (47–49% on Hold and Hold+Claim) and collapse
only on Annihilate (14–17%) — i.e. they are viable exactly to the degree the
scenario asks for something other than killing.

This is the vault's own thesis restated with numbers: **the scenario, not the stat
line, is what makes INT and NRV worth buying.** If the packet adds an INT worked
example, it must ship alongside scenarios that score non-combat work, or the
example teaches a losing build.

## T8 — the XP ceiling  (§4.1)

8000 battles, ~96,000 fighter-battles. Ten observable scoring sources
(kill, multi-kill, first blood, melee kill, terrain kill, against-the-odds,
objective holder, claimed, survivor, last standing).

| distinct sources in one battle | share | P(≥ n) |
|---|---|---|
| 0 | 38.22% | 100% |
| 1 | 19.06% | 61.78% |
| 2 | 11.75% | 42.72% |
| 3 | 16.24% | 30.97% |
| 4 | 11.89% | 14.73% |
| 5 | 1.66% | **2.84%** |
| 6 | 0.80% | **1.18%** |
| 7 | 0.33% | **0.38%** |
| 8 | 0.05% | **0.05%** |

Mean **1.55** sources per fighter per battle. Max observed **8**.

**This answers the review's question directly.** It asked for "a soft per-battle
ceiling, generous enough that it essentially never binds, that still closes the
degenerate tail." The measured distribution gives the number:

- **A cap of 5** binds on 2.84% of fighter-battles — too tight, it would fire in a
  normal game roughly every third battle across a 6-model crew.
- **A cap of 6** binds on **1.18%** — about one fighter in 85. This is the
  recommended value: invisible in normal play, and it halves the observed maximum.
- A cap of 7 binds on 0.38%, which closes almost nothing.

**Recommendation: soft ceiling of 6 distinct XP sources per fighter per battle.**

## T10 — what a Level is worth  (§6.6, Level Surcharge)

2000 games/cell. The review had "no opinion on values pending sim data".

| buff | d mean | per model | **Credits** |
|---|---|---|---|
| +1 primary stat, whole crew | +7.0 | 1.16 | **16** |
| +2 primary stat, whole crew | +12.0 | 2.00 | **27** |
| +1 STR, whole melee crew | +15.1 | 2.51 | **34** |
| +2 STR, whole melee crew | +28.8 | 4.80 | **64** |

**A stat point is worth 16–34 Credits depending on which stat and which role** —
against `ticks.py`'s current `TICK_STAT = 15`, which sits at the **bottom** of the
measured range. STR points on a melee crew measure at **more than double** the
current price.

For the Level Surcharge this means: a flat cumulative tax is the right *shape* (the
review is right that per-combination pricing is a combinatorial nightmare), but it
must be set nearer **25–30 Credits per Level**, not 15, and it is genuinely
role-dependent — the flat number will overcharge shooters and undercharge brawlers.
That residual is the honest cost of the simplification.

## T13 — are extra actions super-linear?  (§9.3, the Bandwidth cap)

2500 games/cell. Extra **action** (not a full extra activation — see caveats).

| fighters given an extra action | d mean | **per buffed fighter** |
|---|---|---|
| 1 | +2.5 | **+2.53** |
| 2 | +5.1 | **+2.57** |
| 3 | +5.1 | **+1.69** |
| 4 | +8.8 | **+2.20** |

**The super-linearity claim did not reproduce at crew scale.** Value per buffed
fighter is flat (~2.2–2.6 points) from one to four — **linear**, and comparable to
+2 DEX on the same fighter (+3.2). On this evidence an extra action *is* priceable,
at roughly 30 Credits.

**This does not mean drop the Bandwidth cap**, and the packet's conclusion may
still be right for reasons this test cannot see:
- the vault's own `Skill Sim` measured Quick Shot at **+24 win%** in a 1v1 WND-3
  duel — an order of magnitude larger, in a context this crew-scale test doesn't
  cover;
- this engine's AI does not exploit a spare action well (it shoots the same target
  again rather than repositioning, screening, or double-objective-grabbing);
- a hard cap costs nothing if the effect really is linear, whereas mispricing a
  non-linear effect is unrecoverable.

**Recommendation: keep the cap, but stop justifying it with "extra actions are
super-linear" — at crew scale on the current engine, they measure linear.** Justify
it as bounded risk instead, which is honest and survives this result.

## T11 — does cutting per-head upkeep remove the only continuous brake?  (§5.2, §5.7)

6000 campaigns × 20 battles. **This was the review's #1 unresolved bet.**
Rating gap = extra Crew Rating the stronger settlement can field at season end.

| configuration | rating gap | p90 gap | roster gap | idle wealth | under-cap battles |
|---|---|---|---|---|---|
| **packet as written (no upkeep)** | **63** | 150 | −0.0 | 2199 | 6.51 |
| + per-head upkeep 10/head | 69 | 140 | −0.1 | 2115 | 4.66 |
| + per-head upkeep 25/head | 91 | 255 | +0.7 | 2124 | 12.50 |
| + per-head upkeep 50/head | **122** | 315 | +0.6 | 2141 | 18.95 |
| no upkeep, tighter lot (6 structures) | 68 | 150 | −0.1 | 2081 | 6.44 |
| no upkeep, bigger lot (15 structures) | 63 | 150 | −0.1 | 1759 | 6.50 |

**The packet is right and the review's objection does not survive contact.** Adding
per-head upkeep makes divergence **worse**, not better: the rating gap roughly
doubles (63 → 122) and the number of battles fought under-strength triples
(6.51 → 18.95). The mechanism is straightforward — upkeep is a **regressive** tax.
It bites hardest on the player who is already losing fighters and already short of
income, so it accelerates the loser's decline instead of restraining the winner.

The **Crew Rating cap is doing the braking on its own**: the roster gap is ~0 in
every configuration, because whatever you own, you may only field 1000.

**But the review is half-right in a way it did not name.** Idle wealth sits at
~2,100 Credits-equivalent in *every* configuration including the tightest lot. The
economy has **no sink**, not no brake. Nothing is snowballing; a large surplus is
simply accumulating with nothing to buy. That is a real gap, and it is the thing to
fix — with sinks (higher tiers, consumables, territory upkeep) rather than with a
per-head tax that the data says backfires.

## T9 — how often is an uncapped scar treatment bought?  (§4.3)

| configuration | treatments per campaign (20 battles) |
|---|---|
| **uncapped (packet as written)** | **3.98** |
| capped at 1 per campaign | 1.00 |
| capped at 2 per campaign | 1.95 |
| unavailable | 0.00 |

**The review's concern is confirmed.** Left uncapped, treatment is bought roughly
**once every five battles** — routine shopping, not "we spent everything to save
this one veteran". It directly undercuts the "scars cost you something real"
principle stated two paragraphs earlier in the same packet section.
**Recommendation: hard cap, once or twice per fighter's career.**

## T12 — economy pacing vs the costed catalogue  (§5.6)

Using `points/ticks.py` prices at the 1000-Credit scale:

| quantity | value |
|---|---|
| battle reward | 65 Credits + 33 Materials |
| Recruit (65 Cr) | **1.00 Recruits per battle** |
| Fighter (135 Cr) | 2.1 battles |
| Leader (375 Cr) | 5.8 battles |
| Tier I structure (100 Mat) | **3.0 battles** |

**Both of §5.6's stated targets hold** at the catalogue's own prices: a normal
battle funds ~1 Recruit or ~⅓ of a Tier I structure, and a Tier I structure takes
2–3 battles. The ratios are internally consistent; they were previously unchecked
because no costed catalogue had been applied to them.

## T14 — Chem Dependence escalation  (§9.4)

Resistance test `1d10 + NRV − Dependence ≥ 7` (nat 1/10 as always):

| NRV | Dep 0 | Dep 1 | Dep 2 | Dep 3 |
|---|---|---|---|---|
| +0 | 40% | 30% | 20% | 10% |
| +2 | 60% | 50% | 40% | 30% |
| +4 | 80% | 70% | 60% | 50% |

Expected consecutive uses before a failed resistance test: **NRV +0 → 1.55 ·
NRV +2 → 2.07 · NRV +4 → 3.02.** Probability of still being clean after four
straight uses: 0% / 4% / 17%.

**The maths is correct and the escalation is the right way round** (the review's
read is confirmed). The system is genuinely light: even an iron-nerved fighter
cracks inside 3 uses, so Chems read as a short-term gamble rather than a build.
That matches the packet's stated intent for a conservative first pass.

---

## Two harness bugs found while running these — both matter beyond this packet

**1. Crew-size parity artefact in objective assignment.** The engine assigns every
model its *nearest* objective at spawn. Because models spread evenly across the
deploy band, coverage depends on crew-size **parity**: a 3-model crew lands exactly
one model on each of the 3 objectives (perfect coverage), a 6-model crew doubles up
on the same three, a 2-model crew abandons the centre. Measured, a full-strength
6-model crew *lost* to 5- and 3-model crews and *beat* 4- and 2-model ones —
non-monotonic in crew size. Fixed behind `engine.BALANCED_GOALS` (default **off**
so no existing finding silently moves). **Any past result that compares crews of
different sizes on Take-a-Hold may carry this artefact** — that includes
`suite.py`'s model-count regression (`r² = 0.708`, +3.78 win-points per model),
which is cited in `POINTS-DECISIONS.md` D21 as the evidence closing the
additive-vs-multiplicative question. Worth re-running before D21 is treated as
settled.

**2. A test that measured a playstyle instead of a mechanic.** The first stealth
harness gave the two sides different AI policies and returned 99% win rates. Fixed
by putting both sides on one policy with the capability as the only difference, and
by adding controls that must land on 50%. The controls are now permanent in the
file so the mistake cannot pass silently again.

## Not tested

- **T7 — controlled-random advancement (§5.4).** Not run. The power-spread half is
  simulable, but the review's actual question is "did the player feel their
  veteran's growth told a story", and it says so itself: *"needs a table, not a
  report."* A sim can tell you the builds are commensurate; it cannot tell you the
  campaign was more interesting.
- **T15 — global-map win normalisation (§10.4–10.7).** Phase 6, app-layer, and
  correctly deferred by the packet.
- Anything requiring the packet's own proposed values (see the note at the top).

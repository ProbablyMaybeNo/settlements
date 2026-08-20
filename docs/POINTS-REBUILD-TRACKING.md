# Points Rebuild — Phase Tracking

**Live status board for the Credits-side rebuild.** Sim results live in
`test-bench/balance/results/` with a provenance envelope each; the reasoning behind
the two hardest findings is in `POINTS-REBUILD-EXPLANATIONS.txt`.

> # ✅ THE REBUILD SHIPPED — 2026-08-13
>
> **The deliverable is `docs/POINTS-CATALOGUE.md`, and the write-back to
> `points/ticks.py` has landed.** Until today no measured price had ever reached
> that file: it carried the legacy ×10 scale, a 1D-board primitive table, and an
> armour level citing a file that has never existed in any commit on any branch.
>
> **Measurement is closed. Table testing refines from here.** Every price now
> carries a confidence tier — **A** measured/significant, **B** measured but
> wide-CI or single-scenario, **C** derived by rule with the derivation stated.
> A C price is fine; an untagged price is not.
>
> **What is deliberately NOT shipped:** five payload traits measuring at or below
> zero — see §BLOCKED below. Everything else ships with its caveat attached
> rather than waiting for a tighter number.
>
> This board continues to record *how* each number was reached and what is still
> wrong with it. It is no longer the thing gating the game.

---

> # ⚠ THE CEILING — what a per-item points system can achieve at all
>
> **Promoted to the top of this board 2026-08-13, deliberately out of the numbered open
> items. It is not one of them. It bounds all of them.**
>
> A weapon's value depends on the crew around it, by **~39%**, measured:
>
> | route to "one model gains an 18″ gun" | value |
> |---|---|
> | **direct** — upgrade one model in an **all-melee** crew | **+10.930** |
> | **composed** — (melee→6″) + (6″→18″), the second hop measured in an **all-6″** crew | **+7.870** |
> | gap | **3.060 ± 1.460 — 2.10 SE, significant** |
>
> Source: `weapon-class-atoms-objective-n5000`, surfaced by `two_route.py` as its first
> **DISAGREE**.
>
> **Why this is not a measurement problem.** Both routes are correctly measured; neither is
> the error. The two hops are measured on **different baseline crews**, and composing them is
> valid only if an item's value is independent of what the rest of the list carries. It is
> not. Giving one model an 18″ gun is worth ~39% more in a crew that owns no other guns.
>
> **What it therefore says.** Every price in this project — every price in most points
> systems — is per-item, set independently of the list it goes into. If item value depends
> materially on list composition, then **a flat per-item catalogue has a hard accuracy
> ceiling, and no amount of better measurement raises it.** Tighter CIs, more scenarios, a
> better AI and a re-derived anchor all improve the numbers *inside* the ceiling. None of
> them move the ceiling itself.
>
> **Stated precisely, because the loose reading is wrong:** this is *not* "reach is
> non-additive within one chassis". It is that the chassis is part of the price.
>
> **Not acted on, and not actionable by measurement.** Whether the catalogue carries
> list-context adjustments — and accepts the complexity that implies — is a design decision.
> The measurement's job here was to establish that the ceiling exists and put a number on it,
> and it has.

---

> ## The test this audit keeps applying
>
> **A number that looks precise, carries a tag or a confidence interval, and is
> denominated in something nobody has measured.**
>
> Every finding so far has been an instance of it. A confidence interval bounds
> sampling noise; it says nothing about whether the units mean anything. Apply it
> before trusting anything below.

---

## 0a · THE BLOCKER, as of 2026-08-13 — scenario coverage, not anchor value

**Ruled: `hold` is dropped.** It scores positionally, the ruleset scores every objective
through an Interact, so it modelled no shipped scenario while carrying half the anchor.

Anchor is now **0.606** (`hold_claim` only, post Sprint + objective-first fix), CI
[0.436, 0.776], **24.77 Cr per win-point**. `gear-anchor-objective-n4000`.

> *Corrected 2026-08-13: this section carried **0.3432 / 43.71 Cr** for a day after §1 and
> `anchor.py` had moved to 0.606. 0.3432 was the pre-policy-fix value of the same quantity —
> measured under an AI that never Sprinted and never took an objective Interact while it had
> a target — and 0.606 rejects it, sitting outside its CI. A stale number in the section a
> reader hits **first** is how the wrong one gets cited later, which is the same findability
> failure as §6's payload table. Both places now agree.*

**0.606 is honest, not correct, and must not read as settled.** It rests on 1 of 5 shipped
scenarios — and the most *static* one.

| Shipped scenario | Shape | Modelled |
|---|---|---|
| Take a Hold | Control, VP accrual | ✅ `hold_claim` |
| Escort | Mobile, **asymmetric** | ❌ |
| Raid | Retrieve, **enemy's half** | ❌ |
| Sabotage | Timer, **sudden death** | ❌ |
| Power Supply | Network, **sudden death** | ❌ |

Pricing the whole game against control play **systematically overvalues defensive and static
atoms — range, damage, armour — and undervalues mobility, tempo, stealth and
objective-running**, which is precisely what the four missing scenarios reward. Internally
clean, structurally biased by what it was measured on: **the DEX-ladder failure one level up.**

**So the question is no longer "which anchor value".** Every atom priced from here inherits
single-scenario bias until the harness covers something structurally different from control
play. **Next build: Sabotage and Raid** — furthest from what `hold_claim` already measures
(sudden-death timing; scoring in the enemy's half), so they expose the bias fastest.

> ### ⚠ PREREQUISITE FOR ESCORT — do not build it until this is resolved
>
> **The Sprint fix introduced a new policy pathology: nobody defends.** Every model's goal is
> the enemy's objective, so crews now leave their own at 12"/round and never return. On
> Sabotage that means a planted charge is **never defused** — pre-fix they defused
> incidentally, by walking past slowly. Encoded as an `xfail` in
> `test_scenario_mechanics.py` with the reasoning attached.
>
> **Escort is explicitly asymmetric** — one side attacks with the caravan, the other *runs out
> the clock and holds a chokepoint*. A policy in which no model ever defends anything cannot
> express the Defender at all, so Escort would be built on an AI that can only play one of its
> two roles. That is the same shape as building Sabotage on an AI that never arrives.
>
> Resolving it means splitting the crew between attack and defence — a policy **design**
> decision (how many defend? chosen how?), not a missed legal action. **Flagged as a
> prerequisite rather than discovered mid-implementation.**

Anchor re-stamp remains **held** — do not spend a durable stamp on a number about to move.

---

## 0c · ⚠ A BUG WAS TREATED AS A PROPERTY OF THE GAME — audit, 2026-08-13

**The most expensive error class in this rebuild, and it ran for the whole project.**

"All-ranged crews cannot score on Take a Hold" was believed to be a fact about the game. It
was load-bearing: a guard was written to exclude those cells as *legitimately* unplayable,
`MIXED6` was added to `rosters.py` specifically to dodge it, the armour baseline was built as
4 rifles + 2 bats for the same reason, and the weapon-class damage ladder was priced from a
**single scenario** because the other "could not resolve".

It was never a property. It was **two missed legal actions** — the AI never Sprinted, and
never took an objective Interact while it had a target. Both fixed 2026-08-13.

### Every excluded configuration now resolves. 4 recovered, 0 still degenerate.

| configuration | scenario | before | after | +1 Damage |
|---|---|---|---|---|
| uniform rifle (6) | hold_claim | **99.3% draws, 0.00 VP** | **33.7% draws** | **+0.951** sig |
| uniform rifle (6) | hold | 100% draws | **2.7% draws** | +1.597 sig |
| uniform pistol (6) | hold_claim | dropped | 29.2% draws | +0.486 n.s. |
| probe chassis (6) | hold_claim | **dropped** | 33.7% draws | **+0.951** sig |

### What has to be re-examined

| Conclusion | Rested on | Status |
|---|---|---|
| Weapon-class **damage ladder priced from `hold` alone** | `hold_claim` "could not resolve" for probe crews | **Void.** Re-run; both cells now live. |
| **Anchor has no second derivation on `hold_claim`** (§5 known gap) | probe chassis degenerating there | **CLOSABLE, not yet closed.** The probe chassis now resolves on `hold_claim` (+0.951 wp, significant), so the cross-check is possible for the first time — but `two_route.py` still reports BASIS-MISMATCH because it reads the *stored* weapon-class artefact, which is pre-fix. It closes when weapon classes are re-run, not before. |
| Stat ladder rows excluding `hold` | uniform rifle crews drawing out | **Void.** Both cells now live. |
| `MIXED6` roster, armour's 4-rifle/2-bat baseline | designed to dodge the degeneracy | Not wrong, but no longer *necessary* — and a uniform chassis is the cleaner isolate. |
| "Uniform ranged crews are structurally unmeasurable" | the guard's stated mechanism | **Withdrawn.** They are measurable and give the tightest cells. |

### The guard itself stays; its explanation was the defect

`measure.py`'s threshold (`draw_rate >= 0.95`) is behaviourally correct and unchanged — it
fires on any cell that fails to resolve, whatever the cause. What was wrong was the comment
attributing the draws to "both sides sit on their own objectives and neither can displace the
other." **That sentence is a claim about the ruleset**, and it is what licensed treating the
symptom as a fact. Rewritten in place: the flag now reads *"this cell did not resolve"*, never
*"this cell cannot resolve"* — a symptom to investigate, not a property to design around.

---

## 0b · POSITIVE evidence: the ruleset's spatial design is coherent as written

Recorded deliberately, because this board is otherwise a list of defects and "no defect
found" is a weaker statement than what the arrival investigation actually produced.

Three independent numbers agree, and each constrains the others:

| | |
|---|---|
| Weapon range caps at **24"** | §558, called load-bearing: the cap exists *because* the zones are 24" apart, so nothing can fire from its own deployment on turn one |
| Deployment zones sit **24"** apart | §558 |
| Take a Hold's ceiling is **15 VP** | = 3 objectives × 5 scoring rounds (no scoring in Round 1) |
| Sabotage's "earliest arm ~Round 2–3" | reachable **only** by Sprint (12"/round): 24" ÷ 12" = 2 rounds to cross, +1 to Interact = 3 |

The clock, the board and the weapon cap were derived from each other and they close. A crew
that sprints crosses in 2 and arms on 3, exactly as the ruleset's own scoring-clock note
claims — **that number was not fitted to the sim, it was written independently and the sim
reproduces it.**

**Corroborated negatively too:** doubling the round limit 6→12 barely moves arrival (sabotage
28.6%→35.9%, raid 55.0%→56.6%). If the geometry or the clock were genuinely wrong, more time
would fix it. It doesn't — crews reach an equilibrium and stop — which locates the fault in
behaviour rather than in space or time.

**The 2026-08-13 "arrival is a ruleset defect" reading is WITHDRAWN on this evidence.** The
rules were internally consistent throughout; `BalancedPolicy` simply never used Sprint, which
the clock assumes. Same error pattern this board exists to catch, caught here by measuring
the fourth candidate instead of choosing among the three named ones.

---

## 0d · THE BROKEN VERSION ALWAYS LOOKS PLAUSIBLE FIRST — ruled a standing expectation, 2026-08-19

Recorded as a rule rather than a run of anecdotes, because the run is now long
enough that treating each instance as a surprise is itself the mistake.

| # | The plausible-looking number | What it was actually measuring |
|---|---|---|
| 1 | anchor **1.150**, twice independently confirmed | an AI that shot instead of advancing |
| 2 | anchor **1.332**, tight CI | Annihilate averaged into an objective price |
| 3 | "all-ranged crews **cannot** score on Take a Hold", 99.3% draws | two legal actions the AI never took |
| 4 | density "clean null", identical **to four decimal places** | terrain that never changed a LOS check — bit-identical games |
| 5 | `two_route` **`ok` — AGREE with 2.0** on armour linearity | a bar set at twice the distance between the rival hypotheses |
| 6 | stat ladder re-run, fully stamped, fresh fingerprints | the void `hold`+`annihilate` basis, reproduced |
| 7 | tier gate **green across all 25 tables** | a 2500-char window reading tags off neighbouring declarations |
| 8 | catalogue validation, Horde beating Elite **69–31** | a fitter that only trimmed downward — a 200-point handicap |

**The pattern.** An instrument artefact is usually *smooth*: bit-identical games,
a clean null, a confident pass, a stable rank order. Real effects are noisy.
**So "this result is clean and interesting" is weak evidence that it is right,
and in this project it has been evidence of the opposite more often than not.**

**The check, before reporting anything:** state what the result would look like
if the instrument were broken, then confirm it does not look like that. #4 and #8
were both caught exactly this way — by asking what a broken version would produce
and noticing the output matched. #7 was caught by printing what the detector saw
instead of trusting that it went green.

**Corollary for a passing check:** a green result deserves the same scepticism as
a red one. Two of the eight above were found by auditing something that passed.

---

## 0 · Standing invariants

| Invariant | Enforced by |
|---|---|
| The unit of account is **raw win-points per model**. Nothing stores Credits. | `harness/measure.py`, `Envelope` |
| The Credits peg (+1 Damage = 15 Cr) is a **choice**, not a measurement. | `harness/anchor.py` |
| Every result carries engine + cost-table + git fingerprints. | `harness/provenance.py` |
| A result whose scenario cannot resolve is **excluded, never averaged**. | `measure.degenerate` guard |
| A dial that does not exist is **refused, never created**. | `measure.set_dials` |
| Body and Gear scales never borrow each other's atoms. | design rule, checked in review |
| Every price carries an SE and a computed significance flag. | `measure.Result` |
| **A guard that fires when nothing is wrong is worse than no guard** — it trains you to ignore it. Every check must be powered well enough that a pass means something. | standing principle, 2026-08-13 |
| A degenerate cell means *"did not resolve"*, never *"cannot resolve"*. Ask what legal action the AI missed. | `measure` guard comment, §0c |
| **EXPECT THE BROKEN VERSION TO LOOK PLAUSIBLE FIRST.** Not a coincidence any more — it has happened on every defect this project has caught, without exception. A measurement that is measuring its own instrument produces a *clean, readable, interesting* number, because the artefact is usually smooth. **Ruled a standing expectation 2026-08-19**: before reporting any result, ask what it would look like if the instrument were broken, and check that it does not look like that. | §0d |
| **A denied action spends nothing.** A condition that denies Sprint/Charge is not shed by *asking* for one — the action never legally occurred. Pinned's "clearing costs the Move" is a stated cost, not a general principle. **Ruled 2026-08-13.** | `policies.can_sprint`, `check_conditions.py` |
| A script that is not a pytest module must not be named `test_*.py`. A file is only collected under the convention its name advertises. | the rename in §5 |
| **PASSING rows get audited, not just failing ones.** A check that cannot fail is worse than no check: it manufactures confidence. Two of the three guard defects found in this project were found by reading a row that said `ok`. **Ruled a standing practice 2026-08-13.** | §5a |
| A ruling that lives in a constant only reaches the callers that read the constant. When a policy changes, **audit every call site**, not just the ones that broke. | §5a |

> ### LIVE CAVEAT — attach to every mobility-adjacent atom measured from here
>
> **"May read low — sprint overcorrection."** Same standing as the Orders AI-limitation
> caveat, not a footnote.
>
> The Sprint fix overcorrects in 3 of 9 head-to-head cells (hold_claim/Mixed 45.6%,
> raid/Fireteam 41.8%, raid/Armoured 39.7%): a crew that runs across open ground gets shot by
> one that advances slowly and shoots. **Accepted deliberately** — the correct fix is an
> expected-value comparison between ground gained and the shot forgone, which is new decision
> surface with its own untested bias, and tuning the threshold until head-to-heads even out is
> fitting the harness to a desired answer.
>
> **It is symmetric** — both arms of every mirror carry the same policy — so it creates no
> A-vs-B skew. What it can do is depress atoms whose value runs through mobility, tempo,
> objective-running or shooting-under-advance, **on Raid especially**.
>
> **If a mobility atom later measures surprisingly low, check this first.** That is the whole
> point of recording it here rather than in a commit message.

---

## 1 · Atom status

Legend — **MEASURED**: current, post-policy-fix. **VOID**: measured under a defect,
must be re-run. **BLOCKED**: cannot be measured on this engine as built.
**JUDGMENT**: chosen, never measured. **OPEN**: Ross's call.

### Gear scale

> **THE OBJECTIVE-ONLY CUT (2026-08-12, commit `09c4462`) VOIDED MORE THAN IT FIXED.**
> `PRICING_SCENARIOS` became `(hold, hold_claim)` — Annihilate is a diagnostic and
> never enters a price. That policy landed **after** every measurement below except
> the sign-split run, so anything priced across `hold+annihilate` is now void by
> construction. Verified per script, not assumed: `measure_anchor.py:45`,
> `measure_payloads.py:65`, `measure_pinned.py:60` each carried
> `SCEN = ('hold','annihilate')`; the stat-ladder and weapon-class result files
> record `scenarios_used: ['hold','annihilate']`. Only `measure_signsplit.py` went
> through `price_atom()` and therefore ran on the new policy.

| Atom | Status | Value | Notes |
|---|---|---|---|
| +1 Damage (the anchor) | **MEASURED — PROVISIONAL** | **0.606** wp/model, CI [0.436, 0.776] | `hold_claim` only, post sprint + objective-first fix. N=4000. **FIFTH value in a row to reject its predecessor** (0.3432 falls outside this CI). `CREDITS_PER_WINPOINT` = **24.75**. Cell spread **1.46×** (0.517–0.756) — tight, and it stayed tight across a fix that nearly doubled the value. **Reproduced by the probe chassis at 0.712** — the project's first real cross-check, and it does *not* settle the number: see §5. |
| Payload table (12 traits) | **MEASURED — post-policy-fix** | suppressive **38** · bleeding **35** · blast **31** · incendiary_fire **23** · AP **10** Cr | Canonical run, `payload-table-objective-n2500`, 2026-08-13. **Three traits now price NEGATIVE and significantly so** — see the box below. Four are indistinguishable from zero (toxic, shocking, heavy_impact, hook). No sign-splits. Values still move with armour prevalence. |
| value(Pinned) | **MEASURED — post-fix** | **+0.510** wp/model, CI [+0.298, +0.722], **significant** (~12.6 Cr) | Tripled from +0.165. It flipped once already (mixed-scenario read −0.013, n.s. — "worth nothing"), and the policy fix tripled it again. Every ranged payload price is NET of this, so gross ≈ measured + 0.510. **Strengthens the redundancy verdict**: Concussive/Crippling/Hook measure ~0 net, so their gross ≈ what the free default already gives. |
| Armour level | **MEASURED — post-policy-fix, single-scenario coverage** | light **+0.953** wp (**23.6 Cr**) · heavy **+1.663** wp (**41.2 Cr**), both significant | `armour-level-n2500`, 2026-08-13, on the fixed policy. Zero prior. **Rebuild-to-pay now brackets it from both sides AND lands one package on parity** — see the box below. Linearity still **CANNOT DISCRIMINATE**: 1.745 ± 0.416, CI [0.930, 2.560]. |
| Range bands | **MEASURED — and the curve REVERSED** | 8″ +5.75 · 12″ +5.17 · 18″ +5.34 · 24″ +4.68 wp | **Flat, and it stayed flat at double the sample.** Whole spread (1.07) sits inside one SE (~0.81). Pre-fix it *accelerated* 8.88 → 12.07. Cited from `-n5000`; the `-n2500` run reads 6.14/5.40/5.22/5.28, same verdict. See the box below. |
| Weapon classes | **MEASURED**, on `hold_claim` for the first time | damage +1 → **0.712** wp | `weapon-class-atoms-objective-n5000`, post-fix. Both cells live — no scenario dropped. **Two runs of this measurement both report LIVE** (N is baked into the measurement name, §9b defect) — `-n5000` is the one to cite and the one `two_route.py` reads. Hands/slots, rank gate, Loud/Quiet, fire-while-Engaged remain unmeasurable, so a class price is damage + range plus a flagged judgment. |
| Hands / slots | **BLOCKED** | — | `Unit` carries one weapon string; `two_handed` is inert. |
| Rank-as-weapon-gate | **BLOCKED** | — | `CLASS_META.min_rank` is read by nothing. |
| Loud / Quiet | **BLOCKED** | — | No noise or alarm system. |
| Fire-while-Engaged | **BLOCKED** | — | `take_action()` forces melee for any engaged unit. |

> ### ⚠ THREE PAYLOAD TRAITS ARE NOW WORSE THAN CARRYING NOTHING — re-measured 2026-08-13
>
> The redundancy verdict has **escalated to a harm verdict**, and it is significant, not noise.
>
> | trait | was (pre-fix, net) | now (net) | Cr | verdict |
> |---|---|---|---|---|
> | **concussive** | +0.018, n.s. | **−0.592 ± 0.143** | **−15** | **significantly NEGATIVE** |
> | **crippling** | +0.012, n.s. | **−0.613 ± 0.145** | **−15** | **significantly NEGATIVE** |
> | **blinding** | (small +) | **−0.317 ± 0.145** | **−8** | **significantly NEGATIVE** |
>
> **What "negative" means here, precisely.** Every payload price is **net of Pinned**, because
> a payload lands *in place of* the ordinary non-wound result and on a ranged hit that result
> is Pinned (worth **+0.510**). A net-negative trait therefore says: **the replacement result
> is worth less than the free default it displaces.** A weapon carrying Concussive is worse
> than the identical weapon carrying nothing. `ticks.py` charges **30** for it.
>
> The old reading was "redundant, not weak — repricing sells the player nothing". The new one
> is stronger and worse: **repricing sells the player a downgrade.** No price fixes it; the
> fix is mechanical.
>
> **Candidate mechanism, flagged as a hypothesis and NOT verified.** Concussive applies
> Off-Balance, and today's ruling changed exactly what Off-Balance does: the target no longer
> burns its whole Move shedding the condition via a denied Sprint, so it keeps its Move *and*
> its Action, and in exchange the condition now persists. That plausibly made the replacement
> result cheaper for the target than the Pinned it displaced. **Plausible is not measured** —
> Crippling and Blinding are unrelated to that code path and moved too, so a single mechanism
> is not established. **The test that would settle it is the one already run for Pinned:
> measure `value(Off-Balance)` directly.** Until then this is a number, not an explanation.
>
> **Also moved, in the other direction:** suppressive **+1.546** (21 → **38 Cr**, now the
> dearest trait) and bleeding **35 Cr**. AP lands at **10 Cr** against `ticks.py`'s 9 — the
> closest agreement between a measured atom and a shipped price anywhere in this rebuild.

> ### ARMOUR NOW HAS A TWO-SIDED BRACKET AND A PACKAGE AT PARITY — re-measured 2026-08-13
>
> `armour-level-n2500`, on the fixed policy. Rebuild-to-pay buys armour and pays for it in
> weapon downgrade; a package at ~0 means the two sides of the trade are equal, so armour's
> price **is** the measured value of what was surrendered.
>
> | package | price | reading |
> |---|---|---|
> | light armour, rifle→pistol | **+0.140 ± 0.200** | **FAIR TRADE — indistinguishable from parity** |
> | heavy armour, rifle→pistol | **+1.110 ± 0.197** | armour worth MORE than the payment |
> | heavy armour, rifle→bat | **−3.400 ± 0.195** | armour worth LESS than the payment |
>
> **Light armour ≈ one rifle→pistol downgrade.** That is the first time an armour price has
> been denominated in a *measured* quantity rather than a prior — `ticks.py`'s Light 30 /
> Heavy 60 is tagged `[measured]` citing `balance/armourprice.py`, **a file that has never
> existed in any commit on any branch**, and the master note's ruled 60/100 is a judgment.
> Heavy is bracketed between the two downgrades rather than pinned.
>
> **This supersedes the pre-fix reading, which said the opposite.** At N=12000 before the
> policy fix, all three packages came back negative and the conclusion was "armour is worth
> *less* than a rifle→pistol step". Post-fix that package sits at parity and heavy clears it.
> The direction of the correction is coherent: the old AI never closed, so a crew that
> surrendered reach was punished far harder than the rules imply.
>
> **Two known biases, both stated because they cut opposite ways.** Armour's own drawbacks
> (Improvised −1 AGI; Heavy −1 MOV / −1 AGI / Loud) are priced at **zero** — AGI is read only
> inside Dodge (`DODGE_ON` False) and there is no noise system — so these figures **overstate**
> armour. Single-scenario coverage (control play) also overstates a defensive atom. Neither
> correction is available yet, so treat the level with suspicion and the bracket as the result.

### Body scale

| Atom | Status | Value | Notes |
|---|---|---|---|
| Stat rung (DEX, one-sided) | **MEASURED — first time on a legitimate basis** | 0→1 **+1.514** · 1→2 +1.044 · 2→3 +1.108 · 3→4 +0.739 · 4→5 +0.619 · 5→6 **+0.422** wp | **37 → 10 Cr, a 3.6× spread, every rung significant, decaying monotonically bar one.** Saturation against the fixed TN, confirmed. **The flat 15 Cr/point charged today is wrong at both ends**: the first point is worth ~2.5× it, the last ~⅔. `stat-ladder-n3000`, `hold_claim` only. |
| Stat rung (STR, opposed) | **MEASURED (structural)** | **+1.011** wp, flat, all six rungs | **25 Cr, identical to four decimals at every rung** — `P(X+a > Y+b)` depends only on `b−a`, so an opposed same-stat roll *cannot* saturate. Structure predicted this before it was measured and the measurement reproduced it exactly. |
| Stat rung (AGI) | **BLOCKED** | — | Read only inside Dodge; `DODGE_ON` defaults False, so it measures zero by construction. |
| Stat rung (INT) | **conditional** | — | Worth zero without a claim step. Books against the **scenario mix**, not the fighter. |
| Stat rung (NRV) | **not started** | — | Never isolated per point by anything. |
| Orders (1 and 2) | **not started** | — | Never measured as an Order on any engine. See §2. |
| Bare body | **not started** | — | Unblocked now that Hold resolves. |
| +1 WND | **not started — LIVE AND UNVALIDATED** | 45 Cr charged | See §7. Not merely unmeasured: it is **shipping in the Level track right now** and the ruleset itself calls it unvalidated in three separate notes. |
| Skills (~150) | **BLOCKED, mostly** | — | 9 of ~150 are wired. The rest need engine work per subsystem. |

> ### A weapon's value depends on the crew around it — ~39%
>
> **Moved to the top of this board as ⚠ THE CEILING.** It does not invalidate the atoms —
> each is correctly measured on its own chassis — but it bounds how well any flat per-item
> price can ever do, which makes it a statement about the project rather than an entry in the
> atom list. Full finding at the head of this document.

> ### RANGE VALUE WAS AN ARTEFACT OF THE AI NEVER CLOSING — 2026-08-13
>
> The single clearest demonstration of the static-bias problem, and it arrived unasked.
>
> | range | pre-fix | post-fix | change |
> |---|---|---|---|
> | 8″ | +8.880 | **+6.140** | −2.74 |
> | 12″ | +9.150 | **+5.400** | −3.75 |
> | 18″ | +10.190 | **+5.220** | −4.97 |
> | 24″ | +12.070 | **+5.280** | −6.79 |
>
> **The drop scales with reach.** That is exactly the signature of an AI that never closed:
> the longer the weapon, the more it profited from a game where nobody advanced, so the
> longer the weapon the more its value was inflated. Fix the advance and the inflation
> unwinds proportionally.
>
> **Post-fix the curve is FLAT** — the entire 0.92 spread sits inside one SE (1.15). Range
> beyond 8″ buys nothing measurable on this chassis.
>
> **Two biases now push range in OPPOSITE directions, which brackets it rather than skewing
> it one way:** single-scenario coverage (control play) *overvalues* static atoms like range,
> while the accepted sprint overcorrection makes crews close hard and *undervalues* it. The
> true value sits between the two, and neither correction is available yet.
>
> The 12″ banding claim remains unsupported — now because the whole curve is flat, not
> because the step at 12″ was small. Same verdict, different reason, and the note below is
> retained because *why* a claim fails changes what would rescue it.

> ### The 12″ turn-one firing threshold does not appear in the data
>
> The banding argument rests on 12″ being the turn-one threshold — deploy zones 24″ apart,
> MOV 6″, so 18″ fires on turn one and 8″ cannot. `measure_weapon_classes.py` was written
> specifically to test that, because nothing ever had. Measured, off a 6″ baseline:
>
> | step | Δ wp | per inch |
> |---|---|---|
> | 6″ → 8″ | **+8.880** | 4.44 |
> | 8″ → 12″ | **+0.270** | 0.07 |
> | 12″ → 18″ | +1.040 | 0.17 |
> | 18″ → 24″ | +1.880 | 0.31 |
>
> **There is no step at 12″.** The 8→12 move is the *smallest* in the whole curve and about
> a quarter of an SE (0.270 against SEs of ~0.77). Above 12″ the curve **accelerates** —
> value per inch rises 0.07 → 0.17 → 0.31 — which is the opposite of a threshold and the
> opposite of diminishing returns.
>
> What dominates instead is the **6″ → 8″ jump: +8.88, thirty times the 8→12 step.** Nearly
> all the value is in "has usable reach at all" rather than in how much. That likely says
> more about the 6″ baseline being pathological on this board than about 8″ being good, so
> the *level* of these Credits figures should be treated with suspicion even though the
> *shape* is clear.
>
> **Caveat on the test, stated because it cuts toward the finding, not away:** all four
> variants were measured against the same `probe_r6` baseline on a shared seed, so their
> errors are correlated and a direct paired 8-vs-12 comparison would be *more* sensitive than
> the naive SEs above. That test has not been run. It could only tighten a difference already
> sitting at a quarter of an SE — but "not significant" here means "no evidence of a
> threshold", not "proof the threshold is absent".

> ### The anchor is 0 for 3. Cite 0.786 with this, every time.
>
> | Anchor | Rejected by | Cause, invisible from inside the number that carried it |
> |---|---|---|
> | 1.150 | 1.332 | `BalancedPolicy` shot instead of advancing |
> | 1.332 | 0.786 | Annihilate averaged into a price |
> | **0.786** | — | *unknown* |
>
> Every one of those runs was **internally clean** — paired estimator, tight CI, sane
> per-cell spread. 1.150 had *two independent confirmations* and they were wrong together.
> The defect was never visible from inside the measurement; it was always in an assumption
> the measurement could not see.
>
> **This is not a reason to doubt 0.786 specifically.** It is the best-founded anchor the
> project has had and the first measured on the scenarios the ruleset actually wins on. It
> is a reason it must never read as *settled* merely because two prior errors were caught.
> Finding two does not imply finding all.
>
> The marking travels in code, not just here: `anchor.PROVISIONAL` is embedded in
> `anchor.describe()`, which every measurement script prints, so a caller who wants only the
> number still gets the caveat.

> ### Two results from 2026-08-13, both labelled single-scenario coverage
>
> **Pinned flipped, and it re-reads the payload table.** Mixed-scenario said −0.013,
> n.s. — "Pinned is worth nothing". Objective-only says **+0.165, CI [+0.033, +0.298],
> significant**. A ranged payload *replaces* Pinned, so every ranged payload price is
> **net** of it and gross ≈ measured + 0.165.
>
> That decides the Concussive/Crippling/Hook question in the direction that **cannot be
> fixed by pricing**. They measured +0.018 / +0.012 / +0.020 net — so gross ≈ 0.18, which
> is *what Pinned is already worth for free*. They are **redundant, not weak**. Repricing a
> trait whose whole effect is to swap one result for an equally-valuable one sells the
> player nothing at any price; the fix is mechanical.
> *Caveat:* the net-of-Pinned relation holds for **ranged** delivery only — a melee
> non-wound is Shaken, not Pinned — so it applies to the ranged share of each trait.
> The per-list gradient (Fireteam −0.04 → Squad −0.17 → **Armoured −0.28**) is coherent:
> Pinned lands on a hit that *fails to wound*, and armour creates those.
>
> **Armour: the "linearity is arithmetic" premise looks wrong.** Measured light **+1.093**,
> heavy **+1.817** (both significant, zero prior). Ratio **1.662 ± 0.239**, CI [1.194, 2.130].
> The guard correctly refuses a verdict — the interval contains 2.0 *and* the ruled 1.667,
> so it cannot discriminate. But note what the point estimate sat on: **1.662 vs the ruled
> Light 60 / Heavy 100 ratio of 1.667.**
> `POINTS-REBUILD-EXPLANATIONS.txt` §2 argued Heavy *must* be exactly 2× Light because each
> armour point is a flat −10% on the injury roll, so "linearity is a property of the
> arithmetic". **That reasoning is about the wrong quantity.** Linear in *injury
> probability* does not imply linear in *win-points* — the second armour point buys
> survival on a model that is already surviving more often, which is a textbook diminishing
> return. So the ruling "the measured invariant wins and Heavy is exactly twice Light"
> rested on an arithmetic claim that does not transfer, and is **reopened**.
> **Rebuild-to-pay bounds armour from above.** All three packages came back significantly
> negative (light+downgrade −2.278; heavy+downgrade −1.358; heavy+drop-to-melee −1.312), so
> even heavy armour does not compensate for losing the rifle. The fair trade lies *between*
> no payment and rifle→pistol — armour is worth **less than** that step, which contradicts
> the old "≈60 Cr, about as much as a rifle" figure that was denominated in the legacy ×10 scale.
> **Known upward bias:** armour's own drawbacks (Improvised −1 AGI; Heavy −1 MOV / −1 AGI /
> Loud) are priced at **zero** here, because AGI is read only inside Dodge (`DODGE_ON` False)
> and there is no noise system. So these figures *overstate* armour.

### Materials axis

| Atom | Status | Notes |
|---|---|---|
| Base gatherer rate | **OPEN — Ross** | Not merely unmeasured: **not computable**. D23 prices structures by payback and the denominator is stated nowhere. Parked, not blocking. |
| Everything downstream | blocked on the above | Structures, workers, trader rates, loot, raid cap/floor. |

---

## 2 · Dependency chain

Read top-down; nothing below a blocked row can be trusted.

```
policy: advance before shooting        FIXED (5bdeafd)
    |
    +-- Take-a-Hold scoring            RESOLVED as a side effect - draws 100% -> 23%
    |       |
    |       +-- proposed tie-break     RE-EVALUATE: it was written for a contest
    |                                   failure, and the failure was non-arrival
    |
    +-- the anchor                     1.332 - itself later voided, see below
    |
    +-- weapon classes                 re-run, then voided again below

policy: objective-only pricing         FIXED (09c4462) - a SECOND root cause,
    |                                   independent of the first
    |
    +-- the anchor                     RE-DERIVED, 0.786 (was 1.332)
    |       |
    |       +-- every Credits figure   all derived through it; everything taken
    |       |                           at 1.332 is low by 1.694x
    |       |
    |       +-- payload table          re-priced by arithmetic, NOT re-run:
    |                                   numerators were already objective-only
    |
    +-- sign-split detector            FIXED - duplicate loose check removed
    |       |
    |       +-- Concussive/Crippling/  re-ran CLEAN: all three flat, no splits.
    |           Hook                    Ross's suspended ruling can resume.
    |
    +-- weapon classes                 VOID AGAIN - re-run on mixed scenarios
            |
            +-- armour level           blocked until classes are real
                    |
                    +-- payload table  moves AGAIN with the armour meta
                    +-- AP             worth 15 vs armour, 0 vs bare

policy: Sprint + objective-first        FIXED (uncommitted) - a THIRD root cause.
    |                                   The AI never took two legal actions.
    |
    +-- the anchor                     RE-DERIVED, 0.606 (was 0.3432)
    |       |
    |       +-- second derivation      CLOSED - probe chassis 0.712, AGREE.
    |       |                           Shares engine+policy+coverage: rules out
    |       |                           derivation error, NOT the failures that
    |       |                           have actually bitten. Still PROVISIONAL.
    |       |
    |       +-- weapon classes         RE-RUN - both cells live, range flat
    |               |
    |               +-- armour level   RE-RUN - bracketed, light ~= rifle->pistol
    |                       |
    |                       +-- payload table   re-running
    |                       +-- AP              after payloads
    |
    +-- degeneracy guard               4 excluded configs recovered, 0 remain
    |
    +-- Off-Balance shed via an        FIXED - a denied action spends nothing.
        illegal Sprint                  The test was right; the policy was wrong.

policy: stat ladder priced on          FIXED - the LAST script hardcoding a
    hold+annihilate                     scenario set. Void twice over, and
    |                                   re-running it reproduced the void basis.
    |
    +-- DEX ladder                     re-running on hold_claim
    +-- STR ladder                     structural (flat); basis corrected anyway
```

**Two independent defects, found in sequence, each invisible from inside the number
the other produced.** The policy fix corrected *how models behave*; the pricing fix
corrected *which games count*. 1.332 was right about the first and wrong about the
second. The general lesson is in §0's one-line test: 1.332 looked precise, carried a
CI, and was denominated in a scenario mix nobody had justified.

**Bare-body pricing** additionally depended on the Take-a-Hold fix, not only on the
deleted `BALANCED_GOALS`. That dependency is now cleared.

---

## 3 · Contaminated prior findings

| Finding | Why | Action |
|---|---|---|
| Anchor 1.12 / 1.1183 / 0.90385 | All measured under the policy defect | **Rejected.** |
| Anchor 1.332 | Correct on policy, wrong on scenario mix — priced across hold+annihilate | **Rejected.** Superseded by **0.786**, which is outside 1.332's own CI. Every Credits figure taken at 1.332 is **low by 1.694×**. |
| "The payload table roughly HALVES" (commit `09c4462`) | Reported a **denominator mismatch**, not a finding: objective-only numerators divided by a mixed-scenario anchor | **Withdrawn.** Numerators were right; the conversion was wrong. True objective-only move is bleeding 44 → **33 Cr**, a ~25% cut, not a halving. |
| Concussive / Crippling "SIGN-SPLIT" verdicts | A second, untightened detector in `measure_signsplit.py` OR'd itself with the real one, so it could only add false positives | **Withdrawn.** Detector removed; re-run reports all three **flat - genuinely ~0**. |
| T9, T11, T12, T14 | `packet_campaign.py` set `BALANCED_GOALS = True`, and campaign crews are exactly the size where it sent every model to one objective | Re-run before use. T12 is **additionally circular** — it sets `BATTLE_CREDITS = RECRUIT_CR` then prints the ratio back as confirmation. |
| T13 | Published table has no harness in any branch; committed raw output is from a superseded implementation | Direction survives, exact values do not. |
| D21's model-count regression | Measured crews of different sizes on a scenario that did not score — **it was reading which crew sizes can deadlock, not which are stronger** | Re-run with crews rebuilt to equal `points/` cost. |
| Turret / roof / lone-runner headlines | `run.py` credits side A half the draws and side B none | Turret edge is ~1.6 pts, not the ~7.8 implied. |
| Every payload price pre-2026-08-12 | Melee never delivered a payload; divisor counted melee carriers anyway | Re-running. |

---

## 4 · Open decisions — Ross

### 4b · ⚠ OPEN RISK — melee loses every matchup. Falsification condition set 2026-08-20.

**Logged as an open risk, NOT a resolved question.** The diagnosis below is a
hypothesis, and plausible hypotheses have been wrong here before (§0d).

`catalogue-validation-n1500`, after the body rebase. The melee archetype loses to
everything:

| Matchup | melee's share |
|---|:--:|
| vs Armoured | **38.8%** |
| vs Horde | 41.1% |
| vs Elite | 44.2% |

**The hypothesis:** it is scenario coverage, not pricing. Melee gets no value from
a range curve that is flat by measurement, and `hold_claim` — the only scenario
anything is priced on — rewards holding ground over closing it. Raid and Sabotage
are built, pass verification, and are structurally where a melee crew should earn
its keep: Raid scores in the *enemy's* half, Sabotage is a timer that rewards
arriving.

> ### THE FALSIFICATION CONDITION — written now so it is testable later
>
> **Re-run `measure_catalogue.py` on `raid` and `sabotage`.**
>
> - **If melee's share rises toward parity on either** → the hypothesis holds. It
>   was coverage. No reprice; extend `PRICING_SCENARIOS` and re-derive.
> - **If melee still loses every matchup on all three scenarios** → the hypothesis
>   is FALSE and this is a **rules problem, not a pricing one**. A reprice cannot
>   fix it: making melee weapons cheaper buys more of something that does not
>   work, which is the Concussive failure in a new place (§BLOCKED). The fix would
>   be **structural — melee needs something ranged does not have** (a charge
>   bonus, a free Interact on arrival, an armour interaction) and that is a design
>   decision, not a number.
>
> **Do not let "better coverage will fix it" survive as an assumption.** It is a
> prediction with a stated way to be wrong, and the run that settles it is cheap.


> ### 🚫 BLOCKED — REDESIGN. Five traits pulled from the catalogue, 2026-08-13.
>
> **The game currently sells five things that make an attack worse than not
> buying them.** Net of Pinned: crippling **−0.613**, concussive **−0.592**,
> blinding **−0.317** (all significant), hook −0.230, toxic −0.080.
>
> **Measured, not assumed** (`condition-values-n3000`): value(Off-Balance)
> **+0.000 exactly** — bit-identical games; value(Hobbled) +0.078 n.s.;
> value(Blind) **+0.369, significant and positive**.
>
> **The mechanism was counted.** Off-Balance and Hobbled are applied 89,498 times
> but land on models that have already arrived and will not move again: afflicted
> models are **0.8% of all movement**, and the reduced cap binds in **0.8% of
> those**. A movement debuff that lands after movement has finished binds on
> nothing. **The tidy "the Sprint ruling caused it" story is dead** — Hobbled
> never touches that code path and behaves identically, exactly as Ross predicted
> when he flagged Crippling and Blinding as the detail that breaks it.
>
> **Blind is a different case entirely**: a genuinely valuable condition that
> still prices negative, because what it *replaces* is worth more.
>
> **THE QUESTION FOR ROSS, and it is a rules question, not a pricing one:**
> replace-not-stack was designed when Pinned was believed worth ~zero. Pinned
> measures **+0.510, significant**. If the default result is strong, every trait
> that replaces it starts in a hole. That is plausibly **one miscalibrated rule,
> not five broken traits.**
>
> *Logged, not chased (per standing instruction):* value(Pinned) is itself
> **list-dependent** — +0.510 on mixed rosters, +0.086 n.s. on a uniform rifle
> chassis. Every payload price is net of it, so the subtrahend moves with the
> crew. THE CEILING, operating on the payload table.

1. **Base gatherer rate.** A scale choice like the 15. Materials is not computable without it.
2. ~~**Does the anchor need non-linear treatment?**~~ — ✅ **CLOSED 2026-08-13. SHIP FLAT.**
   The density re-run on the fixed policy (`density-sweep-n2000`, 9/11/12 nested boards) moves the anchor by **+0.176 ± 0.184 — stable within noise**. The payload also holds; only armour:light moves with density (0.140 at 11, 0.508 at 9), which is a caveat on armour, not on the anchor. Combined with §4a — the 5.0× spread that motivated the question turned out to be the `hold`/`hold_claim` gap, i.e. two different games averaged, and the hold_claim-only spread is 1.46× — **the flat scalar is correct and the question is permanently closed.** Original reasoning retained below.
3. ~~**The armour heavy/light ratio.**~~ — ✅ **CLOSED AS UNANSWERABLE, 2026-08-13.** Measured 1.745 ± 0.416; excluding 2.0 needs N≈66,000 and excluding the ruled 1.667 needs N≈194,000, and if the truth sits between them no N ever separates them. **The individual values (Light 24, Heavy 41) are what get used; nobody plays with the ratio.** Deleted from the open list rather than left to attract effort.

   *Superseded detail for item 2:* **HELD, and the case for "yes" has largely collapsed.**
   The objective-cell spread is **1.46× (0.517–0.756)**, not the 5.0× that motivated this question. §4a found why: the 5× was the `hold`/`hold_claim` gap — *the cost of the claim step*, two different games being averaged — and not dispersion in the atom. Priced on `hold_claim` alone it was 1.35× before the policy fix and 1.46× after, i.e. **tight, and stable across a fix that nearly doubled the anchor.**
   **Still held, but for a smaller reason than before.** Terrain density is a measured **66-point win-rate swing** (`Full Rules System v1` §187; `Crew Sim — Findings`; parity at 9–12 large features), and the sweep that would settle its effect on the spread is **now void** — `density-sweep-n2000` predates the Sprint + objective-first fix. It needs a re-run before this can be closed. **That re-run is cheap and is the obvious next measurement after coverage.**
   *See §4a — the spread number is not the interesting part of this finding, and must not be the thing that gets carried forward.*

### 4a · The `hold` / `hold_claim` gap — ✅ **RESOLVED 2026-08-13. Mechanism found.**

> **The gap was measuring the cost of the claim step.** `hold_claim` requires an INT 7+
> Interact that costs the Action; `hold` scores by proximity and costs nothing. An Action
> spent claiming is an Action not spent attacking, so a damage buff has fewer chances to
> land. The two scenarios were never dispersion around one quantity — they were two
> different games, and `hold` is the one that is not in the ruleset.
>
> **Consequences, all confirmed:**
> - `hold` dropped from pricing (ruled). It carried half the anchor's weight while modelling
>   no shipped scenario.
> - **The 5.0× spread was an artefact.** Priced on `hold_claim` alone the anchor's cell
>   spread is **1.35×** (0.292–0.396). So the main evidence for flat-vs-**curve** was the
>   scenario mix, not the atom. §4.2 is materially weaker than it looked — still open pending
>   density, but no longer pointing where it seemed to.
> - Flagging this as *distinct from* "wide spread" is what made the mechanism findable. Folded
>   into a dispersion narrative it would have been "resolved" by the density sweep showing
>   something unrelated.

> **INDEPENDENT CORROBORATION, 2026-08-13 — recorded separately, not folded into the ruling
> above.** The `hold` drop was decided on the mapping argument (`hold` models no shipped
> scenario). A *second, unrelated* sign-split then turned up in armour rebuild-to-pay, found
> while chasing a different question:
>
> | package | hold | hold_claim | annihilate |
> |---|---|---|---|
> | heavy armour + surrender rifles | **−4.729** | **+1.858** | −5.062 |
>
> Opposite signs, both large. Positional scoring rewards shooting enemies off objectives, so
> losing guns is ruinous; claim scoring spends Actions on INT tests, and an armoured melee
> crew that arrives and claims does fine. **The two scenarios reward opposite loadouts.**
>
> The earlier reading "armour is worth less than the payment" was **−4.7 and +1.9 cancelling**
> into a plausible mid-sized negative — the Pinned failure again, in a new place. This is
> evidence the original ruling did not rest on and did not predict, which is why it is logged
> as corroboration rather than merged into the reasoning above.

*Original analysis retained below — being right for a findable reason is part of the record.*

**Do not fold this into the spread narrative.** A wide spread and this are different objects,
and this one is the more troubling of the two.

| | `hold` | `hold_claim` | ratio |
|---|---|---|---|
| Fireteam (6) | +1.319 | +0.342 | 3.9× |
| Squad (8) | +0.898 | +0.292 | 3.1× |
| Armoured (6) | +1.471 | +0.396 | 3.7× |

A "5× spread" implies dispersion — cells scattered, some high, some low, the average a
reasonable summary of a noisy quantity. **That is not what this is.** This is a *systematic,
replicated, same-signed gap between two named scenarios, 3/3 across every list tested*, with
the ordering identical every time and the ratio stable at 3.1–3.9×. Dispersion would not
reproduce its own rank order three times out of three.

**Why it is worse than a wide spread.** Both scenarios are **inside the pricing set**. The
objective-only cut was justified on exactly this logic — that averaging across two families
which disagree describes neither, and Annihilate had to go. The same test, applied to what
remains, does not obviously pass: `hold` and `hold_claim` do not disagree in *sign*, so the
tightened detector correctly stays silent, but they disagree in *magnitude* by a stable
factor of ~3.5 in every single cell. The pricing set may therefore still straddle a boundary,
one detector-width below the threshold that would flag it.

**What it is not.** Not a sign-split — the detector is right not to fire. Not noise — 3/3
replication with stable ordering. Not an artefact of one list — it holds on Fireteam, Squad
and Armoured alike, across bare and armoured chassis.

**What would resolve it.** The gap has an obvious candidate mechanism: in claim mode
activations go to claiming rather than attacking, so a damage buff has fewer opportunities to
land. If that is the whole story, the correct price depends on **the expected scenario mix in
real play** — which is a Ross decision about what fraction of games are claim games, not a
measurement. That question is not currently on the open-decisions list and should be.

**This may end up mattering more than the density result.** Density moves the spread; this
asks whether averaging inside the pricing set is legitimate at all. Flagged here so it is not
absorbed into "the anchor has a wide spread" and quietly resolved by whatever the density
sweep happens to show.

#### The weapon-class run turned this from a pattern into a quantity

Two independent confirmations arrived from `weapon-class-atoms-objective-n2500`, which was
not designed to test any of this:

**1. The gap replicates on an unrelated atom, harder.** Range probes read `hold` +15.42 to
+18.96 against `hold_claim` +2.26 to +5.18 — a **3.7–6.9× gap**, same direction, all four
rungs. Dispersion does not reproduce its own rank order across unrelated measurements on a
different chassis.

**2. It is worth 36% of the anchor, and the probe chassis proves the anchor is otherwise
right.** All four damage probes returned `hold_claim` **degenerate**, so the damage ladder
priced from `hold` alone. That accident is the cleanest evidence yet:

| | value | basis |
|---|---|---|
| `probe_d2` (= +1 Damage on probe chassis) | **1.300** ± 0.217 | hold only |
| anchor, `hold` cells only | **1.229** | hold only |
| anchor, as published | **0.786** | hold + hold_claim |

The probe chassis **independently reproduces the anchor** — 1.229 sits comfortably inside
`probe_d2`'s CI [0.875, 1.725] — and the entire apparent 1.65× discrepancy between 1.300 and
0.786 is *nothing but the claim-scenario dilution*. Two different crews, two different
chassis, same answer once compared like with like.

**So the scenario-mix question is not academic and is not small.** "+1 Damage" is worth
**1.23** if claim games do not count and **0.786** if they count equally — a **36% swing in
the constant every Credits figure in the project is divided by**. That is a larger lever than
most of the atoms this rebuild is measuring, and it is currently being set by an unexamined
default (`hold` and `hold_claim` weighted 50/50 because there are two of them).

**This is now the top open question, ahead of flat-vs-curve** — see §4.5. Flat-vs-curve asks
what shape the constant should be; this asks what the constant *means*, and it has to be
answered first.

**One comparability defect it leaves behind:** within a single result file, range rows are
priced from two objective scenarios and damage rows from one, because `hold_claim`
degenerated only for the latter. The degeneracy guard is doing the right thing — excluding
rather than averaging a scenario that cannot resolve — but the surviving rows are then
denominated differently from each other, and the file does not say so on its face. A row
priced from `hold` alone is systematically **higher** than one priced across both, by exactly
the §4a factor. Any catalogue built by reading rows off this table side by side inherits
that. `priced_from` is recorded per row; nothing yet *warns* when rows in one table disagree.
### 4.5 · SCENARIO MIX — the mapping, written down BEFORE any weighting

**Ruled 2026-08-13:** weight by actual frequency in the shipped pack, not 50/50, because
50/50 is denominated in "the harness happened to have two scenario types" — the same class of
defect as the legacy ×10 weapon scale and armour's 30/60. **Condition of the ruling: map the
five explicitly here first, and state coverage gaps rather than forcing a scenario into the
nearest bucket.** Executing that condition produced the finding below.

#### The ruleset's own rule for every objective

> "**Objectives are Interacts** — base contact, costs the Action, resolves as `1d10+Stat` vs
> 7+. Claim/activate/connect → INT." — `Full Rules System v1` §12.7 preamble

**There is no proximity-only scoring anywhere in the ruleset.** Every objective in all five
scenarios costs an Action and a stat test.

#### The mapping

| # | Ruleset scenario (§12.7) | Shape | Sim representation | Verdict |
|---|---|---|---|---|
| 1 | **Take a Hold** | Control. 3 terminals on centreline, **claimed via INT 7+**, 1 VP per held terminal per End Phase, Rounds 2–6 | `hold_claim` | **FAITHFUL** |
| 2 | **Escort** | Mobile, **asymmetric**. Caravan 6″/Action to the far edge; defender gates a chokepoint | — | **NOT REPRESENTED** |
| 3 | **Raid** | Retrieve. 3 hidden caches in your *own* half, score by looting the *enemy's*, one secret 2-VP Jackpot | — | **NOT REPRESENTED** |
| 4 | **Sabotage** | Timer, **sudden death**. Arm a charge (INT 7+), 3 End Phases, defuse (DEX 7+) | — | **NOT REPRESENTED** |
| 5 | **Power Supply** | Network, INT-primary, **sudden death**. Hub + 4 nodes, adjacency lines within 8″ | — | **NOT REPRESENTED** (nearest is `hold_claim`, but adjacency and sudden-death are both absent) |
| — | — | — | `hold` | **MODELS NO RULESET SCENARIO** |

#### The two findings that fall out, neither of them small

**1. `hold` is not a scenario in this game.** `engine.py:880-889` scores `claim_mode=False`
positionally — "bodies-in-area", `if a and not b: vp[0] += 1`, no stat test at all. The
ruleset requires an INT 7+ Interact to claim a terminal (`try_claim`, `engine.py:854`). So
`hold` is a **harness simplification that omits the claim step**, and it corresponds to
nothing in §12.7. It is currently carrying **half the weight of the anchor**.

Whether `hold` is a legitimate *proxy* for the four unmodelled scenarios — fighting over
ground generally — is a defensible design position, but **nobody has taken it explicitly**,
it is written down nowhere, and it is not what the rules describe. That is precisely the
convenience-not-measurement pattern the ruling was made to eliminate.

**2. Coverage is 1 of 5, and weighting cannot repair that.** The anchor's sample faithfully
represents **one** of five shipped scenarios. Four are absent — and they are not minor
variants: two resolve by **sudden death** rather than VP accumulation, one is **asymmetric**,
and one scores in the **enemy's** half rather than the centreline. An atom's value under
sudden-death or asymmetric play is not obviously a rescaling of its value under VP control;
it could differ in sign, as Annihilate did.

**Stated plainly rather than smoothed, per the ruling:** weighting the covered part more
precisely does not fix the uncovered 4/5, it makes the gap harder to see.

#### What the honest weighting would do to the anchor

If the pack is the denominator and `hold` is dropped as modelling nothing:

| Basis | Anchor | Cr/wp | vs current |
|---|---|---|---|
| `hold` only | 1.229 | 12.20 | — |
| **50/50 (current, unchosen)** | **0.786** | **19.08** | — |
| `hold_claim` only (= Take a Hold, faithfully) | **0.343** | **43.73** | **prices ×2.29** |

Per-cell `hold_claim`: Fireteam 0.342 · Squad 0.292 · Armoured 0.396.

**This is a bigger move than any correction so far** — larger than the policy fix (×1.19) and
the objective-only cut (×1.69) combined. **It is not applied.** It needs Ross's ruling on
whether `hold` stays as a declared proxy for the unmodelled four or is dropped as
unrepresentative, and that is a design decision about what the game *is*, not a measurement.

**Consequence for the anchor re-stamp:** deliberately not run yet. Re-running under weights
that are themselves in question would spend 72,000 games to durably stamp a number this
mapping may supersede — the exact 1.332 mistake, one level up.

3. **The Take-a-Hold tie-break**, re-evaluated now that the scenario resolves on its own.
4. **`IN_POSITION` 2.5 → 3.0.** Folded into the policy fix as a fidelity correction, not required by the invariant. Can be isolated and measured separately on request.
5. **Concussive, Crippling and Blinding are now measured as a DOWNGRADE, not merely redundant** — significantly negative net of Pinned (−0.592 / −0.613 / −0.317). `ticks.py` charges 30 / 30 / 4. **This is a rules decision, not a pricing one**: no price makes a trait worth buying when it replaces the free default with something worse. Either the traits change mechanically or they leave the weapon list. Was previously "redundant"; the escalation to "harmful" is new evidence and changes what the fix has to be.
6. **Melee models charge foes instead of pressing objectives.** The one remaining Sabotage verification failure (Mixed crew, 59.8% zero-interaction; melee end 9.83″ from the goal against ranged 2.79″). Both actions are already legal and taken — the question is **priority**, which is a genuine behavioural tradeoff rather than a missed action, so it is not being guessed at.
7. **Nobody defends anything.** Prerequisite for Escort, and it also closes the Sabotage no-defuse `xfail`. Needs an attack/defence split — how many defend, chosen how — which is policy *design*.

---

## 5a · THE SCRIPT AUDIT — run 2026-08-13, recorded because it happened, not because it passed

`measure_stat_ladder.py` was found still pricing on `("hold", "annihilate")`, hardcoded in
its own loop, having never routed through `price_atom()`. **Two rulings — the objective-only
cut (`09c4462`) and the `hold` drop (`6a54c6b`) — both changed `PRICING_SCENARIOS`, and
neither reached it.** A ruling that lives in a constant only governs the callers that read
the constant.

So every other script was checked for the same defect rather than assumed clean. **Recorded
in full, because "I checked the rest" is worthless unless it says what was checked.**

| Script | Prices via | Verdict |
|---|---|---|
| `measure_anchor.py` | `price_atom()` | ✅ clean — `hold`/`annihilate` appear as display columns only |
| `measure_pinned.py` | `price_atom()` | ✅ clean — display columns only |
| `measure_payloads.py` | `price_atom()`, averages `price_wp` across lists | ✅ clean — verified the average is over objective-only cells, not over all three scenarios |
| `measure_weapon_classes.py` | `price_atom()` | ✅ clean — display columns only |
| `measure_armour.py` | `price_atom()` | ✅ clean — display columns only |
| `measure_signsplit.py` | `price_atom()` | ✅ clean — display columns only |
| `measure_density.py` | `price_atom()` | ✅ clean |
| `measure_elevation.py` | `price_atom()` | ✅ clean |
| `measure_conditions.py` | `price_atom()` | ✅ clean — written after the ruling |
| **`measure_stat_ladder.py`** | **its own hardcoded loop** | ❌ **THE DEFECT.** Fixed. |

**One of ten.** The value of writing this down is that the next reader can tell the
difference between "audited and clean" and "nobody looked".

---

## 5 · Known harness defects

- **✅ FIXED 2026-08-13 — THE SPRINT FIX WAS SHEDDING A CONDITION VIA AN ILLEGAL ACTION.**
  Caught by `check_conditions.py`, which went from ALL PASS at `6a54c6b` to one FAIL —
  *"Off-Balance PERSISTS until something sheds it"* — under the uncommitted policy. Mechanism:
  the new sprint branch called `move_to(u, goal, 2 * u.mov)` unconditionally, which reaches
  the engine's denial path, and that path spends the Move and clears the condition. So a
  model shed Off-Balance by attempting a Sprint it was never allowed to make.
  **Ruled: a denied Sprint spends nothing; the condition does not shed.** The policy must not
  ask for a sprint it cannot have — `policies.can_sprint(u)` now gates it, and an Off-Balance
  model falls through to an ordinary Move, keeping its Action. **The test was right and the
  policy was wrong**, which is the opposite of the previous two condition-vs-policy conflicts
  (the defuse `xfail`, the degeneracy guard) where the test had been quietly asserting the
  AI's inaction. Worth distinguishing: *"the test encodes the old AI's failure"* and *"the new
  AI does something illegal"* look identical from the failure line alone.
  **The same defect was pre-existing in the melee branch** (`move_to(..., 2 * u.mov)` and the
  charge, both denied by Off-Balance on the same terms) and is corrected in the same pass.
  **Residual, flagged not fixed:** `engine.move_to` still implements shed-on-denial, and
  `check_conditions.py:112` asserts it. That is now unreachable from `BalancedPolicy` but
  `RunnerPolicy` still sprints unconditionally. The ruling's reasoning says the engine line is
  also wrong; changing it would contradict a passing check, so it needs a separate ruling.
- **✅ FIXED 2026-08-13 — THE CONSISTENCY CHECKER ISSUED THE EXACT FALSE ALL-CLEAR IT WAS
  WRITTEN TO PREVENT.** `two_route.py` reported the armour heavy/light row as **`ok` (AGREE
  with 2.0)** on the same numbers `measure_armour.py` printed **CANNOT DISCRIMINATE** from.
  Two files, one dataset, opposite verdicts — and the checker's was the reassuring one.
  **Cause: a relative informativeness test asked the wrong question.** The bar was
  `gse < 0.35 × value`, i.e. 0.611 at a ratio of 1.745 — **nearly twice the entire 0.333
  distance between the two rival hypotheses** (2.0 vs the ruled 1.667). So the row could never
  have separated them and passed anyway. The relative rule is a fine generic proxy for *"is
  this measurement worth anything at all"*; it is the wrong test when the check is asked to
  **separate two named candidates**, where the bar is set by the distance between them.
  Fixed: `compare(..., resolve=)` takes the smallest difference the check must be able to
  detect, and the armour row passes `|2.0 − 1.667|`. It now reads **INCONCLUSIVE**, agreeing
  with the measurement script. **Third instance of the recurring shape** — after "staleness
  couldn't see the pricing policy" and "the fingerprint set didn't cover the scripts", a guard
  again failed to cover the case it was built for. **Found by reading a passing row, not a
  failing one.**
- **✅ FIXED 2026-08-13 — A VOID ARTEFACT WAS REPAIRED BY RE-RUNNING IT, AND THE RE-RUN
  REPRODUCED THE VOID BASIS.** `measure_stat_ladder.py` was the **last script still pricing
  on `("hold", "annihilate")`**, hardcoded in its own loop. It never routed through
  `price_atom()`, so **neither** of this project's two scenario rulings ever reached it: not
  the objective-only cut (`09c4462`, Annihilate is a kill scenario) and not the `hold` drop
  (`6a54c6b`, models no shipped scenario). Both rulings changed `PRICING_SCENARIOS`, and a
  policy that lives in a constant only protects the callers that read the constant.
  The board had this artefact marked **VOID** on both counts and that was not enough — the
  obvious remedy, re-running it on the fixed policy, produced a *fresh* artefact, correctly
  fingerprinted, fully stamped, and denominated in a scenario mix the project rejected twice.
  **A stale result is repaired by fixing the script that made it, never by re-running it.**
  Fixed: routed through `price_atom()`, `hold` and `annihilate` retained as diagnostics so the
  sign-split detector still sees them. The bad run is preserved as
  `…CONTAMINATED-priced-on-hold-plus-annihilate.json`, same treatment as the broken-ladder
  density sweep. **Every other measurement script was then audited for the same defect: all
  remaining `hold`/`annihilate` references are display columns, and only this one priced from
  them.**
- **✅ FIXED 2026-08-13 — pytest ran no tests at all from the repo root or `test-bench/`,
  and the overnight log's "16 passed from all three directories" was false.**
  `engine2d/test_conditions.py` is an executable check script, not a pytest module: it runs
  at import and calls `sys.exit`. Under that name pytest **collected** it, the exit fired
  during collection, and a collection error interrupts the entire run — `no tests ran`.
  Only `harness/` worked, because pytest never walked up to `engine2d/`.
  **Same failure class as the R3 `sys.path` collection error, one directory further out**, and
  the second time a collection error has silently disabled the whole suite. Fixed by the name
  rather than an ignore rule — renamed **`engine2d/check_conditions.py`**, four referencing
  notes updated, and the `sys.exit` wrapped in a `__main__` guard so an import can no longer
  kill the importing process. Verified: **15 passed + 1 xfailed from the repo root, from
  `test-bench/`, and from `harness/`**, and the script still exits non-zero on a real failure.

- **Fingerprint-before-run: fixed in 3 of 6.** The `measure_*` scripts built their `Envelope` at the **end** of a run, so an edit landing mid-run would stamp a result with code it never executed. `measure_anchor.py`, `measure_payloads.py` and `measure_weapon_classes.py` now capture engine/cost/harness/git **before** the first game. `run_stamped.py` always did. **`measure_pinned.py`, `measure_stat_ladder.py` and `measure_signsplit.py` still do not.**
- **ARTEFACT FILENAMES NOW GUARANTEE UNIQUENESS — RULED, FIXED 2026-08-12.**
  The old stem was `name-engine8`, which is content-independent: re-running a script with the same name, N and engine **silently overwrote** the prior result. Not theoretical — it destroyed the sign-split artefact on 2026-08-12, recoverable only because a commit happened to be 26 minutes old. `git show` is not a durability guarantee for an uncommitted run.
  This was the **second** artefact-naming defect in two milestones (after the misleading-filename finding in §6), and both traced to the same root: **the filename carried no uniqueness guarantee**. So the fix is the class, not the instance.
  Stems are now `name-e<engine8>-h<harness8>-<YYYYmmdd-HHMMSS>`, which cannot collide even for a byte-identical re-run, and `write()` **raises `FileExistsError` rather than clobbering** if one ever somehow does. No CI check can catch a silent overwrite after the fact, because the evidence is precisely what got deleted — so the guarantee has to be structural.
  Unique names create their own findability problem — one measurement name, many files, only one live — so `staleness()` now groups by name and labels the newest `<- LIVE` and the rest `superseded by …`, and `provenance.latest(name)` returns the live path so nothing has to hand-pick a filename.
- `policies.py` still carries fixed action priorities beyond the one fixed: no kiting, no focusing a slowed target, unconditional Pinned-clearing, and `issue_orders_attack` picks `ready[0]` by **list order**. So 0.786 is the best estimate under a *less wrong* AI, not a provably right one.
- `engine2d/data.py` keeps its own 100-scale cost table, separate from `points/ticks.py`. No price has ever been verified end to end.
- **A second sign-split detector existed and was removed** (`measure_signsplit.py`). It tested raw sign with no significance requirement and was OR'd with the real one in `price_atom`, so it could only ever *add* false positives and silently defeated the tightening beside it. Lesson recorded because the shape generalises: **a duplicate check OR'd with the real one is strictly worse than no check** — it cannot be fixed by improving the real one.
- **✅ CLOSED 2026-08-13 — the anchor now HAS a second derivation, and it is the first real
  corroboration this project has produced.** Post-fix the probe chassis resolves on
  `hold_claim`, and at N=5000 the two routes agree: **rosters 0.606 vs probe chassis 0.712,
  gap 0.106 ± 0.164 — AGREE.** Different crews, different chassis, same basis. After five
  anchor values each of which was internally clean and wrong, that is worth recording as a
  genuine result rather than a checkbox.
  *It took two attempts: at N=2500 the same comparison read INCONCLUSIVE, flipping on a
  margin of 0.0005 in the informativeness test — a verdict decided at the fourth decimal is
  not a verdict, so N was doubled rather than the pass accepted.*

  > **WHAT IT DOES NOT DO — ruled 2026-08-13, and this is the part that must travel with it.**
  > The two routes share an **engine**, a **policy** and **single-scenario coverage**. So the
  > check rules out *derivation error in one path* — a bad roster, a mis-specified probe, an
  > estimator mistake on one side. It does **not** touch the failure class that has actually
  > bitten this project four times out of four: **a policy missing a legal action, or a
  > scenario sample that does not represent the game.** Both of those move both routes
  > together and by the same amount, and the agreement would be just as tight if both were
  > wrong.
  >
  > **Independent-within-the-same-instrument is not independent.** 1.150 had two independent
  > confirmations and they were wrong together, for exactly this reason. `0.606` therefore
  > stays **PROVISIONAL**; this result raises confidence in the arithmetic, not in the
  > premises. Genuine independence requires a different scenario — which is what the coverage
  > work in §0a is for.

  Original entry retained below.
- **~~KNOWN GAP: the anchor has no independent second derivation on `hold_claim`.~~**
  Surfaced automatically by `two_route.py`. The only other route to +1 Damage is the
  weapon-class probe chassis (`probe_d2`), and its `hold_claim` cell is **degenerate** — a
  uniform ranged crew is exactly the configuration that draws out on claim games. So the
  anchor's only clean cross-check (roster 1.229 vs probe 1.300) lives on **`hold`**, the
  scenario now dropped.
  **Do NOT reintroduce `hold` to close this.** That would be re-adding a scenario the ruleset
  does not contain in order to validate a number, which inverts the point of the check. A
  real second route needs a *mixed* probe chassis that resolves on claim games — i.e. a
  chassis that is not uniformly ranged. Logged as a standing gap; the checker reports it as
  BASIS-MISMATCH rather than silently passing.
- **The live anchor artefact reads STALE, correctly, and should be re-stamped.**
  `gear-anchor-objective-n4000` was measured *after* the objective-only cut but *before*
  `harness_fingerprint()` existed, so it reports `harness(unstamped)` — "cannot verify",
  not "known changed". The checker is right to flag it and the distinction is already in
  the output. But the project's most load-bearing artefact should not be the one file
  that reads unverifiable. A re-run reproduces it exactly (fixed seed, same engine, and
  `measure_anchor.py` derives the anchor rather than importing it) — it costs ~72,000
  games purely to earn a stamp. **Ross's call whether that is worth the time.**
- **THE STALENESS CHECKER CANNOT SEE THE DEFECT THAT VOIDED HALF THIS BOARD — RULED, FIXED 2026-08-12.**
  Before the fix, `weapon-class-atoms-n3000`, `stat-ladder-n3000` and `value-of-pinned-n4000` all reported **`ok` / CURRENT** despite being void: `staleness()` compared only the **engine** and **cost-table** fingerprints, and the pricing policy that voided them lives in `harness/measure.py`, which nothing covered. The module written to catch stale artefacts could not catch itself.
  **Fixed:** `harness_fingerprint()` now text-hashes `measure.py` (PRICING_SCENARIOS, estimator, guards, sign-split detector), `effects.py` (the divisor — a ~20% swing) and `anchor.py` (VALUE). Text-hashed rather than value-hashed, the opposite choice from the cost table, and deliberately: `ticks.py` is mostly commentary so rewording must not invalidate a result, whereas these three are logic and an estimator can change completely while its constants sit still. **False-stale is noise; false-fresh is the failure this module exists to prevent.**
  Every stored result went stale at once, which is the checker finally reporting accurately rather than a cost — everything measured pre-objective-only *is* stale. Results carrying no harness fingerprint report `harness(unstamped)`, distinguishing "cannot verify" from "known changed".

---

## 6 · Artefact hygiene — the payload table exists in three states

All three are **kept on disk deliberately**, none overwritten, on the same footing as
`packet_battle-n2000.txt`: a stale artefact preserved because the *way* it went stale is
the evidence. The staleness checker (`provenance.staleness()`) reads all of them.

| File | bleeding | State |
|---|---|---|
| `payload-table-meleefixed-n2500-3b61ae81.json` | 3.914 wp → **44 Cr** | Mixed numerator ÷ mixed denominator. Superseded. |
| `payload-signsplit-n3000-…SUPERSEDED-mixed-denominator.json` | 1.726 wp → **19 Cr** | Objective numerator ÷ **mixed** denominator. Superseded. Also carries the two false SIGN-SPLIT verdicts. |
| `payload-signsplit-n3000-3b61ae81.json` | 1.726 wp → **33 Cr** | Correct, but under the *diagnostic's* name. Superseded as the table. |
| **`payload-table-objective-n2500-e3b61ae81-h42615a70-…json`** | 1.765 wp → **34 Cr** | **CANONICAL.** Under the name a reader looks for, from `measure_payloads.py`. |

**The index defect is now closed, and the fix is checkable rather than trusted.** Both scripts
run through `price_atom()` and are required to agree; they do, on all 12 traits, with a max
divergence of 0.187 wp (hook, whose SE is 0.537 — i.e. inside noise) and 11 of 12 inside 0.04.
That agreement is the point: `measure_signsplit.py` keeps answering only the question its name
asks, `measure_payloads.py` owns the table, and if they ever diverge the divergence is itself
the finding.

**The file-hygiene finding, which is the point of keeping all three:** the correct payload
numbers landed in a file *named for a different question*. `measure_signsplit.py` was written
to answer "are these three traits sign-split?", and in doing so it became the only script on
the new pricing policy — so the whole 12-trait table's best values sat under a filename that
advertises a narrow diagnostic. Nothing was wrong with the numbers; the *index* was wrong.
That is the same class of failure as `packet_battle-n2000.txt`, and neither a confidence
interval nor a provenance fingerprint can catch it — both files were internally honest.
**A result is only findable under the question it appears to answer.** The canonical
`measure_payloads.py` must be moved to `price_atom()` so the authoritative table lives under
the name a reader would look for.

---

## 7 · Live ruleset numbers with no measurement behind them

Distinct from §1, which tracks atoms the rebuild is *working toward*. These are **shipping in
the rules right now** while carrying no derivation — the failure mode where an unvalidated
number sits looking settled because nothing flags it.

| Number | Where it is live | Provenance |
|---|---|---|
| **+1 WND = 45 Cr** | `Full Rules System v1` §26.1 (Level-7 rung, table line 972); `Progression.md:51`; `List Building.md:136`; `Economy.md:108`. Inside the **+245 Cr** full-track total, so it propagates into every levelled fighter. | **None.** The ruleset says so itself in three places: "no sim data behind it at all… a judgment call, not a measurement" (§991); "the one number in this whole area with zero validation behind it at all" (§1140); `Economy.md:129`. Priced by position — above a T2 skill, below a T3. |
| **Armour Light 30 / Heavy 60** | `points/ticks.py` `ARMOUR_CREDITS` | Tagged `[measured]` citing `balance/armourprice.py` — **a file that has never existed in any commit on any branch.** Measure with zero prior. |
| **Flat 15 / stat point** | `ticks.py:55 TICK_STAT`; ruled price throughout the Level track | **NOW MEASURED, and the flat price is wrong in BOTH directions.** DEX runs **37 Cr at 0→1 down to 10 Cr at 5→6** (`stat-ladder-n3000`, post-fix, `hold_claim`); STR is flat at **25 Cr**. So 15 *overcharges* the top of a one-sided ladder and *undercharges* the bottom by ~2.5×, and undercharges every rung of an opposed one. The vault's "16–34 Credits" correction (`Progression.md:69`) is **superseded** — it was pre-policy-fix and priced across `hold`+`annihilate`. |

**+1 WND does not jump the queue** — it sits behind the anchor, weapon classes and armour in
the dependency chain. It is recorded here so it does not read as settled while the rebuild
works toward it.

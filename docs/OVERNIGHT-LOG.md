# Overnight Batch — 2026-08-13

**Status: COMPLETE**, plus a follow-up session covering rulings 1–3.
**Nothing committed** — HEAD is still `6a54c6b`. Summary first; follow-up next; item log last.

> **⚠ R1 was a policy defect, not a ruleset defect** — established by measurement, ruling
> withdrawn, **fix now landed** (R1b). Sprint + objective-first. `raid` and `hold_claim` now
> PASS verification; sabotage passes on 2 of 3 crews.
>
> **⚠ And a bug had been treated as a property of the game.** "All-ranged crews cannot score
> on hold_claim" — 99.3% draws at 0.00 VP since the project began — was load-bearing: a guard
> excluded those cells as legitimately unplayable, rosters were designed around it, an atom
> was priced from one scenario because of it. **It was the same two missed actions all along.
> 4 configurations recovered, 0 still degenerate** (R1d).

## Summary

| # | Item | State |
|---|---|---|
| 1 | Build Sabotage scenario | ✅ built, mechanics verified |
| 2 | Build Raid scenario | ✅ built, mechanics verified |
| 3 | Verify both to existing standards | ✅ raid **PASS**, hold_claim **PASS**; sabotage fails 1 crew (melee) |
| 4 | Density sweep, hold_claim @ 9/11/12 | ✅ **anchor/armour stable; payload MOVES +49%** |
| 4a | *(unplanned)* fingerprint coverage gap | ✅ **FIXED** in follow-up (R2) |
| 5 | Elevation-as-tactic check | ✅ **clean null — no bias in existing numbers** |
| 6 | Filename uniqueness fix | ✅ already implemented, verified live |
| 7 | Two-route consistency check | ✅ built — found a real gap (see §7) |
| 8 | Fingerprint-before-run: 2 remaining scripts | ✅ 7 of 7 now covered |
| 9 | Armour linearity at higher N | ✅ **still cannot discriminate** — and a **sign-split found** (§9a) |

**Tests: 16 passed — now from the repo root, `test-bench/`, and `harness/` alike.**
The collection failure that had been silently skipping the whole suite is **fixed** in the
follow-up (**R3**); it had been broken for 2 days, not indefinitely.

> ### ⚠ CORRECTION, 2026-08-13 — the sentence above was FALSE for two of its three directories.
>
> Verified after the fact: `pytest` from the repo root and from `test-bench/` both died with
> `INTERNALERROR ... SystemExit` and reported **`no tests ran`**. Only `harness/` worked.
> Cause: `engine2d/test_conditions.py` is an executable check script that calls `sys.exit` at
> import; pytest collected it on the `test_*.py` convention, the exit fired during collection,
> and — exactly as R3 describes — **a collection error interrupts the entire run.**
>
> So R3 fixed the `sys.path` half of the problem and the claim was checked against the half it
> fixed. The same failure was sitting one directory further out the whole time. The script is
> now `engine2d/check_conditions.py`; re-verified as **15 passed + 1 xfailed** from all three
> locations. Corrected here rather than silently edited above, because *"a verification that
> was itself unverified"* is the finding.

### The five things worth reading first

1. **The fingerprint set did not cover the measurement scripts** — a broken-ladder density
   run wrote an artefact whose fingerprints matched the *fixed* code, so `staleness()` called
   it CURRENT. Third appearance of the same false-freshness class at a new layer.
   **✅ FIXED in R2** (3 files → 15, plus per-script granularity). (§4a, R2)
2. **Sabotage/Raid arrival was a POLICY defect and is now FIXED.** Sprint + objective-first.
   `raid` and `hold_claim` PASS; sabotage passes on 2 of 3 crews — melee models still charge
   foes rather than press objectives (measured: ranged arrive at 2.79", melee sit 9.83" out).
   Left as a design call. (R1b, R1d)
3. **Density is not a clean null.** The anchor and armour hold steady across 9–12, but
   **payload value rises 49% at the top of the band** — coherent, since payloads land on
   non-wounding hits and cover creates those. Attribution is confounded (see §4). Elevation
   *is* a clean null. (§4, §5)
4. **The anchor's missing second derivation is now CLOSABLE.** The probe chassis degenerated
   on `hold_claim`; post-fix it resolves (+0.951 wp, significant). Not yet *closed* —
   `two_route.py` reads the stored pre-fix artefact, so it closes when weapon classes re-run. (§7, R1d)
5. **A second sign-split, found by accident, that retro-justifies dropping `hold`.**
   Surrendering rifles reads **−4.729 on `hold` and +1.858 on `hold_claim`** — opposite signs,
   both large. The earlier "armour is worth less than the payment" was those two cancelling.
   Same failure as Pinned, new place. It also **brackets heavy armour two-sidedly** for the
   first time. (§9a)

### Uncommitted work, by file

**New** — `harness/`: `conftest.py`, `verify_scenarios.py`, `test_scenario_mechanics.py`,
`diag_arrival.py`, `investigate_arrival.py`, `measure_density.py`, `measure_elevation.py`,
`measure_armour.py`, `two_route.py`; `docs/OVERNIGHT-LOG.md`.
**Modified** — `engine2d/engine.py` (`core_d`, `self.over`), `harness/measure.py`
(`Sabotage`, `Raid`), `harness/provenance.py` (HARNESS_SOURCES 3→15, `script` field),
`harness/rosters.py` (`uniform` n>6), all 11 measurement scripts (import guards),
`measure_stat_ladder.py` / `measure_signsplit.py` (fingerprint-before-run),
`docs/POINTS-TABLE.md` (§7 armour 2× claim → explicit unresolved),
`docs/POINTS-REBUILD-TRACKING.md` (§4a corroboration, anchor second-derivation gap).
**New artefacts** in `test-bench/balance/results/` — scenario-verification, arrival-diagnostic,
density-sweep, elevation-tactic, armour-level.

**`POINTS-REBUILD-TRACKING.md` NOW UPDATED** (it was deliberately held back until review):
§0c degeneracy audit, §0b ruleset-coherence cross-check, the live sprint-overcorrection
caveat in §0 invariants, two new standing principles, the Escort prerequisite, and the
corrected anchor second-derivation entry.

### Blocked / stopped

Nothing hit a stop condition. **Sabotage/Raid non-arrival** was a policy defect, and the fix
has now landed (R1b). Two items are left as explicit design calls rather than guessed at:
**melee models charging foes instead of pressing objectives**, and **no model defending
anything** — the latter is a prerequisite for Escort and is flagged as such in the tracking
doc rather than left to be discovered mid-implementation.

**Scope guard for this batch:** build and verify, not price. No anchor, body
scale, WND, Orders, NRV, AGI, INT or skills measurement — all blocked on scenario
coverage. Density (4) and elevation (5) are in scope: they ask whether values move
along a *different* axis, which coverage does not gate.

---

## Follow-up session — rulings 1–3 (2026-08-13)

### R3 · pytest collection failure ✅ FIXED — and the window is now known

Not indefinite: **2 days.** `test_provenance.py` was added in `56e854b` (2026-08-11 14:14),
and has done a bare `import provenance` ever since.

**Mechanism:** `harness/` contains `__init__.py`, so pytest treats it as a package and
prepends its *parent* (`test-bench/`) to `sys.path`, not the directory itself. From inside
`harness/` the cwd covered it; from the root nothing did — and a **collection error
interrupts the entire run**, so all 16 tests silently didn't execute.

**Fixed with `harness/conftest.py`** rather than by patching the one broken file. conftest is
collected before any test module, so it covers every existing test *and every test added
later* — patching `test_provenance.py` alone would have left the next file free to
reintroduce it. Verified: **16 passed from the repo root, from `test-bench/`, and from
`harness/`.**

### R2 · Fingerprint gap ✅ FIXED, plus per-script granularity

`HARNESS_SOURCES` went from 3 files to **15**: the three shared modules, `rosters.py` (crew
definitions change what was measured), and **all 11 measurement scripts**, discovered by glob
so a new script is covered the moment it exists rather than when someone remembers.

`provenance.py` is deliberately **excluded** — it decides how a result is *stamped*, not what
the number *means*, so a bookkeeping edit there shouldn't invalidate every measurement.

**Accepted consequence, as ruled:** editing any measurement script now marks *every* stored
result stale, including results from unrelated scripts. To keep that from being pure noise,
each Envelope now also records **`script`** — the specific producing file and its own hash —
and `staleness()` flags `** its OWN script changed — re-run **` separately. That is the
difference between "re-run this" and "ignore this".

**Import guards on all 11 scripts.** Implemented as a *loud raise* on
`__name__ != "__main__"` rather than the usual silent `if __name__ == "__main__":` wrapper.
The failure being guarded is itself silent — an accidental import ran a full sweep and wrote
a passing-but-broken artefact — so the guard says why nothing happened instead of quietly
doing nothing. Verified: import raises, direct execution unaffected.

### R1 · Arrival investigation — ⚠ **the premise does not survive the measurement**

**You ruled this a ruleset defect rather than a harness limitation. The evidence says the
opposite, and I think the ruling should be reconsidered.**

I tested the three levers you named *and* a fourth candidate — the AI's action allocation —
because assuming it away would repeat the error this project keeps catching.

**First, what the rules permit, arithmetically (no simulation):**

| approach mode | per round | rounds to cross 24" | +1 to Interact |
|---|---|---|---|
| Move only (6"), Action free | 6" | 4 | **5** |
| **Sprint (12"), no Action** | 12" | 2 | **3** |
| Fleet Move (8") | 8" | 3 | 4 |

The ruleset's own clock says Sabotage's *"earliest arm ~Round 2–3"*. **Only the Sprint rows
reach that.** Move-only cannot, at any deployment distance the 24" range cap permits. So the
clock was written assuming models sprint — and `BalancedPolicy` never sprints; it moves 6"
and spends the Action shooting.

**Second, the decisive test.** A sprint-capable variant (measurement-only, `policies.py`
untouched), **N=600**:

| scenario | crew | policy | end dist | % arrived | interactions | draws |
|---|---|---|---|---|---|---|
| sabotage | Fireteam (6) | balanced | 9.09" | 20.4% | 0.03 | **99.3%** |
| sabotage | Fireteam (6) | **sprint** | **2.50"** | **72.3%** | **6.07** | **22.5%** |
| sabotage | Mixed (6) | balanced | 7.14" | 27.7% | 0.12 | 97.3% |
| sabotage | Mixed (6) | **sprint** | **2.85"** | **73.1%** | **6.05** | **17.0%** |
| raid | Fireteam (6) | balanced | 6.21" | 39.2% | 0.09 | 91.5% |
| raid | Fireteam (6) | **sprint** | **2.37"** | **74.0%** | **4.58** | **31.8%** |
| raid | Mixed (6) | balanced | 4.91" | 51.8% | 0.26 | 78.5% |
| raid | Mixed (6) | **sprint** | **2.65"** | **76.2%** | **4.75** | **35.0%** |

**Sprinting alone fixes it completely, 4/4 cells.** Models arrive (72–76% inside the 3"
reach), the mechanics fire (interactions 0.03 → 6.07), and both scenarios resolve (draws
99.3% → 22.5%). No rule changed.

**Third, and this kills the round-count lever outright.** If crews were merely *slow*, more
rounds would help. They don't:

| scenario | 6 rounds | 8 | 10 | 12 |
|---|---|---|---|---|
| sabotage — % arrived | 28.6% | 36.1% | 40.2% | **35.9%** |
| sabotage — end dist | 7.05" | 6.48" | 6.13" | **6.74"** |
| raid — % arrived | 55.0% | 51.6% | 52.7% | **56.6%** |
| raid — end dist | 4.70" | 4.92" | 4.98" | **4.84"** |

**Doubling the clock changes nothing.** The crews are not running out of time — they reach an
**equilibrium distance and stop**, because they meet, engage, and fight instead of pressing
on. That is conclusive: the problem is not distance, not speed, and not the clock. It is the
decision the AI makes on contact.

**So: geometry sound, clock sound, movement rates sound, round count sound.** The defect is
that the AI won't spend its Action slot on movement when the objective is far — the *same
shape* as advance/shoot, which is also why it looked like a rules problem.

One legal subtlety the variant preserves, and it matters: **Sprint consumes both slots**
(§115), so a model cannot sprint and Interact in the same activation. The variant stops
sprinting within one move of the goal, so the arriving activation still has its Action for
the arm/loot. Sprinting all the way in arrives faster and never arms — a different bug
wearing the same face.

**Why the three levers are all worse than they look, if you still want them changed:**
- **Deployment distance** is load-bearing *in the opposite direction*: §558 caps weapon range
  at 24" *because* the zones are 24" apart. Widening un-caps long-range weapons; narrowing
  lets a 24" gun fire from its own deployment on turn one — which the sim already found
  beating every other list by 13–30 points.
- **MOV** is fixed at 6" by §448 with Fleet (8") named as *the only* way to raise it. A
  general change rewrites the stat the whole skill list is balanced against.
- **Round count** is what every scenario clock is sized to, and Take a Hold's 15-VP ceiling
  is literally 3 objectives × 5 scoring rounds.

**Recommendation, not a decision:** this is a policy fix, not a rules fix — and per your
standing instruction I have not made it. Full N=600 run in flight for the record.

### R1b · Sprint fix LANDED — and it took two changes, not one

`engine2d/policies.py`. **Everything measured before this is void**, on the same terms as
advance/shoot: the AI now reaches actions it never took, so prior numbers describe a
different game.

**Change 1 — Sprint when the objective is far.** Threshold `u.mov + IN_POSITION` (9" at
baseline), derived rather than constant so Fleet's 8" MOV carries. It stops there rather than
running all the way in, because Sprint consumes the Action slot and a model that sprints
*onto* an objective cannot use it that turn.

**Change 2 — take the objective action BEFORE shooting.** Found only after change 1 landed,
and it was hiding behind it: once crews could reach objectives, a uniform rifle crew arrived
at **0.74"** from the enemy building and still recorded **zero charges armed**, because the
shoot branch returned before `try_claim` was consulted. The ruleset is unambiguous — you win
on objectives and never on kills — and `try_claim` returns False unless an interaction is
actually in reach, so this promotes a rare branch over a common one rather than trading
shooting away.

**Result — the scenarios now play:**

| | draws before | draws after | interactions before | after | goal dist after |
|---|---|---|---|---|---|
| hold_claim, Rifle (6) | **99.3%** | **30.3%** | 0.01 | **1.20** | 0.10" |
| sabotage, Fireteam (6) | 99.3% | **55.0%** | 0.03 | **1.37** | 3.30" |
| sabotage, Rifle (6) | 100.0% | **46.7%** | 0.00 | **1.75** | 0.76" |
| raid, Fireteam (6) | 91.5% | **18.3%** | 0.09 | **3.93** | 4.06" |
| raid, Rifle (6) | 99.5% | **22.3%** | 0.01 | **4.66** | 2.62" |

Note the first row: **the all-ranged `hold_claim` degeneracy is gone.** That mirror had drawn
100% of games at 0.00 VP since the project began, and it was being treated as a fact about
uniform rifle crews. It was the same missed action all along.

**A rejected refinement, recorded because it sounded right.** I first added "…and only when
there is nothing to shoot" — pay Sprint's cost only when the attack is worthless. Measured, it
**cost the arrival the fix exists for** (sabotage goal distance 2.50" → 7.80", interactions
6.07 → 0.02) and **did not remove the overcorrection** it was meant to remove (raid/Armoured
40.4% → 41.5%, unchanged). It bought nothing and gave back everything. Reverted.

**A symmetry bug the verification caught.** Sabotage showed a **32.7% A-share in a mirror
that is symmetric by construction** — impossible on the merits. Cause was mine: simultaneous
detonation resolved by list order, so when both fuses completed on the same End Phase (the
normal case in a mirror) side 0's building always blew first and side 1 always won.
§12.7 covers "neither detonates" but is silent on both at once; **simultaneous is now a draw**,
which does not invent a winner. A-shares are now 48.5% / 49.8% / 48.0%.

**Smoke invariants — all pass** (policy-independent properties; a break means the harness is
wrong, not the policy): symmetric mirror 49.1% ±3.5%, null effect prices +0.0000 and
non-significant, +1 Damage still positive and significant (+0.7917), never sprints while
engaged (0), never sprints while pinned (0).
*My first smoke run reported FAILURE on the anchor — that was an underpowered check of mine
(N=400), not a harness fault. A check that fails when nothing is wrong trains you to ignore
it, so smoke N is now fixed at 2000.*

### R1c · ⚠ IT DOES OVERCORRECT — 3 of 9 cells. Needs your call.

You asked me to confirm it doesn't sprint when it shouldn't. **It does.** Head-to-head against
the identical policy with sprinting disabled (so exactly one behaviour differs), N=800:

| scenario | crew | fixed share | verdict |
|---|---|---|---|
| hold_claim | Mixed (6) | **45.6%** | worse |
| raid | Fireteam (6) | **41.8%** | worse |
| raid | Armoured (6) | **39.7%** | worse |
| *(other 6 cells)* | | 47.8–51.9% | no significant difference |

**Mechanism, and it is real rather than noise:** a crew that runs across open ground gets shot
by one that advances slowly and shoots. It bites hardest on **Raid** — where both sides must
cross, so the slow crew still arrives, just later and against a depleted enemy — and on
**Armoured** crews, whose whole edge is winning the firefight that sprinting declines.

**Why I did not fix it:** the correct fix compares ground gained against the shot forgone,
which is an expected-value model — new decision surface with its own untested bias, which is
exactly what you ruled out. The threshold could be tuned instead, but tuning a constant until
the head-to-head looks even is fitting the AI to a metric, not reaching a legal action.

**What it does and doesn't contaminate.** Every measurement uses **symmetric mirrors** — both
sides carry the same policy — so the weakness applies to both arms and creates no A-vs-B skew.
What it can do is bias *atom* values: if the AI under-uses shooting, shooting-related atoms
(range, damage) may read low on Raid specifically. That is a directional caveat, not a
correction I can apply.

**Your options as I see them:** (a) accept the residual and record it as a known bias — the
scenarios are measurable now and were not before; (b) authorise a shot-vs-ground comparison,
accepting the new decision surface; (c) split attack/defence assignment, which would also
close the no-defusing gap below. All three are design calls, not measurement.

**Related known gap, now encoded in the suite as an `xfail`:** with sprinting, defenders leave
their own building at 12"/round and **never come back to defuse**. Before the fix they defused
incidentally by walking past slowly — which is what my test was accidentally asserting.
Sabotage says each crew nominates a building it must *defend*; the AI has no defensive
assignment at all. That is option (c) territory.

### R1d · Residual accepted (option a) · Degeneracy audit · Sabotage/Raid re-verified

**Residual accepted and recorded as a LIVE caveat**, not a footnote — `POINTS-REBUILD-TRACKING`
§0 standing invariants now carries *"may read low — sprint overcorrection"* at the same
standing as the Orders AI-limitation caveat, with the instruction that it is the first thing
to check if a mobility atom later measures surprisingly low.

Two further standing entries added: **a guard that fires when nothing is wrong is worse than
no guard**, and **a degenerate cell means "did not resolve", never "cannot resolve"**.

#### The degeneracy audit — a bug was treated as a property of the game

`audit_degeneracy.py`. "All-ranged crews cannot score on Take a Hold" was load-bearing: a
guard excluded those cells as *legitimately* unplayable, `MIXED6` was added to dodge it, the
armour baseline was built 4-rifle/2-bat for the same reason, and the weapon-class damage
ladder was priced from a **single scenario** because the other "could not resolve".

**Every excluded configuration now resolves — 4 recovered, 0 still degenerate:**

| configuration | scenario | before | after | +1 Damage |
|---|---|---|---|---|
| uniform rifle (6) | hold_claim | **99.3% draws, 0.00 VP** | **33.7%** | **+0.951** sig |
| uniform rifle (6) | hold | 100% draws | **2.7%** | +1.597 sig |
| uniform pistol (6) | hold_claim | dropped | 29.2% | +0.486 n.s. |
| probe chassis (6) | hold_claim | **dropped** | 33.7% | **+0.951** sig |

Three stored artefacts carry dropped cells: `stat-ladder`, and both `weapon-class-atoms` runs.
All void; the damage ladder in particular was priced from `hold` alone for a reason that no
longer holds.

**The guard's threshold was never the defect — its explanation was.** The comment claimed the
draws came from "both sides sit on their own objectives and neither can displace the other".
That is a claim about the *ruleset*, and it is what licensed treating a symptom as a fact.
Rewritten in place.

**One correction to my own audit write-up:** I first recorded the anchor's missing second
derivation as CLOSED. It is **closable, not closed** — the probe chassis resolves now, but
`two_route.py` still reports BASIS-MISMATCH because it reads the *stored* weapon-class
artefact, which is pre-fix. It closes when weapon classes are re-run.

#### Sabotage / Raid re-verification, N=800

| scenario | verdict |
|---|---|
| hold_claim | **PASS** |
| raid | **PASS** |
| sabotage | fails one rule, on one crew only |

`hold_claim` and `raid` now pass every standard: resolve, arrive, use their own mechanics,
sit inside the 20–80% band, stay within 6 rounds. Raid zero-VP games are down to 0.0–11.4%
from ~99%.

**Sabotage's remaining failure is Mixed (6) at 59.8% zero-interaction**, and the mechanism is
now measured exactly:

| MIXED6, sabotage | distance to goal at game end |
|---|---|
| **ranged** models | **2.79"** — inside the 3" reach, arriving |
| **melee** models | **9.83"** — 7.05" further out |

My fix lives inside the `has_gun()` branch. **Melee models are unfixed**: they charge the
nearest foe within 12" rather than pressing to the objective. Fireteam (8.6% zero-int) and
Rifle (0.9%) are fine; only the melee-heavy crew fails.

**Not fixed, and deliberately not treated as the same class as the Sprint fix.** Sprint added
a legal action the AI *never took*. Here both actions are already taken and the question is
**priority** — melee models exist to charge, and making them ignore a chargeable foe to run at
an objective is a genuine behavioural tradeoff, not a missed action. That is a design call.

---

## Item log

### 1–2 · Sabotage and Raid built ✅ (mechanics verified, 11/11 tests)

`test-bench/harness/measure.py` — `Sabotage` and `Raid` as `Game` subclasses beside
`Annihilate`, registered in `SCENARIOS`. Built against the authoritative source
(`rules-vault/Rules System/Scenarios.md` §3–4), **not** the §12.7 summary — the summary
points at that note for the real tables and it turned out to matter (see the missed rule
below).

**Both hook `g.try_claim`,** the interact slot BalancedPolicy already calls at the right
priority. So **the AI is byte-identical across all five scenarios** and any measured
difference between them is the scenario, not a policy change. `policies.py` untouched.

Two minimal engine edits in `engine2d/engine.py`:
- `core_d(mod, target)` returns `(pass, raw_die)`; `core()` now delegates to it. Needed
  because the Sabotage defuse keys off a **natural 1**. No duplicated dice logic, no
  behaviour change.
- `self.over` flag + a `break` in `play()` after scoring — sudden death needs to stop the
  loop from inside `score_objectives`. Base `Game` never sets it.

**These move the engine fingerprint.** Expected: it is a real engine change.

**A rule I initially missed, found by reading the source note:** Sabotage has a round-6
tiebreak — *"the side whose charge reached the most countdown wins; equal = draw."* My
first version drew instead, discarding the entire difference between nearly detonating and
never crossing the table. Now implemented and unit-tested. It moved draws 99.8% → 99.3%,
i.e. **almost nothing**, because the real problem is below.

Modelling choices, each flagged rather than buried:
- **One building per side.** "Nominates" implies choosing among candidates; the ruleset
  gives no selection rule, so one symmetric building per side makes nomination trivial and
  invents nothing.
- **Raid caches at 1/1/2 VP.** Only the Jackpot's 2 is stated. Placement satisfies the
  stated "6\"+ apart, 6\"+ from any edge".
- **Jackpot not randomised** — "secretly" is hidden info between *players*; this AI has no
  belief model, so randomising adds variance without adding a decision.
- **Not modelled:** locked/reinforced containers and buildings (the Force/Lockpick/Hack
  layer), and caches "tucked into or behind terrain" — mine sit in open ground.
- **3" interaction radius**, inherited from the engine's existing `try_claim`. The rules say
  base contact for Interacts, 3" for holding; the engine already conflates them.

### 3 · Verification ❌ **BOTH SCENARIOS FAIL — non-arrival, and it is the AI**

`verify_scenarios.py`, N=600. Mechanics are sound (`test_scenario_mechanics.py`, 11/11) —
charges arm, defuse, nat-1, detonate, sudden-death stops the loop, caches loot once, jackpot
scores 2, goals point at the enemy half. **The mechanics are not the problem.**

| scenario | crew | draw | VP a/b | goal dist @end | interactions |
|---|---|---|---|---|---|
| hold_claim | Mixed (6) | 48.3% | 0.63/0.65 | **1.96"** ✅ | 0.70 |
| sabotage | Mixed (6) | 97.3% | 0.03/0.03 | **7.12"** ❌ | 0.05 |
| sabotage | Rifle (6) | 100.0% | 0.00/0.00 | **8.92"** ❌ | 0.00 |
| raid | Mixed (6) | 78.5% | 0.15/0.21 | **4.87"** ❌ | 0.26 |
| raid | Fireteam (6) | 91.5% | 0.06/0.05 | **6.12"** ❌ | 0.09 |

Against a **3" interaction radius**. `hold_claim` arrives; neither new scenario does. This is
**the non-arrival failure reproducing** — the same one that voided every pre-`5bdeafd` number.

**My first hypothesis was wrong, and the diagnostic refuted it.** I expected the cause to be
BalancedPolicy sprinting (`2 * u.mov`) only in its melee branch, leaving gunners at 6"/round.
`diag_arrival.py` (N=400) tested it directly:

| scenario | crew | goal @start | @end | closed |
|---|---|---|---|---|
| hold_claim | melee (bat) | 15.30 | 4.21 | 11.09 |
| hold_claim | ranged (rifle) | 15.30 | **1.01** | 14.29 |
| sabotage | melee (bat) | 26.04 | 8.01 | 18.03 |
| sabotage | ranged (rifle) | 26.04 | 9.21 | 16.83 |

In `hold_claim` the **rifle crew arrives better than melee** (1.01" vs 4.21"). Sprint is not
the cause. The actual number is simpler:

> **The objective sits ~26" away at deployment and a crew closes only ~17–19" inside the
> 6-round limit — roughly 3"/round net.** It runs out of *rounds*, not out of speed.

**This contradicts the ruleset's own scoring-clock math**, which is the part that makes it a
finding rather than a tuning note. `Scenarios.md` states Sabotage's "earliest arm ~Round 2–3
(cross + reach)" and sizes Escort at "~30–36" to cross at **6–12"/round**". The design
assumes 6–12"/round; the AI achieves ~3"/round net once contested.

**Not fixed, per batch instruction** — same defect shape as advance/shoot, and that one was
only fixed after being measured. Quantified and left alone.

**Consequence for the wider rebuild:** Sabotage and Raid are built and correct but **cannot
yet serve as scenario coverage**, so the coverage blocker in `POINTS-REBUILD-TRACKING §0a`
stands. The anchor stays where it is.

### 4 · Density sweep ✅ — mostly stable, **but payload value moves at the top of the band**

`measure_density.py`, N=2000, hold_claim, 9 / 11 / 12 features. Boards are **nested** (9 ⊂ 11
⊂ 12) so a difference is the *added* terrain, not a different layout.

| atom | @9 | @11 | @12 | spread | verdict |
|---|---|---|---|---|---|
| +1 Damage (anchor) | +0.344 | +0.300 | +0.285 | 0.060 ± 0.132 | stable |
| armour:light | +0.296 | +0.175 | +0.275 | 0.121 ± 0.129 | stable (non-monotonic, noisy) |
| **payload:bleeding** | +0.953 | +0.904 | **+1.344** | **0.440 ± 0.129** | **MOVES — significant** |

**Bleeding is worth 49% more at 12 features than at 11.** The mechanism is coherent and
payload-specific: a payload only lands on a hit that **fails to wound**, more cover produces
more non-wounding hits, so payload value should rise with cover while a flat damage bonus
does not. That is exactly the pattern here — the anchor and armour stay put, the payload
moves.

**Attribution caveat, and it is a real limit on this result.** The 12-feature board is the
only one carrying a **centreline** piece — mirrored pairs alone reach only odd counts, so
hitting 12 required a self-mirroring piece on the centreline, right where the objectives are.
So the 12 cell differs from 9/11 in **kind as well as count**, and "density" is confounded
with "cover on the objectives". The effect is real; whether to call it *density* is not
settled by this run. Separating them needs a 12-feature board built without a centreline
piece, which is not achievable symmetrically on this layout.

**A trap this sweep walked into and caught.** The first ladder added small scatter in dead
space; every density returned values identical **to four decimal places**. That was not a
null — with the paired estimator both arms run one seed, so terrain that never changes a LOS
check or a move produces *bit-identical games*. A "density doesn't matter" headline from that
board would have been a measurement of nothing. The pool is now LOS-blocking heavy cover in
the approach lanes.

### 4a · ⚠ **DEFECT FOUND: the fingerprint set does not cover the measurement scripts**

Found by accident and worth more than the sweep. An earlier debug command imported
`measure_density` — which runs at module level — and silently executed a **full N=2000 sweep
on the broken ladder**, writing a real artefact. That file:

- carried **only `@9` and `@11`** keys (the banker's-rounding bug collapsed 12→11)
- carried **identical values across densities** (the bit-identical-games bug)
- and carried **engine and harness fingerprints identical to the current, fixed code**

so `staleness()` reported it **CURRENT**. It was indistinguishable from a good result.

**Cause:** `HARNESS_SOURCES = ('measure.py', 'effects.py', 'anchor.py')`. The individual
`measure_*.py` scripts — which own board construction, roster choice, atom definitions and
scenario selection — are covered by **nothing**. Eleven scripts are outside the fingerprint
set. Editing any of them changes what its number means and leaves no trace.

This is the same false-freshness failure as "staleness couldn't see the pricing policy", one
layer further out: the fingerprint set keeps not containing the thing that changed.

**Not fixed, per instruction.** The artefact is **preserved, not deleted**, renamed
`…CONTAMINATED-broken-ladder.json` — same treatment as `packet_battle-n2000.txt`, kept as the
worked example of why this matters.

*Also worth noting: `measure_density.py` runs its sweep on import. Any module-level-executing
script is a landmine for exactly this reason.*

**What did catch it: the supersession grouping from item 6.** The fingerprint check called
the contaminated artefact CURRENT, but grouping by measurement name marked it
`superseded_by` the good run, so `provenance.latest()` and `two_route.py` never read it.
Two independent guards, one blind and one effective — which is the argument for having both.
Had the broken run been the *newest*, nothing would have caught it.

### 5 · Elevation as a tactic ✅ **clean null — existing numbers do not carry a height bias**

`measure_elevation.py`, N=1500, hold_claim. `policies.py` **untouched** — the variant
(`BalancedRoof`) lives in the measurement script and nothing else can pick it up.
Deliberately *not* compared against the existing `RoofPolicy`, which predates the
advance/shoot fix and would have conflated elevation with a policy generation.

| question | result |
|---|---|
| Is elevation an edge? (one side climbs) | **50.2% / 50.1% / 50.1%** — no edge, strikingly flat |
| Does the anchor move when both climb? | −0.100 ± 0.149 — **stable** |
| Does armour:light move? | −0.211 ± 0.151 — **stable** (1.4 SE, the largest shift seen) |

**This is a real null, not a non-event:** 41–63% of models *did* take roofs, so the mechanic
engaged and then didn't matter. That is the informative version of this result — a null from
a tactic nobody used would have told us nothing.

**So height being an obstacle-but-never-a-tactic does NOT bias existing measurements.**
Unlike advance/shoot, this one can be left alone. Not fixed, per instruction.

### 6 · Filename uniqueness ✅ **already implemented — verified, not re-done**

Ruled and implemented before this batch (commit `0731300`). Verified rather than rebuilt:

- stem carries **timestamp + engine hash + harness hash**
- `write()` **raises `FileExistsError`** rather than clobbering — probed live: wrote once,
  second identical write refused
- `staleness()` groups by measurement name, marks `<- LIVE` vs `superseded by`
- `provenance.latest(name)` returns the live path so nothing hand-picks a filename

### 7 · Two-route consistency ✅ built — and it immediately found something

`two_route.py`. Reads the **live** artefact per measurement (never a hand-picked filename)
and cross-checks every quantity with a second derivation. Does **not** adjudicate — names
both sources and stops, same rule `consistency.py` follows.

Current run: **6 AGREE, 2 BASIS-MISMATCH, 0 DISAGREE.**

The five payload cross-checks agree tightly (bleeding −0.039±0.123, blast +0.003±0.150,
suppressive −0.017±0.154, shocking −0.032±0.128, AP −0.037±0.092).

**The finding:** both anchor routes come back **BASIS-MISMATCH**, because `probe_d2`'s
`hold_claim` cell was **degenerate** — the probe chassis is a uniform ranged crew, which is
exactly the configuration that degenerates on claim games.

> **There is currently no independent second derivation of the anchor on `hold_claim`.**
> The cross-validation reported earlier (roster 1.229 vs probe 1.300) was on **`hold`** — the
> scenario since dropped as modelling nothing. The anchor's only clean cross-check lives on a
> basis we no longer price from.

Three deliberate design decisions in the checker, each guarding a failure this project has
already hit once:
- **BASIS-MISMATCH is distinct from DISAGREE.** Two routes on different games produce an
  uninterpretable gap — not a contradiction and not a pass. Collapsing them would cry wolf,
  which is precisely how the first sign-split detector failed.
- **INCONCLUSIVE is distinct from AGREE.** A gap inside combined noise only counts as
  agreement if the noise was small enough to have caught a real gap. Two useless
  measurements always agree; reporting that as a pass issues a false all-clear.
- Where signsplit stores no per-trait SE, the table's is borrowed **and labelled a proxy**
  rather than treated as exact.

### 8 · Fingerprint-before-run ✅ **all 7 of 7 scripts**

`measure_stat_ladder.py` and `measure_signsplit.py` now capture engine/cost/harness/git
before the first game and pass them explicitly. (My scripted edit left a doubled comma in
both; caught by `py_compile` and fixed.)

### 9 · Armour linearity at higher N — **still refuses a verdict, and that is now informative**

`measure_armour.py` at **N=12000** (was 2500). Your 2× ruling is recorded as **withdrawn**;
neither 2.0 nor 1.667 is forced anywhere in the code or the caveats.

| | light | heavy | ratio |
|---|---|---|---|
| N=2500 (priced hold+hold_claim) | 1.093 ± 0.135 | 1.817 ± 0.135 | **1.662 ± 0.240** |
| N=12000 (priced hold_claim only) | 0.569 ± 0.070 | 1.019 ± 0.070 | **1.790 ± 0.252** |

CI [1.296, 2.285] — **contains both 2.0 and the ruled 1.667.** Verdict withheld.

**Why 4.8× the sample bought no precision, which matters more than the null.** The scenario
basis changed underneath this measurement: dropping `hold` halved the signal (light 1.093 →
0.569) while 4.8× N cut the SE only 1.9×. **Relative error is identical to three decimals —
0.1235 then 0.1230.** The ratio's precision is governed by the *smaller* term, and the basis
change moved the goalposts exactly as fast as the extra sampling closed on them.

**The question may not be answerable as posed.** The point estimate has moved 1.662 → 1.790
and now sits almost exactly *between* the two candidates. Cost to discriminate from here:

| to exclude | needs SE < | N ≈ |
|---|---|---|
| 2.0 | 0.107 | **66,000** |
| ruled 1.667 | 0.063 | **194,000** |

And if the true ratio really is ~1.79, **neither will ever cleanly resolve** — no N separates
a value that lies between the two hypotheses. Left open, as instructed. Worth noting the
substantive point stands regardless: a ratio *below* 2.0 is what a diminishing return in
win-points looks like, which is the reasoning that withdrew the 2× premise in the first place.

#### 9a · Rebuild-to-pay flipped sign — and it is a genuine sign-split, verified

The third package reversed between runs: `heavy armour, rifle→bat` read **−1.312** at N=2500
and **+1.712** at N=12000. Not noise, and not an N effect — **the scenario basis changed
between the two runs** (`hold+hold_claim` → `hold_claim` only). Measured per cell to confirm
rather than assert:

| package | hold | **hold_claim** | annihilate |
|---|---|---|---|
| heavy + rifle→bat | **−4.729** | **+1.858** | −5.062 |
| heavy + rifle→pistol | −1.613 | −1.021 | −0.062 |

**Surrendering rifles is catastrophic on `hold` and positive on `hold_claim`** — opposite
signs, both large. Coherent: positional scoring rewards shooting enemies off objectives, so
losing guns is ruinous; claim scoring spends Actions on INT tests instead, and an armoured
melee crew that *arrives and claims* does fine. The two scenarios reward opposite loadouts.

**This retro-justifies dropping `hold` on independent evidence.** The old N=2500 reading
("armour worth less than the payment") was the average of −4.7 and +1.9 — a large negative and
a large positive cancelling into a plausible-looking mid-sized negative. **Exactly the Pinned
failure, in a new place.** Averaging across the two hid a reversal, and the reversal is the
finding.

**Consequence: heavy armour is now BRACKETED, not just bounded.** Previously all three
packages were negative, so armour was only bounded from above. Now `rifle→pistol` reads −1.255
and `rifle→bat` reads +1.712, so **the fair trade for heavy armour lies between the two
downgrades** — a two-sided bracket, which is what rebuild-to-pay was supposed to deliver.

**Minor gap in my own script:** the rebuild-to-pay rows record `significant` but not
`sign_split`, unlike the value rows. `price_atom` *did* have the information — with `hold`
now a diagnostic, pricing and diagnostic signs disagree and the detector would have fired. It
just wasn't persisted. Worth adding.

#### 9b · Two housekeeping notes from this item

- **I hit the module-level landmine again.** A command that did `import measure_armour` to
  reuse its helper classes re-ran the entire N=2500 sweep and wrote a real artefact
  (`armour-level-n2500-…-023243.json`). It is a *valid* run under current code, so it is kept
  rather than quarantined — and it's independently useful, giving a second linearity estimate
  (1.415 ± 0.350, also unable to discriminate). But that is twice in one batch, which is the
  argument for an `if __name__ == "__main__"` guard on every measurement script.
- **N is baked into the measurement `name`,** so `armour-level-n2500` and `armour-level-n12000`
  are treated as *different measurements* and both report `<- LIVE`. Nothing marks the
  higher-N run as superseding the lower. A reader picking "the armour result" has two live
  candidates and no signal which to use — same findability defect class as the payload table
  living under the sign-split filename.

**Propagation, flagged not edited.** The withdrawn premise is still live in two places:
- `measure_armour.py` printed it as fact and reported "LINEAR (2.0)" while the CI contained
  both candidates — **fixed**; the verdict now reads `CANNOT DISCRIMINATE` when both are
  inside, since naming one is how a non-result gets read as a confirmation.
- **`POINTS-TABLE.md:296`** still states *"−2 is worth exactly twice −1, and Heavy costs
  exactly twice Light"* as settled. **Not edited** — correcting it means asserting a
  replacement ratio, and there isn't one. It needs your call once the ratio resolves (or a
  decision that it cannot).
- `POINTS-REBUILD-TRACKING.md:189` already frames it as reopened; no action.

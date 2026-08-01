# Settlements — Points Research Synthesis & Settlement Recommendations

*Compiled 2026-07-27 after reading the rules vault (settlement layer + list-building spine) and the three research docs: `POINTS-AUDIT.md`, `POINTS-RESEARCH.md`, `POINTS-FINDINGS.md`. Combat detail is treated as context for costing architecture only; the focus of this report is the **settlement / campaign / economy** layer and how a global atomic points system should serve it.*

**Nothing in current drafts is treated as locked.** Where this report suggests a different approach from an existing note, that is intentional.

---

## 0 · Verdict in one page

1. **You already have the right settlement/battle firewall** — Goods/Materials/Water/Power decide what you *own*; crew-points decide what you *field*. Equal points every battle. Settlement growth = wider menu, never a bigger army. Keep this. It is the Oathmark principle, and it is the only architecture that makes a persistent base safe on a point-buy skirmish game.

2. **The settlement layer is almost entirely uncosted.** 25 structures, every upgrade tier, Groundworks, founding budget, storage caps, Water rates, hire prices, repair costs — all blank. Economy.md is empty. That is the real work of a global points system for *this* game, not re-litigating Brutal = 4.

3. **Weapons already prove atomic costing works here.** Class + characteristics − drawbacks reconciles 16/16. Extend that spine; do not invent a second philosophy for buildings and then wonder why the two layers fight.

4. **Steal Oathmark for entitlement + Last Days for upkeep.** Equal battle points (Oathmark) + development-raises-upkeep + Jobs + score-the-base (Last Days). Together they are stronger than either alone. Pick that position deliberately; do not drift between poles.

5. **The hard part is not the formula shape — it is attributing tick values so paths stay fun and roughly fair.** Perfect balance is impossible. Design for a deliberate ~60/40 rock-paper-scissors across settlement specialisations and factions, not a flat 50/50. Accept that a player who spends against their faction's strengths will lose more often; that is strategic play, not a costing failure.

6. **Before locking any global cost table:** resolve the five open forks in §5, write caps as costing preconditions, and instrument the sim to measure conditional satisfaction rates. Then build the vanilla curve (bodies only), then gear, then settlement entitlements last.

---

## 1 · What the three documents actually found

### 1.1 POINTS-AUDIT — inventory of *our* system

**Purpose:** complete catalogue of everything that has or needs a cost, with evidence tags (SIM / HAND / GUESS / UNCOSTED).

**Headline constraints that survive a settlement-first lens:**

| # | Finding | Settlement implication |
|---|---|---|
| A1 | Points today buy **bodies and guns only**; stats + 150 skills are free (bundled into rank) | A global atomic system *can* price stats — but that fights the BIG RULE ("depth in settlement, not list-buy"). Decide intentionally (§5 Q1). |
| A2 | Terrain density swings win rate **more than any points cost** (66-pt measured) | Settlement boards must stay inside **9–12**. Points cannot balance an illegal raid board. |
| A3 | Thresholds (24" range, extra attacks) **cannot be priced** — only gated | Same law for settlement: don't try to points-balance "raid always uses whole 12×36" or "Power brown-out." Gate or design around them. |
| A4 | Weapon builder is the **only** sim-validated atomic spine | Structure costs should reuse the same tick language and packaging (versioned cost artefact, not rules text). |
| A5 | Rank validation is stale / partially illegal (swarm lists past pyramid) | Re-validate **before** rescale. Don't bake a broken ladder into 1000-pt numbers. |
| A6 | **Entire settlement + campaign layer uncosted** | This is the primary gap the global system must fill. |
| A7 | 2051 arsenal: 62 items, zero costs, several hooks use banned mechanics (saves, ignore-cover, re-rolls) | Cost only after remapping onto existing levers. Settlement structures that "unlock 2051 kit" are permission gates, not free power. |
| A8 | Nothing Locked; ×10 / 1000-pt rescale was planned but not recorded in vault notes | Treat rescale as a packaging decision when we build the system, not as sacred. |
| A9 | `ff.py` in repo root is a working multiplicative costing engine (different game) | Steal architecture (lookup tables, multiply output-scalers, add flat effects, negative drawbacks), not numbers. |

**Settlement inventory status (from audit §2.7):** all 25 structures UNCOSTED; all upgrade ladders UNCOSTED; Groundworks UNCOSTED; founding Goods budget unset; Med-bay `+X` and Mess Hall Stress unset.

**Critical firewall already written (must survive any redesign):**
> Ownership buys availability, never free board power. Deployables still cost crew-points and still eat 9–12 density. A bigger settlement never means a bigger army.

### 1.2 POINTS-RESEARCH — how other games do atomic costing

**Purpose:** primary-source research across ~18 systems + Gutschera's GDC 2007 "Magic Lessons" as the design textbook.

**Five load-bearing lessons (settlement-relevant):**

1. **Your dice engine is unusually friendly to flat per-+1 pricing** (`1d10+mod vs 7+` is linear). Caps (damage +4, armour −2, ±3, stat +6) are what keep builds on the diagonal where one tick price stays valid. **Caps are costing preconditions, not patches.**

2. **Multiply what the engine multiplies.** Action frequency / reliability → multipliers. One-shot effectiveness → addends. Settlements currently adds everything. Implication for settlement: something that lets a fighter act more often off-table (Drone Bay recon without spending a body) is an *action-economy* effect and should be gated/capped harder than a flat storage bump.

3. **Extra actions cannot be sold on the same scale as +1 damage.** Arithmetic in your engine: one extra attack ≈ 81% of maxing every other combat dial. **Gate, don't price.** Same for settlement: "extra downtime action" / "extra mission dispatch" should be structure *permission* with hard caps, not a cheap Materials buy that snowballs.

4. **You pay for differentiation somehow.** Free gear homogenises flavour (40k 10th → partial reverse in 11th). DIY armoury means you should keep priced characteristics (or price the *decision*, not every atom) — flavour is the expensive currency for this game.

5. **Settlement is an entitlement problem, not a battle-cost problem.** Oathmark is the proof: kingdom widens the menu; battle points stay equal. Last Days is the opposite pole (no post-creation points cap; brakes via attrition + upkeep). **Pick a position; don't drift.**

**Closest thematic precedents for Settlements specifically:**

| Game | What to steal | What not to copy blind |
|---|---|---|
| **Oathmark** | Equal points always; rings + rarity; unlock grammars; heroes capped by buildings; soft reversible losses; start small (~30% ceiling); lead book with settlement | Unvalidated race multipliers; day-one max kingdom |
| **Last Days** | Refuge as free shape (Max Size / Empty Spaces / Built-In Perks); Empty Spaces as real constraint; development raises upkeep; upkeep-reducer buildings; Jobs; post-game base-threat roll; Escape-Vehicle insurance; **score the base** | Unlimited fielded group after creation (conflicts with your equal-points lock) |
| **Trench Crusade** | Four dials per entry (price, LIMIT:N, 0–N slots, value gates); opt-in expensive catch-up; veteran *cap* vs *price* as a deliberate fork | Ducat thresholds if they fight your endless-meta default |
| **Necromunda** | Stashed gear ≠ rating; rating = fielded power | Play-frequency snowball (you're exposed — need a wash table) |
| **Rangers of Shadow Deep** | Archetype adjusts *budget and sub-caps*, never reprices the catalogue | — |
| **Malifaux** | +1 out-of-keyword tax (thematic crews cheaper) | — |
| **TWD: AOW** | Custom formula + deliberate premium for unpriceable combos; neutral threat costed to the *game*; Danger Zones raise threat for *both* | — |

### 1.3 POINTS-FINDINGS — decision layer

**Purpose:** turn research into forks and a recommended sequence.

**Forks already framed (settlement-facing):**

| Fork | Status in findings | Recommendation there | This report's stance |
|---|---|---|---|
| A — Gear costs points? | Keep priced characteristics; import 11th stepper + "cost the decision" | Agree for DIY armoury | Agree — but **settlement unlocks** should mostly be *permission*, not free gear |
| B — Reprice veterans? | Close call: price (you) vs cap (Trench Crusade) | Pick deliberately; add Limited Potential either way | Prefer **keep +2 Advance** for the "grind down to survivors" story; **add** a hard per-model Advance ceiling |
| C — Factions | Steal RoSD archetypes (budget/caps, one price list) + Malifaux keyword tax | Agree | Agree — and map Location boosts the same way (shape, not free points) |
| D — Settlement grants | Oathmark entitlement + Last Days upkeep | Agree hard | **This is the spine of §3–4 below** |
| E — Currencies | Goods/Materials own + points field; no third battle currency | Agree | Agree; Power/Water stay flows/upkeep, never a second battle currency |

**Next-steps sequence from findings (still correct):**
1. Caps as costing preconditions  
2. Sidegrade audit on Weapons.md  
3. Vanilla curve (ranks, no skills/gear)  
4. Measure `f` for conditionals in sim → Hero-style discount ladder  
5. Declare reference environment  
6. Residuals table  
7. Versioned cost artefact separate from rules text  

---

## 2 · Current settlement system (as drafted) — what actually exists

### Locked principles (from Settlement Design Questions + Structures)

- **Own ⟂ field:** four resources (Goods, Materials, Power, Water) vs crew-points.
- **Hybrid board pieces:** build with Materials off-table; fielding a turret/wall piece costs crew-points inside 9–12.
- **Binary structures:** Functional | Disabled; sabotage destroys benefit; flat Materials repair.
- **Endless meta default** + optional season with razing + comeback.
- **One roster**, assigned Battle / Work / Mission each cycle.
- **Location ⟂ Faction.**
- **Canvas:** 12"×36" on 1" grid = defender's back three density squares on 3'×3'. No raid window.
- **Start structures:** HQ, Water Reclaimer, Generator, Processor, Salvage Yard (at Power capacity = draw).
- **25 structures**, five categories (Sustain / Convert / Operate / Recover / Defend). No build prerequisites. Space is the scarce resource (~10 of 25 fit).
- **Goods** currency naming locked (Cash rename reverted).

### Still blank (blocks any points system for settlements)

Economy rates, Materials build costs, founding Goods, storage numbers, Water per head, hire prices, Groundworks cost, repair rate, HQ dispatch increments, Med-bay +X, Mess Hall Stress, what a raider steals, whether owned armoury gear still costs points to field (research says **yes — two-gate**).

### Tension the audit correctly flagged (6.16)

Your BIG RULE: *keep list-building minimal; depth in terrain + base-building.*  
A fully atomic global points system that prices every +1 STR and every skill **deepens list-buy**. That fights the pillar.

**Recommendation:** use atomic ticks as the *designer/sim language* and as the way to **derive** catalogue prices — but player-facing settlement play should stay **catalogue + space + upkeep**, not a second point-buy spreadsheet. Players buy a Med-bay for X Materials; *you* know X was derived from "Fate +N ≈ Y ticks of campaign value." Don't make them assemble buildings from atoms at the table.

---

## 3 · Suggestions — integrate, change, or rethink (settlement-first)

*Combat-adjacent items included only where they protect settlement balance.*

### 3.1 Architecture (high confidence — steal)

| # | Suggestion | Source | Why |
|---|---|---|---|
| S1 | **Keep equal battle points always.** Settlement never buys a bigger army. | Oathmark + already locked | Only safe persistent-base design found |
| S2 | **Structures = permission / capacity / economy / raid-board shape.** Never a free points multiplier. | Structures contract + Oathmark | Already mostly written — enforce ruthlessly when costing |
| S3 | **Adopt Last Days' three payoff channels** for every structure: Capacity · Economy · Battle-effect (raid-only unless priced into crew list) | Last Days | Stops every building becoming a combat buff |
| S4 | **Development raises upkeep.** Bigger/better base burns more Water (and optionally Goods) every cycle. Include ≥1 **upkeep-reducer** structure competing for a slot | Last Days Seasons | Self-limiting growth without points ceiling games |
| S5 | **Jobs / assignment is the throughput valve.** One able body → one job. Drone Bay etc. buy *exceptions*, expensive in space + Power | Last Days + your roster lock | Ties crew size to settlement output |
| S6 | **Score the settlement** in campaign / season victory (fill spaces, bank Goods, healthy roster) — military power a minority of score | Last Days | Makes players care about the pillar without giving free win% |
| S7 | **Start at ~30% of ceiling** (you already do: starters = 24% of lot). Don't gift founding Goods that fill the canvas | Oathmark 2E regret | Room to grow is the campaign |
| S8 | **Soft reversible losses.** Disabled/occupied ≠ permanent wipe of unlocks the player painted models for | Oathmark | Anti death-spiral + goodwill |
| S9 | **Insurance building** (Vault already sketches this; strengthen as catastrophe cover like Escape Vehicle) | Last Days | Real decision: safety vs capability for one slot |
| S10 | **Couple battlefield → base with one post-game roll** (casualties / Guards / specific structures) that can Disable a structure or spill a tank | Last Days | Most base games never connect the layers |
| S11 | **Four catalogue dials per priced entry:** Materials (or Goods) price · LIMIT:N · slot grammar · value gate | Trench Crusade | Price alone cannot do cap work |
| S12 | **Stashed gear does not count toward crew rating**; fielded gear does | Necromunda | Settles armoury fork; enables underdog banding later |
| S13 | **Income wash table** (diminishing returns above a threshold) | Necromunda / Mordheim | You persist outside campaigns — play frequency will otherwise dominate |
| S14 | **Locations = free shape + one Built-In Perk**, not free Materials pile | Last Days Refuge interface | Instant readable trades; balances founding |
| S15 | **Specialists / exotic unlocks capped by buildings**, not by "% of points" | Oathmark | Uses your scarce lot as the hero tax |
| S16 | **Publish costs in a versioned artefact** (`costs/vN.json` or similar), never only in note prose | 40k packaging lesson | Patch without rewriting the rulebook |

### 3.2 Changes worth considering even if they fight current drafts

| # | Current draft | Suggested change | Rationale |
|---|---|---|---|
| C1 | Stats/skills free forever | **Optional:** keep player-facing free, but designer-cost ranks as `(stat ticks) × command multiplier` internally | Fixes acknowledged undercosted rich lines without making list-buy a second game |
| C2 | +2 per Advance / −2 per scar symmetric | **Advances full price; scars refund half** (or scars refund 1) | BattleTech asymmetry — stop farming cheap screens with scars |
| C3 | No per-model Advance ceiling | Add **Limited Potential** (e.g. max 3–5 Advances per fighter unless a structure raises it) | Stops one model becoming the campaign |
| C4 | 25 structures all available at founding | Consider **rarity / Fabricator unlock rings** for T2–T3 and 2051 (Oathmark frontier) | Keeps early game readable; puts scary toys on unreliable frontier |
| C5 | Space-only anti-inflation | Keep space, **add** escalating Materials tier costs + storage caps (already planned) + wash table | Space alone doesn't slow a player who plays 3×/week |
| C6 | Raid = equal points, prepared defence | Explicit **attacker compensation lever** (VP, free Scout intel, +N points, or defender caps defensive crew-point spend on turrets) | Home board is a real advantage; equal points alone may under-serve attackers |
| C7 | "No flat +1" on structures | Keep — but allow **efficiency** buildings that are *only* upkeep reducers | Last Days Stove pattern; otherwise every slot must be a capability spike |
| C8 | Two different five-faction lists in vault vs 2051 research | **Kill one.** Prefer 2051 RPS triangle for release (Remnant / Scavengers / Swarm / Ghosts / Foundry) | Audit §6.13; can't cost two parallel faction sets |
| C9 | Recruiting Board cut | Reintroduce as **economy structure** once hiring exists (Last Days Recruit job home) | Completes Operate category without combat bloat |
| C10 | Depth in settlement *and* 150 skills *and* DIY weapons *and* 25 buildings | **Curate skills to a starter set** for alpha; keep full catalogue as expansion | Audit / RULES-AUDIT already recommend this; protects BIG RULE |

### 3.3 Things *not* to do (research consensus)

- Do **not** let settlement investment raise the battle points budget.
- Do **not** add a second battle currency (SWC) — rank gates already do that job.
- Do **not** try to points-price thresholds (whole-settlement raid geometry, Power cliff at capacity).
- Do **not** chase 50% win rate across every settlement specialisation.
- Do **not** embed final costs only inside Structures.md prose.
- Do **not** price 2051 kit that still uses saves / ignore-cover / re-rolls — remap first.
- Do **not** make Free Wargear the settlement answer; you'll homogenise the DIY armoury.

### 3.4 Global atomic points system — how it should serve settlements

Your example (Rifle class + DMG ticks + Fire condition; Building + Processing + gather buff) is the right *designer* language. Proposed split:

```
DESIGNER / SIM LAYER (global ticks)
  Cost = (Body + Gear + StatTicks) × ActionMult × ConditionalDiscount
  StructureDerivedValue = Σ (capacity ticks, economy ticks, raid-board ticks, unlock ticks)
  MaterialsPrice ≈ f(StructureDerivedValue, footprint opportunity cost, Power draw)

PLAYER LAYER (what they see)
  Crew: rank + gear catalogue prices in crew-points (100 or 1000 scale)
  Settlement: Materials (and sometimes Goods) catalogue prices + Power draw + footprint
  Never: "assemble a building from +1 STR atoms" at the table
```

**Mapping your examples onto settlement:**

| Element | Tick role | Player pays |
|---|---|---|
| Building footprint / Cover / Lockable | raid-board shape ticks | Materials + space |
| Processing (Materials gatherer) | economy ticks / cycle | Materials + Power + space |
| +gather rate | economy multiplier (careful — multiplicative) | upgrade tier or second structure |
| Turret Mount | permission (auto-deploy) | Materials + space + Power; **turret still costs crew-points** |
| Bunkhouse +N heads | capacity ticks | Materials + **ongoing Water** |
| Med-bay +Fate | campaign ticks (not battle win%) | Materials + Power; scar heal costs Goods so −2 rebate stays honest |
| Drone Bay free scout mission | **action-economy exception** | Expensive space/Power; hard LIMIT 1 |

**Balance philosophy (your words, made operational):**
- Paths can be unequal; **strategic spend against inherent strengths should win more often.**
- Target: no path is a *hard brick wall* every game — use scenarios, density band, and RPS factions so "wrong" spends still have boards where they shine.
- Acknowledge openly in the rulebook: *perfect balance is impossible; we cost for a healthy meta, not identical win rates.*

---

## 4 · Open questions for you

Answers here will directly shape the global points system. I've marked ones that block settlement costing first.

### Blocking — answer before we build cost tables

**Q1. Player-facing depth.** Should players ever buy individual stat ticks / skills with points, or should atomic costing stay a **designer/sim tool** while players keep "buy rank, get its bundle"?  
*(BIG RULE tension. My lean: designer-only atoms for v1.)*

**Q2. Scale.** Stay on **100-pt** with finer decimals/internal ticks, or commit to **1000-pt** rescale so multipliers land on integers?  
*(Research leans 1000; only worth it if prices don't all end in 0.)*

**Q3. Veteran valve.** Keep **+2 per Advance** crowding out rookies, switch to **Trench Crusade caps** (XP free, hard ELITE/scar/rate caps), or **hybrid** (small price + hard Limited Potential)?  
*(Narrative you've written wants pricing; anti-snowball wants a hard ceiling too.)*

**Q4. Armoury two-gate.** Confirm: gear costs **Goods to own** and **points to field**, stash doesn't rate?  
*(Research: yes. Your open Economy question.)*

**Q5. Settlement win condition.** Is "develop the settlement" a **scored / season** goal, or only flavour around endless equal-points play?  
*(If you want people to care about buildings, score them.)*

**Q6. Attacker fairness on raids.** What compensation is acceptable: extra points, free intel, VP, capped defender deployables budget, or "defence is supposed to be favoured"?

**Q7. Upkeep intensity.** How punishing should Water (and any Fuel-analogue) be — soft "can't hire more," hard attrition, or Last Days–style Critical tracks?  
*(Sets whether development-raises-upkeep is a slap or a real brake.)*

### High value — shapes catalogue costing

**Q8. Founding Goods budget.** Rough feel: enough for **1–2** extra structures, or a shopping spree?  
*(Oathmark regret: start small.)*

**Q9. Are all 25 buildable day one**, or do Fabricator / location / rarity gate T2–T3 and exotic Operate/Defend pieces?

**Q10. Location list.** Confirm ~10 city locations and that each grants **exactly one** free structure/boost from the shared catalogue (no unique-only buildings).

**Q11. Faction set.** Which five are canonical for release costing — vault names or 2051 RPS set?

**Q12. Hire prices.** Separate Goods scale from battle points (recommended), or reuse 5/8/16/24?

**Q13. Post-game base threat.** Do you want an automatic "your casualties risk a Disabled structure / spilled tank" roll every cycle, or only on lost Defence scenarios?

**Q14. Insurance.** Is Vault the only catastrophe cover, or do you want an explicit Escape / Contingency structure that protects stash on a lost Refuge-equivalent event?

### Philosophy — so we don't over-engineer

**Q15. Fun > flat balance.** Confirm the acceptance bar: *a clever player exploiting faction/location synergies should beat a same-points player who fights their own kit — but every legal specialisation should have scenarios where it thrives.* Any harder requirement?

**Q16. Alpha scope of settlement costing.** Cost the **starter five + ~5 more** for alpha, or the full 25 before playtest?

**Q17. Sim as oracle.** Are you willing to treat `crew_sim` / `engine2d` win-rate bands as the **acceptance test** for costs (with a published residuals table), or do table feel override sim when they conflict?

**Q18. Anything currently drafted you'd protect even if research says change it?** (e.g. free skills, pyramid, WND 1, Goods naming, 12×36 canvas, binary sabotage.)

---

## 5 · Recommended next move (when you're ready for the points system)

1. Answer **Q1–Q7** (and Q11 if you can).  
2. Write a one-page **Costing Preconditions** note (caps, equal-points firewall, gate-don't-price list).  
3. Build **tick dictionary v0** — body, +1 test, +1 damage, payload/condition, armour step, Power draw unit, Water/head, Materials/structure-footprint-band — *numbers provisional*.  
4. Derive **Materials prices** for starter five + Bunkhouse, Storehouse, Med-bay, Perimeter Wall, Turret Mount from that dictionary.  
5. Wire prices into sim / a small costing script (architecture from `ff.py`, Settlements math).  
6. Only then expand to full 25 + gear rescale.

---

## 6 · Source map

| Doc | Role |
|---|---|
| `docs/POINTS-AUDIT.md` | Inventory + constraints + contradictions in *our* vault/sims |
| `docs/POINTS-RESEARCH.md` | External systems, formulas, Oathmark/Last Days primary reads |
| `docs/POINTS-FINDINGS.md` | Decision forks + ordered next steps |
| `rules-vault/.../Structures.md` | Live 25-structure catalogue (uncosted) |
| `rules-vault/.../Settlement.md` | Founding / layout intent (mostly Designing) |
| `rules-vault/.../List Building.md` | Own-vs-field + 100-pt ladder |
| `docs/SETTLEMENT-DESIGN-QUESTIONS.md` | Eight locked forks (2026-07-20) |
| `docs/RULES-INTERVIEW-PLAN.md` | Interview sequence; Economy still open |

---

*End of report. Next session: lock answers to §4, then draft the global tick dictionary and first Materials cost table.*

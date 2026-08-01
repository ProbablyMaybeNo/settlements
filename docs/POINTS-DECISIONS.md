# Points & Settlement — Locked Decisions

*Interview answers 2026-07-27 → 2026-07-28. Feeds `GLOBAL-POINTS-SYSTEM.md`. Nothing here is player-facing rules text — it is the brief for the costing engine.*

---

## Scale & packaging

| # | Decision |
|---|---|
| D1 | Battle budget scale = **1000** Credits. |
| D2 | Players see **final catalogue prices only**. The atomic tick formula is designer/sim-only. |
| D3 | **One Crew Rating system.** A fielded fighter’s cost = **Credits cost of the body + Credits cost of equipped gear**. No separate “fielding points” currency. |
| D4 | **Stashed / unequipped gear** adds **0** to Crew Rating. |
| D5 | Credits cost **is** rating when fielded. Hiring and buying kit spend Credits into the roster/armoury; listing them for battle spends that same number against the agreed cap. |

## Resources

| # | Decision |
|---|---|
| D6 | Resources = **Credits · Materials · Power**. **Water is cut.** |
| D7 | **Credits** = primary currency (hire, gear, most purchases). |
| D8 | **Materials** = build/upgrade structures; convertible to Credits via a **Trader** structure (rate TBD by testing once structure costs exist). |
| D9 | **Power** = assigned each Settlement round. **Generator = +5** output. Structure draw: **T1 = 1 · T2 = 2 · T3 = 3**. Unpowered = **no benefit this round**, still on the board. Assignment free each round. |

## Roster & housing

| # | Decision |
|---|---|
| D10 | Housing: HQ base **12** owned slots; each **Bunkhouse +6**. No per-head upkeep. |
| D11 | Equipment cap: start **30** slots; each Equipment Shed / Armory tier **+30**. 1 item = 1 slot. Over cap → cannot buy/loot more until sell/scrap/build. |
| D12 | **Pyramid at founding only** (starting crew). Always **exactly one Leader** ever. After founding, the **1000 rating cap** (or agreed Crew Rating) governs what you field — chaff vs veterans is a player choice. |
| D13 | Veterans **get more expensive as they Advance**. Exact increment = derived from the global tick of what the Advance bought. |
| D14 | **Scars** = rules penalties only — **no** rating refund. |

## Settlement & raids

| # | Decision |
|---|---|
| D15 | No settlement-development victory score. |
| D16 | Founding Credits/Materials budget ≈ **1–2** extra structures beyond starters. |
| D17 | Gatherers produce every powered Settlement round; **bonus if a worker is assigned**. |
| D18 | Raids: **risk vs reward** (steal Credits/Materials). No attacker list cushion for now. Structure-on-board costing deferred to a raid pass. |
| D19 | Cut Water structures for now (Reclaimer / Cistern / Water Tower). |
| D20 | Anti-snowball: housing + equipment slots + storage + raids + escalating upgrades + **per-Crew Rating cap**. No extra upkeep sink. |

## Costing shape — ruled 2026-08-01

| # | Decision |
|---|---|
| D21 | **Pricing stays additive. A weapon has exactly one price**, independent of who carries it. Closes `POINTS-TABLE.md` §9 / completion-plan **M7**. The coupling §9 predicted is real and large — offensive primitives are worth **2.4–6.0×** more per elite model — but it is swamped by body count (`suite.py`: r² = 0.708 on model count, **+3.78** win-points per extra model; Gunline 4 finished **last** at 32%). Flat pricing leaks *toward* swarms, not away, so a carrier multiplier would push elite lists further down. The ±3 modifier cap and the rank gates bound the residual error. Re-open only if a future run shows elite lists winning at equal points. |
| D22 | **Skills are measured but never charged.** Each of the ~150 skills is priced individually from its primitives, and that price is used as a **design band**, not a purchase price. Buying a rank still buys its stats *and* its skills (`Unit Design` · `List Building` — unchanged). A skill measuring far outside its tier's band is **redesigned, not repriced**. This is what makes `SKILL_TIER_GOODS` (20/35/55) real: the tier premium becomes the *measured median* of its tier instead of an estimate. Action-economy skills (extra attack, extra Order, +WND, +MOV) stay **rank-gated and unpriced** — they are not band-checked, they are capped. |
| D23 | **Scope of the costing pass = everything, structures included.** `Economy.md` gets drafted as part of this work, because structures cannot be priced on the battle anchor — a Storehouse buys zero win probability. Structures use a **second anchor: payback period in Materials against production per cycle.** Two anchors, one catalogue. |

## Vocabulary — ruled 2026-08-01

One number, two words, and nothing else.

| # | Decision |
|---|---|
| D24 | **The old currency name is retired. The currency is Credits.** The previous word read as *cargo*, not money, which is the one job it had to do. (History, so it isn't re-litigated: it was renamed to **Cash** on 07-24 and reverted on 07-26 on a scavengers-haul-it-back argument. **Credits** replaces both.) **Materials** and **Power** are unchanged — both already say what they are. |
| D25 | **Crew Rating** is the battle gate: the sum of the Credit costs of the crew you **field**, against a scenario cap (standard **1000**). This retires **four** names for one number — `crew-points`, `battle rating`, `fielding points`, and bare `points`. |
| D26 | **A unit's Credit cost IS its Crew Rating contribution. One number, no conversion.** A two-number design was floated — a Credit price for acquisition, a separate Rating for the table, linked by an availability band — and **rejected**: it makes every unit get costed twice through two systems for no gain at the table. This restores D3/D5 exactly as written, under the new name. Stashed, unequipped gear still counts **0** against Rating (D4) — you paid Credits to own it, it only occupies Rating when fielded. |

**In one line:** *you buy everything with Credits, and the Credits you put on the table are your Crew Rating.*

## Conflicts to resolve during this pass

- ~~**Water.**~~ **Resolved 2026-08-01** — Water cut and propagated through `Structures.md`, `List Building.md` and `Settlement.md`. Catalogue 25 → **23**, starters five → **four**, Sustain 6 → **4**.
- **Scale.** The vault still prints the **100-point** ladder (Sidearm 4, Standard Ranged 10, Light armour 3, ranks 5/8/16/24); `points/` is on the **1000-Credit** scale. Propagate after the atoms lock, not before.
- **Price authority.** `engine2d/data.py` hand-sets its own 100-scale costs, so the simulator does not price crews with the costing engine. Until they share one table, a price cannot be verified end-to-end.
- **Generator output.** D9 says **+5**; the vault's `Structures.md` says **+3**. The Water cut also removed a −1 draw, so the deliberate "start at exactly Power capacity" tension is now 1 spare. One ruling fixes both.
- **HQ housing.** D10 says **12** slots; the vault says **10**.
- **Scars.** D14 says *rules penalties only, no rating refund*; `List Building.md` still pays a **−2** rebate per lasting scar, and `Structures.md` has a Med-bay callout defending that rebate. D14 is newer. Note also that **no scar effect table has ever been written** — "Full scar / injury effect tables" is still unticked on the roadmap, so a scar currently has a Rating value and no content.

## Open (not blocking v0 engine)

- Exact Materials↔Credits conversion rate
- Raid deployable / wall crew-point interaction
- Final rank Credits ladder (engine will propose; playtest locks)
- Full Materials prices for all 25 structures

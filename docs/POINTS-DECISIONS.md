# Points & Settlement — Locked Decisions

*Interview answers 2026-07-27 → 2026-07-28. Feeds `GLOBAL-POINTS-SYSTEM.md`. Nothing here is player-facing rules text — it is the brief for the costing engine.*

---

## Scale & packaging

| # | Decision |
|---|---|
| D1 | Battle budget scale = **1000** Goods-points. |
| D2 | Players see **final catalogue prices only**. The atomic tick formula is designer/sim-only. |
| D3 | **One battle rating system.** A fielded fighter’s cost = **Goods cost of the body + Goods cost of equipped gear**. No separate “fielding points” currency. |
| D4 | **Stashed / unequipped gear** adds **0** to battle rating. |
| D5 | Goods cost **is** rating when fielded. Hiring and buying kit spend Goods into the roster/armoury; listing them for battle spends that same number against the agreed cap. |

## Resources

| # | Decision |
|---|---|
| D6 | Resources = **Goods · Materials · Power**. **Water is cut.** |
| D7 | **Goods** = primary currency (hire, gear, most purchases). |
| D8 | **Materials** = build/upgrade structures; convertible to Goods via a **Trader** structure (rate TBD by testing once structure costs exist). |
| D9 | **Power** = assigned each Settlement round. **Generator = +5** output. Structure draw: **T1 = 1 · T2 = 2 · T3 = 3**. Unpowered = **no benefit this round**, still on the board. Assignment free each round. |

## Roster & housing

| # | Decision |
|---|---|
| D10 | Housing: HQ base **12** owned slots; each **Bunkhouse +6**. No per-head upkeep. |
| D11 | Equipment cap: start **30** slots; each Equipment Shed / Armory tier **+30**. 1 item = 1 slot. Over cap → cannot buy/loot more until sell/scrap/build. |
| D12 | **Pyramid at founding only** (starting crew). Always **exactly one Leader** ever. After founding, the **1000 rating cap** (or agreed battle rating) governs what you field — chaff vs veterans is a player choice. |
| D13 | Veterans **get more expensive as they Advance**. Exact increment = derived from the global tick of what the Advance bought. |
| D14 | **Scars** = rules penalties only — **no** rating refund. |

## Settlement & raids

| # | Decision |
|---|---|
| D15 | No settlement-development victory score. |
| D16 | Founding Goods/Materials budget ≈ **1–2** extra structures beyond starters. |
| D17 | Gatherers produce every powered Settlement round; **bonus if a worker is assigned**. |
| D18 | Raids: **risk vs reward** (steal Goods/Materials). No attacker list cushion for now. Structure-on-board costing deferred to a raid pass. |
| D19 | Cut Water structures for now (Reclaimer / Cistern / Water Tower). |
| D20 | Anti-snowball: housing + equipment slots + storage + raids + escalating upgrades + **per-battle rating cap**. No extra upkeep sink. |

## Costing shape — ruled 2026-08-01

| # | Decision |
|---|---|
| D21 | **Pricing stays additive. A weapon has exactly one price**, independent of who carries it. Closes `POINTS-TABLE.md` §9 / completion-plan **M7**. The coupling §9 predicted is real and large — offensive primitives are worth **2.4–6.0×** more per elite model — but it is swamped by body count (`suite.py`: r² = 0.708 on model count, **+3.78** win-points per extra model; Gunline 4 finished **last** at 32%). Flat pricing leaks *toward* swarms, not away, so a carrier multiplier would push elite lists further down. The ±3 modifier cap and the rank gates bound the residual error. Re-open only if a future run shows elite lists winning at equal points. |
| D22 | **Skills are measured but never charged.** Each of the ~150 skills is priced individually from its primitives, and that price is used as a **design band**, not a purchase price. Buying a rank still buys its stats *and* its skills (`Unit Design` · `List Building` — unchanged). A skill measuring far outside its tier's band is **redesigned, not repriced**. This is what makes `SKILL_TIER_GOODS` (20/35/55) real: the tier premium becomes the *measured median* of its tier instead of an estimate. Action-economy skills (extra attack, extra Order, +WND, +MOV) stay **rank-gated and unpriced** — they are not band-checked, they are capped. |
| D23 | **Scope of the costing pass = everything, structures included.** `Economy.md` gets drafted as part of this work, because structures cannot be priced on the battle anchor — a Storehouse buys zero win probability. Structures use a **second anchor: payback period in Materials against production per cycle.** Two anchors, one catalogue. |

## Conflicts to resolve during this pass

- **Water.** D6/D19 cut Water; the vault's `Structures.md` still has the Water Reclaimer, Cistern and Water Tower as core structures, with Water consumed per head and tank capacity as the Water cap. One of the two is wrong. Ruling needed before structures are costed.
- **Scale.** The vault prints the **100-point** ladder (Sidearm 4, Standard Ranged 10, Light armour 3, ranks 5/8/16/24); `points/` is on the **1000-point** scale. Propagate after the atoms lock, not before.
- **Price authority.** `engine2d/data.py` hand-sets its own 100-scale costs, so the simulator does not price crews with the costing engine. Until they share one table, a price cannot be verified end-to-end.

## Open (not blocking v0 engine)

- Exact Materials↔Goods conversion rate
- Raid deployable / wall crew-point interaction
- Final rank Goods ladder (engine will propose; playtest locks)
- Full Materials prices for all 25 structures

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

## Open (not blocking v0 engine)

- Exact Materials↔Goods conversion rate
- Raid deployable / wall crew-point interaction
- Final rank Goods ladder (engine will propose; playtest locks)
- Full Materials prices for all 25 structures

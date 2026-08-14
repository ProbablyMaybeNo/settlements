---
type: rule-phase
phase: "11"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 17
depends_on: ["Settlement"]
feeds_into: ["Balance"]
tags: [settlements/phase, settlements/stage/s4]
---
# 11 · Economy
> **S4 Settlement & Campaign** · status **Drafted** · build order **17**

**Depends on:** [[Settlement]]
**Feeds into:** [[Balance]]
**Raw dependency (from Notion):** Settlement

## Focus
Resource flow, upkeep, and anti-inflation sinks that keep the campaign economy from breaking.

The Rules column should nail down:
- The resource types and how they're gathered (gatherer buildings, scavenging, scenario rewards).
- The spending sinks: building, crafting, recruiting, researching, upkeep.
- Upkeep/maintenance costs so growth carries friction.
- Anti-snowball / anti-inflation mechanics (raids, decay, caps) so an early leader can't run away.
- How a solo or drop-in player tracks their own economy independently.

## Working rules / decisions

*Drafted 2026-08-05 from [[Full Rules System v1]] §17.3, §19, §20 and §29. The numbers here are the ones the master note rules; the **sink** question at the bottom is the one thing still genuinely open.*

### Three resources, two of them banked

| Resource | Buys | Banked? |
|---|---|---|
| **Credits** | Bodies, weapons, armour, equipment, Levels — everything that goes on the table | **Yes**, capped by storage |
| **Materials** | Structures, repairs, research, crafting — everything that goes on the lot | **Yes**, capped by storage |
| **Power** | Nothing. It is **output vs draw**, checked each Settlement Phase | **No** — a flow, never a store |

^tbl-three-resources

*(Water was cut 2026-08-01. Housing slots are the only population brake, and there is **no per-head upkeep** — confirmed unneeded and actively harmful.)*

> [!important] Credits do two jobs, and that is deliberate
> **Credits buy what you own; Crew Rating gates what you field** ([[List Building]]). One number does both, so there is no second currency to convert between. **Stashed and unequipped gear counts 0** toward Rating — you paid to own it, it only occupies Rating when it is on the table.

### Income

- **Battle rewards.** Both crews bank Resources from scenario-defined sources — objectives, kills, control, Glorious Deeds — **regardless of who won** ([[Core Game Format]]). Killing pays even when it doesn't win.
- **Gatherers.** The **Processor** produces Materials, the **Salvage Yard** produces Credits, once per Settlement Phase. An assigned worker adds **+1** to either ([[Structures#Worker benefits]]).
- **Scavenge dispatches.** One roll on the territory's Loot table, no battle required ([[Downtime]] · [[Territory#The default loot table]]).
- **Searching and looting** mid-battle, on the same table ([[Terrain Interaction#Searching and looting]]).
- **Raiding.** Taking what an opponent has banked, out of the containers it sits in (below).

> [!success] The reward rate is checked — T12
> A normal battle reward of **65 Credits + 33 Materials** funds about **one Recruit**, and a **Tier I structure takes ~3.0 battles** to afford. That matches the design targets once real prices are applied: a fighter is an impulse buy, a building is a campaign-scale commitment.

### Founding budget

**250 Materials + 150 Credits.** 250 Materials is roughly **two Tier-1 structures** on top of the four free starters ([[Settlement#Starting structures]]).

The **whole 23-structure catalogue is open from turn one** — there are **no prerequisites**, so a founding player is choosing what to specialise in rather than climbing a tree ([[Structures]]).

### Power — output vs draw

The **Generator** produces **+5**. Every powered structure has a **draw** scaled to its tier:

| Tier | Draw |
|:--:|:--:|
| **T1** | **−1** |
| **T2** | **−2** |
| **T3** | **−3** |

^tbl-power-draw-by-tier

A structure left **unpowered is Disabled for the round** — it is Functional or Disabled, never partly working ([[Structures]]).

The four starters draw **3** — HQ 1 + Processor 1 + Salvage Yard 1 — against the Generator's **+5**, so a new settlement opens with **two spare**. More output means another Generator or an upgrade; never a free multiplier.

> [!check] Reconciled — Generator **+5**, not +3
> [[Structures]] carried **+3** with a `POINTS-DECISIONS.md` **D9** conflict flagged against it. [[Full Rules System v1]] §19 rules **+5** with the T1/T2/T3 draw ladder above, which agrees with D9. **+5 is the number**; the old +3 and its "start at capacity" tension note are retired.

### Storage, caps and overflow

Four containers, each with a different raid exposure:

| Container | Holds | Exposure in a raid |
|---|---|---|
| **HQ** | A little of everything | Must be entered; Lockable |
| **Gatherer buffer** | A little of *its own* resource | **Easy pickings** — open ground, Searchable |
| **Storehouse** *(repeatable)* | The bulk of Credits and Materials | **The loot target** — Breachable and Searchable |
| **Vault** *(HQ add-on)* | Small, and secure | **Sabotage or an INT hack only** |

^tbl-storage-containers

**Overflow is lost.** Income above your cap does not bank — it spoils, walks off, or never gets hauled home. That is the primary anti-inflation lever: a rich settlement has to keep building sheds instead of sitting on a pile.

Two other caps run on the same principle:

- **Housing** — **12** body slots from the HQ, **+6 per Bunkhouse**. Housing is the **only** population brake ([[List Building]]).
- **Equipment** — **30** slots to start, **+30 per Armory tier** ([[Structures]]).

### Sinks

Where Credits and Materials actually go:

- **Materials** → structures, **upgrade tiers**, **Groundworks**, **repair at a flat 30 per structure**, research up the Fabricator ladder, crafting at the Workbench/Workshop.
- **Credits** → rank bodies, built weapons, armour, equipment and deployables, **Levels** (15/stat point · 20/35/55 per T1/T2/T3 skill · 41 for the Level-7 wound), Chems, and **ransoming a captured fighter back at half their Credits cost** ([[Campaign]]).

> [!info] The real anti-snowball valve is Crew Rating, not a tax
> Veterans get **more expensive as they Advance** and Scars **refund nothing** ([[Progression]] · [[List Building]]). So the longer a campaign runs, the **smaller** your fielded crew gets, because your best fighters crowd out rookies on the Rating cap. That is the valve — an upkeep tax was tried, measured, and cut as both unnecessary and harmful.

### Open — the economy sink

> [!question] The one genuinely unresolved economy problem
> **"Economy sink"** means: settlements pile up Credits and Materials faster than they have anything worth spending them on, so the number just sits there unused.
>
> This is **not a balance danger** — nobody is winning unfairly — it is closer to a design *waste*: a wealthy settlement's surplus isn't buying interesting decisions, it's idling. The fix is **more expensive high-tier things to build**, or **ongoing costs**, so that wealth is doing something.
>
> Nothing in the 2026-08-05 pass addressed it, and it is the reason [[Territory#The default loot table|the loot table]] is deliberately left untuned — loot is one of the few natural places to route a sink fix through.

## Open dials
- [ ] **The sink** (above) — the headline item.
- [ ] Storage numbers — the actual caps for HQ base, gatherer buffer, Storehouse and Vault.
- [ ] **How much a successful raider actually takes** from each container.
- [ ] Per-structure Materials costs are drafted in [[Structures]] but **untested** — HQ tiers, Med-bay and Mess Hall especially.
- [ ] Territory **supply requirements** per cycle ([[Territory]]).
- [ ] **Stat-point Level pricing is a known underprice** — measurement puts a stat point at **16–34 Credits** against the **15** charged, worst for STR/melee builds ([[Progression]]).
- [x] The **+1 WND price** is now **41 Credits**, derived from the measured value of heavy armour (-2 on the injury roll, 41 Credits, `armour-level-n2500` 2026-08-13) - both buy the same thing, the model staying on the table longer. C-tier: derived, not measured. Was 45 with nothing behind it.
- [ ] Whether owned gear is **also** Credit-costed to field (two-gate) or ownership replaces the cost — E2. *(Ruled in [[Full Rules System v1]] §16: stashed gear counts 0, fielded gear counts full. Confirm this closes E2.)*
- [ ] Solo / drop-in economy tracking is undrafted ([[Solo & Co-op]]).

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

---
type: research-note
title: Bolt Action
game: Bolt Action 2e / 3e
publisher: Warlord Games
depth: published cost tables + official forum + community analysis
tags: [settlements/research]
---
# 🎲 Bolt Action

> [!abstract] In one breath
> **The naive atomic system, and exactly where it breaks.** Per-man bodies priced by troop quality, weapons added at a **quality-independent** flat price — and the failure mode the flat structure predicts arrives right on schedule. Its accidental gift is an **implicit unit of account** the community derived where the designer wouldn't.

| | |
|---|---|
| **Publisher** | Warlord Games |
| **Structure** | Flat quality-priced body + flat weapon add-ons |
| **Depth of read** | Published cost tables, official forum, community cost-effectiveness analysis |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.5 |

---
## The implicit unit of account

**Type:** Costing · **Take:** ⭐ steal

Warlord's own community site hosts an LMG cost-effectiveness piece **[FACT]**:

> *"For the price of two Regular soldiers with rifles (20 points) you add a net **TWO** shots to the squad"* — the gunner and loader lose their rifle shots, so 4 minus 2 = net +2, plus range 24″→36″. Verdict: marginal.

**[INFERENCE]** The implicit exchange rate is therefore:

> **1 Regular rifleman = 10 points = 1 shot at 24″.**

And Warlord dropping the LMG from 20 to **15** in 3rd edition is consistent with them concluding it was overpriced.

**Why it matters.** **Having a public, stated exchange rate makes every other price arguable in the open, and lets playtesters audit the design.** The community reconstructed one here because none was published — which is the expensive way to get it.

**For Settlements.** This is the practical face of the "numeraire" principle, and we should **declare ours explicitly**: `1 point = 1 tick = 1/10 of a probability step` at the 1000-point scale. See `docs/GLOBAL-POINTS-SYSTEM.md`. And publish the **inverse** too — [[Gaslands#Publish the inverse]] shows how that makes it self-auditing.

---
## Where flat pricing breaks

**Type:** Costing · **Take:** ⚠️ instructive failure

Per-man body cost priced by troop quality **[FACT]**:

| Troop quality | Cost per additional rifleman |
|---|:--:|
| Inexperienced | **7 pts** |
| Regular | **10 pts** |
| Veteran | **13 pts** |

Stable across the 2nd → 3rd edition change. **[INFERENCE]** The structure is **additive, not multiplicative** — a flat quality-priced body (steps of +3) with weapon upgrades added at a **quality-independent** price. Back-derived the ladder is 0.7 / 1.0 / 1.3, suspiciously clean, but **weapon costs being flat regardless of carrier argues against a multiplier being the actual mechanism**, and no published statement says otherwise. Weapon costs are flat per item — **the exact opposite of [[Infinity#SWC — the derived second budget]]'s platform scaling.** LMG: 20 pts in 2nd edition, **15 pts** in 3rd.

**And the failure mode is exactly what the flat structure predicts** **[CONSENSUS]**:

> *"You should never take anything other than Inexperienced mortars — you need 6s to hit anyway."*

**When a weapon's performance is independent of the carrier's quality, paying the veteran body tax is pure waste.**

> **3rd edition's fix was to change the rules, not the price** — giving veteran vehicles a mechanical benefit they previously lacked, *"an attempt to make veteran vehicles more attractive."*

**For Settlements — the direct test.** Any weapon in [[Weapons]] whose effect **does not scale with the carrier's stat** creates this exact arbitrage: buy it on the cheapest legal body. Candidates worth checking are anything that applies a **condition** rather than rolling to injure, and anything with a fixed effect on a pass. **The fix is usually to make the weapon care about the shooter — not to reprice it.** Compare [[One Page Rules#Quality adds, then multiplies]], where making weapons scale with Quality removes the arbitrage structurally.

---
## Cull the catalogue

**Type:** Production · **Take:** ⭐ steal

3rd edition **[CONSENSUS]** cut Germany's unit catalogue from *"over 200 unit types"* to about **50**. Other changes: vehicles completely re-costed (a Veteran tank 666 → 528 pts), infantry per-man costs unchanged, support costs cut hard (Regular Forward Observer 100 → 75), the generic platoon selector replaced with **six platoon types unlocking different unit pools** (rated the best change in the edition), and standard game size 1000 → 1250.

> **Every entry deleted is one you no longer have to cost correctly.**

**For Settlements.** This is the anti-bloat tenet in costing form, and it's a live consideration for the [[Weapons]] characteristic list and the [[Structures]] roster. Note also the **platoon types** change: replacing one generic selector with six themed ones that unlock different pools is the same move as [[Oathmark#Concentric rings and the rarity gate]] — **structure the menu instead of restricting it.**

**[NOT FOUND]** No derivation is published — and **Warlord's own forum confirms the vacuum.** A player asking exactly this question got no official answer; the only resource offered was an **unofficial fan-made** "Bolt Action Vehicle Design System" PDF. The best advice on the thread: *"If the tanks feel overpowered, hike up the price, test again, and try again until the tank hits a sweet spot in terms of points."*

---
## Source

- Primary: published Bolt Action cost tables; official Warlord community forum and articles
- Long-form: `docs/POINTS-RESEARCH.md` §7.5
- Related: [[Wargaming Research Hub]] · [[Infinity]] · [[One Page Rules]] · [[Gaslands]] · [[Weapons]]

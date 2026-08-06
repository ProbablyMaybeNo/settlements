---
type: rule-phase
phase: "04"
stage: S5 Content
status: Drafted
build_order: 27
depends_on: ["Unit Design", "List Building", "Settlement", "Morale"]
feeds_into: ["Balance"]
tags: [settlements/phase, settlements/stage/s5]
---
# 04 · Factions
> **S5 Content** · status **Drafted** · build order **27**

**Depends on:** [[Unit Design]], [[List Building]], [[Settlement]], [[Morale]]
**Feeds into:** [[Balance]]
**Raw dependency (from Notion):** Unit Design, List Building, Settlement, full combat loop

## Focus
Build the real factions — but only once the systems they plug into already exist.

The Rules column should nail down:
- A faction template: identity, unique units, signature ability, and faction-wide buffs AND nerfs.
- How each faction's special rules hook into existing systems rather than inventing new subsystems.
- Roster and unlock differences per faction.
- The starter factions (the alpha needs just 1; plan a small spread to follow).
- Asymmetry that's born from the setting/lore, not bolted on for its own sake.

## Working rules / decisions

> [!success] Framework ruled 2026-08-05 — [[Full Rules System v1]] §24
> **One battlefield rule + one settlement affinity per faction. No flat stat bonus, no matched drawback, no exclusive unlock.** Factions are balanced peer-to-peer, not against a paired nerf. Every rule must be a discount, a conditional modifier, an action-economy nudge, or a terrain-verb exception — **none may touch a hard ceiling** (the ±3 modifier cap, the +4 Damage cap, the 24" range cap, re-rolls, or extra attacks).
>
> | Faction | Battlefield rule | Settlement affinity |
> |---|---|---|
> | **Military** | Ready token survives a failed Reaction attempt | +1 free Bunkhouse tier at founding |
> | **First Responders** | Improved Build test for field deployables | Med-bay costs −10% Materials |
> | **Labor** | Re-attempt one failed Search per battle, free | Gatherers +1 flat per Settlement Phase |
> | **Residents** | +1 Break test within 3" of another Resident | Bunkhouse costs one fewer Materials tier |
> | **Tech Workers** | Hack range bands read one step closer | Fabricator ladder −10% Materials |
> | **Criminals** | Hide in Light cover, not just Concealing — never within 6" of an objective | Trade House sell rates +10% |

> [!check] The six-faction roster above **is** the roster — adopted 2026-08-05
> [[Full Rules System v1]] §24 carries the framework **and** this project's roster together, and explicitly **supersedes this note's earlier placeholder**, which was still built on flat stat bonuses and nerfs. So the table above is canon and the WIP list below is now **naming and setting-voice input, not a competing roster.**
>
> The two line up closely: **Residents** ≈ Civilians · **First Responders** ≈ First Enforcers · **Labor** ≈ Laborers · **Military** ≈ Lost Batallion · **Tech Workers** ≈ The HACKERS. **Criminals** is new and has no WIP counterpart.
>
> **What is still yours to call:** the *names*. "Lost Batallion" and "The HACKERS" carry more setting voice than "Military" and "Tech Workers", and nothing in the framework depends on which label wins.

> [!question] Two things the framework still owes
> - **Each faction needs its rule tightened to one sentence a player can act on.** "Improved Build test for field deployables" (First Responders) doesn't say by how much — it needs a number inside the ±3 cap ([[Deployables#Build rating — some things are harder to build]]).
> - **The signature-rule lever from the 2026-07-23 note still applies:** one strong, playstyle-defining rule per faction, modelled on how BLKOUT's **Force Rules** each encode a single identity (aggro / attrition / gunline / cyber) — see `docs/BLKOUT-RULES-ANALYSIS.md` §19, steal #4. The six rules above are conditional nudges; check at the table whether each one is actually *identity-defining* or merely *flavourful*.

### WIP faction list — the original setting voice
*Kept verbatim. Superseded as a roster by the table above; the **flat stat bonuses and nerfs** below are explicitly ruled out by the framework.*

1. Civilians - Jack of all trade master of none, a crew made up of your average soccer moms and little league coach dads.
   
   - Maybe civilians don't get a faction wide bonus instead they get more options for each individual unit. They are the swarm faction, lots of inexpensive, not great, units that swarm the board.
   
1. First Enforcers - Ex-polioce, firemen, EMTs
   
   - Great at building, laying traps, moving around the map. Bonus to AGI and NRV. Larger crew sizes. Gain early access to deployables and excel at map manipulation. 
   
1. Laborers - Factory workers, Miners, Ironworks, etc. 
   
   - Bonus to STR stat or related skills, nerf to INT. Buffed with melee weapons, nerfed at shooting. Focused on super elite specialists and leaders with increased strength and excel in melee. Playstyle: Close Combat Kings
   
1. Lost Batallion - Ex-military, soldiers, airforce, navy, etc.
   
   - Bonus to Dex, experts at shooting not great at melee, have easier access to high-tech weapons and equipment. Glass canons.

1. The HACKERS - Tech experts, nerds, hackers, etc. 
   
   - Bonus to INT minus to STR, early access to high-tech equipment, excel at hacking. Playstyle = Control/buffs/debuffs Elite smaller unit crews.
## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._

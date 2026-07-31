# Settlements — 2D Engine (Phase 2)

A **headless 2D game engine** that plays full Take-a-Hold games — real board, true
line-of-sight, objective scoring, **swappable AI policies**, and wired skills. Built
to answer design questions the 1D subsystem sims (`../crew_sim.py` etc.) can't touch.

## Run it
```
py -3.13 run.py                 # one verbose game (balanced mirror) + VP timeline
py -3.13 run.py 3000            # balanced mirror aggregate (symmetry check)
py -3.13 run.py matrix 2000     # policy matrix: balanced / runner / hunter
py -3.13 run.py lonerunner 4000 # the degeneracy test
py -3.13 run.py deployables 3000 # crew-integration: does an Autoturret break Take-a-Hold?
py -3.13 run.py roofs 3000     # 2.5D verticality: does roof-camping dominate?
py -3.13 run.py sweep 3000     # sensitivity: at what height bonus do roofs tip to dominant?
py -3.13 viz.py 5               # render one game -> replay.html (steppable SVG battle map)
```

## 2.5D elevation (layered levels)
Units carry a `z` (feet elevation); terrain carries a `height`. LOS is **see-over**
(`has_los_3d`) — a rooftop shooter clears a building whose top is below the sight line;
a ground shooter is blocked by it. **Height advantage** (2"+ above) ignores Light cover
(`cover_level_3d`); a piece only covers a target it rises above (so a rooftop model gets
no cover from the building it stands on). Units take a roof via its no-test stair/ladder
(`ascend`), and a fighter shoved off a ledge **falls** (6"+ = an Injury). This is layered
2.5D — discrete levels, matching how the tabletop actually plays — not continuous voxels.

## Visualization
`viz.py` records a game and writes a **self-contained `replay.html`** — an SVG tactical
map you step round-by-round: unit positions, casualties (×), the turret, live VP, and
objectives that glow for whoever holds them. No dependencies; open it in any browser.
This is the layer that turns the sim from a number-printer into a watchable game.

## Architecture
| File | Owns |
|---|---|
| `data.py` | **Single source of truth** — ranks, weapons, armour, costs (matched to the vault). |
| `board.py` | Geometry — distance, movement, **true LOS**, **geometric cover**, and the **mirror-symmetric** Take-a-Hold board. |
| `engine.py` | Unit state, the faithful core resolution, the activation loop, hold/contest **scoring**, and the primitives policies compose (shoot / fight / move / stare-down / orders). |
| `policies.py` | **Swappable AI** — `balanced` (fight for objectives), `runner` (rush objectives, never fight), `hunter` (ignore objectives, kill everything). |
| `crews.py` | The 100-pt "Redline" crew + the lone-runner variant. |
| `run.py` | CLI: one game, aggregate, policy matrix, degeneracy test (all with **side-swapping**). |

## Wired skills
Applied by the engine because they change who holds an objective:
- **Knockback** — winning melee shoves the loser 2" (can break a hold / a contest).
- **Stare Down** — an Action: opposed NRV → +1 Stress + **Cowed** (−1 on the target's next Break test).
- **Keep Moving** — the Leader's Order repositions a stranded ally toward its objective.

Stubbed (no effect in the simplified Take-a-Hold — no terminals / Hidden / claim-Action):
Hacker, Sharp Eyes, Quick Hands, Ready to React (overwatch is already engine-wide).

## Findings (2026-07-17)
**Objective-primary is robust — the vision's "conflict inevitable, killing optional" holds.**
Policy matrix (win %, sides swapped, 2000 games/cell):

| row \ col | balanced | runner | hunter |
|---|--:|--:|--:|
| **balanced** | 49 | **100** | **60** |
| **runner** | 0 | 50 | 2 |
| **hunter** | 41 | 98 | 50 |

- A crew that **only rushes objectives and never fights loses 100%** — it gets shot off every marker.
- A crew that **only kills and ignores objectives (hunter) loses to balanced, 41 vs 60** — killing isn't the win; you must stand on the point.
- A **lone runner** (5 fight + 1 pure rusher) is a **slight net negative** (44.7% vs 49.2%): more VP (3.3 vs 2.7) but a fighter short — a real trade-off, not an exploit.

**Deployables are strong-but-fair.** An Autoturret crew (97 pt, funded by dropping the Molotov + Breach Kit) vs the plain crew (98 pt), 3000 games, sides swapped: **turret 50.8% / plain 43.0%**. The turret improves objective-holding (VP 3.0 vs 2.7) but the crew fields weaker bodies (survivors 2.1 vs 2.6). A worthwhile pick that pays its way — nowhere near the >70% that would flag a nerf.

**Roof-camping is high-risk/high-reward, not dominant.** Roof crew (ranged units seize the objective rooftops) vs ground crew, 3000 games, sides swapped: **roof 48.9% / ground 44.2%**. The height advantage boosts objective control and firepower (**VP 4.1 vs 2.5**) but rooftop exposure gets fighters killed (**survivors 1.5 vs 3.2**) — a high-variance trade-off, only a ~5-pt net edge.

**The height-COVER rule barely matters — the driver is LOS, and it's self-balancing.** Sensitivity sweep of the height-advantage strength (3000 games each): win% is **flat across the whole range** — none 49.1% · ignore-Light (RAW) 48.9% · −1 any cover 50.6% · −2 any cover 51.0%. So the *"watch for roof-camping"* worry is aimed at the wrong lever: the cover bonus is nearly irrelevant; roofs are strong because of **see-over LOS + objective control**, and that nets to ~even via exposure. **You can tune the height-cover bonus freely (even −2) without breaking balance.** Roof also *beats* pure aggression (vs Hunter **55% / 36%** — camping out-shoots the chargers) and crushes Runner (100%).

## Validated / caveat
- **Combat is symmetric** — the pure-combat Hunter mirror is 50/50 (side 0 = side 1), so the core loop, LOS, cover and morale carry no side bias.
- **Known residual (localized):** the *balanced* mirror shows a ~6-pt side-0 edge (equal VP + equal survivors, but side 0 wins slightly more). Bisected: it vanishes with Orders off *or* skills off, and appears only when the **`keep_moving` Order repositions an ally onto an objective** — an activation-order × last-word-scoring interaction, not a resolution bug. **Side-swapping cancels it in every comparative test** (matrix / lonerunner / deployables), so all findings stand. It may be a real statement about how Priority trades against grabbing objectives at the buzzer — flagged, not yet resolved.

## Deployables (Phase 3, partial)
`Autoturret` / `sniper_turret` / `burst_turret` are in `data.py`; the **Autoturret** is
fully wired — deploy via INT test (Build modifier, nat-1 backfire), auto-fire once/round
on enemy movement in range+LOS, WND 1 / Armour −2, killable by return fire (the
counterplay). Still to wire: **mines, traps, beacons, and hacker hijack** (Turret Tamer /
Rewrite Killbox).

## Stubbed (next modules)
Mines / traps / beacons · hacking (terminals + turret hijack) · terrain-interaction /
infrastructure · movement collision (models pass through pieces) · voluntary bottling ·
Down→Stabilize/bleed-out.

## Roadmap
- **Phase 3 done:** pluggable policies + the degeneracy test; the Autoturret module + the
  crew-integration finding; the side-residual localized.
- **Phase 3 remaining:** the rest of the deployables (mines/beacons) + hacking hijack;
  **generate `data.py` from the vault** so the sim tracks rule changes automatically; an
  instrumentation/regression dashboard; and root-cause the objective-scoring residual.

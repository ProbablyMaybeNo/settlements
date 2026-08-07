# Settlements — Tabletop Simulator

A playable Take-a-Hold table plus a Lua rules layer. **No custom assets** — every
object is a TTS built-in, so there is nothing to host, nothing to 404, and the
save loads offline. Your OpenSCAD/STL terrain in `../Terrain/` is the v2 upgrade.

| File | What it is |
|---|---|
| `build_table.py` | Generates `Settlements.json` (the TTS save) from `engine2d/board.py`'s validated board |
| `Global.lua` | The rules layer — core test, morale, End Phase, objective scoring, density check |
| `tts_api.py` | Live connection to a running TTS over its External Editor API |

## Install

```
py -3.13 build_table.py            # writes straight into the TTS Saves folder
```

Launch TTS at least once first — it builds `Documents/My Games/Tabletop Simulator/`
on first run, and the script installs into `Saves/` only if that exists (otherwise
it writes next to itself and tells you). Then in TTS: **Create → Singleplayer →
Load → Settlements**.

## Live connection

TTS listens on `127.0.0.1:39999` and pushes back on `39998` while the game is
running — the same channel the VS Code/Atom TTS plugins use.

```
py -3.13 tts_api.py ping                     is it listening + does it round-trip
py -3.13 tts_api.py push                     send Global.lua (Save & Play)
py -3.13 tts_api.py exec "print(#getAllObjects())"
py -3.13 tts_api.py listen 30                watch TTS print/error output
```

This is **script-level**: it pushes and runs Lua and reads what TTS prints. It
cannot move objects or click menus. `push` uses Save & Play, which **reloads the
open table** — save any hand-placed work first.

## The table

Generated from `engine2d/board.py take_a_hold()`, so the physical board is the one
~6M simulated games were measured on: three objective buildings on the centreline
with 4" roofs you can perch on, and a **mirror-symmetric** pair set so both
deployments face identical ground.

- **11 large terrain features** — inside the sacred 9–12 band, all nine 12" squares occupied
- 6" deployment bands, ~24" apart
- 3 objectives, held at 3"
- Two 4-model Campaign-Start crews, pre-enrolled with legal §13 stat lines
- Condition token supply (copy/paste for more) and two d10s

Heights are real, because the engine is 2.5D: a rooftop shooter sees over a
building that blocks a ground shooter, and height advantage ignores Light cover.

## Commands

Hover a model, type in chat. `!help` lists them.

| | |
|---|---|
| `!enrol <name> S A D I N [W]` | make any object a unit |
| `!test <stat> [mods]` | the core test — 1d10+Stat+Mods vs 7+, nat 1/10 honoured |
| `!shoot [cover]` | DEX test, cover 0/1/2/3 → 0/−1/−2/−3 |
| `!melee` | select two models: opposed STR, ties to the defender |
| `!injury <dmg> [armour]` | 1d10 + Damage − Armour vs 7+ |
| `!stress <+n\|-n>` · `!cond <name>` | Stress and condition tokens |
| `!break` · `!endphase` | one Break test, or the whole End Phase in order |
| `!priority` · `!round` | priority with the underdog +1; round counter |
| `!density` | the 9–12 band **and** the nine-square check |
| `!score` | objective hold/contest right now |

### What it automates, and what it deliberately does not

It automates the bookkeeping that gets fumbled: the natural-1/natural-10 override
(which is not just `d+mod>=7`), Shaken's −1 **not** double-applying to Break tests,
the +1 Stress for a first condition **not** double-counting with Pinned's own, the
End Phase running in the right order, and the density band.

It does not move models, choose targets, or enforce legality. Players still play.

## Two things to calibrate on first load

1. **`INCH` in both files (currently 1.0).** TTS units per game inch. 1:1 is the
   wargaming convention but it is the one value that cannot be checked without
   loading — measure a known 6" gap with the in-game ruler; if it reads wrong,
   change only that constant and regenerate.
2. **Object heights** (`BASE_Y = 1.0`). If terrain floats or sinks, that constant
   is the fix.

`tts_api.py`'s message IDs are transcribed from the documented API and have not
yet been checked against a live build here — `ping` is the two-minute test, and a
mismatch surfaces there rather than silently.

## v2

- Convert `../Terrain/*.stl` (boom gate, spike crusher, prison cell, ranch
  house/garage, barricades) to `.obj` and swap them in for the blocks. They map
  onto Infrastructure verbs directly: the boom gate **is** Open/Close Path, the
  spike crusher **is** CRUSH.
- The 12"×36" settlement canvas as a second table, with live square/Power counters.
- Assets need hosting for multiplayer; local paths work for the host only.

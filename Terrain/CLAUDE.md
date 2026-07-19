# CLAUDE.md — Settlements Interactive Terrain

OpenSCAD-based parametric terrain for **Settlements** (28mm modern American civil war wargame).
Every piece here features a working mechanism: rotation, sliding, winching, or state-swap.

## Environment
- OpenSCAD path: `C:\Program Files\OpenSCAD\openscad.exe` (v2021.01, verified installed)
- Render preview: `& "C:\Program Files\OpenSCAD\openscad.exe" --render -o <name>.png --imgsize=1200,900 --autocenter --viewall <name>.scad`
- Export STL:     `& "C:\Program Files\OpenSCAD\openscad.exe" --render -o <name>.stl <name>.scad`
- **Always render a PNG and visually inspect it before exporting an STL.** Iterate on the preview, not the print.

### Running OpenSCAD from an agent session (verified 2026-07-19)
`openscad.exe` writes its status to **stderr** and returns nothing useful from a
bare call. Capture it like this or you will see empty output and assume failure:
```powershell
$p = Start-Process -FilePath "C:\Program Files\OpenSCAD\openscad.exe" `
     -ArgumentList @('--render','-o','out.png','--imgsize=1200,900',
                     '--autocenter','--viewall','part.scad') `
     -RedirectStandardError "$env:TEMP\o.err" -NoNewWindow -Wait -PassThru
Get-Content "$env:TEMP\o.err"
```
- Passing a **string** via `-D` needs escaped quotes: `'-D','show=\"layout\"'`.
  Unescaped, OpenSCAD warns `Ignoring unknown variable` and silently falls
  through to the `else` branch.
- In the stderr summary, **`Volumes:` counts the parts PLUS one** (CGAL includes
  the unbounded outer volume). 5 printable parts reports `Volumes: 6`.
  `Simple: yes` means manifold — this is the check that matters before export.

### Verify clearances geometrically, not by eye
Perspective renders WILL lie to you about whether a swinging part fouls the
base. Do not judge collisions from a 3/4 view. Instead intersect the moving part
(translated to its real mounted height) with the half-space below the tabletop
and check whether the result is empty — see `_clearance_test.scad`.
Two traps that cost time once already:
- `use <file.scad>` imports modules but **NOT variables** — every parameter comes
  through as `undef`. Use `include <file.scad>` for test harnesses, and guard the
  parent's top-level call with `render_top`.
- Remember to `translate([0,0,pivot_h])` the moving part before testing. A hub
  centred on its own origin straddles z=0 and reports a false collision at every
  angle (the tell: identical facet count regardless of rotation).

## THE WIRE-AXLE STANDARD (non-negotiable)
We do NOT design print-in-place hinges or printed pins. All rotating joints are
**printed holes + metal wire axles** supplied by the builder.

| Wire stock | Diameter | Use for |
|---|---|---|
| Paperclip | 1.0mm | Doors, hatches, small flaps, light gates |
| Floral wire | ~0.9mm | Tiny/decorative articulation |
| 1/16" brass rod | 1.6mm | Load-bearing: rollers, bridge spans, cranes, boom gates |

**Hole sizing rules:**
- FREE-SPIN hole = wire diameter + **0.35–0.4mm** (e.g., 1.4mm hole for a paperclip)
- FRICTION/POSE hole = wire diameter + **0.1mm** (joint holds its position but moves by hand)
- PRESS-FIT hole (cranks, fixed hubs) = wire diameter + **0.05mm** (glue if loose)
- For any mechanism that must HOLD a position (raised boom gate, angled searchlight):
  make ONE side of the joint a friction hole, the rest free-spin.
- Model all holes as simple cylinders. If a print comes out tight, the fix is a
  hand-twisted drill bit, not a reprint.

**Retention:** bend one wire end 90°, add a printed press-fit end cap, or a dab of
superglue on the OUTER face only. Never glue inside the joint.

## Other mechanism patterns
- **Sliding** (portcullis, drop-ladders, catwalks): printed channel + printed slider,
  0.5mm clearance per side, gravity-friendly orientation.
- **Winch** (drawbridge lift, cruncher cage): brass rod axle doubles as the winch
  drum; wrap sewing thread around it. Add a simple crank (press-fit hub).
- **State-swap** (pit reveal, damage states): keyed tiles or 3mm x 2mm disc magnets.
  No moving parts needed.

## Modeling conventions
- One part = one module. Provide an `assembly()` preview module showing everything
  together (include the wire as a `color("gold")` reference cylinder — NOT exported geometry... 
  actually it will export; keep reference rods in assembly() only and export part
  modules individually, or comment the rod out before STL export).
- Print layout: lay parts flat and separated in the default top-level layout so a
  single STL export is sliceable. Doors/flaps lie flat beside their bodies.
- Avoid exact-tangent surfaces (bars touching rails at a single point) — overlap
  intersecting geometry by 0.1–0.5mm to prevent non-manifold warnings.
- `$fn = 24` for small cylinders, 32+ for visible rollers/wheels. Don't go above 64.
- All key dimensions as named parameters at the top under `/* [Section] */` headers
  (enables the OpenSCAD Customizer).
- Scale target: 28mm heroic. Door openings ≥ 25mm tall, walkable catwalks ≥ 25mm wide,
  floors/bases 2–3mm thick, walls ≥ 2mm, bars ≥ 2mm diameter for FDM strength.

## Reference files in this folder
- `spike_crusher.scad` — THE PATTERN for rotating hazards: A-frame stands (free-spin),
  spiked roller (free-spin), crank (press-fit) on a 1.6mm brass rod.
- `prison_cell.scad` — THE PATTERN for hinged doors: knuckle hinges on a 1.0mm
  paperclip. Known issues to fix before printing: knuckle alignment between door
  and body needs a pass; non-manifold warnings from bar/rail tangents.

## Build queue (from the interactive-terrain master list gap analysis)
Tier 1 — signature pieces (no commercial product exists):
1. ~~Checkpoint boom gate (counterweighted arm, friction pivot)~~ — STL exported
   2026-07-19, `checkpoint_boom_gate.scad`. Awaiting first test print.
   Rod is keyed press-fit to the arm hub; drag is taken on ONE post upright.
   Counterweight is deliberately short-tailed so it never fouls the base
   (verified clear 0–90°). Arm is under-balanced on purpose = fails closed.
2. Storm cellar bulkhead doors (twin hinged flaps) ← NEXT
3. Fire escape with sliding drop-ladder (channel + slider)
4. Grain elevator with raising auger arm (friction pivot)
5. Center-pivot irrigation arm (free-spin base bearing, sweeps the field)
6. Highway drawspan bridge (brass rod hinge + thread winch)
Tier 2: covered pit swap-tiles, sliding catwalk, bunker gun-shield flap,
manhole/sewer network, dock leveler (ratchet height stops).

## Workflow per piece
1. Write/modify `.scad` → 2. Render PNG → 3. Inspect the image → 4. Fix → repeat
5. Export STL → 6. USER test-prints and reports fit → 7. Adjust parameters → re-export.
First print of any new joint type: print just the joint region as a small test coupon.

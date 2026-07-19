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

### READ THE FULL STDERR. Never grep it down to Simple/Volumes.
CGAL can fail an operation and **silently return the first operand**. A
`difference()` then appears to do nothing, `Simple: yes` still prints, and the
only clue is a line you filtered out:
```
ERROR: The given mesh is not closed! Unable to convert to CGAL_Nef_Polyhedron.
```
This cost six wasted renders on 2026-07-19. The trigger was a 2D pattern whose
pieces met at **exact tangents** (brick perpends ending precisely where the next
bed joint began), which extrudes to a non-closed mesh. Same root cause as the
overlap rule above — overlap every intersecting piece by ~0.1mm.
Cheap tell: an implausibly fast render plus a facet count equal to the bare
uncut solid (a plain cube reports `Facets: 6`).

### Surface texture cost (measured, 200x90 panel, OpenSCAD 2021.01)
| approach | time | use |
|---|---|---|
| one 3D box per brick (~1400 booleans) | >86s, never finished | never |
| 2D pattern, `linear_extrude`d once | 26.7s | brick / stone |
| horizontal grooves only (~22 boxes) | 1.1s | siding, boards, panelling |
Build patterns in 2D and extrude ONCE. See `house_texture.scad`.

### Texture must suit the nozzle
A groove narrower than the nozzle will smear or vanish. On a 0.4mm nozzle keep
grooves **>= 0.8mm wide and >= 0.4mm deep**. Real brick at 1:56 is ~1mm courses,
which is unprintable, so masonry must be exaggerated. Larger units (cut stone at
11 x 5mm) carry wider joints and print far more reliably than brick.
`texture_swatches.scad` prints all six finishes on one plate - print it and
choose before texturing a whole building.

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
- `prison_cell.scad` — knuckle hinges on a 1.0mm paperclip. BROKEN, do not copy:
  the door carries one knuckle at its BOTTOM while the body carries two at top
  and bottom, so they never interleave and no wire can thread all three.
  Confirmed 2026-07-19. Use the pin hinge in `ranch_house.scad` instead.
- `ranch_house.scad` — THE PATTERN for buildings: removable roof, interior
  rooms, three working doors. Three reusable techniques:
  * **Vertical PIN hinge** (front/back doors) — the door has a full-height tube
    on its hinge edge; a 1.0mm wire goes up through the floor, through the tube
    (friction bore), into a blind hole in the lintel. Preferred over knuckle
    hinges at this scale: a knuckle small enough to fit ends up SMALLER than the
    clearance notch it needs, leaving the frame barrel unattached — that is
    exactly how prison_cell failed. A pin hinge is integral to the wall.
  * **Tilt-up door** (garage) — hinge tube along the top edge on brass rod.
    Watch the rotation axis: a tube built along X must rotate about X.
  * **Removable roof** — pegs stand UP on the wall tops and engage sockets in a
    flat bearing ledge inside the roof. Do NOT use a lip hanging down off the
    roof: it forces the roof to print resting on a thin ring, and it collides
    with any interior wall it isn't explicitly notched around.

### Roof modelling notes (learned the hard way)
- To hollow a gable, the inner cutter must be the outer profile **shifted
  straight DOWN**, not `offset()` inward. `offset()` insets all three edges, so
  the bottom never opens and you silently get a closed slab. Check by cutting a
  thin section and viewing it as an ortho side elevation.
- Print the roof **ridge up**, sitting on its ledge. At a 32° pitch the shell
  tapers inward with ~91% layer overlap, so it is fully self-supporting.
  Do not invert it (balances on the ridge) and do not lay a half on its slope
  (the bearing ledge sits 7.5mm below the slope plane, so it rests on a line).

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

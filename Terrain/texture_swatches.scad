// ============================================================
// TEXTURE SWATCHES - print this one plate first, then decide.
// Six 52 x 44mm panels, 4mm thick, on a common backing strip.
// Print it standing UP (as modelled) so the panels are vertical walls,
// exactly as they will be on the house. Judging a texture printed flat
// on the bed tells you nothing useful.
// ============================================================

include <house_texture.scad>

pw = 52;    // panel width
ph = 44;    // panel height
pt = 4;     // panel thickness
gap = 4;
base_t = 3;

// label bar height at the bottom of each panel (left smooth for a marker)
label_h = 7;

kinds = [
    ["brick",  "fine 0.6mm joints - marginal on a 0.4mm nozzle"],
    ["brickC", "coarse 0.9mm joints - printable brick"],
    ["stone",  "cut stone block - easiest masonry"],
    ["siding", "horizontal lap siding - very forgiving"],
    ["batten", "board and batten - zero overhang"],
    ["smooth", "control - smooth, for fuzzy skin or paint"]
];

module panel(kind) {
    difference() {
        cube([pw, pt, ph]);
        if (kind == "brickC") {
            // coarse brick: wider joints, taller courses
            translate([0, brick_d, label_h]) rotate([90, 0, 0])
                linear_extrude(height = brick_d + 0.2)
                    union() {
                        nc = floor((ph - label_h) / 3.0);
                        nb = floor(pw / 6.5) + 1;
                        for (c = [0 : nc - 1]) {
                            translate([-1, c*3.0]) square([pw + 2, 0.9]);
                            for (b = [0 : nb])
                                translate([(c % 2)*3.25 + b*6.5, c*3.0 - ov])
                                    square([0.9, 3.0 + 2*ov]);
                        }
                    }
        } else if (kind != "smooth") {
            translate([0, 0, label_h])
                face_cut(kind, pw, ph - label_h,
                         kind == "stone" ? 0.6 : brick_d);
        }
    }
}

// backing strip so the six panels print as one handleable part
translate([-gap, 0, 0])
    cube([6*(pw + gap) + gap, pt, base_t]);

for (i = [0 : len(kinds) - 1])
    translate([i*(pw + gap), 0, 0]) panel(kinds[i][0]);

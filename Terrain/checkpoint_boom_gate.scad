// ============================================================
// CHECKPOINT BOOM GATE - 28mm modern checkpoint terrain
// Build queue item 1. Counterweighted arm on a friction pivot.
//
// WIRE-AXLE STANDARD (1/16" brass rod, 1.6mm - load bearing):
//   boom hub      = PRESS fit (rod + 0.05)  -> rod turns WITH the arm
//   post upright A= FRICTION  (rod + 0.10)  -> the drag that holds position
//   post upright B= FREE SPIN (rod + 0.40)  -> alignment only
// Rationale: CLAUDE.md calls for one friction surface and the rest free.
// Because the boom must hold ANY angle, the rod is keyed to the arm and
// the drag is taken on a single post upright. Counterweight brings the
// arm close to balance so only light friction is needed, with a slight
// fall-closed bias (fail-safe: gate defaults shut).
//
// Parts: 1x post, 1x boom arm (with counterweight), 1x rest post,
//        2x end cap   + one 20mm length of 1.6mm brass rod
// ============================================================

/* [Show] */
// "assembly" to inspect, "layout" to export a printable STL
show = "assembly";  // [assembly, layout]
// preview angle of the raised arm (degrees) - preview only, not printed
open_angle = 35;    // [0:90]

/* [Wire Axle Standard] */
rod_d       = 1.6;              // 1/16" brass rod
press_hole  = rod_d + 0.05;     // boom hub - rod keyed to arm
friction_hole = rod_d + 0.10;   // post upright A - holds position
spin_hole   = rod_d + 0.40;     // post upright B - free
rod_len     = 20;               // brass rod the builder cuts

/* [Boom Arm] */
arm_len     = 105;              // reach forward of the pivot
arm_w       = 6;                // across the road (Y)
arm_h       = 5;                // vertical section (Z)
tail_len    = 8;                // pivot to counterweight (short: keeps the
                                // block inside the post's swing radius so it
                                // never fouls the base plate when raised)
hub_d       = 11;
stripe_pitch = 12;              // hazard stripe grooves
stripe_w    = 2.0;
stripe_deep = 0.6;

/* [Counterweight] */
cw_l        = 16;               // along the arm (X)
cw_w        = 18;               // across (Y)
cw_h        = 18;               // vertical (Z)

/* [Post] */
pivot_h     = 30;               // axle height above the base top
post_t      = 4;                // upright plate thickness
post_w      = 14;               // upright plate width (X)
fork_clear  = 0.5;              // per side, arm inside the fork
base_l      = 34;
base_w      = 34;
base_t      = 3;

/* [Rest Post] */
rest_x      = 88;               // distance from pivot to the rest cradle
rest_w      = 10;
rest_t      = 6;
cradle_d    = 9;                // U notch the arm drops into

/* [End Cap] */
cap_d       = 5;
cap_t       = 2;

$fn = 32;

fork_gap = arm_w + 2*fork_clear;          // clear space between uprights
fork_off = fork_gap/2 + post_t/2;         // upright centreline offset in Y

// ---------------- boom arm ----------------
// Pivot at the origin. Arm runs +X, counterweight tail runs -X.
// Printed lying on its side (arm_w face down) - see layout().
module boom_arm() {
    difference() {
        union() {
            // main arm
            translate([0, -arm_w/2, -arm_h/2]) cube([arm_len, arm_w, arm_h]);
            // tail to the counterweight
            translate([-tail_len, -arm_w/2, -arm_h/2]) cube([tail_len, arm_w, arm_h]);
            // pivot hub (axis along Y)
            rotate([-90, 0, 0]) cylinder(d=hub_d, h=arm_w, center=true);
            // counterweight block - concrete, sits at the tail end
            translate([-tail_len - cw_l + 0.3, -cw_w/2, -cw_h/2])
                cube([cw_l, cw_w, cw_h]);
            // arm tip - slightly deeper so it seats in the cradle
            translate([arm_len - 8, -arm_w/2, -arm_h/2 - 1.5])
                cube([8, arm_w, arm_h + 1.5]);
        }
        // press-fit axle bore - rod turns with the arm
        rotate([-90, 0, 0]) cylinder(d=press_hole, h=arm_w + 10, center=true);

        // hazard stripe grooves, cut from top and both sides
        for (i = [1 : floor((arm_len - 14) / stripe_pitch)])
            translate([hub_d/2 + 2 + i*stripe_pitch - stripe_w/2, -arm_w/2 - 1,
                       arm_h/2 - stripe_deep])
                cube([stripe_w, arm_w + 2, stripe_deep + 1]);
        // lightening pocket in the counterweight face (cast-concrete look)
        translate([-tail_len - cw_l + 2.3, -cw_w/2 - 1, -cw_h/2 + 3])
            cube([cw_l - 4, 1.6, cw_h - 6]);
        translate([-tail_len - cw_l + 2.3, cw_w/2 - 0.6, -cw_h/2 + 3])
            cube([cw_l - 4, 1.6, cw_h - 6]);
    }
}

// ---------------- post ----------------
module upright(hole) {
    difference() {
        union() {
            // plate with a rounded top around the axle
            hull() {
                translate([-post_w/2, -post_t/2, 0]) cube([post_w, post_t, 2]);
                translate([0, 0, pivot_h]) rotate([-90, 0, 0])
                    cylinder(d=post_w, h=post_t, center=true);
            }
            // gusset back to the base
            translate([-post_w/2, -post_t/2, 0]) cube([post_w, post_t, 6]);
        }
        // axle hole
        translate([0, 0, pivot_h]) rotate([-90, 0, 0])
            cylinder(d=hole, h=post_t + 10, center=true);
    }
}

module post() {
    // base plate
    translate([-base_l/2, -base_w/2, -base_t]) cube([base_l, base_w, base_t]);
    // chamfered kerb detail around the base
    difference() {
        translate([-base_l/2, -base_w/2, -base_t]) cube([base_l, base_w, base_t + 1.2]);
        translate([-base_l/2 + 2.5, -base_w/2 + 2.5, -base_t])
            cube([base_l - 5, base_w - 5, base_t + 2]);
    }
    // upright A - FRICTION side (holds the arm position)
    translate([0,  fork_off, 0]) upright(friction_hole);
    // upright B - FREE SPIN side
    translate([0, -fork_off, 0]) upright(spin_hole);
}

// ---------------- rest post (arm drops onto this) ----------------
module rest_post() {
    // cradle floor must land exactly on the underside of the arm tip so the
    // gate physically rests closed: floor = pivot_h - arm_h/2 - tip_drop
    rest_h = pivot_h - arm_h/2 - 1.5 + cradle_d/2;
    difference() {
        union() {
            translate([-rest_w/2, -rest_t/2, -base_t])
                cube([rest_w, rest_t, base_t]);
            translate([-rest_w/2, -rest_t/2, 0]) cube([rest_w, rest_t, rest_h]);
        }
        // U-shaped cradle notch
        translate([0, 0, rest_h]) rotate([-90, 0, 0])
            cylinder(d=cradle_d, h=rest_t + 2, center=true);
        translate([-cradle_d/2, -rest_t/2 - 1, rest_h])
            cube([cradle_d, rest_t + 2, cradle_d]);
    }
}

// ---------------- end cap (press-fit rod retainer) ----------------
module end_cap() {
    difference() {
        cylinder(d=cap_d, h=cap_t);
        translate([0, 0, -0.5]) cylinder(d=press_hole, h=cap_t + 1);
    }
}

// ---------------- assembled preview ----------------
module assembly(angle = 0) {
    post();
    translate([rest_x, 0, 0]) rest_post();
    translate([0, 0, 0]) rotate([0, -angle, 0]) boom_arm();
    // brass rod - reference only, never exported
    color("gold") rotate([-90, 0, 0])
        cylinder(d=rod_d, h=rod_len, center=true);
}

// ---------------- print layout ----------------
module layout() {
    // Arm on its side. After rotate([90,0,0]) the part's Y extent becomes Z,
    // so it must be lifted by the LARGEST half-Y in the part - that is the
    // counterweight (cw_w), not the arm (arm_w). Lifting by arm_w/2 buries
    // the counterweight 6mm under the bed.
    translate([0, 0, cw_w/2]) rotate([90, 0, 0]) boom_arm();
    // post and rest post both carry their base below z=0 - lift onto the bed
    translate([0,  50, base_t]) post();
    translate([55, 50, base_t]) rest_post();
    translate([75, 50, 0]) end_cap();
    translate([85, 50, 0]) end_cap();
}

// set false when this file is `include`d by a diagnostic/test script
render_top = true;

if (render_top) {
    if (show == "assembly") assembly(open_angle);
    else layout();
}

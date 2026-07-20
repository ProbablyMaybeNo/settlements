// ============================================================
// PRISON CELL - 28mm wargame terrain
// Hinged barred door swings on a 1.0mm paperclip axle
// Wire-axle standard: hole = wire dia + 0.4mm (free spin)
// Print: cell body + door as separate parts, drop wire through
// ============================================================

/* [Wire Axle Standard] */
wire_d       = 1.0;   // paperclip
hole_d       = wire_d + 0.4;

/* [Cell Dimensions] */
cell_w       = 60;    // interior width
cell_d       = 50;    // interior depth
wall_h       = 45;    // wall height
wall_t       = 3;     // wall thickness
floor_t      = 2;

/* [Bars] */
bar_d        = 2.0;   // bar diameter (chunky for FDM strength)
bar_gap      = 6;     // clear space between bars (mini can't slip through)
frame_t      = 4;     // top/bottom rail of barred sections

/* [Door] */
door_w       = 26;
door_clear   = 0.6;   // gap around door so it swings freely
hinge_knuckle_d = 5;  // outer diameter of hinge knuckles
hinge_knuckle_h = 6;

$fn = 24;

// -------- helpers --------
module bars(width, height) {
    n = floor((width - bar_d) / (bar_d + bar_gap));
    spacing = (width - bar_d) / max(n,1);
    // top + bottom rails
    translate([0,0,0]) cube([width, wall_t, frame_t]);
    translate([0,0,height-frame_t]) cube([width, wall_t, frame_t]);
    // vertical bars
    for (i = [0:n])
        translate([bar_d/2 + i*spacing, wall_t/2, frame_t-0.5])
            cylinder(d=bar_d, h=height - 2*frame_t + 1);
}

module hinge_knuckle() {
    difference() {
        cylinder(d=hinge_knuckle_d, h=hinge_knuckle_h);
        translate([0,0,-0.5]) cylinder(d=hole_d, h=hinge_knuckle_h+1);
    }
}

// -------- cell body --------
module cell_body() {
    // floor
    translate([-wall_t, -wall_t, 0])
        cube([cell_w + 2*wall_t, cell_d + 2*wall_t, floor_t]);
    // back wall (solid)
    translate([-wall_t, cell_d, floor_t])
        cube([cell_w + 2*wall_t, wall_t, wall_h]);
    // side walls (solid)
    translate([-wall_t, 0, floor_t]) cube([wall_t, cell_d + wall_t, wall_h]);
    translate([cell_w, 0, floor_t])  cube([wall_t, cell_d + wall_t, wall_h]);
    // front: barred section left of the door opening
    front_bar_w = cell_w - door_w - 2*door_clear;
    translate([0, -wall_t + (wall_t - wall_t)/2, floor_t])
        translate([0, 0, 0]) bars_front(front_bar_w);
    // door frame post at the opening edge
    translate([front_bar_w, -wall_t, floor_t])
        cube([3, wall_t, wall_h]);
    // body-side hinge knuckles (top & bottom) on the right edge of opening
    hx = cell_w + wall_t - hinge_knuckle_d/2;
    translate([hx, -wall_t/2, floor_t + 2])            hinge_knuckle();
    translate([hx, -wall_t/2, floor_t + wall_h - 2 - hinge_knuckle_h]) hinge_knuckle();
}

module bars_front(width) {
    translate([0, -wall_t, 0]) bars(width, wall_h);
}

// -------- door (print separately, lies flat) --------
module door() {
    difference() {
        union() {
            bars(door_w, wall_h);
            // hinge-side stile
            translate([door_w - 3, 0, 0]) cube([3, wall_t, wall_h]);
            // door-side hinge knuckle (middle - meshes between body knuckles)
            translate([door_w + hinge_knuckle_d/2 - 0.5, wall_t/2, 0]) {
                translate([0,0, 2 + hinge_knuckle_h + 0.5]) hinge_knuckle();
                // arm connecting knuckle to door
                translate([-hinge_knuckle_d/2 - 1, -wall_t/2, 2 + hinge_knuckle_h + 0.5])
                    cube([hinge_knuckle_d/2 + 1, wall_t, hinge_knuckle_h]);
            }
        }
    }
}

// -------- layout --------
cell_body();
translate([cell_w + 25, 0, 0]) door();   // door beside body for printing

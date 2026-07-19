// ============================================================
// HOUSE TEXTURE LIBRARY - shared surface patterns and damage
// Used by ranch_house.scad. Nothing here is a printable part.
//
// CRITICAL LESSON (cost ~6 wasted renders, 2026-07-19):
// A 2D pattern whose pieces meet at EXACT tangents extrudes into a
// non-closed mesh. CGAL then refuses it with
//     "ERROR: The given mesh is not closed!"
// and SILENTLY returns the first operand - so difference() appears to do
// nothing and you get a bare wall with no error in the filtered output.
// Every pattern below deliberately OVERLAPS its pieces by ov (0.1mm).
// Never let a perpend end exactly where a bed joint begins.
// Always read the FULL stderr, not just the Simple/Volumes lines.
//
// COST (measured on a 200x90 panel, OpenSCAD 2021.01):
//   per-brick 3D boxes ...... >86s, never completed   DO NOT USE
//   2D pattern, extruded once  26.7s, 11649 facets    <- brick
//   horizontal grooves only .. 1.1s                   <- siding / boards
// ============================================================

ov = 0.1;   // mandatory overlap - see note above

/* [Brick] */
// Real brick at 1:56 would be ~1mm courses, below what a 0.4mm nozzle can
// resolve. These are deliberately exaggerated so drybrushing catches them.
course_h  = 2.5;
brick_l   = 5.5;
joint_w   = 0.6;
brick_d   = 0.5;   // mortar groove depth

/* [Siding / boards] */
siding_pitch = 4.0;
siding_w     = 0.7;
siding_d     = 0.5;
board_pitch  = 8.0;
board_w      = 0.6;
board_d      = 0.4;

/* [Damage] */
crater_r     = 1.6;
crater_stand = 0.9;   // sphere centre stands this far off the face
                      // -> cut depth = crater_r - crater_stand = 0.7mm,
                      //    leaving 2.3mm of a 3mm wall
through_d    = 1.8;

// ---------- 2D patterns (u = along the wall, v = up) ----------
module brick2d(w, h) {
    nc = floor(h / course_h);
    nb = floor(w / brick_l) + 1;
    union() {
        for (c = [0 : nc - 1]) {
            // bed joint
            translate([-1, c*course_h]) square([w + 2, joint_w]);
            // perpends - overlap the bed joints above and below
            for (b = [0 : nb])
                translate([(c % 2) * brick_l/2 + b*brick_l, c*course_h - ov])
                    square([joint_w, course_h + 2*ov]);
        }
    }
}

module siding2d(w, h) {
    n = floor(h / siding_pitch);
    union() for (i = [0 : n])
        translate([-1, i*siding_pitch]) square([w + 2, siding_w]);
}

// Cut stone block - bigger units than brick, so the joints can be wider and
// still look right. Much friendlier to a 0.4mm nozzle. (Reference photo 2.)
stone_h    = 5.0;
stone_l    = 11.0;
stone_joint = 0.9;

module stone2d(w, h) {
    nc = floor(h / stone_h);
    nb = floor(w / stone_l) + 1;
    union() {
        for (c = [0 : nc - 1]) {
            translate([-1, c*stone_h]) square([w + 2, stone_joint]);
            for (b = [0 : nb])
                translate([(c % 2) * stone_l/2 + b*stone_l, c*stone_h - ov])
                    square([stone_joint, stone_h + 2*ov]);
        }
    }
}

// Board and batten - raised vertical battens. Vertical features on a vertical
// wall have zero overhang, so this is the most forgiving pattern of all.
module batten2d(w, h) {
    n = floor(w / board_pitch);
    union() for (i = [0 : n])
        translate([i*board_pitch, -1]) square([1.6, h + 2]);
}

module boards2d(w, h) {
    n = floor(w / board_pitch);
    union() for (i = [0 : n])
        translate([i*board_pitch, -1]) square([board_w, h + 2]);
}

// ---------- face cutter ----------
// Local frame: u along +X, v along +Z, face plane at y=0, material at +Y.
module face_cut(kind, w, h, depth) {
    translate([0, depth, 0]) rotate([90, 0, 0])
        linear_extrude(height = depth + 0.2) {
            if      (kind == "brick")  brick2d(w, h);
            else if (kind == "stone")  stone2d(w, h);
            else if (kind == "siding") siding2d(w, h);
            else if (kind == "batten") batten2d(w, h);
            else                       boards2d(w, h);
        }
}

// ---------- damage ----------
module crater(u, v) {
    translate([u, -crater_stand, v]) sphere(r = crater_r);
    // slight spall ring so it does not read as a clean dimple
    translate([u, -crater_stand - 0.4, v]) sphere(r = crater_r * 0.72);
}

module through_hole(u, v, thick) {
    translate([u, -2, v]) rotate([-90, 0, 0])
        cylinder(d = through_d, h = thick + 4);
}

// ---------- opening trim ----------
// Casing around an opening, optional projecting sill and flanking shutters.
module opening_trim(u0, v0, w, h, case_w, proud, sill, shutters, shutter_w) {
    // casing
    difference() {
        translate([u0 - case_w, -proud, v0 - case_w])
            cube([w + 2*case_w, proud + ov, h + 2*case_w]);
        translate([u0, -proud - 1, v0]) cube([w, proud + 3, h]);
    }
    // sill
    if (sill)
        translate([u0 - case_w - 1, -proud - 0.8, v0 - case_w - 2])
            cube([w + 2*case_w + 2, proud + 0.8 + ov, 2.2]);
    // shutters
    if (shutters)
        for (sx = [u0 - case_w - shutter_w - 0.6, u0 + w + case_w + 0.6])
            translate([sx, -proud + 0.2, v0 - case_w + 0.5])
                cube([shutter_w, proud - 0.2 + ov, h + 2*case_w - 1]);
}

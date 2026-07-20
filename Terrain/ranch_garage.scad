// ============================================================
// DETACHED 2-CAR GARAGE - companion to ranch_house.scad
//
// Split out of the house so the house gets the full plate width. Because it
// is now its own print, it can have the FRONT-FACING GABLE from the
// reference photo - the ridge runs front-to-back here, perpendicular to the
// house ridge. That was impractical while it was part of the house body,
// since it would have made the main roof a two-piece part.
//
// Butts against the right-hand wall of the house. Two pegs on this side wall
// drop into sockets in the house, so the house has nothing protruding.
// Depth and wall height match the house exactly so the eaves line up.
//
// MECHANISM: tilt-up garage door, hinge tube along the top edge on a 1.6mm
// brass rod. Tube = PRESS (rod turns with the door), left jamb = FRICTION
// (holds it open), right jamb = FREE.
//
// Parts: body, roof, garage door.  Hardware: 1.6mm brass rod ~80mm.
// ============================================================

include <house_texture.scad>

/* [Show] */
show = "assembly";   // assembly | plate | body | roof
texture = true;
open_garage = 0;     // [0:85]

/* [Wire Axle Standard] */
rod_d        = 1.6;
rod_press    = rod_d + 0.05;
rod_friction = rod_d + 0.10;
rod_free     = rod_d + 0.40;

/* [Overall] - depth and wall height MUST match ranch_house.scad */
gar_w   = 95;
gar_d   = 112;
wall_h  = 52;
wall_t  = 3;
floor_t = 3;

/* [Roof] - ridge runs along Y, gable faces the front */
roof_oh   = 10;
roof_rise = 30;
roof_t    = 2.5;
fascia_h  = 3;
ledge_w   = 8;
ledge_t   = 4;
peg_d     = 3;
peg_h     = 3;
shingles     = true;
shingle_n    = 14;
shingle_step = 0.45;

/* [Garage door] */
gd_x0 = 14;
gd_w  = 66;
gd_h  = 40;
gd_t  = 2.2;
gd_tube_d = 4;

/* [Link to house] */
link_y  = [30, 100];
link_z  = 26;
link_d  = 4;
link_len = 2.5;

/* [Side opening to the house] */
side_y0 = 70;
side_w  = 26;
side_h  = 40;

/* [Windows] */
win_sill = 18;
win_h    = 24;

$fn = 24;

ix0 = wall_t;  ix1 = gar_w - wall_t;
iy0 = wall_t;  iy1 = gar_d - wall_t;
ftop = floor_t;
wtop = floor_t + wall_h;

gd_dw = gd_w - 1.0;
gd_dh = gd_h - gd_tube_d/2 - 1.0;

peg_pos = [[wall_t/2, 22], [gar_w - wall_t/2, 22],
           [wall_t/2, 92], [gar_w - wall_t/2, 92]];

batten_proud = 0.8;
batten_w     = 1.6;
case_w = 2.0;
proud  = 1.2;

// ---- face frame: u along +X, v along +Z, face at y=0, material +Y ----
module on_face(f) {
    if      (f == 0) children();
    else if (f == 1) translate([gar_w, gar_d, 0]) rotate([0,0,180]) children();
    else if (f == 2) translate([0, gar_d, 0]) rotate([0,0,-90]) children();
    else             translate([gar_w, 0, 0]) rotate([0,0,90]) children();
}
function face_w(f) = (f == 0 || f == 1) ? gar_w : gar_d;
function fy(gy, w) = gar_d - gy - w;

module on_inner(f) {
    if      (f == 0) translate([gar_w, wall_t, 0]) rotate([0,0,180]) children();
    else if (f == 1) translate([0, gar_d - wall_t, 0]) children();
    else if (f == 2) translate([wall_t, 0, 0]) rotate([0,0,90]) children();
    else             translate([gar_w - wall_t, gar_d, 0]) rotate([0,0,-90]) children();
}

// ============================================================
// OPENINGS
// ============================================================
module openings() {
    zs = ftop + win_sill;
    // garage door
    translate([gd_x0, -1, ftop]) cube([gd_w, wall_t + 2, gd_h]);
    gz = ftop + gd_h - gd_tube_d/2;
    // left jamb FRICTION (holds the door open), right jamb FREE
    translate([gd_x0 - 8, wall_t/2, gz]) rotate([0,90,0])
        cylinder(d = rod_friction, h = 8.5);
    translate([gd_x0 + gd_w - 0.5, wall_t/2, gz]) rotate([0,90,0])
        cylinder(d = rod_free, h = 9);
    // side opening through to the house (no door - the house carries it)
    translate([-1, side_y0, ftop]) cube([wall_t + 2, side_w, side_h]);
    // rear window and side window
    translate([30, gar_d - wall_t - 1, zs]) cube([34, wall_t + 2, win_h]);
    translate([gar_w - wall_t - 1, 40, zs]) cube([wall_t + 2, 30, win_h]);
    // alignment pegs are additive; nothing to cut here
}

// ============================================================
// TEXTURE / TRIM
// ============================================================
module battens_on(w, h) {
    n = floor(w / board_pitch);
    for (i = [0 : n])
        translate([i*board_pitch, -batten_proud, ftop])
            cube([batten_w, batten_proud + ov, h]);
}
module exterior_battens() {
    for (f = [0:3]) on_face(f) battens_on(face_w(f), wall_h);
    for (c = [[0,0],[gar_w - batten_w, 0],
              [0, gar_d - batten_w],[gar_w - batten_w, gar_d - batten_w]])
        translate([c[0] - batten_proud, c[1] - batten_proud, ftop])
            cube([batten_w + 2*batten_proud, batten_w + 2*batten_proud, wall_h]);
}
module all_trim() {
    zs = ftop + win_sill;
    on_face(0) opening_trim(gd_x0, ftop, gd_w, gd_h, case_w, proud, false, false, 0);
    on_face(1) opening_trim(gar_w - 30 - 34, zs, 34, win_h, case_w, proud, true, true, 5);
    on_face(3) opening_trim(40, zs, 30, win_h, case_w, proud, true, true, 5);
}
module interior_boards() {
    for (f = [0:3]) on_inner(f)
        translate([0, 0, ftop]) face_cut("boards", face_w(f), wall_h, board_d);
}
module damage() {
    clusters = [[0, 48, 30, 22, 5], [3, 60, 32, 18, 3], [1, 50, 30, 20, 3]];
    for (ci = [0 : len(clusters)-1]) {
        cl = clusters[ci];  n = cl[4];
        ru = rands(-cl[3], cl[3], n, 17 + ci*5);
        rv = rands(-cl[3]*0.5, cl[3]*0.5, n, 63 + ci*11);
        on_face(cl[0]) for (i = [0:n-1]) crater(cl[1] + ru[i], cl[2] + rv[i]);
    }
    on_face(0) through_hole(88, 34, wall_t);
}

// ============================================================
// BODY
// ============================================================
module garage_body() {
    difference() {
        union() {
            difference() {
                cube([gar_w, gar_d, floor_t + wall_h]);
                translate([ix0, iy0, ftop]) cube([ix1 - ix0, iy1 - iy0, wall_h + 1]);
            }
            for (p = peg_pos)
                translate([p[0], p[1], wtop]) cylinder(d = peg_d, h = peg_h);
            // alignment pegs that mate with the house
            for (ly = link_y)
                translate([-link_len, ly, link_z]) rotate([0,90,0])
                    cylinder(d = link_d, h = link_len + ov);
            if (texture) { exterior_battens(); all_trim(); }
        }
        openings();
        if (texture) { interior_boards(); damage(); }
    }
}

// ============================================================
// GARAGE DOOR - tilt-up, local origin = hinge axis at the top edge
// ============================================================
module garage_door() {
    difference() {
        union() {
            rotate([0, 90, 0]) cylinder(d = gd_tube_d, h = gd_dw);
            translate([0, -gd_t/2, -gd_dh]) cube([gd_dw, gd_t, gd_dh + 1]);
        }
        translate([-1, 0, 0]) rotate([0, 90, 0])
            cylinder(d = rod_press, h = gd_dw + 2);
        pw = (gd_dw - 8)/4;  ph = (gd_dh - 9)/3;
        for (i = [0:3]) for (j = [0:2])
            translate([4 + i*pw, -gd_t/2 - 0.1, -gd_dh + 4.5 + j*ph])
                cube([pw - 3, 0.7, ph - 3]);
    }
}

// ============================================================
// ROOF - ridge along Y, so the GABLE FACES THE FRONT
// Profile is built in X (across the garage) and extruded along Y.
// ============================================================
function slope_steps(x0, z0, x1, z1, n, step) =
    let (dx = (x1 - x0)/n, dz = (z1 - z0 - (n-1)*step)/n)
    [ for (i = [0 : n-1], k = [0, 1])
        k == 0 ? [x0 + i*dx,     z0 + i*(dz + step)]
               : [x0 + (i+1)*dx, z0 + i*(dz + step) + dz] ];

left_slope = slope_steps(-roof_oh, fascia_h, gar_w/2, roof_rise,
                         shingle_n, shingle_step);

roof_pts = shingles
    ? concat([[-roof_oh, 0]], left_slope,
             [ for (i = [len(left_slope)-2 : -1 : 0])
                   [gar_w - left_slope[i][0], left_slope[i][1]] ],
             [[gar_w + roof_oh, 0]])
    : [[-roof_oh, 0], [-roof_oh, fascia_h], [gar_w/2, roof_rise],
       [gar_w + roof_oh, fascia_h], [gar_w + roof_oh, 0]];

slope_ang  = atan((roof_rise - fascia_h) / (gar_w/2 + roof_oh));
shell_drop = roof_t / cos(slope_ang);

// extruded along Y: profile u -> X, v -> Z
module roof_prism(drop, len) {
    translate([0, -roof_oh, -drop]) rotate([90, 0, 0]) mirror([0,0,1])
        linear_extrude(height = len) polygon(roof_pts);
}

// Clip the gable battens against a SMOOTH silhouette, never the shingled one.
// Intersecting thin strips with the stepped profile leaves razor-thin slivers
// at every step edge and the result is non-manifold.
smooth_pts = [[-roof_oh, 0], [-roof_oh, fascia_h], [gar_w/2, roof_rise],
              [gar_w + roof_oh, fascia_h], [gar_w + roof_oh, 0]];

module smooth_clip(len) {
    translate([0, -roof_oh, 0]) rotate([90, 0, 0]) mirror([0,0,1])
        linear_extrude(height = len) offset(delta = -1.2) polygon(smooth_pts);
}

module gable_battens() {
    n = floor(gar_w / board_pitch);
    for (s = [0, 1]) {
        // overlap the gable panel by 0.6, not by ov(0.1) - a 0.1mm sliver
        // contact against the panel face is what made this non-manifold
        yoff = (s == 0) ? -batten_proud : gar_d - 0.6;
        intersection() {
            // Skip any batten the gable vent would slice through - the vent
            // cuts them into thin fragments and the roof goes non-manifold.
            union() for (i = [0 : n])
                if (abs(i*board_pitch + 2 + batten_w/2 - gar_w/2) > 9)
                    translate([i*board_pitch + 2, yoff, -1])
                        cube([batten_w, batten_proud + 0.6, roof_rise + 2]);
            smooth_clip(gar_d + 2*roof_oh);
        }
    }
}

module roof() {
    len = gar_d + 2*roof_oh;
    difference() {
        intersection() {
            union() {
                difference() { roof_prism(0, len); roof_prism(shell_drop, len); }
                // gable end panels - front and back
                for (gy = [0, gar_d - wall_t])
                    intersection() {
                        roof_prism(0, len);
                        translate([0, gy, 0]) cube([gar_w, wall_t, roof_rise + 1]);
                    }
                linear_extrude(height = ledge_t)
                    difference() {
                        square([gar_w, gar_d]);
                        translate([ledge_w, ledge_w])
                            square([gar_w - 2*ledge_w, gar_d - 2*ledge_w]);
                    }
                if (texture) gable_battens();
            }
            translate([-roof_oh - 1, -roof_oh - 1, 0])
                cube([gar_w + 2*roof_oh + 2, len + 2, roof_rise + 2]);
        }
        for (p = peg_pos)
            translate([p[0], p[1], -0.5]) cylinder(d = peg_d + 0.4, h = peg_h + 1);
        // gable vent in the front gable, facing the street
        translate([gar_w/2, wall_t/2, roof_rise * 0.5]) rotate([90, 0, 0])
            cylinder(d = 11, h = 12, center = true);
    }
}

// ============================================================
module assembly() {
    garage_body();
    translate([gd_x0 + 0.5, wall_t/2, ftop + gd_h - gd_tube_d/2])
        rotate([open_garage, 0, 0]) garage_door();
    translate([0, 0, wtop]) roof();
}

module plate() {
    garage_body();
    translate([roof_oh, gar_d + 3 + roof_oh, 0]) roof();
    translate([gar_w + 8, 2, gd_t/2 + 1.2]) rotate([-90, 0, 0])
        translate([0, 0, gd_dh]) garage_door();
}

render_top = true;
if (render_top) {
    if      (show == "plate") plate();
    else if (show == "body")  garage_body();
    else if (show == "roof")  roof();
    else                      assembly();
}

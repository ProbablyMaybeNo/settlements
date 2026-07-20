// ============================================================
// AMERICAN RANCH HOUSE - 28mm interactive terrain  (v2, modular)
//
// v2 changes, after v1 read as a barn:
//   * PROPORTION. v1 had 90mm walls on a 200mm-wide footprint - a ratio of
//     0.45 against ~0.22 on the reference house. Twice as tall as it should
//     be, which is why the windows floated in blank walls and the roof sat
//     on top like a lid. Walls are now 52mm on a 226mm width (0.23).
//     A correctly-proportioned ranch at this footprint is ~85mm tall; it
//     cannot be the 6" originally specified without becoming a barn.
//   * Eaves deepened 6mm -> 10mm. Shallow eaves read as nothing at 28mm.
//   * Windows enlarged and dropped; door heights cut to suit a 52mm wall.
//   * GARAGE SPLIT OUT to ranch_garage.scad, freeing ~90mm of plate width.
//     A side door off the kitchen leads to it. The two butt together and
//     locate on 2 pegs (pegs on the garage, sockets here, so the house has
//     nothing protruding).
//
// MECHANISMS (wire-axle standard, per CLAUDE.md)
//   front / back / side doors - vertical PIN hinge. Door carries a
//   full-height tube; a 1.0mm wire runs up through the floor, through the
//   tube (FRICTION bore, holds any angle), into a blind hole in the lintel.
//
// Roof lifts off, located by 4 pegs into a flat bearing ledge.
// Parts: body, roof, 3 swing doors.  Hardware: 3x 1.0mm wire ~50mm.
// ============================================================

include <house_texture.scad>

/* [Show] */
show = "assembly";   // assembly | plate | body | roof
texture = true;      // OFF while iterating geometry - it is ~3x slower
open_front = 0;      // [0:100]
open_back  = 0;      // [0:100]
open_side  = 0;      // [0:100]

/* [Wire Axle Standard] */
clip_d        = 1.0;
clip_friction = clip_d + 0.10;
clip_free     = clip_d + 0.40;

/* [Overall] */
// 220, not 226: at 226 the plate measured 257.2mm across (body battens at
// x=-2.2 plus the door strip at x=255.2) and overran the 256mm bed by 1.2mm.
house_w    = 220;
house_d    = 112;
wall_h     = 52;    // eave height ~0.23 x width - the ranch proportion
wall_t     = 3;
floor_t    = 3;
int_wall_t = 3;

/* [Roof] */
roof_oh   = 10;
roof_rise = 30;
roof_t    = 2.5;
fascia_h  = 3;
ledge_w   = 8;
ledge_t   = 4;
peg_d     = 3;
peg_h     = 3;

/* [Shingles] */
shingles     = true;
shingle_n    = 16;
shingle_step = 0.45;

/* [Plan] */
part_v1 = 98;    // living/bed1  <->  hall
part_v2 = 138;   // hall <-> bed2/kitchen
part_hl = 62;    // living <-> bed1
part_hr = 55;    // bed2 <-> kitchen
rec_x0    = 104; // entry alcove
rec_x1    = 136;
rec_depth = 12;

/* [Doors] */
door_op_w  = 26;
door_op_h  = 40;
door_t     = 2.2;
tube_d     = 3.6;
tube_invx  = 2.4;
door_gap   = 0.4;

/* [Windows] */
win_sill  = 18;
win_h     = 24;
trim_t    = 1.2;
shutter_w = 5;

$fn = 24;

// ---- derived ----
ix0 = wall_t;  ix1 = house_w - wall_t;
iy0 = wall_t;  iy1 = house_d - wall_t;
ftop = floor_t;
wtop = floor_t + wall_h;

fd_x0 = (rec_x0 + rec_x1)/2 - door_op_w/2;   // front door
fd_y  = rec_depth + wall_t/2;
bd_x0 = 107;                                  // back door
bd_y  = house_d - wall_t/2;
sd_y0 = 70;                                   // side door -> garage
sd_x  = house_w - wall_t/2;

fd_tx = fd_x0 + tube_invx;
bd_tx = bd_x0 + door_op_w - tube_invx;
sd_ty = sd_y0 + tube_invx;

// garage alignment sockets in the right-hand wall
gar_link = [[house_w, 30, 26], [house_w, 100, 26]];
link_d   = 4;

// ============================================================
// FACE FRAME  (u along +X, v along +Z, face at y=0, material at +Y)
// ============================================================
module on_face(f) {
    if      (f == 0) children();
    else if (f == 1) translate([house_w, house_d, 0]) rotate([0,0,180]) children();
    else if (f == 2) translate([0, house_d, 0]) rotate([0,0,-90]) children();
    else             translate([house_w, 0, 0]) rotate([0,0,90]) children();
}
function fx(gx, w) = house_w - gx - w;
function fy(gy, w) = house_d - gy - w;
function face_w(f) = (f == 0 || f == 1) ? house_w : house_d;

module on_inner(f) {
    if      (f == 0) translate([house_w, wall_t, 0]) rotate([0,0,180]) children();
    else if (f == 1) translate([0, house_d - wall_t, 0]) children();
    else if (f == 2) translate([wall_t, 0, 0]) rotate([0,0,90]) children();
    else             translate([house_w - wall_t, house_d, 0]) rotate([0,0,-90]) children();
}

// ============================================================
// WALLS
// ============================================================
module alcove_returns(expand = 0, z0 = ftop, h = wall_h) {
    e = expand;
    translate([rec_x0 - e, -e, z0]) cube([wall_t + 2*e, rec_depth + wall_t + 2*e, h]);
    translate([rec_x1 - wall_t - e, -e, z0]) cube([wall_t + 2*e, rec_depth + wall_t + 2*e, h]);
}

module interior_walls(expand = 0, z0 = ftop, h = wall_h) {
    e = expand;
    translate([part_v1 - e, iy0 - e, z0]) cube([int_wall_t + 2*e, iy1 - iy0 + 2*e, h]);
    translate([part_v2 - e, iy0 - e, z0]) cube([int_wall_t + 2*e, iy1 - iy0 + 2*e, h]);
    translate([ix0 - e, part_hl - e, z0]) cube([part_v1 - ix0 + 2*e, int_wall_t + 2*e, h]);
    translate([part_v2 + int_wall_t - e, part_hr - e, z0])
        cube([ix1 - part_v2 - int_wall_t + 2*e, int_wall_t + 2*e, h]);
}

peg_pos = [[48, wall_t/2], [196, wall_t/2],
           [12, house_d - wall_t/2], [210, house_d - wall_t/2]];

// ============================================================
// OPENINGS
// ============================================================
module openings() {
    zs = ftop + win_sill;
    // front - living room pair, and bedroom 2
    translate([14,  -1, zs]) cube([30, wall_t + 2, win_h]);
    translate([54,  -1, zs]) cube([30, wall_t + 2, win_h]);
    translate([150, -1, zs]) cube([36, wall_t + 2, win_h]);
    // left wall
    translate([-1, 18, zs]) cube([wall_t + 2, 28, win_h]);
    translate([-1, 72, zs]) cube([wall_t + 2, 28, win_h]);
    // back wall
    translate([20,  house_d - wall_t - 1, zs]) cube([36, wall_t + 2, win_h]);
    translate([160, house_d - wall_t - 1, zs]) cube([40, wall_t + 2, win_h]);
    // right wall - bedroom 2
    translate([house_w - wall_t - 1, 14, zs]) cube([wall_t + 2, 28, win_h]);

    // doors
    translate([fd_x0, rec_depth - 1, ftop]) cube([door_op_w, wall_t + 2, door_op_h]);
    translate([bd_x0, house_d - wall_t - 1, ftop]) cube([door_op_w, wall_t + 2, door_op_h]);
    translate([house_w - wall_t - 1, sd_y0, ftop]) cube([wall_t + 2, door_op_w, door_op_h]);
    pin_holes(fd_tx, fd_y);
    pin_holes(bd_tx, bd_y);
    pin_holes(sd_x, sd_ty);

    // interior doorways
    translate([part_v1 - 1, 25, ftop]) cube([int_wall_t + 2, 26, door_op_h]);
    translate([part_v1 - 1, 75, ftop]) cube([int_wall_t + 2, 26, door_op_h]);
    translate([30, part_hl - 1, ftop]) cube([26, int_wall_t + 2, door_op_h]);
    translate([part_v2 - 1, 20, ftop]) cube([int_wall_t + 2, 26, door_op_h]);
    translate([part_v2 - 1, 70, ftop]) cube([int_wall_t + 2, 26, door_op_h]);
    translate([165, part_hr - 1, ftop]) cube([26, int_wall_t + 2, door_op_h]);

    // garage alignment sockets
    for (g = gar_link)
        translate([g[0] - wall_t - 1, g[1], g[2]]) rotate([0,90,0])
            cylinder(d = link_d + 0.4, h = wall_t + 2);
}

module pin_holes(tx, ty) {
    translate([tx, ty, -1]) cylinder(d = clip_free, h = ftop + 2);
    translate([tx, ty, ftop + door_op_h - 0.5]) cylinder(d = clip_free, h = 9);
}

// ============================================================
// BOARD AND BATTEN + TRIM
// ============================================================
batten_proud = 0.8;
batten_w     = 1.6;
case_w = 2.0;
proud  = 1.2;

module battens_on(w, h) {
    n = floor(w / board_pitch);
    for (i = [0 : n])
        translate([i*board_pitch, -batten_proud, ftop])
            cube([batten_w, batten_proud + ov, h]);
}

module exterior_battens() {
    for (f = [0:3]) on_face(f) battens_on(face_w(f), wall_h);
    for (c = [[0,0],[house_w - batten_w, 0],
              [0, house_d - batten_w],[house_w - batten_w, house_d - batten_w]])
        translate([c[0] - batten_proud, c[1] - batten_proud, ftop])
            cube([batten_w + 2*batten_proud, batten_w + 2*batten_proud, wall_h]);
}

module all_trim() {
    zs = ftop + win_sill;
    on_face(0) {
        opening_trim(14,  zs, 30, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(54,  zs, 30, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(150, zs, 36, win_h, case_w, proud, true, true, shutter_w);
    }
    on_face(2) {
        opening_trim(fy(18,28), zs, 28, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(fy(72,28), zs, 28, win_h, case_w, proud, true, true, shutter_w);
    }
    on_face(1) {
        opening_trim(fx(20,36),  zs, 36, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(fx(160,40), zs, 40, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(fx(bd_x0, door_op_w), ftop, door_op_w, door_op_h,
                     case_w, proud, false, false, 0);
    }
    on_face(3) {
        opening_trim(14, zs, 28, win_h, case_w, proud, true, true, shutter_w);
        opening_trim(sd_y0, ftop, door_op_w, door_op_h, case_w, proud, false, false, 0);
    }
    translate([0, rec_depth, 0]) on_face(0)
        opening_trim(fd_x0, ftop, door_op_w, door_op_h, case_w, proud, false, false, 0);
}

module interior_boards() {
    for (f = [0:3]) on_inner(f)
        translate([0, 0, ftop]) face_cut("boards", face_w(f), wall_h, board_d);
}

module damage() {
    clusters = [
        [0,  30, 34, 20, 5],
        [0, 120, 28, 16, 4],
        [0, 190, 32, 20, 4],
        [2,  55, 34, 20, 4],
        [1, 110, 30, 22, 4]
    ];
    for (ci = [0 : len(clusters) - 1]) {
        cl = clusters[ci];  n = cl[4];
        ru = rands(-cl[3], cl[3], n, 42 + ci*7);
        rv = rands(-cl[3]*0.5, cl[3]*0.5, n, 91 + ci*13);
        on_face(cl[0]) for (i = [0 : n-1]) crater(cl[1] + ru[i], cl[2] + rv[i]);
    }
    on_face(0) { through_hole(96, 38, wall_t); through_hole(200, 22, wall_t); }
    on_face(2)   through_hole(60, 36, wall_t);
}

// Clip against a SMOOTH silhouette, never the shingled one - intersecting thin
// strips with the stepped profile leaves slivers at every step and goes
// non-manifold.
smooth_pts = [[-roof_oh, 0], [-roof_oh, fascia_h], [house_d/2, roof_rise],
              [house_d + roof_oh, fascia_h], [house_d + roof_oh, 0]];

module smooth_clip(len) {
    translate([-roof_oh, 0, 0]) rotate([90, 0, 90])
        linear_extrude(height = len) offset(delta = -1.2) polygon(smooth_pts);
}

module gable_battens() {
    n = floor(house_d / board_pitch);
    for (s = [0, 1]) {
        // overlap the gable panel by 0.6, not by ov(0.1) - a sliver contact
        // against the panel face goes non-manifold
        xoff = (s == 0) ? -batten_proud : house_w - 0.6;
        intersection() {
            union() for (i = [0 : n])
                translate([xoff, i*board_pitch + 2, -1])
                    cube([batten_proud + 0.6, batten_w, roof_rise + 2]);
            smooth_clip(house_w + 2*roof_oh);
        }
    }
}

// ============================================================
// BODY
// ============================================================
module house_body() {
    difference() {
        union() {
            difference() {
                cube([house_w, house_d, floor_t + wall_h]);
                translate([ix0, iy0, ftop]) cube([ix1 - ix0, iy1 - iy0, wall_h + 1]);
                translate([rec_x0, -1, ftop])
                    cube([rec_x1 - rec_x0, rec_depth + 1, wall_h + 1]);
            }
            translate([rec_x0, rec_depth, ftop])
                cube([rec_x1 - rec_x0, wall_t, wall_h]);
            alcove_returns();
            interior_walls();
            for (p = peg_pos)
                translate([p[0], p[1], wtop]) cylinder(d = peg_d, h = peg_h);
            if (texture) { exterior_battens(); all_trim(); }
        }
        openings();
        if (texture) { interior_boards(); damage(); }
    }
}

// ============================================================
// SWING DOOR - pin hinge, local origin = hinge axis
// ============================================================
module swing_door() {
    dw = door_op_w - tube_invx - door_gap;
    dh = door_op_h - 2*door_gap;
    difference() {
        union() {
            translate([0, 0, door_gap]) cylinder(d = tube_d, h = dh);
            translate([0, -door_t/2, door_gap]) cube([dw, door_t, dh]);
        }
        translate([0, 0, -1]) cylinder(d = clip_friction, h = dh + 4);
        for (pz = [6, 23])
            translate([3.5, -door_t/2 - 0.1, pz]) cube([dw - 6, 0.7, 12]);
    }
}

// ============================================================
// ROOF
// ============================================================
function slope_steps(y0, z0, y1, z1, n, step) =
    let (dy = (y1 - y0)/n, dz = (z1 - z0 - (n-1)*step)/n)
    [ for (i = [0 : n-1], k = [0, 1])
        k == 0 ? [y0 + i*dy,     z0 + i*(dz + step)]
               : [y0 + (i+1)*dy, z0 + i*(dz + step) + dz] ];

front_slope = slope_steps(-roof_oh, fascia_h, house_d/2, roof_rise,
                          shingle_n, shingle_step);

roof_pts = shingles
    ? concat([[-roof_oh, 0]], front_slope,
             [ for (i = [len(front_slope)-2 : -1 : 0])
                   [house_d - front_slope[i][0], front_slope[i][1]] ],
             [[house_d + roof_oh, 0]])
    : [[-roof_oh, 0], [-roof_oh, fascia_h], [house_d/2, roof_rise],
       [house_d + roof_oh, fascia_h], [house_d + roof_oh, 0]];

slope_ang  = atan((roof_rise - fascia_h) / (house_d/2 + roof_oh));
shell_drop = roof_t / cos(slope_ang);

module roof_prism(drop, len) {
    translate([-roof_oh, 0, -drop]) rotate([90, 0, 90])
        linear_extrude(height = len) polygon(roof_pts);
}

module roof() {
    len = house_w + 2*roof_oh;
    difference() {
        intersection() {
            union() {
                difference() { roof_prism(0, len); roof_prism(shell_drop, len); }
                for (gx = [0, house_w - wall_t])
                    intersection() {
                        roof_prism(0, len);
                        translate([gx, 0, 0]) cube([wall_t, house_d, roof_rise + 1]);
                    }
                linear_extrude(height = ledge_t)
                    difference() {
                        square([house_w, house_d]);
                        translate([ledge_w, ledge_w])
                            square([house_w - 2*ledge_w, house_d - 2*ledge_w]);
                    }
                if (texture) gable_battens();
            }
            translate([-roof_oh - 1, -roof_oh - 1, 0])
                cube([len + 2, house_d + 2*roof_oh + 2, roof_rise + 2]);
        }
        for (p = peg_pos)
            translate([p[0], p[1], -0.5]) cylinder(d = peg_d + 0.4, h = peg_h + 1);
        for (vx = [wall_t/2, house_w - wall_t/2])
            translate([vx, house_d/2, roof_rise * 0.5]) rotate([0, 90, 0])
                cylinder(d = 11, h = 12, center = true);
    }
}

// ============================================================
// ASSEMBLY / PLATE
// ============================================================
module assembly() {
    house_body();
    translate([fd_tx, fd_y, ftop]) rotate([0, 0, open_front]) swing_door();
    translate([bd_tx, bd_y, ftop]) rotate([0, 0, 180 - open_back]) swing_door();
    translate([sd_x, sd_ty, ftop]) rotate([0, 0, 90 - open_side]) swing_door();
    translate([0, 0, wtop]) roof();
}

// Body, roof and all three doors on one A1 plate.
module plate() {
    house_body();
    translate([roof_oh, house_d + 3 + roof_oh, 0]) roof();
    for (i = [0:2])
        translate([house_w + 5, 2 + i*(door_op_h + 3), door_t/2])
            rotate([-90, 0, 0]) swing_door();
}

render_top = true;
if (render_top) {
    if      (show == "plate") plate();
    else if (show == "body")  house_body();
    else if (show == "roof")  roof();
    else                      assembly();
}

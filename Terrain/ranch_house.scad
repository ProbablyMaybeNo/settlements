// ============================================================
// AMERICAN RANCH HOUSE - 28mm interactive terrain
// Single storey brick ranch, attached 2-car garage, recessed entry.
// Footprint 200 x 118mm (7.87 x 4.65"), 138mm tall (5.4") to the ridge.
//
// MECHANISMS (wire-axle standard, per CLAUDE.md)
//   garage door - tilt-up single panel. Hinge tube along the top edge on a
//                 1.6mm brass rod. Tube = PRESS (rod turns with the door),
//                 left jamb = FRICTION (holds it open), right jamb = FREE.
//   front/back  - vertical PIN hinge, not a knuckle hinge. The door carries a
//     doors       full-height tube on its hinge edge; a 1.0mm wire drops
//                 through the floor, up the tube, into a blind hole in the
//                 lintel. Tube = FRICTION (door stays where you put it),
//                 floor + lintel = FREE.
//                 Chosen over interleaved knuckles because knuckles at this
//                 scale end up smaller than the clearance notch they need,
//                 which leaves the frame barrels floating unattached - the
//                 known defect in prison_cell.scad. A pin hinge is integral
//                 to the wall by construction.
//
// Roof lifts off; a registration lip drops inside the wall tops and is
// notched around the interior walls so it seats flat.
//
// Parts: body, roof, garage door, front door, back door
// Hardware: 1.6mm brass rod ~95mm; 2x 1.0mm wire ~70mm
// ============================================================

/* [Show] */
show = "assembly";   // assembly | layout | body | roof
open_garage = 0;     // [0:85]  preview only
open_front  = 0;     // [0:100] preview only
open_back   = 0;     // [0:100] preview only

/* [Wire Axle Standard] */
rod_d         = 1.6;
rod_press     = rod_d + 0.05;
rod_friction  = rod_d + 0.10;
rod_free      = rod_d + 0.40;
clip_d        = 1.0;
clip_friction = clip_d + 0.10;
clip_free     = clip_d + 0.40;

/* [Overall] */
house_w    = 200;
house_d    = 118;
wall_h     = 90;
wall_t     = 3;
floor_t    = 3;
int_wall_t = 3;

/* [Roof] */
roof_oh   = 6;
roof_rise = 45;
roof_t    = 3;
fascia_h  = 4;     // vertical fascia board at the eaves
ledge_w   = 8;     // internal ring that bears on the wall tops
ledge_t   = 4;
peg_d     = 3;     // roof/wall registration pegs
peg_h     = 3;

/* [Plan] */
gar_wall_x = 112;   // garage partition, garage is to the right
part_v     = 68;    // living/bedroom <-> hall/kitchen
part_h     = 62;    // front rooms <-> back rooms
rec_x0     = 68;    // entry recess
rec_x1     = 108;
rec_depth  = 14;

/* [Garage door] */
gar_op_x0  = 120;
gar_op_w   = 70;
gar_op_h   = 56;   // keeps the flat-laid door inside the plate-1 side strip
gar_door_t = 2.5;
gar_tube_d = 5;

/* [Swing doors] */
door_op_w  = 28;
door_op_h  = 58;
door_t     = 2.5;
tube_d     = 4;     // hinge tube on the door edge
tube_invx  = 2.6;   // tube centre, inboard from the jamb
door_gap   = 0.4;

/* [Windows] */
win_sill   = 34;
win_h      = 30;
trim_t     = 1.2;
shutter_w  = 6;

$fn = 24;

// ---- derived ----
ix0 = wall_t;  ix1 = house_w - wall_t;
iy0 = wall_t;  iy1 = house_d - wall_t;
ftop = floor_t;
wtop = floor_t + wall_h;

// door opening spans
fd_x0 = (rec_x0 + rec_x1)/2 - door_op_w/2;   // front door
fd_y  = rec_depth + wall_t/2;                // front door wall mid-plane
bd_x0 = 74;                                  // back door
bd_y  = house_d - wall_t/2;

// hinge tube centres
fd_tx = fd_x0 + tube_invx;                   // front hinges on the LEFT jamb
bd_tx = bd_x0 + door_op_w - tube_invx;       // back hinges on the RIGHT jamb

// ============================================================
// INTERIOR WALLS - z range parameterised so the same footprints
// can notch the roof lip
// ============================================================
// alcove return walls - these sit inside the footprint and so must also be
// notched out of the roof lip, or the roof will not seat.
module alcove_returns(expand = 0, z0 = ftop, h = wall_h) {
    e = expand;
    translate([rec_x0 - e, -e, z0])
        cube([wall_t + 2*e, rec_depth + wall_t + 2*e, h]);
    translate([rec_x1 - wall_t - e, -e, z0])
        cube([wall_t + 2*e, rec_depth + wall_t + 2*e, h]);
}

module interior_walls(expand = 0, z0 = ftop, h = wall_h) {
    e = expand;
    // garage partition, full depth
    translate([gar_wall_x - e, iy0 - e, z0])
        cube([int_wall_t + 2*e, iy1 - iy0 + 2*e, h]);
    // living/bedroom <-> hall/kitchen (starts behind the recess wall)
    translate([part_v - e, rec_depth + wall_t - e, z0])
        cube([int_wall_t + 2*e, part_h + int_wall_t - rec_depth - wall_t + 2*e, h]);
    // front <-> back
    translate([ix0 - e, part_h - e, z0])
        cube([gar_wall_x - ix0 + 2*e, int_wall_t + 2*e, h]);
}

// ============================================================
// OPENINGS
// ============================================================
module openings() {
    // front windows (living room)
    translate([10, -1, ftop + win_sill]) cube([24, wall_t + 2, win_h]);
    translate([40, -1, ftop + win_sill]) cube([22, wall_t + 2, win_h]);
    // left wall - living + bedroom
    translate([-1, 20, ftop + win_sill]) cube([wall_t + 2, 24, win_h]);
    translate([-1, 78, ftop + win_sill]) cube([wall_t + 2, 24, win_h]);
    // back wall - bedroom
    translate([14, house_d - wall_t - 1, ftop + win_sill]) cube([28, wall_t + 2, win_h]);
    // right wall - garage
    translate([house_w - wall_t - 1, 30, ftop + win_sill]) cube([wall_t + 2, 24, win_h]);

    // garage door opening
    translate([gar_op_x0, -1, ftop]) cube([gar_op_w, wall_t + 2, gar_op_h]);
    // garage rod holes: LEFT jamb friction, RIGHT jamb free
    gt_z = ftop + gar_op_h - gar_tube_d/2;
    translate([gar_op_x0 - 6, wall_t/2, gt_z]) rotate([0,90,0])
        cylinder(d = rod_friction, h = 6.5);
    translate([gar_op_x0 + gar_op_w - 0.5, wall_t/2, gt_z]) rotate([0,90,0])
        cylinder(d = rod_free, h = 8);

    // front + back door openings
    translate([fd_x0, rec_depth - 1, ftop]) cube([door_op_w, wall_t + 2, door_op_h]);
    translate([bd_x0, house_d - wall_t - 1, ftop]) cube([door_op_w, wall_t + 2, door_op_h]);
    // pin-hinge wire holes: through the floor, blind into the lintel
    pin_holes(fd_tx, fd_y);
    pin_holes(bd_tx, bd_y);

    // interior doorways (open, no doors)
    translate([part_v - 1, 30, ftop])   cube([int_wall_t + 2, 28, door_op_h]);
    translate([20, part_h - 1, ftop])   cube([28, int_wall_t + 2, door_op_h]);
    translate([78, part_h - 1, ftop])   cube([28, int_wall_t + 2, door_op_h]);
    translate([gar_wall_x - 1, 80, ftop]) cube([int_wall_t + 2, 28, door_op_h]);
}

module pin_holes(tx, ty) {
    // through the floor - wire is inserted from underneath
    translate([tx, ty, -1]) cylinder(d = clip_free, h = ftop + 2);
    // blind into the lintel above the opening
    translate([tx, ty, ftop + door_op_h - 0.5]) cylinder(d = clip_free, h = 12);
}

// ============================================================
// EXTERIOR TRIM
// ============================================================
module win_trim_front(x, w) {
    difference() {
        translate([x - 2, -trim_t, ftop + win_sill - 2])
            cube([w + 4, trim_t + 0.1, win_h + 4]);
        translate([x, -trim_t - 1, ftop + win_sill])
            cube([w, trim_t + 3, win_h]);
    }
    for (sx = [x - 2 - shutter_w, x + w + 2])
        translate([sx, -trim_t + 0.3, ftop + win_sill - 1])
            cube([shutter_w, trim_t, win_h + 2]);
}

// ============================================================
// BODY
// ============================================================
module house_body() {
    difference() {
        union() {
            difference() {
                cube([house_w, house_d, floor_t + wall_h]);
                // interior cavity
                translate([ix0, iy0, ftop])
                    cube([ix1 - ix0, iy1 - iy0, wall_h + 1]);
                // entry recess carved out of the front wall
                translate([rec_x0, -1, ftop])
                    cube([rec_x1 - rec_x0, rec_depth + 1, wall_h + 1]);
            }
            // recessed front wall behind the alcove
            translate([rec_x0, rec_depth, ftop])
                cube([rec_x1 - rec_x0, wall_t, wall_h]);
            // alcove return walls, else you see straight into the rooms
            alcove_returns();
            interior_walls();
            win_trim_front(10, 24);
            win_trim_front(40, 22);
            // roof registration pegs, standing on the wall tops
            for (p = peg_pos)
                translate([p[0], p[1], wtop]) cylinder(d = peg_d, h = peg_h);
        }
        openings();
    }
}

// ============================================================
// SWING DOOR - pin hinge. Local origin = hinge axis.
// Panel runs +X, closed panel lies in the Y=0 plane.
// ============================================================
module swing_door() {
    dw = door_op_w - tube_invx - door_gap;
    dh = door_op_h - 2*door_gap;
    difference() {
        union() {
            // hinge tube on the door edge
            translate([0, 0, door_gap]) cylinder(d = tube_d, h = dh);
            // panel
            translate([0, -door_t/2, door_gap]) cube([dw, door_t, dh]);
        }
        // FRICTION bore - this is what holds the door at any angle
        translate([0, 0, -1]) cylinder(d = clip_friction, h = dh + 4);
        // two recessed panels
        for (pz = [8, 34])
            translate([4, -door_t/2 - 0.1, pz])
                cube([dw - 7, 0.8, 18]);
    }
}

// ============================================================
// GARAGE DOOR - tilt-up. Local origin = hinge axis at the top edge.
// ============================================================
gar_dw = gar_op_w - 1.0;
gar_dh = gar_op_h - gar_tube_d/2 - 1.0;

module garage_door() {
    dw = gar_dw;
    dh = gar_dh;
    difference() {
        union() {
            rotate([0, 90, 0]) cylinder(d = gar_tube_d, h = dw);
            translate([0, -gar_door_t/2, -dh]) cube([dw, gar_door_t, dh + 1]);
        }
        translate([-1, 0, 0]) rotate([0, 90, 0])
            cylinder(d = rod_press, h = dw + 2);
        // 4 x 4 raised panel detail
        pw = (dw - 8)/4;  ph = (dh - 10)/4;
        for (i = [0:3]) for (j = [0:3])
            translate([4 + i*pw, -gar_door_t/2 - 0.1, -dh + 5 + j*ph])
                cube([pw - 3, 0.8, ph - 3]);
    }
}

// ============================================================
// ROOF - gable, ridge along X, lifts off. All in house coords.
// ============================================================
// Profile is a PENTAGON, not a triangle: the two lower corners give the eaves
// a vertical fascia board instead of a knife edge.
roof_pts = [[-roof_oh, 0], [-roof_oh, fascia_h], [house_d/2, roof_rise],
            [house_d + roof_oh, fascia_h], [house_d + roof_oh, 0]];

slope_run  = house_d/2 + roof_oh;
slope_ang  = atan((roof_rise - fascia_h) / slope_run);
shell_drop = roof_t / cos(slope_ang);   // vertical shift giving roof_t normal

module roof_prism(drop, len) {
    translate([-roof_oh, 0, -drop]) rotate([90, 0, 90])
        linear_extrude(height = len) polygon(roof_pts);
}

// Registration pegs stand on the wall tops (printed with the body, pointing
// up - no overhang) and engage holes in the roof ledge. This replaces the
// earlier hanging lip: the roof underside is now a FLAT plane at z=0, which
// is what lets it print ridge-up on a large flat first layer.
peg_pos = [[25, wall_t/2], [114, wall_t/2],
           [25, house_d - wall_t/2], [175, house_d - wall_t/2]];

module roof() {
    len = house_w + 2*roof_oh;
    difference() {
        intersection() {
            union() {
                // open tent shell - inner cutter is the same profile shifted
                // DOWN, so it breaks through the bottom and leaves no floor
                difference() {
                    roof_prism(0, len);
                    roof_prism(shell_drop, len);
                }
                // gable end panels close the two ends
                for (gx = [0, house_w - wall_t])
                    intersection() {
                        roof_prism(0, len);
                        translate([gx, 0, 0])
                            cube([wall_t, house_d, roof_rise + 1]);
                    }
                // bearing ledge - flat ring that sits on the wall tops
                linear_extrude(height = ledge_t)
                    difference() {
                        square([house_w, house_d]);
                        translate([ledge_w, ledge_w])
                            square([house_w - 2*ledge_w, house_d - 2*ledge_w]);
                    }
            }
            // trim everything below z=0 so the underside is one flat plane
            translate([-roof_oh - 1, -roof_oh - 1, 0])
                cube([len + 2, house_d + 2*roof_oh + 2, roof_rise + 2]);
        }
        // peg sockets
        for (p = peg_pos)
            translate([p[0], p[1], -0.5])
                cylinder(d = peg_d + 0.4, h = peg_h + 1);
        // gable vents
        for (vx = [wall_t/2, house_w - wall_t/2])
            translate([vx, house_d/2, roof_rise * 0.55]) rotate([0, 90, 0])
                cylinder(d = 14, h = 12, center = true);
    }
}

// ============================================================
// ASSEMBLY
// ============================================================
module assembly() {
    house_body();
    // doors sit ON the floor slab, not at z=0
    translate([fd_tx, fd_y, ftop]) rotate([0, 0,  open_front]) swing_door();
    translate([bd_tx, bd_y, ftop]) rotate([0, 0, 180 - open_back]) swing_door();
    // the hinge tube runs along X, so the door must rotate about X
    translate([gar_op_x0 + 0.5, wall_t/2, ftop + gar_op_h - gar_tube_d/2])
        rotate([open_garage, 0, 0]) garage_door();
    translate([0, 0, wtop]) roof();
}

// ============================================================
// PRINT LAYOUT - body + roof on one 256 x 256 plate
// ============================================================
// Roof prints RIDGE UP, as modelled, sitting on its flat ledge ring.
// The gable shell tapers inward as it rises (91% layer overlap at this
// pitch) so it is fully self-supporting - no supports, no raft.
// Do NOT invert it and do NOT lay it on a slope: the bearing ledge sticks
// 7.5mm below the slope plane, so a flat-laid half rests on a line.
// Doors lie flat in the strip ABOVE the body in Y. (Putting them in a side
// strip in X overruns the bed: the garage door alone is 69mm wide, which
// pushed plate 1 to 272mm.)
module doors_flat() {
    translate([2, 0, gar_door_t/2 + 1.3]) rotate([-90, 0, 0])
        translate([0, 0, gar_dh]) garage_door();
    translate([80,  0, door_t/2]) rotate([-90, 0, 0]) swing_door();
    translate([112, 0, door_t/2]) rotate([-90, 0, 0]) swing_door();
}

// PLATE 1 - body + all three doors
module plate1() {
    house_body();
    translate([0, house_d + 6, 0]) doors_flat();
}
// PLATE 2 - roof on its own
module plate2() { translate([roof_oh, roof_oh, 0]) roof(); }

// Alternative single plate: body + roof together (248mm of the 256mm bed).
// The doors then have to go on a separate plate.
module plate_bodyroof() {
    house_body();
    translate([roof_oh, house_d + 6 + roof_oh, 0]) roof();
}

module layout() { plate1(); }

render_top = true;
if (render_top) {
    if      (show == "layout")     layout();
    else if (show == "plate1")     plate1();
    else if (show == "plate2")     plate2();
    else if (show == "bodyroof")   plate_bodyroof();
    else if (show == "body")       house_body();
    else if (show == "roof")       roof();
    else                           assembly();
}

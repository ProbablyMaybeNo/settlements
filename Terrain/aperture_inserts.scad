// ============================================================
// APERTURE INSERTS - pop-in windows and doors for ANY wall set
//
// Point it at an aperture size and it generates a matching insert set.
// Works on your own OpenSCAD buildings and on third-party STL terrain
// (Fallout Terrain, Printable Scenery, etc). Measure the aperture once,
// set ap_w / ap_h / wall_t, print.
//
// MEASURED APERTURES (slice analysis of the actual meshes)
//   Fallout "Urban House B" ....... 15.1-16.0 x 25.9,  wall 5.2
//   ranch_house.scad (ours) ....... 28/30/36/40 x 24,  wall 3.0
// NOTE: Urban House 'B' ships NO door and NO doorway - the halves are
// open-backed, which is how minis get in. Doors below are for our own
// buildings and for sets that do have doorways.
//
// THREE WAYS TO MAKE AN OPENING WORK, cheapest first:
//   1. SWAP    - print several inserts, pop one in. No moving parts.
//   2. PIN     - door panel with pins top and bottom, drops into sockets
//                and swings freely. One hole each end, nothing else.
//   3. WIRE    - the full pin hinge from ranch_house.scad. Best feel,
//                needs a wire and a lintel bore.
// For third-party STL, use 1 (no mesh edits) or 2 with drill_socket.scad.
// ============================================================

// ------------------------------------------------------------
// PRIMARY USE: BARRICADES. A barricade fits from the INSIDE - a backing
// plate laps the wall around the opening and the planks drop into the
// aperture to locate it. Because rough boards can sit 0.5mm loose in any
// direction and still look right, a barricade tolerates the 0.9mm aperture
// variation measured across these walls. A glazed pane would not. That is
// why this is the easy option and why no test coupon is needed for it.
// Push it in to close the opening, pull it out to open. Nothing to break.
// ------------------------------------------------------------

/* [Show] */
show  = "barricades";  // barricades | window_set | door_set | coupon | single
style = "barricade";   // barricade | glazed | open | boarded | blown | door | door_pin

/* [Barricade] */
back_o   = 4.0;    // backing plate oversize per side (laps the wall inside)
back_t   = 1.4;
plank_t  = 2.5;    // how far the planks reach into the aperture
plank_n  = 4;
plank_gap = 1.3;
barr_slop = 1.2;   // total width slop - deliberately loose

/* [Aperture] */
ap_w   = 15.5;
ap_h   = 25.9;
wall_t = 5.2;

/* [Fit] */
fit_gap   = 0.5;    // total clearance across the width
plug_t    = 3.4;
flange_o  = 1.3;
flange_t  = 1.0;

/* [Pin hinge] */
pin_d     = 1.8;
pin_len   = 2.6;
pin_gap   = 0.35;   // socket is pin_d + this

/* [Detail] */
bar_w   = 1.0;
frame_w = 1.6;
pane_t  = 0.8;

$fn = 20;

pw = ap_w - fit_gap;
ph = ap_h - fit_gap;

// ---------- shared ----------
module plug_body(w = pw, h = ph) {
    translate([-(w/2 + flange_o), -flange_t, -(h/2 + flange_o)])
        cube([w + 2*flange_o, flange_t + 0.01, h + 2*flange_o]);
    translate([-w/2, 0, -h/2]) cube([w, plug_t, h]);
}

// ---------- window styles ----------
module s_glazed() {
    difference() {
        plug_body();
        translate([-pw/2 + frame_w, pane_t, -ph/2 + frame_w])
            cube([pw - 2*frame_w, plug_t, ph - 2*frame_w]);
    }
    translate([-bar_w/2, pane_t, -ph/2 + frame_w])
        cube([bar_w, plug_t - pane_t, ph - 2*frame_w]);
    translate([-pw/2 + frame_w, pane_t, -bar_w/2])
        cube([pw - 2*frame_w, plug_t - pane_t, bar_w]);
}

module s_open() {
    difference() {
        plug_body();
        translate([-pw/2 + frame_w, -flange_t - 1, -ph/2 + frame_w])
            cube([pw - 2*frame_w, plug_t + flange_t + 2, ph - 2*frame_w]);
    }
    sash = min(7, ph*0.3);
    translate([-pw/2 + frame_w, pane_t, ph/2 - frame_w - sash])
        cube([pw - 2*frame_w, plug_t - pane_t, sash]);
    translate([-bar_w/2, pane_t, ph/2 - frame_w - sash])
        cube([bar_w, plug_t - pane_t, sash]);
    translate([-pw/2 + frame_w, pane_t, -ph/2 + frame_w])
        cube([pw - 2*frame_w, plug_t - pane_t, 1.4]);
}

module s_boarded() {
    difference() {
        plug_body();
        translate([-pw/2 + frame_w, pane_t, -ph/2 + frame_w])
            cube([pw - 2*frame_w, plug_t, ph - 2*frame_w]);
    }
    // tilt kept to 2deg and the gap widened: at 4deg the plank ends rise
    // 0.57mm and adjacent planks meet at an exact tangent -> non-manifold
    n = max(2, floor(ph/8));
    pitch = (ph - 4)/n;
    for (i = [0 : n-1])
        translate([-pw/2 - 0.6, pane_t, -ph/2 + 2 + i*pitch])
            rotate([(i%2 ? 2 : -2), 0, 0])
                cube([pw + 1.2, plug_t - pane_t, pitch - 2.6]);
}

module s_blown() {
    // Cut the void FIRST, then add the shards. Unioning them before the cut
    // put them inside the cut region, so they were silently deleted and the
    // insert came out as a plain empty frame.
    difference() {
        plug_body();
        translate([-pw/2 + frame_w, -flange_t - 1, -ph/2 + frame_w])
            cube([pw - 2*frame_w, plug_t + flange_t + 2, ph - 2*frame_w]);
        for (a = [0 : 4])
            translate([-pw/2 + a*(pw/4) - 1, -flange_t - 1, ph/2 + flange_o - 1.2])
                rotate([0, 45, 0]) cube([2.2, flange_t + 3, 2.2]);
    }
    // glass clinging to the frame - overlap the frame by 0.4 so it welds on
    translate([-pw/2 + frame_w - 0.4, pane_t, ph/2 - frame_w - 5])
        cube([pw*0.3, plug_t - pane_t, 5.4]);
    translate([pw/2 - frame_w - pw*0.22, pane_t, ph/2 - frame_w - 8])
        cube([pw*0.22 + 0.4, plug_t - pane_t, 8.4]);
    translate([-pw/2 + frame_w - 0.4, pane_t, -ph/2 + frame_w - 0.4])
        cube([pw*0.18, plug_t - pane_t, 4]);
}

// ---------- doors ----------
// SWAP door: a solid panel that fills a doorway. Print two and leave one
// out to show the door standing open beside the frame.
module s_door() {
    difference() {
        plug_body();
        // recessed panels
        for (pz = [-ph/4 - 1, ph/4 + 1])
            translate([-pw/2 + 3.5, -flange_t - 0.1, pz - ph*0.14])
                cube([pw - 7, 0.7, ph*0.28]);
    }
    // handle
    translate([pw/2 - 3.5, -flange_t - 1.1, 0]) rotate([90,0,0])
        cylinder(d = 1.8, h = 1.2);
}

// PIN door: pins top and bottom, drops into two sockets and swings.
// Needs no wire and no flange - the frame stops it closing past flush.
module s_door_pin() {
    dw = ap_w - 1.2;
    dh = ap_h - 1.2;
    difference() {
        union() {
            translate([0, -plug_t/2, 0]) cube([dw, plug_t, dh]);
            // pins on the hinge edge, at x=0
            translate([0, 0, -pin_len + 0.01]) cylinder(d = pin_d, h = pin_len);
            translate([0, 0, dh - 0.01]) cylinder(d = pin_d, h = pin_len);
        }
        for (pz = [dh*0.24, dh*0.62])
            translate([3.5, -plug_t/2 - 0.1, pz])
                cube([dw - 7, 0.7, dh*0.22]);
    }
    translate([dw - 3.5, -plug_t/2 - 1.1, dh/2]) rotate([90,0,0])
        cylinder(d = 1.8, h = 1.2);
}

// ---------- BARRICADE ----------
// Backing plate laps the wall on the inside; planks drop into the aperture
// and locate it. Deliberately loose - see note at the top of the file.
module s_barricade(w = ap_w, h = ap_h, diag = true) {
    bw = w - barr_slop;              // plank span inside the aperture
    bh = h - barr_slop;
    pitch = bh / plank_n;
    ph_ = pitch - plank_gap;         // individual plank height
    // backing plate, sits against the inside wall face
    translate([-(w/2 + back_o), -back_t, -(h/2 + back_o)])
        cube([w + 2*back_o, back_t + 0.01, h + 2*back_o]);
    // planks reaching into the aperture
    for (i = [0 : plank_n - 1])
        translate([-bw/2, 0, -bh/2 + i*pitch])
            rotate([(i % 2 ? 1.5 : -1.5), 0, 0])
                cube([bw, plank_t, ph_]);
    // Diagonal brace sits on the PLANK side, not the backing-plate side.
    // On the plate side it would be the first thing to touch the bed and the
    // plate would print floating above it; here it rides on top of the planks.
    if (diag)
        translate([0, plank_t - 0.5, 0])
            rotate([0, 28, 0])
                translate([-(w*0.62)/2, 0, -2.1])
                    cube([w*0.62, 1.6, 4.2]);
    // nail heads
    for (sx = [-bw/2 + 1.6, bw/2 - 1.6]) for (i = [0 : plank_n - 1])
        translate([sx, plank_t - 0.3, -bh/2 + i*pitch + ph_/2])
            rotate([-90, 0, 0]) cylinder(d = 1.1, h = 0.7);
}

module s_barricade_door() s_barricade(door_w, door_h, true);

module insert(s) {
    if      (s == "barricade") s_barricade();
    else if (s == "open")     s_open();
    else if (s == "boarded")  s_boarded();
    else if (s == "blown")    s_blown();
    else if (s == "door")     s_door();
    else if (s == "door_pin") s_door_pin();
    else                      s_glazed();
}

// Socket pair for a pin door - subtract this from a floor and lintel.
// x,y is the hinge axis; h is the opening height.
module pin_sockets(h) {
    translate([0, 0, -pin_len - 0.5]) cylinder(d = pin_d + pin_gap, h = pin_len + 0.6);
    translate([0, 0, h - 0.1]) cylinder(d = pin_d + pin_gap, h = pin_len + 0.6);
}

// ---------- layouts ----------
/* [Door aperture - this pack has none; sized for ranch_house.scad] */
door_w = 26;
door_h = 40;

module flat(s) rotate([-90, 0, 0]) insert(s);

// Barricades print backing-plate-down: flat first layer, planks on top,
// no supports and no overhangs.
module barricades() {
    // six window barricades
    for (i = [0 : 2]) for (j = [0 : 1])
        translate([i*(ap_w + 2*back_o + 5), j*(ap_h + 2*back_o + 5), back_t])
            rotate([90, 0, 0]) s_barricade();
    // two door barricades alongside
    for (j = [0 : 1])
        translate([3*(ap_w + 2*back_o + 5) + door_w/2 + back_o,
                   j*(door_h + 2*back_o + 5), back_t])
            rotate([90, 0, 0]) s_barricade_door();
}

module window_set() {
    styles = ["glazed", "open", "boarded", "blown"];
    for (i = [0 : 3]) for (j = [0 : 2])
        translate([i*(ap_w + 9), j*(ap_h + 8), 0]) flat(styles[i]);
}

module door_set() {
    for (i = [0 : 1]) translate([i*(ap_w + 9), 0, 0]) flat("door");
    translate([2*(ap_w + 9), 0, plug_t/2]) rotate([-90, 0, 0]) s_door_pin();
    translate([3*(ap_w + 9), 0, plug_t/2]) rotate([-90, 0, 0]) s_door_pin();
}

// Print this FIRST. Four plug widths, notched 1..4 so you can tell them
// apart, to find what actually seats before committing to a full set.
module coupon() {
    for (i = [0 : 3]) {
        w = ap_w - 0.9 + i*0.4;
        translate([i*(ap_w + 9), 0, 0]) rotate([-90, 0, 0]) difference() {
            plug_body(w, ph);
            for (k = [0 : i])
                translate([-w/2 + 1.5 + k*2.2, -flange_t - 0.5, -ph/2 - flange_o - 0.5])
                    cube([1.2, flange_t + 1, 1.6]);
        }
    }
}

render_top = true;
if (render_top) {
    if      (show == "barricades") barricades();
    else if (show == "coupon")     coupon();
    else if (show == "door_set")   door_set();
    else if (show == "single")     flat(style);
    else                           window_set();
}

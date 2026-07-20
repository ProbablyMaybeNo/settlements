// ============================================================
// POP-IN WINDOW INSERTS  for Fallout Terrain "Urban House B Suburbia"
// (and any wall with a ~15.5 x 25.9mm aperture)
//
// WHY THIS IS EASY: the pack already ships "NO WINDOWS" wall files. Despite
// the name those are not solid walls - they are the walls WITH the window
// apertures open and the frame moulding already in place; only the glazing
// is missing. So no mesh surgery is needed at all. We just make plugs.
//
// MEASURED FROM THE SUPPLIED MESHES (slice analysis, not guesswork):
//   aperture   15.1 - 16.0 mm wide  x  25.9 mm tall
//   sill z = 13.8, head z = 39.8, wall thickness ~5.2mm
// The 0.9mm spread across walls is either real variation or slicing noise,
// so PRINT THE TEST COUPON FIRST (show="coupon") to find the size that
// actually seats, then set plug_w and print the real inserts.
//
// Each insert is a PLUG that fills the aperture plus a FLANGE that stops it
// pushing through and hides any slop. Flange goes on the OUTSIDE face.
// Swap inserts to change a building's state mid-game.
// ============================================================

/* [Show] */
show = "plate";   // plate | coupon | single
style = "glazed"; // glazed | open | boarded | blown

/* [Aperture - from the measured meshes] */
ap_w   = 15.5;
ap_h   = 25.9;
wall_t = 5.2;

/* [Fit] */
plug_w    = 15.0;   // set from the coupon result
plug_h    = 25.4;
plug_t    = 3.4;    // shorter than wall_t so it never bottoms out
flange_o  = 1.3;    // flange oversize per side
flange_t  = 1.0;

/* [Detail] */
bar_w   = 1.0;      // muntin bars
frame_w = 1.6;      // inner frame around the pane
pane_t  = 0.8;

$fn = 20;

// ---------- shared body ----------
module plug_body() {
    // flange sits proud on the outside (-Y), plug goes into +Y
    translate([-(plug_w/2 + flange_o), -flange_t, -(plug_h/2 + flange_o)])
        cube([plug_w + 2*flange_o, flange_t + 0.01, plug_h + 2*flange_o]);
    translate([-plug_w/2, 0, -plug_h/2]) cube([plug_w, plug_t, plug_h]);
}

// ---------- styles ----------
// closed window: pane with a cross of muntin bars
module s_glazed() {
    difference() {
        plug_body();
        // hollow out the pane area, leaving a thin backing
        translate([-plug_w/2 + frame_w, pane_t, -plug_h/2 + frame_w])
            cube([plug_w - 2*frame_w, plug_t, plug_h - 2*frame_w]);
    }
    // muntins across the opening
    translate([-bar_w/2, pane_t, -plug_h/2 + frame_w])
        cube([bar_w, plug_t - pane_t, plug_h - 2*frame_w]);
    translate([-plug_w/2 + frame_w, pane_t, -bar_w/2])
        cube([plug_w - 2*frame_w, plug_t - pane_t, bar_w]);
}

// open window: sash slid up, so the lower half is a clear void
module s_open() {
    difference() {
        plug_body();
        translate([-plug_w/2 + frame_w, -flange_t - 1, -plug_h/2 + frame_w])
            cube([plug_w - 2*frame_w, plug_t + flange_t + 2, plug_h - 2*frame_w]);
    }
    // raised sash bunched at the top
    translate([-plug_w/2 + frame_w, pane_t, plug_h/2 - frame_w - 7])
        cube([plug_w - 2*frame_w, plug_t - pane_t, 7]);
    translate([-bar_w/2, pane_t, plug_h/2 - frame_w - 7])
        cube([bar_w, plug_t - pane_t, 7]);
    // sill lip at the bottom of the void
    translate([-plug_w/2 + frame_w, pane_t, -plug_h/2 + frame_w])
        cube([plug_w - 2*frame_w, plug_t - pane_t, 1.4]);
}

// boarded up: planks nailed across
module s_boarded() {
    difference() {
        plug_body();
        translate([-plug_w/2 + frame_w, pane_t, -plug_h/2 + frame_w])
            cube([plug_w - 2*frame_w, plug_t, plug_h - 2*frame_w]);
    }
    for (i = [-1, 0, 1])
        translate([-plug_w/2 - 0.6, pane_t, i*7 - 2.6])
            rotate([0, 0, 0]) rotate([i*4, 0, 0])
                cube([plug_w + 1.2, plug_t - pane_t, 5.2]);
}

// blown out: jagged remains of a frame, mostly void
module s_blown() {
    difference() {
        union() {
            plug_body();
            // a couple of glass shards clinging to the frame
            translate([-plug_w/2 + frame_w, pane_t, plug_h/2 - frame_w - 5])
                cube([4.5, plug_t - pane_t, 5]);
            translate([plug_w/2 - frame_w - 3.5, pane_t, plug_h/2 - frame_w - 8])
                cube([3.5, plug_t - pane_t, 8]);
        }
        translate([-plug_w/2 + frame_w, -flange_t - 1, -plug_h/2 + frame_w])
            cube([plug_w - 2*frame_w, plug_t + flange_t + 2, plug_h - 2*frame_w]);
        // chew the flange edge so it reads as damaged
        for (a = [0 : 5])
            translate([-plug_w/2 + a*3.4 - 1, -flange_t - 1, plug_h/2 + flange_o - 1.2])
                rotate([0, 45, 0]) cube([2.2, flange_t + 3, 2.2]);
    }
}

module insert(s) {
    if      (s == "open")    s_open();
    else if (s == "boarded") s_boarded();
    else if (s == "blown")   s_blown();
    else                     s_glazed();
}

// ---------- print layouts ----------
// lay flat: flange face down on the bed, plug pointing up. No supports.
module flat(s) rotate([-90, 0, 0]) insert(s);

module plate() {
    styles = ["glazed", "open", "boarded", "blown"];
    for (i = [0 : 3]) for (j = [0 : 2])
        translate([i*24, j*34, 0]) flat(styles[i]);
}

// Test coupon: four plug widths so you can find the real fit before
// committing to a full set. Widths are engraved as notch counts on the
// flange edge - 1 notch = smallest.
module coupon() {
    widths = [14.6, 15.0, 15.4, 15.8];
    for (i = [0 : 3])
        translate([i*24, 0, 0]) {
            rotate([-90, 0, 0]) difference() {
                union() {
                    translate([-(widths[i]/2 + flange_o), -flange_t,
                               -(plug_h/2 + flange_o)])
                        cube([widths[i] + 2*flange_o, flange_t + 0.01,
                              plug_h + 2*flange_o]);
                    translate([-widths[i]/2, 0, -plug_h/2])
                        cube([widths[i], plug_t, plug_h]);
                }
                // identifying notches
                for (k = [0 : i])
                    translate([-widths[i]/2 + 1.5 + k*2.2, -flange_t - 0.5,
                               -plug_h/2 - flange_o - 0.5])
                        cube([1.2, flange_t + 1, 1.6]);
            }
        }
}

// set false when this file is `include`d by a fit-check script
render_top = true;
if (render_top) {
    if      (show == "coupon") coupon();
    else if (show == "single") flat(style);
    else                       plate();
}

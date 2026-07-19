// Diagnostic only - not a terrain part.
// Checks that moving parts do not interfere with the body.
// An EMPTY result means the parts only touch (zero shared volume) = good fit.
// A non-empty result is real interference and the part will not move.
//
// test = 0 : roof seated on the walls   (lip must drop in without jamming)
// test = 1 : front door swinging        (sweep vs body)
// test = 2 : back door swinging
// test = 3 : garage door tilting up
// Run: openscad --render -o _ft.stl -D test=N -D ang=NN _fit_test.scad

include <ranch_house.scad>

render_top = false;
test = 0;
ang  = 0;

if (test == 0)
    intersection() {
        house_body();
        translate([0, 0, wtop]) roof();
    }
else if (test == 1)
    intersection() {
        house_body();
        translate([fd_tx, fd_y, ftop]) rotate([0, 0, ang]) swing_door();
    }
else if (test == 2)
    intersection() {
        house_body();
        translate([bd_tx, bd_y, ftop]) rotate([0, 0, 180 - ang]) swing_door();
    }
else
    intersection() {
        house_body();
        translate([gar_op_x0 + 0.5, wall_t/2, ftop + gar_op_h - gar_tube_d/2])
            rotate([ang, 0, 0]) garage_door();
    }

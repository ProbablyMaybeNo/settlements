// Diagnostic only - not a terrain part.
// Intersects the rotated boom arm with the half-space BELOW the base top (z<0).
// Empty result = arm clears the tabletop at that angle.
// NOTE: must use `include` (not `use`) so the parameter values come across.
// Run: openscad --render -o _ct.stl -D test_angle=NN _clearance_test.scad

include <checkpoint_boom_gate.scad>

render_top = false;
test_angle = 85;

intersection() {
    // arm as actually mounted: lifted to the axle height on the post
    translate([0, 0, pivot_h]) rotate([0, -test_angle, 0]) boom_arm();
    // half-space below the base top surface (tabletop)
    translate([-300, -150, -400]) cube([600, 300, 400]);
}

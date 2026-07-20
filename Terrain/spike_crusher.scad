// ============================================================
// ROTATING SPIKE CRUSHER - 28mm industrial hazard terrain
// Spiked roller spins on a 1.6mm (1/16") brass rod
// Crank handle on one end so players can rotate it in-game
// Wire-axle standard: free-spin hole = rod + 0.4mm
//                     press-fit hole (crank) = rod + 0.05mm
// Parts: 2x A-frame stands, 1x roller, 1x crank  + brass rod
// ============================================================

/* [Wire Axle Standard] */
rod_d        = 1.6;            // 1/16" brass rod
spin_hole    = rod_d + 0.4;    // roller + stands: free spin
press_hole   = rod_d + 0.05;   // crank: press fit, glue if needed

/* [Roller] */
roller_d     = 14;
roller_len   = 55;
spike_h      = 5;
spike_base   = 3.5;
spike_rows   = 6;              // rows around circumference
spikes_per_row = 7;

/* [Stands] */
stand_h      = 22;             // axle height above ground
stand_w      = 24;
stand_t      = 6;
base_d       = 30;

/* [Crank] */
crank_arm    = 12;
crank_t      = 4;

$fn = 32;

// -------- roller with spikes --------
module roller() {
    difference() {
        union() {
            cylinder(d=roller_d, h=roller_len, center=true);
            // spike rows
            for (r = [0:spike_rows-1])
                rotate([0, 0, r * 360/spike_rows])
                for (s = [0:spikes_per_row-1])
                    translate([roller_d/2 - 0.5, 0,
                              -roller_len/2 + roller_len/(spikes_per_row+1)*(s+1)
                              + (r%2==0 ? 0 : roller_len/(spikes_per_row+1)/2)])
                        rotate([0, 90, 0])
                            cylinder(d1=spike_base, d2=0.6, h=spike_h);
        }
        // axle bore - free spin
        cylinder(d=spin_hole, h=roller_len + 20, center=true);
    }
}

// -------- A-frame stand --------
module stand() {
    difference() {
        union() {
            // base foot
            translate([0, 0, 1.5]) cube([base_d, stand_t + 6, 3], center=true);
            // upright with rounded top
            hull() {
                translate([0, 0, 3]) cube([stand_w, stand_t, 2], center=true);
                translate([0, 0, stand_h]) rotate([90,0,0])
                    cylinder(d=10, h=stand_t, center=true);
            }
            // rivet detail
            for (x = [-stand_w/3, stand_w/3])
                translate([x, stand_t/2, 6]) rotate([-90,0,0]) cylinder(d=2.5, h=1);
        }
        // axle hole - free spin
        translate([0, 0, stand_h]) rotate([90,0,0])
            cylinder(d=spin_hole, h=stand_t + 12, center=true);
    }
}

// -------- crank handle --------
module crank() {
    difference() {
        union() {
            cylinder(d=8, h=crank_t);                       // hub
            translate([0, -3, 0]) cube([crank_arm, 6, crank_t]); // arm
            translate([crank_arm, 0, 0]) cylinder(d=5, h=crank_t + 6); // grip
        }
        translate([0,0,-1]) cylinder(d=press_hole, h=crank_t + 2); // press-fit bore
    }
}

// -------- assembled preview --------
module assembly() {
    gap = roller_len/2 + stand_t/2 + 2;
    translate([-gap, 0, 0]) rotate([0,0,90]) stand();
    translate([ gap, 0, 0]) rotate([0,0,90]) stand();
    translate([0, 0, stand_h]) rotate([0, 90, 0]) roller();
    // brass rod (shown for reference - not printed)
    color("gold") translate([0, 0, stand_h])
        rotate([0, 90, 0]) cylinder(d=rod_d, h=roller_len + 2*stand_t + 24, center=true);
    translate([gap + stand_t/2 + 4, 0, stand_h]) rotate([0, 90, 0]) crank();
}

assembly();

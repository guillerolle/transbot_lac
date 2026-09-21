module Camera(){
    color("#D0D0D0")
    cube([60, 90, 50], center=true);
    color("#505050")
    translate([30,0,0])
    rotate([0, 90, 0])
    cylinder(h=10, d=40, center=false);
}

Camera();
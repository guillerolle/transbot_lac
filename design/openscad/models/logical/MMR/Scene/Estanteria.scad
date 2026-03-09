use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>

module Estanteria(){
    for (x=[-1, 1])
    for (y=[-1, 1]){
        translate([x*200, y*1000, 0])
        extrude_along([0,0,1], length=2000, center=false)
        RectangularProfileHollow(40, 1.2);
    }
    
    for (z=[100:450:2000]){
        translate([0,0,z])
        cube([400, 2000, 5], center=true); 
    }
}

Estanteria();
module Canasto(length = 470, width = 330, height=220, thickness=5){
    color([.25,.25,.25])
    translate([0, 0, thickness/2]){
        cube([length, width, thickness], center=true);
        
        translate([0, 0, height/2]){
            
            for (y=[1, -1]) {
                translate([0, y*(width/2-thickness/2), 0])
                cube([length, thickness, height], center=true);
            }
            for (x=[1, -1]) {
                translate([x*(length/2-thickness/2), 0])
                cube([thickness, width, height], center=true);
            }
        }
    }
}


Canasto();
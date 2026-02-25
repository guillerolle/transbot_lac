module Wheel(diameter, width, hole=0){
    difference(){
        cylinder(h=width, d=diameter, center=true);
        cylinder(h=width*1.1, d=hole, center=true);
    }
}

Wheel(diameter=160, width=80, hole=40);
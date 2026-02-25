module ControlModule(lod=0){
    // base
    translate([0, 0, 13/2]){
        difference(){
            cube([500, 500, 13], center=true); 
            translate([0,0,-(15-13)/2-2])
            cube([200, 600, 15], center=true);
        }
        
        // ABOVE PLATE
        translate([0,0,13/2]){
            // battery
            color([1, 0, 0])
            translate([-120, -150, 225/2])
            cube([230, 175, 225], center=true); 
            
            
            // raspberry
            translate([150, 150, 17/2])
            color([0, 1, 0])
            cube([86, 54, 17], center=true);
            
            translate([150, 70, 17/2])
            color([0, 0, 1])
            cube([86, 54, 17], center=true);
        }
    }
}



ControlModule(lod=0);
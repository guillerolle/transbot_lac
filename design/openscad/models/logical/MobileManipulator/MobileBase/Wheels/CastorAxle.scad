use <CastorWheel.scad>
module CastorAxle(lod=0, wheelbase=600, tubeprofile=[20, 20], extends=50, castor_angles = [[$t*360, $t*360], [$t*360, $t*360]]){
   if (lod==0) {
        translate([-50, 0, tubeprofile[1]/2])
       cube([tubeprofile[0], wheelbase+extends*2, tubeprofile[1]], center=true);
       
       translate([50, 0, tubeprofile[1]/2])
       cube([tubeprofile[0], wheelbase+extends*2, tubeprofile[1]], center=true);
       
       w=[1, -1];
       for (i=[0:1]){
           translate([0, w[i]*wheelbase/2, 0])
           CastorWheel(castortheta=castor_angles[i][0], wheeltheta=castor_angles[i][1]);
       }
   }
}

module CastorAxleJoint(lod=0, wheelbase=600, tubeprofile=[20, 20], extends=50, axle_x=150, axle_z=50, castor_angles = [[$t*360, $t*360], [$t*360, $t*360]]){
    rotate([90, 0, 0])
    cylinder(h=wheelbase, d=15, center=true);
    
    
    translate([axle_x/2, 0, 0])
    cube([axle_x, tubeprofile[0], tubeprofile[1]], center=true);
    
    translate([axle_x, 0, axle_z/2-tubeprofile[1]/4]){
        cube([tubeprofile[1], tubeprofile[0], axle_z+tubeprofile[1]/2], center=true);
    }
    
    translate([axle_x, 0, axle_z])
    cube([100, 100, 1], center=true);
    
    translate([axle_x, 0, axle_z])
    CastorAxle(lod=lod, wheelbase=wheelbase, tubeprofile=tubeprofile, extends=extends, castor_angles=castor_angles);
}

CastorAxleJoint(wheelbase=600, axle_z=30, axle_x=120);
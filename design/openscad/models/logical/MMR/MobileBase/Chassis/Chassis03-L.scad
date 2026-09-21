use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <RobotUtils/core.scad>


module Chassis03_Double(length=800, width=600, tube_profile=[40,20], bottom_align=false, transversal_beams=[1, 0.33, -0.33, -1], height=700, gap=200, sheet_thickness=3, back_width=0, rounded_front=false)
{
    translate( (bottom_align) ? [0,0,0]:[0,0,-tube_profile[0]/2]) 
    {
        // BOTTOM PLANE
        Chassis03_Plane(length=length, width=width, tube_profile=tube_profile, bottom_align=true, transversal_beams=transversal_beams);
        
        // TOP PLANE
        translate([0, 0, gap]){
            Chassis03_Plane(length=length, width=width, tube_profile=tube_profile, bottom_align=true, transversal_beams=transversal_beams);
            translate([0, 0, tube_profile[0]])
            linear_extrude(height=sheet_thickness)
            square([length, width], center=true);
        }
        
        // SEPARATORS
        for (y=[1, -1]){
            beam3(  [ length/2-tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), tube_profile[0]], 
                    [ length/2-tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), gap],
                0)
            RectangularProfileHollow(tube_profile, 1.2);
        }
       
        // BACK ARC
        for (y=[1, -1]){
            beam3(  [ -length/2+tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), tube_profile[0]], 
                    [ -length/2+tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), height],
                0)
            RectangularProfileHollow(tube_profile, 1.2);
            
            if (back_width>0){ 
                //ReferenceFrame(factor=200);
                beam3(  
                    [ -length/2-tube_profile[0]/2+back_width, y*(-width/2+tube_profile[1]/2), gap+tube_profile[0]], 
                    [ -length/2-tube_profile[0]/2+back_width, y*(-width/2+tube_profile[1]/2), height],
                    0
                )
                RectangularProfileHollow(tube_profile, 1.2);
                
                beam3(  
                    [ -length/2+tube_profile[0], y*(-width/2+tube_profile[1]/2), height-tube_profile[0]/2], 
                    [ -length/2-tube_profile[0]+back_width, y*(-width/2+tube_profile[1]/2), height-tube_profile[0]/2],
                    0
                )
                RectangularProfileHollow(tube_profile, 1.2);
            }
        }
        
        beam3(  [ -length/2+tube_profile[0]/2, (-width/2+tube_profile[1]), height-tube_profile[1]/2],
                [ -length/2+tube_profile[0]/2, -1*(-width/2+tube_profile[1]), height-tube_profile[1]/2],
                0)
        RectangularProfileHollow(tube_profile, 1.2);
        
        if (back_width>0){
            beam3(  
                [ -length/2-tube_profile[0]/2+back_width, (-width/2+tube_profile[1]), height-tube_profile[1]/2],
                [ -length/2-tube_profile[0]/2+back_width, -1*(-width/2+tube_profile[1]), height-tube_profile[1]/2],
                0)
            RectangularProfileHollow(tube_profile, 1.2);
        }
        
        translate([-length/2+((back_width==0)?tube_profile[0]:0)+sheet_thickness+back_width, -width/2, gap])
        {
            difference(){
                rotate([0, -90, 0])
                linear_extrude(height=sheet_thickness)
                square([height-gap, width], center=false);
                
                translate([0, width/2, height-gap-50])
                cube([200,100,50], center=true);
            }
        }
        
        // FRONT ARC
        /*
        for (y=[1, -1])
        for (z=[0, gap]){
            translate([length/2, 0, z])
            rotate([0, 0, 00])
            rotate_extrude(angle=90, convexity=2)
            translate([200, tube_profile[0]/2, 0])
            rotate([0, 0, 90])
            RectangularProfileHollow(tube_profile, 1.2);
        }
        //*/
    }
}


module Chassis03_Plane(length=800, width=600, tube_profile=[40,20], bottom_align=false, transversal_beams=[1, 0.33, -0.33, -1]){
    translate( (bottom_align) ? [0,0,tube_profile[0]/2]:[0,0,0]) {
        for (w=[1, -1]) {
            beam3([-length/2, w*(width/2-tube_profile[1]/2), 0], [+length/2, w*(width/2-tube_profile[1]/2), 0], 0)
            RectangularProfileHollow(tube_profile, 1.2);
        }
        
        for (l=transversal_beams) {
            beam3([l*(length/2-tube_profile[1]/2), -width/2+tube_profile[0]/2, 0],
           [l*(length/2-tube_profile[1]/2), +width/2-tube_profile[0]/2, 0], 90) 
            RectangularProfileHollow(tube_profile, 1.2);
        }

        //beam3([] );
    }
}

translate([0, -1000, 0])
Chassis03_Double(bottom_align=false, tube_profile=[30,20], back_width=200);

Chassis03_Double(bottom_align=false, tube_profile=[30,20]);

translate([0, 1000, 0])
Chassis03_Plane(bottom_align=true, tube_profile=[30,20]);
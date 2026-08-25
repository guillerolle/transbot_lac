use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>


module Chassis03_Double(length=800, width=600, tube_profile=[40,20], bottom_align=false, transversal_beams=[1, 0.33, -0.33, -1], height=700, gap=200){
    Chassis03_L(length=length, width=width, tube_profile=tube_profile, bottom_align=bottom_align, transversal_beams=transversal_beams);
    
    translate([0, 0, gap])
    Chassis03_L(length=length, width=width, tube_profile=tube_profile, bottom_align=bottom_align, transversal_beams=transversal_beams);
    
    for (y=[1, -1]){
        beam3(  [ -length/2+tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), tube_profile[0]/2], 
                [ -length/2+tube_profile[0]/2, y*(-width/2+tube_profile[1]/2), height],
            0)
        RectangularProfileHollow(tube_profile, 1.2);
    }
    beam3(  [ -length/2+tube_profile[0]/2, (-width/2), height+tube_profile[1]/2],
            [ -length/2+tube_profile[0]/2, -1*(-width/2), height+tube_profile[1]/2],
            0)
    RectangularProfileHollow(tube_profile, 1.2);
}


module Chassis03_L(length=800, width=600, tube_profile=[40,20], bottom_align=false, transversal_beams=[1, 0.33, -0.33, -1]){
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

Chassis03_Double(bottom_align=true, tube_profile=[30,20]);
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>

module Chassis02(length=800, width=600, tube_profile=[40,20], bottom_align=false, transversal_beams=[1, 0.33, -0.33, -1]){
    translate( (bottom_align) ? [0,0,tube_profile[0]/2]:[0,0,0]) {
        for (w=[1, -1]) {
            beam3([-length/2, w*(width/2-tube_profile[1]/2), 0], [+length/2, w*(width/2-tube_profile[1]/2), 0], 0)
            RectangularProfileHollow([40,20], 1.2);
        }
        
        for (l=transversal_beams) {
            beam3([l*(length/2-tube_profile[1]/2), -width/2+tube_profile[0]/2, 0],
           [l*(length/2-tube_profile[1]/2), +width/2-tube_profile[0]/2, 0], 90) 
            RectangularProfileHollow([40,20], 1.2);

        }
    }
}

Chassis02(bottom_align=true);
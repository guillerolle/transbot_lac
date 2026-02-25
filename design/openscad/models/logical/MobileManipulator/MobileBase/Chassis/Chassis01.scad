module Chassis01(lod=0, length=800, width=600, tube_profile=[40,20]){
    
    if (lod==0){
        for (l=[1, 0.33, -0.33, -1]) {
            translate(l*[(length/2-tube_profile[1]/2),0,0])
            rotate([0, 90, 90])
            linear_extrude(height=width, center=true)
            square(tube_profile, center=true);
        }
        
        for (w=[1, -1]) {
            translate(w*[0,(width/2-tube_profile[1]/2),0])
            rotate([0, 90, 0])
            linear_extrude(height=length, center=true)
            square(tube_profile, center=true);
        }
    }
}

Chassis01();
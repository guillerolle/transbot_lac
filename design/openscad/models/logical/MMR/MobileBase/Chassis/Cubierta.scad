use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>

module Cubierta(lod=0, length=800, width=600, height=400, tube_profile=20){
    if (lod==0){
        corner_pos = [length/2 - tube_profile/2, width/2 - tube_profile/2];
        
        // POSTES
        for (xy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]){
            translate([corner_pos[0]*xy[0], corner_pos[1]*xy[1], height/2])
            cube([tube_profile, tube_profile, height], center=true);
        }
        
        // LARGUEROS
        for (y = [1, -1]) {
            translate([0, y*corner_pos[1], height-tube_profile/2])    
            cube([length, tube_profile, tube_profile], center=true);
        }
        
        // TRAVESAÑOS
        // TECHO
        for (x = [1, 0, -1]) {
            translate([x*corner_pos[0], 0, height-tube_profile/2])    
            cube([tube_profile, width, tube_profile], center=true);
        }
        // FRENTE/RESPALDO
        for (x = [1]) {
            translate([x*corner_pos[0], 0, height*0.33])    
            cube([tube_profile, width, tube_profile], center=true);
        }
        
        // CHAPA TECHO
        translate([0,0,height])
        cube([length, width, 2], center=true);
    }
}

module Cubierta02(length=800, width=600, height=400, tube_profile=20){
    corner_xy = [length/2 - tube_profile/2, width/2 - tube_profile/2, 0];
    // POSTES
    for (xy = [[1, 1, 0], [1, -1, 0], [-1, -1, 0], [-1, 1, 0]]){
        vertex = v_mul(xy,corner_xy);
        beam3(vertex, vertex+[0,0,height], 0)
        RectangularProfileHollow(tube_profile,1.2);
    }       
    // LARGUEROS
    for (y = [1, -1]) {
        translate([0, y*corner_xy[1], height-tube_profile/2])
        extrude_along([1,0,0], length=length-2*tube_profile)
        RectangularProfileHollow(tube_profile,1.2);
    }  
    
    // TRAVESAÑOS
    // TECHO
    for (x = [1, 0, -1]) {
        translate([x*corner_xy[0], 0, height-tube_profile/2])        
        extrude_along([0,1,0],length=width-2*tube_profile, center=true)
        RectangularProfileHollow(tube_profile,1.2);
    }
    
    // CHAPA TECHO
    translate([0,0,height])
    cube([length, width, 2], center=true);
}

Cubierta();
translate([0,1000,0])
Cubierta02();
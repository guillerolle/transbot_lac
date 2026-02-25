module Portico(width=500, height=1500, thickness=2, side=100){
    for (y=[1, -1]) {
        translate([0, y*(width/2-thickness/2), height/2])
        cube([side, thickness, height], center=true);
    }
    
    translate([0, 0, height])
    cube([side, width, thickness], center=true);
}

module Horquilla(width=500, side=100, thickness=2){
    translate([side/2, 0, 0])
    cube([thickness, width, side], center=true);
    
    for (y=[1, -1]) {
        translate([0, y*(width/2+thickness/2), 0])
        cube([side, thickness, side], center=true);
    }
}

module Unna(length=400, side=75, thickness=2){
    translate([0, 0, -thickness/2]){
        translate([thickness/2, 0, side/2])
        cube([thickness, side, side], center=true);
        
        translate([length/2, 0, 0])
        cube([length, side, thickness], center=true);
    }
}

module Autoelevador(width=500, height=1500, length=400, thickness=4, side=100, unna_side=75, joint_z=sin($t*180)^2, joint_y=cos($t*180)^2, joint_z_lims=[100, 1400], joint_z_0 = 0.2){
    
    color([.9,.5,.5])
    Portico(width=width, height=height, thickness=thickness, side=side);

    translate([0, 0, joint_z_lims[0]+(joint_z_lims[1]-joint_z_lims[0])*joint_z]){
        color([0.3, 0.5, 0.3])
        Horquilla(width=width, side=side, thickness=thickness);

        for (y=[1, -1]){
            translate([50, y*(side/2 + joint_y*(width-2*side)/2),-side/2])
            color([0.5, 0.5, 0.9])
            Unna(length=length, side=unna_side, thickness=thickness);
        }
    }
}

Autoelevador();
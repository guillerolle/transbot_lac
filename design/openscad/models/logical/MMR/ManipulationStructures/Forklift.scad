include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>

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

module MForklift(display="*", prefix="", width=500, height=1500, length=400, thickness=4, side=100, unna_side=75, joint_z=sin($t*180)^2, joint_y=cos($t*180)^2, joint_z_0 = 0.2){
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        _portico();
        
        joint_z_lims=[100, height-100];
        PrismaticJoint(name="pj_horquilla", prefix=prefix, axis=[0,0,1], limits=joint_z_lims){
            _horquilla();

            for (y=[1,-1]){
                PrismaticJoint(name=str_join(["pj_unna", (y+1)/2]), prefix=prefix, axis=[0,y,0], p_translate=[50, y*side/2, -side/2], limits=[ width/2-side, 0])
                //translate([50, y*(side/2 + joint_y*(width-2*side)/2),-side/2])
                _unna();
            }
        }
    } else if(_d=="portico"){
        _portico();
    } else if(_d=="horquilla"){
        _horquilla();
    } else if(_d=="unna"){
        _unna();
    }else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _portico(){
        color([.9,.5,.5])
        Portico(width=width, height=height, thickness=thickness, side=side);
    }
    
    module _horquilla(){
        color([0.3, 0.5, 0.3])
        Horquilla(width=width, side=side, thickness=thickness);
    }
    
    module _unna(){
        color([0.5, 0.5, 0.9])
        Unna(length=length, side=unna_side, thickness=thickness);
    }
}

MForklift();
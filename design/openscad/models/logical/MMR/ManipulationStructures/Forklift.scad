include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>

module Portico(width=500, height=1500, thickness=2, side=100){
    for (y=[1, -1]) {
        translate([0, y*(width/2-thickness/2), height/2-side/2])
        cube([side, thickness, height+side], center=true);
    }
    
    translate([0, 0, height])
    cube([side, width, thickness], center=true);
}

module Horquilla(width=500, side=100, thickness=2){
    translate([side/2+25, 0, 0])
    cube([thickness, width, side], center=true);
    
    for (y=[1, -1]) {
        translate([+12.5, y*(width/2+thickness/2), 0])
        cube([side+25, thickness, side], center=true);
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
        FixedJoint(name="portico", prefix=prefix)
        _portico();
        
        joint_z_lims=[-50, height-100];
        PrismaticJoint(name="horquilla", prefix=str_join([prefix,"/portico"]), axis=[0,0,1], limits=joint_z_lims, command_interfaces=["velocity", "effort"]){
            _horquilla();
            //ReferenceFrame(factor=100);
            
            PrismaticJoint(name="unna0", prefix=str_join([prefix,"/portico/horquilla"]), axis=[0,-1,0], p_translate=[side/2+25, -1*side/2, -side/2], limits=[ width/2-side, 0], command_interfaces=["velocity", "effort"]){
                _unna();
            }
            
            PrismaticJoint(name="unna1", prefix=str_join([prefix,"/portico/horquilla"]), axis=[0,1,0], p_translate=[side/2+25, 1*side/2, -side/2], limits=[ width/2-side, 0], mimic=["unna0"]){
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
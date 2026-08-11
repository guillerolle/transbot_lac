include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>


module Assy_PullingClaw(display="*", prefix="", 
        base_diameter=300, base_height=50, base_thickness=3,
        j_table_limit_high=1500, table_size=[800, 600, 3], 
        slider_claw_axis_z=100, claw_height = 600, joint = [false, false, false]){
            
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        part_baseplate();
        
        PrismaticJoint(name="table", prefix=prefix, p_translate=[0, 0, base_height], limits=[0, j_table_limit_high, 1e9, 1], pos=(joint[0]==false?0:joint[0]),
            command_interfaces=["velocity", "effort"], draw=false){
            part_table();
            //ReferenceFrame(factor=200);
            PrismaticJoint(name="table/slider", prefix=prefix, axis=[1,0,0],
                limits=[-table_size[0]/2, +table_size[0]/2, 1e9, 1], draw=false,
                command_interfaces=["velocity", "effort"], pos=(joint[1]==false?-table_size[0]/2:joint[1])){
                    
                    part_slider();
                    //ReferenceFrame(factor=100);
                    
                    RevoluteJoint(name="table/slider/claw", prefix=prefix, 
                        p_translate=[0,0,slider_claw_axis_z], p_rotate=[-90,0,0], axis=[0,0,1],
                        command_interfaces=["velocity", "effort"], limits=[-90, 90], angle=joint[2], draw=false){
                            //ReferenceFrame(factor=100);
                            part_claw();
                }
            }
        }
        

        
    } else if(_d=="_"){
        part_baseplate();
    } else if(_d=="table"){
        part_table();
    } else if(_d=="slider"){
        part_slider();
    } else if(_d=="claw"){
        part_claw();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module part_baseplate(){
        _baseplate(diameter=base_diameter, height=base_height, thickness=base_thickness);
        
        module _baseplate(thickness, diameter, height){
            cylinder(h = thickness, d = diameter, $fn=30);
            extrude_along(axis=[0,0,1], length=height, center=false)
            CircularProfileHollow(d=diameter*0.1, thickness=3);
            translate([0,0,thickness*2]){
                $fn = 2;
                Arrow3D(from=[diameter*0.1/2, 0, 0], to=[diameter/2, 0, 0]);
                Arrow3D(from=[0, diameter*0.1/2, 0], to=[0, diameter/2, 0]);
            }
        }
    }
    
    module part_table(){
        _table(size=table_size);
        
        module _table(size){
            translate([0, 0, -base_height])
            cylinder(h=base_height, d=base_diameter*0.1-base_thickness, center=false);
            //ReferenceFrame(factor=100);
            translate(-size/2)
            cube([size[0]+100, size[1], size[2]], center=false);
            for (y=[-1, 1]){
                translate([0, y*size[1]/2, 0])
                cube([size[0], size[2], 50], center=true);
            }
        }
    }
    
    module part_slider(){
        _slider(size=[50, 3, 100]);
        
        module _slider(size){
            translate([-size[0]/2, 0, (size[2]-60)/2+30])
            cube(size=[size[1], table_size[1]+4*size[1], size[2]-60], center=true); 
            
            for (y=[-1, 1]){
                translate([0, y*(table_size[1]/2+2*size[1]), size[2]/2-25])
                difference(){
                    cube(size, center=true);
                    translate([0,0,slider_claw_axis_z-(size[2]/2-25)])
                    rotate([90,0,0])
                    cylinder(h = size[2]*2, d=size[0]*.5, center=true);
                }
            }
        }
    }
    
    module part_claw(){
        //ReferenceFrame(factor=100);
        size=[50, 3, claw_height];
        claw_length=50;
        rotate([90, 0, 0]){
            //ReferenceFrame(factor=100);
            for (y=[-1, 1]){
                translate([0, y*(table_size[1]/2+4*size[1]), size[2]/2-size[0]*.5])
                difference(){
                    cube([size[0], size[1], size[2]+size[0]], center=true);
                    translate([0,0,-(size[2]/2-size[0]*.5)])
                    rotate([90,0,0])
                    cylinder(h = size[2]*2, d=size[0]*.5, center=true);
                }
            }
            
            translate([0,0,size[2]]){
                cube(size=[size[0], 2*(table_size[1]/2+4*size[1]), size[1]], center=true);
                translate([claw_length/2, 0, 0])
                cube(size=[claw_length*2, size[0], size[1]], center=true);
            }
        }
    }   

}

display = "*";
Assy_PullingClaw(display=display);
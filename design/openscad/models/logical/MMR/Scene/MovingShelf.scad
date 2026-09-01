use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <../MobileBase/Wheels.scad>

module MovingShelf(display="*", prefix="", length=500, width=500, height=500, tube_profile = [20, 20], sheet_thickness=3, castor_height=130, use_back_sheet=true)
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*")
    {
        _structure();
        FixedJoint(name="castor0", prefix=prefix, p_translate=[length/2,width/2,castor_height])
        _castor();
        FixedJoint(name="castor1", prefix=prefix, p_translate=[-length/2,width/2,castor_height])
        _castor();
        FixedJoint(name="castor2", prefix=prefix, p_translate=[length/2,-width/2,castor_height])
        _castor();
        FixedJoint(name="castor3", prefix=prefix, p_translate=[-length/2,-width/2,castor_height])
        _castor();
        
    } else if (_d=="_") {
        // MAIN LINK 
        _structure();
    } else if (_d=="castor") {
        _castor();
    }
    
    module _structure()
    {
        translate([0, 0, castor_height]){
            for (y = [1, -1])
            for (x = [1, -1])
            {
                beam3([x*(length/2), y*(width/2), 0], [x*(length/2), y*(width/2), height-castor_height], 0)
                RectangularProfileHollow(tube_profile, 1.2);
            }
            translate([0, 0, height-castor_height])
            cube([length+tube_profile[0], width+tube_profile[1], sheet_thickness], center=true);
            if (use_back_sheet){
                translate([length/2+tube_profile[0]/2, 0, height-100-castor_height])
                rotate([0,90,0])
                cube([200, width+tube_profile[1], sheet_thickness], center=true);
            }
        }
    }
    
    module _castor(){
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), ch=castor_height);
    }
}

module Shelf_TrailerType(display="*", prefix="", length=500, width=500, height=500, tube_profile = [20, 20], sheet_thickness=3, castor_height=130, coupler_cube_size=100, coupler_position_z=250, coupler_position_x=200, coupler_hollow_size=80)
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*")
    {
        _structure();
        FixedJoint(name="castor0", prefix=prefix, p_translate=[-length/2,width/2,castor_height])
        _castor();
        FixedJoint(name="castor1", prefix=prefix, p_translate=[-length/2,-width/2,castor_height])
        _castor();
        
    } else if (_d=="_") {
        // MAIN LINK 
        _structure();
    } else if (_d=="castor") {
        _castor();
    }
    
    module _structure()
    {
        translate([0, 0, castor_height]){
            for (y = [1, -1])
            for (x = [-1])
            {
                beam3([x*(length/2), y*(width/2), 0], [x*(length/2), y*(width/2), height-castor_height], 0)
                RectangularProfileHollow(tube_profile, 1.2);
            }            
            for (y = [1, -1])
            for (x = [1])
            {
                beam3([x*(length/2), y*(width/2), -(castor_height)], [x*(length/2), y*(width/2), height-castor_height], 0)
                RectangularProfileHollow(tube_profile, 1.2);
            }
            translate([0, 0, height-castor_height])
            cube([length+tube_profile[0], width+tube_profile[1], sheet_thickness], center=true);
            
            
            translate([0, 0, -castor_height]){
                // BACK SHEET //
                translate([length/2+tube_profile[0]/2, 0, coupler_position_z+coupler_cube_size/2]){
                    // COUPLER ARMS //
                    beam3([0, -width/2, 0], [coupler_position_x+coupler_cube_size/2, -coupler_cube_size/2, 0], 0)
                    RectangularProfileHollow([20,20], 1.2);
                    beam3([0, width/2, 0], [coupler_position_x+coupler_cube_size/2, +coupler_cube_size/2, 0], 0)
                    RectangularProfileHollow([20,20], 1.2);
                    
                    // COUPLER 
                    difference()
                    {
                        union()
                        { 
                        ReferenceFrame(factor=200);
                        rotate([0,90,0])
                        cube([coupler_cube_size, width+tube_profile[1], sheet_thickness], center=true);
                        // COUPLER CUBE //
                        translate([coupler_position_x, 0, 0])
                        cube([coupler_cube_size, coupler_cube_size, coupler_cube_size], center=true);
                       }
                        // COUPLER HOLE //
                        translate([coupler_position_x, 0, 0])
                        rotate([0, 0, 45])
                        cylinder(h=coupler_cube_size*1.1, d1=coupler_hollow_size, d2=coupler_hollow_size*0.8, center=true, $fn=4);
                    }
                }
            }
        }
    }
    
    module _castor(){
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), ch=castor_height);
    }
}

display="*";
length=500;
width=700;
height=500;
use_back_sheet=true;
//MovingShelf(display=display, width=width, length=length, height=height, use_back_sheet=use_back_sheet);
Shelf_TrailerType(display=display, width=width, length=length, height=height);
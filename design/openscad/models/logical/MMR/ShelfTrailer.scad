include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <MobileBase/DifferentialDrives/FourWheels.scad>
use <MobileBase/DifferentialDrives/SixWheels_L.scad>
//use <ManipulationStructures/RobotArm.scad>

module Base_ShelfTrailer(display="*", prefix="", base_length=650, base_width=600, base_height=300, trailer_coupler_x=100, trailer_coupler_size=80, trailer_coupler_height=100, trailer_coupler_z=250, trailer_joint_limit=200, trailer_coupler_reduction=0.6, coupler_fn=4)
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        FixedJoint(name="mobilebase", prefix=prefix)
        _mobilebase();
        
        PrismaticJoint(name="coupler", prefix=prefix, p_translate=[-base_length/2+trailer_coupler_x, 0, base_height], limits=[-5,trailer_joint_limit], pos=0)
        _coupler();
    } else if(_d=="mobilebase"){
        _mobilebase();
    } else if(_d=="coupler"){
        _coupler();
    }
    
    module _mobilebase(){
        DD4W_Rigid(display=_s, prefix=get_full_prefix(prefix, "mobilebase"), 
        bbox=[base_length, base_width, base_height], force_internal_castor=false, differential_suspension="RR", control_module_x=0, fixed_control=false, roof=false);
    }
    
    module _coupler(){
        translate([0, 0, -trailer_coupler_height]){
            cube([trailer_coupler_size*2, trailer_coupler_size*2, 3], center=true);
            /*beam3([0,0,-trailer_coupler_height], [0,0,0], 0)
            RectangularProfileHollow([40,40], 1.2); //*/
            // COUPLER //
            rotate([0, 0, 45])
            cylinder(h=trailer_coupler_height, d1=trailer_coupler_size, d2=trailer_coupler_size*trailer_coupler_reduction, center=false, $fn=coupler_fn);
        }
    }
}


display="*";
coupler_fn=40;
trailer_coupler_size=120;
trailer_coupler_height=150;
trailer_coupler_reduction=0.3;
Base_ShelfTrailer(display=display, coupler_fn=coupler_fn, trailer_coupler_size=trailer_coupler_size, trailer_coupler_height=trailer_coupler_height, trailer_coupler_reduction=trailer_coupler_reduction);
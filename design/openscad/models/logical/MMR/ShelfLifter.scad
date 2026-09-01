include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <MobileBase/DifferentialDrives/FourWheels.scad>
use <MobileBase/DifferentialDrives/SixWheels_L.scad>
//use <ManipulationStructures/RobotArm.scad>


module ShelfLifter(display="*", prefix="", base_length=650, base_width=600, base_height=300)
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        FixedJoint(name="mobilebase", prefix=prefix)
        _mobilebase();
        
        PrismaticJoint(name="lifter", prefix=prefix, p_translate=[0, 0, base_height], limits=[-5,100], pos=0, command_interfaces=["velocity", "effort"])
        _lifter();
    } else if(_d=="mobilebase"){
        _mobilebase();
    } else if(_d=="lifter"){
        _lifter();
    }
    
    module _mobilebase(){
        DD4W_Rigid(display=_s, prefix=get_full_prefix(prefix, "mobilebase"), 
        bbox=[base_length, base_width, base_height], force_internal_castor=false, differential_suspension="RR", control_module_x=0, fixed_control=false, roof=false);
    }
    
    module _lifter(){
        cube([base_length, base_width*2/3, 3], center=true);
        for (y=[1,-1])
        for (x=[1,-1]){
            beam3([x*(base_length/3),y*(base_width/4),-100], [x*(base_length/3),y*(base_width/4),0], 0)
            RectangularProfileHollow([40,40], 1.2);
        }
    }
}

display="*";
ShelfLifter(display=display);
include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <MobileBase/DifferentialDrives/FourWheels.scad>
use <MobileBase/DifferentialDrives/SixWheels_L.scad>
//use <ManipulationStructures/RobotArm.scad>


module LType(display="*", prefix="")
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        _mobilebase();
    }
    
    module _mobilebase(){
        DD4W_Rigid(display=_s, prefix=get_full_prefix(prefix, "mobilebase"), bbox=[650, 600, 300], force_internal_castor=false, differential_suspension="RR");
    }
}


display="*";

LType(display=display);
include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <MobileBase/DifferentialDrives/FourWheels.scad>
use <ManipulationStructures/Forklift.scad>

module Forklift(display="*", prefix="", bbox=[800, 600, 2000], display_bbox=false, cwheel_h=130, differential_axle_suspension=""){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        if (display_bbox){
            translate([0, 0, bbox[2]/2])
            %cube(bbox, center=true);
        }
        
        
        FixedJoint(name="fj_mobilebase", prefix=prefix)
        _mobilebase();
        
        
        PrismaticJoint(name="pj_manipulator", prefix=prefix, p_translate=[+bbox[0]/2-50, 0, cwheel_h], axis=[-1,0,0], limits=[0, bbox[0]-100])
        _manipulator();
        
    } else if(_d=="mobilebase"){
        _mobilebase();
    } else if(_d=="manipulator"){
        _manipulator();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _mobilebase(){
        mirror([1,0,0])
        DD4W_Rigid(display=_s, prefix=get_full_prefix(prefix, "mobilebase"), bbox=[bbox[0], bbox[1], 450], cwheel_h=cwheel_h, force_internal_castor=false, differential_suspension=differential_axle_suspension);
    }
    
    module _manipulator(){
        MForklift(display=_s, prefix=get_full_prefix(prefix, "manipulator"), height=bbox[2]-cwheel_h, width=bbox[1]+50, length=bbox[0]-100);
    }
}

display="*";
extra_wide=false;
differential_axle_suspension = "";
Forklift(display=display, bbox=[800, extra_wide? 800:600, 2000], display_bbox=false, differential_axle_suspension=differential_axle_suspension);
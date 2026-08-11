include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <MobileBase/DifferentialDrives/FourWheels.scad>
use <ManipulationStructures/PullingClaw.scad>

module MobileManipulator(display="*", prefix="", bbox=[800, 600, 2000], display_bbox=false, cwheel_h=130, differential_axle_suspension="", force_internal_castor=false, manipulator_joints=[false, false, false]){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        if (display_bbox){
            translate([0, 0, bbox[2]/2])
            %cube(bbox, center=true);
        }
        
        
        FixedJoint(name="mobilebase", prefix=prefix, p_rotate=[0,0,180])
        _mobilebase();
        
        
        FixedJoint(name="manipulator", prefix=prefix, p_translate=[+bbox[0]*1/4, 0, 450])
        _manipulator();
        
    } else if(_d=="mobilebase"){
        _mobilebase();
    } else if(_d=="manipulator"){
        _manipulator();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _mobilebase(){
        // mirror([1,0,0])
        DD4W_Rigid(display=_s, prefix=get_full_prefix(prefix, "mobilebase"), bbox=[bbox[0], bbox[1], 450], cwheel_h=cwheel_h, force_internal_castor=force_internal_castor, differential_suspension=differential_axle_suspension);
    }
    
    module _manipulator(){
        Assy_PullingClaw(display=_s, prefix=get_full_prefix(prefix, "manipulator"), joint=manipulator_joints, j_table_limit_high=1000);
    }
}

display="*";
extra_wide=false;
differential_axle_suspension = "";
force_internal_castor = false;
manipulator_joints = [500, 250, 90];
MobileManipulator(display=display, bbox=[800, extra_wide? 800:600, 1500], display_bbox=false, differential_axle_suspension=differential_axle_suspension, force_internal_castor=force_internal_castor, manipulator_joints=manipulator_joints);
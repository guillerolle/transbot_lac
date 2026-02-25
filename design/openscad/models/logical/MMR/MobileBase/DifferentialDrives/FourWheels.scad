use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <DifferentialModule/DifferentialModule.scad>
use <../Wheels.scad>
use <../Chassis/Chassis02.scad>
use <../Chassis/Cubierta.scad>
use <../ControlModule/ControlModule.scad>

module DD4W_Rigid(display="*", prefix="", display_bbox=false, bbox=[800, 600, 450], floor_clearance=100, fwheel_d=120, fwheel_w=40, daxle_d=20, cwheel_d=120, cwheel_w=45, cwheel_h=130, cwheel_f=100, cwheel_cd=40, force_internal_castor=true, differential_suspension="", double_bar_offset = 100){
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    floor_clearance=cwheel_h;
    daxle_t = bbox[1];
    
    if (_d=="*"){
        if (display_bbox){
            translate([0, 0, bbox[2]/2])
            %cube(bbox, center=true);
        }
        
        FixedJoint(name="fj_chassis", prefix=prefix, p_translate=[0,0,floor_clearance])
        _chassis();
        
    if (differential_suspension==""){
        FixedJoint(name="fj_diffmodule", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2*1.5, 0, fwheel_d/2])
        _diffmodule();
    } else if (differential_suspension=="P") {
        PrismaticJoint(name="pj_diffmodule", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2*1.5, 0, fwheel_d/2], axis=[0,0,1], limits=[0,-50]){
        ReferenceFrame(factor=100);
        _diffmodule();
        }
    } else if (differential_suspension=="RR") {
        ContinuousJoint(name="rj_diff_1", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2*1.5+double_bar_offset, 0, fwheel_d/2], axis=[0,1,0]){
            _doublebar();
            ContinuousJoint(name="rj_diff_2", prefix=prefix, p_translate=[-double_bar_offset, 0, 0], axis=[1,0,0]){
                _diffmodule();
            }
        }
    }
    
        FixedJoint(name="fj_castor0", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?-(-bbox[1]/2+cwheel_d/2+cwheel_cd):-(-bbox[1]/2+cwheel_f/2), cwheel_h]){
        _castor();
        }
    
        FixedJoint(name="fj_castor1", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?+(-bbox[1]/2+cwheel_d/2+cwheel_cd):+(-bbox[1]/2+cwheel_f/2), cwheel_h])
        _castor();
        
        PrismaticJoint(name="pj_control", prefix=prefix, p_translate=[0,0,floor_clearance+40], axis=[1,0,0], limits=[0, 500])
        _controlmodule();
        
    } else if (_d=="_") {
        // MAIN LINK 
    } else if (_d=="chassis") {
        _chassis();
    } else if (_d=="diff") {
        _diffmodule();
    } else if (_d=="doublebar") {
        _doublebar();
    } else if (_d=="castor") {
        _castor();
    } else if (_d=="control") {
        _controlmodule();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _doublebar(){
        extrude_along(axis=[0,1,0], length=bbox[1]*.8)
        CircularProfileHollow(d=15, thickness=1);
        extrude_along(axis=[-1,0,0], length=double_bar_offset, center=false)
        CircularProfileHollow(d=15, thickness=1);
    }
    
    module _diffmodule(){
        DifferentialModule(display=_s, prefix=get_full_prefix(prefix, "diffmodule"), track=(differential_suspension=="RR")? daxle_t-60: daxle_t, wheel_diam=fwheel_d, wheel_width=fwheel_w);
    }  
    
    module _castor(){
        rotate([0,0,180])
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), wd=cwheel_d, ww=cwheel_w, wh=20, ch=cwheel_h, cf=cwheel_f, cd=cwheel_cd);
    }
    
    module _chassis(){
        Chassis02(length=bbox[0], width=bbox[1], bottom_align=true);
        translate([0, 0, 40])
        mirror([1,0,0])
        Cubierta02(length=bbox[0], width=bbox[1], height=bbox[2]-floor_clearance-40);
    }
    
    module _controlmodule(){
        rotate([0,0,-90])
        ControlModule();
    }
}


/*
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=false);

translate([0,1000,0])
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=true);
//

translate([0,2000,0])
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=false, differential_suspension="P");
// */

translate([0,3000,0])
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=false, differential_suspension="RR");
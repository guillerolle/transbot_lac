use <RobotUtils/core.scad>
use <../Wheels.scad>
use <DifferentialModule/DifferentialModule.scad>


module RigidTricycle(display="*", prefix="", bbox=[800, 600, 300], fwheel_d=120, fwheel_w=40, daxle_d=20, daxle_t=600, floor_clearance=100, cwheel_h=130, display_bbox=true){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        if (display_bbox){
            translate([0, 0, bbox[2]/2])
            %cube(bbox, center=true);
        }
        
        FixedJoint(name="jf_chassis", prefix=prefix, p_translate=[0, 0, bbox[2]/2+floor_clearance/2])
        %_chassis();
        
        FixedJoint(name="jf_diffmodule", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2, 0, fwheel_d/2])
        _diffmodule();
        
        FixedJoint(name="jf_caster0", prefix=prefix, p_translate=[+bbox[0]/2-fwheel_d/2, 0, cwheel_h])
        _castor();
        
    } else 
    if (_d=="chassis"){
        _chassis();
    } else
    if (_d=="diffmodule"){
        _diffmodule();
    } else
    if (_d=="castor"){
        _castor();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _castor(){
        rotate([0,0,180])
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), wh=20, ch=cwheel_h);
    }
    
    module _chassis(){
      cube(bbox-[0,0,floor_clearance], center=true);
    }  
    
    module _diffmodule(){
        DifferentialModule(display=_s, prefix=get_full_prefix(prefix, "diffmodule"), track=daxle_t, wheel_diam=fwheel_d, wheel_width=fwheel_w);
    }  
}


RigidTricycle(display="*", display_bbox=false, fwheel_d=200, fwheel_w=60);
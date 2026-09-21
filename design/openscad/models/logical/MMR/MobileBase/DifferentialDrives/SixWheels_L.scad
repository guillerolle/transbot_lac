use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <DifferentialModule/DifferentialModule.scad>
use <../Wheels.scad>
use <../Chassis/Chassis02.scad>
use <../Chassis/Chassis03-L.scad>
use <../Chassis/Cubierta.scad>
use <../ControlModule/ControlModule.scad>
use <../../Sensors/Camera.scad>
use <../../Sensors/Lidar.scad>

module DD6W_L(display="*", prefix="", display_bbox=false, bbox=[800, 600, 450], floor_clearance=100, fwheel_d=120, fwheel_w=40, daxle_d=20, cwheel_d=120, cwheel_w=45, cwheel_h=130, cwheel_f=100, cwheel_cd=40, force_internal_castor=true, differential_suspension="", double_bar_offset = 100, fixed_control=false, back_width=0, back_height=600, gap=150, castor_suspension="F"){
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    echo(_xdisp);
    
    floor_clearance=cwheel_h;
    daxle_t = bbox[1];
    
    if (_d=="*"){
        if (display_bbox){
            translate([0, 0, bbox[2]/2])
            %cube(bbox, center=true);
        }
        
        FixedJoint(name="chassis", prefix=prefix, p_translate=[0,0,floor_clearance])
        _chassis();
        
    if (differential_suspension==""){
        FixedJoint(name="diff", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2*1.5+double_bar_offset, 0, fwheel_d/2])
        _diffmodule();
        
    } else if (differential_suspension=="P") {
        PrismaticJoint(name="diff", prefix=prefix, p_translate=[-bbox[0]/2+fwheel_d/2*1.5+double_bar_offset, 0, fwheel_d/2], axis=[0,0,1], limits=[0,-50], draw=true){
        ReferenceFrame(factor=100);
        _diffmodule();
        }
        
    } else if (differential_suspension=="RR") {
        //ReferenceFrame(factor=200);
        RevoluteJoint(name="doublebar", prefix=prefix, 
        p_translate=[-100+fwheel_d/2*1.5+double_bar_offset, 0, fwheel_d*3/8],
        axis=[0,1,0], spring=[50], damping=[2], limits=[-10,10], draw=true){
            _doublebar();
            }
        }

    if (castor_suspension=="F"){
        FixedJoint(name="castor0", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?-(-bbox[1]/2+cwheel_d/2+cwheel_cd):-(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180]){
        _castor();
        }

        FixedJoint(name="castor1", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?+(-bbox[1]/2+cwheel_d/2+cwheel_cd):+(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180])
        _castor();
        
        FixedJoint(name="castor2", prefix=prefix, p_translate=[-1*(+bbox[0]/2-cwheel_f/2), (force_internal_castor)?-(-bbox[1]/2+cwheel_d/2+cwheel_cd):-(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180]){
        _castor();
        }

        FixedJoint(name="castor3", prefix=prefix, p_translate=[-1*(+bbox[0]/2-cwheel_f/2), (force_internal_castor)?+(-bbox[1]/2+cwheel_d/2+cwheel_cd):+(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180])
        _castor();
    } else if (castor_suspension=="P"){
        PrismaticJoint(name="castor0", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?-(-bbox[1]/2+cwheel_d/2+cwheel_cd):-(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180], limits=[-50, 50], spring=[10], damping=[0.1], draw=false){
        _castor();
        }

        PrismaticJoint(name="castor1", prefix=prefix, p_translate=[+bbox[0]/2-cwheel_f/2, (force_internal_castor)?+(-bbox[1]/2+cwheel_d/2+cwheel_cd):+(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180], limits=[-50, 50], spring=[10], damping=[0.1] )
        _castor();
        
        PrismaticJoint(name="castor2", prefix=prefix, p_translate=[-1*(+bbox[0]/2-cwheel_f/2), (force_internal_castor)?-(-bbox[1]/2+cwheel_d/2+cwheel_cd):-(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180], limits=[-50, 50], spring=[10], damping=[0.1] ){
        _castor();
        }

        PrismaticJoint(name="castor3", prefix=prefix, p_translate=[-1*(+bbox[0]/2-cwheel_f/2), (force_internal_castor)?+(-bbox[1]/2+cwheel_d/2+cwheel_cd):+(-bbox[1]/2+cwheel_f/2), cwheel_h], p_rotate=[0,0,180], limits=[-50, 50], spring=[10], damping=[0.1] )
        _castor();
    }
    
    
    if (fixed_control==false) {
        PrismaticJoint(name="control", prefix=prefix, p_translate=[-75,0,floor_clearance+40], p_rotate=[0, 0, +90], axis=[0,1,0], limits=[0, 500], pos=0, command_interfaces=["position"], spring=[200], damping=[10], friction=[10])
        _controlmodule();
    } else {
        FixedJoint(name="control", prefix=prefix, p_translate=[75,0,floor_clearance+40], p_rotate=[0,0,90])
        _controlmodule();
    }
    
    FixedJoint(name="camera", prefix=prefix, p_translate=[-bbox[0]/2+back_width-30,0,back_height+gap-70], p_rotate=[0,0,0])
    _camera();
    
    FixedJoint(name="lidar", prefix=prefix, p_translate=[bbox[0]/2-100,0,cwheel_h+40], p_rotate=[0,0,0])
    _lidar();
        
    } else if (_d=="_") {
        // MAIN LINK 
    } else if (_d=="chassis") {
        _chassis();
    } else if ((_d=="diff")){
       _diffmodule();
    /*} else if ((_d=="doublebar") && (_s=="diff")) {
        _xdisp = extract_assembly_parts(_s);
        _d = _xdisp[0];
        _s = _xdisp[1];
        echo(_xdisp);
        _diffmodule(display=_s);*/
    } else if (_d=="doublebar") {
        _doublebar(display=_s);
    } else if (_d=="castor") {
        _castor();
    } else if (_d=="control") {
        _controlmodule();
    } else if (_d=="camera") {
        _camera();
    } else if (_d=="lidar") {
        _lidar();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _doublebar(display=display){
        _xdisp = extract_assembly_parts(display);
        _d = _xdisp[0];
        _s = _xdisp[1];
        echo("_doublebar()|", _d, _s);
        
        if (_d=="*"){
            __doublebar();
            RevoluteJoint(name="diff", prefix=str_join([prefix, "doublebar"]), p_translate=[-double_bar_offset, 0, 0], axis=[1,0,0], limits=[-5, 5],
            spring=[50], damping=[2], draw=true){
                _diffmodule(display=_s, prefix=str_join([prefix, "doublebar"]));
            }
        } else if (_d=="_"){
            __doublebar();
        } else if (_d=="diff"){
            _diffmodule(display=_s, prefix=str_join([prefix, "doublebar"]));
        }
        module __doublebar(){
            extrude_along(axis=[0,1,0], length=bbox[1]*.8)
            CircularProfileHollow(d=15, thickness=1);
            extrude_along(axis=[-1,0,0], length=double_bar_offset, center=false)
            CircularProfileHollow(d=15, thickness=1);
        }
    }
    
    module _diffmodule(display=_s, prefix=prefix){
        DifferentialModule(display=display, prefix=get_full_prefix(prefix, "diff"), track=(differential_suspension=="RR")? daxle_t-60: daxle_t, wheel_diam=fwheel_d, wheel_width=fwheel_w);
    }  
    
    module _castor(){
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), wd=cwheel_d, ww=cwheel_w, wh=20, ch=cwheel_h, cf=cwheel_f, cd=cwheel_cd);
    }
    
    module _chassis(){
        Chassis03_Double(length=bbox[0], width=bbox[1], bottom_align=true, gap=gap, back_width=back_width, height=back_height);
    }
    
    module _controlmodule(){
        //rotate([0,0,-90])
        ControlModule();
    }
    
    module _camera(){
        Camera();
    }
    
    module _lidar(){
        Lidar();
    }
}



/*DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=false);

translate([0,1000,0])
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=true);
// */

/*translate([0,2000,0])
DD4W_Rigid(display="*", display_bbox=false, force_internal_castor=false, differential_suspension="P");
// */

display="*";
castor_suspension="P";
translate([0,0,0])
DD6W_L(display=display, display_bbox=false, force_internal_castor=false, differential_suspension="RR", back_width=150, castor_suspension=castor_suspension); //*/
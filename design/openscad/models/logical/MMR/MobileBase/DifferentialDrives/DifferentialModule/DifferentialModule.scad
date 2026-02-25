use <RobotUtils/core.scad>
use <../../Wheels.scad>


module DifferentialModule(display="*", prefix="", track=600, wheel_diam=120, wheel_width=45, shaft=20){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        _baselink();
        
        // WHEELS 
        for (w=[-1, 1]) {
            ContinuousJoint(name=str_join(["cj", (w+1)/2]), prefix=prefix, p_translate=w*[0, track/2-wheel_width/2, 0], p_rotate=[-90, 0, 0], axis=[0,0,1])
            _wheel();
        }
    } else
    if (_d=="_"){
        _baselink();
    } else 
    if (_d=="wheel"){
        _wheel();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    
    module _baselink(){
        rotate([90, 0, 0])
        cylinder(h=track+wheel_width*0.5, d=shaft, center=true);
    }
    
    module _wheel(){
        FixedWheel(d=wheel_diam, w=wheel_width, h=shaft+1);
    }
}


DifferentialModule(display="*", track=400, wheel_diam=160, wheel_width=30);
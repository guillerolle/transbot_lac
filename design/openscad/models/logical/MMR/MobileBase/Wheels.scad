use <RobotUtils/core.scad>

module FixedWheel(d, w, h, $fn=60){
    /*
        params:
            d: diameter
            w: width
            h: hole diameter
    */
    difference(){
        color([.3,.3,.3])
        cylinder(d=d, h=w, center=true);
        cylinder(d=h, h=w*1.1, center=true);
    }
}

module CastorWheel(display="*", prefix="", wd=120, ww=40, wh=0, cd=40, ch=130, cf=100){
    /*
        params:
            wd: wheel diameter
            ww: wheel width
            wh: wheel hole diameter
            cd: castor distance
            ch: castor height (full height of castor assembly)
            cf: castor flange size (plate size)
    */
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        _baselink();
        ContinuousJoint(name="arm", prefix=prefix, p_translate=[0, 0, -(ch-wd)], axis=[0,0,1]){
            _castorarm();
            // CASTOR JOINT
            translate([0, 0, +(ch-wd)/2])
            color([1,0,0])
            cylinder(h=ch-wd, d=10, center=true);
                
            ContinuousJoint(name="wheel", prefix=str_join([prefix, "/arm"]),p_translate=[cd, 0, -wd/2], p_rotate=[90,0,0], axis=[0,0,1]){
                _wheel();

            }
        }
    } else if (_d=="_") {
        _baselink();
    } else if (_d=="arm") {
        _castorarm();
    } else if (_d=="wheel") {
        _wheel();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    module _wheel(){
        FixedWheel(d=wd, w=ww, h=wh);
    }
    
    module _baselink(){
        cube([cf, cf, 1], center=true);
    }
    
    module _castorarm(){
        module _halfarm(){
            hull(){
                translate([0, ww/2*1.25, 0])
                mirror([0,0,1]){
                    rotate([90, 0, 0])
                    cube([cd+wh/2, cd*.5, 1], center=false);
                    
                    translate([cd+wh/2, 0, 0])
                    //mirror([-1,0,0])
                    rotate([90, -90, 0])
                    cube([wd/2+wh/2, cd*.5, 1], center=false);
                }
            }
        }
        
        difference(){
            union(){
                _halfarm();
                mirror([0,1,0])
                _halfarm();
                cube([ww*0.5, ww*1.25, 1], center=true);
            }
            
            translate([cd, 0, -wd/2])
            rotate([90,0,0])
            cylinder(h=ww*1.5, d=wh*.5+1, center=true);
        }
        
    }
}

rotate([90, 0, 0])
FixedWheel(d=120, w=40, h=20);

translate([0, 100, 150])
CastorWheel(display="*", wh=20);
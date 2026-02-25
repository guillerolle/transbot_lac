include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>

use <Soporte.scad>


module Wheel(diam=120, width=40, hole=20){
    rotate([90,0,0])
    difference(){
        cylinder(h=width, d=diam, center=true);
        cylinder(h=width*1.1, d=hole, center=true);
    }
}

module WheelWithSatellite(wdiam=120, wwidth=40, whole=20, satheight=100, satlength=100, satdiam=10, display="*", prefix=""){
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*" || _d=="_"){ 
        Wheel(wdiam, wwidth, whole);
    }
    
    if (_d=="satellite_link")
        satellite_link();
    
    if (_d=="*"){
        RevoluteJoint(name="satellite_joint", prefix=prefix, p_translate=[0,0,wdiam/2], axis=[0,0,1]){
            satellite_link();
        }
    }
    
    module satellite_link(){
        cylinder(h=satheight-wdiam/2, d=satdiam, center=false);
        translate([0, 0, satheight-wdiam/2])
        rotate([90,0,0])
        cylinder(h=satlength, d=satdiam, center=true);
    }
}

module Axle(diam=20, length=500){
    rotate([90,0,0])
    cylinder(h=length, d=diam, center=true);
}

module Assembly(axle_length=500, axle_diam=20, wheel_diam = 120, wheel_width=40, display="*", prefix=""){
    
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        Axle();
       
        RevoluteJoint(name="left_wheel_joint", prefix=prefix, p_translate=[0, axle_length/2, 0], axis=[0,0,1])
        left_wheel();
        
        RevoluteJoint(name="right_wheel_joint", prefix=prefix, p_translate=[0, -axle_length/2, 0], axis=[0,1,0])
        right_wheel();
    }
    
    if (_d=="_")
        Axle();
 
    if (_d=="left_wheel")
        left_wheel();
    
    if (_d=="right_wheel")
        right_wheel();
    
    module left_wheel(){
        WheelWithSatellite(wdiam=150, display=_s, prefix=get_full_prefix(prefix, "left_wheel"));
    }
    
    module right_wheel(){
        Wheel(diam=80);
    }
}


module DobleEje(display="*", prefix="", largo=600, altura=150, radio=120, soporte=40){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        
        Chasis();
        
        
       FixedJoint(name=str_join(["fixed_soportes"]), p_translate=[400,0,300])
        _soporte();
        
        FixedJoint(p_translate=[150,0,300])
        _soporte_trasero();
        
        PrismaticJoint(name="rodillo_susp_joint", p_translate=[0, 0, 0], axis=[0,0,-1])
        RevoluteJoint(name="rodillo_joint", p_translate=[200+0.25*largo,0,100+altura/2+radio], axis=[0,0,1], p_rotate=[90,0,0])
        rodillo();
        
        Assembly(display="*", prefix="eje_trasero");

        RevoluteJoint(name="eje2", p_translate=[400,0,0], axis=[1,0,0], angle=sin($t*360)*45)
        _eje_delantero();
    }
    
    if (_d=="_"){
        Chasis();
    }    
    
    if (_d=="rodillo"){
        rodillo();
    }
 
    if (_d=="soporte"){
        _soporte();
    }
     
    if (_d=="soporte_trasero"){
        _soporte_trasero();
    }
    
    if (_d=="eje_delantero"){
        _eje_delantero();
    }
    
    module _eje_delantero(){
        Assembly(display=_s, prefix="eje_delantero");
    }

    module _soporte(){
        for (y=[-150, 0, 150]){
            translate([0,y,0])
            Soporte(lado=soporte);
        }
    }
    
    module _soporte_trasero(){
        Soporte(lado=soporte/2);
    }
    
    module Chasis(){
        translate([200, 0, 100])
        cube([largo, 300, altura], center=true);
    }
    
    module rodillo(){
        cylinder(h=200, d=radio*2, center=true);
    }
}

DobleEje(display="*", largo=300, radio=120, soporte=100);

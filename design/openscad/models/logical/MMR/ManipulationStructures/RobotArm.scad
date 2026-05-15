include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>

module base_link(){
    difference(){
        cylinder(h = 250, d = 100);
        cylinder(h = 270, d = 80);
    }
    cylinder(h = 10, d = 250);
}

module link1(){
    difference(){
        cylinder(h = 250, d = 80);
        cylinder(h = 270, d = 60);
    }
    cylinder(h = 5, d=80);
    translate([100, -60, 200]){
        rotate([0, 90, 0]){
            difference(){
                cylinder(h = 250, d = 100, center=true);
                cylinder(h = 270, d = 80, center=true);
            }
        }
    }
}

module link2(){
    difference(){
        cylinder(h = 250, d = 80);
        cylinder(h = 270, d = 60);
    }    
    cylinder(h = 5, d=80);
    translate([100, -60, 200]){
        rotate([0, 90, 0]){
            difference(){
                cylinder(h = 250, d = 100, center=true);
                cylinder(h = 270, d = 80, center=true);
            }
        }
    }
}

module link3(){
    difference(){
        cylinder(h = 250, d = 80);
        cylinder(h = 270, d = 60);
    }    
    cylinder(h = 5, d=80);
    translate([80, -60, 200]){
        rotate([0, 90, 0]){
            difference(){
                cylinder(h = 200, d = 50, center=true);
                cylinder(h = 210, d = 40, center=true);
            }
        }
    }
}

module RobotArm(display="*", prefix=""){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    
    if (_d=="*"){
        FixedJoint(name="link0", prefix=prefix)
        _link0();   
       
       ContinuousJoint(name="link1", prefix=str_join([prefix,"link0"]), p_translate=[0, 0, 200], axis=[0,0,1], 
        command_interfaces=["position","velocity","effort"]){
          _link1();
           
          ContinuousJoint(name="link2", prefix=str_join([prefix,"link0/link1"]), p_translate=[100, -60, 200], p_rotate=[90,0,90],axis=[0,0,1], 
           command_interfaces=["position","velocity","effort"]){
          _link2();
              ContinuousJoint(name="link3", prefix=str_join([prefix,"link0/link1/link2"]), p_translate=[100, -60, 200], p_rotate=[90,0,90],axis=[0,0,1], 
              command_interfaces=["position","velocity","effort"]){
              _link3();
               }
           }
       } 
        
    } else if(_d=="link0"){
        _link0();
    } else if(_d=="link1"){
        _link1();
    } else if(_d=="link2"){
        _link2();
    } else if(_d=="link3"){
        _link3();
    } else {
        echo(str_join(["Unknown component: <", _d, ">"]));
    } 
    
    
    module _link0(){
        color([1, 0, 0])
        base_link();
    }
    
    module _link1(){
        //ReferenceFrame(factor=200);
        color([0, 1, 0])
        link1();
    }
    
    module _link2(){
        //ReferenceFrame(factor=200);
        color([0, 0, 1])
        link2();
    }
    
    module _link3(){
        //ReferenceFrame(factor=200);
        color([1, 1, 0])
        link3();
    }
}



RobotArm(display="*");
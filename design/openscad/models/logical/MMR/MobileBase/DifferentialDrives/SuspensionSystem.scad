use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <DifferentialModule/DifferentialModule.scad>
use <../Wheels.scad>
use <../Chassis/Chassis02.scad>
use <../Chassis/Cubierta.scad>
use <../ControlModule/ControlModule.scad>

length = 500;
width = 300;
wdiam = 80;
sqsection = 20;
height = sqsection;

module FullRigid(){
    ReferenceFrame(factor=200);
    /*
    Chassis02(bottom_align=true);
    translate([0, 0, 40])
    mirror([1,0,0])
    Cubierta02(); //*/
    translate([0,0,-height])
    for(x=[length/2,-length/2]){
        for(y=[width/2,-width/2]){
            translate([x, y, 0]){
                ReferenceFrame(factor=150);
                rotate([90, 0, 0])
                color([0.2,0.2,0.2])
                cylinder(h=30, d=80, center=true);
            }
        }
        beam2([x, width/2, 0], [x, -width/2, 0], 0)
        square(sqsection, center=true);
    }
    beam2([length/2+sqsection/2, width*.3, 0], [-length/2-sqsection/2, width*.3, 0], 0)
    square(sqsection, center=true);
    beam2([length/2+sqsection/2, -width*.3, 0], [-length/2-sqsection/2, -width*.3, 0], 0)
    square(sqsection, center=true);
}

module SemiRigid(){
    ReferenceFrame(factor=200);
    /*
    Chassis02(bottom_align=true);
    translate([0, 0, 40])
    mirror([1,0,0])
    Cubierta02(); //*/
    translate([0,0,-height]){
        for(x=[-length/2]){
            for(y=[width/2,-width/2]){
                translate([x, y, 0]){
                    ReferenceFrame(factor=150);
                    rotate([90, 0, 0])
                    color([0.2,0.2,0.2])
                    cylinder(h=30, d=80, center=true);
                }
            }
            beam2([x, width/2, 0], [x, -width/2, 0], 0)
            square(sqsection, center=true);
        }
        beam2([length/2, width*.3, sqsection], [length/2, -width*.3, sqsection], 0)
        square(sqsection, center=true);
        
        translate([0, 0, sqsection]){
            beam2([length/2+sqsection/2, width*.3, 0], [-length/2-sqsection/2, width*.3, 0], 0)
            square(sqsection, center=true);
            beam2([length/2+sqsection/2, -width*.3, 0], [-length/2-sqsection/2, -width*.3, 0], 0)
            square(sqsection, center=true);
        }
        
        PrismaticJoint(p_translate=[length/2, 0, 0], limits=[-20, 0], draw=true){
            for(x=[0]){
                for(y=[width/2,-width/2]){
                    translate([x, y, 0]){
                        ReferenceFrame(factor=150);
                        rotate([90, 0, 0])
                        color([0.2,0.2,0.2])
                        cylinder(h=30, d=80, center=true);
                    }
                }
                beam2([x, width/2, 0], [x, -width/2, 0], 0)
                square(sqsection, center=true);
            }
        }
    }
}

module IndependentAxle(){
    ReferenceFrame(factor=200);
    /*
    Chassis02(bottom_align=true);
    translate([0, 0, 40])
    mirror([1,0,0])
    Cubierta02(); //*/
    translate([0,0,-height]){
        for(x=[length/2, -length/2]){
            PrismaticJoint(p_translate=[x, 0, 0], limits=[-20, 0], draw=true){
                for(y=[width/2,-width/2]){
                    translate([0, y, 0]){
                        ReferenceFrame(factor=150);
                        rotate([90, 0, 0])
                        color([0.2,0.2,0.2])
                        cylinder(h=30, d=80, center=true);
                    }
                }
                beam2([0, width/2, 0], [0, -width/2, 0], 0)
                square(sqsection, center=true);
            }
            beam2([x, width*.3, sqsection], [x, -width*.3, sqsection], 0)
            square(sqsection, center=true);
        }
        translate([0, 0, sqsection]){
            beam2([length/2+sqsection/2, width*.3, 0], [-length/2-sqsection/2, width*.3, 0], 0)
            square(sqsection, center=true);
            beam2([length/2+sqsection/2, -width*.3, 0], [-length/2-sqsection/2, -width*.3, 0], 0)
            square(sqsection, center=true);
        }
    }
}


module IndependentWheel(){
    ReferenceFrame(factor=200);
    /*
    Chassis02(bottom_align=true);
    translate([0, 0, 40])
    mirror([1,0,0])
    Cubierta02(); //*/
    translate([0,0,-height]){
        for(x=[length/2, -length/2]){
            for(y=[width*.3,-width*.3]){
                PrismaticJoint(p_translate=[x, y, 0], limits=[-20, 0], draw=true){
                    beam2([0, -sign(y)*sqsection, 0], [0, sign(y)*width*.2, 0], 0)
                    square(sqsection, center=true);
                    translate([0, sign(y)*width*.2, 0]){
                        ReferenceFrame(factor=150);
                        rotate([90, 0, 0])
                        color([0.2,0.2,0.2])
                        cylinder(h=30, d=80, center=true);
                    }
                }
            }
            beam2([x, width*.3, sqsection], [x, -width*.3, sqsection], 0)
            square(sqsection, center=true);
        }
        translate([0, 0, sqsection]){
            beam2([length/2+sqsection/2, width*.3, 0], [-length/2-sqsection/2, width*.3, 0], 0)
            square(sqsection, center=true);
            beam2([length/2+sqsection/2, -width*.3, 0], [-length/2-sqsection/2, -width*.3, 0], 0)
            square(sqsection, center=true);
        }
    }
}

translate([0, 0, height+wdiam/2])
{
    FullRigid();
    
    translate([0, 500, 0])//*/
    SemiRigid(); //*/
    
    translate([0, 1000, 0])//*/
    IndependentAxle(); //*/
    
    translate([0, 1500, 0])//*/
    IndependentWheel(); //*/
}
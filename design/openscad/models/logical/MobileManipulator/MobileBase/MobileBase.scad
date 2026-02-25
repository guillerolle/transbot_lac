use <Chassis/Chassis01.scad>
use <Chassis/Cubierta.scad>
use <DifferentialModule/DifferentialModule.scad>
use <Wheels/CastorWheel.scad>
use <Wheels/CastorAxle.scad>
use <ControlModule/ControlModule.scad>

module MB_SingleSuspension(lod=0, cubesize=[800, 600, 250], castor_angles=[ [$t*360, $t*360], [$t*360, $t*360] ], control_module_joint=(cos($t*360)-1)/2){
    // castor_angles: [ [castor1_dir, castor1_roll], [castor2_dir, castor2_roll], ... ]
    
    if (lod==1) {
        wheeldiam = 120;
        chassis_width = cubesize[1];
        chassis_height = 150;
        
        translate([-cubesize[0]/2+wheeldiam/2*1.5, 0, wheeldiam/2 + sin($t*360)*20])
        DifferentialModule(wheelbase=chassis_width-100, wheeldiam=wheeldiam);
        
        // INDEPENDENT WHEELS
        translate([0, 0, chassis_height]){
            Chassis01(width=chassis_width, length=cubesize[0]);
            w=[1, -1];
            for (i=[0:1]){
                translate([cubesize[0]/2-50, w[i]*((chassis_width)/2-50), -20])
                CastorWheel(castortheta=castor_angles[i][0], wheeltheta=castor_angles[i][1]);
            }
        }
        
        
        // ABOVE CHASSIS
        translate([0, 0, chassis_height+20]){
            
            // CONTROL MODULE
            translate([-control_module_joint*cubesize[0]/2, 0, 0])
            // mirror([0, 0, 0])
            ControlModule();
            
            // CUBIERTA
            mirror([1, 0, 0])
            Cubierta(width=chassis_width, length=cubesize[0], height=300);
        }

    }
    
    if (lod==0) {
        color(alpha=0.25) 
        translate([0, 0, cubesize[2]/2])
        cube(cubesize, center=true);
    }
}

module MB_DoubleSuspension(lod=0, cubesize=[800, 600, 250], castor_angles=[ [$t*360, $t*360], [$t*360, $t*360] ], castoraxle_joint = sin($t*360)*10, control_module_joint=(cos($t*360)-1)/2){
    // castor_angles: [ [castor1_dir, castor1_roll], [castor2_dir, castor2_roll], ... ]
    
    if (lod==1) {
        wheeldiam = 120;
        chassis_width = cubesize[1];
        chassis_height = 120;
        
        translate([-cubesize[0]/2+wheeldiam/2*1.5, 0, wheeldiam/2 + sin($t*360)*20])
        DifferentialModule(wheelbase=chassis_width-100, wheeldiam=wheeldiam);
        
        // CASTOR AXLE 
        xreduction = 200;
        translate([-xreduction/2, 0, chassis_height])
        Chassis01(width=chassis_width, length=cubesize[0]-xreduction);
        
        translate([(cubesize[0]-xreduction*2)/2+15, 0, chassis_height])
        rotate([0, castoraxle_joint, 0])
        CastorAxleJoint(wheelbase=chassis_width-100, axle_z=00, axle_x=120, castor_angles=castor_angles);
        
        
        // ABOVE CHASSIS
        translate([0, 0, chassis_height+20]){
            
            // CONTROL MODULE
            translate([-100+control_module_joint*cubesize[0]/2, 0, 0])
            mirror([1, 0, 0])
            ControlModule();
            
            // CUBIERTA
            xreduction = 200;
            translate([-xreduction/2, 0, 0])
            Cubierta(width=chassis_width, length=cubesize[0]-xreduction, height=300);
        }

    }
    
    if (lod==0) {
        color(alpha=0.25) 
        translate([0, 0, cubesize[2]/2])
        cube(cubesize, center=true);
    }
}


//MobileBase(lod=1, castor_type=0, castor_angles=[ [-30, 0], [ 15, 0] ]);
MB_DoubleSuspension(lod=1);

translate([0, 1000, 0])
MB_SingleSuspension(lod=1);
//MobileBase(lod=1, castor_type=1, castor_angles=[ [-30, 0], [ 15, 0] ]);

//MobileBase(lod=0);
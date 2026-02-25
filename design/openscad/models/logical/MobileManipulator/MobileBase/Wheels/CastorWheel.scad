module CastorWheel(lod=0, wheeldiam=120, wheelwidth=45, castordistance=40, platesize=100, totalheight=130, wheeltheta=00, castortheta=0){
    
    module CastorHalfArm(){
        hull(){
            translate([0, wheelwidth/2*1.25, wheeldiam/2-5])
            rotate([90, 0, 0])
            translate([0, -10, 0])
            cube([castordistance, 20, 1], center=false);
            
            translate([0, wheelwidth/2*1.25, -10])
            rotate([90, -90, 0])
            translate([0, -10, 0])
            cube([wheeldiam/2, 20, 1], center=false);
        }
    }
    
    module CastorArm(){
        CastorHalfArm();
        mirror([0, 1, 0]){
            CastorHalfArm();
        }
        translate([castordistance-10, 0, wheeldiam/2+5])
        {
            cube([20, wheelwidth*1.25, 1], center=true);
        }
    }
    //CastorArm();
    
    if (lod==0){
        cube([platesize, platesize, 1], center=true);
        translate([0,0,-5])
        color([1,0,0])
        cylinder(5, d=10);
        rotate([0, 0, castortheta]) {

            
            translate([-castordistance, 0, -totalheight+wheeldiam/2]){
                rotate([90, 0, 0]) {
                    color([1,0,0])
                    cylinder(h=wheelwidth*1.5, d=10, center=true);    
                    
                    rotate([0, 0, wheeltheta])
                    color([.3,.3,.3])
                    cylinder(h=wheelwidth, d=wheeldiam, center=true);
                };
                CastorArm();
            }
        }
    }
}

CastorWheel();
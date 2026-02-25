module DifferentialModule(lod=0, wheelbase=600, wheeldiam=120, wheelwidth=45){
    
    if (lod==0){
        rotate([90, 0, 0])
        cylinder(h=wheelbase-wheelwidth, d=15, center=true);
        
        // WHEELS 
        for (w=[-1, 1]) {
            translate( w*[0, wheelbase/2, 0])
            rotate([90, 0, 0]){
                color([1,0,0])
                cylinder(d=20, h=wheelwidth*1.25, center=true);
                color([.3,.3,.3])
                cylinder(d=wheeldiam, h=wheelwidth, center=true);
            }
        }
    }
}

DifferentialModule();
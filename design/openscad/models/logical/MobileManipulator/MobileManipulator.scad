use <MobileBase/MobileBase.scad>
use <Scene/Canasto.scad>
use <ManipulationStructures/Forklift.scad>

module FkDSusp(lod=0, cubesize=[800, 600, 1800]){
    if (lod==1){
        //color([1, 0, 0])
        MB_DoubleSuspension(lod=1, cubesize=cubesize);
        
        translate([150-sin($t*180)^2*500, 0, 100])
        mirror([1, 0, 0])
        Autoelevador(height=cubesize[2]-100, width=cubesize[1]+50, length=500, joint_z=0.23);
    
        translate([-150, 0, 440])
        Canasto();    
    }
    
    if (lod==0){
        color(alpha=0.25)
        translate([0, 0, cubesize[2]/2])
        cube(cubesize, center=true);
    } 
} 

module FkSSusp(lod=0, cubesize=[800, 600, 1800]){
    if (lod==1){
        //color([1, 0, 0])
        MB_SingleSuspension(lod=1, cubesize=cubesize);
        
        translate([cubesize[0]/2-50-sin($t*180)^2*(cubesize[0]-100), 0, 120])
        mirror([1, 0, 0])
        Autoelevador(height=cubesize[2]-120, width=cubesize[1]+50, length=650, joint_z=0.25);
    
        translate([-150, 0, 470])
        Canasto();    
    }
    
    if (lod==0){
        color(alpha=0.25)
        translate([0, 0, cubesize[2]/2])
        cube(cubesize, center=true);
    } 
} 

FkDSusp(lod=1);

translate([0, 1000, 0])
//color([.8,.8,.8])
//mirror([1, 0, 0])
FkSSusp(lod=1);
//FkDSusp(lod=0);

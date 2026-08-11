include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <RobotUtils/profiles.scad>
use <../Chassis/Chassis02.scad>
use <../Chassis/Cubierta.scad>
use <DifferentialModule/DifferentialModule.scad>

module DD6W(display="*", prefix="", length=500, width=500, height=250, clearance=50){
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];
    echo(_xdisp);
    
    translate([0, 0, clearance])
    Chassis02(length=length, width=width, bottom_align=true, transversal_beams=[-0.8, 0.8]);
    
    RevoluteJoint(draw=true, axis=[0, 1, 0], p_translate=[100, 0, 50], limits=[-15, 15]){
        ReferenceFrame(factor=100);
        __doublebar();
        translate([-100, 0, 0])
        DifferentialModule(track=width*0.9);
    }
    
    module __doublebar(){
        extrude_along(axis=[0,1,0], length=width*.8)
        CircularProfileHollow(d=15, thickness=1);
        extrude_along(axis=[-1,0,0], length=width*.2, center=false)
        CircularProfileHollow(d=15, thickness=1);
    }
}

DD6W();
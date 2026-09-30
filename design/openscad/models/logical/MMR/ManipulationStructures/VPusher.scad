include <BOSL2/std.scad>
include <BOSL2/strings.scad>
use <RobotUtils/core.scad>
use <RobotUtils/profiles.scad>

module vtable(table_length=400, table_width=300, thickness=3, max_height=200, v_angle=60, v_length=150, gap=50){

    color([0.9, 0.7, 0.2])
    cube(size=[table_length, table_width, thickness], center=true);
    
    color([0.7, 0.3, 0.3]){
        translate([-gap/2, 0, 0])
        linear_extrude(max_height)
        polygon([
            [-v_length, tan(v_angle/2)*v_length],
            [0, 0],
            [-v_length, -tan(v_angle/2)*v_length],
        ]);    
        translate([v_length+gap/2, 0, 0])
        linear_extrude(max_height/2)
        polygon([
            [-v_length, tan(v_angle/2)*v_length],
            [0, 0],
            [-v_length, -tan(v_angle/2)*v_length],
        ]); 
    }
}

vtable();
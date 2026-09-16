use <../ShelfLifter.scad>
use <../ShelfTrailer.scad>
use <../MobileBase/DifferentialDrives/SixWheels_L.scad>
use <MovingShelf.scad>
use <ShelfTrailerType.scad>
use <Canasto.scad>
use <RobotUtils/core.scad>

// TABLE PUSHER //
translate([0, -1000, 0]){
    DD6W_L(bbox=[800, 400, 300], double_bar_offset=300,force_internal_castor=false);
    rotate([0,0,180])
    translate([0, 0, 0]){
        MovingShelf(width=600, length=500, height=400);
        translate([0, 0, 400])
        Canasto(use_lower_base=false);
    }
}

// TABLE TRAILER //
translate([0, 0, 0]){
    Base_ShelfTrailer();
    translate([-700, 0, 0]){
        Shelf_TrailerType(width=500, length=500, height=500, coupler_position_z=325);
        translate([0, 0, 500])
        Canasto(use_lower_base=false);
    }
}

// TABLE LIFTER //
translate([0, 1000, 0]){
    ShelfLifter();
    MovingShelf(width=800, length=500, height=350, use_back_sheet=false);
    translate([0, 0, 350])
    Canasto(use_lower_base=false);
}
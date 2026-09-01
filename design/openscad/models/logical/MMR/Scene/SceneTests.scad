use <../ShelfLifter.scad>
use <../ShelfTrailer.scad>
use <MovingShelf.scad>
use <Canasto.scad>
use <RobotUtils/core.scad>


// SHELF TRAILER //
translate([0, 0, 0]){
    ReferenceFrame(factor=500);
    Base_ShelfTrailer();
    translate([-700, 0, 0]){
        Shelf_TrailerType(width=500, length=500, height=500, coupler_position_z=325);
        translate([0, 0, 500])
        Canasto(use_lower_base=false);
    }
}

// SHELF LIFTER //
translate([0, 1000, 0]){
    ReferenceFrame(factor=500);
    ShelfLifter();
    MovingShelf(width=800, length=500, height=350, use_back_sheet=false);
    translate([0, 0, 350])
    Canasto(use_lower_base=false);
}
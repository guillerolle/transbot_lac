use <RobotUtils/core.scad>
use <RobotUtils/beam.scad>
use <RobotUtils/profiles.scad>
use <../MobileBase/Wheels.scad>
use <../ManipulationStructures/VPusher.scad>

module MovingShelf(display="*", prefix="", length=500, width=500, height=500, tube_profile = [20, 20], sheet_thickness=3, castor_height=130, use_back_sheet=true, pusher_module="", vtable_height=300)
{
    _xdisp = extract_assembly_parts(display);
    _d = _xdisp[0];
    _s = _xdisp[1];

    module _castor(){
        CastorWheel(display=_s, prefix=get_full_prefix(prefix, "castor"), ch=castor_height, cf=50);
    }

    module _vtable(){
        _width = 300;
        _length = 400;
        _height = 200;
        _vangle = 60;
        _vlength = 160;
        _vheight = 200;
        _gap = 100;
        //ReferenceFrame(factor=200);
        difference() {
            translate(v = [0,0,_height/2]) 
            cube([_length-5, _width, _height], center=true);

            vtable(table_length=_length, table_width=_width, v_angle=_vangle, gap=100, v_length=_vlength, max_height=_vheight);
            linear_extrude(_vheight/2-5) 
            polygon(points = [
                [_gap/2+10, tan(_vangle/2)*(_vlength-5)],
                [_gap/2+10, -tan(_vangle/2)*(_vlength-5)],
                [-_length/2,-tan(_vangle/2)*(_vlength-5)],
                [-_length/2,tan(_vangle/2)*(_vlength-5)],
            ]);            
            
            linear_extrude(_vheight+5) 
            polygon(points = [
                [-_vlength-_gap/2+5, tan(_vangle/2)*(_vlength-5)],
                [-_vlength-_gap/2+5, -tan(_vangle/2)*(_vlength-5)],
                [-_length/2,-tan(_vangle/2)*(_vlength-5)],
                [-_length/2,tan(_vangle/2)*(_vlength-5)],
            ]);
        }
    }
    
    if (_d=="*")
    {
        _structure();
        FixedJoint(name="castor0", prefix=prefix, p_translate=[length/2,width/2,castor_height])
        _castor();
        FixedJoint(name="castor1", prefix=prefix, p_translate=[-length/2,width/2,castor_height])
        _castor();
        FixedJoint(name="castor2", prefix=prefix, p_translate=[length/2,-width/2,castor_height])
        _castor();
        FixedJoint(name="castor3", prefix=prefix, p_translate=[-length/2,-width/2,castor_height])
        _castor();

        if (pusher_module=="vtable"){
            FixedJoint(name="vtable", prefix=prefix, p_translate=[0, 0, vtable_height])
            _vtable();
        }
        
    } else if (_d=="_") {
        // MAIN LINK 
        _structure();
    } else if (_d=="castor") {
        _castor();
    } else if ((pusher_module=="vtable") && (_d=="vtable")) {
        _vtable();
    }
    
    module _structure()
    {
        translate([0, 0, castor_height]){
            for (y = [1, -1])
            for (x = [1, -1])
            {
                beam3([x*(length/2), y*(width/2), 0], [x*(length/2), y*(width/2), height-castor_height], 0)
                RectangularProfileHollow(tube_profile, 1.2);
            }
            translate([0, 0, height-castor_height])
            cube([length+tube_profile[0], width+tube_profile[1], sheet_thickness], center=true);
            if (use_back_sheet){
                translate([length/2+tube_profile[0]/2, 0, height-100-castor_height])
                rotate([0,90,0])
                cube([200, width+tube_profile[1], sheet_thickness], center=true);
            }
        }
    }
}

display="*";
length=500;
width=700;
height=500;
use_back_sheet=false; 
pusher_module="vtable";
MovingShelf(display=display, width=width, length=length, height=height, use_back_sheet=use_back_sheet, pusher_module=pusher_module);
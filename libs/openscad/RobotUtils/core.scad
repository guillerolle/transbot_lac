include <BOSL2/std.scad>
include <BOSL2/strings.scad>
include <beam.scad>

function extract_assembly_parts(display) = 
    (display=="*") ? ["*", "*"]: let(
        _dlist = (display=="*") ? ["*"] : str_split(display, "/"),
        _slist = (len(_dlist)>1) ? [for (i = [1: len(_dlist) -1]) _dlist[i]] : [],
        
        _d = _dlist[0],
        _s = (len(_slist)>0) ? str_join(_slist,"/") : "*"
    ) [_d, _s];
        
function get_full_prefix(base, prefix) = str_join([base, prefix], (len(base)==0)?"":"/");
        
module align_vectors(v1, v2){
    n1 = norm(v1);
    n2 = norm(v2);
    assert(n1>0);
    assert(n2>0);
    _cross=cross(v1,v2);
    _dot=v1*v2;
    n12 = n1*n2;
    ang = atan2(norm(_cross)/n12, _dot/n12);
    rotate(v=_cross, a=ang)
    children();
}

module FixedJoint(p_translate=[0,0,0], p_rotate=[0,0,0], name="joint_fixed", prefix=""){
    echo(["joint", "fixed", (len(prefix) == 0) ? name:str_join([prefix, "/", name]), str_join(["xyz: ", str(p_translate)]), str_join(["rpy: ", str(p_rotate)])])
    translate(p_translate)
    rotate(p_rotate)
    children();
}

module ContinuousJoint(
    p_translate=[0,0,0], p_rotate=[0,0,0], axis=[0,0,1], angle=$t*360, 
    name="joint_continuous", prefix="", 
    command_interfaces=[], mimic=[], spring=[], damping=[], friction=[], draw=false){
    echo(["joint", "continuous", 
        (len(prefix) == 0) ? name:str_join([prefix, "/", name]), 
        str_join(["xyz: ", str(p_translate)]), 
        str_join(["rpy: ", str(p_rotate)]), 
        str_join(["axis: ", str(axis)]), 
        str_replace_char(str_join(["command_interfaces: ", command_interfaces]), "\"", "\\\""), 
        str_replace_char(str_join(["mimic: ", mimic]), "\"", "\\\""),
        str_join(["spring: ", str(spring)]), 
        str_join(["damping: ", str(damping)]), 
        str_join(["friction: ", str(damping)])
    ])
    translate(p_translate)
    rotate(p_rotate){
        if (draw){
            color([0.7, 0.3, 0])
            extrude_along(axis, 50)
            circle(d=30);
        }
        rotate(angle, axis)
        children();
    }
}

module PrismaticJoint(
    p_translate=[0,0,0], p_rotate=[0,0,0], axis=[0,0,1], 
    unitpos=(-cos($t*360)+1)/2, name="joint_prismatic", prefix="", 
    limits=[-100, 100], command_interfaces=[], mimic=[],
    spring=[], damping=[], friction=[], draw=false, pos=false, animate=true
    ){
    _extension = abs(limits[1]-limits[0]);
    _pos0 = pos==false?(limits[1]+limits[0])/2:pos;
    _t0 = acos(1-2*(_pos0-limits[0])/_extension)/360;
    _pos = animate ? (-cos( ($t - _t0)*360)+1)/2*_extension + limits[0] : _pos0;
    assert((_pos>=limits[0]) && (_pos<=limits[1]), "position must be between limits");
    
    echo(["joint", "prismatic", 
        (len(prefix) == 0) ? name:str_join([prefix, "/", name]),
        str_join(["xyz: ", str(p_translate)]),
        str_join(["rpy: ", str(p_rotate)]),
        str_join(["axis: ", str(axis)]), 
        str_join(["limits: ", str(limits)]), 
        str_replace_char(str_join(["command_interfaces: ", command_interfaces]), "\"", "\\\""), 
        str_replace_char(str_join(["mimic: ", mimic]), "\"", "\\\""), 
        str_join(["spring: ", str(spring)]), 
        str_join(["damping: ", str(damping)]), 
        str_join(["friction: ", str(damping)])
    ]);
    _uaxis = axis/norm(axis);
    
    translate(p_translate)
    rotate(p_rotate){
        if (draw){
            color([0.7, 0.3, 0])
            translate(axis*min(limits[0], limits[1]))
            extrude_along(axis, _extension, center=false)
            square(size=30, center=true);
        }
        translate(_uaxis*_pos)
        children();
    }
}


module RevoluteJoint(
    p_translate=[0,0,0], p_rotate=[0,0,0], axis=[0,0,1], 
    angle=false, name="joint_revolute", prefix="", 
    limits=[-100, 100], command_interfaces=[], mimic=[],
    spring=[], damping=[], friction=[], draw=false, animate=true
    ){
    _extension = abs(limits[1]-limits[0]);
    _angle0 = angle==false?(limits[1]+limits[0])/2:angle;
    _t0 = acos(1-2*(_angle0-limits[0])/_extension)/360;
    _angle = animate ? (-cos( ($t - _t0)*360)+1)/2*_extension + limits[0] : _angle0;
    assert((_angle>=limits[0]) && (_angle<=limits[1]), "angle must be between limits");
    //_abspos = _extension*unitpos+limits[0];
    
    echo(["joint", "revolute", 
        (len(prefix) == 0) ? name:str_join([prefix, "/", name]),
        str_join(["xyz: ", str(p_translate)]),
        str_join(["rpy: ", str(p_rotate)]),
        str_join(["axis: ", str(axis)]), 
        str_join(["limits: ", str(limits)]), 
        str_replace_char(str_join(["command_interfaces: ", command_interfaces]), "\"", "\\\""), 
        str_replace_char(str_join(["mimic: ", mimic]), "\"", "\\\""), 
        str_join(["spring: ", str(spring)]), 
        str_join(["damping: ", str(damping)]), 
        str_join(["friction: ", str(damping)])
    ]);
    _uaxis = axis/norm(axis);
    
    translate(p_translate)
    rotate(p_rotate){
        if (draw){
            color([0.7, 0.3, 0])
            extrude_along(axis, 50)
            circle(d=30);
        }
        rotate(_angle, axis)
        children();
    }
}

module Arrow3D(to, from=[0,0,0], cyl_d, cone_d, cone_h){
    delta = to-from;
    length=norm(delta);
    cyl_d = is_undef(cyl_d) ? length*0.05:cyl_d;
    cone_d = is_undef(cone_d) ? length*0.15:cone_d;
    cone_h = is_undef(cone_h) ? length*0.15:cone_h;
    
    translate(from)
    align_vectors([0,0,1],delta){
        cylinder(h=length-cone_h, d=cyl_d);
        translate([0,0,length-cone_h])
        cylinder(h=cone_h, d1=cone_d, d2=0);
    }
}

module ReferenceFrame($fn=4, factor=1){
    scale(factor){
        color([1,0,0])
        Arrow3D(to=[1,0,0]);
        color([0,1,0])
        Arrow3D(to=[0,1,0]);
        color([0,0,1])
        Arrow3D(to=[0,0,1]);
    }
}
ReferenceFrame($scale=1);

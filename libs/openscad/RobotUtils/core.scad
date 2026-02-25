include <BOSL2/std.scad>
include <BOSL2/strings.scad>

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
    echo(["joint", "fixed", (len(prefix) == 0) ? name:str_join([prefix, "/", name]), str(p_translate), str(p_rotate)])
    translate(p_translate)
    rotate(p_rotate)
    children();
}

module ContinuousJoint(p_translate=[0,0,0], p_rotate=[0,0,0], axis=[0,0,1], angle=$t*360, name="joint_continuous", prefix=""){
    echo(["joint", "continuous", (len(prefix) == 0) ? name:str_join([prefix, "/", name]), str(p_translate), str(p_rotate), str(axis)])
    translate(p_translate)
    rotate(p_rotate)
    rotate(angle, axis)
    children();
}

module PrismaticJoint(p_translate=[0,0,0], p_rotate=[0,0,0], axis=[0,0,1], unitpos=(-cos($t*360)+1)/2, name="joint_prismatic", prefix="", limits=[-100, 100]){
    _extension = limits[1]-limits[0];
    assert((unitpos>=0) && (unitpos<=1), "position must be in range [0,1]");
    _abspos = _extension*unitpos+limits[0];
    
    echo(["joint", "prismatic", (len(prefix) == 0) ? name:str_join([prefix, "/", name]), str(p_translate), str(p_rotate), str(axis), str(limits)]);
    _uaxis = axis/norm(axis);
    
    translate(p_translate)
    rotate(p_rotate)
    translate(_uaxis*_abspos)
    children();
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

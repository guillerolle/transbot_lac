use <core.scad>
use <profiles.scad>

function d3d(p1,p2)=norm(p2-p1);
function d2d(p1,p2)=let(dp=p2-p1)norm([dp[0], dp[1]]);

module beam2(N1,N2,beta_angle){
    /*
    extrude profile from point N1 to point N2, with profile angle beta_angle
    usage:
        beam2(N1,N2,beta_angle)<2d-profile>;
    args:
        N1: [x1,y1,z1] (init point)
        N2: [x2,y2,z2] (final point)
        beta_angle: float (profile angle)
    */
lenght=d3d(N1,N2);
    rot_y=atan((N1[2]-N2[2])/d2d([N1[0],N1[1]],[N2[0],N2[1]]));
rot_z=atan2(N2[1]-N1[1],N2[0]-N1[0]);
translate(N1)rotate([beta_angle,rot_y,rot_z])rotate([90,0,90])linear_extrude(lenght)children();
}

module beam3(N1, N2, profile_angle){
    /*
    extrude profile from point N1 to point N2, with profile angle beta_angle
    usage:
        beam3(N1,N2,beta_angle)<2d-profile>;
    args:
        N1: [x1,y1,z1] (init point)
        N2: [x2,y2,z2] (final point)
        profile_angle: float (profile angle)
    */
    vector = N2-N1;
    length = norm(vector);
    assert(length>0);
    align_z(N1,N2)
    linear_extrude(length)rotate(profile_angle)
    children();
}

module extrude_along(axis, length, profile_angle=0, center=true){
    align_vectors([0,0,1], axis)
    linear_extrude(length, center=center)rotate(profile_angle)
    children();
}

module align_z(N1=[0,0,0],N2){
    _align = get_z_alignment(N1=N1,N2=N2);
    translate(N1)
    rotate(v=_align[0], a=_align[1])
    children();
}

function get_z_alignment(N1=[0,0,0],N2)=let(
    v = N2-N1,
    u = v/norm(v),
    _cross=cross([0,0,1], u),
    dot=[0,0,1]*u,
    ang = atan2(norm(_cross), dot)
    )[_cross, ang];


n1=[100,0,0];
n2=[0,0,200];
beam2(n1,n2,90)MakeProfileHollow(5)vigueta();
translate([0,200,0])beam2(n1,n2,0)vigueta();

translate([0,-200,0])beam2(n1,n2,90)RectangularProfileHollow([40,20],2);

translate([-200,0,0])beam2(n1,n2,90)CircularProfileHollow(d=20,thickness=2);

translate([100, -200, 0])
beam3(n1,n2,90)
RectangularProfileHollow([40,20],2);

beam3([0,0,0], [0,0,1e3], 0)
translate([20,10,0])
RectangularProfileHollow([40,20],2);

beam3([0,0,0], [1e3,0,0], 0)
translate([20,10,0])
RectangularProfileHollow([40,20],2);

beam3([0,0,0], [0,1e3,0], 0)
translate([20,10,0])
RectangularProfileHollow([40,20],2);




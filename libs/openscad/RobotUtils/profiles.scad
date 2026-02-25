module MakeProfileHollow(thickness){
    assert(thickness>0);
    difference(){
        children();
        offset(delta=-thickness)children();
    }
}

module vigueta(){polygon([[55,0],[55,36],[20,46],[25,80],[-25,80],[-20,46],[-55,36],[-55,0]]);}

module RectangularProfileHollow(size, thickness){
    MakeProfileHollow(thickness)square(size, center=true);
}

module CircularProfileHollow(d, thickness){
    MakeProfileHollow(thickness)circle(d=d);
}

RectangularProfileHollow([40,20], 2);

translate([0,50,0])
CircularProfileHollow(20, 1.2);

translate([0,100,0])
vigueta();

translate([0,-100,0])
MakeProfileHollow(5)vigueta();
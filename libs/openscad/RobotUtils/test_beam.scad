use <beam.scad>
use <profiles.scad>

bound = 5*1e3;
for (x=[-bound:50:bound]){
    for (y=[-bound:50:bound]){
        beam3([x,y,0],[x,y,100],0)
        RectangularProfileHollow¨([40,20],2);
    }
}

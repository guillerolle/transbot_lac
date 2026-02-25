module Soporte(lado=50){
    cube([lado, lado, lado], center=true);
    cube([lado*2, lado, lado/2], center=true);
}


Soporte();

translate([0,100,0])
Soporte(lado=30);
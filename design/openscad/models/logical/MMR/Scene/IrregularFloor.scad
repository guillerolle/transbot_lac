module IrregularFloor(length=1000, width=800, thickness=20, cell_size=50, noise_amplitude=10, mode="bumps", seed=42)
{
    cols = max(1, floor(length/cell_size));
    rows = max(1, floor(width/cell_size));
    noise = rands(0, 1, cols*rows, seed);
    //echo(cols, rows, noise);
    //echo(noise[77]);
    color([0.35, 0.35, 0.35])
    {
        // NOISE LAYER //
        if (mode=="bumps")
        {
            
            translate([0, 0, (thickness)/2]){
                difference()
                {
                    // BASE SLAB (bottom surface at z = 0) //
                    {
                        cube([length, width, thickness], center=true);
                    }
                    for (i=[0:cols-1]) 
                    for (j=[0:rows-1])
                    {
                        x = -length/2 + (i+0.5)*cell_size;
                        y = -width/2 + (j+0.5)*cell_size;
                        //echo(i*rows+j, i, j, noise[i*cols+j]);
                        h = noise[i*rows+j] * noise_amplitude;
                        translate([x, y, thickness/2-h/2+0.05])
                        cube([cell_size*1.1, cell_size*1.1, abs(h)+0.1], center=true);
                    }
                }
            }
            // RAMP
            translate([length/2, 0, 0])
            rotate([0, -90, -90])
            linear_extrude(width, center = true)
            polygon([ [0,0], [thickness,0], [thickness,cell_size], [0,300]]);
            
            // RAMP
            translate([-length/2, 0, 0])
            rotate([0, -90, 90])
            linear_extrude(width, center = true)
            polygon([ [0,0], [thickness-noise_amplitude/2,0], [thickness-noise_amplitude/2,cell_size], [0,300]]);
        }
        /*
        else if (mode=="craters")
        {
            difference()
            {
                translate([0, 0, z_top - noise_amplitude])
                cube([length, width, noise_amplitude], center=false);

                for (i=[0:cols-1])
                for (j=[0:rows-1])
                {
                    x = -length/2 + (i+0.5)*cell_size;
                    y = -width/2 + (j+0.5)*cell_size;
                    h = noise[i*cols+j];
                    translate([x, y, z_top - abs(h)*noise_amplitude])
                    sphere(d=cell_size*0.9*abs(h)*2 + cell_size*0.3, $fn=16);
                }
            }
        }
            
            
        }//*/
    }
}

IrregularFloor();

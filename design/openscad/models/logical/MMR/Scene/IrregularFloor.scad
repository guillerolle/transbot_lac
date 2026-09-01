module IrregularFloor(length=1000, width=800, thickness=10, cell_size=50, noise_amplitude=10, mode="bumps", seed=42, z_top=0)
{
    cols = max(1, floor(length/cell_size));
    rows = max(1, floor(width/cell_size));
    noise = rands(-1, 1, cols*rows, seed);
    //echo(cols, rows, noise);
    //echo(noise[77]);
    color([0.35, 0.35, 0.35])
    {
        // BASE SLAB (top surface at z = z_top) //
        translate([0, 0, z_top-thickness])
        cube([length, width, thickness], center=true);

        // NOISE LAYER //
        if (mode=="bumps")
        {
            difference()
            {
                translate([0, 0, z_top - noise_amplitude/2])
                cube([length, width, noise_amplitude], center=true);

                for (i=[0:cols-1]) 
                for (j=[0:rows-1])
                {
                    x = -length/2 + (i+0.5)*cell_size;
                    y = -width/2 + (j+0.5)*cell_size;
                    //echo(i*rows+j, i, j, noise[i*cols+j]);
                    h = noise[i*rows+j] * noise_amplitude;
                    translate([x, y, z_top - h/2])
                    cube([cell_size*1.1, cell_size*1.1, abs(h)+0.1], center=true);
                }
            }
        }
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
    }
    
    {
        translate([length/2, 0, -thickness-noise_amplitude])
        rotate([0, -90, -90])
        linear_extrude(width, center = true)
        polygon([ [0,0], [thickness+noise_amplitude,0], [0,300]]);
    }
}

IrregularFloor();

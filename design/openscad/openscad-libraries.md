# OpenSCAD Libraries Documentation

Generated: 2026-09-01T12:01:41.312Z

Library paths scanned:
- `/home/guillermo/.local/share/OpenSCAD/libraries`

Found **89** library file(s).

## BOSL2/affine.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/affine.scad`

### Functions

#### `affine2d_identity()`

//   ]

#### `affine2d_translate(v=[0, 0])`

//   ]

#### `affine2d_scale(v=[1, 1])`

//   ]

#### `affine2d_zrot(ang=0)`

//   ]

#### `affine2d_mirror(v)`

//   ]

#### `affine2d_skew(xa=0, ya=0)`

//   ]

#### `affine3d_identity()`

//   ]

#### `affine3d_translate(v=[0, 0, 0])`

//   ]

#### `affine3d_scale(v=[1, 1, 1])`

//   ]

#### `affine3d_xrot(ang=0)`

//   ]

#### `affine3d_yrot(ang=0)`

//   ]

#### `affine3d_zrot(ang=0)`

//   ]

#### `affine3d_rot_by_axis(u=UP, ang=0)`

//   ]

#### `affine3d_rot_from_to(from, to)`

//   ]

#### `affine3d_mirror(v)`

//   ]

#### `affine3d_skew(sxy=0, sxz=0, syx=0, syz=0, szx=0, szy=0)`

//   ]

#### `affine3d_skew_xy(xa=0, ya=0)`

//   ]

#### `affine3d_skew_xz(xa=0, za=0)`

//   ]

#### `affine3d_skew_yz(ya=0, za=0)`

//   ]

## BOSL2/attachments.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/attachments.scad`

### Modules

#### `position(at, from)`

}

#### `orient(anchor, spin)`

}

#### `align(anchor, align=CENTER, inside=false, inset=0, shiftout=0, overlap)`

#### `attach(parent, child, overlap, align, spin=0, norot, inset=0, shiftout=0, inside=false, from, to)`

#### `attach_part(name, ind=0)`

#### `tag(tag)`

}

#### `tag_this(tag)`

#### `force_tag(tag)`

}

#### `default_tag(tag, do_tag=true)`

}

#### `tag_scope(scope)`

}

#### `diff(remove="remove", keep="keep")`

}

#### `tag_diff(tag="", remove="remove", keep="keep")`

tag("keep")cyl(r=5,h=9);

#### `intersect(intersect="intersect", keep="keep")`

}

#### `tag_intersect(tag="", intersect="intersect", keep="keep")`

}

#### `conv_hull(keep="keep")`

tag("remove")cyl(r=2,h=12);

#### `tag_conv_hull(tag="", keep="keep")`

}

#### `hide(tags)`

}

#### `hide_this()`

#### `show_only(tags)`

}

#### `show_all()`

Sets `$tags_hidden=[]`

#### `show_int(tags)`

Sets `$tags_shown`

#### `_show_highlight()`

#### `_show_ghost()`

#### `change_anchors(named=[], alias=[], remove=[])`

#### `show_anchors(s=10, std=true, custom=true)`

cube(50, center=true) show_anchors();

#### `anchor_arrow(s=10, color=[0.333, 0.333, 1], flag=true, $tag="anchor-arrow", $fn=12, anchor=BOT, spin=0, orient=UP)`

anchor_arrow(s=20);

#### `anchor_arrow2d(s=15, color=[0.333, 0.333, 1], $tag="anchor-arrow")`

anchor_arrow2d(s=20);

#### `expose_anchors(opacity=0.2)`

expose_anchors() cube(50, center=true) show_anchors();

#### `show_transform_list(tlist, s=5)`

show_transform_list(tlist) frame_ref();

#### `generic_airplane(s=5)`

generic_airplane(s=20);

#### `frame_ref(s=15, opacity=1)`

frame_ref(30, opacity=0.5);

#### `_edges_text3d(txt, size=3)`

#### `_show_edges(edges="ALL", size=20, text, txtsize=3, toplabel)`

/   _show_edges(size=30, edges=["X","Y"]);

#### `_show_corners(corners="ALL", size=20, text, txtsize=3, toplabel)`

/   _show_corners(corners=FWD+RIGHT, size=30);

#### `_show_cube_faces(faces, size=20, toplabel, botlabel)`

#### `restore(desc)`

#### `desc_copies(transforms)`

### Functions

#### `_quant_anch(x)`

Quantize anchor entry to {-1,0,1}

#### `_make_anchor_legal(anchor, geom)`

Make arbitrary anchor legal for a given geometry

#### `_get_part(name, ind)`

#### `_is_geometry(entry)`

#### `named_anchor(name, pos, orient, spin, rot, flip, info)`

flip = If true, flip the anchor the opposite direction.  Default: false

#### `define_part(name, geom, inside=false, T=IDENT)`

#### `_attach_geom_2d(geom)`

/   Returns true if the given attachment geometry description is for a 2D shape.

#### `_attach_geom_size(geom)`

/   Returns the `[X,Y,Z]` bounding size for the given attachment geometry description.

#### `_attach_geom_edge_path(geom, edge)`

/   If the edge is invalid for the geometry, returns `undef`.

#### `_attach_transform(anchor, spin, orient, geom, p)`

#### `_get_cp(geom)`

#### `_get_cp(geom)`

#### `_three_edge_corner_dir(facevecs, edges)`

#### `_find_anchor(anchor, geom)`

#### `_is_shown()`

/   Returns true if objects should currently be shown based on the tag settings.

#### `_standard_anchors(two_d=false)`

/   two_d = If true, returns only the anchors where the Z component is 0.  Default: false

#### `_edges_vec_txt(x)`

#### `_edges_text(edges)`

#### `_is_edge_array(x)`

/ See Also: edges(), EDGES_NONE, EDGES_ALL

#### `_edge_set(v)`

#### `_normalize_edges(v)`

/ See Also:  edges(), EDGES_NONE, EDGES_ALL

#### `_edges(v, except=[])`

/

#### `_is_corner_array(x)`

/ See Also: CORNERS_NONE, CORNERS_ALL, _corners()

#### `_normalize_corners(v)`

/ See Also: CORNERS_NONE, CORNERS_ALL, _corners()

#### `_corner_set(v)`

#### `_corners(v, except=[])`

/   set descriptor, you do not have to pass it in a list.

#### `_corner_edges(edges, v)`

/ See Also: CORNERS_NONE, CORNERS_ALL, _corners()

#### `_corner_edge_count(edges, v)`

/ See Also: CORNERS_NONE, CORNERS_ALL, _corners()

#### `_corners_text(corners)`

#### `_force_rot(T)`

#### `_local_struct_val(struct, key)`

#### `_force_anchor_2d(anchor)`

#### `_compute_spin(anchor_dir, spin_dir, backup_dir)`

backup_dir will be used instead of spin_dir if anchor_dir is parallel to spin_dir

#### `_canonical_edge(edge)`

Compute canonical edge direction so that edge is either Z+, Y+ or X+ in that order

#### `parent()`

continues to run and produces a valid result.

#### `parent_part(name, ind=0)`

#### `desc_point(desc, p, anchor)`

stroke([[0,0,0], desc_point(desc,anchor=TOP+FWD+RIGHT)],width=.5,color="red");

#### `desc_dir(desc, dir, anchor)`

position(TOP) cyl(d=2,h=15,orient=desc_dir(pris,anchor=FWD),anchor=LEFT);

#### `desc_attach(desc, anchor=UP, p, reverse=false)`

#### `desc_dist(desc1, anchor1=CENTER, desc2, anchor2=CENTER)`

#### `transform_desc(T, desc)`

#### `is_description(desc)`

desc = argument to check

## BOSL2/ball_bearings.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/ball_bearings.scad`

### Modules

#### `ball_bearing(trade_size, id, od, width, shield=true, flange=false, fd, fw, rounding, anchor=CTR, spin=0, orient=UP)`

ball_bearing(id=12,od=24,width=6,shield=true, flange=true, fd=26.5, fw=1.5, rounding=0.6, $fn=72);

### Functions

#### `ball_bearing_info(trade_size)`

size = Inner diameter of lmXuu bearing, in mm.

## BOSL2/beziers.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/beziers.scad`

### Modules

#### `debug_bezier(bezpath, width=1, N=3)`

#### `debug_bezier_patches(patches=[], size, splinesteps=16, showcps=true, showdots=false, showpatch=true, convexity=10, style="default")`

debug_bezier_patches(patches=[patch1, patch2], splinesteps=8, showcps=true);

### Functions

#### `bezier_points(curve, u)`

Note that everything I tried to simplify or tidy this code made is slower, sometimes a lot slower.

#### `_signed_pascals_triangle(N, tri=[[-1]])`

Not public.

#### `_compute_bezier_matrix(N)`

Not public.

#### `_bezier_matrix(N)`

Not public.

#### `bezier_curve(bezier, splinesteps=16, endpoint=true)`

debug_bezier(bez, N=len(bez)-1);

#### `bezier_derivative(bezier, u, order=1)`

order = The order of the derivative to return.  Default: 1 (for the first derivative)

#### `bezier_tangent(bezier, u)`

u = Parameter values for evaluating the curve, given as a single value, a list or a range.

#### `bezier_curvature(bezier, u)`

u = Parameter values for evaluating the curve, given as a single value, a list or a range.

#### `bezier_closest_point(bezier, pt, max_err=0.01, u=0, end_u=1)`

color("blue") translate(bezier_points(bez,u)) sphere(r=1);

#### `bezier_length(bezier, start_u=0, end_u=1, max_deflect=0.01)`

echo(bezier_length(bez));

#### `bezier_line_intersection(bezier, line)`

line = a list of two distinct 2d points defining a line

#### `bezpath_points(bezpath, curveind, u, N=3)`

N = The degree of the Bezier path curves.  Default: 3

#### `bezpath_curve(bezpath, splinesteps=16, N=3, endpoint=true, order=[])`

#### `bezpath_closest_point(bezpath, pt, N=3, max_err=0.01, seg=0, min_seg=undef, min_u=undef, min_dist=undef)`

color("blue") translate(xy) sphere(r=1);

#### `bezpath_length(bezpath, N=3, max_deflect=0.001)`

max_deflect = The largest amount of deflection from the true curve to allow for approximation.

#### `path_to_bezpath(path, closed, tangents, uniform=false, size, relsize)`

relsize = relative size specification for the curve, a number or vector.  Default: 0.1.

#### `path_to_bezcornerpath(path, closed, size, relsize)`

/   relsize = relative curve deviation (between 0 and 1) from the corners, a number or vector. Default: 0.5.

#### `_bez_path_corner(p, curvesize, relative, mincurvesize=0.001)`

/   relative = if true, curvesize is a proportion between 0 and 1. If false, curvesize is an absolute distance that gets converted to a proportion internally.

#### `bezpath_close_to_axis(bezpath, axis="X", N=3)`

debug_bezier(closed);

#### `bezpath_offset(offset, bezier, N=3)`

debug_bezier(closed);

#### `bez_begin(pt, a, r, p)`

debug_bezier(bezpath);

#### `bez_tang(pt, a, r1, r2, p)`

p = If given, specifies the number of degrees away from the Z+ axis.

#### `bez_joint(pt, a1, a2, r1, r2, p1, p2)`

p2 = If given, specifies the number of degrees away from the Z+ axis of the departing control point.

#### `bez_end(pt, a, r, p)`

p = If given, specifies the number of degrees away from the Z+ axis.

#### `is_bezier_patch(x)`

x = The value to check the type of.

#### `bezier_patch_flat(size, N=1, spin=0, orient=UP, trans=[0, 0, 0])`

debug_bezier_patches([patch], size=1, showcps=true);

#### `bezier_patch_reverse(patch)`

patch = The patch to reverse.

#### `bezier_patch_points(patch, u, v)`

for (row=pts) move_copies(row) color("magenta") sphere(d=3, $fn=12);

#### `_bezier_rectangle(patch, splinesteps=16, style="default")`

#### `bezier_vnf(patches=[], splinesteps=16, style="default")`

vnf_polyhedron(concat(edges,corners,faces));

#### `bezier_vnf_degenerate_patch(patch, splinesteps=16, reverse=false, return_edges=false)`

color("red")move_copies(flatten(patch)) sphere(r=0.3,$fn=9);

#### `bezier_patch_normals(patch, u, v)`

#### `bezier_sheet(patch, delta, splinesteps=16, style="default", thickness=undef)`

## BOSL2/bosl1compat.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/bosl1compat.scad`

### Modules

#### `translate_copies(a=[[0, 0, 0]])`

#### `xspread(spacing, n, l, sp)`

#### `yspread(spacing, n, l, sp)`

#### `zspread(spacing, n, l, sp)`

#### `spread(p1=[0, 0, 0], p2=[10, 0, 0], spacing, l, n=2)`

#### `grid_of(xa=[0], ya=[0], za=[0], count, spacing)`

#### `xring(n=2, r=0, sa=0, cp=[0, 0, 0], rot=true)`

#### `yring(n=2, r=0, sa=0, cp=[0, 0, 0], rot=true)`

#### `zring(n=2, r=0, sa=0, cp=[0, 0, 0], rot=true)`

#### `leftcube(size)`

#### `rightcube(size)`

#### `fwdcube(size)`

#### `backcube(size)`

#### `downcube(size)`

#### `upcube(size)`

#### `cube2pt(p1, p2)`

#### `offsetcube(size=[1, 1, 1], v=[0, 0, 0])`

#### `rrect(size=[1, 1, 1], r=0.25, center=false)`

#### `rcube(size=[1, 1, 1], r=0.25, center=false)`

#### `chamfcube(size=[1, 1, 1], chamfer=0.25, chamfaxes=[1, 1, 1], chamfcorners=false)`

#### `trapezoid(size1=[1, 1], size2=[1, 1], h=1, shift=[0, 0], align=CTR, orient=0, center)`

#### `pyramid(n=4, h=1, l=1, r, d, circum=false)`

#### `prism(n=3, h=1, l=1, r, d, circum=false, center=false)`

#### `chamferred_cylinder(h, r, d, chamfer=0.25, chamfedge, angle=45, top=true, bottom=true, center=false)`

#### `chamf_cyl(h=1, r, d, chamfer=0.25, chamfedge, angle=45, center=false, top=true, bottom=true)`

#### `filleted_cylinder(h=1, r, d, r1, r2, d1, d2, fillet=0.25, center=false)`

#### `rcylinder(h=1, r=1, r1, r2, d, d1, d2, fillet=0.25, center=false)`

#### `thinning_brace(h=50, l=100, thick=5, ang=30, strut=5, wall=3, center=true)`

## BOSL2/bottlecaps.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/bottlecaps.scad`

### Modules

#### `pco1810_neck(wall=2, anchor="support-ring", spin=0, orient=UP)`

show_anchors(std=false);

#### `pco1810_cap(h, r, d, wall, texture="none", anchor=BOTTOM, spin=0, orient=UP)`

show_anchors(std=false);

#### `pco1881_neck(wall=2, anchor="support-ring", spin=0, orient=UP)`

show_anchors(std=false);

#### `pco1881_cap(wall=2, texture="none", anchor=BOTTOM, spin=0, orient=UP)`

show_anchors(std=false);

#### `sp_neck(diam, type, wall, id, style="L", bead=false, anchor, spin, orient)`

#### `sp_cap(diam, type, wall, style="L", top_adj=0, bot_adj=0, texture="none", anchor, spin, orient)`

sp_cap(28,415,1.5,style="M");

### Functions

#### `pco1810_neck(wall=2, anchor="support-ring", spin=0, orient=UP)`

#### `pco1810_cap(h, r, d, wall, texture="none", anchor=BOTTOM, spin=0, orient=UP)`

#### `pco1881_neck(wall=2, anchor="support-ring", spin=0, orient=UP)`

#### `pco1881_cap(wall=2, texture="none", anchor=BOTTOM, spin=0, orient=UP)`

#### `_sp_thread_profile(tpi, a, S, style, flip=false)`

#### `sp_neck(diam, type, wall, id, style="L", bead=false, anchor, spin, orient)`

#### `sp_diameter(diam, type)`

type = closure type number (400, 410 or 415)

## BOSL2/builtins.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/builtins.scad`

### Modules

#### `_square(size, center=false)`

/ Section: Builtin Modules

#### `_circle(r, d)`

#### `_text(text, size, font, halign, valign, spacing, direction, language, script)`

#### `_color(color)`

#### `_cube(size, center)`

#### `_cylinder(h, r1, r2, center, r, d, d1, d2)`

#### `_sphere(r, d)`

#### `_multmatrix(m)`

#### `_translate(v)`

#### `_rotate(a, v)`

#### `_scale(v)`

## BOSL2/color.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/color.scad`

### Modules

#### `recolor(c="default")`

attach(TOP,BOT) cuboid([4,4,2]);

#### `color_this(c="default")`

attach(TOP,BOT) cuboid([4,4,2]);

#### `rainbow(list, stride=1, maxhues, shuffle=false, seed)`

rainbow(rgn) stroke($item, closed=true);

#### `color_overlaps(color="red")`

}

#### `highlight(highlight=true)`

#### `highlight_this()`

#### `ghost(ghost=true)`

#### `ghost_this()`

#### `hsl(h, s=1, l=0.5, a=1)`

#### `hsv(h, s=1, v=1, a=1)`

### Functions

#### `highlight(highlight)`

highlight(false) attach(RIGHT,BOT)cuboid(5);

#### `highlight_this()`

attach(TOP,BOT)cuboid(5);

#### `ghost(ghost)`

ghost(false) cuboid(5);

#### `ghost_this()`

cuboid(5);

#### `hsl(h, s=1, l=0.5, a)`

color(rgb) cube(60, center=true);

#### `hsv(h, s=1, v=1, a)`

color(rgb) cube(60, center=true);

## BOSL2/comparisons.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/comparisons.scad`

### Functions

#### `approx(a, b, eps=_EPSILON)`

test6 = approx([0,0,sin(45)],[0,0,sqrt(2)/2]);  // Returns: true

#### `all_zero(x, eps=_EPSILON)`

d = all_zero([0,0,1e-3]);  // Returns: false.

#### `all_nonzero(x, eps=_EPSILON)`

e = all_nonzero([1e-3,1e-3,1e-3]);  // Returns: true.

#### `all_positive(x, eps=0)`

g = all_positive([3,-1,2]);  // Returns: false.

#### `all_negative(x, eps=0)`

h = all_negative([-3,-1,-2]);  // Returns: true.

#### `all_nonpositive(x, eps=0)`

h = all_nonpositive([-3,-1,-2]);  // Returns: true.

#### `all_nonnegative(x, eps=0)`

i = all_nonnegative([-3,-1,-2]);  // Returns: false.

#### `all_equal(vec, eps=0)`

eps = Set to tolerance for approximate equality.  Default: 0

#### `are_ends_equal(list, eps=_EPSILON)`

eps = Tolerance for approximate equality.  Default: 1e-9

#### `is_increasing(list, strict=false)`

e = is_increasing([4,3,2,1]);  // Returns: false

#### `is_decreasing(list, strict=false)`

c = is_decreasing([4,3,2,1]);  // Returns: true

#### `_type_num(x)`

#### `compare_vals(a, b)`

b = Second value to compare.

#### `compare_lists(a, b)`

b = Second list to compare.

#### `min_index(vals, all=false)`

b = min_index([5,3,9,6,2,7,8,2,7],all=true); // Returns: [4,7]

#### `max_index(vals, all=false)`

max_index([5,3,9,6,2,7,8,9,1],all=true); // Returns: [2,7]

#### `find_approx(val, list, start=0, all=false, eps=_EPSILON)`

find_approx(9,[4,5,3.01,2,2.99], all=true, eps=0.1);  // Returns []

#### `__find_approx(val, list, eps, i=0)`

#### `deduplicate(list, closed=false, eps=_EPSILON)`

e = deduplicate([[7,undef],[7,undef],[1,4],[1,4+1e-12]],eps=0);    // Returns: [[7,undef],[1,4],[1,4+1e-12]]

#### `deduplicate_indexed(list, indices, closed=false, eps=_EPSILON)`

echo(select(b,ind));         // Displays:  ["B", "C", "D", "F", "I"]

#### `list_wrap(list, eps=_EPSILON)`

#### `cleanup_path(list, eps=_EPSILON)`

#### `close_path(list, eps=_EPSILON)`

#### `list_unwrap(list, eps=_EPSILON)`

eps = epsilon for comparison.  Default: 1e-9

#### `unique(list)`

sorted = unique([true,2,"xba",[1,0],true,[0,0],3,"a",[0,0],2]); // Returns: [true,2,3,"a","xba",[0,0],[1,0]]

#### `_unique_sort(l)`

#### `unique_count(list)`

sorted = unique([5,2,8,3,1,3,8,3,5]);  // Returns: [ [1,2,3,5,8], [1,1,3,2,2] ]

#### `unique_approx(data, eps=_EPSILON)`

Returns a subset of items that differ by more thatn eps.

#### `unique_approx_indexed(data, eps=_EPSILON)`

Returns the indices of a subset of items that differ by more thatn eps.

#### `_valid_idx(idx, imin, imax)`

this allows imax=INF as a bound to numerical lists

#### `_group_sort_by_index(l, idx)`

idx should be an index of the arrays l[i]

#### `_group_sort(l)`

#### `_sort_scalars(arr)`

all elements should have the same type.

#### `_sort_vectors(arr, _i=0)`

uses native comparison operator

#### `_sort_vectors(arr, idxlist, _i=0)`

uses native comparison operator

#### `_sort_general(arr, idx=undef, indexed=false)`

sorting using compare_vals(); returns indexed list when `indexed==true`

#### `_lexical_sort(arr)`

lexical sort using compare_vals()

#### `_indexed_sort(arrind)`

the sorting is done using compare_vals()

#### `sort(list, idx=undef)`

sorted3 = sort(l3); // Returns: [20,[3,1],[3,9],[4],[4,0],[7],[8]]

#### `sortidx(list, idx=undef)`

idxs3 = sortidx(lst, idx=[1,3]); // Returns: [3,0,2,1]

#### `group_sort(list, idx)`

sorted2 = group_sort([[5,"a"],[2,"b"], [5,"c"], [3,"d"], [2,"e"] ], idx=0);

#### `group_data(groups, values)`

groups = group_data([1,3,1], ["A","B","C"]);  // Returns [[],["A","C"],[],["B"]]

#### `list_smallest(list, k)`

k = number of items to return

## BOSL2/constants.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/constants.scad`

### Functions

#### `get_slop()`

Always access the `$slop` variable using this function.

#### `EDGE(a, b)`

#### `FACE(i)`

## BOSL2/coords.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/coords.scad`

### Functions

#### `point2d(p, fill=0)`

fill = Value to fill missing values in vector with.  Default: 0

#### `path2d(points)`

points = A list of 2D or 3D points/vectors.

#### `point3d(p, fill=0)`

fill = Value to fill missing values in vector with.  Default: 0

#### `path3d(points, fill=0)`

fill = Scalar value to fill missing values in vectors with (in the 2D case).  Default: 0

#### `point4d(p, fill=0)`

fill = Scalar value to fill missing values in vector with.  Default: 0

#### `path4d(points, fill=0)`

fill = Scalar value to fill missing values in vectors with.  Default: 0

#### `polar_to_xy(r, theta)`

color("red") move(pt) circle(d=3);

#### `xy_to_polar(x, y)`

color("red") move(pt) circle(d=3);

#### `project_plane(plane, p)`

stroke(xypath,closed=true);

#### `lift_plane(plane, p)`

p = points, path, region, VNF, or bezier patch to transform.

#### `cylindrical_to_xyz(r, theta, z)`

xyz = cylindrical_to_xyz([40,60,50]);

#### `xyz_to_cylindrical(x, y, z)`

cyls = xyz_to_cylindrical([[40,50,70], [-10,15,-30]]);

#### `spherical_to_xyz(r, theta, phi)`

xyzs = spherical_to_xyz([[40,60,50], [50,120,100]]);

#### `xyz_to_spherical(x, y, z)`

sphs = xyz_to_spherical([[40,50,70], [25,-14,27]]);

#### `altaz_to_xyz(alt, az, r)`

xyz = altaz_to_xyz([40,60,50]);

#### `xyz_to_altaz(x, y, z)`

aa = xyz_to_altaz([40,50,70]);

## BOSL2/cubetruss.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/cubetruss.scad`

### Modules

#### `cubetruss(extents=6, clips=[], bracing, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss(extents=[1,4,2], bracing=false);

#### `cubetruss_corner(h=1, extents=[1, 1, 0, 0, 1], bracing, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss_corner(extents=[3,3,3,3,2]);

#### `cubetruss_support(size, strut, extents=1, anchor=CENTER, spin=0, orient=UP)`

cubetruss_support(extents=2) show_anchors();

#### `cubetruss_foot(w=1, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss_foot(w=3);

#### `cubetruss_joiner(w=1, vert=true, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss_joiner(w=2, vert=true, anchor=BOT);

#### `cubetruss_uclip(dual=true, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss_uclip(dual=true);

#### `cubetruss_segment(size, strut, bracing, anchor=CENTER, spin=0, orient=UP)`

cubetruss_segment(size=40);

#### `cubetruss_clip(extents=1, size, strut, clipthick, anchor=CENTER, spin=0, orient=UP)`

cubetruss_clip(clipthick=2.5);

### Functions

#### `cubetruss_dist(cubes=0, gaps=0, size, strut)`

strut = The width of the struts on the cubetruss cubes.  Default: `$cubetruss_strut_size` (usually 3)

## BOSL2/distributors.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/distributors.scad`

### Modules

#### `move_copies(a=[[0, 0, 0]])`

move_copies([[-25,-25,0], [25,-25,0], [0,0,50], [0,25,0]]) sphere(r=10);

#### `xcopies(spacing, n, l, sp)`

xcopies([1,2,3,5,7]) sphere(d=1);

#### `ycopies(spacing, n, l, sp)`

ycopies([1,2,3,5,7]) sphere(d=1);

#### `zcopies(spacing, n, l, sp)`

zcopies([1,2,3,5,7]) sphere(d=1);

#### `line_of(spacing, n, l, p1, p2)`

#### `line_copies(spacing, n, l, p1, p2)`

#### `grid2d(spacing, n, size, stagger=false, inside=undef, nonzero)`

#### `grid_copies(spacing, n, size, stagger=false, inside=undef, nonzero, axes="xy")`

#### `rot_copies(rots=[], v, cp=[0, 0, 0], n, sa=0, offset=0, delta=[0, 0, 0], subrot=true)`

color("red",0.333) yrot(90) cylinder(h=20, r1=5, r2=0);

#### `xrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true)`

color("red",0.333) xrot(-90) cylinder(h=20, r1=5, r2=0, center=true);

#### `yrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true)`

color("red",0.333) yrot(-90) cylinder(h=20, r1=5, r2=0, center=true);

#### `zrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true)`

color("red",0.333) yrot(-90) cylinder(h=20, r1=5, r2=0, center=true);

#### `arc_of(n=6, r, rx, ry, d, dx, dy, sa=0, ea=360, rot=true)`

#### `ovoid_spread(n=100, r=undef, d=undef, cone_ang=90, scale=[1, 1, 1], perp=true)`

#### `sphere_copies(n=100, r=undef, d=undef, cone_ang=90, scale=[1, 1, 1], perp=true)`

#### `path_spread(path, n, spacing, sp=undef, rotate_children=true, dist, closed)`

#### `path_copies(path, n, spacing, sp=undef, dist, rotate_children=true, dist, closed)`

#### `xflip_copy(offset=0, x=0)`

color("blue",0.25) left(5) cube([0.01,15,15], center=true);

#### `yflip_copy(offset=0, y=0)`

color("blue",0.25) fwd(5) cube([15,0.01,15], center=true);

#### `zflip_copy(offset=0, z=0)`

color("blue",0.25) down(5) cube([15,15,0.01], center=true);

#### `mirror_copy(v=[0, 0, 1], offset=0, cp)`

color("blue",0.25) translate([0,-5,-5]) rot(from=UP, to=BACK+UP) cube([15,15,0.01], center=true);

#### `xdistribute(spacing=10, sizes=undef, l=undef)`

}

#### `ydistribute(spacing=10, sizes=undef, l=undef)`

}

#### `zdistribute(spacing=10, sizes=undef, l=undef)`

}

#### `distribute(spacing=undef, sizes=undef, dir=RIGHT, l=undef)`

}

### Functions

#### `move_copies(a=[[0, 0, 0]], p=_NO_ARG)`

#### `xcopies(spacing, n, l, sp, p=_NO_ARG)`

#### `ycopies(spacing, n, l, sp, p=_NO_ARG)`

#### `zcopies(spacing, n, l, sp, p=_NO_ARG)`

#### `line_copies(spacing, n, l, p1, p2, p=_NO_ARG)`

#### `grid_copies(spacing, n, size, stagger=false, inside=undef, nonzero, axes="xy", p=_NO_ARG)`

#### `rot_copies(rots=[], v, cp=[0, 0, 0], n, sa=0, offset=0, delta=[0, 0, 0], subrot=true, p=_NO_ARG)`

#### `xrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true, p=_NO_ARG)`

#### `yrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true, p=_NO_ARG)`

#### `zrot_copies(rots=[], cp=[0, 0, 0], n, sa=0, r, d, subrot=true, p=_NO_ARG)`

#### `sphere_copies(n=100, r=undef, d=undef, cone_ang=90, scale=[1, 1, 1], perp=true, p=_NO_ARG)`

#### `path_copies(path, n, spacing, sp=undef, dist, rotate_children=true, dist, closed, p=_NO_ARG)`

#### `xflip_copy(offset=0, x=0, p=_NO_ARG)`

#### `yflip_copy(offset=0, y=0, p=_NO_ARG)`

#### `zflip_copy(offset=0, z=0, p=_NO_ARG)`

#### `mirror_copy(v=[0, 0, 1], offset=0, cp, p=_NO_ARG)`

## BOSL2/drawing.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/drawing.scad`

### Modules

#### `setcolor(clr)`

#### `dashed_stroke(path, dashpat=[3, 3], width=1, closed=false, fit=true, roundcaps=false)`

#### `arc(n, r, angle, d, cp, points, corner, width, thickness, start, wedge=false, rounding, anchor=CENTER, spin=0)`

#### `catenary(width, droop, n=100, angle, anchor=CTR, spin=0)`

#### `helix(l, h, turns, angle, r, r1, r2, d, d1, d2)`

stroke(helix(h=0,r1=50,r2=25,l=0, turns=4));

#### `turtle(commands, state=[[[0, 0]], [1, 0], 90, 0], full_state=false, repeat=1)`

polygon(turtle(koch));

#### `debug_polygon(points, paths, vertices=true, edges=true, convexity=2, size=1)`

);

#### `_debug_poly_verts(points, size)`

#### `_debug_poly_edges(j, points, path, vertices, size)`

### Functions

#### `_shape_defaults(cap)`

#### `_shape_path(cap, linewidth, w, l, l2)`

#### `dashed_stroke(path, dashpat=[3, 3], closed=false, fit=true, mindash=0.5)`

dashed_stroke(path, [3,2], width=1);

#### `arc(n, r, angle, d, cp, points, corner, width, thickness, start, wedge=false, long=false, cw=false, ccw=false, endpoint=true, rounding, _minpts=2)`

#### `_rounded_arc(radius, rounding=0, angle, n)`

#### `catenary(width, droop, n=100, angle)`

path_sweep(circle(r=1.5, $fn=24), path);

#### `helix(l, h, turns, angle, r, r1, r2, d, d1, d2)`

#### `_normal_segment(p1, p2)`

#### `turtle(commands, state=[[[0, 0]], [1, 0], 90, 0], full_state=false, repeat=1)`

#### `_turtle_repeat(commands, state, full_state, repeat)`

#### `_turtle_command_len(commands, index)`

#### `_turtle(commands, state, full_state, index=0)`

#### `_turtle_command(command, parm, parm2, state, index)`

## BOSL2/examples/boolean_geometry.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/examples/boolean_geometry.scad`

### Modules

#### `showit(label, rgn, poly=polycolor, outline=outlinecolor, width=0.5)`

## BOSL2/examples/fractal_tree.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/examples/fractal_tree.scad`

### Modules

#### `tree(l=1500, sc=0.7, depth=10)`

## BOSL2/examples/lsystems.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/examples/lsystems.scad`

### Functions

#### `_lsystem_recurse(s, rules, lev)`

#### `_lsystem_to_turtle(s, step=1, angle=90, startang=0)`

#### `lsystem_turtle(basis, rules, levels=5, step=1, angle=90, startang=0)`

#### `dragon_curve(levels=9, step=1)`

#### `terdragon_curve(levels=7, step=1)`

#### `twindragon_curve(levels=11, step=1)`

#### `moore_curve(levels=4, step=1)`

#### `hilbert_curve(levels=4, step=1)`

#### `gosper_curve(levels=4, step=1)`

#### `quadratic_gosper(levels=2, step=1)`

#### `peano_curve(levels=4, step=1)`

#### `koch_snowflake(levels=4, step=1)`

#### `sierpinski_arrowhead(levels=6, step=1)`

#### `sierpinski_triangle(levels=4, step=1)`

#### `square_sierpinski(levels=5, step=1)`

#### `cesaro_curve(levels=4, step=1)`

#### `paul_bourke1(levels=3, step=1)`

#### `paul_bourke_triangle(levels=6, step=1)`

#### `paul_bourke_crystal(levels=4, step=1)`

#### `space_filling_tree(levels=4, step=1)`

#### `krishna_anklets(levels=6, step=1)`

## BOSL2/examples/orientations.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/examples/orientations.scad`

### Modules

#### `orient_cube(ang)`

#### `text3d(text, h=0.01, size=3)`

#### `dottedline(l, d)`

#### `orient_cubes()`

## BOSL2/fnliterals.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/fnliterals.scad`

### Functions

#### `map(func, list)`

seglens = map(function (p) norm(p[1]-p[0]), pair(path,wrap=true));

#### `filter(func, list)`

// ECHO: [6,7]

#### `reduce(func, list, init=0)`

y = reduce(f_or(),[true,false,true]);   // Returns: true

#### `accumulate(func, list, init=0)`

echo(accumulate(f_mul(),[3,4,5],1)); // ECHO: [3,12,60,360]

#### `while(init, cond, func)`

);  // Returns: [1,1,2,3,5,8,13,21]

#### `for_n(n, init, func)`

)[1];

#### `find_all(func, list)`

// ECHO: [3,4]

#### `find_first(func, list, start=0)`

// ECHO: 4

#### `binsearch(key, list, idx, cmp=f_cmp()`

idx = binsearch("G", items, idx=0);

#### `simple_hash(x)`

x = simple_hash([[10,20],[-5,3]]);

#### `hashmap(hashsize=127, items, table)`

}

#### `f_1arg(target_func)`

fn_str3 = f_str(3); // = function() str(3);

#### `f_2arg(target_func)`

fn_3lt4 = f_lt(3,4); // = function() 3<4;

#### `f_2arg_simple(target_func)`

fn_3lt4 = f_lt(3,4);  // = function() 3<4;

#### `f_3arg(target_func)`

fn_va4 = f_lt(a=p1,c=p2); // = function() vector_angle(p1,b,p2);

#### `ival(target_func)`

x = while(0, ival(f_lt(5)), xval(f_add(1)));

#### `xval(target_func)`

x = while(0, ival(f_lt(5)), xval(f_add(1)));

#### `f_cmp(a, b)`

fn_3cmp4 = f_cmp(3,4);  // = function() 3==4?0: 3>4?1: -1;

#### `f_gt(a, b)`

fn_3gt4 = f_gt(3,4);  // = function() 3>4;

#### `f_lt(a, b)`

fn_3lt4 = f_lt(3,4);  // = function() 3<4;

#### `f_gte(a, b)`

fn_3gte4 = f_gte(3,4);  // = function() 3>=4;

#### `f_lte(a, b)`

fn_3lte4 = f_lte(3,4);  // = function() 3<=4;

#### `f_eq(a, b)`

fn_3eq4 = f_eq(3,4);  // = function() 3==4;

#### `f_neq(a, b)`

fn_3neq4 = f_neq(3,4);  // = function() 3!=4;

#### `f_approx(a, b)`

fn_3approx4 = f_approx(3,4);  // = function() approx(3,4);

#### `f_napprox(a, b)`

fn_3napprox4 = f_napprox(3,4);  // = function() napprox(3,4);

#### `f_or(a, b)`

b = If given, replaces the second argument.

#### `f_and(a, b)`

b = If given, replaces the second argument.

#### `f_nor(a, b)`

b = If given, replaces the second argument.

#### `f_nand(a, b)`

b = If given, replaces the second argument.

#### `f_xor(a, b)`

b = If given, replaces the second argument.

#### `f_not(a)`

a = If given, replaces the argument.

#### `f_even(a)`

l2 = filter(f_even(), [3,4,5,6,7,8]);  // Returns: [4,6,8]

#### `f_odd(a)`

l2 = filter(f_odd(), [3,4,5,6,7,8]);  // Returns: [3,5,7]

#### `f_add(a, b)`

b = If given, replaces the second argument.

#### `f_sub(a, b)`

b = If given, replaces the second argument.

#### `f_mul(a, b)`

b = If given, replaces the second argument.

#### `f_div(a, b)`

b = If given, replaces the second argument.

#### `f_mod(a, b)`

b = If given, replaces the second argument.

#### `f_pow(a, b)`

b = If given, replaces the second argument.

#### `f_neg(a)`

a = If given, replaces the argument.

#### `f_min(a)`

a = If given, replaces the argument.

#### `f_max(a)`

a = If given, replaces the argument.

#### `f_min2(a, b)`

b = If given, replaces the second argument.

#### `f_max2(a, b)`

b = If given, replaces the second argument.

#### `f_min3(a, b, c)`

c = If given, replaces the third argument.

#### `f_max3(a, b, c)`

c = If given, replaces the third argument.

#### `f_sin(a)`

a = If given, replaces the argument.

#### `f_cos(a)`

a = If given, replaces the argument.

#### `f_tan(a)`

a = If given, replaces the argument.

#### `f_asin(a)`

a = If given, replaces the argument.

#### `f_acos(a)`

a = If given, replaces the argument.

#### `f_atan(a)`

a = If given, replaces the argument.

#### `f_atan2(a, b)`

b = If given, replaces the second argument.

#### `f_len(a)`

a = If given, replaces the argument.

#### `f_chr(a)`

a = If given, replaces the argument.

#### `f_ord(a)`

a = If given, replaces the argument.

#### `f_str(a)`

a = If given, replaces the argument.

#### `f_str2(a, b)`

b = If given, replaces the second argument.

#### `f_str3(a, b, c)`

c = If given, replaces the third argument.

#### `f_floor(a)`

a = If given, replaces the argument.

#### `f_round(a)`

a = If given, replaces the argument.

#### `f_ceil(a)`

a = If given, replaces the argument.

#### `f_abs(a)`

a = If given, replaces the argument.

#### `f_sign(a)`

a = If given, replaces the argument.

#### `f_ln(a)`

a = If given, replaces the argument.

#### `f_log(a)`

a = If given, replaces the argument.

#### `f_exp(a)`

a = If given, replaces the argument.

#### `f_sqr(a)`

a = If given, replaces the argument.

#### `f_sqrt(a)`

a = If given, replaces the argument.

#### `f_norm(a)`

a = If given, replaces the argument.

#### `f_cross(a, b)`

b = If given, replaces the second argument.

#### `f_is_def(a)`

a = If given, replaces the argument.

#### `f_is_undef(a)`

a = If given, replaces the argument.

#### `f_is_bool(a)`

a = If given, replaces the argument.

#### `f_is_num(a)`

a = If given, replaces the argument.

#### `f_is_int(a)`

a = If given, replaces the argument.

#### `f_is_nan(a)`

a = If given, replaces the argument.

#### `f_is_finite(a)`

a = If given, replaces the argument.

#### `f_is_string(a)`

a = If given, replaces the argument.

#### `f_is_list(a)`

a = If given, replaces the argument.

#### `f_is_range(a)`

a = If given, replaces the argument.

#### `f_is_function(a)`

a = If given, replaces the argument.

#### `f_is_vector(a, b)`

a = If given, replaces the argument.

#### `f_is_path(a, b)`

a = If given, replaces the argument.

#### `f_is_region(a)`

a = If given, replaces the argument.

#### `f_is_vnf(a)`

a = If given, replaces the argument.

#### `f_is_patch(a)`

a = If given, replaces the argument.

## BOSL2/gears.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/gears.scad`

### Functions

#### `_inherit_gear_param(name, val, pval, dflt, invert=false)`

#### `_inherit_gear_pitch(fname, pitch, circ_pitch, diam_pitch, mod, warn=true)`

#### `_inherit_gear_pa(pressure_angle)`

#### `_inherit_gear_helical(helical, invert=false)`

#### `_inherit_gear_thickness(thickness, dflt=10)`

#### `circular_pitch(circ_pitch, mod, pitch, diam_pitch)`

#### `diametral_pitch(circ_pitch, mod, pitch, diam_pitch)`

#### `module_value(circ_pitch, mod, pitch, diam_pitch)`

#### `outer_radius(circ_pitch, teeth, clearance, internal=false, helical=0, profile_shift="auto", pressure_angle=20, shorten=0, mod, pitch, diam_pitch)`

#### `root_radius(teeth, helical=0, clearance, internal=false, profile_shift="auto", pressure_angle=20, mod, circ_pitch, diam_pitch, backlash=0)`

#### `_root_radius_basic(circ_pitch, teeth, clearance, internal=false, helical=0, profile_shift=0, diam_pitch, mod, pitch)`

#### `_base_radius(circ_pitch, teeth, pressure_angle=20, helical=0, diam_pitch, mod, pitch)`

#### `bevel_pitch_angle(teeth, mate_teeth, drive_angle=90)`

#### `worm_dist(d, starts, teeth, mod, profile_shift=0, diam_pitch, circ_pitch, pressure_angle=20, backlash=0)`

#### `_invol(a)`

#### `_working_pressure_angle(teeth1, profile_shift1, teeth2, profile_shift2, pressure_angle, helical)`

#### `_working_normal_pressure_angle_skew(teeth1, profile_shift1, helical1, teeth2, profile_shift2, helical2, pressure_angle)`

#### `gear_skew_angle(teeth1, teeth2, helical1, helical2, profile_shift1, profile_shift2, pressure_angle=20)`

#### `get_profile_shift(desired, teeth1, teeth2, helical=0, pressure_angle=20, internal1=false, internal2=false, mod, diam_pitch, circ_pitch)`

#### `auto_profile_shift(teeth, pressure_angle=20, helical=0, min_teeth, profile_shift, get_min=false)`

profile_shift = If numerical then just return this value; if "auto" or not given then compute the automatic profile shift.

#### `gear_shorten(teeth1, teeth2, helical=0, profile_shift1="auto", profile_shift2="auto", pressure_angle=20)`

spur_gear2d(mod=mod,teeth=teeth2,profile_shift=ps2,shorten=shorten,gear_spin=-90);

#### `gear_shorten_skew(teeth1, teeth2, helical1, helical2, profile_shift1="auto", profile_shift2="auto", pressure_angle=20)`

pressure_angle = The pressure angle of the gear.

## BOSL2/geometry.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/geometry.scad`

### Modules

#### `show_plane(plane, size, offset=0)`

#### `hull_points(points, fast=false)`

hull_points(pts);

### Functions

#### `is_point_on_line(point, line, bounded=false, eps=_EPSILON)`

eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `_is_point_on_line(point, line, bounded=false, eps=_EPSILON)`

#### `_dist2line(d, n)`

/_dist2line works for any dimension

#### `_valid_line(line, dim, eps=_EPSILON)`

/Internal

#### `_valid_plane(p, eps=_EPSILON)`

Internal

#### `_is_at_left(pt, line, eps=_EPSILON)`

/   eps = Tolerance in the geometrical tests.

#### `_degenerate_tri(tri, eps)`

/   eps = Tolerance in the geometrical tests.

#### `_tri_class(tri, eps=_EPSILON)`

/   eps = Tolerance in the geometrical tests.

#### `_pt_in_tri(point, tri, eps=_EPSILON)`

/   eps = Tolerance in the geometrical tests.

#### `_point_left_of_line2d(point, line, eps=_EPSILON)`

/   line  = Array of two points forming the line segment to test against.

#### `is_collinear(a, b, c, eps=_EPSILON)`

eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `point_line_distance(pt, line, bounded=false)`

dist3 = point_line_distance([14,3], [[-10,0], [10,0]],SEGMENT);  // Returns: 5

#### `segment_distance(seg1, seg2, eps=_EPSILON)`

dist2 = segment_distance([[-5,5], [5,-5]], [[-10,3], [10,-3]]);  // Returns: 0

#### `line_normal(p1, p2)`

color("blue") move_copies([p1,p2]) circle(d=2, $fn=12);

#### `_general_line_intersection(s1, s2, eps=_EPSILON)`

#### `line_intersection(line1, line2, bounded1, bounded2, bounded, eps=_EPSILON)`

isect = line_intersection(line1, line2, bounded=true);  // Returns undef

#### `line_closest_point(line, pt, bounded=false)`

color("red") translate(p2) sphere(r=1,$fn=12);

#### `_line_greatest_distance(points, line)`

#### `line_from_points(points, check_collinear=false, eps=_EPSILON, fast)`

#### `is_coplanar(points, eps=_EPSILON)`

eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `plane3pt(p1, p2, p3)`

p3 = The third point on the plane.

#### `plane3pt_indexed(points, i1, i2, i3)`

i3 = The index into `points` of the third point on the plane.

#### `plane_from_normal(normal, pt=[0, 0, 0])`

plane_from_normal([0,0,1], [2,2,2]);  // Returns the xy plane passing through the point (2,2,2)

#### `_eigenvals_symm_3(M)`

Based on: https://en.wikipedia.org/wiki/Eigenvalue_algorithm

#### `_eigenvec_symm_3(M, evals, i=0)`

https://en.wikipedia.org/wiki/Eigenvalue_algorithm

#### `_covariance_evec_eval(points, eigenvalue_id)`

returns the mean of the points, the eigenvector and the greatest eigenvalue

#### `plane_from_points(points, check_coplanar=false, eps=_EPSILON, fast)`

}

#### `plane_from_polygon(poly, check_coplanar=true, eps=_EPSILON, fast)`

move(cp) rot(from=UP,to=plane_normal(plane)) anchor_arrow(45);

#### `plane_normal(plane)`

plane = The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.

#### `plane_offset(plane)`

plane = The `[A,B,C,D]` plane definition where `Ax+By+Cz=D` is the formula of the plane.

#### `_general_plane_line_intersection(plane, line, eps=_EPSILON)`

Returns undef if line is parallel to, but not on the given plane.

#### `_normalize_plane(plane)`

/   Returns a new representation [A,B,C,D] of `plane` where norm([A,B,C]) is equal to one.

#### `plane_line_intersection(plane, line, bounded=false, eps=_EPSILON)`

eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `plane_intersection(plane1, plane2, plane3)`

plane3 = The [A,B,C,D] coefficients for the third plane equation `Ax+By+Cz=D`.

#### `plane_line_angle(plane, line)`

the same side of the plane as the plane's normal vector.

#### `plane_closest_point(plane, points)`

}

#### `point_plane_distance(plane, point)`

point = The distance evaluation point.

#### `_pointlist_greatest_distance(points, plane)`

the maximum distance from points to the plane

#### `are_points_on_plane(points, plane, eps=_EPSILON)`

eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `_is_point_above_plane(plane, point)`

/   point = The 3D point to test.

#### `circle_line_intersection(r, cp, line, bounded=false, d, eps=_EPSILON)`

color("#f44") move_copies(isects) circle(d=1);

#### `_circle_or_sphere_line_intersection(r, cp, line, bounded=false, d, eps=_EPSILON)`

#### `circle_circle_intersection(r1, cp1, r2, cp2, eps=_EPSILON, d1, d2)`

color("red") move_copies(pts) circle(r=.3);

#### `circle_2tangents(r, pt1, pt2, pt3, tangents=false, d)`

}

#### `circle_3points(pt1, pt2, pt3)`

move_copies(pts) color("blue") circle(d=3, $fn=12);

#### `circle_point_tangents(r, cp, pt, d)`

color("blue") move_copies([cp,pt]) circle(d=3,$fn=12);

#### `circle_circle_tangents(r1, cp1, r2, cp2, d1, d2)`

echo(pts);   // Returns []

#### `_noncollinear_triple(points, error=true, eps=_EPSILON)`

/   eps = Tolerance for collinearity test. Default: 1e-9.

#### `sphere_line_intersection(r, cp, line, bounded=false, d, eps=_EPSILON)`

color("red") move_copies(isects) sphere(d=3, $fn=12);

#### `polygon_area(poly, signed=false)`

signed = If true, a signed area is returned. Default: false.

#### `centroid(object, eps=_EPSILON)`

color("red") move(cp) sphere(d=2);

#### `_region_centroid(region, eps=_EPSILON)`

/ Compute centroid of region

#### `_polygon_centroid(poly, eps=_EPSILON)`

/   eps = Tolerance in geometric comparisons.  Default: 1e-9

#### `polygon_normal(poly)`

stroke([[0,0,0], [0,0,20]], endcap2="arrow2");

#### `_point_above_below_segment(point, edge)`

#### `point_in_polygon(point, poly, nonzero=false, eps=_EPSILON)`

#### `polygon_line_intersection(poly, line, bounded=false, nonzero=false, eps=_EPSILON)`

stroke(part);

#### `_merge_segments(insegs, outsegs, eps, i=1)`

#### `polygon_triangulate(poly, ind, error=true, eps=_EPSILON)`

vnf_wireframe(vnf_tri, width=.15);

#### `_triangulate(poly, ind, error, eps=_EPSILON, tris=[])`

CW polygons.

#### `_get_ear(poly, ind, eps, _i=0)`

/ the returned ear is specified by the index of `ind` of its first vertex

#### `_none_inside(idxs, poly, p0, p1, p2, eps, i=0)`

/ note: to simplify the expressions it is assumed that the input polygon has no twists

#### `is_polygon_clockwise(poly)`

For algorithm see 2.07 here: http://www.faqs.org/faqs/graphics/algorithms-faq/

#### `clockwise_polygon(poly)`

poly = The list of 2D path points for the perimeter of the polygon.

#### `ccw_polygon(poly)`

poly = The list of 2D path points for the perimeter of the polygon.

#### `reverse_polygon(poly)`

poly = The list of the path points for the perimeter of the polygon.

#### `reindex_polygon(reference, poly, return_error=false)`

color("blue") translate(reindexed[0])circle(r=.1,$fn=32);

#### `align_polygon(reference, poly, angles, cp, trans, return_ind=false)`

color("blue")stroke(aligned,width=.5,closed=true);

#### `are_polygons_equal(poly1, poly2, eps=_EPSILON)`

rot(90, p=pentagon(r=4)));    // returns false

#### `_are_polygons_equal(poly1, poly2, eps, st)`

#### `_is_polygon_in_list(poly, polys)`

/   polys = The list of polygons to look for the polygon in.

#### `___is_polygon_in_list(poly, polys, i)`

#### `hull(points)`

points = The set of 2D or 3D points to find the hull of.

#### `_backtracking(i, points, h, t, m, all)`

#### `_is_cw(a, b, c, all)`

clockwise check (2d)

#### `hull2d_path(points, all=false)`

#### `_hull_collinear(points)`

#### `hull3d_faces(points)`

%polyhedron(points=pts, faces=faces);

#### `_hull3d_iterative(points, triangles, planes, remaining, _i=0)`

Adds the remaining points one by one to the convex hull

#### `_remove_internal_edges(halfedges)`

#### `_find_first_noncoplanar(plane, points, i=0)`

#### `is_polygon_convex(poly, eps=_EPSILON)`

test = is_polygon_convex(spiral);                                        // Returns: false

#### `convex_distance(points1, points2, eps=_EPSILON)`

echo(convex_distance(sphr1[0], sphr3[0])); // Returns: 0.5

#### `_GJK_distance(points1, points2, eps=_EPSILON, lbd, d, simplex=[])`

http://www.dtecta.com/papers/jgt98convex.pdf

#### `convex_collision(points1, points2, eps=_EPSILON)`

#### `_GJK_collide(points1, points2, d, simplex, eps=_EPSILON)`

http://www.dtecta.com/papers/jgt98convex.pdf

#### `_closest_simplex(s, eps=_EPSILON)`

- the smallest sub-simplex of s that contains that point

#### `_closest_s1(s, eps=_EPSILON)`

find the point of a 1-simplex closest to the origin

#### `_closest_s2(s, eps=_EPSILON)`

find the point of a 2-simplex closest to the origin

#### `_closest_s3(s, eps=_EPSILON)`

find the point of a 3-simplex closest to the origin

#### `_tri_normal(tri)`

#### `_support_diff(p1, p2, d)`

#### `rot_decode(M, long=false)`

// Returns: [0, [0,0,1], [0,0,0], [3,4,5]]

## BOSL2/hinges.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/hinges.scad`

### Modules

#### `living_hinge_mask(l, thick, layerheight=0.2, foldangle=90, hingegap=undef, anchor=CENTER, spin=0, orient=UP)`

living_hinge_mask(l=100, thick=3, foldangle=60);

#### `folding_hinge_mask(l, thick, layerheight=0.2, foldangle=90, hingegap=undef, anchor=CENTER, spin=0, orient=UP)`

#### `apply_folding_hinges_and_snaps(thick, foldangle=90, hinges=[], snaps=[], sockets=[], snaplen=5, snapdiam=5, hingegap=undef, layerheight=0.2)`

}

#### `snap_lock(thick, snaplen=5, snapdiam=5, layerheight=0.2, foldangle=90, hingegap=undef, anchor=CENTER, spin=0, orient=UP)`

snap_lock(thick=3, foldangle=60);

#### `snap_socket(thick, snaplen=5, snapdiam=5, layerheight=0.2, foldangle=90, hingegap=undef, anchor=CENTER, spin=0, orient=UP)`

snap_socket(thick=3, foldangle=60);

## BOSL2/isosurface.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/isosurface.scad`

### Modules

#### `metaballs(spec, bounding_box, voxel_size, voxel_count, isovalue=1, closed=true, exact_bounds=false, convexity=6, cp="centroid", anchor="origin", spin=0, orient=UP, atype="hull", show_stats=false, show_box=false, debug=false)`

#### `metaballs2d(spec, bounding_box, pixel_size, pixel_count, isovalue=1, use_centers=false, smoothing=undef, exact_bounds=false, convexity=6, cp="centroid", anchor="origin", spin=0, atype="hull", show_stats=false, show_box=false, debug=false)`

#### `isosurface(f, isovalue, bounding_box, voxel_size, voxel_count=undef, reverse=false, closed=true, exact_bounds=false, convexity=6, cp="centroid", anchor="origin", spin=0, orient=UP, atype="hull", show_stats=false, show_box=false, _mball=false)`

#### `contour(f, isovalue, bounding_box, pixel_size, pixel_count=undef, use_centers=true, smoothing=undef, exact_bounds=false, cp="centroid", anchor="origin", spin=0, atype="hull", show_stats=false, show_box=false, _mball=false)`

### Functions

#### `_cubeindex(f, isoval)`

/ Return the index ID of a voxel depending on the field strength at each corner exceeding isoval.

#### `_clipfacindex(f, isovalmin, isovalmax)`

Returns a decimal version of a 4-digit base-3 index.

#### `_bbox_faces(v0, voxsize, bbox)`

/ return an array of face indices in _MCFaceVertexIndices if the voxel at coordinate v0 corresponds to the bounding box. voxsize is a 3-vector.

#### `_isosurface_cubes(voxsize, bbox, fieldarray, fieldfunc, isovalmin, isovalmax, closed=true)`

#### `_isosurface_triangles(cubelist, voxsize, isovalmin, isovalmax, tritablemin, tritablemax)`

/ Given a list of voxel cubes structures, triangulate the isosurface(s) that intersect each cube and return a list of triangle vertices.

#### `_clipfacevertices(vcube, fld, bbface, isovalmin, isovalmax)`

/ Generate triangles for the special case of voxel faces clipped by the bounding box

#### `_mctrindex(f, isoval)`

/ Return the index ID of a pixel depending on the field strength at each vertex exceeding isoval.

#### `_bbox_sides(pc, pixsize, bbox)`

/ return an array of edgee indices in _MTEdgeVertexIndices if the pixel at coordinate pc corresponds to the bounding box.

#### `_contour_pixels(pixsize, bbox, fieldarray, fieldfunc, pixcenters, isovalmin, isovalmax, closed=true)`

#### `_contour_vertices(pxlist, pxsize, isovalmin, isovalmax, segtablemin, segtablemax)`

#### `mb_cutoff(dist, cutoff)`

#### `_mb_sphere_basic(point, r, neg)`

#### `_mb_sphere_influence(point, r, ex, neg)`

#### `_mb_sphere_cutoff(point, r, cutoff, neg)`

#### `_mb_sphere_full(point, r, cutoff, ex, neg)`

#### `mb_sphere(r, cutoff=INF, influence=1, negative=false, hide_debug=false, d)`

#### `_mb_cuboid_basic(point, inv_size, xp, neg)`

#### `_mb_cuboid_influence(point, inv_size, xp, ex, neg)`

#### `_mb_cuboid_cutoff(point, inv_size, xp, cutoff, neg)`

#### `_mb_cuboid_full(point, inv_size, xp, ex, cutoff, neg)`

#### `mb_cuboid(size, squareness=0.5, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `_revsurf_basic(point, path, coef, neg, maxdist)`

#### `_revsurf_influence(point, path, coef, exp, neg, maxdist)`

#### `_revsurf_cutoff(point, path, coef, cutoff, neg, maxdist)`

#### `_revsurf_full(point, path, coef, cutoff, exp, neg, maxdist)`

#### `mb_cyl(h, r, rounding=0, r1, r2, l, height, length, d1, d2, d, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `_mb_disk_basic(point, hl, r, neg)`

#### `_mb_disk_influence(point, hl, r, ex, neg)`

#### `_mb_disk_cutoff(point, hl, r, cutoff, neg)`

#### `_mb_disk_full(point, hl, r, cutoff, ex, neg)`

#### `mb_disk(h, r, cutoff=INF, influence=1, negative=false, hide_debug=false, d, l, height, length)`

#### `_mb_capsule_basic(dv, hl, r, neg)`

#### `_mb_capsule_influence(dv, hl, r, ex, neg)`

#### `_mb_capsule_cutoff(dv, hl, r, cutoff, neg)`

#### `_mb_capsule_full(dv, hl, r, cutoff, ex, neg)`

#### `mb_capsule(h, r, cutoff=INF, influence=1, negative=false, hide_debug=false, d, l, height, length)`

#### `mb_connector(p1, p2, r, cutoff=INF, influence=1, negative=false, hide_debug=false, d)`

#### `_mb_torus_basic(point, rmaj, rmin, neg)`

#### `_mb_torus_influence(point, rmaj, rmin, ex, neg)`

#### `_mb_torus_cutoff(point, rmaj, rmin, cutoff, neg)`

#### `_mb_torus_full(point, rmaj, rmin, cutoff, ex, neg)`

#### `mb_torus(r_maj, r_min, cutoff=INF, influence=1, negative=false, hide_debug=false, d_maj, d_min, or, od, ir, id)`

#### `_mb_octahedron_basic(point, invr, xp, neg)`

#### `_mb_octahedron_influence(point, invr, xp, ex, neg)`

#### `_mb_octahedron_cutoff(point, invr, xp, cutoff, neg)`

#### `_mb_octahedron_full(point, invr, xp, cutoff, ex, neg)`

#### `mb_octahedron(size, squareness=0.5, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `_debug_cube(size, squareness)`

/ beveled cube with squareness argument to approximate mb_cuboid() for debug view

#### `_debug_octahedron(size, squareness)`

/ beveled octahedron with squareness argument to approximate mb_octahedron for debug view

#### `debug_tetra(r)`

/ simplest and smallest possible VNF, to display for hide_debug or undefined metaballs; r=corner radius

#### `metaballs(spec, bounding_box, voxel_size, voxel_count, isovalue=1, closed=true, exact_bounds=false, show_stats=false, _debug=false)`

#### `_mb_unwind_list(list, parent_trans=[IDENT], depth=0, twoD=false)`

/ internal function: unwrap nested metaball specs in to a single list

#### `_mb_circle_full(point, r, cutoff, ex, neg)`

#### `mb_circle(r, cutoff=INF, influence=1, negative=false, hide_debug=false, d)`

#### `_mb_squircle_full(point, inv_size, xp, ex, cutoff, neg)`

#### `mb_rect(size, squareness=0.5, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `_trapsurf_full(point, path, coef, cutoff, exp, neg, maxdist)`

#### `mb_trapezoid(h, w1, w2, ang=undef, rounding=0, w, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `_mb_stadium_full(dv, hl, r, cutoff, ex, neg)`

#### `_mb_stadium_sideways_full(dv, hl, r, cutoff, ex, neg)`

#### `mb_stadium(size, cutoff=INF, influence=1, negative=false, hide_debug=false)`

#### `mb_connector2d(p1, p2, r, cutoff=INF, influence=1, negative=false, hide_debug=false, d)`

#### `_mb_ring_full(point, rmaj, rmin, cutoff, ex, neg)`

#### `mb_ring(r1, r2, cutoff=INF, influence=1, negative=false, hide_debug=false, d1, d2)`

#### `metaballs2d(spec, bounding_box, pixel_size, pixel_count, isovalue=1, closed=true, use_centers=false, smoothing=undef, exact_bounds=false, show_stats=false, _debug=false)`

#### `_metaballs2dfield(funclist, transmatrix, bbox, pixsize, nballs)`

accumulate metaball contributions using matrices rather than sums

#### `isosurface(f, isovalue, bounding_box, voxel_size, voxel_count=undef, reverse=false, closed=true, exact_bounds=false, show_stats=false, _mball=false)`

#### `_getautovoxsize(bbox, numvoxels)`

/ internal function: get voxel size given a desired number of voxels in a bounding box

#### `_getvoxsize(voxel_size, bounding_box, exactbounds)`

/ internal function: get voxel size, adjusted if necessary to fit bounding box

#### `_getbbox(voxel_size, bounding_box, exactbounds, f=undef)`

/ internal function: get bounding box, adjusted in size and centered on requested box

#### `_showstats_isosurface(voxsize, bbox, isoval, cubes, triangles, faces)`

/ Display statistics about isosurface

#### `contour(f, isovalue, bounding_box, pixel_size, pixel_count=undef, use_centers=true, smoothing=undef, closed=true, exact_bounds=false, show_stats=false, _mball=false)`

#### `_region_smooth(reg, passes, bbox, count=0)`

/ internal function: do multiple 2-point smoothing passes of all the paths in a region

#### `_is_pt_on_bbox(p, bbox)`

/ internal function: return true if a point is within _EPSILON of the bounding box edge

#### `_pathpts_on_bbox(path, bbox, i=0, count=0)`

/ internal function: return number of path points that fall on the bounding box edge

#### `_getautopixsize(bbox, numpixels)`

/ internal function: get pixel size given a desired number of pixels in a bounding box

#### `_getpixsize(pixel_size, bounding_box, exactbounds)`

/ internal function: get pixel size, adjusted if necessary to fit bounding box

#### `_getbbox2d(pixel_size, bounding_box, exactbounds, f=undef)`

/ internal function: get 2D bounding box, adjusted in size and centered on requested box

#### `_showstats_contour(pixelsize, bbox, isovalmin, isovalmax, pixels, pathlist)`

/ Display statistics about a contour region

## BOSL2/joiners.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/joiners.scad`

### Modules

#### `half_joiner_clear(l=20, w=10, ang=30, clearance=0, overlap=0.01, anchor=CENTER, spin=0, orient=UP)`

#### `half_joiner(l=20, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

#### `half_joiner2(l=20, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

#### `joiner_clear(l=40, w=10, ang=30, clearance=0, overlap=0.01, anchor=CENTER, spin=0, orient=UP)`

#### `joiner(l=40, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

#### `dovetail(gender, width, height, slide, h, w, angle, slope, thickness, taper, back_width, chamfer, extra=0.01, entry_slot_length=0, r, radius, round=false, anchor=BOTTOM, spin=0, orient)`

#### `_pin_nub(r, nub, h)`

nub extends below xy plane by distance nub/2

#### `_pin_slot(l, r, t, d, nub, depth, stretch)`

#### `_pin_shaft(r, lStraight, nub, nubscale, stretch, d, pointed)`

#### `snap_pin(size, r, radius, d, diameter, l, length, nub_depth, snap, thickness, clearance=0.2, preload, pointed=true, anchor=FRONT, spin=0, orient=FRONT, center)`

#### `snap_pin_socket(size, r, radius, l, length, d, diameter, nub_depth, snap, fixed=true, pointed=true, fins=false, anchor=BOTTOM, spin=0, orient=DOWN)`

#### `apply_lock()`

#### `hirth(n, ir, or, id, od, tooth_angle=60, cone_angle=0, chamfer, rounding, base=1, crop=false, skew=0, rot=false, orient, anchor, spin)`

### Functions

#### `half_joiner_clear(l=20, w=10, ang=30, clearance=0, overlap=0.01, anchor=CENTER, spin=0, orient=UP)`

half_joiner_clear();

#### `half_joiner(l=20, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

xcopies(20) half_joiner();

#### `half_joiner2(l=20, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

xcopies(20) half_joiner2();

#### `joiner_clear(l=40, w=10, ang=30, clearance=0, overlap=0.01, anchor=CENTER, spin=0, orient=UP)`

joiner_clear();

#### `joiner(l=40, w=10, base=10, ang=30, screwsize, anchor=CENTER, spin=0, orient=UP)`

joiner();

#### `dovetail(gender, width, height, slide, h, w, angle, slope, thickness, taper, back_width, chamfer, extra=0.01, entry_slot_length=0, r, radius, round=false, anchor=BOTTOM, spin=0, orient)`

}

#### `_pin_size(size)`

#### `snap_pin(size, r, radius, d, diameter, l, length, nub_depth, snap, thickness, clearance=0.2, preload, pointed=true, anchor=FRONT, spin=0, orient=FRONT, center)`

xcopies(spacing=10, n=4) snap_pin("standard", $fn=40);

#### `snap_pin_socket(size, r, radius, l, length, d, diameter, nub_depth, snap, fixed=true, pointed=true, fins=false, anchor=BOTTOM, spin=0, orient=DOWN)`

}

#### `valid_edge_or_corner(v)`

TOP, BOTTOM, LEFT, RIGHT, or any corner thereof

#### `valid_edge_or_corner_vector(v)`

#### `valid_double_lock()`

#### `valid_lock()`

#### `is_edge_or_corner(v, e1, e2)`

#### `relative_lock_vector_value(edge)`

#### `relative_lock_value(edge)`

## BOSL2/linalg.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/linalg.scad`

### Modules

#### `echo_matrix(M, description, sig=4, sep=1, eps=1e-9)`

### Functions

#### `is_matrix(A, m, n, square=false)`

square = If true, matrix must have height equal to width. Default: false

#### `is_matrix_symmetric(A, eps=1e-12)`

eps = epsilon for comparing equality.  Default: 1e-12

#### `is_rotation(A, dim, centered=false)`

centered = if true then require rotation to be around the origin.  Default: false

#### `echo_matrix(M, description, sig=4, sep=1, eps=1e-9)`

eps = numbers smaller than this display as zero.  Default: 1e-9

#### `column(M, i)`

e = column(data,1);   // Returns [[3,4],[9,3],[3,1]]

#### `submatrix(M, idx1, idx2)`

submatrix(A,[0,2],[1,2]);   // Returns [[17, "test"], [[3, 4], undef]]

#### `ident(n)`

//   ]

#### `diagonal_matrix(diag, offdiag=0)`

offdiag = Value to put in non-diagonal matrix cells.

#### `transpose(M, reverse=false)`

#### `outer_product(u, v)`

M = outer_product(u,v);

#### `submatrix_set(M, A, m=0, n=0)`

n = Column number of upper-left corner to place A at.  Default: 0

#### `hstack(M1, M2, M3)`

//            [ "five",  "six",  "five",  "six"]]

#### `block_matrix(M)`

//         [    3,     4,     3,     4]]

#### `linear_solve(A, b, pivot=true)`

pivot = if true use pivoting when computing the QR factorization.  Default: true

#### `linear_solve3(A, b)`

b = length 3 vector, right hand side of linear system

#### `matrix_inverse(A)`

will be faster and more accurate.

#### `rot_inverse(T)`

so it may include a translation.  This is faster and likely to be more accurate than using `matrix_inverse()`.

#### `null_space(A, eps=1e-12)`

If the null space is just the origin then returns an empty list.

#### `qr_factor(A, pivot=false)`

for rank estimation or computation of the null space, but it may be slower.

#### `_qr_factor(A, Q, P, pivot, col, m, n)`

#### `_swap_matrix(n, i, j)`

Produces an n x n matrix that swaps column i and j (when multiplied on the right)

#### `back_substitute(R, b, transpose = false)`

is singular (e.g. has a zero on the diagonal) then it returns [].

#### `_back_substitute(R, b, x=[])`

#### `cholesky(A)`

not positive definite then undef is returned.

#### `_cholesky(A, L, n)`

#### `det2(M)`

det = det2(M);  // Returns: 50

#### `det3(M)`

det = det3(M);  // Returns: -334

#### `det4(M)`

det = det4(M);  // Returns: -1773

#### `determinant(M)`

det = determinant(M);  // Returns: 2267

#### `norm_fro(A)`

This is an easily computed norm that is convenient for comparing two matrices.

#### `matrix_trace(M)`

Computes the trace of a square matrix, the sum of the entries on the diagonal.

## BOSL2/linear_bearings.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/linear_bearings.scad`

### Modules

#### `linear_bearing_housing(d=15, l=24, tab=8, gap=5, wall=3, tabwall=5, screwsize=3, anchor=BOTTOM, spin=0, orient=UP)`

linear_bearing_housing(d=19, l=29, wall=2, tab=8, screwsize=2.5);

#### `linear_bearing(l, od=15, id=8, length, anchor=CTR, spin=0, orient=UP)`

linear_bearing(l=24, od=15, id=8);

#### `lmXuu_housing(size=8, tab=7, gap=5, wall=3, tabwall=5, screwsize=3, anchor=BOTTOM, spin=0, orient=UP)`

lmXuu_housing(size=10, wall=2, tab=6, screwsize=2.5);

#### `lmXuu_bearing(size=8, anchor=CTR, spin=0, orient=UP)`

lmXuu_bearing(size=10);

### Functions

#### `lmXuu_info(size)`

size = Inner diameter of lmXuu bearing, in mm.

## BOSL2/lists.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/lists.scad`

### Functions

#### `is_homogeneous(l, depth=10)`

e = is_homogeneous([[1,["a"]], [true,["b"]]]);  // Returns true

#### `is_homogenous(l, depth=10)`

#### `_same_type(a, b, depth)`

#### `min_length(list)`

slen = min_length([[3,4,5],[6,7,8,9]]);  // Returns: 3

#### `max_length(list)`

llen = max_length([[3,4,5],[6,7,8,9]]);  // Returns: 4

#### `_list_shape_recurse(v)`

Internal.  Not exposed.

#### `_list_shape_recurse(v)`

#### `list_shape(v, depth=undef)`

d = list_shape([[[1,2,3],[4,5,6]],[[7,8,9]]]);                // Returns [2,undef,3]

#### `in_list(val, list, idx)`

with all hits, which could be slow for long lists.

#### `select(list, start, end)`

i = select(l, [3,1]);  // Returns [6,4]

#### `slice(list, start=0, end=-1)`

h = slice([3,4,5], 5, 7);           // Returns []

#### `last(list)`

x = last(l);  // Returns 9.

#### `list_head(list, to=-2)`

hlist5 = list_head(["foo", "bar", "baz"], 5);  // Returns: ["foo","bar","baz"]

#### `list_tail(list, from=1)`

tlist5 = list_tail(["foo", "bar", "baz"], 5);  // Returns: []

#### `bselect(list, index)`

a = bselect([3,4,5,6,7], [false,true,true,false,true]);  // Returns: [4,5,7]

#### `repeat(val, n, i=0)`

e = repeat(4, -1);       // Returns []

#### `list_bset(indexset, valuelist, dflt=0)`

b = list_bset([false,true,false,true,false], [3,4], dflt=1);  // Returns: [1,3,1,4,1]

#### `list(l)`

l4 = list(23);       // Returns: [23]

#### `force_list(value, n=1, fill)`

w = force_list(4, n=3, fill=1);  // Returns: [4,1,1]

#### `reverse(list)`

reverse([3,4,5,6]);  // Returns [6,5,4,3]

#### `list_rotate(list, n=1)`

l9 = list_rotate([1,2,3,4,5],6);  // Returns: [2,3,4,5,1]

#### `shuffle(list, seed)`

deck = shuffle(cards);

#### `repeat_entries(list, N, exact=true)`

c = repeat_entries(list, [1,1,2,1], exact=false);  // Returns: [0,1,2,2,3]

#### `list_pad(list, minlen, fill)`

nlist = list_pad(list,5,23);  // Returns: [3,4,5,23,23]

#### `list_set(list=[], indices, values, dflt=0, minlen=0)`

b = list_set([2,3,4,5], [1,3], [81,47]);  // Returns: [2,81,4,47]

#### `list_insert(list, indices, values)`

b = list_insert([3,6,9,12],[1,3],[5,11]);  // Returns [3,5,6,9,11,12]

#### `list_remove(list, ind)`

c = list_remove([3,6],3);           // Returns: [3,6]

#### `list_remove_values(list, values=[], all=false)`

animals4 = list_remove_values(animals, ["tucan","rat"], all=true);  // Returns: ["bat","cat","dog","bat"]

#### `idx(list, s=0, e=-1, step=1)`

for (i=idx(colors)) right(20*i) color(colors[i]) circle(d=10);

#### `pair(list, wrap=false)`

echo([for (p=pair(l)) str(p.y,p.x)]);  // Outputs: ["BA", "CB", "DC"]

#### `triplet(list, wrap=false)`

stroke(path);

#### `combinations(l, n=2, _s=0)`

for (p=combinations(regular_ngon(n=7,d=100))) stroke(p);

#### `permutations(l, n=2)`

pairs = permutations([3,4,5,6]);  // // Returns: [[3,4],[3,5],[3,6],[4,3],[4,5],[4,6],[5,3],[5,4],[5,6],[6,3],[6,4],[6,5]]

#### `list_to_matrix(v, cnt, dflt=undef)`

c = list_to_matrix(v,4,0)  // returns [[1,2,3,4], [5,6,0,0]]

#### `flatten(l)`

l = flatten([[1,2,3], [4,5,[6,7,8]]]);  // returns [1,2,3,4,5,[6,7,8]]

#### `full_flatten(l)`

l = full_flatten([[1,2,3], [4,5,[6,7,8]]]);  // returns [1,2,3,4,5,6,7,8]

#### `set_union(a, b, get_indices=false)`

// set_v now equals [[5,0,1,2,6], [2,3,5,7,11,1,8]]

#### `set_difference(a, b)`

// set_d now equals [7,11]

#### `set_intersection(a, b)`

// set_i now equals [2,3,5]

## BOSL2/masks.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/masks.scad`

### Modules

#### `mask2d_roundover(r, inset=0, mask_angle, excess=0.01, flat_top, d, h, height, cut, quarter_round=false, joint, anchor=CENTER, spin=0, clip_angle)`

mask2d_roundover(r=5, mask_angle=$edge_angle, quarter_round=true, inset=1.5, $fn=128);

#### `mask2d_smooth(mask_angle, cut, joint, height, h, k=0.5, excess=.01, inset=0, flat_top=false, splinesteps=16, anchor=CENTER, spin=0)`

#### `mask2d_teardrop(r, angle=45, mask_angle, excess=0.01, inset=0, flat_top=false, height, d, h, cut, joint, anchor=CENTER, spin=0)`

#### `mask2d_cove(r, inset=0, mask_angle, excess=0.01, flat_top, bulge, d, h, height, quarter_round=false, anchor=CENTER, spin=0)`

#### `mask2d_chamfer(edge, angle, inset=0, excess=0.01, mask_angle=90, flat_top=false, x, y, h, w, height, width, anchor=CENTER, spin=0)`

#### `mask2d_rabbet(size, mask_angle=90, excess=0.01, anchor=CTR, spin=0)`

mask2d_rabbet(size=[5,10]);

#### `mask2d_dovetail(edge, angle, shelf=0, inset=0, mask_angle=90, excess=0.01, flat_top=true, w, h, width, height, slope, anchor=CENTER, spin=0, x, y)`

mask2d_dovetail(width=10,angle=30);

#### `mask2d_ogee(pattern, excess=0.01, anchor=CENTER, spin=0)`

]);

#### `face_profile(faces=[], r, d, excess=0.01, convexity=10)`

mask2d_roundover(r=10);

#### `edge_profile(edges=EDGES_ALL, except=[], excess=0.01, convexity=10)`

#### `corner_profile(corners=CORNERS_ALL, except=[], r, d, axis="Z", convexity=10)`

}

#### `rot_to_axis(axis)`

#### `mirror_if(cond, plane)`

#### `mirror_to_corner(corner)`

#### `corner_round_mask2d(r)`

#### `chamfer_edge_mask(l, chamfer=1, excess=0.1, h, length, height, anchor=CENTER, spin=0, orient=UP)`

#### `rounding_angled_edge_mask(h, r, r1, r2, d, d1, d2, ang=90, anchor=CENTER, spin=0, orient=UP, l, height, length)`

#### `rounding_angled_corner_mask(r, ang=90, d, anchor=CENTER, spin=0, orient=UP)`

#### `teardrop_edge_mask(l, r, angle=45, excess=0.1, d, anchor=CTR, spin=0, orient=UP, h, height, length)`

#### `polygon_edge_mask(mask, length, height, l, h, scale=1, anchor="origin", atype="hull", spin=0, orient=UP)`

#### `chamfer_corner_mask(chamfer=1, anchor=CENTER, spin=0, orient=UP)`

#### `rounding_corner_mask(r, ang=90, d, style="octa", excess=0.1, anchor=CENTER, spin=0, orient=UP)`

#### `teardrop_corner_mask(r, angle=45, excess=0.1, d, anchor=CTR, spin=0, orient=UP)`

#### `chamfer_cylinder_mask(r, chamfer, d, ang=45, from_end=false, anchor=CENTER, spin=0, orient=UP)`

#### `rounding_cylinder_mask(r, rounding, d, anchor=CENTER, spin=0, orient=UP)`

#### `rounding_hole_mask(r, rounding, excess=0.1, d, anchor=CENTER, spin=0, orient=UP)`

#### `face_mask(faces=[LEFT, RIGHT, FRONT, BACK, BOT, TOP])`

zrot(45*$idx) zrot_copies([0,90]) cuboid([5,61,10]);

#### `edge_mask(edges=EDGES_ALL, except=[])`

rounding_edge_mask(l=71,r=10);

#### `corner_mask(corners=CORNERS_ALL, except=[])`

}

### Functions

#### `_inset_corner(corner, mask_angle, inset, excess, flat_top)`

#### `mask2d_roundover(r, inset=0, mask_angle=90, excess=0.01, clip_angle, flat_top, quarter_round=false, d, h, height, cut, joint, anchor=CENTER, spin=0)`

#### `mask2d_smooth(mask_angle, cut, joint, height, h, k=0.5, excess=.01, inset=0, flat_top=false, splinesteps=16, anchor=CENTER, spin=0)`

#### `mask2d_teardrop(r, angle=45, inset=[0, 0], mask_angle=90, excess=0.01, flat_top=false, d, h, height, cut, joint, anchor=CENTER, spin=0)`

#### `mask2d_cove(r, inset=0, mask_angle=90, excess=0.01, flat_top, d, h, height, bulge, quarter_round=false, anchor=CENTER, spin=0)`

#### `mask2d_chamfer(edge, angle, inset=0, excess=0.01, mask_angle=90, flat_top=false, x, y, h, w, width, height, anchor=CENTER, spin=0)`

#### `mask2d_rabbet(size, mask_angle=90, excess=0.01, anchor=CTR, spin=0)`

#### `mask2d_dovetail(edge, angle, slope, shelf=0, inset=0, mask_angle=90, excess=0.01, flat_top=true, w, width, h, height, anchor=CENTER, spin=0, x, y)`

#### `mask2d_ogee(pattern, excess=0.01, anchor=CENTER, spin=0)`

#### `_corner_orientation(pos, pvec)`

#### `_default_edge_orientation(edge)`

#### `_edge_transition_needs_flip(from, to)`

#### `_edge_corner_numbers(vec)`

#### `_gather_contiguous_edges(edge_corners)`

#### `_gather_contiguous_edges_r(edge_corners, ecns, curr, out)`

#### `_edge_transition_inversions(edge_string)`

#### `_is_closed_edge_loop(edge_string)`

#### `_edge_pair_perp_vec(e1, e2)`

#### `chamfer_edge_mask(l, chamfer=1, excess=0.1, h, length, height, anchor=CENTER, spin=0, orient=UP)`

}

#### `rounding_angled_edge_mask(h, r, r1, r2, d, d1, d2, ang=90, anchor=CENTER, spin=0, orient=UP, l, height, length)`

#### `rounding_angled_corner_mask(r, ang=90, d, anchor=CENTER, spin=0, orient=UP)`

#### `rounding_edge_mask(l, r, ang=90, r1, r2, d, d1, d2, excess=0.1, anchor=CENTER, spin=0, orient=UP, h, height, length)`

#### `make_path(r)`

#### `getarc(bigr, r, chamfer, p1, p2, h, print=false)`

#### `teardrop_edge_mask(l, r, angle=45, excess=0.1, d, anchor, spin, orient, h, height, length)`

}

#### `polygon_edge_mask(mask, length, height, l, h, scale=1, anchor="origin", atype="hull", spin=0, orient=UP)`

Tags the children with "remove" (and hence sets `$tag`) if no tag is already set.

#### `chamfer_corner_mask(chamfer=1, anchor=CENTER, spin=0, orient=UP)`

show_anchors();

#### `rounding_corner_mask(r, ang, d, style="octa", excess=0.1, anchor=CENTER, spin=0, orient=UP)`

#### `teardrop_corner_mask(r, angle=45, excess=0.1, d, anchor, spin, orient)`

}

#### `chamfer_cylinder_mask(r, chamfer, d, ang=45, from_end=false, anchor=CENTER, spin=0, orient=UP)`

tag("remove")chamfer_cylinder_mask(d=100, chamfer=10);

#### `rounding_cylinder_mask(r, rounding, d, anchor, spin, orient)`

}

#### `rounding_hole_mask(r, rounding, excess=0.1, d, anchor=CENTER, spin=0, orient=UP)`

}

## BOSL2/math.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/math.scad`

### Functions

#### `count(n, s=0, step=1, reverse=false)`

nl5 = count(5,3,reverse=true);  // Returns: [7,6,5,4,3]

#### `lerp(a, b, u)`

rainbow(pts) translate($item) circle(d=3,$fn=8);

#### `lerpn(a, b, n, endpoint=true)`

l = lerpn(0,1,5,false);   // Returns: [0, 0.2, 0.4, 0.6, 0.8]

#### `bilerp(points, x, y)`

#### `slerp(v1, v2, u)`

u = The proportion from `v1` to `v2` to calculate. Standard range is 0.0 to 1.0, inclusive. If given as a list or range of values, returns a list of results.

#### `slerpn(v1, v2, n, endpoint=true)`

%sphere(radius);

#### `sqr(x)`

sqr([[1,2],[3,4]]);  // Returns [[7,10],[15,22]]

#### `log2(x)`

log2(256);    // Returns: 8

#### `hypot(x, y, z=0)`

l = hypot(3,4,5);  // Returns: ~7.0710678119

#### `factorial(n, d=0)`

z = factorial(9);  // Returns: 362880

#### `binomial(n)`

z = binomial(6);  // Returns: [1,6,15,20,15,6,1]

#### `binomial_coefficient(n, k)`

y = binomial_coefficient(10,6); // Returns: 210

#### `gcd(a, b)`

Computes the Greatest Common Divisor/Factor of `a` and `b`.

#### `_lcm(a, b)`

Computes lcm for two integers

#### `_lcmlist(a)`

Computes lcm for a list of values

#### `lcm(a, b=[])`

as an argument.

#### `rational_approx(x, maxq, cfrac=[], p, q)`

pq4 = rational_approx(0,50);         // Returns: [0,1]

#### `_cfrac_to_pq(cfrac, p=0, q=1, ind)`

into a fraction in the form p / q, returning [p,q].

#### `sinh(x)`

Description: Takes a value `x`, and returns the hyperbolic sine of it.

#### `cosh(x)`

Description: Takes a value `x`, and returns the hyperbolic cosine of it.

#### `tanh(x)`

#### `asinh(x)`

Description: Takes a value `x`, and returns the inverse hyperbolic sine of it.

#### `acosh(x)`

Description: Takes a value `x`, and returns the inverse hyperbolic cosine of it.

#### `atanh(x)`

Description: Takes a value `x`, and returns the inverse hyperbolic tangent of it.

#### `quant(x, y)`

r = quant([[9,10,10.4],[10.5,11,12]],3);  // Returns: [[9,9,9],[12,12,12]]

#### `_roundall(data)`

#### `quantdn(x, y)`

r = quantdn([[9,10,10.4],[10.5,11,12]],3);  // Returns: [[9,9,9],[9,9,12]]

#### `_floorall(data)`

#### `quantup(x, y)`

r = quantup([[9,10,10.4],[10.5,11,12]],3);  // Returns: [[9,12,12],[12,12,12]]

#### `_ceilall(data)`

#### `constrain(v, minval, maxval)`

g = constrain([[1,2,3,4], [5,6,7], [8,9]], 3, 7);  // Returns: [[3,3,3,4], [5,6,7], [7,7]]

#### `posmod(x, m)`

g = posmod(3,2.5);     // Returns: 0.5

#### `modang(x)`

a6 = modang(700);   // Returns: -20

#### `mean_angle(angle1, angle2)`

angle2 = second angle

#### `fit_to_range(M, minval, maxval)`

#### `sum(v, dflt=0)`

sum([[1,2,3], [3,4,5], [5,6,7]]);  // returns [9, 12, 15]

#### `_sum(v, _total, _i=0)`

#### `mean(v)`

mean([[1,2,3], [3,4,5], [5,6,7]]);  // returns [3, 4, 5]

#### `median(v)`

Returns the median of the given vector.

#### `deltas(v, wrap=false)`

deltas([[1,2,3], [3,6,8], [4,8,11]]);  // returns [[2,4,5], [1,2,3]]

#### `cumsum(v)`

cumsum([[1,2,3], [3,4,5], [5,6,7]]);  // returns [[1,2,3], [4,6,8], [9,12,15]]

#### `product(list, right=true)`

product([[1,2,3], [3,4,5], [5,6,7]]);  // returns [15, 48, 105]

#### `cumprod(list, right=false)`

#### `convolve(p, q)`

d = convolve([[1,1],[2,2],[3,1]],[[1,2],[2,1]])); // Returns:  [3,9,11,7]

#### `sum_of_sines(a, sines)`

v = sum_of_sines(30, [[10,3,0], [5,5.5,60]]);

#### `rand_int(minval, maxval, n, seed=undef)`

int = rand_int(-10,10,1)[0];

#### `random_points(n, dim, scale=1, seed)`

seed = an optional seed for the random generation.

#### `gaussian_rands(n=1, mean=0, cov=1, seed=undef)`

seed = If given, sets the random number seed.

#### `exponential_rands(n=1, lambda=1, seed)`

lambda = distribution parameter.  The mean is 1/lambda.  Default: 1

#### `spherical_random_points(n=1, radius=1, seed)`

See https://mathworld.wolfram.com/SpherePointPicking.html

#### `random_polygon(n=3, size=1, seed)`

polygon(random_polygon(17, [10,20], 888));

#### `deriv(data, h=1, closed=false)`

closed = boolean to indicate if the data set should be wrapped around from the end to the start.

#### `_dnu_calc(f1, fc, f2, h1, h2)`

#### `_deriv_nonuniform(data, h, closed)`

#### `deriv2(data, h=1, closed=false)`

closed = boolean to indicate if the data set should be wrapped around from the end to the start.

#### `deriv3(data, h=1, closed=false)`

closed = boolean to indicate if the data set should be wrapped around from the end to the start.

#### `complex(list)`

by replacing all entries with a 2-vector that has zero imaginary part.

#### `c_mul(z1, z2)`

z2 = Second complex number, vector or matrix

#### `_split_complex(data)`

#### `_combine_complex(data)`

#### `_c_mul(z1, z2)`

#### `c_div(z1, z2)`

z2 = Second complex number, given as a 2D vector [REAL, IMAGINARY]

#### `c_conj(z)`

complex vector or complex matrix.

#### `c_real(z)`

Returns real part of a complex number, vector or matrix.

#### `c_imag(z)`

Returns imaginary part of a complex number, vector or matrix.

#### `c_ident(n)`

Produce an n by n complex identity matrix

#### `c_norm(z)`

Compute the norm of a complex number or vector.

#### `quadratic_roots(a, b, c, real=false)`

Algorithm from: https://people.csail.mit.edu/bkph/articles/Quadratics.pdf

#### `polynomial(p, z, k, total)`

The result is a number if `z` is a number and a complex number otherwise.

#### `poly_mult(p, q)`

computes the coefficient list of the product polynomial.

#### `poly_div(n, d)`

the returned quotient is [0].

#### `_poly_div(n, d, q)`

#### `_poly_trim(p, eps=0)`

/    or give epsilon for approximate zeros. Returns [0] for a zero polynomial.

#### `poly_add(p, q)`

Computes the sum of two polynomials.

#### `poly_roots(p, tol=1e-14, error_bound=false)`

https://www.researchgate.net/publication/225654837_Numerical_computation_of_polynomial_zeros_by_means_of_Aberth's_method

#### `_poly_roots(p, pderiv, s, z, tol, i=0)`

i=iteration counter

#### `real_roots(p, eps=undef, tol=1e-14)`

#### `root_find(f, x0, x1, tol=1e-15)`

https://www.embedded.com/worlds-best-root-finder/

#### `_rfcheck(x, y, range, tol)`

#### `_rootfind(f, xpts, ypts, yrange, tol, i=0)`

tolerance test).

## BOSL2/metric_screws.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/metric_screws.scad`

### Functions

#### `get_metric_bolt_head_size(size)`

Description: Returns the diameter of a typical metric bolt's head, based on the bolt `size`.

#### `get_metric_bolt_head_height(size)`

Description: Returns the height of a typical metric bolt's head, based on the bolt `size`.

#### `get_metric_socket_cap_diam(size)`

Description: Returns the diameter of a typical metric socket cap bolt's head, based on the bolt `size`.

#### `get_metric_socket_cap_height(size)`

Description: Returns the height of a typical metric socket cap bolt's head, based on the bolt `size`.

#### `get_metric_socket_cap_socket_size(size)`

Description: Returns the diameter of a typical metric socket cap bolt's hex drive socket, based on the bolt `size`.

#### `get_metric_socket_cap_socket_depth(size)`

Description: Returns the depth of a typical metric socket cap bolt's hex drive socket, based on the bolt `size`.

#### `get_metric_iso_coarse_thread_pitch(size)`

Description: Returns the ISO metric standard coarse threading pitch for a given bolt `size`.

#### `get_metric_iso_fine_thread_pitch(size)`

Description: Returns the ISO metric standard fine threading pitch for a given bolt `size`.

#### `get_metric_iso_superfine_thread_pitch(size)`

Description: Returns the ISO metric standard superfine threading pitch for a given bolt `size`.

#### `get_metric_jis_thread_pitch(size)`

Description: Returns the JIS metric standard threading pitch for a given bolt `size`.

#### `get_metric_nut_size(size)`

Description: Returns the typical metric nut flat-to-flat diameter for a given bolt `size`.

#### `get_metric_nut_thickness(size)`

Description: Returns the typical metric nut thickness for a given bolt `size`.

## BOSL2/miscellaneous.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/miscellaneous.scad`

### Modules

#### `extrude_from_to(pt1, pt2, convexity, twist, scale, slices)`

}

#### `path_extrude2d(path, caps=false, closed=false, s, convexity=10)`

circle(r=1.5);

#### `path_extrude(path, convexity=10, clipsize=100)`

path_extrude(path) circle(r=10, $fn=6);

#### `cylindrical_extrude(ir, or, od, id, size, convexity=10, spin=0, orient=UP)`

zrot(-10)text(text="This long text wraps around the cylinder.", size=10, halign="center", valign="center");

#### `bounding_box(excess=0, planar=false)`

shapes();

#### `_xProjection()`

a 3d (or 2d when planar=true) approx. of the children projection on X axis

#### `_oversize_bbox()`

a bounding box with an offset of 1 in all axis

#### `_shrink_cube()`

offsets a cube by `excess`

#### `chain_hull()`

}

#### `minkowski_difference(planar=false)`

}

#### `offset3d(r, size=1000, convexity=10)`

convexity = Max number of times a line could intersect the walls of the object.  Default: 10

#### `round3d(r, or, ir, size=1000)`

size = size of centered cube that contains the children.  Default: 1000

## BOSL2/modular_hose.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/modular_hose.scad`

### Modules

#### `modular_hose(size, type, clearance=0, waist_len, anchor=BOTTOM, spin=0, orient=UP)`

### Functions

#### `modular_hose(size, type, clearance=0, waist_len, anchor=BOTTOM, spin=0, orient=UP)`

attach(TOP) modular_hose(3/4, "socket", waist_len=0);

#### `modular_hose_radius(size, outer=false)`

}

## BOSL2/nema_steppers.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/nema_steppers.scad`

### Modules

#### `nema_stepper_motor(size=17, h=24, shaft_len=20, details=true, atype="body", anchor=TOP, spin=0, orient=UP)`

nema_stepper_motor(size=23, h=50, shaft_len=40, details=false);

#### `nema_mount_mask(size, depth=5, l=5, atype="full", anchor=CENTER, spin=0, orient=UP)`

nema_mount_mask(size=17, depth=5, l=0);

### Functions

#### `nema_motor_info(size)`

size = The standard NEMA motor size.

## BOSL2/nurbs.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/nurbs.scad`

### Modules

#### `debug_nurbs(control, degree, splinesteps=16, width=1, size, mult, weights, type="clamped", knots, show_weights, show_knots=false, show_index=true)`

### Functions

#### `nurbs_curve(control, degree, splinesteps, u, mult, weights, type="clamped", knots)`

#### `_nurbs_pt(knot, control, u, r, p, k)`

#### `_extend_knot_mult(mult, next, len)`

#### `_extend_knot_vector(knots, next, len)`

#### `_calc_mult(knots)`

#### `is_nurbs_patch(x)`

x = The value to check the type of.

#### `nurbs_patch_points(patch, degree, splinesteps, u, v, weights, type=["clamped", "clamped"], mult=[undef, undef], knots=[undef, undef])`

#### `nurbs_vnf(patch, degree, splinesteps=16, weights, type="clamped", mult, knots, style="default")`

vnf_polyhedron(vnf);

## BOSL2/partitions.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/partitions.scad`

### Modules

#### `half_of(v=UP, cp, s=100, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(200, center=true);

#### `maybe_offset(r)`

#### `ghost_if(cond)`

#### `left_half(s=100, x=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `right_half(s=100, x=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `front_half(s=100, y=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `back_half(s=100, y=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `bottom_half(s=100, z=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `top_half(s=100, z=0, planar=false, cut_path, cut_angle=0, offset=0, show_frameref=false, convexity=10)`

cube(300, center=true);

#### `partition_cut_mask(l=100, h=100, cutsize=10, cutpath="jigsaw", gap=0, cutpath_centered=true, convexity=10, anchor=CENTER, spin=0, orient=UP)`

partition_cut_mask(cutpath="jigsaw",h=10,$slop=0.5,$fn=12);

#### `partition(size=100, spread=10, cutsize=10, cutpath="jigsaw", gap=0, cutpath_centered=true, convexity=10, spin=0)`

### Functions

#### `half_of(p, v=UP, cp, cut_path, cut_angle=0, offset=0)`

#### `left_half(p, x=0, cut_path, cut_angle=0, offset=0)`

#### `right_half(p, x=0, cut_path, cut_angle=0, offset=0)`

#### `front_half(p, y=0, cut_path, cut_angle=0, offset=0)`

#### `back_half(p, y=0, cut_path, cut_angle=0, offset=0)`

#### `bottom_half(p, z=0, planar=false, cut_path, cut_angle=0, offset=0)`

#### `top_half(p, z=0, planar=false, cut_path, cut_angle=0, offset=0)`

#### `_partition_subpath(type)`

#### `_partition_cutpath(l, h, cutsize, cutpath, gap, cutpath_centered)`

#### `ptn_sect(type, length=25, width=25, invert=false)`

#### `partition_path(pathdesc, repeat=1, y, altpath)`

#### `_ptn_path_redirect(major_path, minor_path, center=true)`

## BOSL2/paths.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/paths.scad`

### Functions

#### `is_path(list, dim=[2, 3], fast=false)`

fast = set to true for fast check that looks at only the first entry.  Default: false

#### `is_1region(path, name="path")`

name = name of parameter to use in error message.  Default: "path"

#### `force_path(path, name="path")`

name = name of parameter to use in error message.  Default: "path"

#### `_path_select(path, s1, u1, s2, u2, closed=false)`

/   closed = If true, treat path as a closed polygon.

#### `path_merge_collinear(path, closed, eps=_EPSILON)`

eps = Largest positional variance allowed.  Default: 1e-9

#### `path_merge_collinear_indexed(path, indices, closed, eps=_EPSILON)`

eps = Largest positional variance allowed.  Default: 1e-9

#### `path_length(path, closed)`

echo(path_length(path));

#### `path_segment_lengths(path, closed)`

closed = true if the path is closed.  Default: false

#### `path_length_fractions(path, closed)`

closed = set to true if path is closed.  Default: false

#### `_path_self_intersections(path, closed=true, eps=_EPSILON)`

/   for (isect=isects) translate(isect[0]) color("blue") sphere(d=10);

#### `_sum_preserving_round(data, index=0)`

This generally distributes the error in a uniform manner.

#### `subdivide_path(path, n, refine, maxlen, closed=true, exact, method)`

move_copies(mypath)sphere(r=.1,$fn=32);

#### `resample_path(path, n, spacing, keep_corners, closed=true)`

#### `simplify_path(path, maxerr, closed=false)`

#### `_err_resample(path, maxerr, n, i1=0, i2=2, resultidx=[0], iter=0)`

/ return a resampled path based on error deviation, retaining path endpoints (i.e. assume path is not closed)

#### `is_path_simple(path, closed, eps=_EPSILON)`

eps = Epsilon error value used for determine if points coincide.  Default: 1e-9

#### `path_closest_point(path, pt, closed=true)`

color("red") translate(closest[1]) circle(d=3, $fn=12);

#### `path_tangents(path, closed, uniform=true)`

stroke([rect[i]-tangents[i], rect[i]+tangents[i]],width=.25, endcap2="arrow2");

#### `path_normals(path, tangents, closed)`

closed = if true path is treated as a polygon.  Default: false

#### `path_curvature(path, closed)`

closed = if true then treat the path as a polygon.  Default: false

#### `path_torsion(path, closed=false)`

closed = if true then treat path as a polygon.  Default: false

#### `surface_normals(surf, col_wrap=false, row_wrap=false)`

#### `path_cut(path, cutdist, closed)`

rainbow(segs) stroke($item, endcaps="butt", width=3);

#### `_path_cut_getpaths(path, cutlist, closed)`

#### `path_cut_points(path, cutdist, closed=false, direction=false)`

path_cut_points(square, [0,0.8,1.6,2.4,3.2]);               // Returns [[[0, 0], 1], [[0.8, 0], 1], [[1, 0.6], 2], [[0.6, 1], 3], undef]

#### `path_cut_points_recurse(path, dists, closed=false, pind=0, dtotal=0, dind=0, result=[])`

Main recursive path cut function

#### `_path_cut_single(path, dist, closed=false, ind=0, eps=1e-7)`

Search for a single cut point in the path

#### `_path_cuts_normals(path, cuts, dirs, closed=false)`

Or return a vector parallel to the x-y plane if the above fails

#### `_path_plane(path, ind, i, closed)`

to define the plane of the path.

#### `_path_cuts_dir(path, cuts, closed=false, eps=1e-2)`

Find the direction of the path at the cut points

#### `_cut_to_seg_u_form(pathcut, path, closed)`

form list that works withi path_select

#### `split_path_at_self_crossings(path, closed=true, eps=_EPSILON)`

rainbow(paths) stroke($item, closed=false, width=3);

#### `_tag_self_crossing_subpaths(path, nonzero, closed=true, eps=_EPSILON)`

#### `polygon_parts(poly, nonzero=false, eps=_EPSILON)`

move([16,-14])rainbow(polygon_parts(poly,nonzero=true)) polygon($item);

#### `_extreme_angle_fragment(seg, fragments, rightmost=true, eps=_EPSILON)`

#### `_assemble_a_path_from_fragments(fragments, rightmost=true, startfrag=0, eps=_EPSILON)`

/   eps = The epsilon error value to determine whether two points coincide.  Default: 1e-9

#### `_assemble_path_fragments(fragments, eps=_EPSILON, _finished=[])`

/   eps = The epsilon error value to determine whether two points coincide.  Default: 1e-9

#### `_assemble_partial_paths(paths, closed=false, eps=1e-7)`

#### `_assemble_partial_paths_recur(edges, eps, paths=[], i=0)`

## BOSL2/polyhedra.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/polyhedra.scad`

### Functions

#### `_unique_groups(m)`

#### `_even_perms(v)`

#### `_all_perms(v)`

#### `_point_ref(points, sign="both")`

#### `_stellate_faces(scalefactor, stellate, vertices, faces_normals)`

#### `_trapezohedron(faces, r, side, longside, h, height, d)`

#### `_facenormal(pts, face)`

#### `_full_faces(pts, faces)`

## BOSL2/regions.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/regions.scad`

### Modules

#### `region(r, anchor="origin", spin=0, cp="centroid", atype="hull")`

region(rgn);

#### `debug_region(region, vertices=true, edges=true, convexity=2, size=1)`

debug_region(region,size=1);

#### `exclusive_or()`

#### `hull_region(region)`

### Functions

#### `is_region(x)`

that the argument is a list whose first entry is a path.

#### `is_valid_region(region, eps=_EPSILON)`

move([-5,11.4])text(is_valid_region(region) ? "region" : "non-region", size=3);

#### `_polygon_crosses_region(region, poly, eps=_EPSILON)`

polygon is inside the region and part is outside.

#### `is_region_simple(region, eps=_EPSILON)`

move([1,13])text(is_region_simple(region) ? "simple" : "not-simple", size=2);

#### `make_region(polys, nonzero=false, eps=_EPSILON)`

#### `force_region(poly)`

poly = polygon to turn into a region

#### `point_in_region(point, region, eps=_EPSILON)`

move([x,y]) color("#ddf") circle(0.1, $fn=12);

#### `_point_in_region(point, region, eps=_EPSILON, i=0, cnt=0)`

#### `region_area(region)`

area = region_area([square(10), right(20,square(8))]);  // Returns 164

#### `_clockwise_region(r)`

#### `are_regions_equal(region1, region2, either_winding=false)`

either_winding = if true then two shapes test equal if they wind in opposite directions.  Default: false

#### `__are_regions_equal(region1, region2, i)`

#### `_region_region_intersections(region1, region2, closed1=true, closed2=true, eps=_EPSILON)`

/    Self crossings of the paths in the regions are not returned.)

#### `split_region_at_region_crossings(region1, region2, closed1=true, closed2=true, eps=_EPSILON)`

}

#### `region_parts(region)`

rainbow(region_list) region($item);

#### `_offset_chamfer(center, points, delta)`

#### `_shift_segment(segment, d)`

#### `_segment_extension(s1, s2)`

which can happen if two colinear segments are input to the path variant of `offset()`

#### `_makefaces(direction, startind, good, pointcount, closed)`

#### `_makefaces_recurse(startind1, startind2, numfirst, numsecond, lenlist, closed, firstind=0, secondind=0, faces=[])`

#### `_good_segments(path, d, shiftsegs, closed, quality)`

Determine which of the shifted segments are good

#### `_segment_good(path, pathseg_unit, pathseg_len, d, seg, alpha, index=0)`

makes the test more accurate, but slower.

#### `_point_dist(path, pathseg_unit, pathseg_len, pt)`

account that the minimal distance may be anywhere along a path segment, not just at the ends.

#### `_filter_region_parts(region1, region2, keep, eps=_EPSILON)`

/ You specify which type of subpaths to keep with a string of the desired types such as "OS".

#### `_list_three(a, b, c)`

#### `union(regions=[], b=undef, c=undef, eps=_EPSILON)`

stroke(shape, width=0.5, closed=true, color="red");

#### `difference(regions=[], b=undef, c=undef, eps=_EPSILON)`

color("green") region(difference(shape1,shape2));

#### `intersection(regions=[], b=undef, c=undef, eps=_EPSILON)`

color("green") region(intersection(shape1,shape2));

#### `exclusive_or(regions=[], b=undef, c=undef, eps=_EPSILON)`

}

#### `hull_region(region)`

stroke([hull_region(data)],color="red");

#### `fill(region)`

## BOSL2/rounding.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/rounding.scad`

### Modules

#### `round_corners(path, method="circle", radius, r, cut, joint, width, k, closed=true, verbose=false)`

polygon(rpath2);

#### `smooth_path(path, tangents, size, relsize, method="edges", splinesteps=10, uniform, closed=false)`

color("red")move_copies(pts)circle(r=.15,$fn=12);

#### `path_join(paths, joint=0, k=0.5, relocate=true, closed=false)`

closed=true,width=.5);

#### `bent_cutout_mask(r, thickness, path, radius, convexity=10)`

### Functions

#### `round_corners(path, method="circle", radius, r, cut, joint, width, k, closed=true, verbose=false)`

#### `_smooth_bez_fill(points, k)`

up to 1 for a sharp transition that doesn't have continuous curvature any more

#### `_bezcorner(points, parm)`

#### `_chamfcorner(points, parm)`

#### `_circlecorner(points, parm)`

#### `_rounding_offsets(edgespec, z_dir=1)`

z_dir is the direction multiplier (1 to build up, -1 to build down)

#### `smooth_path(path, tangents, size, relsize, method="edges", splinesteps=10, uniform, closed)`

#### `_scalar_to_vector(value, length, varname)`

#### `path_join(paths, joint=0, k=0.5, relocate=true, closed=false)`

#### `_path_join(paths, joint, k=0.5, i=0, result=[], relocate=true, closed=false)`

#### `os_pointed(dist, loc=0)`

#### `os_round(cut, angle, abs_angle, k, r)`

#### `os_flat(angle, abs_angle)`

#### `angle_between_lines(line1, line2)`

Return angle in (-90,90] required to map line1 onto line2 (lines specified as lists of two points)

#### `_parse_stroke_end(spec, name)`

#### `_stroke_end(width, left, right, spec)`

#### `_path_line_intersection(path, line, ind=0)`

returns [intersection_pt, index of first point in path after the intersection]

#### `_struct_valid(spec, func, name)`

#### `os_circle(r, cut, h, height, clip_angle, extra, check_valid, quality, steps, offset)`

#### `os_teardrop(r, cut, extra, check_valid, quality, steps, offset)`

#### `os_chamfer(height, width, cut, angle, extra, check_valid, quality, steps, offset)`

#### `os_smooth(cut, joint, k, extra, check_valid, quality, steps, offset)`

#### `os_profile(points, extra, check_valid, quality, offset)`

#### `os_mask(mask, out=false, extra, check_valid, quality, offset)`

#### `_remove_undefined_vals(list)`

#### `_rp_compute_patches(top, bot, rtop, rsides, ktop, ksides, concave)`

#### `_cyl_hole(r, path)`

Converts a 2d path to a path on a cylinder at radius r

#### `_circle_mask(r)`

Mask profile of 180 deg of a circle to round an edge

#### `bent_cutout_mask(r, thickness, path, radius, convexity=10)`

}

#### `_fix_angle_list(list, ind=0, result=[])`

#### `_cyl_line_intersection(R, line, ref)`

if ref is given, return point with larger inner product with ref.

#### `_sphere_line_isect_best(R, line, ref)`

#### `_prism_line_isect(poly_pairs, line, ref)`

point, ind ind and u are the segment index and u value.  Prism is z-aligned.

#### `_prism_fillet(name, base, R, bot, top, d, k, N, overlap, uniform, smooth_normals, debug)`

#### `_prism_fillet_plane(name, bot, top, d, k, N, overlap, debug)`

#### `_prism_fillet_cyl(name, R, bot, top, d, k, N, overlap, uniform, debug)`

output is un-rotated.

#### `_prism_fillet_sphere(name, R, bot, top, d, k, N, overlap, uniform, debug)`

#### `_getnormal(polygon, index, u, smooth_normals)`

#### `_polygon_step(poly, ind, u, dir, length)`

Returns [ point, ind, u] where point is the actual point desired.

#### `_prism_fillet_prism(name, basepoly, bot, top, d, k, N, overlap, uniform, smooth_normals, inside, debug)`

Needs check for zero overlap case and zero joint case

#### `_get_obj_type(ind, geom, anchor, prof, edge_r, edge_joint, edge_k)`

Note that profile is needed just to find its dimensions for making a big enough edge profile

#### `_check_join_shift(ind, type, shift, flip)`

#### `_is_geom_an_edge(geom, anchor)`

#### `_prismoid_isect(geom, line, bounded, flip=false)`

#### `_cone_isect(geom, line, bounded, flip)`

then the sides of a right angle cylinder only.

#### `_extrusion_isect(geom, line, bounded, flip)`

#### `_find_center_anchor(desc1, desc2, anchor2, flip)`

## BOSL2/screw_drive.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/screw_drive.scad`

### Modules

#### `phillips_mask(size="#2", $fn=36, anchor=BOTTOM, spin=0, orient=UP)`

#### `hex_drive_mask(size, length, l, h, height, anchor, spin, orient)`

#### `torx_mask(size, l=5, center, anchor, spin=0, orient=UP)`

torx_mask(size=30, l=10, $fa=1, $fs=1);

#### `torx_mask2d(size, anchor=CENTER, spin)`

torx_mask2d(size=30, $fa=1, $fs=1);

#### `robertson_mask(size, extra=1, ang=2.5, anchor=TOP, spin, orient)`

}

### Functions

#### `_phillips_shaft(x)`

#### `_ph_bot_angle()`

#### `_ph_side_angle()`

#### `phillips_depth(size, d)`

d = desired diameter

#### `phillips_diam(size, depth)`

depth = depth of recess to find the diameter of

#### `hex_drive_mask(size, length, l, h, height, anchor, spin, orient)`

#### `torx_info(size)`

size = Torx size.

#### `torx_diam(size)`

size = Torx size.

#### `torx_depth(size)`

size = Torx size.

## BOSL2/screws.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/screws.scad`

### Modules

#### `_driver(spec)`

#### `screw_head(screw_info, details=false, counterbore=0, flat_height, teardrop=false, slop=0)`

#### `nut_trap_side(trap_width, spec, shape, thickness, nutwidth, anchor=BOT, orient, spin, poke_len=0, poke_diam)`

screw_hole(length=20,anchor=BOT);

#### `nut_trap_inline(length, spec, shape, l, height, h, nutwidth, anchor, orient, spin)`

}

### Functions

#### `_struct_reset(s, keyval, grow=true)`

#### `_nominal_diam(spec)`

#### `_ISO_thread_tolerance(diameter, pitch, internal=false, tolerance=undef)`

#### `_UTS_thread_tolerance(diam, pitch, internal=false, tolerance=undef)`

#### `_exact_thread_tolerance(d, P)`

#### `_parse_screw_name(name)`

#### `_parse_drive(drive=undef, drive_size=undef)`

or you can specify "ph0" up to "ph4" for phillips and "t20" for torx 20

#### `screw_head(screw_info, details=false, counterbore=0, flat_height, teardrop=false, slop=0)`

slop = enlarge diameter by this extra amount (beyond that specified in the screw specification).  Default: 0

#### `screw_info(name, head, drive, thread, drive_size, shaft_oversize, head_oversize, _origin)`

#### `nut_info(name, shape, thickness, thread, hole_oversize=0, width, _origin)`

#### `_nut_info_english(diam, threadcount, thread, shape, thickness, width)`

Nut data is from ASME B18.2.2, mostly Table A-1

#### `_downcase_if_str(s)`

#### `_nut_info_metric(diam, pitch, thread, shape, thickness, width)`

#### `_screw_info_english(diam, threadcount, head, thread, drive)`

#### `_screw_info_metric(diam, pitch, head, thread, drive)`

#### `_is_positive(x)`

#### `_validate_nut_spec(spec)`

#### `_validate_screw_spec(spec)`

#### `thread_specification(screw_spec, tolerance=undef, internal=false)`

internal = true for internal threads.  Default: false

## BOSL2/shapes2d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/shapes2d.scad`

### Modules

#### `square(size=1, center, anchor, spin)`

#### `rect(size=1, rounding=0, atype="box", chamfer=0, anchor=CENTER, spin=0, corner_flip = false)`

move_copies(path) color("blue") circle(d=2,$fn=8);

#### `circle(r, d, points, corner, anchor=CENTER, spin=0)`

#### `ellipse(r, d, realign=false, circum=false, uniform=false, anchor=CENTER, spin=0)`

}

#### `regular_ngon(n=6, r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

#### `pentagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

#### `hexagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

#### `octagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

#### `right_triangle(size=[1, 1], center, anchor, spin=0)`

#### `trapezoid(h, w1, w2, ang, shift, chamfer=0, rounding=0, flip=false, anchor=CENTER, spin=0, atype="box", angle)`

#### `star(n, r, ir, d, or, od, id, step, realign=false, align_tip, align_pit, anchor=CENTER, spin=0, atype="hull")`

#### `jittered_poly(path, dist=1/512)`

jittered_poly(spath);

#### `teardrop2d(r, ang=45, cap_h, d, circum=false, realign=false, bot_corner=0, anchor=CENTER, spin=0)`

#### `egg(length, r1, r2, R, d1, d2, D, anchor=CENTER, spin=0)`

#### `ring(n, ring_width, r, r1, r2, angle, d, d1, d2, cp, points, corner, width, thickness, start, long=false, full=true, cw=false, ccw=false, anchor=CENTER, spin=0)`

#### `glued_circles(r, spread, tangent, r1, r2, d, d1, d2, bulge, blendR, blendD, width, anchor=CENTER, spin=0)`

#### `squircle(size, squareness=0.5, style="fg", anchor=CENTER, spin=0, atype="box")`

#### `keyhole(l, r1, r2, shoulder_r=0, d1, d2, length, anchor=CTR, spin=0)`

#### `reuleaux_polygon(n=3, r, d, anchor=CENTER, spin=0)`

reuleaux_polygon(n=3, d=50) show_anchors(std=false);

#### `supershape(step=0.5, n, m1=4, m2=undef, n1, n2=undef, n3=undef, a=1, b=undef, r=undef, d=undef, anchor=CENTER, spin=0, atype="hull")`

#### `text(text, size=10, font, halign, valign, spacing=1.0, direction="ltr", language="en", script="latin", anchor="baseline", spin=0)`

text(select(txt,-1-$idx), size=10, anchor=str("baseline",CENTER), spin=-90);

#### `round2d(r, or, ir)`

round2d(or=16,ir=8) {square([40,100], center=true); square([100,40], center=true);}

#### `shell2d(thickness, or=0, ir=0)`

shell2d(8,or=[16,8],ir=[16,8]) {square([40,100], center=true); square([100,40], center=true);}

### Functions

#### `square(size=1, center, anchor, spin=0)`

move_copies(path) color("blue") circle(d=2,$fn=8);

#### `rect(size=1, rounding=0, chamfer=0, atype="box", anchor=CENTER, spin=0, _return_override, corner_flip = false)`

#### `circle(r, d, points, corner, anchor=CENTER, spin=0)`

stroke(path,closed=true);

#### `_ellipse_refine(a, b, N, _theta=[])`

in an ellipse whose side lengths are all equal

#### `_ellipse_refine_realign(a, b, N, _theta=[], i=0)`

#### `ellipse(r, d, realign=false, circum=false, uniform=false, anchor=CENTER, spin=0)`

#### `regular_ngon(n=6, r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0, _mat, _anchs)`

stroke(closed=true, regular_ngon(n=6, or=30));

#### `pentagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

stroke(closed=true, pentagon(or=30));

#### `hexagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

stroke(closed=true, hexagon(or=30));

#### `octagon(r, d, or, od, ir, id, side, rounding=0, realign=false, align_tip, align_side, anchor=CENTER, spin=0)`

stroke(closed=true, octagon(or=30));

#### `right_triangle(size=[1, 1], center, anchor, spin=0)`

show_anchors(std=false);

#### `_trapezoid_dims(h, w1, w2, shift, ang)`

#### `trapezoid(h, w1, w2, ang, shift, chamfer=0, rounding=0, flip=false, anchor=CENTER, spin=0, atype="box", _return_override, angle)`

#### `star(n, r, ir, d, or, od, id, step, realign=false, align_tip, align_pit, anchor=CENTER, spin=0, atype="hull", _mat, _anchs)`

stroke(closed=true, star(n=5, r=50, ir=25));

#### `_path_add_jitter(path, dist=1/512, closed=true)`

/      polygon(jpath);

#### `teardrop2d(r, ang=45, cap_h, d, circum=false, realign=false, anchor=CENTER, spin=0, bot_corner=0, _extrapt=false)`

#### `egg(length, r1, r2, R, d1, d2, D, anchor=CENTER, spin=0)`

color("black") text(str("r2=",r2), size=8, halign="center", valign="center");

#### `ring(n, ring_width, r, r1, r2, angle, d, d1, d2, cp, points, corner, width, thickness, start, long=false, full=true, cw=false, ccw=false)`

#### `glued_circles(r, spread, tangent, r1, r2, d, d1, d2, bulge, blendR, blendD, width, anchor=CENTER, spin=0)`

#### `_gs_waist_R(r1, r2, s, waist)`

#### `gs_get_tangent_R(r1, r2, s, ang)`

#### `_gs_indent_R(r1, r2, s, h)`

#### `squircle(size, squareness=0.5, style="fg", anchor=CENTER, spin=0, atype="box")`

#### `_squircle_fg(size, squareness)`

#### `squircle_radius_fg(squareness, r, angle)`

#### `_linearize_squareness(s)`

#### `_squircle_se(size, squareness)`

#### `squircle_radius_se(n, r, angle)`

#### `_squircle_se_exponent(squareness)`

#### `_squircle_bz(size, squareness)`

#### `keyhole(l, r1, r2, shoulder_r=0, d1, d2, length, anchor=CTR, spin=0)`

#### `reuleaux_polygon(n=3, r, d, anchor=CENTER, spin=0)`

#### `supershape(step=0.5, n, m1=4, m2, n1=1, n2, n3, a=1, b, r, d, anchor=CENTER, spin=0, atype="hull")`

linear_extrude(height=5, scale=0) supershape(step=1, b=3, m1=6, n1=3.8, n2=16, n3=10);

#### `_superformula(theta, m1, m2, n1, n2=1, n3=1, a=1, b=1)`

## BOSL2/shapes3d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/shapes3d.scad`

### Modules

#### `cube(size=1, center, anchor, spin=0, orient=UP)`

#### `trunc_cube(s, corner)`

#### `xtcyl(l, r)`

#### `ytcyl(l, r)`

#### `tsphere(r)`

#### `corner_shape(corner)`

#### `wedge(size=[1, 1, 1], center, anchor, spin=0, orient=UP)`

#### `octahedron(size=1, anchor=CENTER, spin=0, orient=UP)`

#### `cylinder(h, r1, r2, center, r, d, d1, d2, anchor, spin=0, orient=UP)`

#### `sphere(r, d, anchor=CENTER, spin=0, orient=UP)`

#### `spheroid(r, style="aligned", d, circum=false, dual=false, anchor=CENTER, spin=0, orient=UP)`

#### `onion(r, ang=45, cap_h, d, circum=false, realign=false, anchor=CENTER, spin=0, orient=UP)`

#### `interior_fillet(l=1.0, r, ang=90, overlap=0.01, d, length, h, height, anchor=CENTER, spin=0, orient=UP)`

#### `plot3d(f, x, y, zclip, zspan, base=1, anchor="origin", orient=UP, spin=0, atype="hull", cp="box", convexity=4, style="default")`

#### `heightfield(data, size=[100, 100], bottom=-20, maxz=100, xrange=[-1:0.04:1], yrange=[-1:0.04:1], style="default", convexity=10, anchor=CENTER, spin=0, orient=UP)`

### Functions

#### `cube(size=1, center, anchor, spin=0, orient=UP)`

#### `_rect_tube_rounding(factor, ir, r, alternative, size, isize)`

#### `wedge(size=[1, 1, 1], center, anchor, spin=0, orient=UP)`

#### `octahedron(size=1, anchor=CENTER, spin=0, orient=UP)`

#### `cylinder(h, r1, r2, center, r, d, d1, d2, anchor, spin=0, orient=UP)`

#### `_teardrop_corner(r, corner, ang=45)`

#### `_clipped_corner(r, corner, ang=45)`

#### `sphere(r, d, anchor=CENTER, spin=0, orient=UP)`

#### `_subsample_triangle(p, N)`

to add, so output triangle has N+2 points on each side.

#### `_dual_vertices(vnf)`

Input should have only triangular faces

#### `_vector_planes_intersection(A, B, C, D)`

#### `_make_octa_sphere(r)`

#### `spheroid(r, style="aligned", d, circum=false, anchor=CENTER, spin=0, orient=UP)`

#### `onion(r, ang=45, cap_h, d, anchor=CENTER, spin=0, orient=UP)`

#### `_cut_interp(pathcut, path, data)`

This could be replaced with _cut_to_seg_u_form

#### `fillet(l, r, ang, r1, r2, d, d1, d2, excess=0.1, anchor=CENTER, spin=0, orient=UP, h, height, length)`

#### `plot3d(f, x, y, zclip, zspan, base=1, anchor="origin", orient=UP, spin=0, atype="hull", cp="box", style="default")`

#### `heightfield(data, size=[100, 100], bottom=-20, maxz=100, xrange=[-1:0.04:1], yrange=[-1:0.04:1], style="default", anchor=CENTER, spin=0, orient=UP)`

## BOSL2/skin.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/skin.scad`

### Modules

#### `sweep_attach(parent, child, frac, idx, pathlen, spin=0, overlap=0, atype="hull", cp="centroid")`

### Functions

#### `_make_all_prism_anchors(bot, top, startind=0)`

#### `_force_xplus(data)`

#### `_ss_polygon_r(N, theta)`

#### `_ofs_vmap(ofs, closed=false)`

#### `_ofs_face_edge(face, firstlen, second=false)`

the index into each curve with a 0 base.

#### `_force_int(x)`

#### `_find_ps_dir(frac, prevind, nextind, twist, anchor_pos, anchor_dir)`

#### `subdivide_and_slice(profiles, slices, numpoints, method="length", closed=false)`

closed = the first and last profile are connected.  Default: false

#### `slice_profiles(profiles, slices, closed=false)`

closed = set to true if last profile connects to first one.  Default: false

#### `_closest_angle(alpha, beta)`

#### `_smooth(data, len, closed=false, angle=false)`

If closed=false pads data with left/right value (probably wrong behavior...should do linear interp)

#### `rot_resample(rotlist, n, twist, scale, smoothlen=1, long=false, turns=0, closed=false, method="length")`

skin(belt,slices=0,closed=true);

#### `_dp_distance_array(small, big, abort_thresh=1/0, small_ind=0, tdist=[], map=[])`

#### `_dp_distance_array(small, big, abort_thresh=1/0)`

#### `_dp_distance_row(small, big, small_ind, tdist)`

#### `_dp_extract_map(map)`

#### `_skin_distance_match(poly1, poly2)`

/   poly2 = second polygon to match

#### `_skin_aligned_distance_match(poly1, poly2)`

#### `_skin_tangent_match(poly1, poly2)`

/   poly2 = input polygon

#### `_find_one_tangent(curve, edge, curve_offset=[0, 0, 0], closed=true)`

#### `associate_vertices(polygons, split, curpoly=0)`

skin(concat(grow, reverse(shrink)), slices=10, refine=10, method="distance", z=[0,2,2,4]);

#### `_tex_fn_default()`

#### `texture(tex, n, border, gap, roughness, inset)`

#### `_get_vnf_tile_edges(texture)`

#### `_validate_texture(texture)`

#### `_tex_height(scale, inset, z)`

#### `_get_texture(texture, tex_rot)`

#### `_tile_edge_path_list(vnf, axis, maxopen=1)`

#### `_resample_point_array(data, size, col_wrap=false, row_wrap=false)`

## BOSL2/sliders.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/sliders.scad`

### Modules

#### `slider(l=30, w=10, h=10, base=10, wall=5, ang=30, chamfer=2, anchor=BOTTOM, spin=0, orient=UP)`

#### `rail(l=30, w=10, h=10, chamfer=1.0, ang=30, anchor=BOTTOM, spin=0, orient=UP)`

### Functions

#### `slider(l=30, w=10, h=10, base=10, wall=5, ang=30, chamfer=2, anchor=BOTTOM, spin=0, orient=UP)`

slider(l=30, base=10, wall=4) show_anchors();

#### `rail(l=30, w=10, h=10, chamfer=1.0, ang=30, anchor=BOTTOM, spin=0, orient=UP)`

rail(l=100, w=10, h=10) show_anchors();

## BOSL2/strings.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/strings.scad`

### Functions

#### `_is_liststr(s)`

#### `substr(str, pos=0, len=undef)`

s5=substr("abcdefg",len=-2);  // Returns ""

#### `_substr(str, pos, len)`

#### `suffix(str, len)`

len = The number of characters of suffix to get.

#### `str_find(str, pattern, start=undef, last=false, all=false)`

n=str_find("abc","",all=true);                  // Returns [0,1,2]

#### `_str_find_first(str, pattern, max_sindex, sindex)`

#### `_str_find_last(str, pattern, sindex)`

#### `_str_find_all(str, pattern)`

#### `substr_match(str, start, pattern)`

comparison methods were slower.

#### `_substr_match_recurse(str, sindex, pattern, plen, pindex=0)`

#### `starts_with(str, pattern)`

b3=starts_with("abcdef","");     // Returns true

#### `ends_with(str, pattern)`

b3=ends_with("abcdef","");     // Returns true

#### `str_split(str, sep, keep_nulls=true)`

s6=str_split("abc+def-qrs*iop",["-","+","*"]);     // Returns ["abc+def", "qrs*iop", "", ""]

#### `_str_split_recurse(str, sep, i, result)`

#### `_remove_empty_strs(list)`

#### `str_join(list, sep="", _i=0, _result="")`

s2=str_join(["abc","def","ghi"], " + ");  // Returns "abc + def + ghi"

#### `_str_count_leading(s, c, _i=0)`

#### `_str_count_trailing(s, c, _i=0)`

#### `str_strip(s, c, start, end)`

#### `str_pad(str, length, char=" ", left=false)`

#### `str_replace_char(str, char, replace)`

#### `downcase(str)`

s=downcase("ABCdef");   // Returns "abcdef"

#### `upcase(str)`

s=upcase("ABCdef");   // Returns "ABCDEF"

#### `rand_str(n, charset, seed)`

seed = random number seed

#### `parse_int(str, base=10)`

parse_int("");           // Returns 0

#### `_parse_int_recurse(str, base, i)`

#### `parse_float(str)`

parse_float("");         // Returns 0

#### `parse_frac(str, mixed=true, improper=true, signed=true)`

parse_frac("2 1/4",mixed=false);      // Returns nan

#### `parse_num(str)`

parse_num("3.4e-2"); // Returns 0.034

#### `format_int(i, mindigits=1)`

format_int(12,3);             // Returns 012

#### `format_fixed(f, digits=6)`

digits = The number of digits after the decimal to show.  Default: 6

#### `format_float(f, sig=12)`

format_float([PI,-16.75],12);  // Returns: "[3.14159265359, -16.75]"

#### `_format_matrix(M, sig=4, sep=1, eps=1e-9)`

/   eps = values smaller than this are shown as zero.  Default: 1e-9

#### `format(fmt, vals)`

format("{:-10.9s}{:.3f}", ["plecostamus",27.43982]);  // Returns: "plecostam 27.440"

#### `is_lower(s)`

Returns true if all the characters in the given string are lowercase letters. (a-z)

#### `is_upper(s)`

Returns true if all the characters in the given string are uppercase letters. (A-Z)

#### `is_digit(s)`

Returns true if all the characters in the given string are digits. (0-9)

#### `is_hexdigit(s)`

Returns true if all the characters in the given string are valid hexadecimal digits. (0-9 or a-f or A-F))

#### `is_letter(s)`

Returns true if all the characters in the given string are standard ASCII letters. (A-Z or a-z)

## BOSL2/structs.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/structs.scad`

### Modules

#### `echo_struct(struct, name="")`

### Functions

#### `struct_set(struct, key, value, grow=true)`

// quote: What a nice day

#### `_format_key(key)`

#### `struct_remove(struct, key)`

key = a single key or list of keys to remove.

#### `struct_val(struct, key, default=undef)`

default = default value to return if key is not present.  Default: undef

#### `struct_keys(struct)`

struct = input structure

#### `echo_struct(struct, name="")`

name = optional structure name to list at the top of the output.  Default: ""

#### `is_struct(x)`

Returns true if the input is a list of pairs, false otherwise.

## BOSL2/tests/test_affine.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_affine.scad`

### Modules

#### `test_affine2d_identity()`

#### `test_affine2d_translate()`

#### `test_affine2d_scale()`

#### `test_affine2d_mirror()`

#### `test_affine2d_zrot()`

#### `test_affine2d_skew()`

#### `test_affine3d_identity()`

#### `test_affine3d_translate()`

#### `test_affine3d_scale()`

#### `test_affine3d_mirror()`

#### `test_affine3d_xrot()`

#### `test_affine3d_yrot()`

#### `test_affine3d_zrot()`

#### `test_affine3d_rot_by_axis()`

#### `test_affine3d_rot_from_to()`

#### `test_affine3d_skew()`

#### `test_affine3d_skew_xy()`

#### `test_affine3d_skew_xz()`

#### `test_affine3d_skew_yz()`

## BOSL2/tests/test_attachments.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_attachments.scad`

### Modules

#### `test__standard_anchors()`

## BOSL2/tests/test_comparisons.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_comparisons.scad`

### Modules

#### `test_sort()`

#### `test_sortidx()`

#### `test_group_sort()`

#### `test_unique()`

#### `test_unique_count()`

#### `test_list_wrap()`

#### `test_list_unwrap()`

#### `test_is_increasing()`

#### `test_is_decreasing()`

#### `test_are_ends_equal()`

#### `test_find_approx()`

#### `test_deduplicate()`

#### `test_deduplicate_indexed()`

#### `test_all_zero()`

#### `test_all_equal()`

#### `test_all_nonzero()`

#### `test_all_positive()`

#### `test_all_negative()`

#### `test_all_nonpositive()`

#### `test_all_nonnegative()`

#### `test_approx()`

#### `test_group_data()`

#### `test_compare_vals()`

#### `test_compare_lists()`

#### `test_min_index()`

#### `test_max_index()`

## BOSL2/tests/test_coords.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_coords.scad`

### Modules

#### `test_point2d()`

#### `test_path2d()`

#### `test_point3d()`

#### `test_path3d()`

#### `test_point4d()`

#### `test_path4d()`

#### `test_polar_to_xy()`

#### `test_xy_to_polar()`

#### `test_project_plane()`

#### `test_lift_plane()`

#### `test_cylindrical_to_xyz()`

#### `test_xyz_to_cylindrical()`

#### `test_spherical_to_xyz()`

#### `test_xyz_to_spherical()`

#### `test_altaz_to_xyz()`

#### `test_xyz_to_altaz()`

## BOSL2/tests/test_cubetruss.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_cubetruss.scad`

### Modules

#### `test_cubetruss_dist()`

## BOSL2/tests/test_distributors.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_distributors.scad`

### Modules

#### `test_line_copies()`

## BOSL2/tests/test_drawing.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_drawing.scad`

### Modules

#### `test_turtle()`

#### `test_arc()`

#### `test_dashed_stroke()`

## BOSL2/tests/test_edges.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_edges.scad`

### Modules

#### `test__is_edge_array()`

#### `test__edge_set()`

#### `test__normalize_edges()`

#### `test__edges()`

#### `test__corner_edge_count()`

#### `test__corner_edges()`

#### `test__corners()`

#### `test__is_corner_array()`

#### `test__normalize_corners()`

## BOSL2/tests/test_fnliterals.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_fnliterals.scad`

### Modules

#### `test_map()`

#### `test_filter()`

#### `test_reduce()`

#### `test_accumulate()`

#### `test_while()`

#### `test_for_n()`

#### `test_find_first()`

#### `test_binsearch()`

#### `test_simple_hash()`

#### `test_f_1arg()`

#### `test_f_2arg()`

#### `test_f_3arg()`

#### `test_ival()`

#### `test_xval()`

#### `_test_fn1arg(dafunc, tests)`

#### `_test_fn2arg(dafunc, tests)`

#### `_test_fn2arg_simple(dafunc, tests)`

#### `_test_fn3arg(dafunc, tests)`

#### `test_f_cmp()`

#### `test_f_gt()`

#### `test_f_gte()`

#### `test_f_lt()`

#### `test_f_lte()`

#### `test_f_eq()`

#### `test_f_neq()`

#### `test_f_approx()`

#### `test_f_napprox()`

#### `test_f_or()`

#### `test_f_and()`

#### `test_f_nor()`

#### `test_f_nand()`

#### `test_f_xor()`

#### `test_f_not()`

#### `test_f_even()`

#### `test_f_odd()`

#### `test_f_add()`

#### `test_f_sub()`

#### `test_f_mul()`

#### `test_f_div()`

#### `test_f_mod()`

#### `test_f_pow()`

#### `test_f_sin()`

#### `test_f_cos()`

#### `test_f_tan()`

#### `test_f_asin()`

#### `test_f_acos()`

#### `test_f_atan()`

#### `test_f_atan2()`

#### `test_f_exp()`

#### `test_f_ln()`

#### `test_f_log()`

#### `test_f_sqr()`

#### `test_f_sqrt()`

#### `test_f_sign()`

#### `test_f_abs()`

#### `test_f_neg()`

#### `test_f_ceil()`

#### `test_f_floor()`

#### `test_f_round()`

#### `test_f_cross()`

#### `test_f_norm()`

#### `test_f_chr()`

#### `test_f_ord()`

#### `test_f_len()`

#### `test_f_str()`

#### `test_f_str2()`

#### `test_f_str3()`

#### `test_f_min()`

#### `test_f_max()`

#### `test_f_min2()`

#### `test_f_max2()`

#### `test_f_min3()`

#### `test_f_max3()`

#### `test_f_is_bool()`

#### `test_f_is_def()`

#### `test_f_is_undef()`

#### `test_f_is_num()`

#### `test_f_is_int()`

#### `test_f_is_nan()`

#### `test_f_is_finite()`

#### `test_f_is_string()`

#### `test_f_is_list()`

#### `test_f_is_path()`

## BOSL2/tests/test_geometry.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_geometry.scad`

### Modules

#### `assert_std(vc, ve, info)`

#### `test_polygon_triangulate()`

#### `test__normalize_plane()`

#### `test_plane_line_intersection()`

#### `test_plane_intersection()`

#### `test_plane_offset()`

#### `test_plane_from_polygon()`

#### `test_plane_from_normal()`

#### `test_plane_line_angle()`

#### `test__general_plane_line_intersection()`

#### `test_are_points_on_plane()`

#### `test_plane_closest_point()`

#### `test_line_from_points()`

#### `test_is_point_on_line()`

#### `test__point_left_of_line2d()`

#### `test_is_collinear()`

#### `test_point_line_distance()`

#### `test_segment_distance()`

#### `test_line_normal()`

#### `test_line_intersection()`

#### `test_line_closest_point()`

#### `test_circle_2tangents()`

#### `test_circle_3points()`

#### `test_circle_point_tangents()`

#### `test_plane3pt()`

#### `test_plane3pt_indexed()`

#### `test_plane_from_points()`

#### `test_polygon_normal()`

#### `test_plane_normal()`

#### `test_point_plane_distance()`

#### `test_polygon_line_intersection()`

#### `test_is_coplanar()`

#### `test__is_point_above_plane()`

#### `test_polygon_area()`

#### `test_is_polygon_convex()`

#### `test_reindex_polygon()`

#### `test_align_polygon()`

#### `test__noncollinear_triple()`

#### `test_centroid()`

#### `test_point_in_polygon()`

#### `test_is_polygon_clockwise()`

#### `test_clockwise_polygon()`

#### `test_ccw_polygon()`

#### `test_reverse_polygon()`

#### `test_convex_distance()`

#### `test_convex_collision()`

#### `test_rot_decode()`

#### `test_hull()`

#### `test_hull2d_path()`

#### `test_hull3d_faces()`

### Functions

#### `standardize(v)`

from a function like a plane output; v must be a vector

#### `info_str(list, i=0, string=chr(10)`

#### `standard_faces(faces)`

## BOSL2/tests/test_linalg.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_linalg.scad`

### Modules

#### `test_is_matrix()`

#### `test_ident()`

#### `test_qr_factor()`

#### `test_matrix_inverse()`

#### `test_det2()`

#### `test_det3()`

#### `test_determinant()`

#### `test_matrix_trace()`

#### `test_norm_fro()`

#### `test_linear_solve()`

#### `test_null_space()`

#### `test_back_substitute()`

#### `test_outer_product()`

#### `test_column()`

#### `test_submatrix()`

Need decision about behavior for out of bounds ranges, empty ranges

#### `test_hstack()`

#### `test_block_matrix()`

#### `test_diagonal_matrix()`

#### `test_submatrix_set()`

#### `test_transpose()`

### Functions

#### `is_ut(R)`

Check that R is upper triangular

#### `qrok(qr, M)`

Test the R is upper trianglar, Q is orthogonal and qr=M

#### `qrokpiv(qr, M)`

Test the R is upper trianglar, Q is orthogonal, R diagonal non-increasing and qrp=M

#### `nullcheck(A, dim)`

## BOSL2/tests/test_linear_bearings.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_linear_bearings.scad`

### Modules

#### `test_lmXuu_info()`

## BOSL2/tests/test_lists.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_lists.scad`

### Modules

#### `test_is_homogeneous()`

#### `test_select()`

#### `test_slice()`

#### `test_last()`

#### `test_list_head()`

#### `test_list_tail()`

#### `test_in_list()`

#### `test_repeat()`

#### `test_count()`

#### `test_reverse()`

#### `test_list_rotate()`

#### `test_list_set()`

#### `test_list_remove()`

#### `test_list_remove_values()`

#### `test_list_insert()`

#### `test_bselect()`

#### `test_list_bset()`

#### `test_min_length()`

#### `test_max_length()`

#### `test_list_pad()`

#### `test_idx()`

#### `test_shuffle()`

#### `test_set_union()`

#### `test_set_difference()`

#### `test_set_intersection()`

#### `test_force_list()`

#### `test_pair()`

#### `test_triplet()`

#### `test_combinations()`

#### `test_repeat_entries()`

#### `test_list_to_matrix()`

#### `test_flatten()`

#### `test_full_flatten()`

#### `test_list_shape()`

## BOSL2/tests/test_masks2d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_masks2d.scad`

### Modules

#### `test_mask2d_chamfer()`

#### `test_mask2d_cove()`

#### `test_mask2d_roundover()`

#### `test_mask2d_dovetail()`

#### `test_mask2d_rabbet()`

#### `test_mask2d_teardrop()`

#### `test_mask2d_ogee()`

## BOSL2/tests/test_math.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_math.scad`

### Modules

#### `test_quant()`

#### `test_quantdn()`

#### `test_quantup()`

#### `test_constrain()`

#### `test_all_integer()`

#### `test_posmod()`

#### `test_modang()`

#### `test_mean_angle()`

#### `test_sqr()`

#### `test_log2()`

#### `test_rand_int()`

#### `test_gaussian_rands()`

#### `test_lerp()`

#### `test_u_add()`

#### `test_u_sub()`

#### `test_u_mul()`

#### `test_u_div()`

#### `test_hypot()`

#### `test_sinh()`

#### `test_cosh()`

#### `test_tanh()`

#### `test_asinh()`

#### `test_acosh()`

#### `test_atanh()`

#### `test_sum()`

#### `test_cumsum()`

#### `test_sum_of_sines()`

#### `test_deltas()`

#### `test_product()`

#### `test_mean()`

#### `test_median()`

#### `test_convolve()`

#### `test_any()`

#### `test_all()`

#### `test_factorial()`

#### `test_binomial()`

#### `test_binomial_coefficient()`

#### `test_gcd()`

#### `test_lcm()`

#### `test_rational_approx()`

#### `test_complex()`

#### `test_c_mul()`

#### `test_c_div()`

#### `test_c_conj()`

#### `test_c_real()`

#### `test_c_imag()`

#### `test_c_ident()`

#### `test_c_norm()`

#### `test_cumprod()`

#### `test_deriv()`

#### `test_deriv2()`

#### `test_deriv3()`

#### `test_polynomial()`

#### `test_poly_roots()`

#### `test_real_roots()`

#### `test_quadratic_roots()`

#### `test_poly_mult()`

#### `test_poly_div()`

#### `test_poly_add()`

#### `test_root_find()`

## BOSL2/tests/test_miscellaneous.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_miscellaneous.scad`

### Modules

#### `test_hsl()`

#### `test_hsv()`

## BOSL2/tests/test_paths.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_paths.scad`

### Modules

#### `test_is_path()`

#### `test_is_1region()`

#### `force_path()`

#### `test_path_merge_collinear()`

#### `test_path_length()`

#### `test_path_segment_lengths()`

#### `test_path_length_fractions()`

#### `test_subdivide_path()`

#### `test_subdivide_long_segments()`

#### `test_resample_path()`

#### `test_path_closest_point()`

#### `test_path_tangents()`

#### `test_path_curvature()`

#### `test_path_torsion()`

#### `test_is_path_simple()`

## BOSL2/tests/test_regions.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_regions.scad`

### Modules

#### `test_is_region()`

#### `test_union()`

#### `test_intersection()`

#### `test_difference()`

#### `test_exclusive_or()`

#### `test_point_in_region()`

#### `test_make_region()`

#### `test_region_area()`

## BOSL2/tests/test_rounding.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_rounding.scad`

### Modules

#### `test_round_corners()`

## BOSL2/tests/test_screw_drive.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_screw_drive.scad`

### Modules

#### `test_torx_diam()`

#### `test_torx_depth()`

## BOSL2/tests/test_shapes2d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_shapes2d.scad`

### Modules

#### `test_square()`

#### `test_circle()`

#### `test_rect()`

#### `test_trapezoid()`

#### `test_ellipse()`

#### `test_star()`

#### `test_regular_ngon()`

#### `test_pentagon()`

#### `test_hexagon()`

#### `test_octagon()`

#### `test_teardrop2d()`

#### `test_glued_circles()`

#### `test_supershape()`

#### `test_reuleaux_polygon()`

## BOSL2/tests/test_shapes3d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_shapes3d.scad`

### Modules

#### `test_cube()`

#### `test_cylinder()`

#### `test_sphere()`

#### `test_prismoid()`

#### `sphere_OK(style)`

#### `test_spheroid()`

#### `test_cyl()`

## BOSL2/tests/test_skin.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_skin.scad`

### Modules

#### `test_skin()`

#### `test_sweep()`

## BOSL2/tests/test_strings.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_strings.scad`

### Modules

#### `test_upcase()`

#### `test_downcase()`

#### `test_substr_match()`

#### `test_starts_with()`

#### `test_ends_with()`

#### `test_format_int()`

#### `test_format_fixed()`

#### `test_format_float()`

#### `test_is_digit()`

#### `test_is_hexdigit()`

#### `test_is_letter()`

#### `test_is_lower()`

#### `test_is_upper()`

#### `test_parse_float()`

#### `test_parse_frac()`

#### `test_parse_num()`

#### `test_parse_int()`

#### `test_str_join()`

#### `test_str_split()`

#### `test_str_strip()`

#### `test_substr()`

#### `test_suffix()`

#### `test_str_find()`

#### `test_format()`

#### `test_echofmt()`

#### `test_str_pad()`

#### `test_str_replace_char()`

## BOSL2/tests/test_structs.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_structs.scad`

### Modules

#### `test_struct_set()`

#### `test_struct_remove()`

#### `test_struct_val()`

#### `test_struct_keys()`

#### `test_echo_struct()`

#### `test_is_struct()`

## BOSL2/tests/test_transforms.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_transforms.scad`

### Modules

#### `test_translate()`

#### `test_move()`

#### `test_left()`

#### `test_right()`

#### `test_back()`

#### `test_fwd()`

#### `test_down()`

#### `test_up()`

#### `test_scale()`

#### `test_xscale()`

#### `test_yscale()`

#### `test_zscale()`

#### `test_mirror()`

#### `test_xflip()`

#### `test_yflip()`

#### `test_zflip()`

#### `test_rot()`

#### `test_xrot()`

#### `test_yrot()`

#### `test_zrot()`

#### `test_frame_map()`

#### `test_skew()`

#### `test_apply()`

#### `check_path_apply(mat, path)`

#### `check_patch_apply(mat, patch)`

#### `test_is_2d_transform()`

## BOSL2/tests/test_trigonometry.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_trigonometry.scad`

### Modules

#### `test_tri_functions()`

#### `test_hyp_opp_to_adj()`

#### `test_hyp_ang_to_adj()`

#### `test_opp_ang_to_adj()`

#### `test_hyp_adj_to_opp()`

#### `test_hyp_ang_to_opp()`

#### `test_adj_ang_to_opp()`

#### `test_adj_opp_to_hyp()`

#### `test_adj_ang_to_hyp()`

#### `test_opp_ang_to_hyp()`

#### `test_hyp_adj_to_ang()`

#### `test_hyp_opp_to_ang()`

#### `test_adj_opp_to_ang()`

## BOSL2/tests/test_utility.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_utility.scad`

### Modules

#### `test_num_true()`

#### `test_typeof()`

#### `test_is_type()`

#### `test_is_def()`

#### `test_segs()`

#### `test_is_str()`

#### `test_is_int()`

#### `test_is_integer()`

#### `test_is_nan()`

#### `test_is_finite()`

#### `test_is_range()`

#### `test_valid_range()`

#### `test_is_consistent()`

#### `test_same_shape()`

#### `test_default()`

#### `test_first_defined()`

#### `test_one_defined()`

#### `test_num_defined()`

#### `test_any_defined()`

#### `test_all_defined()`

#### `test_get_anchor()`

#### `test_get_radius()`

#### `test_scalar_vec3()`

#### `test_segs()`

## BOSL2/tests/test_vectors.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_vectors.scad`

### Modules

#### `test_is_vector()`

#### `test_v_floor()`

#### `test_v_ceil()`

#### `test_v_lookup()`

#### `test_v_mul()`

#### `test_v_div()`

#### `test_v_abs()`

#### `test_v_theta()`

#### `test_min_index()`

#### `test_max_index()`

#### `test_unit()`

#### `test_vector_angle()`

#### `test_vector_axis()`

#### `test_vector_search()`

#### `test_vector_search_tree()`

#### `test_vector_nearest()`

#### `test_add_scalar()`

#### `test_pointlist_bounds()`

#### `test_closest_point()`

#### `test_furthest_point()`

## BOSL2/tests/test_version.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_version.scad`

### Modules

#### `test_bosl_version()`

#### `test_bosl_version_num()`

#### `test_bosl_version_str()`

#### `test_bosl_required()`

#### `test_version_to_list()`

#### `test_version_to_str()`

#### `test_version_to_num()`

#### `test_version_cmp()`

#### `testvercmp(x, y, z)`

### Functions

#### `diversify(x)`

## BOSL2/tests/test_vnf.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tests/test_vnf.scad`

### Modules

#### `test_is_vnf()`

#### `test_is_vnf_list()`

#### `test_vnf_vertices()`

#### `test_vnf_faces()`

#### `test_vnf_from_polygons()`

#### `test_vnf_volume()`

#### `test_vnf_area()`

#### `test_vnf_join()`

#### `test_vnf_triangulate()`

#### `test_vnf_vertex_array()`

## BOSL2/threading.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/threading.scad`

### Modules

#### `_nutshape(nutwidth, h, shape, bevel1, bevel2, bevang)`

## BOSL2/transforms.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/transforms.scad`

### Modules

#### `move(v=[0, 0, 0], p)`

mat3d = move([2,3,4]);  // Returns: [[1,0,0,2],[0,1,0,3],[0,0,1,4],[0,0,0,1]]

#### `left(x=0, p)`

mat3d = left(4);  // Returns: [[1,0,0,-4],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#### `right(x=0, p)`

mat3d = right(4);  // Returns: [[1,0,0,4],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

#### `xmove(x=0, p)`

#### `fwd(y=0, p)`

mat3d = fwd(4);  // Returns: [[1,0,0,0],[0,1,0,-4],[0,0,1,0],[0,0,0,1]]

#### `back(y=0, p)`

mat3d = back(4);  // Returns: [[1,0,0,0],[0,1,0,4],[0,0,1,0],[0,0,0,1]]

#### `ymove(y=0, p)`

#### `down(z=0, p)`

mat3d = down(4);  // Returns: [[1,0,0,0],[0,1,0,0],[0,0,1,-4],[0,0,0,1]]

#### `up(z=0, p)`

mat3d = up(4);  // Returns: [[1,0,0,0],[0,1,0,0],[0,0,1,4],[0,0,0,1]]

#### `zmove(z=0, p)`

#### `rot(a=0, v, cp, from, to, reverse=false)`

stroke(rot(30,p=path), closed=true);

#### `xrot(a=0, p, cp)`

xrot(90) cylinder(h=50, r=10, center=true);

#### `yrot(a=0, p, cp)`

yrot(90) cylinder(h=50, r=10, center=true);

#### `zrot(a=0, p, cp)`

zrot(90) cube(size=[60,20,40], center=true);

#### `tilt(to, p, cp, reverse=false)`

stroke(tilt(RIGHT+FWD,path3d(path)), closed=true);

#### `xscale(x=1, p, cp=0)`

stroke(xscale(2,path),closed=true);

#### `yscale(y=1, p, cp=0)`

stroke(yscale(2,path),closed=true);

#### `zscale(z=1, p, cp=0)`

stroke(zscale(2,path),closed=true);

#### `xflip(p, x=0)`

color("red", 0.333) yrot(90) cylinder(d1=10, d2=0, h=20);

#### `yflip(p, y=0)`

color("red", 0.333) xrot(90) cylinder(d1=10, d2=0, h=20);

#### `zflip(p, z=0)`

color("red", 0.333) cylinder(d1=10, d2=0, h=20);

#### `frame_map(x, y, z, p, reverse=false)`

#### `skew(p, sxy, sxz, syx, syz, szx, szy, axy, axz, ayx, ayz, azx, azy)`

stroke(pts,closed=true,dots=true,dots_color="blue");

#### `translate(v)`

#### `rotate(a, v)`

#### `scale(v, cp=[0, 0, 0], dir)`

#### `multmatrix(m)`

### Functions

#### `move(v=[0, 0, 0], p=_NO_ARG)`

#### `translate(v=[0, 0, 0], p=_NO_ARG)`

#### `left(x=0, p=_NO_ARG)`

#### `right(x=0, p=_NO_ARG)`

#### `xmove(x=0, p=_NO_ARG)`

#### `fwd(y=0, p=_NO_ARG)`

#### `back(y=0, p=_NO_ARG)`

#### `ymove(y=0, p=_NO_ARG)`

#### `down(z=0, p=_NO_ARG)`

#### `up(z=0, p=_NO_ARG)`

#### `zmove(z=0, p=_NO_ARG)`

#### `rot(a=0, v, cp, from, to, reverse=false, p=_NO_ARG)`

#### `xrot(a=0, p=_NO_ARG, cp)`

#### `yrot(a=0, p=_NO_ARG, cp)`

#### `zrot(a=0, p=_NO_ARG, cp)`

#### `tilt(to, p=_NO_ARG, cp, reverse=false)`

#### `scale(v=1, p=_NO_ARG, cp=[0, 0, 0], dir)`

stroke(scale([1.5,3],path),closed=true);

#### `xscale(x=1, p=_NO_ARG, cp=0)`

#### `yscale(y=1, p=_NO_ARG, cp=0)`

#### `zscale(z=1, p=_NO_ARG, cp=0)`

#### `mirror(v, p=_NO_ARG)`

#### `xflip(p=_NO_ARG, x=0)`

#### `yflip(p=_NO_ARG, y=0)`

#### `zflip(p=_NO_ARG, z=0)`

#### `frame_map(x, y, z, p=_NO_ARG, reverse=false)`

#### `skew(p=_NO_ARG, sxy, sxz, syx, syz, szx, szy, axy, axz, ayx, ayz, azx, azy)`

#### `is_2d_transform(t)`

/   b = is_2d_transform(scale([2,3,4]));  // Returns: true

#### `apply(transform, points)`

#### `_apply(transform, points)`

## BOSL2/trigonometry.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/trigonometry.scad`

### Functions

#### `law_of_cosines(a, b, c, C)`

C = The reference angle in degrees of the corner opposite of the third side.

#### `law_of_sines(a, A, b, B)`

B = The reference angle in degrees of the corner opposite of the second side.

#### `hyp_opp_to_adj(hyp, opp)`

adj = hyp_opp_to_adj(5,3);  // Returns: 4

#### `opp_hyp_to_adj(opp, hyp)`

adj = opp_hyp_to_adj(3,5);  // Returns: 4

#### `hyp_ang_to_adj(hyp, ang)`

adj = hyp_ang_to_adj(8,60);  // Returns: 4

#### `ang_hyp_to_adj(ang, hyp)`

adj = ang_hyp_to_adj(60,8);  // Returns: 4

#### `opp_ang_to_adj(opp, ang)`

adj = opp_ang_to_adj(8,45);  // Returns: 8

#### `ang_opp_to_adj(ang, opp)`

adj = ang_opp_to_adj(45,8);  // Returns: 8

#### `hyp_adj_to_opp(hyp, adj)`

opp = hyp_adj_to_opp(5,4);  // Returns: 3

#### `adj_hyp_to_opp(adj, hyp)`

#### `hyp_ang_to_opp(hyp, ang)`

opp = hyp_ang_to_opp(8,30);  // Returns: 4

#### `ang_hyp_to_opp(ang, hyp)`

opp = ang_hyp_to_opp(30,8);  // Returns: 4

#### `adj_ang_to_opp(adj, ang)`

opp = adj_ang_to_opp(8,45);  // Returns: 8

#### `ang_adj_to_opp(ang, adj)`

opp = ang_adj_to_opp(45,8);  // Returns: 8

#### `adj_opp_to_hyp(adj, opp)`

hyp = adj_opp_to_hyp(3,4);  // Returns: 5

#### `opp_adj_to_hyp(opp, adj)`

hyp = opp_adj_to_hyp(4,3);  // Returns: 5

#### `adj_ang_to_hyp(adj, ang)`

hyp = adj_ang_to_hyp(4,60);  // Returns: 8

#### `ang_adj_to_hyp(ang, adj)`

hyp = ang_adj_to_hyp(60,4);  // Returns: 8

#### `opp_ang_to_hyp(opp, ang)`

hyp = opp_ang_to_hyp(4,30);  // Returns: 8

#### `ang_opp_to_hyp(ang, opp)`

hyp = opp_ang_to_hyp(30,4);  // Returns: 8

#### `hyp_adj_to_ang(hyp, adj)`

ang = hyp_adj_to_ang(8,4);  // Returns: 60 degrees

#### `adj_hyp_to_ang(adj, hyp)`

ang = adj_hyp_to_ang(4,8);  // Returns: 60 degrees

#### `hyp_opp_to_ang(hyp, opp)`

ang = hyp_opp_to_ang(8,4);  // Returns: 30 degrees

#### `opp_hyp_to_ang(opp, hyp)`

ang = opp_hyp_to_ang(4,8);  // Returns: 30 degrees

#### `adj_opp_to_ang(adj, opp)`

ang = adj_opp_to_ang(sqrt(3)/2,0.5);  // Returns: 30 degrees

#### `opp_adj_to_ang(opp, adj)`

ang = opp_adj_to_ang(0.5,sqrt(3)/2);  // Returns: 30 degrees

## BOSL2/tripod_mounts.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/tripod_mounts.scad`

### Modules

#### `manfrotto_rc2_plate(chamfer="all", anchor, orient, spin)`

manfrotto_rc2_plate("bot");

## BOSL2/turtle3d.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/turtle3d.scad`

### Modules

#### `turtle3d(commands, state=RIGHT, transforms=false, full_state=false, repeat=1)`

### Functions

#### `_transpart(T)`

Translation vector from a matrix

#### `_rotpart(T)`

The non-translation part of a matrix

#### `_turtle3d_state_valid(state)`

#### `turtle3d(commands, state=RIGHT, transforms=false, full_state=false, repeat=1)`

#### `_turtle3d_repeat(commands, state, repeat)`

#### `_turtle3d_command_len(commands, index)`

#### `_turtle3d(commands, state, index=0)`

#### `_turtle3d_rotation(command, angle, center)`

#### `_tupdate(state, tran, pretran)`

to the state.

#### `_turtle3d_command(command, parm, parm2, state, index)`

#### `_turtle3d_list_command(command, arcsteps, movescale, lastT, lastPre, index)`

## BOSL2/utility.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/utility.scad`

### Modules

#### `no_children(count)`

}

#### `req_children(count)`

}

#### `no_module()`

module foo() { no_module(); }

#### `deprecate(new_name)`

new_name = name of the new module that replaces the old one

#### `echo_viewport()`

#### `assert_approx(got, expected, info)`

assert_approx(1/3, 0.333333333333333, str("number=",1,", denom=",3));

#### `assert_equal(got, expected, info)`

assert_equal(3*9, 27, str("a=",3,", b=",9));

#### `shape_compare(eps=1/1024)`

}

### Functions

#### `typeof(x)`

typ = typeof(function (x,y) x+y);  // Returns: "function"

#### `is_type(x, types)`

is_str4 = is_type(3, "string");  // Returns: false

#### `is_def(x)`

bool = is_def("foo");  // Returns: true

#### `is_str(x)`

bool = is_str("foo");  // Returns: true

#### `is_int(n)`

bool = is_int("foo");  // Returns: false

#### `is_integer(n)`

#### `all_integer(x)`

b = all_integer([3,[4,7],5]); // Returns: false

#### `is_nan(x)`

bool = is_nan(NAN);    // Returns: true

#### `is_finite(x)`

bool = is_finite(-INF);   // Returns: false

#### `is_range(x)`

bool = is_range([3:5]);   // Returns: true

#### `valid_range(x)`

bool = is_range([3:1]);   // Returns: false

#### `is_func(x)`

bool = is_func(f);  // Returns: true

#### `is_consistent(list, pattern)`

is_consistent([], [1,[2,3]]);                        // Returns true

#### `_list_pattern(list)`

Creates a list with the same structure of `list` with each of its elements replaced by 0.

#### `same_shape(a, b)`

same_shape([3,4,5], [7,[3,4]]);    // Returns false

#### `is_bool_list(list, length)`

length = if given, list must be this length

#### `any(l, func)`

any([[0,0], [1,0]]);   // Returns true.

#### `_any_func(l, func, i=0, out=false)`

#### `_any_bool(l, i=0, out=false)`

#### `all(l, func)`

test6 = all([[1,1], [1,1]]);   // Returns true.

#### `_all_func(l, func, i=0, out=true)`

#### `_all_bool(l, i=0, out=true)`

#### `num_true(l, func)`

num6 = num_true([[], [1,0]]);      // Returns 1.

#### `default(v, dflt=undef)`

dflt = Value to return if `v` *is* `undef`.  Default: undef

#### `first_defined(v, recursive=false, _i=0)`

val = first_defined([undef,7,undef,true]);  // Returns: 7

#### `one_defined(vals, names, dflt=_UNDEF)`

#### `num_defined(v)`

cnt = num_defined([3,7,undef,2,undef,undef,1]);  // Returns: 4

#### `any_defined(v, recursive=false)`

bool = any_defined([undef,undef,[42]],recursive=true);     // Returns: true

#### `all_defined(v, recursive=false)`

bool = all_defined([23,34,[42]],recursive=true);     // Returns: true

#### `u_add(a, b)`

b = Second value.

#### `u_sub(a, b)`

b = Second value.

#### `u_mul(a, b)`

b = Second value.

#### `u_div(a, b)`

b = Second value.

#### `get_anchor(anchor, center, uncentered=BOT, dflt=CENTER)`

anchr6 = get_anchor(RIGHT, true,  BOTTOM, TOP);  // Returns: [0, 0, 0] (CENTER)

#### `get_radius(r1, r2, r, d1, d2, d, dflt)`

r = get_radius(r1=8, d=6, dflt=1);              // Returns: 8

#### `scalar_vec3(v, dflt)`

vec = scalar_vec3([10]);       // Returns: [10,0,0]

#### `segs(r, angle)`

$fa=2; $fs=3; sides=segs(10,180); // Returns: 11

#### `no_function(name)`

x = no_function("foo");

#### `_valstr(x)`

#### `looping(state)`

state = The loop state value.

#### `loop_while(state, continue)`

continue = A boolean value indicating whether the current loop should progress.

#### `loop_done(state)`

state = The loop state value.

## BOSL2/vectors.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/vectors.scad`

### Functions

#### `is_vector(v, length, zero, all_nonzero=false, eps=_EPSILON)`

is_vector([],zero=false);              // Returns false

#### `add_scalar(v, s)`

a = add_scalar([1,2,3],3);            // Returns: [4,5,6]

#### `v_mul(v1, v2)`

v_mul([3,4,5], [8,7,6]);  // Returns [24, 28, 30]

#### `v_div(v1, v2)`

v_div([24,28,30], [8,7,6]);  // Returns [3, 4, 5]

#### `v_abs(v)`

v_abs([-1,3,-9]);  // Returns: [1,3,9]

#### `v_ceil(v)`

Returns the given vector after performing a `ceil()` on all items.

#### `v_floor(v)`

Returns the given vector after performing a `floor()` on all items.

#### `v_round(v)`

Returns the given vector after performing a `round()` on all items.

#### `v_lookup(x, v)`

x = v_lookup(4.5, [[4, [3,4,5]], [5, [5,6,7]]]);  // Returns: [4,5,6]

#### `unit(v, error=[[["ASSERT"]]])`

v6 = unit([0,0,0]);    // Asserts an error.

#### `v_theta(v)`

Given a vector, returns the angle in degrees counter-clockwise from X+ on the XY plane.

#### `vector_angle(v1, v2, v3)`

ang6 = vector_angle([[10,0,10], [0,0,0], [-10,10,0]]);  // Returns: 120

#### `vector_axis(v1, v2=undef, v3=undef)`

axis6 = vector_axis([[10,0,10], [0,0,0], [-10,10,0]]);  // Returns: [-0.57735, -0.57735, 0.57735]

#### `vector_bisect(v1, v2)`

If given two vectors that are directly opposed, returns `undef`.

#### `vector_perp(v, w)`

stroke([[0,0],vector_perp(v,w)], endcap2="arrow2", color="blue");

#### `closest_point(pt, points)`

points = The list of points to search.

#### `furthest_point(pt, points)`

points = The list of points to search.

#### `vector_search(query, r, target)`

}

#### `_bt_search(query, r, points, tree)`

Ball tree search

#### `vector_search_tree(points, leafsize=25, treemin=400)`

}

#### `_bt_tree(points, ind, leafsize=25)`

Ball tree construction

#### `vector_nearest(query, k, target)`

}

#### `_bt_nearest(p, k, points, tree, answers=[])`

Ball tree nearest

#### `_insert_sorted(list, k, new)`

#### `_insert_many(list, k, newlist, i=0)`

#### `pointlist_bounds(pts)`

pts = List of points.

#### `fit_to_box(pts, x, y, z)`

vnf_polyhedron(vnf_boxed);

## BOSL2/version.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/version.scad`

### Modules

#### `bosl_required(version)`

version = version required

### Functions

#### `bosl_version()`

For example, version 2.1.43 will be returned as `[2,1,43]`.

#### `bosl_version_num()`

revision number.  For example, version 2.1.43 will be returned as `2.010043`.

#### `bosl_version_str()`

For example, version 2.1.43 will be returned as `"2.1.43"`.

#### `_version_split_str(x, _i=0, _out=[], _num=0)`

#### `version_to_list(version)`

v4 = version_to_list([2,3,4,5]); // Returns: [2,3,4]

#### `version_to_str(version)`

v4 = version_to_str("2.3.89");  // Returns: "2.3.89"

#### `version_to_num(version)`

v4 = version_to_num("2.6.79");   // Returns: 2.060079

#### `version_cmp(a, b)`

cmp3 = version_cmp(2.010034, "2.1.35");  // Returns: <0

## BOSL2/vnf.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/vnf.scad`

### Modules

#### `vnf_polyhedron(vnf, convexity=2, cp="centroid", anchor="origin", spin=0, orient=UP, atype="hull")`

"origin" = Anchor at the origin, oriented UP.

#### `vnf_wireframe(vnf, width=1)`

vnf_wireframe(octahedron,width=5);

#### `vnf_hull(vnf, fast=false)`

#### `_show_vertices(vertices, size=1, filter)`

/   }

#### `_show_faces(vertices, faces, size=1, filter)`

/   }

#### `debug_vnf(vnf, faces=true, vertices=true, opacity=0.5, size=1, convexity=6, filter)`

debug_vnf([verts,faces], size=2);

#### `vnf_validate(vnf, size=1, show_warns=true, check_isects=false, big_face=true, opacity=0.67, adjacent=false, label_verts=false, label_faces=false, wireframe=false)`

### Functions

#### `_lofttri(p1, p2, i1offset, i2offset, n1, n2, reverse=false, trilist=[], i1=0, i2=0, tricount1=0, tricount2=0, trimax=INF)`

#### `vnf_join(vnfs)`

orient=FRONT,h=.1);

#### `vnf_from_polygons(polygons, fast=false, eps=_EPSILON)`

#### `_path_path_closest_vertices(path1, path2)`

#### `_join_paths_at_vertices(path1, path2, v1, v2)`

#### `_cleave_connected_region(region, eps=_EPSILON)`

/   https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf

#### `_polyHoles(outer, holes, extremes, eps=_EPSILON, n=0)`

see: _cleave_connected_region(region, eps)

#### `_bridge(pt, outer, eps)`

see _polyHoles(outer, holes, extremes, eps)

#### `vnf_from_region(region, transform, reverse=false, triangulate=true)`

vnf_wireframe(vnf,width=.25);

#### `is_vnf(x)`

Returns true if the given value looks like a VNF structure.

#### `is_vnf_list(x)`

Description: Returns true if the given value looks passingly like a list of VNF structures.

#### `vnf_vertices(vnf)`

Description: Given a VNF structure, returns the list of vertex points.

#### `vnf_faces(vnf)`

Description: Given a VNF structure, returns the list of faces, where each face is a list of indices into the VNF vertex list.

#### `vnf_reverse_faces(vnf)`

Reverses the orientation of all the faces in the given VNF.

#### `vnf_quantize(vnf, q=pow(2, -12)`

q = The quanta to quantize the VNF coordinates to.

#### `vnf_merge_points(vnf, eps=_EPSILON)`

eps = the tolerance in finding duplicates. Default: 1e-9

#### `vnf_drop_unused_points(vnf)`

and this function may be slow on large VNFs.

#### `_link_indicator(l, imin, imax)`

#### `vnf_triangulate(vnf)`

color("red")vnf_wireframe(triangulated,width=.3);

#### `vnf_unify_faces(vnf)`

#### `_detri_combine_faces(edgelist, faces, normals, facelist, curface)`

#### `vnf_slice(vnf, dir, cuts)`

color("red")vnf_wireframe(sliced,width=.3);

#### `_shift_cut_plane(vnf, dir, cut, off=0.001)`

#### `_split_polygon_at_x(poly, x)`

#### `_split_2dpolygons_at_each_x(polys, xs, _i=0)`

#### `_slice_3dpolygons(polys, dir, cuts)`

/   cuts = A list of scalar values for locating the cuts

#### `vnf_volume(vnf)`

Divide the polyhedron into tetrahedra with the origin as one vertex and sum up the signed volume.

#### `vnf_area(vnf)`

Returns the surface area in any VNF by adding up the area of all its faces.  The VNF need not be a manifold.

#### `_vnf_centroid(vnf, eps=_EPSILON)`

/ The centroid of the total is the volume weighted average.

#### `vnf_bounds(vnf, fast=false)`

echo(vnf_bounds(cube([2,3,4],center=true)));   // Displays [[-1, -1.5, -2], [1, 1.5, 2]]

#### `projection(vnf, cut=false, z=0, eps=_EPSILON)`

#### `vnf_halfspace(plane, vnf, closed=true, boundary=false)`

stroke(boundary,color="red");

#### `_assemble_paths(vertices, edges, paths=[], i=0)`

#### `_vnfcut(plane, vertices, vertexmap, inside, faces, vertcount, newfaces=[], newedges=[], newvertices=[], i=0)`

#### `_triangulate_planar_convex_polygons(polys)`

#### `vnf_bend(vnf, r, d, axis="Z")`

vnf_polyhedron(bent);

#### `vnf_hull(vnf)`

vnf_hull(vnf);

#### `_sort_pairs0(arr)`

#### `vnf_boundary(vnf, merge=true, idx=false)`

stroke(boundary,color="green");

#### `vnf_small_offset(vnf, delta, merge=true)`

}

#### `vnf_sheet(vnf, delta, style="default", merge=true, thickness=undef)`

#### `_vnf_validate(vnf, show_warns=true, check_isects=false, big_face=false)`

Each error has the format `[ERR_OR_WARN,CODE,MESG,POINTS,COLOR]`.

#### `_vnf_validate_err(name, extra)`

#### `_pts_not_reported(pts, varr, reports)`

#### `_edge_not_reported(edge, varr, reports)`

#### `_vnf_find_edge_faces(vnf, edge)`

#### `_vnf_find_corner_faces(vnf, corner)`

## BOSL2/walls.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/walls.scad`

### Modules

#### `sparse_wall(h=50, l=100, thick=4, maxang=30, strut=5, max_bridge=20, anchor=CENTER, spin=0, orient=UP)`

sparse_wall(h=40, l=100, thick=3, strut=2, maxang=45, max_bridge=30);

#### `sparse_wall2d(size=[50, 100], maxang=30, strut=5, max_bridge=20, anchor=CENTER, spin=0)`

sparse_wall2d(size=[40,100], strut=2, maxang=45, max_bridge=30);

#### `_honeycomb(shape, spacing=10, hex_wall=1)`

#### `_bevelWall(shape, bevel, thickness)`

#### `corrugated_wall(h=50, l=100, thick=5, strut=5, wall=2, anchor=CENTER, spin=0, orient=UP)`

corrugated_wall(h=50, l=100, strut=8, wall=3);

#### `thinning_wall(h=50, l=100, thick=5, ang=30, braces=false, strut, wall, anchor=CENTER, spin=0, orient=UP)`

thinning_wall(h=50, l=[80,50], thick=4, strut=4, wall=2, braces=true);

#### `thinning_triangle(h=50, l=100, thick=5, ang=30, strut=5, wall=3, diagonly=false, center, anchor, spin=0, orient=UP)`

thinning_triangle(h=50, l=80, thick=4, ang=30, strut=5, wall=2, diagonly=true, center=false);

#### `narrowing_strut(w=10, l=100, wall=5, ang=30, anchor=BOTTOM, spin=0, orient=UP)`

narrowing_strut(w=10, l=100, wall=5, ang=30);

### Functions

#### `_bevelSolid(shape, bevel)`

## BOSL2/wiring.scad

**Path:** `/home/guillermo/.local/share/OpenSCAD/libraries/BOSL2/wiring.scad`

### Modules

#### `wire_bundle(path, wires, wirediam=2, rounding=10, wirenum=0, corner_steps=15)`

wire_bundle([[50,0,-50], [50,50,-50], [0,50,-50], [0,0,-50], [0,0,0]], rounding=10, wires=13);

### Functions

#### `_hex_offset_ring(d, lev=0)`

/   _hex_offset_ring(d=1, lev=3); // Returns a hex ring of 18 points.

#### `_hex_offsets(n, d, lev=0, arr=[])`

/   d = How far to space each point away from others.

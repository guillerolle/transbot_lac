$fn = 100;

union() {
	difference() {
		cube(size = [100, 50, 20]);
		translate(v = [5, 5, 5]) {
			cube(size = [90, 40, 20]);
		}
		translate(v = [3, 3, 23]) {
			mirror(v = [0, 0, 1]) {
				union() {
					cylinder(h = 2, r1 = 2.5);
					cylinder(h = 1, r1 = 10);
				}
			}
		}
		translate(v = [3, 47, 23]) {
			mirror(v = [0, 0, 1]) {
				union() {
					cylinder(h = 2, r1 = 2.5);
					cylinder(h = 1, r1 = 10);
				}
			}
		}
		translate(v = [97, 3, 23]) {
			mirror(v = [0, 0, 1]) {
				union() {
					cylinder(h = 2, r1 = 2.5);
					cylinder(h = 1, r1 = 10);
				}
			}
		}
		translate(v = [97, 47, 23]) {
			mirror(v = [0, 0, 1]) {
				union() {
					cylinder(h = 2, r1 = 2.5);
					cylinder(h = 1, r1 = 10);
				}
			}
		}
	}
	%translate(v = [0, 0, 20]) {
		difference() {
			union() {
				translate(v = [0, 0, 0]) {
					cube(size = [100, 50, 5]);
				}
				translate(v = [5, 5, 5]) {
					linear_extrude(height = 1) {
						text(text = "box");
					}
				}
			}
			translate(v = [3, 3, 0.5]) {
				mirror(v = [0, 0, 1]) {
					union() {
						cylinder(h = 2, r1 = 2.5);
						cylinder(h = 1, r1 = 10);
					}
				}
			}
			translate(v = [3, 47, 0.5]) {
				mirror(v = [0, 0, 1]) {
					union() {
						cylinder(h = 2, r1 = 2.5);
						cylinder(h = 1, r1 = 10);
					}
				}
			}
			translate(v = [97, 3, 0.5]) {
				mirror(v = [0, 0, 1]) {
					union() {
						cylinder(h = 2, r1 = 2.5);
						cylinder(h = 1, r1 = 10);
					}
				}
			}
			translate(v = [97, 47, 0.5]) {
				mirror(v = [0, 0, 1]) {
					union() {
						cylinder(h = 2, r1 = 2.5);
						cylinder(h = 1, r1 = 10);
					}
				}
			}
		}
	}
}

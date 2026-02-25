use </home/grolle/vscode-workspaces/transbot/libs/python/openscad2physical/Axle.scad>;
use </home/grolle/vscode-workspaces/transbot/libs/python/openscad2physical/Wheel.scad>;
use </home/grolle/vscode-workspaces/transbot/libs/python/openscad2physical/castorwheel.scad>;

union() {
	translate(v = [0, 0, 60]) {
		rotate(a = [0, 0, 0]) {
			translate(v = [0, 0, 0]) {
				rotate(a = [0, 0, 0]) {
					translate(v = [0, 0, 0]) {
						rotate(a = [0, 90, 90]) {
							translate(v = [0, 0, 0]) {
								rotate(a = [0, 0, 0]) {
									union() {
										Axle(diameter = 20, length = 500);
										translate(v = [0, 0, 250]) {
											rotate(a = [0, 0, 0]) {
												rotate(a = ($t * 360), v = [1, 0, 0]) {
													translate(v = [0, 0, 0]) {
														rotate(a = [0, 0, 0]) {
															Wheel(diameter = 140, hole = 20, width = 50);
														}
													}
												}
											}
										}
										translate(v = [0, 0, -250]) {
											rotate(a = [0, 0, 0]) {
												rotate(a = ($t * 360), v = [0, 0, 1]) {
													translate(v = [0, 0, 0]) {
														rotate(a = [0, 0, 0]) {
															Wheel(diameter = 120, hole = 20, width = 30);
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	translate(v = [600, 0, 130]) {
		rotate(a = [0, 0, 0]) {
			translate(v = [0, 0, 0]) {
				rotate(a = [0, 0, 0]) {
					translate(v = [0, 0, 0]) {
						rotate(a = [0, 0, 0]) {
							rotate(a = ($t * 360), v = [0, 0, 1]) {
								translate(v = [-40, 0, -70]) {
									rotate(a = [0, 0, 0]) {
										union() {
											CastorArm();
											translate(v = [0, 0, 0]) {
												rotate(a = [-90, 0, 0]) {
													rotate(a = ($t * 360), v = [0, 0, 1]) {
														translate(v = [0, 0, 0]) {
															rotate(a = [0, 0, 0]) {
																Wheel(diameter = 120, hole = 20, width = 30);
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}

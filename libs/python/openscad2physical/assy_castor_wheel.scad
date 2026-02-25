use </home/grolle/vscode-workspaces/transbot/libs/python/openscad2physical/castorwheel.scad>;
use </home/grolle/vscode-workspaces/transbot/libs/python/openscad2physical/Wheel.scad>;

translate(v = [0, 0, 0]) {
	rotate(a = [0, 0, 0]) {
		rotate(a = ($t * 360), v = [0, 0, 1]) {
			translate(v = [-40, 0, -65]) {
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

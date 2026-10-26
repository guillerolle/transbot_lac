ros2 run depth_image_proc point_cloud_xyzrgb_node --ros-args \
  -r __ns:=/transbot \
  -r rgb/image_rect_color:=rgbd_camera/rgb \
  -r depth_registered/image_rect:=rgbd_camera/depth \
  -r rgb/camera_info:=rgbd_camera/camera_info \
  -r points:=rgbd_camera/points \
  -p use_sim_time:=true

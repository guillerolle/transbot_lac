#!/bin/env python3
# coding: utf-8

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    robot_name = LaunchConfiguration('robot_name')
    robot_model = LaunchConfiguration('robot_model')
    
    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'world.launch.py']),
        ),
        launch_arguments={
            # 'gz_args': '-r empty.sdf --physics-engine gz-physics-bullet-featherstone-plugin'
            # 'gz_args': '-r',
            # 'world': LaunchConfiguration('world')
            # 'robot_name': robot_name,
            # 'robot_model': robot_model,
            # 'robot_pkg': robot_pkg,
        }.items()
    )
    
    robot_spawn_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'spawner.launch.py']),
        ),
        launch_arguments={
            'robot_name': robot_name,
            'robot_model': robot_model,
            'robot_pkg': 'transbot_gazebo',
        }.items()
    )
    
    controllers_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_controller'), 'launch', PythonExpression(['"', LaunchConfiguration('controllers_launch'), '.launch.py"']) ]),
        ),
        launch_arguments={
            'robot_name': robot_name
        }.items()
    )
    
    camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_camera_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/rgbd_camera/image@sensor_msgs/msg/Image[gz.msgs.Image"'
                ]),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/rgbd_camera/image"']), 'rgbd_camera/image'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )    
    
    rgbd_camera_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_rgbd_camera_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/rgbd_camera/points@sensor_msgs/msg/PointCloud2[gz.msgs.PointCloudPacked"'
                ]),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/rgbd_camera/points"']), 'rgbd_camera/points'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )
    
    rgbd_camera_info_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_rgbd_camera_info_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/rgbd_camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo"'
                ]),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/rgbd_camera/camera_info"']), 'rgbd_camera/camera_info'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )
    
    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_imu_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU"'
                ]),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/imu"']), 'imu'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )
    
    lidar_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_lidar_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan"'
                ]),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/scan"']), 'scan'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )
    
    teleop_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_teleop'), 'launch', 'teleop.launch.py' ]), # PythonExpression(['"', robot_model, '.launch.py"'])
        ),
        launch_arguments={
            'robot_name': LaunchConfiguration('robot_name')
        }.items()
    )
    
    passive_spawn = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'spawner.launch.py']),
        ),
        launch_arguments={
            'robot_name': 'movingshelf',
            'robot_model': 'movingshelf_4wheels_low_lifter',
            'robot_pkg': 'transbot_gazebo',
            'y': '2.0',
        }.items()
    )    
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('robot_model', default_value='shelf_lifter'),
        DeclareLaunchArgument('controllers_launch', default_value='diff_drive'),
        world_launch,
        robot_spawn_launch,
        controllers_launch,
        camera_bridge,
        rgbd_camera_bridge,
        rgbd_camera_info_bridge, 
        imu_bridge,
        lidar_bridge,
        teleop_launch,
        # passive_spawn,
    ])
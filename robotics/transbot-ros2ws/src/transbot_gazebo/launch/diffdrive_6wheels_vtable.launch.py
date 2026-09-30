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
    # Launch Configurations
    robot_name = LaunchConfiguration('robot_name')
    robot_model = LaunchConfiguration('robot_model')
    robot_pkg = LaunchConfiguration('robot_pkg')
    
    passive_rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_description'), 'launch', 'robot_state_publisher.launch.py']),
        ),
        launch_arguments={
            'robot_name': 'moving_table',
            'robot_model': 'table_4wheels_vtable',
            'robot_pkg': 'transbot_gazebo',
        }.items()
    )
    
    passive_spawn_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='passive_spawn',
        arguments=[
            '-topic', PythonExpression(['"/moving_table/robot_description"']),
            '-name', 'moving_table',
            '-allow_renaming', 'true',
            '-x', '0', 
            '-y', '2', 
            '-z', '0',
            '-R', '0',
            '-P', '0',
            '-Y', '0',
        ]
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
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('robot_model', default_value='diffdrive_6wheels_vtable'),
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        # spawn_launch,
        # controllers_launch,
        # teleop_launch,
        camera_bridge,
        imu_bridge,
        lidar_bridge,
        # passive_spawn,
        rgbd_camera_bridge,
        rgbd_camera_info_bridge,
        passive_rsp_launch,
        passive_spawn_node
    ])
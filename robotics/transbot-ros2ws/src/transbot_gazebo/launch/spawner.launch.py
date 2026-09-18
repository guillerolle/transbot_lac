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
    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')
    z = LaunchConfiguration('z')
    R = LaunchConfiguration('R')
    P = LaunchConfiguration('P')
    Y = LaunchConfiguration('Y')
    
    rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_description'), 'launch', 'robot_state_publisher.launch.py']),
        ),
        launch_arguments={
            'robot_name': robot_name,
            'robot_model': robot_model,
            'robot_pkg': robot_pkg,
        }.items()
    )
    
    spawn_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='spawn_entity',
        arguments=[
            '-topic', PythonExpression(['"', robot_name, '/robot_description"']),
            '-name', robot_name,
            '-allow_renaming', 'true',
            '-x', x, 
            '-y', y, 
            '-z', z,
            '-R', R,
            '-P', P,
            '-Y', Y,
        ]
    )
    
    ground_truth_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='gz_ground_truth_bridge',
        namespace=robot_name,
        arguments=[
            PythonExpression([
                '"/model/', robot_name,
                '/ground_truth/pose@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V"'
                ]),

            # PythonExpression(['/model/', robot_name, '/ground_truth/odometry',
            # '@nav_msgs/msg/Odometry[gz.msgs.Odometry']),
        ],
        remappings=[
            (PythonExpression(['"/model/', robot_name, '/ground_truth/pose"']), '/tf'),
        ],
        parameters=[
            {'use_sim_time': True},
        ],
        output='screen'
    )
    
    controllers_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_controller'), 'launch', PythonExpression(['"', robot_model, '.launch.py"']) ]),
        ),
        launch_arguments={
            'robot_name': robot_name
        }.items()
    )

    
    return LaunchDescription([
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('robot_name', default_value='transbot'),        
        DeclareLaunchArgument('x', default_value='0.0'),
        DeclareLaunchArgument('y', default_value='0.0'),
        DeclareLaunchArgument('z', default_value='0.1'),
        DeclareLaunchArgument('R', default_value='0.0'),
        DeclareLaunchArgument('P', default_value='0.0'),
        DeclareLaunchArgument('Y', default_value='0.0'),
        rsp_launch,
        spawn_node,
        ground_truth_bridge,
        controllers_launch
    ])
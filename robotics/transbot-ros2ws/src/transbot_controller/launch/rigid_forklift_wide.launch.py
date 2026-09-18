
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
    
    joint_state_publisher = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=['joint_state_broadcaster']
    )
    
    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=['diff_drive_controller']
    )
    
    twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        name='twist_mux',
        namespace=LaunchConfiguration('robot_name'),
        parameters=[
            PathJoinSubstitution([
                FindPackageShare('transbot_controller'), 'config', 
                PythonExpression(['"', robot_model, '.yaml"'])
            ]),
        ],
        remappings=[('cmd_vel_out', 'diff_drive_controller/cmd_vel')]
    )
 
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('robot_model', default_value='mobilebase_diffdrive_6wheels_ltype'),
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        joint_state_publisher,
        diff_drive_controller,
        twist_mux
    ])
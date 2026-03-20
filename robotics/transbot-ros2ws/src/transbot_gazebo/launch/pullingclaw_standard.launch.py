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
    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=['diff_drive_controller']
    )
    
    manipulator_controller = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=['manipulator_pid_velocity_controller']
    )
    
    teleop_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_teleop'), 'launch', 'teleop.launch.py' ]), # PythonExpression(['"', robot_model, '.launch.py"'])
        ),
        launch_arguments={
            'robot_name': LaunchConfiguration('robot_name')
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('robot_model', default_value='pullingclaw_standard'),
        diff_drive_controller,
        manipulator_controller,
        teleop_launch,
    ])
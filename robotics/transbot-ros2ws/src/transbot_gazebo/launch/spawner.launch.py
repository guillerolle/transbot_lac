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
            '-allow_renaming', 'true'
        ]
    )

    
    return LaunchDescription([
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        rsp_launch,
        spawn_node
    ])
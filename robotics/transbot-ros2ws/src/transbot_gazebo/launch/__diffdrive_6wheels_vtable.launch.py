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
    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'world.launch.py']),
        ),
        launch_arguments={
            'world': 'deepseek',
            'headless': 'false',
        }.items()
    )
    
    transbot_rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_description'), 'launch', 'robot_state_publisher.launch.py']),
        ),
        launch_arguments={
            'robot_name': 'transbot',
            'robot_model': 'diffdrive_6wheels_vtable',
            'robot_pkg': 'transbot_gazebo'
        }.items()
    )

    
    return LaunchDescription([
        world_launch,
        transbot_rsp
    ])
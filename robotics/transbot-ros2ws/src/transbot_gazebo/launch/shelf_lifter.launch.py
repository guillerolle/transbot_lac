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
        passive_spawn
    ])
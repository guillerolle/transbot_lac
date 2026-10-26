#!/bin/env python3
# coding: utf-8

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    slam_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('slam_toolbox'), 'launch', 'online_async_launch.py']),
        ),
        launch_arguments={
            'slam_params_file': PathJoinSubstitution([
                FindPackageShare('transbot_localization'), 'config', 'slam.yaml'
            ]),
            'use_sim_time': LaunchConfiguration('use_sim_time'),
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        slam_node,
    ])
    

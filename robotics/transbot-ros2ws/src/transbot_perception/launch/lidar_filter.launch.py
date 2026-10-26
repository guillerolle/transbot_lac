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
    lidar_filter = Node(
        package='laser_filters',
        executable='scan_to_scan_filter_chain',
        name='lidar_filter',
        namespace=LaunchConfiguration('robot_name'),
        remappings=[
            ('scan_in', 'scan'),
            ('scan_out', 'scan_filtered'),
        ],
        parameters=[
            PathJoinSubstitution([
                FindPackageShare('transbot_perception'),
                'config',
                'lidar_filter.yaml'
            ]),
            {'use_sim_time': LaunchConfiguration('use_sim_time')}, 
        ]
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        lidar_filter,
    ])
    

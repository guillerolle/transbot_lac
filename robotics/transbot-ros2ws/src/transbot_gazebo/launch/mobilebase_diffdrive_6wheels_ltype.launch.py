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
    
    # controller_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         PathJoinSubstitution([
    #             FindPackageShare('transbot_controller'), 'launch', LaunchConfiguration('robot_model'), 
    #             PythonExpression(['"', LaunchConfiguration('robot_model'), '.launch.py"'])
    #         ])
    #     )
    # )
    spawn_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'spawner.launch.py']),
        ),
        launch_arguments={
            'robot_name': robot_name,
            'robot_model': robot_model,
            'robot_pkg': robot_pkg,
        }.items()
    )
    
    controllers_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_controller'), 'launch', PythonExpression(['"', robot_model, '.launch.py"']) ]),
        ),
        launch_arguments={
            'robot_name': robot_name
        }.items()
    )
    
    # controller_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         PathJoinSubstitution([
    #             FindPackageShare('transbot_controller'), 'launch', 'differential_drive_controller.launch.py'
    #         ])
    #     ),
    #     launch_arguments={
    #         'controller_config': 'mobilebase_diffdrive_6wheels_ltype.yaml'
    #     }.items()
    # )
   
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
            'robot_model': 'movingshelf_4wheels',
            'robot_pkg': 'transbot_gazebo',
            'y': '2.0',
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('robot_model', default_value='mobilebase_diffdrive_6wheels_ltype'),
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        spawn_launch,
        controllers_launch,
        teleop_launch,
        passive_spawn
    ])
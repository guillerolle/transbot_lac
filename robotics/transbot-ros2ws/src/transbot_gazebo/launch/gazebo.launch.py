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
    
    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'world.launch.py']),
        ),
        launch_arguments={
            # 'gz_args': '-r empty.sdf --physics-engine gz-physics-bullet-featherstone-plugin'
            'gz_args': '-r',
            'world': LaunchConfiguration('world')
            # 'robot_name': robot_name,
            # 'robot_model': robot_model,
            # 'robot_pkg': robot_pkg,
        }.items()
    )
    
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
    
    joint_state_publisher_spawner = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=['joint_state_broadcaster']
    )
    
    controllers_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', PythonExpression(['"', robot_model, '.launch.py"']) ]),
        ),
        launch_arguments={
            'robot_name': robot_name
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_pkg', default_value='transbot_gazebo'),
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('world', default_value='transbot_gazebo/worlds/empty.sdf'),
        world_launch,
        spawn_launch,
        joint_state_publisher_spawner,
        controllers_launch
    ])
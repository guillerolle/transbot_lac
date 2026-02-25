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
    # Declare Arguments
    declare_gz_args = DeclareLaunchArgument('gz_args', default_value='',
                              description='Arguments to be passed to Gazebo Sim')
    
    declare_world = DeclareLaunchArgument('world', default_value='',description='Gazebo world to load')
    
    gz_args = PythonExpression([
        '"', LaunchConfiguration('gz_args'), ' ', LaunchConfiguration('world'), '"'
    ])
    
    # Paths  
    pkg_ros_gz_sim = FindPackageShare(package='ros_gz_sim')
    
    # Gazebo launch 
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'])
        ),
        launch_arguments={
                          'gz_args': gz_args,
                          }.items()
    )
    
    # ROS-GZ Bridge
    # Bridge for /clock (required for ros2_control)
    clock_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )
    
    return LaunchDescription([
        declare_gz_args,
        declare_world,
        gazebo_launch,
        clock_bridge
    ])
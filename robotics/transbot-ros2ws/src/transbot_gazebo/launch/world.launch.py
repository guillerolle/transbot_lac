#!/bin/env python3
# coding: utf-8

import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.logging import logging


def generate_launch_description():
    # Declare Arguments
    declare_gz_args = DeclareLaunchArgument('gz_args', default_value='',
                              description='Other arguments to be passed to Gazebo Sim')
    
    gz_args_list = ['"']
    gz_args_list.append(
        PythonExpression(["'-r ' if '", LaunchConfiguration('running'), "' == 'true' else ''"])
    )
    gz_args_list.append(
        PythonExpression(["'-s ' if '", LaunchConfiguration('headless'), "' == 'true' else ''"])
    )
    gz_args_list.extend(['transbot_gazebo/worlds/', LaunchConfiguration('world'), '.sdf '])
    gz_args_list.append('"')
    
    gz_args = PythonExpression(gz_args_list)
    
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
        name='ros_gz_clock_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock'],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )
            
    return LaunchDescription([
        DeclareLaunchArgument('running', default_value='true', choices=['true', 'false'],
                              description='Run simulation at start (true) or not (false)'),
        DeclareLaunchArgument('world', default_value='empty',description='Gazebo world to load'),
        DeclareLaunchArgument('headless', default_value='false', choices=['true', 'false'],
                              description='Run Gazebo in headless mode'),
        declare_gz_args,
        gazebo_launch,
        clock_bridge
    ])
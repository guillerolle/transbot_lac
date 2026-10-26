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
    robot_name = LaunchConfiguration('robot_name')
    gz_headless = LaunchConfiguration('gz_headless')
    rviz = LaunchConfiguration('rviz')
    rqt = LaunchConfiguration('rqt')
    
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_gazebo'), 'launch', 'shelf_lifter.launch.py']),
        ),
        launch_arguments={
            'robot_name': robot_name,
            'headless': gz_headless,
            'world': 'warehouse',
        }.items()
    )
    
    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_description'), 'launch', 'rviz.launch.py']),
        ),
        launch_arguments={
            'use_sim_time': 'true',
        }.items(),
        condition=IfCondition(rviz)
    )
    
    rqt_node = Node(
        package='rqt_gui',
        executable='rqt_gui',
        name='rqt',
        parameters=[{'use_sim_time': True}],
        condition=IfCondition(rqt),
    )
    
    teleop_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_teleop'), 'launch', 'teleop.launch.py' ]), # PythonExpression(['"', robot_model, '.launch.py"'])
        ),
        launch_arguments={
            'robot_name': robot_name,
        }.items()
    )
    
    teleop_delayed = TimerAction(
        period=5.0,
        actions=[teleop_launch]
    )
    
    lidar_filter = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_perception'), 'launch', 'lidar_filter.launch.py']),
        ),
        launch_arguments={
            'robot_name': robot_name,
            'use_sim_time': 'true',
        }.items()
    )
    
    lidar_filter_delayed = TimerAction(
        period=5.0,
        actions=[lidar_filter]
    )
    
    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('transbot_localization'), 'launch', 'slam.launch.py']),
        ),
        launch_arguments={
            'use_sim_time': 'true',
        }.items()
    )
    
    slam_delayed = TimerAction(
        period=5.0,
        actions=[slam]
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('gz_headless', default_value='true',
                              description='Run Gazebo without GUI'),
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Launch Rviz'),
        DeclareLaunchArgument('rqt', default_value='true',
                              description='Launch rqt'),
        gazebo_launch,
        rviz_launch,
        rqt_node,
        teleop_delayed,
        lidar_filter_delayed,
        slam_delayed,
    ])
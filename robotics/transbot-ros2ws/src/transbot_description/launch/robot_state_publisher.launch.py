#!/bin/env python3
# coding: utf-8

from ament_index_python.packages import get_package_share_directory

from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node 
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_name = LaunchConfiguration('robot_name')
    robot_model = LaunchConfiguration('robot_model')
    robot_basemodel = PythonExpression(['"', robot_model, '"', '.split("/")[-1]'])
    
    robot_urdf = PathJoinSubstitution([
        FindPackageShare(LaunchConfiguration('robot_pkg')),
        'urdf',
        robot_model,
        PythonExpression(['"', robot_basemodel, '.urdf.xacro','"']), 
    ])
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_pkg', default_value='transbot_description'),
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=robot_name,
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', robot_urdf]),
                'frame_prefix': [robot_name, '/']
            }],
            # remappings=[('tf', '/tf'),
            #             ('tf_static', '/tf_static')],
        )
    ])
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
        PythonExpression(['"__all__.urdf.xacro','"']), 
    ])
    
    ## For Gazebo Controller Manager Plugin ##
    control_config_list = [' ros2_control_dict:=', LaunchConfiguration('control_config')] if LaunchConfiguration('control_config') else []
    control_pkg_list    = [' ros2_control_pkg:=',  LaunchConfiguration('control_pkg')]    if LaunchConfiguration('control_pkg')    else []

    return LaunchDescription([
        DeclareLaunchArgument('robot_pkg', default_value='transbot_description'),
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('control_config', default_value=''),
        DeclareLaunchArgument('control_pkg', default_value=''),
        
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=robot_name,
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro "', robot_urdf, 
                                              '" ros2_control_namespace:=/', robot_name,
                                              *control_config_list,
                                              *control_pkg_list]),
                'frame_prefix': [robot_name, '/'],
            }],
            # remappings=[('tf', '/tf'),
            #             ('tf_static', '/tf_static')],
        )
    ])
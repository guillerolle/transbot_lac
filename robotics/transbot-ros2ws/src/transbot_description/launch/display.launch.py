#!/bin/env python3
# coding: utf-8

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, EmitEvent, IncludeLaunchDescription, RegisterEventHandler, Shutdown
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node 

def generate_launch_description():    
    robot_name = LaunchConfiguration('robot_name')
    
    rviz_config = get_package_share_directory('transbot_description') + '/rviz/display.rviz'
    
    robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('transbot_description'), 'launch', 'robot_state_publisher.launch.py')
        ),
        launch_arguments={
            'robot_name': robot_name
        }.items()
    )
    
    # RViz
    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('transbot_description'), 'launch', 'rviz.launch.py')
        )
    )
    
    # --- Event Handler for RViz exit ---
    # This handler listens for the rviz_node process to exit.
    # When it does, it emits a Shutdown event, which stops the entire launch.
    # shutdown_on_rviz_exit = RegisterEventHandler(
    #     OnProcessExit(
    #         target_action=rviz_node,
    #         on_exit=[
    #             Shutdown(reason='RViz window was closed')
    #         ]
    #     )
    # )
    
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen',
        namespace=robot_name
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_name',
            default_value='transbot',
            description='Name of the robot (used as namespace)'
        ),        
        rviz_launch,
        # shutdown_on_rviz_exit,
        robot_description_launch,
        joint_state_publisher_gui_node
    ])
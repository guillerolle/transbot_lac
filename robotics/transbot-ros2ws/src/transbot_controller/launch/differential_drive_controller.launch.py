#!/bin/env python3
# coding: utf-8

import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess, RegisterEventHandler, LogInfo
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    controller_manager_set_param = ExecuteProcess(
        cmd=[
           'ros2', 'param', 'set', 
           PythonExpression(['"/',LaunchConfiguration('robot_name'), '/', LaunchConfiguration('controller_manager'),'"']),
            PythonExpression(['"',LaunchConfiguration('controller_name'),'.type"']), LaunchConfiguration('controller_type')
        ],
    )
    
    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        namespace=LaunchConfiguration('robot_name'),
        arguments=[LaunchConfiguration('controller_name'), '--ros-args'],
        parameters=[PathJoinSubstitution([
            FindPackageShare('transbot_controller'), 'config', LaunchConfiguration('controller_config'),
        ]),
        ]
    )
    
    def _on_param_exit(event, context):
        if event.returncode == 0:
            return [diff_drive_controller]
        else:
            LogInfo(f"Controller type parameter couldn't be set. Skipping controller spawner...")
            return []
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),
        DeclareLaunchArgument('controller_manager', default_value='controller_manager'),
        DeclareLaunchArgument('controller_name', default_value='diff_drive_controller'),
        DeclareLaunchArgument('controller_type', default_value='diff_drive_controller/DiffDriveController'),
        DeclareLaunchArgument('controller_config', default_value='ros2_control.yaml'),
        controller_manager_set_param,
        RegisterEventHandler(
            OnProcessExit(
                target_action=controller_manager_set_param,
                on_exit=_on_param_exit,
            )    
        ),
    ])
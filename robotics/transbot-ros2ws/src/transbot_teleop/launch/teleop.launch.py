from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = FindPackageShare('transbot_teleop')
    
    # Paths to config files
    # base_config = os.path.join(pkg_share, 'config', 'base_teleop.yaml')
    joint_config = PathJoinSubstitution([pkg_share, 'config', 'joint_teleop.yaml'])
    
    joint_teleop_node = Node(
        package='transbot_teleop',
        executable='joint_teleop_joy',
        name='joint_teleop_joy',
        parameters=[joint_config],
        output='screen'
    )
    
    twist_teleop_joy_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare('teleop_twist_joy'), 'launch', 'teleop-launch.py']),
        ),
        launch_arguments={
            'joy_vel': PythonExpression(['"/', LaunchConfiguration('robot_name'), '/diff_drive_controller/cmd_vel"']),
            'publish_stamped_twist': 'true'
        }.items()
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'),    
        twist_teleop_joy_launch,
        joint_teleop_node,
    ])
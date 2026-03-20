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
    joint_config = PathJoinSubstitution([pkg_share, 'config', LaunchConfiguration('robot_model'), 'teleop.yaml'])
    
    joint_teleop_node = Node(
        package='transbot_teleop',
        executable='joint_teleop_joy',
        name='joint_teleop_joy',
        namespace=LaunchConfiguration('robot_name'),
        parameters=[joint_config],
        output='screen'
    )
    
    twist_joy_node = Node(
        package='teleop_twist_joy', executable='teleop_node', name='teleop_twist_joy_node',
        namespace=LaunchConfiguration('robot_name'),
        parameters=[joint_config],
        remappings={('cmd_vel', PythonExpression(['"/', LaunchConfiguration('robot_name'), '/diff_drive_controller/cmd_vel"']))},
    )
    
    joy_node = Node(
        package='joy', executable='joy_node', name='joy_node',
        namespace=LaunchConfiguration('robot_name'),
        parameters=[{
            'device_id': LaunchConfiguration('joy_dev'),
            'deadzone': LaunchConfiguration('joy_deadzone'),
            'autorepeat_rate': LaunchConfiguration('joy_autorepeat_rate'),
        }]
    )

    return LaunchDescription([
        DeclareLaunchArgument('robot_name', default_value='transbot'), 
        DeclareLaunchArgument('robot_model', default_value='rigid_forklift'),
        DeclareLaunchArgument('joy_dev', default_value='0'),
        DeclareLaunchArgument('joy_deadzone', default_value='0.0'),
        DeclareLaunchArgument('joy_autorepeat_rate', default_value='20.0'),
        joy_node,
        twist_joy_node,
        joint_teleop_node,
    ])

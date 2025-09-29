from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=[
                '--x', '0', '--y', '0', '--z', '0',
                '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
                '--frame-id', 'map', '--child-frame-id', 'cloud'
            ]
        ),
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            parameters=[{
                'target_frame': 'base_link',
                'transform_tolerance': 0.01,
                'min_height': -0.20,
                'max_height': 0.20,
                'angle_min': -3.141592654,  # -M_PI/2
                'angle_max': 3.141592654,  # M_PI/2
                'angle_increment': 0.008726646,  # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 0.5,
                'range_max': 40.0,
                'use_inf': False,
                'inf_epsilon': 0.05
            }],
            name='pointcloud_to_laserscan'
        )
    ])

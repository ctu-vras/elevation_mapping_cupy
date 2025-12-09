from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node, SetParameter
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node, SetParameter
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    rviz_config = os.path.join("/media/robot/data/nav2.rviz")
    bag_launch_path = os.path.join("/media/robot/data/helhest_2025_07_09-17_02_48/helhest_2025_07_09-17_02_48_0.mcap")

    return LaunchDescription([

        ExecuteProcess(
             cmd=['ros2', 'bag', 'play', bag_launch_path,
                  '--clock', '--rate', '0.5',
                  '--start-offset', '0.0'],
        ),

        # Uncompress images for stereo_image_rect and remap to expected names from stereo_image_proc
        
        # LR FRONT

        Node(
            package='image_transport', executable='republish', name='republish_rgb', output='screen',
            namespace='luxonis/oak',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'left/image_raw/compressed'),
                        ('out', 'left/image_raw')]),
        Node(
            package='image_transport', executable='republish', name='republish_rgb2', output='screen',
            namespace='luxonis/oak',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'right/image_raw/compressed'),
                        ('out', 'right/image_raw')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo', output='screen',
            namespace='luxonis/oak',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'stereo/image_raw/compressedDepth'),
                        ('out', 'stereo/image_raw')]),


        # SR FRONT

        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_front', output='screen',
            namespace='luxonis_tof_front/tof_front',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'left/image_rect/compressed'),
                        ('out', 'left/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_front2', output='screen',
            namespace='luxonis_tof_front/tof_front',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'right/image_rect/compressed'),
                        ('out', 'right/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_front', output='screen',
            namespace='luxonis_tof_front/tof_front',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'stereo/image_raw/compressedDepth'),
                        ('out', 'stereo/image_raw')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_front_tof', output='screen',
            namespace='luxonis_tof_front/tof_front',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'tof/image_raw/compressedDepth'),
                        ('out', 'tof/image_raw')]),


        # SR RIGHT

        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_right', output='screen',
            namespace='luxonis_tof_right/tof_right',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'left/image_rect/compressed'),
                        ('out', 'left/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_right2', output='screen',
            namespace='luxonis_tof_right/tof_right',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'right/image_rect/compressed'),
                        ('out', 'right/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_right', output='screen',
            namespace='luxonis_tof_right/tof_right',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'stereo/image_raw/compressedDepth'),
                        ('out', 'stereo/image_raw')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_right_tof', output='screen',
            namespace='luxonis_tof_right/tof_right',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'tof/image_raw/compressedDepth'),
                        ('out', 'tof/image_raw')]),


        # SR LEFT

        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_left', output='screen',
            namespace='luxonis_tof_left/tof_left',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'left/image_rect/compressed'),
                        ('out', 'left/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_rgb_sr_left2', output='screen',
            namespace='luxonis_tof_left/tof_left',
            parameters=[{
                'in_transport': 'compressed',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressed', 'right/image_rect/compressed'),
                        ('out', 'right/image_rect')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_left', output='screen',
            namespace='luxonis_tof_left/tof_left',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'stereo/image_raw/compressedDepth'),
                        ('out', 'stereo/image_raw')]),
        Node(
            package='image_transport', executable='republish', name='republish_stereo_sr_left_tof', output='screen',
            namespace='luxonis_tof_left/tof_left',
            parameters=[{
                'in_transport': 'compressedDepth',
                'out_transport': 'raw',
            }],
            remappings=[('in/compressedDepth', 'tof/image_raw/compressedDepth'),
                        ('out', 'tof/image_raw')]),



        Node(
            package='depth_image_proc', executable='point_cloud_xyz_radial_node', name='stereo2pcd', output='screen',
            remappings=[("depth/image_raw", "/luxonis/oak/stereo/image_raw"),
                        ("depth/camera_info", "/luxonis/oak/stereo/camera_info"),
                        ("points", "points/filtered")]),
        Node(
            package='depth_image_proc', executable='point_cloud_xyz_radial_node', name='stereo2pcdsrfront', output='screen',
            remappings=[("depth/image_raw", "/luxonis_tof_front/tof_front/stereo/image_raw"),
                        ("depth/camera_info", "/luxonis_tof_front/tof_front/stereo/camera_info"),
                        ("points", "points/filtered/sr_front")]),
        Node(
            package='depth_image_proc', executable='point_cloud_xyz_radial_node', name='stereo2pcdsrleft', output='screen',
            remappings=[("depth/image_raw", "/luxonis_tof_left/tof_left/stereo/image_raw"),
                        ("depth/camera_info", "/luxonis_tof_left/tof_left/stereo/camera_info"),
                        ("points", "points/filtered/sr_left")]),
        Node(
            package='depth_image_proc', executable='point_cloud_xyz_radial_node', name='stereo2pcdsrright', output='screen',
            remappings=[("depth/image_raw", "/luxonis_tof_right/tof_right/stereo/image_raw"),
                        ("depth/camera_info", "/luxonis_tof_right/tof_right/stereo/camera_info"),
                        ("points", "points/filtered/sr_right")]),

        
        # Node(
        #     package='image_transport', executable='republish', name='republish_rgb', output='screen',
        #     namespace='luxonis/oak',
        #     parameters=[{
        #         'in_transport': 'compressed',
        #         'out_transport': 'raw',
        #     }],
        #     remappings=[('in/compressed', 'rgb/image_raw/compressed'),
        #                 ('out', 'rgb/image_raw')]),
        # Node(
        #     package='image_transport', executable='republish', name='republish_stereo', output='screen',
        #     namespace='luxonis/oak',
        #     parameters=[{
        #         'in_transport': 'compressedDepth',
        #         'out_transport': 'raw',
        #     }],
        #     remappings=[('in/compressed', 'stereo/image_raw/compressedDepth'),
        #                 ('out', 'stereo/image_raw')]),
        # Node(
        #     package='image_transport', executable='republish', name='republish_stereo2', output='screen',
        #     namespace='luxonis_tof_left/tof_left',
        #     parameters=[{
        #         'in_transport': 'compressedDepth',
        #         'out_transport': 'raw',
        #     }],
        #     remappings=[('in/compressed', 'stereo/image_raw/compressedDepth'),
        #                 ('out', 'stereo/image_raw')]),
        # Node(
        #     package='image_transport', executable='republish', name='republish_stereo3', output='screen',
        #     namespace='luxonis_tof_right/tof_right',
        #     parameters=[{
        #         'in_transport': 'compressedDepth',
        #         'out_transport': 'raw',
        #     }],
        #     remappings=[('in/compressed', 'stereo/image_raw/compressedDepth'),
        #                 ('out', 'stereo/image_raw')]),
        Node(
             package='rviz2',
             executable='rviz2',
             name='rviz2',
             arguments=['-d', rviz_config],
        )
    ])

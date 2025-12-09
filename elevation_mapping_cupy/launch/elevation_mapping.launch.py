import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.conditions import IfCondition

def generate_launch_description():
    package_name = 'elevation_mapping_cupy'
    share_dir = get_package_share_directory(package_name)

    # Define paths
    core_param_path = os.path.join(share_dir, 'config', 'core', 'core_param.yaml')

    # Declare launch arguments
    robot_param_arg = DeclareLaunchArgument(
        'robot_config',
        # default_value='turtle_bot/turle_bot_simple.yaml',
        default_value='helhest/base.yaml',
        description='Name of the robot-specific config file within config/setups/'
    )
    

    launch_rviz_arg = DeclareLaunchArgument(
        'launch_rviz',
        default_value='false',
        description='Whether to launch RViz'
    )

    rviz_config_arg = DeclareLaunchArgument(
        'rviz_config',
        default_value='',
        description='Path to the RViz config file'
    )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation clock if true'
    )

    # Get launch configurations
    robot_config = LaunchConfiguration('robot_config')
    robot_param_path = PathJoinSubstitution([share_dir, 'config', 'setups', robot_config])
    launch_rviz = LaunchConfiguration('launch_rviz')
    rviz_config = LaunchConfiguration('rviz_config')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Verify core config exists
    if not os.path.exists(core_param_path):
        raise FileNotFoundError(f"Config file {core_param_path} does not exist")

    # Define nodes
    elevation_mapping_node = Node(
        package=package_name,
        executable='elevation_mapping_node',
        name='elevation_mapping_node',
        output='screen',
	respawn=True,
	respawn_delay=1.0,
        parameters=[
            core_param_path,
            robot_param_path,
            {'use_sim_time': use_sim_time}
        ],
    )

    # Log the resolved path at launch time
    print_path_action = LogInfo(msg=['Resolved robot param path: ', robot_param_path])
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen',
        condition=IfCondition(launch_rviz)
    )

    relay_front = Node(
        package='topic_tools',
        executable='relay',
        name='relay_front',
        arguments=['/livox/lidar_front', '/livox/lidar_both'],
        output='screen',
    )

    relay_rear = Node(
        package='topic_tools',
        executable='relay',
        name='relay_rear',
        arguments=['/livox/lidar_rear', '/livox/lidar_both'],
        output='screen',
    )

    return LaunchDescription([
        robot_param_arg,
        print_path_action,
        launch_rviz_arg,
        rviz_config_arg,
        use_sim_time_arg,
        elevation_mapping_node,
        rviz_node,
        #relay_front,
        #relay_rear
    ])

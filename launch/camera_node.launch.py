import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # Getting directories and launch-files
    depth_anything_dir = get_package_share_directory('camera_ros')
    default_params_file = os.path.join(depth_anything_dir, 'config', 'depth_camera_config.yaml')
    default_namespace = "camera"

    # Input parameters declaration
    params_file = LaunchConfiguration('params_file')
    namespace = LaunchConfiguration('namespace')

    declare_params_file_arg = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to desired camera_node config file NOTE: NOT camera calibration file'
    )
    
    declare_namespace_arg = DeclareLaunchArgument(
        'namespace',
        default_value=default_namespace,
        description='The namespace of the camera_node'
    )

    camera_node = Node(
        package="camera_ros",
        executable="camera_node",
        name=namespace,
        parameters=[
            params_file
        ],
    )

    return LaunchDescription([
        declare_params_file_arg,
        declare_namespace_arg,
        camera_node
    ])

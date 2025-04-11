from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    ld = LaunchDescription()

    urdf_tutorial_path = FindPackageShare('motoman_ma2010_support')
    default_model_path = PathJoinSubstitution(['urdf', 'ma2010.xacro'])

    # These parameters are maintained for backwards compatibility
    gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                    description='Flag to enable joint_state_publisher_gui')
    ld.add_action(gui_arg)

    # This parameter has changed its meaning slightly from previous versions
    ld.add_action(DeclareLaunchArgument(name='model', default_value=default_model_path,
                                        description='Path to robot urdf file'))

    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('motoman_ma2010_support'), 'launch', 'robot_state_visualize_ma2010.launch.py']),
        launch_arguments={
            'urdf_package': 'motoman_ma2010_support',
            'urdf_package_path': LaunchConfiguration('model'),
            'jsp_gui': LaunchConfiguration('gui')}.items()
    ))

    return ld

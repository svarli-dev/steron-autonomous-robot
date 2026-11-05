import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction 
from launch_ros.actions import Node


def generate_launch_description():
    world_file = os.path.expanduser(
        '~/steron-autonomous-robot/simulation/worlds/steron_world.sdf'
    )

    robot_file = os.path.expanduser(
    '~/steron-autonomous-robot/simulation/test_assets/steron_robot.sdf'
    )


    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            '-v',
            '3',
            '-r',
            world_file,
            '--render-engine',
            'ogre'
        ],
        output='screen'
        )
    
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'steron_world',
            '-file', robot_file,
            '-name', 'steron_diffdrive_test',
            '-x', '0',
            '-y', '0',
            '-z', '0.25'
        ],
        output='screen'
    )

    cmd_vel_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist'
        ],
        output='screen'
    )

    odom_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/model/steron_diffdrive_test/odometry@nav_msgs/msg/Odometry[ignition.msgs.Odometry'
        ],
        output='screen'
    )

    odometry_monitor = Node(
        package='steron_control',
        executable='odometry_monitor',
        output='screen'
    )
    

    return LaunchDescription([
        gazebo,
        cmd_vel_bridge,
        odom_bridge,
        odometry_monitor,
        TimerAction(
            period=5.0,
            actions=[spawn_robot]
        )
    ])


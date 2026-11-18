import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class ClosedLoopController(Node):

    def __init__(self):
        super().__init__('steron_closed_loop_controller')

         # Output: velocity publisher

        self.initial_x = None

        self.latest_x = None
        self.latest_y = None

        self.target_distance = 2.0
        self.tolerance = 0.05

        self.kp = 0.5

        self.max_speed = 0.2
        self.done = False

        # Control loop: 10 Hz (100 ms)
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.odom_subscriber = self.create_subscription(
            Odometry,
            '/model/steron_diffdrive_test/odometry',
            self.odom_callback,
            10
        )

        # Control loop: 10 Hz (100 ms)
        self.control_timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.get_logger().info('/cmd_vel command started.')

    def odom_callback(self, msg):

        self.latest_x = msg.pose.pose.position.x
        self.latest_y = msg.pose.pose.position.y

        if self.initial_x is None:
            self.initial_x = self.latest_x

    def timer_callback(self):

        if self.latest_x is None:
            return

        if self.initial_x is None:
            return

        if self.done:
            return


        distance_taken = self.latest_x - self.initial_x
        remaining_distance = self.target_distance - distance_taken

        self.get_logger().info(
            f'Distance taken: {distance_taken: .3f} m'
        )

        if remaining_distance <= self.tolerance:

            stop_msg = Twist()
            stop_msg.linear.x = 0.0
            stop_msg.angular.z = 0.0

            self.cmd_vel_publisher.publish(stop_msg)
            self.done = True

        else:

            move_msg = Twist()

            move_msg.linear.x = min(
                self.kp * remaining_distance,
                self.max_speed
            )

            move_msg.angular.z = 0.0

            self.cmd_vel_publisher.publish(move_msg)



def main(args=None):

    rclpy.init(args=args)

    node = ClosedLoopController()

    try:
        rclpy.spin(node)

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()
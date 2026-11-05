import rclpy
from rclpy.node import Node 
from rclpy.executors import ExternalShutdownException 
from nav_msgs.msg import Odometry 

class OdometryMonitor(Node):

    def __init__(self):
        super().__init__('steron_odometry_monitor')

        # Last known robot pozition
        self.latest_x = 0.0
        self.latest_y = 0.0

        # Odometry subscriber
        self.odom_subscriber = self.create_subscription(
            Odometry, 
            '/model/steron_diffdrive_test/odometry',
            self.odom_callback,
            10
        )

        # The timer works per a second
        self.log_timer = self.create_timer(
            1.0,
            self.timer_callback
        )

        self.get_logger().info('Odometry monitor started.')

    def odom_callback(self, msg):

        self.latest_x = msg.pose.pose.position.x
        self.latest_y = msg.pose.pose.position.y 

    def timer_callback(self):

        self.get_logger().info(
            f'Robot pozition: X={self.latest_x:.3f} m, '
            f'Y={self.latest_y:.3f} m'
        )


def main(args=None):

    rclpy.init(args=args)

    node = OdometryMonitor()

    try:
        rclpy.spin(node)

    except (KeyboardInterrupt, ExternalShutdownException):
        pass

    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()


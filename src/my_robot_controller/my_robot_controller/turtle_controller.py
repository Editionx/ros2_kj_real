#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init__("Controller")
        self.get_logger().info("ERROR: it works")

        self._pose_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self._pose_listener = self.create_subscription(Pose, "/turtle1/pose",
                                                        self.robot_controller, 10)

    def robot_controller(self,pose: Pose):
        msg = Twist()

        msg.linear.x = 2.0
        msg.angular.z = 2.0

        self._pose_publisher.publish(msg)
        self.get_logger().info("[ X = " + str(pose.x) + " Y = " + str(pose.y) + " ]")




def main (args=None):
    rclpy.init(args=args)

    node = TurtleControllerNode()

    rclpy.spin(node) #Node
    rclpy.shutdown()


#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1, self.timer_callback)
        self._counter = 0

    def timer_callback(self):
        self.get_logger().info("Helo " + str(self._counter))
        self._counter+= 1
 

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
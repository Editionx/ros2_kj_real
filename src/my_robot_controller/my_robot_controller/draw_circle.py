#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")

        self.count = 0

        self.x = [2.0, 2.0,  0.0, 2.0, 2.0,  0.0, 2.0, 2.0, 3.16, 2.0, 2.0]
        self.z = [2.0, 2.0, -2.0, 2.0, 2.0, -1.5, 0.0, 0.0, 3.16, 0.0, 0.0]
        self.sleep = 1

        self.vel_pub_cmd = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        #self._time = self.create_timer(0.5, self.send_velocity_command)
        self._time = self.create_timer(0.5, self.draw_cock)
        self.get_logger().info("Good fr fr")

    def send_velocity_command(self):
        msg = Twist()

        #msg.linear.x = 5000.0
        #msg.linear.y = 0.0
        #msg.angular.z = 10000.0

        self.get_logger().info("--------")
        self.get_logger().info(str(self.x) + "  "+ str(self.z))
        

        msg.linear.x = self.x
        msg.angular.z = self.z
        
        self.x += 2.5
        self.z += 5.0
        
        
        self.vel_pub_cmd.publish(msg)
    
    def draw_cock(self):
        msg = Twist()

        msg.linear.x = self.x[self.count]
        msg.angular.z = self.z[self.count]

        self.count += 1

        self.vel_pub_cmd.publish(msg)
        time.sleep(1)

def main(args=None):
    rclpy.init(args=args)

    node = DrawCircleNode()
    rclpy.spin(node)

    rclpy.shutdown


if __name__ == "__main__":
    main()
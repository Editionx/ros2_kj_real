#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from sensor_msgs.msg import LaserScan
import tf_transformations
import time

class TurtleNavigationNode(Node):
    
    def __init__(self):
        super().__init__("navgation")
        self.get_logger().info("ERROR: NAVIGATION WORKING")

        self.initial_pose_publisher = self.create_publisher(PoseWithCovarianceStamped, "/initialpose", 10)
        self.goal_pose_publisher = self.create_publisher(PoseStamped, "/goal_pose", 10)

        self.odom_listener = self.create_subscription(Odometry, "/odom",
                                                        self.robot_controller, 10)

        #------------------INITIAL------------------
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id =  "map"
        initial_pose.pose.pose.position.x = 0.0
        initial_pose.pose.pose.position.y = 0.0

        qq = tf_transformations.quaternion_from_euler(0,0,0)#x,y,z or roll pitch yaw
        initial_pose.pose.pose.orientation.x = qq[0]
        initial_pose.pose.pose.orientation.y = qq[1]
        initial_pose.pose.pose.orientation.z = qq[2]
        initial_pose.pose.pose.orientation.w = qq[3]
        self.initial_pose_publisher.publish(initial_pose)
        #--------------------------------------------
        #time.sleep(1)
        #------------------DESTINATION---------------
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.pose.position.x = 3.5
        goal.pose.position.y = 0.0

        qq = tf_transformations.quaternion_from_euler(0,0,1.57)#x,y,z or roll pitch yaw
        goal.pose.orientation.x = qq[0]
        goal.pose.orientation.y = qq[1]
        goal.pose.orientation.z = qq[2]
        goal.pose.orientation.w = qq[3]

        self.goal_pose_publisher.publish(goal)

    def robot_controller(self,scan: Odometry):
        pass



def main (args=None):
    rclpy.init(args=args)

    node = TurtleNavigationNode()

    rclpy.spin(node) #Node
    rclpy.shutdown()

if __name__ == "__main__":
    main()
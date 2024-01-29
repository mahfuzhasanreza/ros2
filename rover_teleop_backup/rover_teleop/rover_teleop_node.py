#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class RoverTeleopNode(Node):
    
    def __init__(self):
        super().__init__("rover_teleop_node")

        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self.joy_subscriber_ = self.create_subscription(
            Joy, "/joy", self.joy_callback, 10)
        
        self.get_logger().info("Rover teleop node has been started")
        self.enable = False
    
    def joy_callback(self, joy: Joy):
        cmd = Twist()

        # FOR FORWARD BACKWARD
        if(joy.axes[3] > 0):
            cmd.linear.x = joy.axes[3]
        if(joy.axes[3] < 0):
            cmd.linear.x = joy.axes[3]
        
        # FOR LEFT RIGHT
        if(joy.axes[2] > 0):
            cmd.angular.z = joy.axes[2]
        if(joy.axes[2] < 0):
            cmd.angular.z = joy.axes[2]

        enable_button = joy.buttons[0]
        disable_button = joy.buttons[2]
        
        if(disable_button):
            self.enable = False
        elif(enable_button):
            self.enable = True

        if(self.enable):
            self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = RoverTeleopNode()
    rclpy.spin(node)
    rclpy.shutdown()
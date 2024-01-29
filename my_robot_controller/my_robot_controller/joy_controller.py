#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init__("joy_controller")

        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "/turtle1/cmd_vel", 10)
        self.joy_subscriber_ = self.create_subscription(
            Joy, "/joy", self.joy_callback, 10)
        
        self.get_logger().info("Joystick turtle controller has been started")
        self.enable = False
    
    def joy_callback(self, joy: Joy):
        cmd = Twist()

        cmd.linear.x = joy.axes[3]
        cmd.angular.z = joy.axes[2]

        disable_button = joy.buttons[2]
        enable_button = joy.buttons[0]
        
        if(disable_button):
            self.enable = False
        elif(enable_button):
            self.enable = True

        if(self.enable):
            self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()



# ------------------------------------------------------------------
# (Tested with main Joystic)



# #!/usr/bin/env python3
# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import Joy
# from geometry_msgs.msg import Twist

# class TurtleControllerNode(Node):
    
# def __init__(self):
#     super().__init__("joy_controller")
#     self.cmd_vel_publisher_ = self.create_publisher(
#         Twist, "/turtle1/cmd_vel", 10)
#     self.joy_subscriber_ = self.create_subscription(
#         Joy, "/joy", self.joy_callback, 10)
    
#     self.get_logger().info("Joystick turtle controller has been started")
#     self.count = 0
#     self.three_sixty_count = 1.2

# def joy_callback(self, joy: Joy):
#     cmd = Twist()
#     cmd.linear.x = joy.axes[1] + joy.axes[4]
#     cmd.angular.z = joy.axes[0] + joy.axes[3]
#     enable_button = joy.buttons[1]
    
#     if(enable_button == 1 and self.count == 0):
#         self.count = 1
#     elif(enable_button == 0 and self.count == 1):
#         self.count = 2
#     elif(enable_button == 1 and self.count == 2):
#         self.count = 3
#         elif(enable_button == 0 and self.count == 3):
#             self.count = 0
        
#         if(joy.buttons[8] == 1):
#             cmd.angular.z = self.three_sixty_count

#         if(joy.buttons[7] == 1):
#             if(self.three_sixty_count > 0):
#                 self.three_sixty_count = -self.three_sixty_count
#         if(joy.buttons[6] == 1):
#             if(self.three_sixty_count < 0):
#                 self.three_sixty_count = -self.three_sixty_count

#         if(joy.buttons[5] == 1):
#             cmd.linear.x = -1.99
#             cmd.angular.z = 0.45
#         if(joy.buttons[4] == 1):
#             cmd.linear.x = -1.99
#             cmd.angular.z = -0.45

#         if(joy.buttons[3] == 1):
#             cmd.linear.x = 1.2
#         if(joy.buttons[0] == 1):
#             cmd.linear.x = -1.2

#         if(self.count == 1 or self.count == 2):
#             self.cmd_vel_publisher_.publish(cmd)

# def main(args=None):
#     rclpy.init(args=args)
#     node = TurtleControllerNode()
#     rclpy.spin(node)
#     rclpy.shutdown()

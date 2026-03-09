#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from control_msgs.msg import DynamicJointState, InterfaceValue, MultiDOFCommand
import yaml
import math

class JointTeleopJoy(Node):
    def __init__(self):
        super().__init__('joint_teleop_joy')
        
        # Declare parameters
        self.declare_parameter('joy_topic', 'joy')
        self.declare_parameter('command_topic', 'joint_references')
        self.declare_parameter('enable_button', -1)  # -1 = no enable button
        self.declare_parameter('deadzone', 0.05)
        self.declare_parameter('dof_names', rclpy.Parameter.Type.STRING_ARRAY)
        self.dof_names = self.get_parameter('dof_names').value
        
        
        for d in self.dof_names:
            self.declare_parameter(f"{d}.axis", rclpy.Parameter.Type.INTEGER)
            try: 
                self.get_parameter(f"{d}.axis").value
            except:
                self.get_logger().error(f"No joint mappings provided for joint {d}!")
                return

            self.declare_parameter(f"{d}.scale", 1.0)
            self.declare_parameter(f"{d}.offset", 0.0)
            self.declare_parameter(f"{d}.invert", False)
                
        
        # Get parameters
        joy_topic = self.get_parameter('joy_topic').value
        cmd_topic = self.get_parameter('command_topic').value
        self.enable_btn = self.get_parameter('enable_button').value
        self.deadzone = self.get_parameter('deadzone').value
        
        
        # Publisher
        self.cmd_pub = self.create_publisher(MultiDOFCommand, cmd_topic, 10)
        
        # Subscriber to joy
        self.joy_sub = self.create_subscription(Joy, joy_topic, self.joy_callback, 10)
        
        # State: current axis values (initialized to 0.0)
        self.axes_values = [0.0] * 8  # assume up to 8 axes, will be resized if needed
        
        self.get_logger().info('Joint teleop node started. Enable button: %d' % self.enable_btn)
    
    def joy_callback(self, msg):
        # Store axes (extend list if needed)
        if len(msg.axes) > len(self.axes_values):
            self.axes_values.extend([0.0] * (len(msg.axes) - len(self.axes_values)))
        for i, val in enumerate(msg.axes):
            self.axes_values[i] = val
        
        # Check enable button
        if self.enable_btn >= 0:
            self.get_logger().debug(f"joy message received! buttons: {msg.buttons}", throttle_duration_sec=1.0)
            if len(msg.buttons) <= self.enable_btn or msg.buttons[self.enable_btn] == 0:
                # Button not pressed: publish zeros (or nothing)
                # We'll publish zeros to stop the joints
                self.publish_joint_commands(enable=False)
                return
        
        # Button pressed (or no button): compute commands
        self.publish_joint_commands(enable=True)
    
    def publish_joint_commands(self, enable=True):
        # Build DynamicJointState message
        msg = MultiDOFCommand()
        # msg.header.stamp = self.get_clock().now().to_msg()
        
        joint_names = []
        interface_values = []
        
        for d in self.dof_names:
            joint_name = d
            axis = self.get_parameter(f"{d}.axis").value
            scale = self.get_parameter(f"{d}.scale").value
            offset = self.get_parameter(f"{d}.offset").value
            invert = -1.0 if self.get_parameter(f"{d}.invert").value else 1.0
            
            # Get axis value, apply deadzone
            if axis < len(self.axes_values):
                raw = self.axes_values[axis]
            else:
                raw = 0.0
            
            if abs(raw) < self.deadzone:
                raw = 0.0
            
            # Compute reference
            if enable:
                ref = raw * scale * invert + offset
            else:
                ref = 0.0  # or keep last? safer to set zero when disabled
            
            # Append to message
            msg.dof_names.append(joint_name)
            msg.values.append(ref)
        
        # msg.dof_names = joint_names
        # msg.values = interface_values
        
        self.cmd_pub.publish(msg)
        self.get_logger().debug('Published joint commands: %s' % str(msg), throttle_duration_sec=1.0)

def main(args=None):
    rclpy.init(args=args)
    node = JointTeleopJoy()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
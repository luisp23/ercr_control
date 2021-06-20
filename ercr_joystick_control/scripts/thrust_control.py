import rospy

from ercr_msgs.msg import Thrust
from sensor_msgs.msg import Joy

class ThrustControl():

    def __init__(self) -> None:
    
        self.thrust_cntrol_pub = rospy.Publisher('/cmd_drive', Thrust, queue_size=1)
        self.joystick_cmd_sub = rospy.Subscriber("joy", Joy, self.joystick_cmd_callback)

        pub_rate = 100
        self.pos_timer = rospy.Timer(rospy.Duration(1.0/pub_rate), self.thrust_control_callback)

        self.thrust_setpoint = Thrust()

        self.joystick_cmd_left = 0.0
        self.joystick_cmd_right = 0.0


    
    def thrust_control_callback(self, timer):

        # TODO: Add stamp to message def in ercr_msgs + protobuf message def in ercr_gazebo
        #self.actuator_control_setpoint.header.stamp = rospy.get_rostime()
        
        self.thrust_setpoint.left = self.joystick_cmd_left
        self.thrust_setpoint.right = self.joystick_cmd_right
    
        self.thrust_cntrol_pub.publish(self.thrust_setpoint)


    def joystick_cmd_callback(self, joy_cmd):
       self.joystick_cmd_left = joy_cmd.axes[1]
       self.joystick_cmd_right = joy_cmd.axes[4]



if __name__ == '__main__':

    rospy.init_node('thrust_control', anonymous=True)
    rospy.loginfo('Running thrust_control node')
    
    thrust_control = ThrustControl()

    try:
        rospy.spin()

    except KeyboardInterrupt:
        pass

    finally:
        rospy.info('Shutting down!')

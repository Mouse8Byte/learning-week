# turtle_controller.py
#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# Node Output: Menerima perintah dan menggerakkan TurtleSim
def callback(data):
    rospy.loginfo(f"Received: {data.data}")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    twist = Twist()
    
    if data.data == 'w':
        twist.linear.x = 2.0
    elif data.data == 's':
        twist.linear.x = -2.0
    elif data.data == 'a':
        twist.angular.z = 2.0
    elif data.data == 'd':
        twist.angular.z = -2.0
    
    pub.publish(twist)

def output_node():
    rospy.init_node('output_node', anonymous=True)
    rospy.Subscriber('/turtle_commands', String, callback)
    rospy.spin()

if _name_ == '_main_':
    try:
        output_node()
    except rospy.ROSInterruptException:
        pass

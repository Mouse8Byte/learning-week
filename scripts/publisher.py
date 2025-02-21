#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import sys
import termios
import tty

# Node Input: Mengirim perintah ke topik /turtle_commands
def get_key():
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
    return key

def input_node():
    rospy.init_node('input_node', anonymous=True)
    pub = rospy.Publisher('/turtle_commands', String, queue_size=10)
    rate = rospy.Rate(10)
    
    print("Gunakan WASD untuk menggerakkan TurtleSim. Tekan Q untuk keluar.")
    while not rospy.is_shutdown():
        key = get_key()
        if key in ['w', 'a', 's', 'd']:
            rospy.loginfo(f"Sending command: {key}")
            pub.publish(key)
        elif key == 'q':
            break
        rate.sleep()

if _name_ == '_main_':
    try:
        input_node()
    except rospy.ROSInterruptException:
        pass

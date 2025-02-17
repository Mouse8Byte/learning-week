#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"Menerima pesan: {data.data}")  # Menampilkan pesan yang diterima

def listener():
    rospy.init_node('listener', anonymous=True)  # Inisialisasi node dengan nama 'listener'
    rospy.Subscriber('/chatter', String, callback)  # Subscribe ke topic 'chatter'

    rospy.spin()  # Looping agar tetap aktif

if __name__ == "__main__":
    listener()

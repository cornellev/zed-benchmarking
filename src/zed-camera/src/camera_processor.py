#!/usr/bin/env python

import rospy

from nav_msgs.msg import Odometry

"""
Simple (re)publisher of the ZED odometry, for testing purposes
"""
class CameraProcessor:
    
    def __init__(self):
        rospy.Subscriber("/zed/zed_node/odom", Odometry, self.read_odom)
        self.odom_pub = rospy.Publisher("camera_processor/odom", data_class=Odometry, queue_size=10)

    def read_odom(self, odom):
        self.odom_pub.publish(odom)


if __name__ == "__main__":
    rospy.init_node("camera_processor")

    cp = CameraProcessor()

    rospy.spin()
#!/usr/bin/env python

import rospy

from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped


class RunningAverage:
    def __init__(self):
        self.x_total = 0
        self.n = 0

    def get_average(self):
        return self.x_total / self.n
    
    def add_measurement(self, x): 
        self.x_total += x
        self.n += 1

    def reset(self):
        self.x_total = 0
        self.n = 0

class VarianceCalculator:
    
    def __init__(self):
        self.measurements = []
        self.average = RunningAverage()

    def add_sample (self, measurement,):
        self.measurements.append(measurement)
        self.average.add_measurement(measurement)

    def get_covariance(self):
        x_bar = self.average.get_average()
        return sum((x_i - x_bar)**2 for x_i in self.measurements) / len(self.measurements)

class CameraProcessor:
    
    def __init__(self):
        rospy.Subscriber("/zed/zed_node/odom", Odometry, self.read_odom)
        rospy.Subscriber("/zed/zed_node/pose", PoseStamped, self.read_pose)

    def read_odom(self, odom):
        pass

    def read_pose(self, odom):
        pass


if __name__ == "__main__":
    rospy.init_node("camera_processor")

    cp = CameraProcessor()

    rospy.spin()
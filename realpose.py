#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from sensor_msgs.msg import Joy, Range
import sys
import json
from collections import deque
import time

def lidar_pose(data):
        global x
        global y
        global z
        global rx
        global ry
        global rz
        global rw
        global seq

        pose = PoseStamped()
        pub = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=1)

        print("x=",x)
        print("y=",y)
        print("z=",z)

        pose.header.frame_id = "map"
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = data.range-0.08
        pose.pose.orientation.x = rx
        pose.pose.orientation.y = ry
        pose.pose.orientation.z = rz
        pose.pose.orientation.w = rw

        print("ha ho raha hai")

        for j in range(17):
#                seq=seq+1
#                pose.header.seq = seq
                pub.publish(pose)

def callback(data):
        global x
        global y
        global z
        global rx
        global ry
        global rz
        global rw
        global seq

        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        z = data.pose.pose.position.z
        rx = data.pose.pose.orientation.x
        ry = data.pose.pose.orientation.y
        rz = data.pose.pose.orientation.z
        rw = data.pose.pose.orientation.w

if __name__ == '__main__':
        global x
        global y
        global z
        global rx
        global ry
        global rz
        global rw
        global seq
        x = 0.0
        y = 0.0
        z = 0.0
        rx = 0.0
        ry = 0.0
        rz = 0.0
        rw = 0.0
        seq = 0

        rospy.init_node('vision_pose')
        vision_p = PoseStamped()
        msg = Odometry()
        i=0

        try:
                while not rospy.is_shutdown():

                    msg = rospy.Subscriber('/tag_Odometry', Odometry, callback)
                    msg = rospy.Subscriber('/mavros/distance_sensor/rangefinder_pub', Range, lidar_pose)
                    rospy.spin()
                    print(i)
                    i=i+1

        except rospy.ROSInterruptException:
                pass


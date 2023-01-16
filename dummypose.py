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
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "map"
        pose.pose.position.x = 0
        pose.pose.position.y = 0
        pose.pose.position.z = data.range
        pose.pose.orientation.x = 0
        pose.pose.orientation.y = 0
        pose.pose.orientation.z = 0
        pose.pose.orientation.w = 1
        pose.header.seq = int(data.header.seq)
        # pose.header.seq = int(seq)
        # seq=seq+1

        # if (xAnt != pose.pose.position.x and yAnt != pose.pose.position.y):
        #         pose.header.seq = path.header.seq + 1
        #         path.header.frame_id = "main"
        #         path.header.stamp = rospy.Time.now()
        #         pose.header.stamp = path.header.stamp
        #         path.poses.append(pose)
                # Published the msg

        # cont = cont + 1

        # rospy.loginfo("Hit: %i" % cont)
        # if cont > max_append:
                # path.poses.pop(0)
        print("ha ho raha hai")
        pub.publish(pose)



if __name__ == '__main__':
        # Initializing global variables

        # Initializing node
        rospy.init_node('vision_pose')

        # Rosparams set in the launch (can ignore if running directly from bag)
        # max size of array pose msg from the path


        vision_p = PoseStamped() 
        msg = Odometry()

        # Subscription to the required odom topic (edit accordingly)
        i=0

        rate = rospy.Rate(10)  # 30hz

        try:
                while not rospy.is_shutdown():

                    msg = rospy.Subscriber('/mavros/distance_sensor/rangefinder_pub', Range, lidar_pose)
                   # rate.sleep()
        except rospy.ROSInterruptException:
                pass


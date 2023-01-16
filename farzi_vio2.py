#!/usr/bin/env python
import rospy
import time
from nav_msgs.msg import Odometry

def talker():
    rospy.init_node("Bhadwa", anonymous=True)
    pub1 = rospy.Publisher("/mavros/odometry/out", Odometry, queue_size=50)
    pub = Odometry()
    i = 0

    while not rospy.is_shutdown():
        pub.header.stamp = rospy.Time.now()
        pub.header.frame_id = "odom"
        pub.child_frame_id = "base_link"
        pub.pose.pose.position.x = i
        pub.pose.pose.position.y = 0
        pub.pose.pose.position.z = 0
        pub.pose.pose.orientation.x = 0
        pub.pose.pose.orientation.y = 0
        pub.pose.pose.orientation.z = 0
        pub.pose.pose.orientation.w = 0
        pub.pose.covariance = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        pub.twist.twist.linear.x = 0
        pub.twist.twist.linear.y = 0
        pub.twist.twist.linear.z = 0
        pub.twist.twist.angular.x = 0
        pub.twist.twist.angular.y = 0
        pub.twist.twist.angular.z = 0
        pub.twist.covariance = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        rate = rospy.Rate(30)
        pub1.publish(pub)
        rate.sleep()
        i = i + 0.1

talker()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Pose

def poseCallback(msg):
    rospy.loginfo("turtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)

def pose_subscriber():
    # 初始化ROS节点
    rospy.init_node('pose_sub', anonymous=True)
    # 订阅名为/turtle1/pose的topic，消息类型为geometry_msgs::Pose，回调函数为poseCallback
    rospy.Subscriber('turtle1/pose', Pose, poseCallback)
    # 循环等待回调函数
    rospy.spin()

if __name__ == "__main__":
    pose_subscriber()

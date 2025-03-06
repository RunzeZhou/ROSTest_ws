#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def vel_publisher():
    # 创建ROS节点
    rospy.init_node('turtle_pub', anonymous=True)

    # 创建一个Publisher，发布名为/turtle1/cmd_vel的topic，消息类型为geometry_msgs::Twist，队列长度10
    turtle_vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    # 设置循环的频率
    rate = rospy.Rate(10)
    counter = 0
    
    while not rospy.is_shutdown():
        # 初始化geometry_msgs::Twist类型的消息
        vel_msg = Twist()

        # 发布消息
        vel_msg.linear.x = 0.5
        vel_msg.linear.y = 0.05 * counter
        vel_msg.angular.z = 0.01 * counter
        counter += 1

        turtle_vel_pub.publish(vel_msg)
        rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                      vel_msg.linear.x, vel_msg.angular.z)
        
        rate.sleep()

if __name__ == "__main__":
    try:
        vel_publisher()
    except rospy.ROSInterruptException:
        pass

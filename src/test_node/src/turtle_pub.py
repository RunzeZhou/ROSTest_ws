#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def vel_publisher():
    rospy.init_node('turtle_pub', anonymous=True)

    turtle_vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)
    counter = 0
    
    while not rospy.is_shutdown():
        vel_msg = Twist()
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

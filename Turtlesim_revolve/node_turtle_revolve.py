#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def turtle_move_circle():
        pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 2)
        rospy.init_node('node_turtle_revolve')
        vel_msg = Twist()

        print "Your wish is my command"
        print "If you want to quit and watch me draw squares, Ctl-c me"


        vel_msg.linear.x = 2
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 2

        #Move Robot in circle
        while not rospy.is_shutdown():
                pub.publish(vel_msg)


if __name__ == "__main__":
        try:
                turtle_move_circle()
        except rospy.ROSInterruptException:
                pass




#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback()
       global x_pose, y_pose
	x_pose=posi.x
	y_pose=posi.y

def turtle_move_circle():
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
        rospy.init_node('node_turtle_revolve')
	vel_msg = Twist()
	posi = Pose()

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
		if x_pose!= 5.544445 && y_pose!=5.544445:
		   pub.publish(vel_msg)
		else :
	            break


if __name__ == "__main__":
	try:
		turtle_move_circle()
	except rospy.ROSInterruptException:
		pass

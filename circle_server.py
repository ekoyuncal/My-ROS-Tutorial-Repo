#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from basic_apps.srv import CircleMotion

def circle_Function(request):
    speed_msg = Twist()
    linear_speed = 0.5
    speed_msg.linear.x = linear_speed
    yaricap = request.yaricap

    #w = v/r
    speed_msg.angular.z = linear_speed/yaricap

    while not rospy.is_shutdown():
        pub.publish(speed_msg)
        rospy.sleep(0.1)

rospy.init_node("Circle_Motion")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

rospy.Service("circle_service", CircleMotion, circle_Function)
rospy.spin()



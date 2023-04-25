#!/usr/bin/env python

import rospy
from basic_apps.srv import CircleMotion

rospy.wait_for_service("circle_service")

try:
    yaricap = float(input("Yaricap giriniz: "))
    service = rospy.ServiceProxy("circle_service", CircleMotion)
    service(yaricap)
except rospy.ServiceException:
    print("Error!")

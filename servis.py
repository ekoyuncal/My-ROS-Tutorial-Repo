#!/usr/bin/env python

import rospy
from deneme.srv import GecenZaman


def gecenZamanFonksiyonu(request):
    robot_hiz = 0.5
    sure = request.hedef_konum/robot_hiz
    return sure


def sendAnswer():
    rospy.init_node("Server_node")
    rospy.Service("zaman", GecenZaman, gecenZamanFonksiyonu)
    rospy.spin()

sendAnswer()

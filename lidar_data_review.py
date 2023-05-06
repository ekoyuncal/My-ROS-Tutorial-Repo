#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LaserData():
    def __init__(self):
        rospy.init_node("laser_node")
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.velocity_msg = Twist()
        rospy.Subscriber("scan", LaserScan, self.laserCallback)
        rospy.spin()

    def laserCallback(self, msg):
        left_front = list(msg.ranges[0:9])
        right_front = list(msg.ranges[350:359])
        
        front = left_front + right_front

        left = list(msg.ranges[80:100])
        right = list(msg.ranges[260:280])

        behind = list(msg.ranges[170:190])

        min_front = min(front)
        min_left = min(left)
        min_right = min(right)
        min_behind = min(behind)

        print(min_front, min_left, min_right, min_behind)

        if min_front < 1.0:
            self.velocity_msg.linear.x = 0.0
            self.pub.publish(self.velocity_msg)

        else:
            self.velocity_msg.linear.x = 0.25
            self.pub.publish(self.velocity_msg)

object = LaserData()
    
#!/usr/bin/env python


import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge



class LineTracker():
    def __init__(self):
        rospy.init_node("line_tracker")
        self.bridge = CvBridge()
        rospy.Subscriber("/camera/rgb/image_raw", Image, self.camera_callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.speed_msg = Twist()
        rospy.spin()

    def camera_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        downlimit_red = np.array([10, 100, 100])
        uplimit_red = np.array([40, 255, 255])

        mask = cv2.inRange(hsv, downlimit_red, uplimit_red)
        result = cv2.bitwise_and(img, img, mask=mask)
        
        h, w, d = img.shape
        cv2.circle(img, (int(w/2), int(h/2)), 5, (255, 0, 0), -1)

        M = cv2.moments(mask)
        if M["m00"] > 0:   
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)
            sapma = cx - w/2
            self.speed_msg.linear.x = 0.2
            self.speed_msg.angular.z = -sapma/100
            self.pub.publish(self.speed_msg)

        else:
            self.speed_msg.linear.x = 0
            self.speed_msg.angular.z = 0.0
            self.pub.publish(self.speed_msg)

        cv2.imshow("result", result)
        cv2.imshow("mask", mask)
        cv2.imshow("img", img)
        cv2.waitKey(1)


LineTracker()
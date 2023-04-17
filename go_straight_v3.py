#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from basic_apps.msg import Goal

class goGoal():
    def __init__(self):
        rospy.init_node("go_goal")
        self.goal_location = 0.0
        self.current_location = 0.0
        self.control = True

        rospy.Subscriber("/odom", Odometry, self.odom_callback)
        rospy.Subscriber("/goal", Goal, self.goal_callback)
        pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        vel_msg = Twist()
        rate = rospy.Rate(10)#10 time in 1 second
        
        while not rospy.is_shutdown():
            
            if self.control:
                vel_msg.linear.x = 0.5
                pub.publish(vel_msg)
            else:
                vel_msg.linear.x = 0.0
                pub.publish(vel_msg)
                rospy.loginfo("Goal Reached")
            rate.sleep()


    def odom_callback(self, msg):
        #print(msg.pose.pose.position.x)
        #pass
        self.current_location = msg.pose.pose.position.x

        if self.current_location < self.goal_location:
            self.control = True
        else:
            self.control = False
    def goal_callback(self, msg):
        self.goal_location = msg.goal
        
try:
    goGoal()
except rospy.ROSInterruptException:
    print("Ros Node is Done")
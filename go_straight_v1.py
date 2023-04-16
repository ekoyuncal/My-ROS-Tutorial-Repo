#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Twist

def move():
    rospy.init_node("go_straight", anonymous=False)
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    velo_msg  = Twist()
    velo_msg.linear.x = 0.5
    distance = 5
    count_distance = 0
    
    t0 = rospy.Time.now().to_sec()

    while(count_distance < distance):
        pub.publish(velo_msg)
        count_distance = (rospy.Time.now().to_sec() - t0) * velo_msg.linear.x
        
    velo_msg.linear.x = 0.0
    pub.publish(velo_msg)
    rospy.loginfo("Go straight complete !")

move()

"""
if __name__ == "__main__":
    try:
        move()
    except rospy.ROSInterruptException:
        pass
#chmod +x go_straight_v1.py /if its python file we dont have to compile we can just do like this
"""
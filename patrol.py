#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def patrol_func():
    rospy.init_node("Patrol_Node")
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    twist_msg = Twist()
    vehicle_speed = 0.25
    
    patrol_length = rospy.get_param("/PatrolLength")
    patrol_number = rospy.get_param("/PatrolCount")
    current_patrol_number = 0

    rospy.loginfo("Patrol_Node Started")

    while(current_patrol_number < patrol_number):
        t0 = rospy.Time.now().to_sec()
        displacement = 0

        if(current_patrol_number %2 == 0):
            twist_msg.linear.x = vehicle_speed
        else:
            twist_msg.linear.x = -vehicle_speed
        
        while(displacement < patrol_length):
            pub.publish(twist_msg)
            t1 = rospy.Time.now().to_sec()
            displacement = vehicle_speed * (t1-t0)

        twist_msg.linear.x = 0
        pub.publish(twist_msg)
        current_patrol_number = current_patrol_number + 1
    
    rospy.loginfo("Patrol_Node Ended")
    rospy.is_shutdown()

patrol_func()
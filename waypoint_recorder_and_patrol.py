#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseWithCovarianceStamped
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#https://drive.google.com/file/d/1semDco4h72GzKqOr40qNGQ_-7NgV0pQA/view?usp=share_link

waypoints = []

def callback_waypoints(sended_goal):
    pose = sended_goal.pose.pose
    x = pose.position.x
    y = pose.position.y
    z = pose.position.z

    qx = pose.orientation.x
    qy = pose.orientation.y
    qz = pose.orientation.z
    qw = pose.orientation.w

    waypoint = [(x, y, z), (qx, qy, qz, qw)]
    waypoints.append(waypoint)

    rospy.loginfo("Waypoint saved: {}".format(waypoint))

def waypoint_recorder():
    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, callback_waypoints)
    rospy.loginfo("Waypoint recorder started !")
    rospy.loginfo("Press Ctrl+C to stop recording")
    rospy.spin()

def waypoint_sender(waypoints):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    for waypoint in waypoints:
        goal.target_pose.pose.position.x = waypoint[0][0]
        goal.target_pose.pose.position.y = waypoint[0][1]
        goal.target_pose.pose.position.z = waypoint[0][2]

        goal.target_pose.pose.orientation.x = waypoint[1][0]
        goal.target_pose.pose.orientation.y = waypoint[1][1]
        goal.target_pose.pose.orientation.z = waypoint[1][2]
        goal.target_pose.pose.orientation.w = waypoint[1][3]

        rospy.loginfo("Waypoint sent: {}".format(waypoint))
        client.send_goal(goal)
        client.wait_for_result()
        rospy.loginfo("Waypoint reached !")


#waypoint_recorder()
#waypoint_sender()

if __name__ == '__main__':
    rospy.init_node("waypoint_patrol")

    input("Press Enter to start waypoint recording")
    try:
        waypoint_recorder()
    except rospy.ROSInterruptException:
        pass
    input("Press Enter to start waypoint sending")
    waypoint_sender(waypoints)


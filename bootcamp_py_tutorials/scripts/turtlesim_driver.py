import rospy
import numpy as np
from geometry_msgs.msg import Twist
import math


def main():
    n = np.linspace(0, 2*np.pi ,11)
    sin_values_y = np.sin(n)
    #2 boyutlu değerlerin hızını ve açısını bulmak icin
    #sin_velocity[i] = math.sqrt((i+1 -i)**2  + (y[i+1] - y[i])**2)
    #sin_angular[i] = math.atan((y[i+1] - y[i])/(i+1 -i))

    sin_velocity = np.array([1.14, 1.07, 1.003, 1.03, 1.11, 1.15, 1.11, 1.03, 1.003, 1.07, 1.14])
    sin_angular = np.array([0.495629, 0.353492, 0.0800182, -0.229932, -0.442646, -0.513122, -0.442646, -0.229932,
                            0.0800182, 0.353492, 0.495629])


    rospy.init_node('turtlesim_driver')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(50)
    
    while not rospy.is_shutdown():
        twist = Twist()
        for i in range(11):

            twist.angular.z = float(round(sin_angular[i], 3))
            twist.linear.x = float(round(sin_velocity[i], 3))
            pub.publish(twist)

            rate.sleep()

if __name__ == '__main__':
    main()
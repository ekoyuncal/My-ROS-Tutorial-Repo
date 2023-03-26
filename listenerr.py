import rospy
from std_msgs.msg import String

def callback_f(msg):
    received = msg.data
    rospy.loginfo("I Heard From My first Listener node :" + received)

def listenerr():
    rospy.init_node("listenerr")
    sub_topic = rospy.Subscriber("Konusma", String, callback= callback_f)

    rospy.spin() #like while



listenerr()

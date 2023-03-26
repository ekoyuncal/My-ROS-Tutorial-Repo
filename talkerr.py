import rospy
from std_msgs.msg import String

def talkerr():
    pub_topic = rospy.Publisher("Konusma", String, queue_size = 10)
    rospy.init_node("talkerr")

    while not rospy.is_shutdown():
        rate = rospy.Rate(2) #1 saniyede yapmasini istedigimiz tekrar miktari
        str_hello = String("Hello From My first Publisher node" + str(rospy.get_time()))
        rospy.loginfo(str_hello)
        pub_topic.publish(str_hello)
        rate.sleep()
    

talkerr()
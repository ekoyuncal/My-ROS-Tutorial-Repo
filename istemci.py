#!/usr/bin/env python

import rospy
from deneme.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman")#Wait till service is active

    try:
        servis = rospy.ServiceProxy("zaman", GecenZaman)
        cevap = servis(x)
        return cevap.gecen_sure
    except rospy.ServiceException:
        print("Error!")

hedef = float(input("Hedef konum giriniz: "))
t = istekteBulun(hedef)
print("Hedefe varana kadar gecen sure : ", t)


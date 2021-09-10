#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from std_srvs.srv import Trigger, TriggerResponse

def clbk(req):
    res=TriggerResponse()
    word=input(":")
    print(f'item :{word}')
    res.succes=True
    res.message=word
    return res
    
if __name__ == '__main__':
    rospy.init_node('testmic_server)

    s = rospy.Service('test', Trigger, clbk)

#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 
from custom_messages.msg import Custom_topic


def callback1(msg):
    print("callback1") 
    print (msg.data)

def callback2(msg):
    print("callback2") 
    print (msg.a)
    print (msg.b)
    
rospy.init_node('topic_subscriber')
sub_1 = rospy.Subscriber('/counter', Int32, callback1)
sub_1 = rospy.Subscriber('/custom_topic', Custom_topic, callback2)
rospy.spin()
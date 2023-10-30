#! /usr/bin/env python

import rospy
import actionlib
from custom_messages.msg import CounterAction, CounterGoal, CounterResult, CounterFeedback

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    print('feedback :',feedback)

def result_callback(status,result):
    print('status : ',status)
    print('result :',result.count)

# initializes the action client node
rospy.init_node('counter_client')


action_server_name = '/counter_server'
client = actionlib.SimpleActionClient(action_server_name, CounterAction)
# waits until the action server is up and running
rospy.loginfo('Waiting for action Server '+action_server_name)
client.wait_for_server()
rospy.loginfo('Action Server Found...'+action_server_name)


# creates a goal to send to the action server
goal = CounterGoal()
goal.max_number = 10
goal.duration = 3
print(goal)


client.send_goal(goal, feedback_cb=feedback_callback, done_cb=result_callback)

rate = rospy.Rate(1)

rospy.loginfo("Lets Start The Wait for the Action To finish Loop...")
while not client.wait_for_result():
    rospy.loginfo("Doing Stuff while waiting for the Server to give a result....")
    
    rate.sleep()

rospy.loginfo("Example with WaitForResult Finished.")
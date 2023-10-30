#! /usr/bin/env python
import rospy
import actionlib
from custom_messages.msg import CounterAction, CounterGoal, CounterResult, CounterFeedback

class CounterClass(object):
    
    # create messages that are used to publish feedback/result
    _feedback = CounterFeedback()
    _result   = CounterResult()

    def __init__(self):
        # creates the action server
        self._as = actionlib.SimpleActionServer("counter_server", CounterAction, self.goal_callback, False)
        self._as.start()
        
    def goal_callback(self, goal):
        # this callback is called when the action server is called.
        # this is the function that computes the Fibonacci sequence
        # and returns the sequence to the node that called the action server
        
        # helper variables
        r = rospy.Rate(1)
        success = True
        
        # append the seeds for the fibonacci sequence
        self._feedback.percentage = 0
        # publish info to the console for the user
        rospy.loginfo('"Counter Server"')
        
        # starts calculating the Fibonacci sequence
        maxnumber = goal.max_number
        duration = goal.duration
        
        cur_count = 0
        
        r = rospy.Rate(duration)
        for i in range(0, maxnumber + 1):
        
        # check that preempt (cancelation) has not been requested by the action client
            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                # the following line, sets the client in preempted state (goal cancelled)
                self._as.set_preempted()
                success = False
                # we end the calculation of the Fibonacci sequence
                break
        
            # builds the next feedback msg to be sent
            
            self._feedback.percentage = cur_count/maxnumber
            cur_count += 1
            
            # publish the feedback
            self._as.publish_feedback(self._feedback)
            # the sequence is computed at 1 Hz frequency
            r.sleep()
        
        # at this point, either the goal has been achieved (success==true)
        # or the client preempted the goal (success==false)
        # If success, then we publish the final result
        # If not success, we do not publish anything in the result
        if success:
            self._result.count = maxnumber
            rospy.loginfo('Succeeded!! Count is %i' % self._result.count )
            self._as.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('Counter_server')
    CounterClass()
    rospy.spin()
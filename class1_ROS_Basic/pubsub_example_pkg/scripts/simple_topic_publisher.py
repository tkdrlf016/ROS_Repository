#! /usr/bin/env python

# Import the Python library for ROS
import rospy
# Import the Int32 message from the std_msgs package
from std_msgs.msg import Int32             
from custom_messages.msg import Custom_topic

# Initiate a Node named 'topic_publisher'
rospy.init_node('topic_publisher')

# Create a Publisher object, that will publish on the /counter topic
# messages of type Int32
pub_1 = rospy.Publisher('/counter', Int32, queue_size=1)    
pub_2 = rospy.Publisher('/custom_topic', Custom_topic, queue_size=1)
# Set a publish rate of 2 Hz
rate = rospy.Rate(2)
# Create a variable of type Int32
count = Int32()
# Initialize 'count' variable
count.data = 0

custom_msg = Custom_topic()                        

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  # Publish the message within the 'count' variable
  print("count : ",count)
  print("custom_msg_a : ",custom_msg.a)
  print("custom_msg_b : ",custom_msg.b)
  # Increment 'count' variable
  count.data += 1
  custom_msg.a = count.data
  custom_msg.b = count.data
  pub_1.publish(count)
  pub_2.publish(custom_msg)
  # Make sure the publish rate maintains at 2 Hz
  rate.sleep()                             
#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include <custom_messages/Custom_topic.h>

void counterCallback(const std_msgs::Int32::ConstPtr& msg)
{
    ROS_INFO("Counter Callback");
    ROS_INFO("%d", msg->data);
}

void customCallback(const custom_messages::Custom_topic::ConstPtr& msg)
{
    ROS_INFO("Custom Callback");
    ROS_INFO("%d", msg->a);
    ROS_INFO("%d", msg->b);
}

int main(int argc, char** argv) {

    ros::init(argc, argv, "topic_subscriber");
    ros::NodeHandle nh;
    
    ros::Subscriber sub = nh.subscribe("counter", 1000, counterCallback);
    ros::Subscriber sub2 = nh.subscribe("custom", 1000, customCallback);
    ros::spin();
    
    return 0;
}
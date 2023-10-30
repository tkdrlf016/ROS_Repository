#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include <custom_messages/Custom_topic.h>

int main(int argc, char** argv) {

    ros::init(argc, argv, "topic_publisher");
    ros::NodeHandle nh;
    
    ros::Publisher pub = nh.advertise<std_msgs::Int32>("counter", 1000);
    ros::Publisher pub2 = nh.advertise<custom_messages::Custom_topic>("custom",1000);
    ros::Rate loop_rate(2);
    
    std_msgs::Int32 count;
    custom_messages::Custom_topic custom_msg;

    count.data = 0;
    custom_msg.a = 1;
    custom_msg.b = 2;
    
    while (ros::ok())
    {
        pub.publish(count);
        pub2.publish(custom_msg);
        ros::spinOnce();
        loop_rate.sleep();
        ++count.data;
    }
    
    return 0;
}
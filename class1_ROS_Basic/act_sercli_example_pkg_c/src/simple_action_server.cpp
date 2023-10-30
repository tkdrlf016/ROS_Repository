#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <custom_messages/CounterAction.h>

class CounterClass
{
protected:

  ros::NodeHandle nh_;
  // NodeHandle instance must be created before this line. Otherwise strange error occurs.
  actionlib::SimpleActionServer<custom_messages::CounterAction> as_; 
  std::string action_name_;
  // create messages that are used to publish feedback and result
  custom_messages::CounterFeedback feedback_;
  custom_messages::CounterResult result_;

public:

  CounterClass(std::string name) :
    as_(nh_, name, boost::bind(&CounterClass::executeCB, this, _1), false),
    action_name_(name)
  {
    as_.start();
  }

  ~CounterClass(void)
  {
  }

  void executeCB(const custom_messages::CounterGoalConstPtr &goal)
  {
    // helper variables
    int cur_count = 0;
    int maxnumber = 0;
    int duration = 0;

    maxnumber = goal->max_number;
    duration = goal->duration;
    ROS_INFO("%d: maxnumber", maxnumber);
    ROS_INFO("%d: duration", duration);
    bool success = true;

    ros::Rate r(duration);
    feedback_.percentage = 0;

    for(int i = 0; i < maxnumber +1 ; i++)
    {
      if (as_.isPreemptRequested() || !ros::ok())
      {
        ROS_INFO("%s: Preempted", action_name_.c_str());
        // set the action state to preempted
        as_.setPreempted();
        success = false;
        break;
      }
      feedback_.percentage = (float)(cur_count)/(float)(maxnumber);
      cur_count++;
      ROS_INFO("%d: cur_count", cur_count);
      as_.publishFeedback(feedback_);
      r.sleep();
    }
    
    ROS_INFO("Counter Server");
  
    if(success)
    {
      result_.count = maxnumber;
      ROS_INFO("%s: Succeeded", action_name_.c_str());
      as_.setSucceeded(result_);
    }
  }


};


int main(int argc, char** argv)
{
  ros::init(argc, argv, "counter_server");

  CounterClass counter("counter_server");
  ros::spin();

  return 0;
}
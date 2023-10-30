#include <custom_messages/CounterAction.h> // Note: "Action" is appended
#include <actionlib/client/simple_action_client.h>

void doneCb(const actionlib::SimpleClientGoalState& state,
            const custom_messages::CounterResultConstPtr& result)
{
  ROS_INFO("result : %d",result->count);
  ros::shutdown();
}

// Called once when the goal becomes active
void activeCb()
{
  ROS_INFO("Goal just went active");
}

void feedbackCb(const custom_messages::CounterFeedbackConstPtr& feedback)
{
  ROS_INFO("feedback : %f", feedback->percentage);
}

int main(int argc, char** argv)
{

  ros::init(argc, argv, "wait_for_result");
  
  actionlib::SimpleActionClient<custom_messages::CounterAction> client("counter_server", true);
  
  client.waitForServer();

  custom_messages::CounterGoal goal;
  goal.max_number = 10;
  goal.duration = 3;
  
  client.sendGoal(goal, &doneCb, &activeCb, &feedbackCb);
  //client.waitForResult();
  
  ros::Rate loop_rate(2);
    
  while (client.waitForResult() != true)
  {
    ROS_INFO("Doing Stuff while waiting for the Server to give a result...");
    loop_rate.sleep();
  }
  
  return 0;
}
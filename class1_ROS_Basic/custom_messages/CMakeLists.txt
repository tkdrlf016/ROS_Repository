cmake_minimum_required(VERSION 3.0.2)
project(custom_messages)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  actionlib_msgs # For Action
  message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  Custom_topic.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  AddTwoInts.srv
)

## Generate actions in the 'action' folder
add_action_files(
      FILES
      Counter.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs # For Action
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
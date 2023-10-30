cmake_minimum_required(VERSION 3.0.2)
project(pubsub_example_pkg_c)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  custom_messages
  roscpp
  std_msgs
)


catkin_package(
  INCLUDE_DIRS include
  LIBRARIES pubsub_example_pkg_c
  CATKIN_DEPENDS custom_messages roscpp std_msgs
  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(simple_topic_publisher src/simple_topic_publisher.cpp)


## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(simple_topic_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(simple_topic_publisher
  ${catkin_LIBRARIES}
)
#############################################################################

add_executable(simple_topic_subscriber src/simple_topic_subscriber.cpp)


## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(simple_topic_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(simple_topic_subscriber
  ${catkin_LIBRARIES}
)




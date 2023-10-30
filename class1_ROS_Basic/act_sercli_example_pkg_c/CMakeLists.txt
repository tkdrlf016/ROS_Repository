cmake_minimum_required(VERSION 3.0.2)
project(act_sercli_example_pkg_c)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  custom_messages
  roscpp
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES act_sercil_example_pkg_c
  CATKIN_DEPENDS actionlib_msgs custom_messages roscpp std_msgs actionlib
#  DEPENDS system_lib
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
add_executable(simple_action_client_wait src/simple_action_client_wait.cpp)


## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(simple_action_client_wait ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(simple_action_client_wait
  ${catkin_LIBRARIES}
)

##########################################################################################################
## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(simple_action_client_no_wait src/simple_action_client_wait.cpp)


## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(simple_action_client_no_wait ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(simple_action_client_no_wait
  ${catkin_LIBRARIES}
)

###########################################################################################################
add_executable(simple_action_server src/simple_action_server.cpp)


## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(simple_action_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(simple_action_server
  ${catkin_LIBRARIES}
)
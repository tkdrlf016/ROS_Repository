cmake_minimum_required(VERSION 3.0.2)
project(sercli_exmaple_pkg_c)

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
#  INCLUDE_DIRS include
#  LIBRARIES sercli_exmaple_pkg_c
#  CATKIN_DEPENDS custom_msgs roscpp std_msgs
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

add_executable(simple_service_client src/simple_service_client.cpp)

add_dependencies(simple_service_client ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(simple_service_client
  ${catkin_LIBRARIES}
)

##################################################################################

add_executable(simple_service_server src/simple_service_server.cpp)

add_dependencies(simple_service_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(simple_service_server
  ${catkin_LIBRARIES}
)



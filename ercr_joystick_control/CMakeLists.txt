cmake_minimum_required(VERSION 3.0.2)
project(ercr_joystick_control)

find_package(catkin REQUIRED COMPONENTS
    rospy
    ercr_msgs
    sensor_msgs
)

catkin_package(
  # INCLUDE_DIRS 
  CATKIN_DEPENDS rospy ercr_msgs sensor_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS scripts/thrust_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

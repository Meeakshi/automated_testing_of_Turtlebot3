#!/bin/bash 
cd ~/catkin_ws/ && catkin_make && source devel/setup.bash
roslaunch "turtlebot3_gazebo" "turtlebot3_world.launch"
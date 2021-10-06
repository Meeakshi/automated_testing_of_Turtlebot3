#!/bin/bash 
cd ~/catkin_ws/ && source devel/setup.bash
rosrun "test_simulation" "test_turtlebot3_obstacleavoidance.py"

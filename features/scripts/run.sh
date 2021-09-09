#!/bin/bash
echo "Hello world"

cd ~/catkin_ws/ && catkin_make && source devel/setup.bash 
rosrun test_simulation test_avoid_obstacle.py


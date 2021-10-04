#!/bin/bash 
cd ~/catkin_ws/ && source devel/setup.bash
rosrun "test_simulation" "pointtest.py" 0.1 0 0

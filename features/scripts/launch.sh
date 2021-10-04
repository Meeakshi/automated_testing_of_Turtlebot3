#!/bin/bash
echo "Hello world"

#gnome-terminal -e "roslaunch test_simulation my_world_master.launch"
cd ~/catkin_ws/ && catkin_make && source devel/setup.bash 
roslaunch test_simulation my_world_master.launch


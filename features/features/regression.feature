Feature: test turtlebot3 navigation

   Scenario: TC1: navigation test
      Given create a launch file with package name "test_simulation" and launch file name "my_world_master.launch"
      Then Perform Catkin make, setup bash & roslaunch
      When Process "roslaunch" has launched successfully
      Then create a run file with package name "test_simulation" and file name "test_point_test.py" with params "1 1 180"
      Then Run rorun for turtlebot3 navigation test
      Then Finally close all terminals and exit execution

  Scenario: TC2: obstacle avoidance test
      Given create a launch file with package name "turtlebot3_gazebo" and launch file name "turtlebot3_world.launch"
      Then Perform Catkin make, setup bash & roslaunch
      When Process "roslaunch" has launched successfully
      Then create a run file with package name "test_simulation" and file name "test_avoid_obstacle.py" with params ""
      Then Run rorun for turtlebot3 OT test
      Then Finally close all terminals and exit execution

   Scenario: TC3: test image detection one object
      Given Run image detection algorithm and load images "image_2.jpg" from a directory and find "cat, person, car, bicycle"
     

 

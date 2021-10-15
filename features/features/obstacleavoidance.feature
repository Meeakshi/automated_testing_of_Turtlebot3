Feature: showing off behave

  Scenario: run turtlebot3 in an gazebo world for obstacle avoidance test
      Given create a launch file with package name "turtlebot3_gazebo" and launch file name "turtlebot3_world.launch"
      Then Perform Catkin make, setup bash & roslaunch
      When Process "roslaunch" has launched successfully
      Then create a run file with package name "test_simulation" and file name "test_avoid_obstacle.py" with params ""
      Then Run rorun for turtlebot3 OT test
      Then Finally close all terminals and exit execution
      Then Open reports


  #Scenario: run turtlebot3 in an empty gazebo world for obstacle avoidance test
      #Given create a launch file with package name "test_simulation" and launch file name "my_world_master.launch"
      #Then Perform Catkin make, setup bash & roslaunch
      #When Process "roslaunch" has launched successfully
      #Then create a run file with package name "test_simulation" and file name "test_avoid_obstacle.py" with params ""
      #Then Run rorun for turtlebot3 OT test
      #Then Finally close all terminals and exit execution


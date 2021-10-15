Feature: test turtlebot3 navigation

  Scenario: run turtlebot3 in an tb defined gazebo world
      Given create a launch file with package name "turtlebot3_gazebo" and launch file name "turtlebot3_world.launch"
      Then Perform Catkin make, setup bash & roslaunch
      When Process "roslaunch" has launched successfully
      Then create a run file with package name "test_simulation" and file name "test_point_test.py" with params "1 0 180"
      Then Run rorun for turtlebot3 navigation test
      Then Finally close all terminals and exit execution

  Scenario: run turtlebot3 in an empty gazebo world
      Given create a launch file with package name "test_simulation" and launch file name "my_world_master.launch"
      Then Perform Catkin make, setup bash & roslaunch
      When Process "roslaunch" has launched successfully
      Then create a run file with package name "test_simulation" and file name "test_point_test.py" with params "1 0 180"
      Then Run rorun for turtlebot3 navigation test
      Then Finally close all terminals and exit execution
      Then Open reports

  #Scenario: run turtlebot3 in a static gazebo world cafe
      #Given create a launch file with package name "test_simulation" and launch file name "my_world_master.launch"
      #Then Perform Catkin make, setup bash & roslaunch
      #When Process "roslaunch" has launched successfully
      #Then create a run file with package name "test_simulation" and file name "test_point_test.py" with params "1 0 180"
      #Then Run rorun for turtlebot3 navigation test
      #Then Finally close all terminals and exit execution

  #Scenario: run turtlebot3 in a gazebo workshop world
      #Given create a launch file with package name "test_simulation" and launch file name "turtlebot3_empty_world.launch"
      #Then Perform Catkin make, setup bash & roslaunch
      #When Process "roslaunch" has launched successfully
      #Then create a run file with package name "test_simulation" and file name "test_point_test.py" with params "1 1 180"
      #Then Run rorun for turtlebot3 navigation test
      #Then Finally close all terminals and exit execution


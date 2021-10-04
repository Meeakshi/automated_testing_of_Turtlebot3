Feature: test turtlebot3 navigation

  Scenario: run turtlebot3 in a static gazebo world
     #Given Catkin make and Devel setup bash 
      #When Run roslaunch for turtlebot3
      #Then test the bot navigation

  Scenario: run turtlebot3 in a dynamic gazebo world
      Given create a launch file with package name "test_simulation" and launch file name "my_world_master.launch"
      Then Perform Catkin make, setup bash & roslaunch
      Then create a run file with package name "test_simulation" and file name "pointtest.py" with params "1 0 0"
      Then Run rorun for turtlebot3 navigation test
      #Then Navigate turtlebot3 to |x|y|z| "0.5 0.5 90"
      #Then test the bot navigation

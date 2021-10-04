Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: run turtlebot3 in a static gazebo world
     Given Catkin make and Devel setup bash 
      When Run roslaunch for turtlebot3
      #Then Test absolute avoidance using lidar sensor

  #Scenario: run turtlebot3 in a dynamic gazebo world
     #Given Catkin make and Devel setup bash 
      #When Run roslaunch for turtlebot3
      #Then test absolute avoidance using lidar sensor

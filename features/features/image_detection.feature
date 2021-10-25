Feature: test image detection

  Scenario: TC1: test image detection one object
     Given Run image detection algorithm and load images "image_2.jpg" from a directory and find "bicycle"
     #Then Open reports

  Scenario: TC2: test image detection many objects
     Given Run image detection algorithm and load images "image_2.jpg" from a directory and find "cat, person, car, bicycle"
     #Then Open reports
 

      #When image is deteced verify if the classified image is as expected "Dog, cat, Cycle"
      #Then behave will test it for us!

  #Scenario: test video detection
     #Given run image detection algorithm and load videos from a directory "~"
      #When image is deteced verify if the classified image is as expected "Dog, cat, Cycle"
      #Then behave will test it for us!

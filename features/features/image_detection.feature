Feature: test image detection

  Scenario: test image detection
     Given Run image detection algorithm and load images from a directory and find "Bus"
     Then Finally close terminal and exit execution
      #When image is deteced verify if the classified image is as expected "Dog, cat, Cycle"
      #Then behave will test it for us!

  #Scenario: test video detection
     #Given run image detection algorithm and load videos from a directory "~"
      #When image is deteced verify if the classified image is as expected "Dog, cat, Cycle"
      #Then behave will test it for us!

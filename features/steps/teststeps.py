#!/usr/bin/env python


from behave import *
import os
import subprocess
import time
from subprocess import call
import allure 
import psutil
import signal
import cv2
import numpy as np
import sys 
from sys import exit
import rospy
import unittest
import xmlrunner
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import os
import math



@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
#************************************************************************************************************************************************************
@Given('Catkin make and Devel setup bash')
def step_impl(context):
	p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/launch.sh'",stdout=subprocess.PIPE,shell=True) 
	output = p.communicate()[0]
	print output
	#("gnome-terminal --x sh ~/automation_pack/features/scripts/launch.sh", shell=True)
	#os.system('~/automation_pack/features/scripts/launch.sh')
	#subprocess.call(['sh', '~/automation_pack/features/scripts/launch.sh']) #("gnome-terminal '~/automation_pack/features/scripts/launch.sh'")
	#os.system('~/automation_pack/features/scripts/launch.sh')
	print("Hi")
	time.sleep(60)
	print output
#************************************************************************************************************************************************************
@When('Run roslaunch for turtlebot3')
def step_impl(context):
	print("ros launch start")
	p=os.system('~/automation_pack/features/scripts/temp_run.sh') 
	#output = p.communicate()[0]
	print p
#************************************************************************************************************************************************************
@then('Test absolute avoidance using lidar sensor')
def step_impl(context):
	os.system("gnome-terminal 'cd ~/catkin_ws/ && source devel/setup.bash && rosrun test_simulation test_avoid_obstacle.py'")	
#************************************************************************************************************************************************************
@Given('run image detection algorithm and load images from a directory')
def step_impl(context):
	#call(["python", "~/OpenCV_CNN_For_ImageAndVideo_Detection/python/detection/detect_img.py"])
	os.system('python ~/OpenCV_CNN_For_ImageAndVideo_Detection/python/detection/detect_img.py')
#************************************************************************************************************************************************************

@then('Perform Catkin make, setup bash & roslaunch')
def step_impl(context):
	print("Start of test")
	print("Launch new terminal and run roslaunch for turtlebot3")
	with open('logs.txt', 'w') as f:
		p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_launch.sh'",stdout=subprocess.PIPE,shell=True) 
		p.wait()
	output = p.communicate()[0]
	time.sleep(10)
	if(p.returncode ==None):
		assert True
	else:
		assert True
	print("Roslaunch successfull")
#************************************************************************************************************************************************************

@then('Navigate turtlebot3 to |x|y|z| {text}')
def step_impl(context,text):
	print("Hello")	
	print(text)
#************************************************************************************************************************************************************

@Given("create a launch file with package name {} and launch file name {}")
def writetextfile(context, package, launchfile):
	print("Generate new sh file for running roslaunch in user defined gazebo world")
	directory = os.getcwd()
	filelocation="/home/meenakshi/automation_pack/features/scripts/temp_launch.sh"
	buildlines = "#!/bin/bash \ncd ~/catkin_ws/ && catkin_make && source devel/setup.bash"
	launchlines = "roslaunch {} {}".format(package,launchfile)
	with open(filelocation, 'w') as f:
		f.writelines(buildlines + '\n' + launchlines)
	if(os.path.exists(filelocation)):
		assert True
	else:
		assert False
	print("New file generated successfully")
#************************************************************************************************************************************************************

@Then("create a run file with package name {} and file name {} with params {}")
def writetextfile(context, package, launchfile, parameters):
	print("Generate new sh file for running rosrun in user defined gazebo world with given parameters")
	directory = os.getcwd()
	filelocation="/home/meenakshi/automation_pack/features/scripts/temp_run.sh"
	buildlines = "#!/bin/bash \ncd ~/catkin_ws/ && source devel/setup.bash"
	launchlines = "rosrun {} {}".format(package,launchfile)
	with open(filelocation, 'w') as f:
		f.writelines(buildlines + '\n' + launchlines +' '+ parameters.strip('"'))
	if(os.path.exists(filelocation)):
		assert True
	else:
		assert False
	print("New file generated successfully")
#************************************************************************************************************************************************************

@Then('Run rorun for turtlebot3 navigation test')
def step_impl(context):
	print("Start Rosrun python script to test navigation")
	time.sleep(20)
	with open('logs.txt', 'w') as f:
		p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_run.sh'",stdout=subprocess.PIPE,shell=True)
		
	time.sleep(20)
	
	print (p.returncode)
	if(p.returncode == None):
		assert True 
	else:
		assert False#assert context.failed is False
	while checkIfProcessRunning('python'):
		time.sleep(1)
	print "Test execution complete"
	filename="~/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml"
	filenamelink="""<a href='/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml'>xml report</a>"""
	#allure.attach('Hi there!', name='user attachment', attachment_type=allure.attachment_type.TEXT)
	allure.attach(filename,name="unittest.xml" , attachment_type=allure.attachment_type.XML)
	allure.attach(filenamelink,name="unittest" , attachment_type=allure.attachment_type.HTML)

#************************************************************************************************************************************************************
@Then('Run rorun for turtlebot3 OT test')
def step_impl(context):
	print("Start Rosrun python script to test navigation")
	time.sleep(20)
	with open('logs.txt', 'w') as f:
		p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_run.sh'",stdout=subprocess.PIPE,shell=True)
		
	time.sleep(10)

	print (p.returncode)
	if(p.returncode == None):
		assert True 
	else:
		assert False#assert context.failed is False
	while checkIfProcessRunning('python'):
		time.sleep(1)
	print "Test execution complete"
	filename="~/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml"
	filenamelink="""<a href='/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml'>xml report</a>"""
	#allure.attach('Hi there!', name='user attachment', attachment_type=allure.attachment_type.TEXT)
	allure.attach(filename,name="unittest.xml" , attachment_type=allure.attachment_type.XML)
	allure.attach(filenamelink,name="unittest" , attachment_type=allure.attachment_type.HTML)

#************************************************************************************************************************************************************
#@And('Attach unittest xml report to allure')
def after_scenario(context):
	print('After all executed')
	filename='/home/meenakshi/catkin_ws/src/test_simulation/results/results.xml'
	#allure.attach(name=filename, attachment_type=allure.attachment_type.XML)
	allure.attach(filename,name="unit test xml" , attachment_type=allure.attachment_type.XML)

#***********************************************************************************************************************************************************
def after_all(context):
	print('Before all executed')

#************************************************************************************************************************************************************

def checkIfProcessRunning(processName):
         
    processName= processName.strip('"')
    
    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
		print('{} process running'.format(processName))
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print('{} process not found'.format(processName))
    return False;
#******************************************************************************************************************************

@When('Process {} has launched successfully')
def checkforprocess(context, pname):
	if checkIfProcessRunning(pname):
		assert True
	else:
		assert False

#******************************************************************************************************************************
@Then('Finally close all terminals and exit execution')
def processkill(context):
    print('start killing')
    # Ask user for the name of process
    name = "gazebo"
    
    try:
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
             
            # extracting Process ID from the output
            pid = fields[0]
             
            # terminating process
	    #exit(0)
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")
         
    except:
        print("Error Encountered while running script")

#******************************************************************************************************************************
@Then('Finally close terminal and exit execution')
def processkillbehave(context):
    print('start killing')
    # Ask user for the name of process
    name = "behave"
    
    try:
        # iterating through each instance of the process
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()
             
            # extracting Process ID from the output
            pid = fields[0]
             
            # terminating process
            os.kill(int(pid), signal.SIGKILL)
	    exit(0)
        print("Process Successfully terminated")
         
    except:
        print("Error Encountered while running script")

#******************************************************************************************************************************
@Given('Run image detection algorithm and load images from a directory and find {}')
def loadimageforclassification(context, imageName):
	print("Start of test for image detection")
	# load the COCO class names
	with open('/home/meenakshi/CNN/input/object_detection_classes_coco.txt', 'r') as f:
	    class_names = f.read().split('\n')

	# get a different color array for each of the classes
	COLORS = np.random.uniform(0, 255, size=(len(class_names), 3))

	# load the DNN model
	model = cv2.dnn.readNet(model='/home/meenakshi/CNN/input/frozen_inference_graph.pb',
		                config='/home/meenakshi/CNN/input/ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt', 
		                framework='TensorFlow')


	# Loading the cascades
	face_cascade = cv2.CascadeClassifier('/home/meenakshi/CNN/cascades/haarcascade_frontalface_default.xml')
	smile_cascade = cv2.CascadeClassifier('/home/meenakshi/CNN/cascades/haarcascade_smile.xml')

	#name = input("Enter any of the two options 1 for Camera/2 for Load image from device: ")
	#findobj = input("Enter name of the object to be found: ")

	#name = str(name)
	findobj = 'car'#str(imageName)
	#print findobj	
	image = cv2.imread('/home/meenakshi/CNN/input/image_2.jpg')
	image_height, image_width, _ = image.shape
	# create blob from image
	blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), 
		                     swapRB=True)
	# create blob from image
	model.setInput(blob)
	# forward pass through the model to carry out the detection
	output = model.forward()
	
	print (output)
	listofnames = imageName.split(',')
	for name in listofnames:
		global flagtofind
		flagtofind = 0
		# loop over each of the detection
		for detection in output[0, 0, :, :]:
		    # extract the confidence of the detection
		    confidence = detection[2]
		    # draw bounding boxes only if the detection confidence is above...
		    # ... a certain threshold, else skip
		    if confidence > .4:
			# get the class id
			class_id = detection[1]
			# map the class id to the class
			#print(len(class_names))
			#print(class_names)
			class_name = class_names[int(class_id)-1]
			compareobjectfound(class_name.lower(),name.strip('"'))
			if(flagtofind > 0):
				color = COLORS[int(class_id)]
				# get the bounding box coordinates
				box_x = detection[3] * image_width
				box_y = detection[4] * image_height
				# get the bounding box width and height
				box_width = detection[5] * image_width
				box_height = detection[6] * image_height
				# draw a rectangle around each detected object
				cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)
				# put the FPS text on top of the frame
				cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
				#print(len(class_name.lower()))
				#print(len(imageName.lower().strip('"')))
				#print(class_name.lower() is imageName.lower().strip('"'))
				#imageName = imageName.lower().strip('"')
				cv2.imshow('image', image)
				cv2.imwrite('/home/meenakshi/CNN/outputs/image_result.jpg', image)
				cv2.waitKey(0)
				cv2.destroyAllWindows()

		if(flagtofind ==0):
			print("Test failed Object {} not found" .format(name))
			#assert False 
		else:
			print("Test pass Object {} found & number of obejcts found are {}" .format(name.strip(),flagtofind))
			assert True

def compareobjectfound(class_name,name):
	global flagtofind
	if  name.strip() == class_name.strip():
		print("Test pass Object {} found" .format(name.strip()))
		flagtofind = flagtofind+1
	
	#if flagtofind == 0:
	#	print("Test failed Object {} not found" .format(namenotfound))
#******************************************************************************************************************************
@Then('Open reports')
def openreport(context):
	print("Open allure report")
	p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_report.sh'",stdout=subprocess.PIPE,shell=True) 
	
#******************************************************************************************************************************
def callback(msg):
	    if msg.ranges[0] > 0.5: #and msg.ranges[90] > laserthreshold2 and msg.ranges[270] > laserthreshold2:
		print("No Obstacle found") 
		print(msg.ranges[0])

	    else:
		print("Obstacle found") 

#******************************************************************************************************************************
def fetchscandata():
	time.sleep(20)
	print(rospy.get_published_topics())
	print('==============Start=======================')
	rospy.init_node('obstacle_avoidance')
	counter = 0
	sub=rospy.Subscriber('/scan', LaserScan, callback)
	pub=rospy.Publisher('/cmd_vel', Twist)
	move=Twist()
	rospy.spin()






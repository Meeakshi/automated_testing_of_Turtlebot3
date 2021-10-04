from behave import *
import os
import subprocess
import time
from subprocess import call
import allure 


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

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
	time.sleep(100)
	print output

@When('Run roslaunch for turtlebot3')
def step_impl(context):
	print("ros launch start")
	p=os.system('~/automation_pack/features/scripts/temp_run.sh') 
	#output = p.communicate()[0]
	print p

@then('Test absolute avoidance using lidar sensor')
def step_impl(context):
	os.system("gnome-terminal 'cd ~/catkin_ws/ && source devel/setup.bash && rosrun test_simulation test_avoid_obstacle.py'")	

@Given('run image detection algorithm and load images from a directory')
def step_impl(context):
	#call(["python", "~/OpenCV_CNN_For_ImageAndVideo_Detection/python/detection/detect_img.py"])
	os.system('python ~/OpenCV_CNN_For_ImageAndVideo_Detection/python/detection/detect_img.py')

@then('Perform Catkin make, setup bash & roslaunch')
def step_impl(context):
	with open('logs.txt', 'w') as f:
		p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_launch.sh'",stdout=subprocess.PIPE,shell=True) 
	output = p.communicate()[0]
	time.sleep(50)
	if(p.returncode ==None):
		assert True
	else:
		assert True
	print output
	
@then('Navigate turtlebot3 to |x|y|z| {text}')
def step_impl(context,text):
	print("Hello")	
	print(text)

@Given("create a launch file with package name {} and launch file name {}")
def writetextfile(context, package, launchfile):
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

@Then("create a run file with package name {} and file name {} with params {}")
def writetextfile(context, package, launchfile, parameters):
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

@Then('Run rorun for turtlebot3 navigation test')
def step_impl(context):
	print("Start Rosrun python script to test navigation")
	with open('logs.txt', 'w') as f:
		p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_run.sh'",stdout=subprocess.PIPE,shell=True)
		#p= os.system('~/automation_pack/features/scripts/temp_run.sh',stdout=f) 
	#p=subprocess.Popen("gnome-terminal -- $SHELL -c '~/automation_pack/features/scripts/temp_run.sh'",stdout=subprocess.PIPE,shell=True) 
	#output = p.communicate()[0]
	#print p.communicate()[0]
	time.sleep(50)
	print (p.stdout)
	if(p.returncode == None):
		assert True 
	else:
		assert False#assert context.failed is False
	print "End"


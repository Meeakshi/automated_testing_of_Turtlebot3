from behave import *
import os
import subprocess


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
	os.system('~/automation_pack/features/scripts/launch.sh')

@When('Run roslaunch for turtlebot3')
def step_impl(context):
	os.system('~/automation_pack/features/scripts/run.sh')

@then('Run absolute avoidance test code')
def step_impl(context):
	os.system("cd ~/catkin_ws/ && source devel/setup.bash && rosrun test_simulation test_avoid_obstacle.py")	

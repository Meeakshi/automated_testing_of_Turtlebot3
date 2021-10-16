# Automated testing of Turtlebot3

The overall objective of this project is to build an automation pack that can be used for automated testing of various mobile robots and their important basic features like navigation, obstacle avoidance and image classification. For this thesis turtlebot 3 models( Burger, waffle, waffle-pi) have been used. The primary purpose of this thesis is to promote use of automation for quality assurance and testing in simulation. Below listed are some of the significances of using this developed automation pack,
•	Cost effective testing can be achieved because once development of this automation pack is complete one resource would be sufficient to execute and test the robot. 
•	Parallel testing of multiple robots at the same time by a single resource can be achieved. 
•	Time and cost are saved as manual intervention will not be required at all during testing. 
•	Testing time for one test case execution can be reduced form minutes to seconds which enables the defect tracking process much faster.
•	Retest and regressive testing are feasible and fast through automation compared to manual. 

# Installations:

conda install -c conda-forge behave 

pip install unittest

pip install allure-behave 

pip install msgpack argparse

pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp27-none-linux_x86_64.whl 

pip install tensorboard

pip install numpy pyqtgraph

Clone automation pack from https://github.com/Meeakshi/automated_testing_of_Turtlebot3.git and switch to master branch

For turtlebot 3 packages clone product from https://github.com/Meeakshi/product_tobe_tested_turtlebot3.git and switch to master branch

# Directory:
![image](https://user-images.githubusercontent.com/76649126/137586735-9a89dcc3-4f54-43d9-8790-3ad440d431aa.png)

1	allure - Allure folder contains json allure reports that gets generated after every scenario execution

2	features -	All the test cases are written inside features folder with “.feature” file extension.

3	reports -	Xml parser.py code is saved here for reports

4	scripts -	Roslaunch and Rosrun execution files are created here and saved here during runtime.  

5	steps -	Step implementation for every test step is available here in teststeps.py file. 


# Test	Commands:
## Prerequisite:                     	
Cd to features directory inside automation_pack folder

## Test Navigation:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./navigation.feature --no-capture

## Test Obstacle avoidance:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./ obstacle_avoidance.feature --no-capture

## Test image detection algorithm:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./image_detection.feature --no-capture

## To view reports:
allure serve results

# Reports

![navigation_report](https://user-images.githubusercontent.com/76649126/137587258-54e46147-d247-42e0-a74e-35a14c88c769.png)


![obstacle_avoidance_report](https://user-images.githubusercontent.com/76649126/137587274-b408805c-19ab-4842-a267-1e18f6b352c9.png)


![image_detection_report](https://user-images.githubusercontent.com/76649126/137587277-f39f1fc0-1011-42b6-a451-2d60766878e5.png)



# automated_testing_of_Turtlebot3
#Automated testing of Turtlebot3

The overall objective of this project is to build an automation pack that can be used for automated testing of various mobile robots and their important basic features like navigation, obstacle avoidance and image classification. For this thesis turtlebot 3 models( Burger, waffle, waffle-pi) have been used. The primary purpose of this thesis is to promote use of automation for quality assurance and testing in simulation. Below listed are some of the significances of using this developed automation pack,
•	Cost effective testing can be achieved because once development of this automation pack is complete one resource would be sufficient to execute and test the robot. 
•	Parallel testing of multiple robots at the same time by a single resource can be achieved. 
•	Time and cost are saved as manual intervention will not be required at all during testing. 
•	Testing time for one test case execution can be reduced form minutes to seconds which enables the defect tracking process much faster.
•	Retest and regressive testing are feasible and fast through automation compared to manual. 


#Directory:
├── python │ ├── classification │ │ ├── classify.py │ │ └── README.md │ ├── detection │ │ ├── detect_img.py │ │ └── detect_vid.py │ └── requirements.txt └── README.md

1	allure	Allure folder contains json allure reports that gets generated after every scenario execution
2	features	All the test cases are written inside features folder with “.feature” file extension.
3	reports	Xml parser.py code is saved here for reports
4	scripts	Roslaunch and Rosrun execution files are created here and saved here during runtime.  
5	steps	Step implementation for every test step is available here in teststeps.py file. 


#Installations:
conda install -c conda-forge behave 
pip install unittest
pip install allure-behave 
pip install msgpack argparse
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp27-none-linux_x86_64.whl 
pip install tensorboard
pip install numpy pyqtgraph


#Test	Commands:
Prerequisite:                     	Cd to feature directory

Test Navigation:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./navigation.feature --no-capture

Test Obstacle avoidance:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./ obstacle_avoidance.feature --no-capture

Test image detection algorithm:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./image_detection.feature --no-capture

To view reports:
allure serve results


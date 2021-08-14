# ENPM 661 - Planning for Autonomous Robots Project 3 (Phase 4)

## Authors

@ Nikhil Lal Kolangara (116830768)
@ Sanaulla Patan (116950985)

## Installation

-- Install all package dependencies like [matplotlib](https://matplotlib.org/users/installing.html) and [numpy](https://numpy.org/) and [OpenCV](https://opencv.org/) before running the code.
-- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib and all the packages to the latest versions.
-- Install [ROS Melodic](http://wiki.ros.org/melodic/Installation) and Gazebo on Ubuntu 18.04. Follow the instructions to install and setup the catkin workspace.
-- Clone the GIT Repository for the [Turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3). 
-- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install matplotlib and other packages and to update all the packages to the latest versions.
-- Place the "Map.world" file in the 'worlds" file and refer to it in the ".launch" file


'''bash
pip install matplotlib
'''

## Usage

'''python
import matplotlib.plyplot as plt
import numpy as np
plt.style.use('seaborn-pastel')
import cv2
'''

## NOTE: Values are in centimeters for the obstacle map.

## Directory Structure

"proj3_group26_ros_python.zip" 										
 (Extract this compressed file to any desired folder) 					
	Folder Name after extraction: proj3_group26_ros_python
					|- Phase_3
					|   |- Phase3_video.avi
					|   |- Phase3.py
					|   |- ReadMe.txt
					|   |- MapInfo.py
					|   |- README.md
					|- Phase_4
					|   |- Phase4_video1.mp4
					|   |- Phase4_video2.mp4
					|   |- ReadMe.txt
					|   |- README.md
					|   |- ros_ws
					|   |   |- build
					|   |   |- devel
					|   |   |- src
					|   |   |- .catkin_workspace
						

## Intructions to run the files

-> Extract the "proj3_group26_ros_python.zip" to any desired folder.

-> 1. Using the Terminal:

->-> Navigate to the "ros_ws" folder under the "Phase_4" folder inside "proj3_group26_ros_python" folder, right click and select open terminal.
	*** use 'python3' instead of 'python' in the terminal if using Linux based OS ***
	
	-------------------------TERMINAL 1--------------------------------------------------------------------------------------------
	*** Run the command "roscore" 
	
	-------------------------TERMINAL 2--------------------------------------------------------------------------------------------
	*** Now to Spawn the robot we need to give the values of the turtle bot in the robotDrive.launch file ( x -4.8 y -4.8 z 0)
	and open one more terminal at the same location
	*** Run command "source ~/ros_ws/devel/setup.bash"
	*** Run command "roslaunch robotDrive robotDrive.launch"
	-------------------------TERMINAL 3--------------------------------------------------------------------------------------------
	*** Now to run the Astart Algorithm on the spwaned robot, we need to start the python code which subscribes and publishes the'
	values for the '/odom' and '/cmd_vel' respectively. To run your python code
	*** Make sure that all the python files are given chmd +x to make them executable. 
	*** Run command "source ~/ros_ws/devel/setup.bash"
	*** Run command "rosrun robotDrive moveRobot.py"
	This command internally calls the Astar_rigid and MapInfo files to generate the steps for the robot to move.
	
	Enter the inputs for the code to run. 
	-- Enter the Start Points [x, y, theta] position: [-480, -480, 30] (parameters in single line and inside square brackets)
	-- Enter the Goal Points [x, y] position: [-400, -400] (parameters in single line and inside square brackets)
	-- Enter the Robot RPM Values [left, right] for the robot: [8, 10]
	-- Enter the Clearance of the robot: 5
	
	-------------------------OUTPUT--------------------------------------------------------------------------------------------------
	Once the path generator finds an optimal path it returns the values to the GAZEBO, and the robot recieves the values for the 
	'/cmd_vel' rostopic. Once the robot reads ROS topic values it begins to move. Thereby reaching the required goal point.

## Sample Execution

### Video 1

'''bash

Enter the Start Points (x,y,theta) position: -415 -310 30
Enter the Goal Points (x,y) position: -10 -310
Enter the RPM Values for the robot: 8 10
Enter the Clearance of the robot: 5

Total Cost to reach the final Point: 255.54
total time for A star in seconds:  0.0469
length of step_object_list 160
length of the pathvalues 119

'''bash

Enter the Start Points (x,y,theta) position: -410 -420 30
Enter the Goal Points (x,y) position: 390 260
Enter the RPM Values for the robot: 8 10
Enter the Clearance of the robot: 5

Total Cost to reach the final Point: 666.63
total time for A star in seconds:  0.550
length of step_object_list 1729
length of the pathvalues 760

'''

## Final Note

-> The Output files generated are 'Phase4_video1.mp4' and 'Phase4_video2.mp4' video file. 



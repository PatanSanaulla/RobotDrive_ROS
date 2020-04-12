#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2
from Astar_rigid import *

currPos = {'x': 0.0, 'y': 0.0, "theta": 0.0}


def odomCallback(position):
    global currPos

    x = position.pose.pose.position.x
    y = position.pose.pose.position.y

    oreintation = position.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([oreintation.x, oreintation.y, oreintation.z, oreintation.w])
    currPos = {'x': x, 'y': y, 'theta': theta}
    rospy.loginfo("Current values from ODOM: " + str(currPos['x']) + ':' + str(currPos['y']))


def moveRobot(STEPS):
    rospy.init_node('turtlebot_driver')

    sub = rospy.Subscriber("/odom", Odometry, odomCallback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    step_msg = Twist()
    rate = rospy.Rate(0.2)  # 10hz

    counter = 0
    goal = Point()


    while not rospy.is_shutdown():
        goal.x = STEPS[counter][0]
        goal.y = STEPS[counter][1]
        rospy.loginfo("Reaching to point: " + str(goal.x) + ':' + str(goal.y))

        step_msg.linear.y = 0
        step_msg.linear.z = 0
        step_msg.angular.x = 0
        step_msg.angular.y = 0

        inc_x = goal.x - currPos['x']
        inc_y = goal.y - currPos['y']

        if abs(inc_x) < 0.1 and abs(inc_y) < 0.1:
            counter += 1

            step_msg.linear.x = 0.0
            step_msg.angular.z = 0.0

        else:
            angle = atan2(inc_y, inc_x)
            angleDiff = abs(angle - currPos["theta"])

            if angleDiff > 0.1:

                if angleDiff < 0.5:
                    step_msg.angular.z = (angle - currPos["theta"]) #* 0.7
                    step_msg.linear.x = ((inc_x ** 2 + inc_y ** 2) ** 0.5) #* 0.7
                    rospy.loginfo("move and rotate"+str(step_msg.linear.x)+" : "+str(step_msg.linear.z))

                else:
                    step_msg.linear.x = 0.0
                    step_msg.angular.z = (angle - currPos["theta"])*0.3
                    rospy.loginfo("rotate"+str(step_msg.linear.x)+" : "+str(step_msg.linear.z))

            else:
                step_msg.linear.x = ((inc_x**2 + inc_y **2 )**0.5 )*0.5
                step_msg.angular.z = 0.0
                rospy.loginfo("move"+str(step_msg.linear.x)+" : "+str(step_msg.linear.z))

        pub.publish(step_msg)
        #rate.sleep()


if __name__ == '__main__':
    try:
        moveRobot(getValues())
    except rospy.ROSInterruptException:
        pass

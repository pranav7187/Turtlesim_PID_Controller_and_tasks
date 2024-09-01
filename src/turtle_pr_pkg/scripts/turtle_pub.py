#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


def current_pose(pose_message):
    global x
    global y 
    global yaw

    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta
   
    
    

def main_function():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    loop_rate = rospy.Rate(10)
    rospy.sleep(1)
    global x
    global y
    global yaw
    yaw = 0
    x = 0
    y = 0
    Kp_linear = 0.4
    Kp_angular = 0.2
    velocity = Twist()


    rospy.sleep(2)
    x_to_go = float(input())
    y_to_go = float(input())
    distance = 0.0
    while not rospy.is_shutdown() :
        velocity.linear.x = Kp_linear*distance
        velocity.angular.z = Kp_angular * ((math.atan2(y_to_go - y , x_to_go - x)) - yaw)
        pub.publish(velocity)
        loop_rate.sleep()
        distance = abs(math.sqrt((x_to_go - x)**2 + (y_to_go - y)**2))
        rospy.loginfo(distance)
        

        
        
        
         
if __name__ == "__main__":
    try:
        rospy.init_node('turtle_pub', anonymous= False)
        rospy.sleep(2)
        rospy.Subscriber('/turtle1/pose', Pose, current_pose)
        rospy.sleep(1)
        main_function()
    except rospy.ROSInterruptException:
        pass

    
    
    
    
    
    
    



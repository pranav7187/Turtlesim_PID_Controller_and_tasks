#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String
from geometry_msgs.msg import Twist

rospy.init_node('rrt',anonymous=False)
pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)



def main():




if __name__ == "__main__":
    try:

        main()
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String




def player():
    global counter
    global flag
    counter = 0
    flag = 0
    
    
    rospy.init_node('PlayerB',anonymous=False) #intializing the node
    pub = rospy.Publisher('playerB_line', String, queue_size=10)
    rospy.Subscriber('hitpoint_senderB', String, handleinput)
    print("Waiting for connection")
    rospy.sleep(1)
    
    
    while not rospy.is_shutdown():

        
         

        if flag == 1 :
            playerinput(pub)
            flag = 0

        


def handleinput(data):
    global counter
    global flag
    if data.data == 'You have won!' or data.data == 'You have lost':
        print(data.data)
        rospy.signal_shutdown()
    
    print(data.data)
    counter = counter + 1

    if counter == 9 :
        counter = 0
        flag = 1
    

def playerinput(pub):
    message = input("Rock's Attack:")
    pub.publish(f'Rock {message}')
    message = input("Thunder's Attack:")
    pub.publish(f'Thunder {message}')
    message = input("Wind's Attack:")
    pub.publish(f'Wind {message}')
    







if __name__ == "__main__":
    try:
        player()
    except rospy.ROSInterruptException:
        pass
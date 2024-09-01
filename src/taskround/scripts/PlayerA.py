#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String




def player():
    global counter
    global flag
    counter = 0
    flag = 0
    
    
    rospy.init_node('PlayerA',anonymous=False) #intializing the node
    pub = rospy.Publisher('playerA_line', String, queue_size=10)
    rospy.Subscriber('hitpoint_senderA', String, handleinput)
    print("Waiting for connection")
    rospy.sleep(5)
    pub.publish("Player A connected!")
    
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
    message = input("Fire's Attack:")
    pub.publish(f'Fire {message}')
    message = input("Water's Attack:")
    pub.publish(f'Water {message}')
    message = input("Earth's Attack:")
    pub.publish(f'Earth {message}')
    







if __name__ == "__main__":
    try:
        player()
    except rospy.ROSInterruptException:
        pass
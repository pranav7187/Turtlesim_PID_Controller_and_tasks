#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String








def server():
    global inputcounter1
    global inputcounter2
    global flag
    
    global Fire
    global Water
    global Earth
    global Rock
    global Thunder
    global Wind
    #player A
    Fire = 300
    Water = 400
    Earth = 500

    #player B
    Rock = 300
    Thunder = 400
    Wind = 500
    flag = 0
    inputcounter1 = 0
    inputcounter2 = 0

   
    
    
    rospy.init_node('server',anonymous=False) #intializing the node
    pubA = rospy.Publisher('hitpoint_senderA',String, queue_size=10)
    pubB = rospy.Publisher('hitpoint_senderB',String, queue_size=10)
    rospy.Subscriber('playerB_line', String, input_playerB)
    rospy.Subscriber('playerA_line', String, input_playerA)
    print("Game started successfully !")
    print("All topics present !")
    print("Connecting to players")
    rate = rospy.Rate(10)
    
    
    while not rospy.is_shutdown():
        if flag == 1:
            hitpoint_senderA(pubA)
            flag = 0
            rate.sleep()
            


        elif inputcounter2 == 3 :
            hitpoint_senderA(pubA)
            inputcounter2 = 0


            rate.sleep()
        
        
        elif inputcounter1 == 3 :
            hitpoint_senderB(pubB)
            inputcounter1 = 0
            rate.sleep()
        



        
            
        
        
        

 
        
        
        if (Fire == 0 and Water==0 and Earth==0)or(Rock==0 and Thunder == 0 and Wind ==0) :
            if Fire == 0 and Water == 0 and Earth == 0:
                print("Player B has won !")
                pubB.publish("You have won!")
                pubA.publish("You have lost")
                rospy.signal_shutdown()
            elif Rock == 0 and Thunder == 0 and Wind == 0 :
                print("Player A has won")
                pubA.publish("You have won!")
                pubB.publish("You have lost")
                rospy.signal_shutdown()
                

        



def hitpoint_senderA(pub):
    #this is the function that will send hitpoints to node A
    global Fire
    global Water
    global Earth
    global Rock
    global Thunder
    global Wind
    pub.publish('Player A:')
    pub.publish(f'Fire : {Fire}')
    pub.publish(f'Water : {Water}')
    pub.publish(f'Earth: {Earth}')
    pub.publish('Player B:')
    pub.publish(f'Rock : {Rock}')
    pub.publish(f'Thunder : {Thunder}')
    pub.publish(f'Wind: {Wind}')
    pub.publish('Please enter input Player A:')

    
    return

def hitpoint_senderB(pub):
    #this is the function that will send hitpoints to node B
    global Fire
    global Water
    global Earth
    global Rock
    global Thunder
    global Wind
    pub.publish('Player A:')
    pub.publish(f'Fire : {Fire}')
    pub.publish(f'Water : {Water}')
    pub.publish(f'Earth: {Earth}')
    pub.publish('Player B:')
    pub.publish(f'Rock : {Rock}')
    pub.publish(f'Thunder : {Thunder}')
    pub.publish(f'Wind: {Wind}')
    pub.publish('Please enter input Player B:')
    
    return

def input_playerA(data): # make cases for player A input
    global Fire
    global Water
    global Earth
    global Rock
    global Thunder
    global Wind
    global flag
    global inputcounter1
    global inputcounter2

    if data.data == 'Fire 1' and Fire != 0:
        Rock = Rock - 30
        Thunder = Thunder - 30
        Wind = Wind - 30
        if Rock < 0 :
            Rock = 0 
        if Wind < 0 :
            Wind = 0 
        if Thunder < 0 :
            Thunder = 0
        inputcounter1 = inputcounter1 + 1
    
    elif data.data == 'Water 1' and Water != 0 :
        Rock = Rock - 40
        Thunder = Thunder - 40
        Wind = Wind - 40
        if Rock < 0 :
            Rock = 0 
        if Wind < 0 :
            Wind = 0 
        if Thunder < 0 :
            Thunder = 0
        inputcounter1 = inputcounter1 + 1
    
    elif data.data == 'Earth 1' and Earth != 0 :
        Rock = Rock - 50
        Thunder = Thunder - 50
        Wind = Wind - 50
        if Rock < 0 :
            Rock = 0 
        if Wind < 0 :
            Wind = 0 
        if Thunder < 0 :
            Thunder = 0
        inputcounter1 = inputcounter1 + 1
    
    elif data.data == 'Fire 2 Rock' and Fire != 0:
        Rock = Rock - 60
        if Rock < 0 :
            Rock = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Fire 2 Thunder' and Fire != 0:
        Thunder = Thunder - 60
        if Thunder < 60 :
            Thunder = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Fire 2 Wind' and Fire != 0:
        Wind = Wind - 60
        if Wind < 0 :
            Wind = 0
        inputcounter1 = inputcounter1 + 1

    elif data.data == 'Water 2 Rock' and Water != 0:
        Rock = Rock - 80
        if Rock < 0 :
            Rock = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Water 2 Thunder' and Water != 0:
        Thunder = Thunder - 80
        if Thunder < 0 :
            Thunder = 0 
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Water 2 Wind' and Water != 0:
        Wind = Wind -  80
        if Wind < 0 :
            Wind = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Earth 2 Rock' and Earth != 0:
        Rock = Rock - 100
        if Rock < 0:
            Rock = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Earth 2 Thunder' and Earth != 0:
        Thunder = Thunder - 100
        if Thunder < 0 :
            Thunder = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Earth 2 Wind' and Earth != 0:
        Wind = Wind - 100
        if Wind < 0 :
            Wind = 0
        inputcounter1 = inputcounter1 + 1
    elif data.data == 'Player A connected!':
        print(data.data) 
        flag = 1
    else:
        Rock = Rock
        Thunder = Thunder 
        Wind = Wind
        inputcounter1 = inputcounter1 + 1
    
    
    

    

def input_playerB(data): # make cases for player B input
    global Fire
    global Water
    global Earth
    global Rock
    global Thunder
    global Wind
    global inputcounter1
    global inputcounter2

    if data.data == 'Rock 1' and Rock != 0:
        Fire = Fire - 30
        Water = Water - 30
        Earth = Earth - 30
        if Fire < 0 :
            Fire = 0 
        if Water < 0 :
            Water = 0 
        if Earth < 0 :
            Earth = 0
        inputcounter2 = inputcounter2 + 1
    
    elif data.data == 'Thunder 1' and Thunder != 0:
        Fire = Fire - 40
        Water = Water - 40
        Earth = Earth - 40
        if Fire < 0 :
            Fire = 0 
        if Water < 0 :
            Water = 0 
        if Earth < 0 :
            Earth = 0
        inputcounter2 = inputcounter2 + 1
    
    elif data.data == 'Wind 1' and Wind != 0:
        Fire = Fire - 50
        Water = Water - 50
        Earth = Earth - 50
        if Fire < 0 :
            Fire = 0 
        if Water < 0 :
            Water = 0 
        if Earth < 0 :
            Earth = 0
        inputcounter2 = inputcounter2 + 1
    
    elif data.data == 'Rock 2 Fire' and Rock != 0:
        Fire = Fire - 60
        if Fire < 0 :
            Fire = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Rock 2 Water'and Rock != 0:
        Water = Water - 60
        if Water < 60 :
            Water = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Rock 2 Earth' and Rock != 0:
        Earth = Earth - 60
        if Earth < 0 :
            Earth = 0
        inputcounter2 = inputcounter2 + 1

    elif data.data == 'Thunder 2 Fire' and Thunder != 0:
        Fire = Fire - 80
        if Fire < 0 :
            Fire = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Thunder 2 Water' and Thunder != 0:
        Water = Water - 80
        if Water < 0 :
            Water = 0 
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Thunder 2 Earth' and Thunder != 0:
        Earth = Earth -  80
        if Earth < 0 :
            Earth = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Wind 2 Fire' and Wind != 0:
        Fire = Fire - 100
        if Fire < 0:
            Fire = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Wind 2 Water' and Wind != 0:
        Water = Water - 100
        if Water < 0 :
            Water = 0
        inputcounter2 = inputcounter2 + 1
    elif data.data == 'Wind 2 Earth' and Wind != 0:
        Earth = Earth - 100
        if Earth < 0 :
            Earth = 0 
        inputcounter2 = inputcounter2 + 1
    else:
        Fire = Fire
        Water = Water
        Earth = Earth
        inputcounter2 = inputcounter2 + 1

    
    


        


    
    

if __name__ == "__main__":
    try:

        server()
    except rospy.ROSInterruptException:
        pass
     
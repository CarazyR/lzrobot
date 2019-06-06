#! /usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import roslib; #roslib.load_manifest('mybot_navigation')
import rospy
import actionlib
import time
import socket
import os
import sys
from std_msgs.msg import String

def app_talker(words):
    pub = rospy.Publisher('speak_string', String, queue_size=1)
    rospy.init_node('app_talker', anonymous=True)
    rospy.loginfo(words)
    pub.publish(words)

if __name__ == '__main__':	
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_address = ("192.168.0.108",2139)
        print "Staring up on %s:%s" %  server_address
        sock.bind(server_address)
        sock.listen(5)
        app_talker('Hello,my name is Libo.')
        state = 0
        
        while True:
            print "waiting .........."
            connetion,client_address = sock.accept()
            while True:
    #try:
                print  "Connection from ",client_address
                data = connetion.recv(1024)
                print "Receive '%s'" % data
                # come to me at ponint 2.
                if ((data.find('come to me')!= -1)and (state == 0) ):
                    app_talker('OK,I am coming.')
                    param = '1'
                    os.system("python /home/crazyr/catkin_ws/src/lzrobot/scripts/send_simple_goal.py %s" % (param))
                    app_talker('What can I do for you?')
                    state = 1
                    time.sleep(2)
                # where is the book apple?
                if ((data.find('where')!= -1) and (data.find('apple')!= -1) and (state == 1)):
                    app_talker('Book Apple is on the bookshelf number five. May I get you there?')
                    state = 2
                    time.sleep(2)
                # yes
                if (((data.find('yes')!= -1) or (data.find('okay')!= -1))and (state == 2)):
                    app_talker('Ok! Follow me.')
                    param = '2'
                    os.system("python /home/crazyr/catkin_ws/src/lzrobot/scripts/send_simple_goal.py %s" % (param))
                    app_talker('Arrived! The book is on second floor of the bookshelf.')
                    time.sleep(5)
                    state = 3
                    app_talker('Is there other book you want to find?')
                    time.sleep(2)

                if ((data.find('no')!= -1) and (state == 3)):
                    app_talker('Ok! Goodbye!')
                    param = '3'
                    os.system("python /home/crazyr/catkin_ws/src/lzrobot/scripts/send_simple_goal.py %s" % (param))
                    time.sleep(1)
                    state = 0
                    app_talker('mission complete!')
                    time.sleep(2)
                    app_talker('I have one more thing to say.')
                    time.sleep(2)
                    app_talker('傅老師是最帥的！祝大家新年快樂！')

    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"
        connetion.close()      
        #finally:      
            #print "Receive '%s'" % data
            #connetion.close()

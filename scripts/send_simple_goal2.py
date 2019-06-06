#!/usr/bin/env python
#vim: set fileencoding:utf-8
import roslib; 
#roslib.load_manifest('mybot_navigation')
import rospy
import actionlib
import time
from std_msgs.msg import String
#move_base_msgs
from move_base_msgs.msg import *
import socket

#move_base_msgs
from move_base_msgs.msg import *
class Socket:
    def __init__(self, input_port):
        self.port = input_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(None)
        self.s.bind(('', self.port))
        self.s.listen(5000)

    def accept_socket(self):
        conn, addr = self.s.accept()
        conn.settimeout(None)
        print 'Server start, connected by ', addr

def simple_move(px, py, rz, rw):
    pub = rospy.Publisher('speak_string', String, queue_size=1)
    rospy.init_node('simple_move')

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()

    #set goal
    goal.target_pose.pose.position.x = px
    goal.target_pose.pose.position.y = py
    goal.target_pose.pose.orientation.z = rz
    goal.target_pose.pose.orientation.w = rw
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    #start listner
    sac.wait_for_server()

    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()

    rate = rospy.Rate(1)
    
    hello_str = "灵风大帅哥"
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    #rate.sleep()


if __name__ == '__main__':
    try:
        #for send
	     #   socket_server.conn.send("Message rescived !!")

        #for receive
	     #   global socket_server
	      #  socket_server = Socket(8001)
	       # print 'Socket Defined'
	       # socket_server.accept_socket()
	       # info = socket_server.conn.recv(1024)
	       # print 'info from Socket: ', info

        #pub.publish("hello")
        #talker("get the goal.")
        #time.sleep(2)
        #simple_move(4.363,0.035,0.416,0.910) #MD
        #simple_move(3.480,-0.957,0.533,0.845)
        talker("傅老师 is too handsome"）
        time.sleep(1)
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"

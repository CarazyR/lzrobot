#!/usr/bin/env python
#vim: set fileencoding:utf-8
import roslib; 
#roslib.load_manifest('mybot_navigation')
import rospy
import actionlib
import time
import sys
from std_msgs.msg import String
#move_base_msgs
from move_base_msgs.msg import *

def simple_move(px,py,rz,rw):

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

def shut():
    print "shutdown"

if __name__ == '__main__':
    try:
        #simple_move(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        #time.sleep(2)
        #print "move_base '%s','%s','%s','%s'" % (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        if sys.argv[1]=='1':
            time.sleep(1)
            simple_move(3.351,-1.222,-0.026,0.999)#center
            simple_move(8.279,-0.618,0.999,0.050)#point 2
            time.sleep(1)
        if sys.argv[1]=='2':
            time.sleep(1)
            simple_move(3.351,-1.222,-0.026,0.999)#center
            simple_move(3.009,0.768,-0.530,0.847)#point 1
            time.sleep(1)
        if sys.argv[1]=='3':
            time.sleep(1)
            simple_move(3.091,-3.139,0.278,0.960)#origin
            time.sleep(1)
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"

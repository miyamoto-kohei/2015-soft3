#!/usr\bin\env python
import roslib; roslib.load_manifest('beginer_tutorials')
import rospy
import actionlib
from beginer_tutorials.msg import *

class DoDishesServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, 
                                                   self.execute, False)
        self.server.start()

    def execute(self, goal):
        # Do lots of awesome groundbreaking robot stuff here
        print "Requesting dishwasher %d"%(goal.dishwasher_id)
        result = self.server.get_default()
        result.total_dishes_cleaned = 100
        print "Requesting dishes_cleaned %d"%(result.total_dishes_cleaned)
        self.server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node('do_dishes_server')
    server = DoDishesServer()
    rospy.spin()

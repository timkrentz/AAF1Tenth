#!/usr/bin/env python

import rospy
import numpy as np
import numpy.random as rand
import tf
from race.msg import drive_param
from geometry_msgs.msg import PoseStamped, Pose
from gazebo_msgs.msg import ModelStates
from gazebo_msgs.srv import GetModelState
from std_msgs.msg import Header

args = rospy.myargv()[1:]
racecar_name=args[0]
number_of_racecars=int(args[1])

pub = rospy.Publisher(racecar_name+"_position_gazebo", PoseStamped, queue_size=1)

racecar_pose = Pose()

def timer_callback(event):
    global racecar_pose
    msg = PoseStamped()
    msg.pose = racecar_pose
    pub.publish(msg)

# Gets the racecar pose from gazebo/model_states topic. Since Gazebo has multiple
# models (racecar, ground plane) we have to index for the "racecar".
def robot_pose_update(data):
    global racecar_pose
    global racecar_name
    global number_of_racecars
    names = data.name
    # Break out of this callback if racecar not properly initialized in Gazebo yet so that we don't see red error statements in Terminal about no index of "racecar" in names.
    if len(names) < number_of_racecars+1:
        return
    racecar_index = names.index(racecar_name)
    racecar_pose = data.pose[racecar_index]

if __name__ == "__main__":
    rospy.init_node("remap_gazebo_pose")
    # Set the update rate
    rospy.Timer(rospy.Duration(.025), timer_callback) # 40hz
    # Set subscribers
    rospy.Subscriber("gazebo/model_states", ModelStates, robot_pose_update)
    rospy.spin()

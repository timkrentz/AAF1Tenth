#!/usr/bin/env python
"""
@package 
@file Color_Camera_impl.py
"""
import rospy
import tf
import actionlib
from sensor_msgs.msg import Image
# protected region user include package begin #
import cv2
from cv_bridge import CvBridge, CvBridgeError
# protected region user include package end #
class Color_CameraImplementation(object):
    """
    Class to contain Developer implementation.
    """
    def __init__(self):
        """
        Definition and initialization of class attributes
        """
        #parameters
        self.camera_model = rospy.get_param("~camera_model","")
        self.port = rospy.get_param("~port","")
        self.racecar_name = rospy.get_param("~racecar_name","car_1")
        self.topic_pub_Image_Pub = rospy.get_param("~topic_pub_Image_Pub","")
        #publishers
        self.Image_Pub_ = rospy.Publisher(self.topic_pub_, Image, queue_size=1)
        self.out_Image_Pub = Image()
        self.out_Image_Pub_active = bool()

        # protected region user member variables begin #
        self.cap = cv2.VideoCapture(-1)
        self.cap.set(3,320)
        self.cap.set(4,240)
        self.cap.set(5,10)
        self.cap.set(12,100)
        self.bridge = CvBridge()
        # protected region user member variables end #

    


    def update(self, event):
        # protected region user update functions begin #
        ret, frame = self.cap.read()
        image = bridge.cv2_to_imgmsg(frame, encoding="passthrough")
        self.Image_Pub.publish(image)
        # protected region user update functions end #
        return

# protected region user additional functions begin #
# protected region user additional functions end #


def main():
    """
    @brief Entry point of the package.
    Instanciate the node interface containing the Developer implementation
    @return nothing
    """
    rospy.init_node("Color_Camera", anonymous=False)
    node = Color_CameraImplementation()
    rospy.Timer(rospy.Duration(1.0/10), node.update)
    rospy.spin()

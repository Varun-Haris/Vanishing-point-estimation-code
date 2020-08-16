# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:19:54 2020

@author: varun
"""
#!C:/Python/python.exe
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

arr = Floats()

def callback(data):
    global arr
    arr = data

rospy.init_node("arraySub", anonymous=True)
rospy.Subscriber("/vp_array", numpy_msg(Floats), callback)

while True:
    print(arr)

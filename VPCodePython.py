# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:38:17 2020

@author: varun
"""
#!C:/Python/python.exe
import matlab.engine, matlab
import numpy as np
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

eng = matlab.engine.start_matlab()

codeDir = "C:\\Users\\varun\\Desktop\\NCSU\\eccv_indoor-master\\eccv_indoor-master\\UIUC_Varsha\\SpatialLayout\\spatiallayoutcode\\"
imgDir = "C:\\Users\\varun\\Desktop\\NCSU\\eccv_indoor-master\\Cell Phone\\"
workDir = "C:\\Users\\varun\\Desktop\\NCSU\\eccv_indoor-master\\vanishing_point\\"

## Start ROS node
rospy.init_node('vanishingPoint', anonymous=True)
pub = rospy.Publisher("/vp_array", numpy_msg(Floats),queue_size=0)
r = rospy.Rate(10) # 10hz

## Adding the path into the python interpreter
eng.addpath(codeDir,nargout=0)
eng.addpath(codeDir+"ComputeVP\\",nargout=0)
i = 1

while not rospy.is_shutdown() and i < 9343:
    try:
        imageName = "img"+str(i)+".jpg"
        i+=10
        #_, frame = cam.read()
        #cv2.imwrite(imgDir+imageName, cv2.resize(frame, (640,360)))
        (boxlayout, surface_labels, resizefactor, vpdata) = eng.getspatiallayout(imgDir, imageName, workDir, nargout=4)
        arr = np.asarray(vpdata['vp']).astype('float').flatten()
        
        send = Floats()
        send.data = list(arr)
        pub.publish(send)
        r.sleep()
        
    except matlab.engine.MatlabExecutionError:
        print("Okay, I think something just went wrong there !")
# Vanishing-point-estimation-code

This is a python wrapper around the vanishing point estimation developed by Varsha Hedau (vhedau2@uiuc.edu). The original code is written in MATLAB and can be found here
https://github.com/wgchoi/eccv_indoor/tree/master/UIUC_Varsha/SpatialLayout

Required system configuration: -
1) Ubuntu 16.04 (with Python 3.x)
2) Matlab R2016 or above
3) Unity3D simulation engine with ROS#
4) ROS Kinetic

To run the python wrapper, the matlab engine for python has to be installed. Please refer here :- https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

This wrapper publishes the vanishing points as a numpy array over a ROS topic. To be able to subscribe this on Unity3D, a customized ROS# subscriber has to be written inside the camera component of the game engine. To connect Unity with ROS, an additional package called ROSBridgeClient has to be installed which translates ROS to ROS# for Unity3D to interpret appropriately. For more information please refer to https://github.com/MathiasCiarlo/ROSBridgeLib

Dataset used : - https://www.cs.cmu.edu/~halismai/wean/ 

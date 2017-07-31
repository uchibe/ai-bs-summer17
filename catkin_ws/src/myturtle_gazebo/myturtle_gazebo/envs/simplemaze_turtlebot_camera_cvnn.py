import gym
import rospy
import numpy as np
import cv2
import sys
import os
import random
import math

from gym import utils, spaces
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from gym.utils import seeding
from cv_bridge import CvBridge, CvBridgeError

class SimplemazeTurtlebotCameraCvNnEnv(gym.Env):

    def __init__(self):

        self.force_reset=True
        self.vel_pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=5)
        self.unpause=rospy.ServiceProxy('/gazebo/unpause_physics',Empty)
        self.pause=rospy.ServiceProxy('/gazebo/pause_physics',Empty)
        self.reset_proxy=rospy.ServiceProxy('/gazebo/reset_simulation',Empty)

        self.img_rows=32
        self.img_cols=32
        self.img_channels=1

    def calculate_observation(self,data):
        min_range=0.21 #0.21
        bumped=False
        #print(data.ranges)
        #np.save('datarange.npy',data.ranges)
        datarangenew=data.ranges[1:-1]
        for i, item in enumerate(datarangenew):#data.ranges):
            if(min_range>datarangenew[i]>0):
            #if(min_range>data.ranges[i]>0):
                bumped=True
        return bumped

    def _step(self,action):
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except rospy.ServiceException, e:
            print("/gazebo/unpause_physics service call failed")


        if action==0:#forward
            vel_cmd=Twist()
            vel_cmd.linear.x=0.2
            vel_cmd.angular.z=0.0
            self.vel_pub.publish(vel_cmd)
        elif action==1:#left
            vel_cmd=Twist()
            vel_cmd.linear.x=0.05
            vel_cmd.angular.z=0.2
            self.vel_pub.publish(vel_cmd)
        elif action==2:#right
            vel_cmd=Twist()
            vel_cmd.linear.x=0.05
            vel_cmd.angular.z=-0.2
            self.vel_pub.publish(vel_cmd)
        #elif action==3:#back
        #    vel_cmd=Twist()
        #    vel_cmd.linear.x=-0.2
        #    vel_cmd.angular.z=0.0
        #    self.vel_pub.publish(vel_cmd)

            
        data=None
        while data is None:
            try:
                data=rospy.wait_for_message('/scan',LaserScan,timeout=5)
            except:
                pass

        bumped=self.calculate_observation(data)
        #done=self.calculate_observation(data)

        depth_data=None
        success=False
        #cv_image=None
        image_data=None
        success_img=False
        

        while depth_data is None or success is False:
            try:
                #print(1.5)
                depth_data=rospy.wait_for_message('/camera/depth/image_raw',Image,timeout=5)
                h=depth_data.height
                w=depth_data.width
                cv_depth=CvBridge().imgmsg_to_cv2(depth_data,"passthrough")
                #np.save('cv_depth_nan.npy',cv_depth)
                cv_depth=np.nan_to_num(cv_depth)
                #np.save('cv_depth.npy',cv_depth)
                #print(cv_depth[h/2,w/2])
                if not (cv_depth[h/2,w/2]==178):
                    success=True
                else:
                    pass

            except:
                pass

        while image_data is None or success_img is False:
            try:
                #print(2)
                image_data=rospy.wait_for_message('/camera/rgb/image_raw',Image,timeout=5)
                h_img=image_data.height
                w_img=image_data.width
                cv_image=CvBridge().imgmsg_to_cv2(image_data,"bgr8")
                np.save('cv_image.npy',cv_image)
                #print(h_img)
                #print(w_img)
                #print(cv_image[h_img/2,w_img/2])
                if not (cv_image[h_img/2,w_img/2,0]==178 and cv_image[h_img/2,w_img/2,1]==178 and cv_image[h_img/2,w_img/2,2]==178):
                    success_img=True
                else:
                    pass

            except:
                pass

        #print(3)
        rospy.wait_for_service('/gazebo/pause_physics')

        try:
            self.pause()
        except rospy.ServiceException,e:
            print("/gazebo/pause_physics service call failed")

        cv_image_out=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        cv_image_out=cv2.resize(cv_image_out,(self.img_rows,self.img_cols))
        state_out=cv_image_out.reshape(1,cv_image_out.shape[0],cv_image_out.shape[1],1)
        

        hsv=cv2.cvtColor(cv_image,cv2.COLOR_BGR2HSV)
        red=cv2.inRange(hsv,np.array([0,100,100]),np.array([5,255,255]))
        img2,contours,hierarchy=cv2.findContours(red,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #print(4)

        if contours:
            cv2.drawContours(cv_image,contours,-1,(0,255,0),3)
            area=cv2.contourArea(contours[0])
            distance=1000/(math.sqrt(area)+1)
            #print("area="+str(area))
        else:
            pass
            #print("empty contours!")

        #cv2.imshow("image window",cv_image)
        #cv2.waitKey(3)
        done=False
        distance=10
        if not bumped:
            if contours:
                reward=1
                if 2.8<distance<3:
                    done=True
            else:
                reward=0
        else:
            reward=-1
            done=True
        #print(bumped)
        '''
        if not bumped:
            if contours:
                reward=1
            else:
                reward=0
        else:
            reward=-1
        '''        
        
        cv_depth=cv2.resize(cv_depth,(self.img_rows,self.img_cols))
        state=cv_depth.reshape(1,cv_depth.shape[0],cv_depth.shape[1],1)
        #done=False
        return state,reward,done,{}
        

    def _reset(self):

        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            self.reset_proxy()
        except rospy.ServiceException,e:
            print("/gazebo/reset_simulation service call failed")

        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except rospy.ServiceException,e:
            print("/gazebo/unpause_physics service call failed")

        depth_data=None
        success=False
        cv_depth=None
        image_data=None
        success_img=False
        cv_image=None

        while depth_data is None or success is False:
            try:
                depth_data=rospy.wait_for_message('/camera/depth/image_raw',Image,timeout=5)
                h=depth_data.height
                w=depth_data.width
                cv_depth=CvBridge().imgmsg_to_cv2(depth_data,"passthrough")
                cv_depth=np.nan_to_num(cv_depth)
                if not (cv_depth[h/2,w/2]==178):
                    success=True
                else:
                    pass

            except:
                pass

        while image_data is None or success_img is False:
            try:
                #print(2)
                image_data=rospy.wait_for_message('/camera/rgb/image_raw',Image,timeout=5)
                h_img=image_data.height
                w_img=image_data.width
                cv_image=CvBridge().imgmsg_to_cv2(image_data,"bgr8")
                #np.save('cv_image.npy',cv_image)
                #print(h_img)
                #print(w_img)
                #print(cv_image[h_img/2,w_img/2])
                if not (cv_image[h_img/2,w_img/2,0]==178 and cv_image[h_img/2,w_img/2,1]==178 and cv_image[h_img/2,w_img/2,2]==178):
                    success_img=True
                else:
                    pass

            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')

        try:
            self.pause()
        except rospy.ServiceException,e:
            print("/gazebo/pause_physics service call failed")

        cv_image_out=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        cv_image_out=cv2.resize(cv_image_out,(self.img_rows,self.img_cols))
        state_out=cv_image_out.reshape(1,cv_image_out.shape[0],cv_image_out.shape[1],1)
        

        cv_depth=cv2.resize(cv_depth,(self.img_rows,self.img_cols))
        state=cv_depth.reshape(1,cv_depth.shape[0],cv_depth.shape[1],1)
        return state

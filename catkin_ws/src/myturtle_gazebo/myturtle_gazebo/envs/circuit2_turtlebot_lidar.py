import gym
import rospy
import time
import numpy as np

from gym import utils, spaces
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from sensor_msgs.msg import LaserScan
from gym.utils import seeding

class Circuit2TurtlebotLidarEnv(gym.Env):

    def __init__(self):
        #print(1)
        rospy.init_node('testenv',anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.vel_pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=5)
        self.unpause=rospy.ServiceProxy('/gazebo/unpause_physics',Empty)
        self.pause=rospy.ServiceProxy('/gazebo/pause_physics',Empty)
        self.reset_proxy=rospy.ServiceProxy('/gazebo/reset_simulation',Empty)
        self.action_space=spaces.Discrete(3) #forward, left, right
        self.reward_range=(-np.inf,np.inf)
        self._seed()

    def shutdown(self):
        rospy.loginfo("Stop")
        self.vel_pub.publish(Twist())
        rospy.sleep(1)

    
    def discretize_observation(self,data,new_ranges):
        discretize_ranges=[]
        min_range=0.2
        done=False
        mod=len(data.ranges)/new_ranges
        for i,item in enumerate(data.ranges):
            if(i%mod==0):
                if data.ranges[i]==float('Inf') or np.isinf(data.ranges[i]):
                    discretize_ranges.append(6)
                elif np.isnan(data.ranges[i]):
                    discretize_ranges.append(0)
                else:
                    discretize_ranges.append(int(data.ranges[i]))
            if(min_range>data.ranges[i]>0):
                done=True
        return discretize_ranges,done

    def _seed(self,seed=None):
        self.np_random,seed=seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except rospy.ServiceException, e:
            print("/gazebo/unpause_physics service call failed")

        if action==0: #forward
            vel_cmd=Twist()
            vel_cmd.linear.x=0.3
            vel_cmd.angular.z=0.0
            self.vel_pub.publish(vel_cmd)
        elif action==1: #left
            vel_cmd=Twist()
            vel_cmd.linear.x=0.05
            vel_cmd.angular.z=0.3
            self.vel_pub.publish(vel_cmd)
        elif action==2: #right
            vel_cmd=Twist()
            vel_cmd.linear.x=0.05
            vel_cmd.angular.z=-0.3
            self.vel_pub.publish(vel_cmd)

        data=None
        while data is None:
            try:
                data=rospy.wait_for_message('/scan',LaserScan,timeout=5)
            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            self.pause()
        except rospy.ServiceException,e:
            print("/gazebo/pause_physics service call failed")

        #print(data)
        state,done=self.discretize_observation(data,5)

        if not done:
            if action==0:
                reward=5
            else:
                reward=1
        else:
            reward=-200

        return state, reward, done, {}

    def _reset(self):
        rospy.wait_for_service('/gazebo/reset_simulation')
        #print(4)
        try:
            self.reset_proxy()
        except rospy.ServiceException,e:
            print("/gazebo/reset_simulation service call failed")

        rospy.wait_for_service('/gazebo/unpause_physics')
        #print(5)
        try:
            self.unpause()
        except rospy.ServiceException,e:
            print("/gazebo/unpause_physics service call failed")

        data=None
        while data is None:
            try:
                data=rospy.wait_for_message('/scan',LaserScan,timeout=5)
            except:
                pass

        #print(data)
        #print(self.discretize_observation(data,5))
        rospy.wait_for_service('/gazebo/pause_physics')
        #print(6)
        try:
            self.pause()
        except rospy.ServiceException,e:
            print("/gazebo/pause_physics service call failed")

        state=self.discretize_observation(data,5)

        return state
            

#!/usr/bin/env python

import gym
import myturtle_gazebo
import memory
import numpy as np
import random
import rospy
from deepq import DeepQ
# from memory_profiler import profile

# @profile
def main():
    rospy.init_node('testcvenvsm', anonymous=False)
    env = gym.make('SimplemazeTurtlebotCameraCvNn-v0')
    outdir = 'experiment/'
    img_rows, img_cols, img_channels = env.img_rows, env.img_cols, env.img_channels

    env = gym.wrappers.Monitor(env, outdir, force=True)

    number_of_episodes = 400   # number of episodes in one experimental run
    max_steps_per_episode = 150   # maximum number of steps per episode

    alpha = 1e-3   # learning rate
    gamma = 0.99   # discount factor
    EXPLORE = 20000  # 100000
    epsilon0 = 0.5
    epsilonf = 0.01

    output_size = 3
    memory_size = 1000
    learnStart = 0   # The agent collects the data, but does not learn
    updateTarget = 450
    deepQ = DeepQ(output_size, memory_size, gamma, alpha, learnStart, img_rows, img_cols, img_channels)

    for iter in xrange(1):  # 1 experimental run
        epsilon = epsilon0
        deepQ.initNetworks()
        # deepQ.loadModel('0newModel_smcv.h5')
        # deepQ.loadTargetModel('0newModel_smcv.h5')

        rew = []
        stps = []
        wts = []
        losses = []
        batches = []
        qvalueep = []
        stepCounter = 0

        for ep in xrange(number_of_episodes):
            done = False
            o = env.reset()
            r_sum = 0
            loss = 0
            stp = 0
            qvalue = []
            epsilon = epsilon0 - (epsilon0 - epsilonf)/number_of_episodes*ep
            # epsilon = epsilon0

            for t in xrange(max_steps_per_episode):
                q = deepQ.getQValues(o)
                qvalue.append(q)
                a = deepQ.selectAction(q, epsilon)
                newO, r, done, info = env.step(a)
                deepQ.addMemory(o, a, r, newO, done)
                o = newO

                if stepCounter >= learnStart:
                    loss = deepQ.learnOnMini(True)

                if t == max_steps_per_episode:
                    done = True

                r_sum += r

                if done:
                    break

                stp += 1
                stepCounter += 1

                if stepCounter % updateTarget == 0:
                    deepQ.updateTargetNetwork()
                    deepQ.saveModel(str(iter) + 'newModel_smcv.h5')
                    print("The target network is updated")
            print("Episode: " + str(ep) + " Steps: " + str(stp) + " Total steps: " + str(stepCounter) + " Total rewards: " + str(r_sum) + " Epsilon: " + str(epsilon))
            # deepQ.printNetwork()
            losses.append(loss)
            stps.append(stp)
            rew.append(r_sum)
            qvalueep.append(qvalue)
            np.save(str(iter) + 'reward_smcv.npy', rew)
            np.save(str(iter) + 'step_smcv.npy', stps)
            np.save(str(iter) + 'loss_smcv.npy', losses)
            np.save(str(iter) + 'q_smcv.npy', qvalueep)
            env.close()

if __name__ == '__main__':
    main()

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

    episodes = 1   # 600
    steps = 1500   # 150

    alpha = 1e-3
    gamma = 0.99
    EXPLORE = 20000  # 100000
    epsilon0 = 0.5  # 0.5
    epsilonf = 0.01

    output_size = 3
    memory_size = 10000
    learnStart = 3000
    updateTarget = 3000
    deepQ = DeepQ(output_size, memory_size, gamma, alpha, learnStart, img_rows, img_cols, img_channels)

    for iter in xrange(1):
        epsilon = epsilon0   # 0.3236049
        deepQ.initNetworks()
        # deepQ.loadModel('0newModel_smcv_img_to259.h5')
        # deepQ.loadTargetModel('0newModel_smcv_img_to259.h5')

        rew = []
        stps = []
        wts = []
        losses = []
        batches = []
        qvalueep = []
        stpCounter = 0

        for ep in xrange(episodes):

            done = False
            o = env.reset()
            r_sum = 0
            loss = 0
            stp = 0
            qvalue = []

            for t in xrange(steps):
                q = deepQ.getQValues(o)
                # print(q)
                # print('target:')
                # print(deepQ.getTargetPredict(o))
                qvalue.append(q)
                a = deepQ.selectAction(q, epsilon)
                # np.save(str(t) + 'state.npy', o)
                # a = 0
                newO, r, done, info = env.step(a)
                deepQ.addMemory(o, a, r, newO, done)
                o = newO

                if epsilon > epsilonf and stpCounter > learnStart:
                    epsilon -= (epsilon0 - epsilonf)/EXPLORE

                if stpCounter >= learnStart:
                    if stpCounter <= updateTarget:
                        loss = deepQ.learnOnMini(False)
                    else:
                        loss = deepQ.learnOnMini(True)

                if(t == steps):
                    # print("reached the end")
                    done = True
                # deepQ.printNetwork()

                r_sum += r

                if done:
                    break

                stp += 1
                stpCounter += 1

                if stpCounter % updateTarget == 0:
                    deepQ.updateTargetNetwork()
                    deepQ.saveModel(str(iter) + 'newModel_smcv.h5')
                    print("model saved!")
            print("Ep:" + str(ep) + " Stps:" + str(stp) + " Stps_all:" + str(stpCounter) + " R:" + str(r_sum) + " Epsilon:" + str(epsilon))
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

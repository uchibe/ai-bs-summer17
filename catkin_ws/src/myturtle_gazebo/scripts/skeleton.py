#!/usr/bin/env python

import gym
import myturtle_gazebo
import random
import rospy


def main():
    rospy.init_node('testcvenvsm', anonymous=False)
    env = gym.make('SimplemazeTurtlebotCameraCvNn-v0')
    outdir = 'experiment/'
    img_rows, img_cols, img_channels = env.img_rows, env.img_cols, env.img_channels

    env = gym.wrappers.Monitor(env, outdir, force=True)

    number_of_episodes = 10   # number of episodes in one experimental run
    max_steps_per_episode = 150   # maximum number of steps per episode

    stepCounter = 0
    for ep in xrange(number_of_episodes):
        done = False
        o = env.reset()
        r_sum = 0
        stp = 0

        for t in xrange(max_steps_per_episode):
            a = random.randrange(3)   # uniform random
            newO, r, done, info = env.step(a)
            o = newO

            if t == max_steps_per_episode:
                done = True

            r_sum += r
            if done:
                break

            stp += 1
            stepCounter += 1

        print("Episode: " + str(ep) + " Steps: " + str(stp) + " Total steps: " + str(stepCounter) + " Total rewards: " + str(r_sum))

        env.close()

if __name__ == '__main__':
    main()

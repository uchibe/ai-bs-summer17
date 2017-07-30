import gym
import roboschool
import random

NUM_EPISODES = 10
NO_OP_STEPS = 30

env = gym.make('RoboschoolAtlasForwardWalk-v1')

print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

print(env.action_space)
print(env.action_space.high)
print(env.action_space.low)

for _ in range(NUM_EPISODES):
    observation, is_terminal = env.reset(), False
    print(_)

    while not is_terminal:
        env.render()
        # print(observation)
        last_observation = observation
        action = env.action_space.sample()
        observation, reward, is_terminal, info = env.step(action)

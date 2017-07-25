import gym
import random

NUM_EPISODES = 10

env = gym.make('CartPole-v0')

for _ in range(NUM_EPISODES):
    observation, is_terminal = env.reset(), False
    print(_)

    while not is_terminal:
        last_observation = observation
        action = env.action_space.sample()
        observation, reward, is_terminal, _ = env.step(action)
        env.render()

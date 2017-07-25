import gym
import random

NUM_EPISODES = 10
NO_OP_STEPS = 30

env = gym.make('SpaceInvaders-v0')

for _ in range(NUM_EPISODES):
    observation, is_terminal = env.reset(), False
    print(_)
    for _ in range(random.randint(1, NO_OP_STEPS)):
        last_observation = observation
        observation, _, _, _ = env.step(0)

    while not is_terminal:
        last_observation = observation
        action = env.action_space.sample()
        observation, reward, is_terminal, _ = env.step(action)
        env.render()

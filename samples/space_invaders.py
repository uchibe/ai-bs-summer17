import gym
import random

NUM_EPISODES = 10
NO_OP_STEPS = 30

env = gym.make('SpaceInvaders-v0')

for _ in range(NUM_EPISODES):
    terminal = False
    observation = env.reset()
    print(_)
    for _ in range(random.randint(1, NO_OP_STEPS)):
        last_observation = observation
        observation, _, _, _ = env.step(0)

    while not terminal:
        last_observation = observation
        action = env.action_space.sample()
        observation, reward, terminal, _ = env.step(action)
        env.render()

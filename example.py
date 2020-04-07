#!/usr/bin/env python
# encoding: utf-8

import gym
import gym_trivial

N_ITER = 10
           

if __name__ == "__main__":
    env = gym.make("trivial-v0")

    for i in range(N_ITER):
        x = env.step(env.action_space.sample())
        print(x)

#!/usr/bin/env python
# encoding: utf-8

import gym
import gym_trivial

N_ITER = 3
           

if __name__ == "__main__":
    env = gym.make("trivial-v0")

    for i in range(N_ITER):
        env.step(i)

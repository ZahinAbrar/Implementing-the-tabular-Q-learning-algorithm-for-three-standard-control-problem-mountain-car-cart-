# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:14:01 2019

@author: User 01
"""
import numpy as np
import gym
from gym import spaces
from gym.utils import seeding
env = gym.make("MountainCar-v0")
import random

pos  = [round(i,1) for i in (np.linspace(-1.2,0.6,19))]
vel = [round(i,2) for i in (np.linspace(-0.07,0.07,15))]

# creating an empty dictionary

Q_sa = {} 
for i in pos:
    for j in vel:
        for k in range(0,3):
            Q_sa[(i,j,k)] = 0
            
gamma = 1 # discounting factor
alpha = 0.1 # learning rate
           
# Q- update formula            
def Q_Update(state, observation,reward, action):
    max=-10000
    action_prime=0
    for j in range(0,3):
        if Q_sa[(observation[0],observation[1],j)]>max:
            max=Q_sa[(observation[0],observation[1],j)]
            action_prime=j

    Q_sa[(state[0],state[1],action)] = Q_sa[(state[0],state[1],action)] + gamma*(reward + alpha* Q_sa[(observation[0],observation[1],action_prime)]- Q_sa[(state[0],state[1],action)] )
    
    
# set the environment          
state = env.reset()  
# sampling the actions
action = env.action_space.sample()  

for i in range(0,20000):
    env.render()
    state[0]=round(state[0],1)  #  
    state[1]=round(state[1],2)      
    observation, reward, done, info = env.step(action)
    if reward == 1:
        print(Q_sa)
        break
    observation[0]=round(observation[0],1)  
    observation[1]=round(observation[1],2)
    Q_Update(state,observation, reward,action)
    state=observation
    explore  = random.uniform(0,1)
    epsilon = 0.05
    
    if explore > epsilon:
        
        max=-10000
        for j in range(0,3):
            if Q_sa[(state[0],state[1],j)]>max:
                max=Q_sa[(state[0],state[1],j)]
                action=j
    else:
        action=env.action_space.sample()


    
    
    
    

            

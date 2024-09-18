# Implementing the Tabular Q-Learning Algorithm for Mountain Car & CartPole

This project implements the **Tabular Q-Learning Algorithm** to solve reinforcement learning environments such as **Mountain Car** and **CartPole**. Q-learning is a model-free reinforcement learning algorithm that allows an agent to learn the optimal policy by interacting with an environment.

## Problem Description

### Mountain Car Environment

In the **Mountain Car** environment, the goal is to drive an underpowered car up a steep hill. The car needs to build up momentum by moving back and forth to eventually reach the goal at the top of the hill.

**State Space**: Continuous (Position, Velocity)  
**Action Space**: Discrete (Accelerate Left, No Acceleration, Accelerate Right)  
**Goal**: Drive the car to the top of the hill within a certain number of steps.


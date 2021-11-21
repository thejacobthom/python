import gym
from gym import Env
from gym.spaces import Discrete, Box, MultiDiscrete
import numpy as np
import random

from stable_baselines3 import PPO

#this incorporates a time reward for speedier solves
class ArrayEnv3(Env):
    
    def __init__(self, game_size):
    
        self.steps = 0
        self.game_array_size = game_size

        self.action_space = MultiDiscrete([self.game_array_size, self.game_array_size]) #10 possible xs and 10 possible ys

        high = np.array([1000] * self.game_array_size)
        low = np.array([0] * self.game_array_size)

        self.observation_space = Box(low, high, dtype=np.int16)

        #create an array of 100 random numbers between 0 and 1000
        self.state = np.random.randint(1000, size=(self.game_array_size))
        #game legnth of 100, shouldn't take more than 100 swaps

        self.end_array = np.copy(self.state)
        self.end_array.sort()

    #results when action taken
    def step(self, action):
        self.steps+=1 #keeps track of how many steps have been completed
        
        x_indice = action[0]
        y_indice = action[1]
        #print("From: {}\tX: {}\tY: {}".format(action, x_indice, y_indice))
        #save the original values in order for ease of reading
        x_original = self.state[x_indice]
        y_original = self.state[y_indice]

        #perform the swap
        temp = self.state[x_indice]
        self.state[x_indice] = self.state[y_indice]
        self.state[y_indice] = temp


        #to calculate reward we first need to know how many elements are in the right spot
        correct_position = np.count_nonzero(self.state == self.end_array)
        # let's only reward if x comes before y in the array to simplify learning
        if x_indice < y_indice:
            #reward is set to the amount of things in correct position with size relative to
            #0.9/100 so that when everything is in place, the reward == 0.9 and then may be added to if the
            # movement itself is correct
            reward = correct_position*(0.9/self.game_array_size)
            #check if value at x is greater than value at y
            if x_original > y_original:
                #if a large x value is moving down the array
                reward +=0.1
            else:
                #undesirable action i.e. swapping two equal values or moving a large value up in the array
                reward = -100

        elif x_indice > y_indice:
            #reward is set to the amount of things in correct position with size relative to
            #0.9/100 so that when everything is in place, the reward == 0.9 and then may be added to if the
            # movement itself is correct
            reward = correct_position*(0.9/self.game_array_size)
            #check if value at x is greater than value at y
            if x_original < y_original:
                #if a large x value is moving down the array
                reward +=0.1
            else:
                #undesirable action i.e. swapping two equal values or moving a large value up in the array
                reward = -100
        
        else:
            reward = -100 #swapping the same array place, useless action

        #check if game is over by comparing the current state to the final intended array
        
        if (self.state == self.end_array).all() == True:
            #add in extra reward based off of time it took to solve the array.
            if self.steps <= self.game_array_size:
                reward+=100
            else:
                reward += 100/self.steps
            
            done = True
        else:
            done = False

        #set placeholder for info
        info = {}

        #return all data
        return self.state, reward, done, info        


    #implement printing the array here
    def render(self):
        #print (np.count_nonzero(self.state == self.end_array))
        print(self.state)

    #reset/setup the environment
    def reset(self):
        #reset array to random numbers
        self.state = np.random.randint(1000, size=(self.game_array_size))

        #create a sorted array for our final state
        self.end_array = np.copy(self.state)
        self.end_array.sort()
        #reset game length

        return self.state
    
    
    

for i in range (1, 6):
    #del env
    #del model
    model = PPO.load("test5-0{}.zip".format(i))
    env = ArrayEnv3(5)

    obs = env.reset()
    episodes = 1000000
    negatives = 0
    total_moves = 0
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0 
        #print("--- original array ---")
        #env.render()
        #print("--- beginning sort ---")
        moves = 0
        #print("|", end="")
        while not done:
            total_moves+=1
            moves+=1
            action, _states = model.predict(state)
            state, reward, done, info = env.step(action)
            score+=reward
            #env.render()
        if score < 0:
            negatives+=1
        #print("Episode: {} \tMoves: {}\tScore: {}".format(episode, moves, score))

    print("For test5-0{}\t avg. moves: {}\t % Neg: {}".format(i, (total_moves/episodes), (negatives/episodes)*100))
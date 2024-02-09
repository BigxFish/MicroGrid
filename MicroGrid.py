import gym
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random

class Microgrid(Env):
    def __init__(self):
        
        #initalize
        self.P = 0
        self.Q = 0
        self.I = 0
        self.V = 0
        self.F = 0
        
        #Actions that can be taken i.e. increase, decrease
        self.action_space = Discrete(2)
        #Limits of values (since pu, between 0 and 2 for now *100)
        self.observation_space = Box(low=np.array([0]), high =np.array([200]))
        #Starting value
        self.V = 0  #pull in value from excel
        self.F = 0  #pull in value from excel
        
                
        
    def step(self, action):
        #apply ation
        if action == 0: #decrease
            self.V += -1
            self.F += -1
        elif action == 1: #increase
            self.V +=1
            self.F +=1
        
        #calculate reward
        if self.V >=90 or self.V <=110:
            reward_V = 1
        else:
            reward_V = -1
        
        if self.F >= 59 or self.F <= 61:
            reward_F = 1
        else:
            reward_F = -1
            
        #need a done condition
        
        #apply noise
        self.V += random.randint(-1,1)
        self.F += random.randint(-1,1)
        
        #info placeholder
        info = {}
        
        #return step information
        return self.state, reward, done, info
        
    def render(self):
        #if decide to create visual
        pass
    
    def reset(self):
        self.V = 0  #next value in the excel table?
        self.F = 0  #next value in he excel table?
        
        return self.V, self.F
        
        
        
        
import gym
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random



from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


from stable_baselines3 import PPO, DQN


class ArrayEnv(Env):
#git test

	def __init__(self):
		#game array size variable so i don't have to change it everywhere, will be used later, for now just a reminder
		self.game_array_size = 100

		#action space will be an integer between 0 and 10000 (so 9999 inclusive). this number will have its first two values be the x indice to swap and the last two values as the second indice to swap
		self.action_space = Discrete(10000)

		high = np.array([1000] * 100)  # 360 degree scan to a max of 4.5 meters
		low = np.array([0] * 100)
# low = 0, high = 1000, shape=(1, 100)
		#possible values for an array length 100, low end is 0, high end is 999. dtype set to be ONLY whole numbers (integers)

		#POSSIBLE USE unit16 FOR KERAS DQN METHOD
		self.observation_space = Box(low, high, dtype=np.int16)

		#create an array of 100 random numbers between 0 and 1000
		self.state = np.random.randint(1000, size=(1, 100))
		#game legnth of 100, shouldn't take more than 100 swaps

		self.end_array = np.copy(self.state)
		self.end_array.sort()

	#results when action taken
	def step(self, action):
		#print(self.state)
		#get the two values to swap
		x_indice = (action // (100))
		y_indice = (action % 100)

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
			reward = correct_position*(0.9/100)
			#check if value at x is greater than value at y
			if x_original > y_original:
				#if a large x value is moving down the array
				reward +=0.1
			else:
				#undesirable action i.e. swapping two equal values or moving a large value up in the array
				reward = -1
		# if y comes before x in the array
		else:
			reward = -1

		#check if game is over by comparing the current state to the final intended array
		if (self.state == self.end_array).all() == True:
			done = True
		else:
			done = False

		#set placeholder for info
		info = {}

		#return all data
		return self.state, reward, done, info		


	#implement printing the array here
	def render(self):
		print (np.count_nonzero(self.state == self.end_array))

	#reset/setup the environment
	def reset(self):
		#reset array to random numbers
		self.state = random.sample(range(1000), 100)

		#create a sorted array for our final state
		self.end_array = np.copy(self.state)
		self.end_array.sort()
		#reset game length

		return self.state



def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape = (1, 100)))

    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(25, activation='relu'))
    #model.add(Dense(1000, activation='relu'))
    #model.add(Dense(1000, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=500000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                  nb_actions=actions, nb_steps_warmup=100000, target_model_update=1e-2)
    return dqn




def main():

	env = ArrayEnv()

	model = PPO("MlpPolicy", env, verbose=1)

	model.learn(total_timesteps=5000000)

	model.save("TEST_MODEL_STABLEBASELINES1")

	obs = env.reset()
	while True:
		action, _states = model.predict(obs)
		obs, rewards, dones, info = env.step(action)
		env.render()


#############DQN WITH KERAS
	#create an object of the array env above
#	env = ArrayEnv()
#	env.reset()
#	states = env.observation_space.shape
#	actions = env.action_space.n


#	model = build_model(states, actions)
#
#	dqn = build_agent(model, actions)
#
#	dqn.compile(Adam(lr=1e-3), metrics=['mae'])
#
#	dqn.fit(env, nb_steps=150000, visualize=False, verbose=1)
#
#	scores = dqn.test(env, nb_episodes=100, visualize=False)
#	print(np.mean(scores.history['episode_reward']))
#
#	dqn.save_weights('DQN_Overnight_Test', overwrite=True)

if __name__ == "__main__":
	main()

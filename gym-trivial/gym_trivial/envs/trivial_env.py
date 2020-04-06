from gym import spaces
import gym


class Trivial (gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__ (self):
        self.reset()
        #self.action_space = spaces.Discrete(1)
        #self.observation_space = spaces.Box(low, high, dtype=np.float32)


    def reset (self):
        """
        Reset the state of the environment and returns an initial observation.

        Returns
        -------
        observation (object): the initial observation of the space.
        """
        self.state = [0, 0]
        self.reward = 0
        self.done = 0
        self.info = {}

        return self.state


    def check (self):
        if self.state[0] == 1 and self.state[1] == 1:
            return True
        else:
            return False


    def step (self, action):
        """
        The agent takes a step in the environment.

        Parameters
        ----------
        action : int

        Returns
        -------
        state, reward, done, info : tuple
            state (object) :
                an environment-specific object representing your observation of
                the environment.

            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.

            done (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)

            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        if self.done == 1:
            print("game over")
            return [self.state, self.reward, self.done, self.info]

        else:
            pos = action % len(self.state)

            if self.state[pos] != 0:
                print("Invalid Step")
                return [self.state, self.reward, self.done, self.info]
            else:
                self.state[pos] = 1
                self.render()


        if self.check():
            self.reward = 100
            self.done = 1;
            print("win")

        return [self.state, self.reward, self.done, self.info]


    def render (self, mode="human"):
        print(self.state)

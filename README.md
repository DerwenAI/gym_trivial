# gym_trivial

A trivial implementation of an [OpenAI Gym](http://gym.openai.com/)
environment, to illustrate and explore the baseline operations.


## Usage

Clone the repo and connect into its top level directory.
Then run:

```
pip install -r requirements.txt
pip install -e gym-trivial

python example.py
```

If you want to use this environment to train a policy in 
[RLlib](https://ray.readthedocs.io/en/latest/rllib.html)
the first install via:

```
pip install git+git://github.com/DerwenAI/gym_trivial.git#egg=pkg&subdirectory=gym-trivial
```

Then after launching [Ray](https://ray.io/) run:

```
from gym_trivial.envs.trivial_env import Trivial
from ray.tune.registry import register_env

register_env("trivial-v0", lambda config: Trivial())
```


## Kudos

h/t:

  - <https://github.com/apoddar573/Tic-Tac-Toe-Gym_Environment/>
  - <https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa>
  - <https://github.com/openai/gym/blob/master/docs/creating-environments.md>
  - <https://stackoverflow.com/questions/45068568/how-to-create-a-new-gym-environment-in-openai>

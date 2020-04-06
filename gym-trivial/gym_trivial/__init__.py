from gym.envs.registration import register

register(
    id="trivial-v0",
    entry_point="gym_trivial.envs:Trivial",
)

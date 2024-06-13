import random

import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
import time

# look here! https://towardsdatascience.com/q-learning-for-beginners-2837b777741
# Initialize the FrozenLake environment
env = gym.make("CliffWalking-v0")

# Q-learning parameters
alpha = 0.6  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.3  # Exploration rate (at the beginning it shouldn't be too low!!!!)
num_episodes = 3000
max_steps = 1000

# Initialize the Q-table with zeros
q_table = np.zeros((env.observation_space.n, env.action_space.n))


# Function to choose the next action
def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Explore
    else:
        return np.argmax(q_table[state, :])  # Exploit


# Training the agent
rewards = []

for _ in range(num_episodes):
    # if episode % 100 == 0:
    #     print(f"Running episode {episode}/{num_episodes}")
    state = env.reset()[0]
    total_rewards = 0

    for _ in range(max_steps):
        action = choose_action(state)
        new_state, reward, done, truncated, info = env.step(action)

        # Update Q-table
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action]
        )

        state = new_state
        total_rewards += reward

        if done:
            break

    rewards.append(total_rewards)


print("Q-table after training:")
print(q_table)

# Plotting the results
plt.plot(range(num_episodes), rewards)
plt.xlabel("Episodes")
plt.ylabel("Rewards")
plt.title("Q-learning on CliffWalking-v0")
plt.show()

# Testing the trained agent
total_test_episodes = 100
total_test_rewards = 0

for _ in range(total_test_episodes):
    state = env.reset()[0]
    episode_rewards = 0

    for _ in range(max_steps):
        action = np.argmax(q_table[state, :])
        new_state, reward, done, truncated, info = env.step(action)

        episode_rewards += reward
        state = new_state

        if done:
            break

    total_test_rewards += episode_rewards

print(
    f"Average reward over {total_test_episodes} test episodes: {total_test_rewards / total_test_episodes}"
)


# Extract and print the best policy
def extract_policy(q_table):
    policy = []
    for state in range(env.observation_space.n):
        best_action = np.argmax(q_table[state])
        policy.append(best_action)
    return policy


def action_to_char(action):
    return ["L", "D", "R", "U"][action]


policy = extract_policy(q_table)
policy_moves = [action_to_char(action) for action in policy]

print("Best policy moves:")
new_moves = [policy_moves[i : i + 12] for i in range(0, len(policy_moves), 12)]
for new_move in new_moves:
    print(new_move)


mapa = gym.make("CliffWalking-v0", render_mode="human")
mapa.reset()
print(mapa.render())

time.sleep(5)

env.close()

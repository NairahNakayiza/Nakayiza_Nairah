import numpy as np
import random

# Environment setup
road_length = 10
goal_position = road_length - 1

# Actions
LEFT = 0
STAY = 1
RIGHT = 2
actions = [LEFT, STAY, RIGHT]

# Q-table initialization
q_table = np.zeros((road_length, len(actions)))

# Hyperparameters
alpha = 0.1      
gamma = 0.9       
epsilon = 0.2     
episodes = 1000

# Training
for episode in range(episodes):
    position = 0  # Start position

    while position != goal_position:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)  
        else:
            action = np.argmax(q_table[position])  

        # Take action
        if action == LEFT:
            new_position = max(0, position - 1)
        elif action == STAY:
            new_position = position
        elif action == RIGHT:
            new_position = min(road_length - 1, position + 1)

        # Reward system
        if new_position == goal_position:
            reward = 10
        else:
            reward = -1

        # Update Q-table
        q_table[position, action] = q_table[position, action] + alpha * (
            reward + gamma * np.max(q_table[new_position]) - q_table[position, action]
        )

        position = new_position

# learned Q-table
print("Trained Q-Table:")
print(q_table)

# Test the trained agent
position = 0
steps = 0
print("\nAgent path:")
while position != goal_position and steps < 20:
    print("Position:", position)
    action = np.argmax(q_table[position])
    if action == LEFT:
        position = max(0, position - 1)
    elif action == STAY:
        pass
    elif action == RIGHT:
        position = min(road_length - 1, position + 1)
    steps += 1

print("Final Position:", position)
if position == goal_position:
    print("Success: Crossed the road!")
else:
    print("Failed: Did not reach the goal.")

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def monty_hall_simulation(switch, num_trials):
    win_count = 0

    for _ in range(num_trials):
        # Randomly place the car behind one of the doors (index 0, 1, or 2)
        car_position = random.randint(0, 2)
        
        # Contestant randomly picks a door (index 0, 1, or 2)
        contestant_choice = random.randint(0, 2)
        
        # Monty reveals a goat by opening one of the remaining doors
        remaining_doors = [i for i in range(3) if i != contestant_choice and i != car_position]
        monty_opens = random.choice(remaining_doors)
        
        # If the contestant switches, they choose the door that is neither their original choice nor Monty's opened door
        if switch:
            final_choice = [i for i in range(3) if i != contestant_choice and i != monty_opens][0]
        else:
            final_choice = contestant_choice

        # Count a win if the contestant's final choice is the car
        if final_choice == car_position:
            win_count += 1

    # Return the win percentage
    return win_count / num_trials

# Run the simulation
num_trials = 10000
win_rate_switch = monty_hall_simulation(switch=True, num_trials=num_trials)
win_rate_stay = monty_hall_simulation(switch=False, num_trials=num_trials)

print(f"Winning rate if switching: {win_rate_switch * 100:.2f}%")
print(f"Winning rate if staying: {win_rate_stay * 100:.2f}%")


# In[ ]:


import random

# 1. Function to set up doors (one car and two goats)
def setup_doors():
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)  # Randomize door arrangement
    return doors

# 2. Function for Monty to open a door (always revealing a goat)
def monty_opens_door(doors, initial_choice):
    # Monty opens a door that is not the contestant's choice and has a goat
    available_doors = [i for i in range(3) if i != initial_choice and doors[i] == 0]
    monty_opens = random.choice(available_doors)
    return monty_opens

# 3. Function to handle switching decision
def make_final_choice(switch, initial_choice, monty_opens):
    if switch:
        # Switch to the remaining unopened door
        final_choice = [i for i in range(3) if i != initial_choice and i != monty_opens][0]
    else:
        # Stick with the initial choice
        final_choice = initial_choice
    return final_choice

# 4. Simulation function to run trials
def monty_hall_simulation(switch, num_trials):
    win_count = 0

    for _ in range(num_trials):
        # Step 1: Set up doors
        doors = setup_doors()
        
        # Step 2: Contestant makes an initial choice
        initial_choice = random.randint(0, 2)
        
        # Step 3: Monty opens a door with a goat
        monty_opens = monty_opens_door(doors, initial_choice)
        
        # Step 4: Contestant makes the final choice (whether to switch or stay)
        final_choice = make_final_choice(switch, initial_choice, monty_opens)
        
        # Check if the final choice is the car (i.e., a win)
        if doors[final_choice] == 1:
            win_count += 1

    # Return the percentage of wins
    return win_count / num_trials

# Run the simulation
num_trials = 10000
win_rate_switch = monty_hall_simulation(switch=True, num_trials=num_trials)
win_rate_stay = monty_hall_simulation(switch=False, num_trials=num_trials)

print(f"Winning rate if switching: {win_rate_switch * 100:.2f}%")
print(f"Winning rate if staying: {win_rate_stay * 100:.2f}%")


# I think the #2 should be " the rule of Monty"
# 
# I prefer the simplified code, I have not taken CS courses, so the simplified code is very easy for me to understand, especially the simplified code is shorter and very easy to understand

# In[ ]:


import random

# 1. Function to set up doors (one car and two goats)
def setup_doors():
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)  # Randomize door arrangement
    return doors

# 2. Function for Monty to open a door (always revealing a goat)
def monty_opens_door(doors, initial_choice):
    # Monty opens a door that is not the contestant's choice and has a goat
    available_doors = [i for i in range(3) if i != initial_choice and doors[i] == 0]
    monty_opens = random.choice(available_doors)
    return monty_opens

# 3. Function to handle switching decision
def make_final_choice(switch, initial_choice, monty_opens):
    if switch:
        # Switch to the remaining unopened door
        final_choice = [i for i in range(3) if i != initial_choice and i != monty_opens][0]
    else:
        # Stick with the initial choice
        final_choice = initial_choice
    return final_choice

# 4. Simulation function to run trials
def monty_hall_simulation(switch, num_trials):
    win_count = 0

    for _ in range(num_trials):
        # Step 1: Set up doors
        doors = setup_doors()
        
        # Step 2: Contestant makes an initial choice
        initial_choice = random.randint(0, 2)
        
        # Step 3: Monty opens a door with a goat
        monty_opens = monty_opens_door(doors, initial_choice)
        
        # Step 4: Contestant makes the final choice (whether to switch or stay)
        final_choice = make_final_choice(switch, initial_choice, monty_opens)
        
        # Check if the final choice is the car (i.e., a win)
        if doors[final_choice] == 1:
            win_count += 1

    # Return the percentage of wins
    return win_count / num_trials

# Run the simulation
num_trials = 10000
win_rate_switch = monty_hall_simulation(switch=True, num_trials=num_trials)
win_rate_stay = monty_hall_simulation(switch=False, num_trials=num_trials)

print(f"Winning rate if switching: {win_rate_switch * 100:.2f}%")
print(f"Winning rate if staying: {win_rate_stay * 100:.2f}%")


# In the chat process, ChatGPT's response speed is relatively fast, but in some difficult questions, ChatGPT's response speed will be a little slow. ChatGPT has helped me a lot in writing code, which may not be as good as I want when I am a little unclear, but it can also get the right code after prompting. But in math, ChatGPT would give wrong answers, for example, once in the process of simplifying a matrix, I found that the procedure given to me was wrong and the result was correct

# Last year, I found ChatGPT very useful and helped me a lot. This year, I learned STA130 course and MAT223 course. In these two courses, I tried to use ChatGPT to help me learn, but ChatGPT could not give me very accurate answers.

# https://chatgpt.com/share/66eba81c-9ea8-8000-b264-b37dc706f9c6

# I've read the course wiki-textbook, and Chat with ChatGPT

# https://chatgpt.com/share/66eba9d2-84f4-8000-adb2-af0d10552e75

# https://chatgpt.com/share/66eba9e5-3194-8000-8d04-6c6bad85fd50

# In[ ]:





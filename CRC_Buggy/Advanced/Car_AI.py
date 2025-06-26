from microbit import *
import random

s = 200  # Speed
t = 500  # Time (not used in this example)
iterations = 10 # Number of times the AI will learn
#This is the pins for the motor
motor1_1 = pin0
motor1_2 = pin1
motor2_1 = pin2
motor2_2 = pin14
#This is the pins for enabeling the motor
enable1 = pin8
enable2 = pin12
#This is variable contains the address for the i2c bus
address = 0x10
# Initial weights for the moves
forwards = 25
backwards = 25
rights = 25
lefts = 25

forwar = 25
backwar = 25
righ = 25
lef = 25

# These are the functions that control movement
def enable():
    enable1.write_digital(1)
    enable2.write_digital(1)
def forward():
    motor1_1.write_analog(1023)
    motor1_2.write_digital(0)
    motor2_1.write_analog(1023)
    motor2_2.write_digital(0)

def backward():
    motor1_1.write_analog(0)
    motor1_2.write_digital(1)
    motor2_1.write_analog(0)
    motor2_2.write_digital(1)

def right():
    motor1_1.write_analog(1023)
    motor1_2.write_digital(0)
    motor2_1.write_analog(0)
    motor2_2.write_digital(1)

def left():
    motor1_1.write_analog(0)
    motor1_2.write_digital(1)
    motor2_1.write_analog(1023)
    motor2_2.write_digital(0)
def stop():
    enable1.write_digital(0)
    enable2.write_digital(0)
    motor1_1.write_analog(0)
    motor1_2.write_digital(0)
    motor2_1.write_analog(0)
    motor2_2.write_digital(0)

# The list of actions
actions = [forward, backward, right, left]

# Initial weights for each action
weights = [forwards, backwards, lefts, rights]

b_weights = [forwar, backwar, lef, righ]
# Learning rate (how much to change the weights)
lr = 0.3

# Weighted choice function
def weighted_choice(moves, weights):
    total = sum(weights)
    rand = random.uniform(0, total) # Random number between 0 and the sum of weights
    cumulative = 0
    for i in range(len(moves)):
        cumulative += weights[i]
        if rand < cumulative:
            return i  # Return the index of the chosen move
def b_weighted_choice(moves, weights):
    total = sum(weights)
    rand = random.uniform(0, total) # Random number between 0 and the sum of weights
    cumulative = 0
    for i in range(len(moves)):
        cumulative += weights[i]
        if rand < cumulative:
            return i  # Return the index of the chosen move
        
for x in range(iterations):
    # Request Sensor 1
    i2c.write(address, b'\x01')  # Tell Arduino to send sensor 1 data
    received_data = i2c.read(address, 2)
    distance1 = (received_data[0] << 8) | received_data[1]  # Convert to integer
    # Request Sensor 2
    i2c.write(address, b'\x02')  # Tell Arduino to send sensor 2 data
    received_data = i2c.read(address, 2)
    distance2 = (received_data[0] << 8) | received_data[1]
    # Request Senosr 3
    i2c.write(address, b'\x03') # Tell Arduino to send sensor 3 data
    received_data = i2c.read(address, 2)
    distance3 = (received_data[0] << 8) | received_data[1]
    #Request Sensor 4
    i2c.write(address, 'b\x04')# Tell Arduino to send sensor 4 data
    received_data = i2c.read(address, 2)
    distance4 = (received_data[0] << 8) | received_data[1]
    
    selected_move_index = weighted_choice(actions, weights)
    selected_move = actions[selected_move_index]

    # Subtract a fixed portion of the learning rate from the other weights
    rate = lr / 3  # You can adjust this value as needed
    if distance1 < 15 and distance2 < 15:
        b_selected_move_index = b_weighted_choice(actions, b_weights)
        b_selected_move = actions[b_selected_move_index]
        b_selected_move()
        if distance1 < 15:
            b_weights[b_selected_move_index] -= lr
            if i != b_selected_move_index:
                b_weights[i] += rate
        else:
            for i in range(len(r_weights)):
                b_weights[b_selected_move_index] += lr
                if i != b_selected_move_index:
                    b_weights[i] -= rate
    elif distance2 < 15:
        distance3 = distance2
        for i in range(len(weights)):
            enable()
            selected_move()
            sleep(s)
            stop()
            if distance2 < distance3:
                weights[selected_move_index] -= lr
                if i != selected_move_index:
                     weights[i] += rate
            elif distance2 >= 15:
                weights[selected_move_index] += lr
                if i != selected_move_index:
                    weights[i] -= rate
    else:
        for i in range(len(weights)):
            enable()
            selected_move()
            stop()
            if distance1 < 15:
                weights[selected_move_index] -= lr
                if i != selected_move_index:
                    weights[i] += rate
            elif distance1 >= 15:
                weights[selected_move_index] += lr
                if i != selected_move_index:
                    weights[i] -= rate

    # Ensure weights do not go negative
    for i in range(len(weights)):
        if weights[i] < 0:
            weights[i] = 0

    # Normalize the weights to ensure they sum to 100
    total_weight = sum(weights)
    for i in range(len(weights)):
        weights[i] = (weights[i] / total_weight) * 100  # Normalize to keep sum = 100

    selected_move_index = weighted_choice(actions, weights)
    selected_move = actions[selected_move_index]
print(weights, selected_move_index)
print(b_weights)
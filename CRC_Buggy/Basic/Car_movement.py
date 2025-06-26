from microbit import *

# Motor control pins
motor1_1 = pin0
motor1_2 = pin1
motor2_1 = pin2
motor2_2 = pin14
enable1 = pin8
enable2 = pin12
s = 500
t = 2000
# Enable motors
def enable():
    enable1.write_digital(1)
    enable2.write_digital(1)

# Movement functions
def forward(distance):
    motor1_1.write_analog(1023)
    motor1_2.write_digital(0)
    motor2_1.write_analog(1023)
    motor2_2.write_digital(0)
    distance = distance * 50
    sleep(distance)

def backward(distance):
    motor1_1.write_analog(0)
    motor1_2.write_digital(1)
    motor2_1.write_analog(0)
    motor2_2.write_digital(1)
    distance = distance * 50
    sleep(distance)

def right_turn(distance):
    motor1_1.write_analog(1023)
    motor1_2.write_digital(0)
    motor2_1.write_analog(0)
    motor2_2.write_digital(1)
    d = 0.63/2
    sleep(d)

def left_turn(distance):
    motor1_1.write_analog(0)
    motor1_2.write_digital(1)
    motor2_1.write_analog(1023)
    motor2_2.write_digital(0)
    d = 0.63/2
    sleep(d)

def stop():
    motor1_1.write_analog(0)
    motor1_2.write_digital(0)
    motor2_1.write_analog(0)
    motor2_2.write_digital(0)

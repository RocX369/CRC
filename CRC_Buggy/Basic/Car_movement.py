from microbit import *

# This is the address for the slave
address = 0x10

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

# Check if Arduino is detected on I2C bus
devices = i2c.scan()
print("I2C devices found:", devices)
if address not in devices:
    print("Error: Arduino not found on I2C bus")

while True:
    if button_a.is_pressed():
        # Initialize distance lists
        distance1 = [0] * 5
        distance2 = [0] * 5
        distance3 = [0] * 5
        distance4 = [0] * 5
        sleep(t)
        try:
            for x in range(5):
                # Request Sensor 1 data
                i2c.write(address, b'\x01')
                sleep(10)
                received_data = i2c.read(address, 2)
                distance1[x] = (received_data[0] << 8) | received_data[1]

                # Request Sensor 2 data
                i2c.write(address, b'\x02')
                sleep(10)
                received_data = i2c.read(address, 2)
                distance2[x] = (received_data[0] << 8) | received_data[1]

                # Request Sensor 3 data
                i2c.write(address, b'\x03')
                sleep(10)
                received_data = i2c.read(address, 2)
                distance3[x] = (received_data[0] << 8) | received_data[1]

                # Request Sensor 4 data
                i2c.write(address, b'\x04')
                sleep(10)
                received_data = i2c.read(address, 2)
                distance4[x] = (received_data[0] << 8) | received_data[1]

            # Find the max distance
            d1 = max(distance1)
            d2 = max(distance2)
            d3 = max(distance3)
            d4 = max(distance4)
            distance1.remove(d1)
            distance2.remove(d2)
            distance3.remove(d3)
            distance4.remove(d4)
            average = sum(distance1) / len(distance1)
            average1 = sum(distance2) / len(distance2)
            average2 = sum(distance3) / len(distance3)
            average3 = sum(distance4) / len(distance4)
            mylist = [average, average1, average2, average3]
            d = max(mylist)
            # Determine movement
            if d == d1:
                move = forward
            elif d == d2:
                move = right_turn
            elif d == d3:
                move = backward
            elif d == d4:
                move = left_turn

            distance = d * 90 / 1000  # Convert distance
            # Execute movement
            print(distance, "seconds")
            display.show(distance)
            enable()
            move(d)
            stop()
            print("Max distance", d, "cm")
            display.show(d)
        except Exception as e:
            print("Error", e)
            sleep(t)
    if button_b.is_pressed():
        display.clear()
        break
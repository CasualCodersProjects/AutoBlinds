# Python program to demonstrate
# sys.argv

#List of arguments: driver number; direction; steps; time

# pins:
# 8: enable
# 12: leftStep
# 16: leftDirection
# 38: rightStep
# 40: rightDirection


import sys
import RPi.GPIO as GPIO
import time

print("Driver number:", sys.argv[1])
print("Direction:", sys.argv[2])    # LOW OPEN, HIGH CLOSE
print("Steps:", sys.argv[3])
print("Time:", sys.argv[4])

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.output(8, False)

#convert time to double
driver = int(sys.argv[1])
direction = sys.argv[2]
steps = int(sys.argv[3])
duration = float(sys.argv[4])
StepDelay = (duration/float(steps))/2.0



if direction == "open":
    GPIO.output(16, False)
    GPIO.output(40, False)
elif direction == "close":
    GPIO.output(16, True)
    GPIO.output(40, True)
else:
    print("Invalid direction")
    exit()


if driver == 1:
    for i in range(steps):
        GPIO.output(12, True)
        time.sleep(StepDelay)
        GPIO.output(12, False)
        time.sleep(StepDelay)

elif driver == 2:
    for i in range(steps):
        GPIO.output(38, True)
        time.sleep(StepDelay)
        GPIO.output(38, False)
        time.sleep(StepDelay)

else:
    print("Invalid driver number")
    exit()
    # for loop




'''for index in range(steps):
    if direction == "open":
        if(driver == 1):
            GPIO.output(16, True)
            GPIO.output(12, True)
            time.sleep(StepDelay)
            GPIO.output(12, False)
        elif(driver == 2):
            GPIO.output(40, True)
            GPIO.output(38, True)
            time.sleep(StepDelay)
            GPIO.output(38, False)
    elif direction == "close":
        if(driver == 1):
            GPIO.output(16, False)
            GPIO.output(16, True)
            GPIO.output(12, True)
            time.sleep(StepDelay)
            GPIO.output(12, False)
        elif(driver == 2):
            GPIO.output(40, False)
            GPIO.output(38, True)
            time.sleep(StepDelay)
            GPIO.output(38, False)
        
    else:
        print("Invalid direction")
        break
'''
GPIO.output(8, True)
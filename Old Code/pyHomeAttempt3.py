import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import keyboard
import time
import datetime
import string

STEPS = 8500	#steps (1/16)
TIME = 10		#seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.output(14, True)
time.sleep(1)

print("Open declaration\n")
def openBlinds():
    GPIO.output(14, 0)
    print("Enabling Stepper motor\n")
    GPIO.output(21, 0)
    print("Set direction\n")
    for i in range(STEPS):
        print("looping\n")
        GPIO.output(20, 1)
        time.sleep(float(TIME)/float(STEPS))
        GPIO.output(20, 0)
        time.sleep(float(TIME)/float(STEPS))
    GPIO.output(14, 1)
print("Close declaration\n")
def closeBlinds():
    GPIO.output(14, 0)
    GPIO.output(21, 1)
    for i in range(STEPS):
        GPIO.output(20, 1)
        time.sleep(float(TIME)/float(STEPS))
        GPIO.output(20, 0)
        time.sleep(float(TIME)/float(STEPS))
    GPIO.output(14, 1)


print("Closing Blinds using verbose logging\n")
closeBlinds()

time.sleep(30)

openBlinds()
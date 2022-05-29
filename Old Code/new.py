import RPi.GPIO as GPIO
import time

from RpiMotorLib import RpiMotorLib
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

while(True):
	GPIO.output(8, True)



GPIO.cleanup()

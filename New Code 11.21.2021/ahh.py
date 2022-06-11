import RPi.GPIO as GPIO
import time
import datetime


def spinMotor(steps):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)     # en1
    GPIO.setup(5, GPIO.OUT)    # step1
    GPIO.setup(3, GPIO.OUT)    # dir1

    GPIO.output(7, False)       # pull enable low
    GPIO.output(3, False)      # set direction
    for _ in range(steps):
        GPIO.output(5, True)
        time.sleep(0.0001)
        GPIO.output(5, False)
        time.sleep(0.0001)

    GPIO.output(7, True)
    GPIO.cleanup()
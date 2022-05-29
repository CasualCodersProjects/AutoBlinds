import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)     # en1
GPIO.setup(5, GPIO.OUT)    # step1
GPIO.setup(3, GPIO.OUT)    # dir1


GPIO.output(7, False)       # pull enable low
GPIO.output(3, False)      # set direction


for x in range(100):
    GPIO.output(5, True)
    time.sleep(0.01)
    GPIO.output(5, False)
    time.sleep(0.01)


GPIO.output(7, True)
GPIO.cleanup()
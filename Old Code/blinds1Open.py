import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
blinds1=GPIO.PWM(32, 50)

#blinds1.start(12)       #Open
blinds1.start(3)        #Close

sleep(6.75)
blinds1.start(0)
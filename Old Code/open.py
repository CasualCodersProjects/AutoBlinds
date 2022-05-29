import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

pwm0=GPIO.PWM(8, 50)

sleep(1)					#1 second delay
pwm0.start(12)				#open blinds
sleep(6.5)					#1 second delay
pwm0.stop()					#kill motor power
GPIO.cleanup()				#clean GPIO usage
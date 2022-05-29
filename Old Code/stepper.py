import RPi.GPIO as GPIO
import threading
import time

# import the library
from RpiMotorLib import RpiMotorLib



def leftBlind():
	left.motor_go(True, "1/16", 10000, 0.0001, False, 0.05)
	
def rightBlind():
	right.motor_go(True, "1/16", 10000, 0.0001, False, 0.05)
    

# Declare an named instance of class pass GPIO pins numbers
left = RpiMotorLib.A4988Nema(21, 20, (0,0,0), "A4988")
right = RpiMotorLib.A4988Nema(23, 18, (0,0,0), "A4988")

leftThread = threading.Thread(target=leftBlind, args=())
rightThread = threading.Thread(target=rightBlind, args=())

time.sleep(10)

leftThread.start()
rightThread.start()

time.sleep(0.5)

leftThread.join()
rightThread.join()




# call the function, pass the arguments
#left.motor_go(False, "1/16" , 100, .01, False, .05)
#right.motor_go(False, "1/16" , 100, .01, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
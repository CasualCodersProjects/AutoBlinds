import RPi.GPIO as GPIO
import threading

# import the library
from RpiMotorLib import RpiMotorLib
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.OUT)

    
#define GPIO pins
#GPIO_pins = (14, 15, 18) # Microstep Resolution MS1-MS3 -> GPIO Pin
#direction= 20       # Direction -> GPIO Pin
#step = 21      # Step -> GPIO Pin

# Declare an named instance of class pass GPIO pins numbers
motor1 = RpiMotorLib.A4988Nema(21, 20, (0,0,0), "A4988")
#motor2 = RpiMotorLib.A4988Nema(23, 18, (0,0,0), "A4988")

#GPIO.output(8, False);

# call the function, pass the arguments
motor1.motor_go(False, "1/16", 8000, 62.5e-6, False, 0)
#motor2.motor_go(True, "1/16", 20000, 0.0001, False, 10)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

class Stepper:
    def __init__(self, enable_pin, step_pin, dir_pin):
        '''Enable Pin: Pin to enable the stepper
        Step Pin: Send a square wave to this pin to step the motor
        Dir Pin: Pin to set the direction of the motor'''
        self.enable_pin = enable_pin
        self.step_pin = step_pin
        self.dir_pin = dir_pin

        # Set the pins to output mode
        GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)

    
    def spin_motor(self, steps, time):
        '''Steps: Number of steps to take. Polarity (+/-) sets the direction.
        Time: Overall time to accomplish the move'''
        # Enable the motor driver by pulling the enable pin low
        GPIO.output(self.enable_pin, GPIO.LOW)

        # Set the direction of the motor based on the polarity of steps
        if steps > 0:
            GPIO.output(self.dir_pin, GPIO.HIGH)
        elif steps < 0:
            GPIO.output(self.dir_pin, GPIO.LOW)

        # Calculate the delay between steps
        delay  = float(time) / float(steps)

        # Step the motor
        for _ in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(delay/2.0)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(delay/2.0)

        # Disable the motor driver by pulling the enable pin high
        GPIO.output(self.enable_pin, GPIO.HIGH)
import sys
import asyncio
import RPi.GPIO as GPIO


# Requires a step pin, enable pin
async def spinMotor(enable_pin, step_pin, dir_pin, steps, direction, time):
    # Enable the motor driver by pulling the enable pin low
    GPIO.output(enable_pin, GPIO.LOW)

    # # Set the direction of the motor
    # if direction == "CW" or direction == "cw":
    #     GPIO.output(dir_pin, GPIO.HIGH)
    # elif direction == "CCW" or direction == "ccw":
    #     GPIO.output(dir_pin, GPIO.LOW)
    # else:
    #     print("Invalid direction")
    #     return

    # Calculate the delay between steps
    delay  = float(time) / float(steps)

    # Step the motor
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        await asyncio.sleep(delay/2.0)
        GPIO.output(step_pin, GPIO.LOW)
        await asyncio.sleep(delay/2.0)
    
    # Disable the motor driver by pulling the enable pin high
    GPIO.output(enable_pin, GPIO.HIGH)

async def main():
    asyncio.gather(spinMotor(7, 5, 3, 200, "cw", 10))
    asyncio.gather(spinMotor(13, 15, 17, 200, "ccw", 20))


if __name__ == "__main__":
    # Check if the correct number of arguments were provided
    # if len(sys.argv) != 6:
    #     print("Usage: python3 async_motor_control.py <enable_pin> <step_pin> <dir_pin> <steps> <direction> <time>")
    #     sys.exit(1)

    # Get the arguments
    # enable_pin = int(sys.argv[1])
    # step_pin = int(sys.argv[2])
    # dir_pin = int(sys.argv[3])
    # steps = int(sys.argv[4])
    # direction = sys.argv[5]
    # time = float(sys.argv[6])

    # Setup the GPIO pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    # Spin the motor
    asyncio.run(main())

    # Cleanup the GPIO pins
    GPIO.cleanup()
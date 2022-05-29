import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import keyboard
import time
import datetime
import string

STEPS = 8500	#steps (1/16)
TIME = 10		#seconds

schedule = open("schedule.txt")
scheduleArray = schedule.read().splitlines()
schedule.close()
for x in scheduleArray:
  print(x) 

motor = RpiMotorLib.A4988Nema(21, 20, (0,0,0), "A4988")
#TRUE CLOSES
#FALSE OPENS

GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)
time.sleep(1)

def openBlinds():
    GPIO.output(14, 0)
    GPIO.output(21, 0)
    for i in range(STEPS):
        GPIO.output(20, 1)
        time.sleep(float(TIME)/float(STEPS))
        GPIO.output(20, 0)
        time.sleep(float(TIME)/float(STEPS))
    GPIO.output(14, 1)

def closeBlinds():
    GPIO.output(14, 0)
    GPIO.output(21, 1)
    for i in range(STEPS):
        GPIO.output(20, 1)
        time.sleep(float(TIME)/float(STEPS))
        GPIO.output(20, 0)
        time.sleep(float(TIME)/float(STEPS))
    GPIO.output(14, 1)

try:
    while (True):
        currTime = str(datetime.datetime.today().time())
        currTime = currTime[:5]
        date = datetime.datetime.today().weekday()

        if(str(currTime) == "00:00"):
            schedule = open("schedule.txt")
            scheduleArray = schedule.read().splitlines()
            schedule.close()
            time.sleep(60)

        if(date == 0 and currTime == scheduleArray[0]):
            print("Monday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 1 and currTime == scheduleArray[1]):
            print("Tuesday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 2 and currTime == scheduleArray[2]):
            print("Wednesday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 3 and currTime == scheduleArray[3]):
            print("Thursday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 4 and currTime == scheduleArray[4]):
            print("Friday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 5 and currTime == scheduleArray[5]):
            print("Saturday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)

        elif(date == 6 and currTime == scheduleArray[6]):
            print("Sunday Opening")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(False, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)
    
        elif (currTime == scheduleArray[7]):
            print("Closing")
            GPIO.output(14, False)
            time.sleep(1)
            motor.motor_go(True, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)
            time.sleep(1)
            GPIO.output(14, True)
            time.sleep(60)
            
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
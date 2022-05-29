"""
Since this project is not intended for external use, Blinds 1, 2, and 3 are defined as follows.
Blinds 1 is directly right of the closet, above the left half of the dresser. Blinds 2 is right
of 1, above the right half of the dresser. Blinds 3 is directly above the bed, to the right of
blinds 2.

Pins for blinds 1, 2, and 3 are as follows: 32, 12, 33.
"""

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from time import sleep
import threading
import datetime
import string

STEPS = 8000	#steps (1/16)
TIME = 10		#seconds

#mymotortest = RpiMotorLib.A4988Nema(21, 20, (0,0,0), "A4988")
left = RpiMotorLib.A4988Nema(21, 20, (0,0,0), "A4988")
right = RpiMotorLib.A4988Nema(23, 18, (0,0,0), "A4988")

def leftBlind(direction):
	left.motor_go(direction, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)

def rightBlind(direction):
	right.motor_go(direction, "1/16", STEPS, float(TIME)/float(STEPS), False, 0)

openLeftThread = threading.Thread(target=leftBlind, args=(False,))
openRightThread = threading.Thread(target=rightBlind, args=(False,))
closeLeftThread = threading.Thread(target=leftBlind, args=(True,))
closeRightThread = threading.Thread(target=rightBlind, args=(True,))

def openBlinds():
	#implementing states as a method of preventing multiple opens/closes. Open is 1; closed is 0;
	state = open("state.txt")
	currState = state.read()
	state.close()

	if (currState == "0"):
		state = open("state.txt","w+")
		state.write("1")
		state.close()
		print("Entered open state on " + str(date) + " at " + str(time))
		GPIO.output(14, False)
		openLeftThread.start()
		openRightThread.start()
		openLeftThread.join()
		openRightThread.join()
		GPIO.output(14, True)
		sleep(60)
				
	elif (currState == "1"):
		print("Already open on " + str(date) + " at " + str(time))
		sleep(60)
		
def closeBlinds():
	state = open("state.txt")
	currState = state.read()
	state.close()

	if (currState == "1"):
		state = open("state.txt","w+")
		state.write("0")
		state.close()
		print("Entered closed state on " + str(date) + " at " + str(time))
		GPIO.output(14, False)
		closeLeftThread.start()
		closeRightThread.start()
		closeLeftThread.join()
		closeRightThread.join()
		GPIO.output(14, True)
		sleep(60)
		
	elif (currState == "0"):
		print("Already closed on " + str(date) + " at " + str(time))
		sleep(60)

#start initialization
schedule = open("schedule.txt")

scheduleArray = schedule.read().splitlines()
monOpen = scheduleArray[0]
tuesOpen = scheduleArray[1]
wedsOpen = scheduleArray[2]
thusOpen = scheduleArray[3]
friOpen = scheduleArray[4]
satOpen = scheduleArray[5]
sunOpen = scheduleArray[6]
allClose = scheduleArray[7]
print(monOpen, tuesOpen, wedsOpen, thusOpen, friOpen, satOpen, sunOpen, allClose)
#initialize the schedule into RAM.


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.output(14, True)
#setup the GPIO Pinout



date = datetime.datetime.today().weekday()     #get the date for when the program starts, and then inform the user.
print ("Today is the " + str(date) + "th day of the week, where monday is 0 and sunday is 6.")
#end initialization

try:
    while (True):
        time = str(datetime.datetime.today().time())
        time = time[:5]
        date = datetime.datetime.today().weekday()

        if(date == 0 and str(time) == monOpen):
            openBlinds()

        elif(date == 1 and str(time) == tuesOpen):
            openBlinds()

        elif(date == 2 and str(time) == wedsOpen):
            openBlinds()

        elif(date == 3 and str(time) == thusOpen):
            openBlinds()

        elif(date == 4 and str(time) == friOpen):
            openBlinds()

        elif(date == 5 and str(time) == satOpen):
            openBlinds()

        elif(date == 6 and str(time) == sunOpen):
            openBlinds()
    
        elif (str(time) == allClose):
            closeBlinds()
            
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

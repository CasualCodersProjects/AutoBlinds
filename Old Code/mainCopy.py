"""
Since this project is not intended for external use, Blinds 1, 2, and 3 are defined as follows.
Blinds 1 is directly right of the closet, above the left half of the dresser. Blinds 2 is right
of 1, above the right half of the dresser. Blinds 3 is directly above the bed, to the right of
blinds 2.

Pins for blinds 1, 2, and 3 are as follows: 32, 12, 33.
"""

import RPi.GPIO as GPIO
import RpiMotorLib
import time
import datetime
import string

def openBlinds():
	#implementing states as a method of preventing multiple opens/closes. Open is 1; closed is 0;
	state = open("state.txt")
	currState = state.read()
	state.close()

	state = open("state.txt","w+")
	if (currState == "0"):
		state.write("1")
		print("Entered open state on " + str(date) + " at " + str(time))
		'''blinds1.start(12)
		blinds2.start(12)
		sleep(6.5)
		blinds1.start(0)
		blinds2.start(0)
		sleep(60)'''
		
		
		
	elif (currState == "1"):
		print("Already open on " + str(date) + " at " + str(time))
		
	state.close()

def closeBlinds():
	state = open("state.txt")
	currState = state.read()
	state.close()

	state = open("state.txt","w+")
	if (currState == "1"):
		state.write("0")
		print("Entered closed state on " + str(date) + " at " + str(time))
		'''blinds1.start(3)
		blinds2.start(3)
		sleep(6.5)
		blinds1.start(0)
		blinds2.start(0)
		sleep(60)'''
		
		#new open logic. Something like:
		#de-assert pin 8, call both functions to open blinds, (re)assert pin 8
		
	elif (currState == "0"):
		print("Already closed on " + str(date) + " at " + str(time))
		
	state.close()



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

'''GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)             #Previuously 8
GPIO.setup(32, GPIO.OUT)            #Previously 10
GPIO.setup(33, GPIO.OUT)            #Previously 12

blinds1=GPIO.PWM(32, 50)
blinds2=GPIO.PWM(12, 50)
blinds3=GPIO.PWM(33, 50)'''

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
    blinds1.stop()
    blinds2.stop()
    blinds3.stop()
    GPIO.cleanup()

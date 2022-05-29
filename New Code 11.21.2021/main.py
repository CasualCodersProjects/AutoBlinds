import RPi.GPIO as GPIO
import time
import datetime

STEPS = 16000       # number of steps (1/16th microstepping)
TIME = 10

SCHEDULE = open("schedule.txt")
scheduleArray = SCHEDULE.read().splitlines()
SCHEDULE.close()
for x in scheduleArray:
  print(x)

# pins:
# 8: enable
# 12: leftStep
# 16: leftDirection
# 38: rightStep
# 40: rightDirection

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.output(8, True)

def openBlinds():             # open both sets of blinds
    #state = open("state.txt", "w+")
    #if state.read() == "0":
        #print("Actually openig")
    GPIO.output(8, False)
    GPIO.output(16, False)
    GPIO.output(40, False)
    for x in range(STEPS):
        GPIO.output(12, True)
        GPIO.output(38, True)
        time.sleep(float(TIME)/float(STEPS * 2))
        GPIO.output(12, False)
        GPIO.output(38, False)
        time.sleep(float(TIME)/float(STEPS * 2))
    GPIO.output(8, True)
        #state.write("1")
    #else:
    #    print("Already open")
    #state.close()

def closeBlinds():            # close both sets of blinds
    #state = open("state.txt", "w+")
    #if state.read() == "1":
    GPIO.output(8, False)
    GPIO.output(16, True)
    GPIO.output(40, True)
    for x in range(STEPS):
        GPIO.output(12, True)
        GPIO.output(38, True)
        time.sleep(float(TIME)/float(STEPS * 2))
        GPIO.output(12, False)
        GPIO.output(38, False)
        time.sleep(float(TIME)/float(STEPS * 2))
    GPIO.output(8, True)
    #    state.write("0")
    #state.close()

def log(direction):
    log = open("log.txt", "a")
    log.write(direction + "  " + str(datetime.datetime.now()) + "\n")
    log.close()

try:
    while(True):
        currTime = str(datetime.datetime.today().time())
        currTime = currTime[:5]
        date = datetime.datetime.today().weekday()
        
        if(str(currTime) == "00:00"):
            schedule = open("schedule.txt")
            scheduleArray = schedule.read().splitlines()
            schedule.close()
            time.sleep(60)
        
        if(currTime == scheduleArray[date]):
            print("Opening")
            log("Opening")
            openBlinds()
            time.sleep(60)

        elif(currTime == scheduleArray[7]):
            print("Closing")
            log("Closing")
            closeBlinds()
            time.sleep(60)
        
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
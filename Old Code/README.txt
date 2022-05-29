This is a python script meant to turn a $5 Pi Zero W or similar into a home automation system for blinds.

The overall system consists of servo motors and a pi, all connected together, and to the pulleys of the blinds.
This allows the Pi to move the servos at set times in a schedule.txt file.
This file needs to be made with open times for monday-sunday all on their own lines with no spaces.
There is a master close time at the bottom (8th line) of this file.
#!/usr/bin/env python
import os, eZ430
from time import sleep

verbose = 1 # set this to 0 if you don't want detailed log

watch = eZ430.watch("/dev/tty.usbmodem001") #replace this 

# commands
leftcmd = """
osascript -e 'tell application "System Events" to key code 124' 
"""

rightcmd = """
osascript -e 'tell application "System Events" to key code 123' 
"""

while 1:
	data = watch.read(7)
	button = int(ord(data[6]))

	if(button == 18):
		if(verbose): print "Right pressed."
		os.system(rightcmd)
		watch.debounce()
		sleep(0.3) # sleep for 300 ms. So that the slide doesn't move very fast
	elif(button == 50):
		if verbose: print "Left pressed."
		os.system(leftcmd)
		watch.debounce()
		sleep(0.3) # sleep for 300 ms. So that the slide doesn't move very fast

#!/usr/bin/env python
import os, eZ430

verbose = 1
watch = eZ430.watch("/dev/tty.usbmodem001") #replace this 

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
	elif(button == 50):
		if verbose: print "Left pressed."
		os.system(leftcmd)
		watch.debounce()

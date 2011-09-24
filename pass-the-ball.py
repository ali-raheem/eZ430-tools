#!/usr/bin/env python
import "eZ430-tools/eZ430"
import time
#Wireless link init
watch = eZ430.watch("/dev/tty.usbmodem001")

def neutral():
	print "Neutral"

def left():
	print "Left"

def right():
	print "Right"

current = 1

#Variables
#Gestures
while 1:
	time.sleep(1)
	data = watch.read()
   	acc={'x':ord(data[0]), 'y':ord(data[1]), 'z':ord(data[2])}
   	
	if acc['x']+acc['y']+acc['z']!=0:
#    		print "x: %s\ty:%s\tz:%s\tpd:%s"%(acc['x'],acc['y'],acc['z'],pd)
		x=acc['x']
		y=acc['y']
		z=acc['z']
		
		#left
		if (y > 220 and y < 235):
			print "l"
			if (current != 0):
				current = 0
				left()

		#neutral
		if (y > 210 and y < 215):
			print "n"
			if (current != 1):
				current = 1
				neutral()

		#right
		if (y > 0 and y < 20):
			print "r"
			if (current != 2):
				current = 2
				right()
		

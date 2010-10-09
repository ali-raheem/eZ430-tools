#!/usr/bin/python
import os
import eZ430

watch = eZ430.sensors()
print "Opening eZ430 on",watch.dev
if(os.system("xdotool --version")!=0):
	print "You need xdotool."
	os.exit(1)
while 1:
	data = watch.read(7)
	button = int(ord(data[6]))
	if(button == 18):
		print "Right pressed."
		os.system("xdotool click 3")
		watch.debounce()
	elif(button == 50):
		print "Left pressed."
		os.system("xdotool click 1")
		watch.debounce()
	elif(button == 34):
		print "Home pressed."
		os.system("xdotool key Home")
		watch.debounce()

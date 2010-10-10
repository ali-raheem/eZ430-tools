#!/usr/bin/env python
import os, eZ430

verbose = 1
watch = eZ430.watch()
if verbose: print "Opening eZ430 on",watch.dev
if(os.system("xdotool --version")!=0):
	print "You need xdotool."
	os.exit(1)
while 1:
	data = watch.read(7)
	button = int(ord(data[6]))
	if(button == 18):
		if(verbose): print "Right pressed."
		os.system("xdotool click 3")
		watch.debounce()
	elif(button == 50):
		if verbose: print "Left pressed."
		os.system("xdotool click 1")
		watch.debounce()
	elif(button == 34):
		if verbose: print "Home pressed."
		os.system("xdotool key Home")
		watch.debounce()

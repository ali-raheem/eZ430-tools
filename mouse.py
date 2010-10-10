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
	y=ord(data[0])
	x=ord(data[1])
	if(x*y != 0):
		x-=128
		y-=128
		x/=50
		y/=50
		os.system('xdotool mousemove_relative -- %s %s'%(x,y))

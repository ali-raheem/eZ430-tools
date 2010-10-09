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
	print "X",ord(data[0]),"Y",ord(data[1]),"Z",ord(data[2])
	y=ord(data[1])
	x=ord(data[2])
	if(x*y != 0):
		for i in data:
			print ord(i)
		x-=128
		y-=128
		y=-y
		x/=50
		y/=50
		os.system('xdotool mousemove_relative -- %s %s'%(x,y))

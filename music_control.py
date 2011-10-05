#!/usr/bin/env python
import eZ430, dbus, time, math
#Rhythmbox dbus
session_bus = dbus.SessionBus()
proxy_obj = session_bus.get_object('org.gnome.Rhythmbox', '/org/gnome/Rhythmbox/Player')
player = dbus.Interface(proxy_obj, 'org.gnome.Rhythmbox.Player')
#Wireless link init
watch = eZ430.watch()

#Variables
#link=0
#pd=0
r=0
l=0
down=0
up=0
playing=0
paused=0

downmillies=int(round(time.time()*1000))
upmillies=int(round(time.time()*1000))

x=0
y=0
z=0

#Gestures
def raised():
	print "Gesture detected!"
	print "Name:\tHeld up"
	print "Bind:\tToggle Play/Pause\n"
	playing!=playing
	player.playPause(playing)
def pronate():
	print "Gesture detected!"
	print "Name:\tPronate"
	print "Bind:\tVolume +1%\n"
	player.setVolumeRelative(0.01)
def supanate():
	print "Gesture detected!"
	print "Name:\tSupanate"
	print "Bind:\tVolume -1%\n"
	player.setVolumeRelative(-0.01)
def swing_down():
	print "Gesture detected!"
	print "Name:\tSwing down"
	print "Bind:\tNext track\n"
	player.next()
#def clear():
#	down=0
#	l=0
#	r=0
while 1:
	data = watch.read()
   	acc={'x':ord(data[0]), 'y':ord(data[1]), 'z':ord(data[2])}
	if acc['x']+acc['y']+acc['z']!=0:
		x=(acc['x'] + x) /2
		y=(acc['y'] + y) /2
		z=(acc['z'] + z) /2
		print "x: %s\ty:%s\tz:%s"%(acc['x'],acc['y'],acc['z'])
	if (y>25) & (y<100) & (z>35):
		down+=1
	if (y<220) & (y>190) & (z>240) & (z<250):
		up+=1
	# volume, but only if hand not holding the head ;)
	if (y>230) or (y<30):
		if (x>20) & (x<=35):
			r+=1;
		elif (x>35) & (x<55):
			r+=8 #strong tilt
		elif (x<225) & (x>=205):
			l+=1
		elif (x<205) & (x>190):
			l+=8 #strong tilt
		else:
			r=0
			l=0
	if (r>20):
		pronate()
		r=0
	if (l>20):
		supanate()
		l=0
	#down gesture unpaus OR next title
	if (down>5) & (downmillies-int(round(time.time()*1000))<-2000):
		downmillies=int(round(time.time()*1000))
		down=0
		up=0
		if (paused==1):
				paused=0
				raised()
		else:
			swing_down()
	#raise hand to pause, down gesture to unpause
	if (up>5) & (paused==0) & (upmillies-int(round(time.time()*1000))<-2000):
		paused=1
		upmillies=int(round(time.time()*1000))
		up=0
		down=0
		raised()

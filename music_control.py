#!/usr/bin/env python
import serial
import array
import dbus
#Rhythmbox dbus
session_bus = dbus.SessionBus()
proxy_obj = session_bus.get_object('org.gnome.Rhythmbox', '/org/gnome/Rhythmbox/Player')
player = dbus.Interface(proxy_obj, 'org.gnome.Rhythmbox.Player')
#Wireless link init
usb = serial.Serial('/dev/ttyACM1',115200,timeout=1)
usb.write(array.array('B', [0xFF, 0x07, 0x03]).tostring())

#Variables
#link=0
pd=0
r=0
s=0
p=0
playing=0
#val=[0,0,0,0]

def getData():
    usb.write(array.array('B', [0xFF, 0x08, 0x07, 0x00, 0x00, 0x00, 0x00]).tostring())

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
	print "Bind:\tVolume +20%\n"
	player.setVolumeRelative(0.2)
def supanate():
	print "Gesture detected!"
	print "Name:\tSupanate"
	print "Bind:\tVolume -20%\n"
	player.setVolumeRelative(-0.2)
def swing_down():
	print "Gesture detected!"
	print "Name:\tSwing down"
	print "Bind:\tNext track\n"
	player.next()
def clear():
	pd=0
	s=0
	p=0
	r=0
while 1:
	getData()
	data = usb.read(7)
   	acc={'x':ord(data[0]), 'y':ord(data[1]), 'z':ord(data[2])}
	if acc['x']+acc['y']+acc['z']!=0:
#		print "x: %s\ty:%s\tz:%s\tpd:%s"%(acc['x'],acc['y'],acc['z'],pd)
		x=acc['x']
		y=acc['y']
		z=acc['z']
	if (y>128) & (x<128):
		pd+=1
		r+=1
	else:
		pd-=1
	if (y<128):
		r=0
	if pd>10:
		pd=10
	if pd<0:
		pd=0
	if p<0:
		p=0
	if s<0:
		s=0
	if (y<128) & (pd>7):
		pd=0
		swing_down()
	if (r>500):
		r=0
		raised()
	if (x>128)&(y>128)&(z>128):
		p+=1
		s=0
	else:
		p=0
		s+=1
	if p>500:
		p=0
		pronate()
	if s>500:
		s=0
#		supanate()
usb.close()

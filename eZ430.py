#!/usr/bin/python
import serial

class sensors():
        def __init__(self, dev="/dev/ttyACM0",deb=50):
                self.dev=dev
                self.conn = serial.Serial(self.dev, 115200,timeout=1)
                self.write("\xFF\x07\x03")
                self.deb=deb
        def write(self,msg):
                self.conn.write(msg)
        def read(self,len=7):
                self.conn.write("\xFF\x08\x07\x00\x00\x00\x00")
                return self.conn.read(len)
        def debounce(self):
                i=self.deb
                while i:
                        self.read(7)
                        i-=1

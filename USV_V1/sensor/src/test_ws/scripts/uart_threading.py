#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import binascii
from datetime import datetime
import struct
import csv
from time import sleep
import threading
import signal
import sys

serialPort0 = '/dev/ttyPS1'  
baudRate0 = 9600  
is_exit=False
data_bytes=bytearray(100)

serialPort5 = '/dev/ttyS4'  
baudRate5 = 9600  

def hcu_to_computer_function(ser1,ser2):
    while True:
        count = ser2.read(1)
        ser1.write(count)

def uart0_to_uart5():
    ser1 = serial.Serial(serialPort0, baudRate0)    #open uast5
    ser2 = serial.Serial(serialPort5, baudRate5)    #open uast5
    t1 = threading.Thread(target=hcu_to_computer_function,args=(ser1,ser2))
    t1.setDaemon(True)
    t1.start()
    print('t1 threading ok')

    while True:
        data = ser1.read(1)
        #data = struct.unpack('H', data)
        print(hex(ord(data)))
        ser2.write(data)
     

if __name__ == '__main__':
    uart0_to_uart5()

           



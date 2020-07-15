# -*-coding: utf-8 -*-
import pi
import time

while True:
    for i in range(0,6):
	print(pi.pwm_capture(i))
    time.sleep(2)

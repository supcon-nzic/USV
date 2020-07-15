# -*-coding: utf-8 -*-
import do
import time

while True:
    for i in range(0,4):
	do.do_on(i)
    time.sleep(2)
    for i in range(0,4):
	do.do_off(i)
    time.sleep(2) 

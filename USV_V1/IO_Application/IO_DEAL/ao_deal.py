# -*-coding: utf-8 -*-
import ao
import time

while True:
    for i in range(0,10000,1000):
	ao.ao_output(i)
        time.sleep(10)

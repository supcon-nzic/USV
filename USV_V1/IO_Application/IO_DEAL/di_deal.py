# -*-coding: utf-8 -*-
import di
import time

while True:
    for i in range(0,4):
	print(di.di_read(i))
    time.sleep(2)

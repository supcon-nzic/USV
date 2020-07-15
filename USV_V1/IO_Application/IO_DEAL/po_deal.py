# -*-coding: utf-8 -*-
import po
import time

for i in range(0,6):
    po.pwm_period_config(i,20000000)
    po.pwm_enable(i)
while True:
    for i in range(0,20000000,1000000):
	for j in range(0,6):
            po.pwm_duty_cycle_config(j,i)
        time.sleep(10)

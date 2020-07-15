# -*- coding: utf-8 -*- 
import sys
import string
import time

pwm_func_PATH ="/root/USV_V1/sensor/src/test_ws/scripts"
if pwm_func_PATH not in sys.path:
	sys.path.append(pwm_func_PATH)

import sensor_dep.pwm_func as pwmf

pwmf.pwm_period_config(1,20000000)
pwmf.pwm_period_config(2,20000000)
pwmf.pwm_period_config(0,20000000)
pwmf.pwm_duty_cycle_config(1,1500000)
pwmf.pwm_duty_cycle_config(0,1500000)
pwmf.pwm_duty_cycle_config(2,1500000)
pwmf.pwm_enable(1)
pwmf.pwm_enable(0)
pwmf.pwm_enable(2)

if __name__ == '__main__':
	judge_mid = 1500000
	while True:
		cap_period, cap_pwm = pwmf.pwm_capture(3)
		#print(cap_period, cap_pwm)  
		if(cap_pwm>9000000):
			continue
		if(cap_period<15000000):
			continue        
	
		judge_flag = (cap_pwm>judge_mid)
		c,d = pwmf.pwm_capture(0)

		if(c > 15000000):
			pwmf.pwm_duty_cycle_config(2, d)
			print('1111', d)
			h = abs(d - 1500000)
			if d > 1500000:
				d = 1500000-h
        	else:
				d = 1500000+h
		pwmf.pwm_duty_cycle_config(0, d)
		print("sail_PWM")
		#print(d)
                time.sleep(0.1)
		
		if not judge_flag:
			a,b = pwmf.pwm_capture(1)
			#c,d = pwmf.pwm_capture(0)
			if(a > 15000000):
				if((b%10000)>9000):
					b=int(b/10000+1)*10000
				else:
					b=int(b/10000+1)*10000
				pwmf.pwm_duty_cycle_config(1,b)
                time.sleep(0.03)

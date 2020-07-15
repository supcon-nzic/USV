# -*- coding: utf-8 -*- 
import string

def pwm_export(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/export'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_export = open(pwm_dir,'w')
	file_export.write('0')
	file_export.close

def pwm_unexport(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/unexport'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_unexport = open(pwm_dir,'w')
	file_unexport.write('0')
	file_unexport.close

def pwm_period_config(pwm_num, period):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/period'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_period = open(pwm_dir,'w')
	pwm_period = str(period)
	file_period.write(pwm_period)
	file_period.close()

def pwm_duty_cycle_config(pwm_num, duty_cycle):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/duty_cycle'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_duty = open(pwm_dir,'w')
	pwm_duty_cycle = str(duty_cycle)
	file_duty.write(pwm_duty_cycle)
	file_duty.close()

def pwm_enable(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/enable'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_enable = open(pwm_dir,'w')
	pwm_enable = str("1")
	file_enable.write(pwm_enable)
	file_enable.close()

def pwm_capture(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/capture'
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	file_capture = open(pwm_dir)
	pwm_capture = file_capture.read()
	period = pwm_capture.split(' ')[0]
	duty_cycle = pwm_capture.split(' ')[1]
	pwm_capture_period = int(period)
	pwm_capture_duty_cycle = int(duty_cycle)
	file_capture.close()
	
	return pwm_capture_period, pwm_capture_duty_cycle
#	return pwm_capture_duty_cycle



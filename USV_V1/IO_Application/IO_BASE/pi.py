# -*-coding: utf-8 -*-
import string
#函数功能：获取指定PI通道的输入周期与高电平时间
#输入参数：对应PI通道：0-5
def pwm_capture(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/capture'
	#对应PI通道信息处理的操作文件路径
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	#以可读方式打开操作文件
	file_capture = open(pwm_dir)
	#读取操作文件中的数据，即为输入信号周期以及高电平时间
	pwm_capture = file_capture.read()
	#周期信号数据与高电平时间数据分离（通过两个数据之间的' '）
	period = pwm_capture.split(' ')[0]
	duty_cycle = pwm_capture.split(' ')[1]
	file_capture.close()
	#返回对应PI通道的输入信号周期与高电平时间
	return int(period), int(duty_cycle)



# -*-coding: utf-8 -*-
import string
#函数功能：配置指定PO通道的输出周期
#输入参数：PO通道：0-5;PO输出周期
def pwm_period_config(pwm_num, period):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/period'
	#对应PO通道周期配置的操作文件路径
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	#以可写方式打开操作文件
	file_period = open(pwm_dir,'w')
	pwm_period = str(period)
	#将PO周期值写入到操作文件中
	file_period.write(pwm_period)
	file_period.close()

#函数功能：配置指定PO通道的高电平时间
#输入参数：PO通道：0-5;PO输出高电平时间
def pwm_duty_cycle_config(pwm_num, duty_cycle):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/duty_cycle'
	#对应PO通道高电平时间配置的操作文件路径
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	#以可写方式打开操作文件
	file_duty = open(pwm_dir,'w')
	pwm_duty_cycle = str(duty_cycle)
	#将PO高电平时间写入到操作文件中
	file_duty.write(pwm_duty_cycle)
	file_duty.close()

#函数功能：使能指定PO通道输出
#输入参数：PO通道：0-5
def pwm_enable(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/enable'
	#对应PO通道使能信号配置的操作文件路径
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	#以可写方式打开操作文件
	file_enable = open(pwm_dir,'w')
	#向操作文件内写入使能信号'1'
	file_enable.write('1')
	file_enable.close()

#函数功能：关闭指定PO通道输出
#输入参数：PO通道：0-5
def pwm_disable(pwm_num):
	pwm_num = str(pwm_num)
	pwm = '/sys/class/pwm/pwmchip/pwm0/enable'
	#对应PO通道输出关闭配置的操作文件路径
	pwm_dir = pwm[:22] + pwm_num + pwm[22:]
	#以可写方式打开操作文件
	file_enable = open(pwm_dir,'w')
	#向操作文件内写入关闭输出信号'0'
	file_enable.write('0')
	file_enable.close()


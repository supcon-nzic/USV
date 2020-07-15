# -*-coding: utf-8 -*-
import string
#函数功能：读取ADC采样值
#输入参数：对应ADC采样通道：1,2
#输出参数：ADC采样值：0-4096
def ai_read(channel):
	cnt = str(channel + 7)
	channel = str(channel)
	ai = '/sys/bus/iio/devices/iio:device1/in_voltage_vaux_raw'
	#对应ADC采样通道的操作文件路径
	ai_dir = ai[:43] + cnt + ai[43:48] + channel + ai[48:]
	#以可读方式打开操作文件
	file_ai = open(ai_dir)
	#读取文件中的值，即为ADC采样值
	ai_value = file_ai.read()
	#关闭操作文件
	file_ai.close()
	#返回ADC采样值
	return int(ai_value)

#函数功能：获取电源电压值
#输出参数：电源电压值
def voltage_read():
	#电源电压采样通道的操作文件路径
	voltage_dir = '/sys/bus/iio/devices/iio:device1/in_voltage10_vaux8_raw'
	#以可读方式打开操作文件
	file_voltage = open(voltage_dir)
	#读取文件中的值，即为电源电压采样值
	voltage_value = file_voltage.read()
	file_voltage.close()
	#计算电源电压值
	voltage_value = float(voltage_value) * 34 / 4096
	#返回电源电压值
	return round(voltage_value,2)






	

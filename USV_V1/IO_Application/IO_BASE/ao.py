# -*-coding: utf-8 -*-
import string
#函数功能：输出电压
#输入参数：需要输出的电压值（mV）
#输出参数：无
def ao_output(value):
	#ao操作文件路径
	ao_dir = '/sys/bus/iio/devices/iio:device2/out_voltage_raw'
	#以可写方式打开操作文件
	file_ao = open(ao_dir,'w')
	ao_value = str(value)
	#读取文件中的值，即为ADC采样值
	file_ao.write(ao_value)
	#关闭操作文件
	file_ao.close()





	

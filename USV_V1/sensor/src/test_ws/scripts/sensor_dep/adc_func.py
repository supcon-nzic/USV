import string

def adc_read(channel):
	cnt = str(channel+7)
	channel = str(channel)
	adc = '/sys/bus/iio/devices/iio:device1/in_voltage_vaux_raw'
	adc_dir = adc[:43]+cnt+adc[43:48]+channel + adc[48:]
	# adc_dir = '/home/wangxuexi/adc'
	file_adc = open(adc_dir)
	adc_value = file_adc.read()
	adc_value = int(adc_value)
	return adc_value

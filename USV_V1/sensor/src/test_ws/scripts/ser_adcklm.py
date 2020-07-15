#!/usr/bin/env python
# -*-coding: utf-8 -*-
#license removed for brevity

import rospy
from std_msgs.msg import Float64
import time
import sqlite3
#import matplotlib.pyplot as plt
#import numba
import numpy as np
import copy
from sensor_dep.adc_func import adc_read


class Kl_fit:
    def __init__(self):
#     这些不要动
        self.X = np.array([[0],
                            [0]])
        self.F = np.array([[1,0],
                            [0,1]])
        self.P = np.array([[1,0],
                            [0,1]])

        self.H = np.array([[1,0],
                            [0,1]])

        self.I = np.array([[1,0],
                            [0,1]])
#  这些是参数
        self.Q = np.array([[1,0],
                           [0,1]])

        self.R = np.array([[80,0],
                           [0,80]])
#@表示矩阵相乘
    def run_kl(self,x,y):
        #x_ = self.F@self.X
        x_ = np.dot(self.F, self.X)
        #P_ = self.F@self.P@self.F.T + self.Q  
        P_ = np.dot(np.dot(self.F, self.P), self.F.T)+ self.Q  #3个矩阵连乘能否这么表示
        z = np.array([[x],
                      [y]])
        
        #y = z - self.H@x_
        y = z - np.dot(self.H, x_)

        #S = self.H@P_@self.H.T + self.R
        S = np.dot(np.dot(self.H, P_), self.H.T) + self.R
        #K = P_@self.H.T@np.linalg.inv(S)
        K = np.dot(np.dot(P_, self.H.T), np.linalg.inv(S))

        #self.X = x_ + K@y
        self.X = x_ + np.dot(K, y)
        #self.P = (self.I - K@self.H)@P_
        self.P = np.dot((self.I - np.dot(K, self.H)), P_)

# class fir():
#     def __init__(self,fir_len):
#         self.window_array = np.zeros((fir_len),dtype=float)
#         self.in_count = 0
#         self.fir_len = fir_len
#     def do_fir(self,input_):
#         self.window_array[self.in_count] = input_
#         if self.in_count == self.fir_len-1:
#             self.in_count = 0
#         else:
#             self.in_count +=1 
#         temp_array = copy.copy(self.window_array)
#         temp_array.sort()
#         temp_array = temp_array[1:-1]
#         output = sum(temp_array)//len(temp_array)
#         return output

# class sqlite_wind():
#     def __init__(self):
#         self.con=sqlite3.connect('wind_data232_485.db')
#         print("Opened database successfully")

#     def excu_sql(self,sql):
#         cursor = self.con.cursor().execute(sql)
#         return cursor.fetchall()

#     def read_data(self):
#         sql = 'SELECT TIME,WIND_232,SPEED_485,WIND_485 from WIND'
#         data_speed = self.excu_sql(sql)
#         return data_speed

# def on_press(event):
#         x_u= event.xdata//1
#         timeArray = time.localtime(x_u)
#         otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
#         plt.title(otherStyleTime)
#         event.canvas.draw()



def a360_2_pi(ag):
    out = (float(ag)/360*np.pi*2)
    return out

def pi_2_360(pi):
    out = (pi/(2*np.pi)*360)
    #print('out'+str(out))
    return out


#ikla = Kl_fit()
def klfir_wind(kla,i):
    x = np.cos(a360_2_pi(i))
    y = np.sin(a360_2_pi(i))
    kla.run_kl(x,y)
    x = kla.X[0]
    y = kla.X[1]
    if x>=0:
        if x!=0:
            if y>=0:
                ag = np.arctan(y/x)
            else:
                ag = np.arctan(y/x)+2*np.pi
        else:
            ag = 0
    else:
            ag = np.arctan(y/x)+np.pi

    return pi_2_360(ag)





# db = sqlite_wind()
# data = db.read_data()
# time_list = []
# w_232_list = []
# sp_485_list = []
# w_485_list = []

#w_232_klfit_list = []
# w_232_winfit_list = []



kla = Kl_fit()
#wid = fir(10)
wind  = klfir_wind(kla,10)
#读取风向函数替换i  adc_read(1)
#for i in data:
    #w_232_list.append(i[1])
    #w_232_klfit_list.append(klfir_wind(kla,i[1]))
    #w_232_winfit_list.append(wid.do_fir(i[1]))

class wind_list():
	def wind_direction_apparent_list(self):
		self.wind_direction_apparent = Float64()
		self.wind_direction_apparent_list = []
		self.list1 = []
		self.temp = Float64()
		for i in range(10):
			self.wind_direction_apparent.data=int(float(adc_read(1))/3490*360)     #accept adc data and convert wind data
			if self.wind_direction_apparent.data > 360:
				self.wind_direction_apparent.data = 360
			self.wind_direction_apparent_list.append(self.wind_direction_apparent.data)
		self.wind_direction_apparent_list.sort()
		self.wind_direction_apparent_list = self.wind_direction_apparent_list[1:-1]
		#solve 0-360 jump
		for i in range(len(self.wind_direction_apparent_list)-1):
			t = abs(self.wind_direction_apparent_list[i]-self.wind_direction_apparent_list[i+1])
			self.list1.append(t)
		yy = False
		for i in range(len(self.list1)):
			if self.list1[i] > 100:
				yy = True
				break
			
		if yy == True:
			for i in range(len(self.wind_direction_apparent_list)):
				if self.wind_direction_apparent_list[i] > 180:
					self.wind_direction_apparent_list[i] = self.wind_direction_apparent_list[i]-360
				else:
					self.wind_direction_apparent_list[i] = self.wind_direction_apparent_list[i]
			self.wind_direction_apparent.data = np.mean(self.wind_direction_apparent_list)
			if self.wind_direction_apparent.data < 0:
				self.wind_direction_apparent.data = self.wind_direction_apparent.data +360
		else:
			self.wind_direction_apparent.data = np.mean(self.wind_direction_apparent_list)
		self.wind_direction_apparent.data = int(self.wind_direction_apparent.data)
		return self.wind_direction_apparent.data 
	

def ser_adc():
    rospy.init_node('ser_adc', anonymous = True)
    pub = rospy.Publisher('wind_direction_apparent', Float64, queue_size = 10)
    rate = rospy.Rate(10)
    wind_direction = Float64()
    wind_direction_klm = Float64()
   # kla = Kl_fit()
    while not rospy.is_shutdown():
        A = wind_list()
        wind_direction.data = A.wind_direction_apparent_list()
	print('wind_direction.data'+str(wind_direction.data))
	#with open("yuqizhi.txt","a") as f:
		#f.write(str(wind_direction.data)+'\n')
        wind_direction_klm.data = int(klfir_wind(kla,wind_direction.data))
        print('wind'+str(wind_direction_klm.data))
	#with open('yuqi.txt','a') as f:
		#f.write(str(wind_direction_klm.data)+'\n')
        pub.publish(wind_direction_klm)
        rate.sleep()


if __name__ == '__main__':
    try:
	kla = Kl_fit()
        ser_adc()
    except rospy.ROSInterruptException:
        pass


#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(w_232_list,'-r',label='sour')
#ax.plot(w_232_klfit_list,'-g',label='KL')
#ax.plot(w_232_winfit_list,'-b',label='AVG')
# ax2 = ax.twinx()
# ax2.plot(time_array,sp_485_array,'-b',label='speed')

#ax.legend(loc=2)
# ax2.legend(loc=1)
#fig.canvas.mpl_connect('button_press_event',on_press)
#plt.show()

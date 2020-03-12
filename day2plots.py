# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:44:30 2020

@author: agarw_ftjrwf3
"""
import matplotlib.pyplot as plt
x=[1,2,3,7,8,6]
y=[4,5,6,2,4,9]
z=[9,6,4,8,3,7]
plt.plot(x,y,label='x v/s y',linestyle='--',color='b',marker='x',markerfacecolor='r',linewidth=2)

#plt.plot(x,y,label='x v/s y',linestyle='--',color='b',marker='x',markerfacecolor='r')


plt.plot(x,z,label='x v/s z',color='g',linestyle='-.',linewidth=2,marker='o',markerfacecolor='g')
#plt.legend(['y_waala','z_waala'])

plt.xlim(1,4)
plt.ylim(1,7)

plt.title('info')

plt.grid(True,linewidth=1,color='y')
plt.xlabel('x-axis')
plt.ylabel('y_axis')
plt.show()
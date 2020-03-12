# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:45:02 2020

@author: agarw_ftjrwf3
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('iris.csv')
x=dataset.iloc[:,:4].values
y=dataset.iloc[:,-1].values
#plt.plot(x[:,0],y)
a=x[:,0]
for i in range(0,x.shape[1]):
    X=x[:,i]
    plt.plot(X,y)
    plt.xlabel('xaxis')
    plt.ylabel('yaxis')
    plt.show()
    
    
color=['red','blue','green','yellow']
for i in range(0,x.shape[1]):
    X=x[:,i]
    plt.scatter(X,y,c=color[i])
    plt.show()
    
import seaborn    
dataset.boxplot(by='sepal.length',column=['sepal.width'],grid=False)
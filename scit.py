#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:28:54 2019

@author: kazzastic
"""

import numpy as np
import os
import tarfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Loadinng data of my class
data = pd.read_csv('SCIT dataset.csv',index_col = 0)

# Already mentioned in our dataset, the distrcits are 
# East, West, South, Central, Malir, Korangi
Districts = ('East', 'West', 'South', 'Central', 'Malir', 'Korangi')

y_pos = np.arange(len(Districts))

'''
Starting of multiple bar chart
'''
def multi_chart():
    data = pd.read_csv('SCIT dataset.csv',index_col = 0)
    freq = [[]]
    for i in range(1,7):
        dist = data[data['X1']==i]
        freq[i-1].append(len(dist[(dist['X2'] >= 11) & (dist['X2'] <= 20)]))
        freq[i-1].append(len(dist[(dist['X2'] >= 21) & (dist['X2'] <= 30)]))
        freq[i-1].append(len(dist[(dist['X2'] >= 31) & (dist['X2'] <= 45)]))
        freq[i-1].append(len(dist[dist['X2'] > 45]))
        freq.append([])
    freq.pop(6)
    
    frq = [[freq[j][i] for j in range(len(freq))] for i in range(len(freq[0]))] 
    plt.bar(y_pos-0.3,frq[0],width = 0.2)
    plt.bar(y_pos-0.1,frq[1],width = 0.2)
    plt.bar(y_pos+0.1,frq[2],width = 0.2)
    plt.bar(y_pos+0.3,frq[3],width = 0.2)

'''
Strating of bar chart
'''
def chart():
    #breaking the data for the x-axis values
    frequency = []
    for i in range(1,7):
        dist = data[data['X1']==i]
        frequency.append(len(dist))
    
    plt.bar(y_pos, frequency, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, Districts)
    plt.yticks('Frequency')
    plt.title("Simple Bar Diagram")
    
chart()
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:31:18 2019

@author: kazzastic
"""

import os
import tarfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
.
data = pd.read_csv('SCIT dataset.csv',index_col = 0)
Transportation = ["Van", "Private Transport", "Car", "Bike", "Walk"]
y_pos = np.arange(len(Transportation))

def multi_chart():
    freq = [[]]
    for i in range(1,6):
        dist = data[data['X3']==i]
        freq[i-1].append(len(dist[(dist['X2'] >= 11) & (dist['X2'] <= 20)]))
        freq[i-1].append(len(dist[(dist['X2'] >= 21) & (dist['X2'] <= 30)]))
        freq[i-1].append(len(dist[(dist['X2'] >= 31) & (dist['X2'] <= 45)]))
        freq[i-1].append(len(dist[dist['X2'] > 45]))
        freq.append([])
    freq.pop(5)
    
    frq = [[freq[j][i] for j in range(len(freq))] for i in range(len(freq[0]))] 
    plt.bar(y_pos-0.3,frq[0],width = 0.2)
    plt.bar(y_pos-0.1,frq[1],width = 0.2)
    plt.bar(y_pos+0.1,frq[2],width = 0.2)
    plt.bar(y_pos+0.3,frq[3],width = 0.2)

















Van = data[data['X3'] == 1]
Pvt = data[data['X3'] == 2]
Car = data[data['X3'] == 3]
Bike = data[data['X3'] == 4]
Walk = data[data['X3'] == 5]

Van_east = Van[Van['X1']==1]
Van_east = Van_east.values
Van_east = Van_east[:, [2, 0, 1]]

Van_west = Van[Van['X1']==2]
Van_west = Van_west.values
Van_west = Van_west[:, [2, 0, 1]]

Van_south = Van[Van['X1']==3]
Van_south = Van_south.values
Van_south = Van_south[:, [2, 0, 1]]

Van_central = Van[Van['X1']==4]
Van_central = Van_central .values
Van_central = Van_central [:, [2, 0, 1]]

Van_Malir= Van[Van['X1']==5]
Van_Malir= Van_Malir.values
Van_Malir= Van_Malir[:, [2, 0, 1]]

Van_korangi= Van[Van['X1']==5]
Van_korangi= Van_korangi.values
Van_korangi= Van_korangi[:, [2, 0, 1]]

X = np.arange(1)
plt.bar(X + 0.00, Van_east, color = 'b', width = 0.25)
plt.bar(X + 0.25, Van_west, color = 'g', width = 0.25)
plt.bar(X + 0.50, Van_south, color = 'r', width = 0.25)
plt.bar(X + 0.75, Van_central, color = 'y', width = 0.25)
plt.bar(X + 1.00, Van_korangi, color = 'm', width = 0.25)
plt.bar(X + 1.25, Van_Malir, color = 'c', width = 0.25)

plt.show()
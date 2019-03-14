#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 01:52:58 2019

@author: kazzastic
"""

import numpy as np
import os
import tarfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('SCIT dataset.csv', index_col = 0)

transport = ['Van', 'Public', 'Car', 'Bike', 'Walk']

y_pos = np.arange(len(transport))

freq = [[]]
for i in range(1,6):    
    trans = data[data['X3']==i]
    freq[i-1].append(len(trans[(trans['X2'] >= 1) & (trans['X2'] <= 10)]))
    freq[i-1].append(len(trans[(trans['X2'] >= 11) & (trans['X2'] <= 20)]))
    freq[i-1].append(len(trans[(trans['X2'] >= 21) & (trans['X2'] <= 30)]))
    freq[i-1].append(len(trans[(trans['X2'] >= 31) & (trans['X2'] <= 45)]))
    freq[i-1].append(len(trans[trans['X2'] > 45]))
    freq.append([])
freq.pop(5)


#frq = [[freq[j][i] for j in range(len(freq))] for i in range(len(freq[0]))]

plt.bar(y_pos-0.3,freq[0],width = 0.2)
plt.bar(y_pos-0.1,freq[1],width = 0.2)
plt.bar(y_pos+0.1,freq[2],width = 0.2)
plt.bar(y_pos+0.3,freq[3],width = 0.2)
plt.show()

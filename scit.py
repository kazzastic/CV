#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:54:55 2019

@author: kazzastic
"""
import numpy as np
import os
import tarfile
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = os.path.join("datasets", "housing")


def load_housing_data(data_path = DATA_PATH):
    csv_path = os.path.join(data_path, "SCIT dataset.csv")
    return pd.read_csv(csv_path, index_col = 0)

data = load_housing_data()
#simply use this
data = pd.read_csv('SCIT dataset - Sheet1.csv',index_col = 0)
# Already mentioned in our dataset, the distrcits are 
# East, West, South, Central, Malir, Korangi
Districts = ('East', 'West', 'South', 'Central', 'Malir', 'Korangi')
y_pos = np.arange(len(Districts))

frequency = []
for i in range(1,7):
    dist = data[data['X1']==i]
    frequency.append(len(dist)) 

plt.bar(y_pos, frequency, align = 'center', alpha = 0.5)
plt.xticks(y_pos, Districts)
plt.yticks('Frequency')
plt.title("Simple Bar Diagram")
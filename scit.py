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

'''
simply use this
data = pd.read_csv('SCIT dataset - Sheet1.csv',index_col = 0)
'''
# Already mentioned in our dataset, the distrcits are 
# East, West, South, Central, Malir, Korangi
Districts = ('East', 'West', 'South', 'Central', 'Malir', 'Korangi')
y_pos = np.arange(len(Districts))

'''
breaking the data for the x-axis values
'''
frequency = []
for i in range(1,7):
    dist = data[data['X1']==i]
    frequency.append(len(dist)) 

'''
Selecting data from East Column and dividing them according 
to thier time/duration
'''
East = data[data['X1'] == 1]
East_ten = East[data['X2'] <= 10]
East_eleven = East[(data['X2'] >= 11) & (data['X2'] <= 20)]
East_twenty = East[(data['X2'] >= 21) & (data['X2'] <= 30)]
East_thirty = East[(data['X2'] >= 31) & (data['X2'] <= 45)]
East_fourty = East[data['X2'] > 45]

'''
Selecting the data from West column and dividing them 
according to thier time/duration
'''
West = data[data['X1'] == 2]
West_ten = West[data['X2'] <= 10]
West_eleven = West[(data['X2'] >= 11) & (data['X2'] <= 20)]
West_twenty = West[(data['X2'] >= 21) & (data['X2'] <= 30)]
West_thirty = West[(data['X2'] >= 31) & (data['X2'] <= 45)]
West_fourty = West[data['X2'] > 45]

'''
Selecting the data from the South and dividing it w.r.t duration
'''
South = data[data['X1'] == 3]
South_ten = South[data['X2'] <= 10]
South_eleven = South[(data['X2'] >= 11) & (data['X2'] <= 20)]
South_twenty = South[(data['X2'] >= 21) & (data['X2'] <= 30)]
South_thirty = South[(data['X2'] >= 31) & (data['X2'] <= 45)]
South_fourty = South[data['X2'] > 45]

'''
Selecting the data from the Central and dividing it w.r.t to time durations
'''
Central = data[data['X1'] == 4]
Central_ten = Central[data['X2'] <= 10]
Central_eleven = Central[(data['X2'] >= 11) & (data['X2'] <= 20)]
Central_twenty = Central[(data['X2'] >= 21) & (data['X2'] <= 30)]
Central_thirty = Central[(data['X2'] >= 31) & (data['X2'] <= 45)]
Central_fourty = Central[data['X2'] > 45]

'''
Selecting the data from the Malir and dividing it w.r.t to time durations
'''
Malir = data[data['X1'] == 5]
Malir_ten = Malir[data['X2'] <= 10]
Malir_eleven = Malir[(data['X2'] >= 11) & (data['X2'] <= 20)]
Malir_twenty = Malir[(data['X2'] >= 21) & (data['X2'] <= 30)]
Malir_thirty = Malir[(data['X2'] >= 31) & (data['X2'] <= 45)]
Malir_fourty = Malir[data['X2'] > 45]

'''
Selecting the data from the Korangi and dividing it w.r.t to time durations
'''
Korangi = data[data['X1'] == 5]
Korangi_ten = Korangi[data['X2'] <= 10]
Korangi_eleven = Korangi[(data['X2'] >= 11) & (data['X2'] <= 20)]
Korangi_twenty = Korangi[(data['X2'] >= 21) & (data['X2'] <= 30)]
Korangi_thirty = Korangi[(data['X2'] >= 31) & (data['X2'] <= 45)]
Korangi_fourty = Korangi[data['X2'] > 45]

'''
plotting the graph code

plt.bar(y_pos, frequency, align = 'center', alpha = 0.5)
plt.xticks(y_pos, Districts)
plt.ylabel('Frequency')
plt.title("Simple Bar Diagram")
plt.show()
'''
'''
plotting the second graph
'''
#data of plot
n_groups = 6

#create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, East_ten, bar_width, aplha = opacity, color = 'b', label = "some")

plt.xlabel('Districts')
plt.ylabel("Duration")
plt.title("I hope this works")
plt.xticks(y_pos, Districts)
plt.legend()
plt.tight_layout()
plt.show()
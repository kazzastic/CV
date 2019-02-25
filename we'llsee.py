__author__ = "kazim"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics 

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
data.head()

feature_cols = ['TV' , 'radio' , 'newspaper' ]
#x = data.reset_index(drop=True)
x = data[feature_cols]

y = data['sales']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

linreg = LinearRegression()
linreg.fit(x_train, y_train)

print(linreg.intercept_)
print(linreg.coef_)

list(zip(feature_cols, linreg.coef_))

y_pred = linreg.predict(x_test)
true = [100, 50, 30, 20]
pred = [90, 50, 50, 30]

print(metrics.mean_absolute_error(true, pred))
print(metrics.mean_squared_error(true, pred))
print(np.sqrt(metrics.mean_squared_error(true, pred)))
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# -*- coding: utf-8 -*-
"""Regression-Classroom.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KmIvYfnIVXszeuCkdzmrKeMugH3bBe1c
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('Real_Estate.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

dataset.describe()

dataset.drop(['No', 'X1_Transaction_Date'], axis=1, inplace=True)

dataset.head

dataset.info()

plt.figure(figsize=(6,12))
sns.pairplot(dataset)
plt.show()

corr=dataset.corr()
plt.figure(figsize=(12,6))
sns.heatmap(corr,annot=True)

dataset['X5_Latitude']=dataset['X5_Latitude'] * dataset['X6_Longitude']
dataset.drop(['X6_Longitude'],axis=1,inplace=True)

dataset.describe()

sns.boxplot(dataset['X2_House_Age'])

sns.boxplot(dataset['X3_Distance_of_Nearest_MRT_Station'])

sns.boxplot(dataset['X4_Number_of_Convenience_Stores'])

sns.boxplot(dataset['X5_Latitude'])

upper_limit = dataset['X3_Distance_of_Nearest_MRT_Station'].mean() + 3*dataset['X3_Distance_of_Nearest_MRT_Station'].std()
lower_limit = dataset['X3_Distance_of_Nearest_MRT_Station'].mean() - 3*dataset['X3_Distance_of_Nearest_MRT_Station'].std()
print("Upper Limit:", upper_limit)
print("Lower Limit:", lower_limit)

dataset.loc[(dataset['X3_Distance_of_Nearest_MRT_Station'] > upper_limit)|(dataset['X3_Distance_of_Nearest_MRT_Station'] < lower_limit)]

new_dataset = dataset.loc[(dataset['X3_Distance_of_Nearest_MRT_Station'] > upper_limit)|(dataset['X3_Distance_of_Nearest_MRT_Station'] < lower_limit)]
print("Before Removal:", len(dataset))
print("After Removal:", len(new_dataset))

sns.boxplot(new_dataset['X3_Distance_of_Nearest_MRT_Station'])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

from sklearn.metrics import r2_score
r2_score(y_test,y_pred,)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

y_pred_poly = regressor.predict(x_test)

from sklearn.metrics import r2_score
r2_score(y_test,y_pred_poly,)


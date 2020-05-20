import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Salary_Data.csv')
x = data.loc[:, 'YearsExperience'].values
y = data.loc[:,'Salary'].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 1/3 , random_state=0)
regresor = LinearRegression()
regresor.fit(x_train.reshape(-1,1),y_train.reshape(-1,1),sample_weight=None)
x_test = x_test.reshape(-1,1)
y_pred = regresor.predict(x_test.reshape(-1,1))

pd.to_pickle(regresor,'regresor.pickle')

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:32:59 2022

@author: SPTINT-04
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/SPTINT-04/Desktop/TRAIN/train.csv')
fig1=plt.figure()
first_axis=fig1.add_subplot()
second_axis=first_axis.twinx()
survived_df=data.groupby(['Embarked']).mean()[["Survived"]]
fare_df=data.groupby(['Embarked']).mean()[["Fare"]]
fare_df.plot(kind='bar', grid=True,ax=first_axis,width=0.2,position=0)
survived_df.plot(kind='bar',color='yellow',ax=second_axis, grid=True,width=0.2,position=1)
first_axis.set_ylabel('Average Fare Amount')
second_axis.set_ylabel('Survival %')
first_axis.legend(["Average Fare"],loc="upper right")
second_axis.legend(["Survival %"], loc="upper left")
plt.title('Survival Rate and Fare paid for each embarked port')

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:09:45 2019

@author: jaehooncha

@email: chajaehoon79@gmail.com

pandas
"""
import pandas as pd
import numpy as np

arr = np.array([['A',50,1],['B',60,2],['C',90,7]])
df = pd.DataFrame(arr, columns = ['name', 'grade', 'hours'])

### save dataframe ###
df.to_csv('practice.csv')

### call dataframe ###
df = pd.read_csv('practice.csv', header = 0, index_col=[0])

### columns ###
df.columns 
# print Index(['name', 'grade', 'hours'], dtype='object')

### read first n columns ###
df.head(2)
# read first two columns, default is 5

### read last n columns ###
df.tail(2)
# read last 2 columns, default is 5

### read specific column ###
df['name']
# print name column

### set index ###
df.index = [2,3,4]
# index becomes [2,3,4]
df.set_index('name', inplace = True)
# set name column to index
df.reset_index(level=0, inplace = True)
# set index to column
df.reset_index(drop = True, inplace = True)
# index begins from 0




import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3

#Grouping: a process involving
#Splitting the data into groups based on some criteria
#Applying a function to each group independently
#Combining the result into a data structure

print('-'*20)
df = pd.DataFrame(
    {'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
     'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
     'C' : np.random.randn(8),
     'D' : np.random.randn(8)})#91
print(df)#92
print('-'*20)
#Grouping and then applying the sum() function to the resulting groups.
print(df.groupby('A').sum())#93
print('-'*20)
#Grouping by multiple columns forms a hierarchical index,
#and again we can apply the sum function.
print(df.groupby(['A','B']).sum())#94
print('-'*20)
print(df.groupby(['B','A']).sum())#94
print('-'*20)

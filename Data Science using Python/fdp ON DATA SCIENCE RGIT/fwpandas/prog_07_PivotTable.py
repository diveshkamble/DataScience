import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
#105
df = pd.DataFrame(
    {'A' : ['one', 'one', 'two', 'three'] * 3,
     'B' : ['A', 'B', 'C'] * 4,
     'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
     'D' : np.random.randn(12),
     'E' : np.random.randn(12)})
print('-'*20)
print("df :\n",df)#106
print('-'*20)
#We can produce pivot tables from this data very easily:
print( pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))#107

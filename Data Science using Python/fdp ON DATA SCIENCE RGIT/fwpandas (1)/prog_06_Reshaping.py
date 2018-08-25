import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
#Stack
#95
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz','foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']]))
print('-'*20)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])#96
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])#97
df2 = df[:4]#98
print("df2 :\n",df2)#99
print('-'*20)
#The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()#100
print("stacked :\n",stacked)#101
print('-'*20)
#With a “stacked” DataFrame or Series (having a MultiIndex as the index),
#the inverse operation of stack() is unstack(),
#which by default unstacks the last level:
print("stacked.unstack():\n",stacked.unstack())#102
print('-'*20)
print("stacked.unstack(1):\n",stacked.unstack(1))#103
print('-'*20)
print("stacked.unstack(0):\n",stacked.unstack(0))#104
print('-'*20)

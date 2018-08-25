import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                      columns=['A', 'B', 'C', 'D'])
    

df = df.cumsum()
#Writing to a csv file.
df.to_csv('foo.csv')  #141
#Reading from a csv file.
print(pd.read_csv('foo.csv'))#142
print('-'*20)
#Reading and writing to HDFStores.
#Writing to a HDF5 Store.
df.to_hdf('foo.h5','df')#143
#Reading from a HDF5 Store.
print(pd.read_hdf('foo.h5','df'))#144
print('-'*20)
#Reading and writing to MS Excel.
#Writing to an excel file.
df.to_excel('foo.xlsx', sheet_name='Sheet1')#145
#Reading from an excel file.
#146
print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))

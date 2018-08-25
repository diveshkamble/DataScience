import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000',periods=1000))

ts = ts.cumsum()#136
#On a DataFrame, the plot() method is a convenience to plot all of
#the columns with labels:
#138
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                      columns=['A', 'B', 'C', 'D'])
df = df.cumsum()#139

plt.figure(); df.plot(); plt.legend(loc='best')#140
plt.show()

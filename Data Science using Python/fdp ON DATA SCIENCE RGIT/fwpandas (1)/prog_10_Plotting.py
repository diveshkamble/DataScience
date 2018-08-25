import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3

#135
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000',periods=1000))

ts = ts.cumsum()#136
print(ts)
ts.plot()#137
plt.show()

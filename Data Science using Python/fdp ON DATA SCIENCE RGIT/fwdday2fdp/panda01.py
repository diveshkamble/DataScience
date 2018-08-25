import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3

s=pd.Series(np.random.randint(0,7,size=10))#68
print(s)#69
print('-'*20)
print(s.value_counts())#70
x=s.value_counts()
plt.plot(x)
plt.show()

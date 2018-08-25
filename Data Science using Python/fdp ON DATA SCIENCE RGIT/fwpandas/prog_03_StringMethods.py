import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
lst=['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat']
print(lst)
print('-'*20)
#s=pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
s=pd.Series(lst)#71
print(s.str.lower())#72






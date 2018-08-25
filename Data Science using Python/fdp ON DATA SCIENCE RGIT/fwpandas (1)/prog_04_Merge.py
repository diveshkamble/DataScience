import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3

#Concatenating pandas objects together with concat()
df=pd.DataFrame(np.random.randn(10,4))#73
print("df:\n",df)#74
print('-'*20)
#break it into pieces
pieces=[df[:3],df[3:7],df[7:]]#75
print("pieces:")
print(pieces[0])
print('-'*20)
print(pieces[1])
print('-'*20)
print(pieces[2])
print('-'*20)
print("pd.concat:\n",pd.concat(pieces)) #76
print('-'*20)
#Join SQL style merges
left=pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})#77
#print("left:\n",left)
right=pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})#78
print("left:\n",left)#79
print('-'*20)
print("right:\n",right)#80
print('-'*20)
print("Merging:\n",pd.merge(left,right,on='key'))#81
print('-'*20)
#Another example of merging
left=pd.DataFrame({'key':['foo','bar'],'lval':[1,2]})#82
right=pd.DataFrame({'key':['foo','bar'],'rval':[4,5]})#83
print("left:\n",left)#84
print('-'*20)
print("right:\n",right)#85
print('-'*20)
print("Merging:\n",pd.merge(left,right,on='key'))#86
print('-'*20)
#Append: Append rows to a dataframe
df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])#87
print("df:\n",df)#88
print('-'*20)
s=df.iloc[3] #89
print("s: \n",s)
print("df.append:\n",df.append(s,ignore_index=True))#90










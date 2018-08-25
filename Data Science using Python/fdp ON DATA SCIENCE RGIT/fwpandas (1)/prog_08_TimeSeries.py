import pandas as pd#1
import numpy as np#2
import matplotlib.pyplot as plt#3
"""
pandas has simple, powerful, and efficient functionality for performing
resampling operations during frequency conversion (e.g., converting secondly
data into 5-minutely data).
This is extremely common in, but not limited to, financial applications.
"""


rng = pd.date_range('1/1/2012', periods=100, freq='S')#108
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)#109
print("ts:\n",ts)
print('#'*10)
print(ts.resample('5Min').sum())#110
print('-'*20)
#Time zone representation:
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')#111
ts = pd.Series(np.random.randn(len(rng)), rng)#112
print('*'*10)
print("ts :\n", ts)#113
print('-'*20)
ts_utc = ts.tz_localize('UTC')#114
print('-'*20)
print("UTC")
print("ts_utc :\n",ts_utc)#115
#Converting to another time zone:
print('-'*20)
print("US/Eastern")
print(ts_utc.tz_convert('US/Eastern'))#116
print('-'*20)
#Converting between time span representations:
rng = pd.date_range('1/1/2012', periods=5, freq='M')#117
ts = pd.Series(np.random.randn(len(rng)), index=rng)#118
print("ts :\n",ts)#119
print('-'*20)
ps = ts.to_period()#120
print("ps :\n",ps   )#121
print('-'*20)
print(ps.to_timestamp())#122
"""
Converting between period and timestamp enables some convenient
arithmetic functions to be used.
In the following example, we convert a quarterly frequency
with year ending in November to 9am of the end of the month
following the quarter end:
"""
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')#123
ts = pd.Series(np.random.randn(len(prng)), prng)#124
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9  #125
print("ts.head():\n", ts.head())#126
print('-'*20)



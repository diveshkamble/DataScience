#Numpy operation
# reshape slicing
import numpy as np
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
a=a.reshape(4,2)
print(a)

# slicing: extract particular set of elements from array
a=np.array([(1,2,3,4),(13,14,15,16)])
print(a[0,2])#3 in zero row 2 column
print(a[1,2])#15 in first row 2 column
print(a[0:,3])#4, 16
a=np.array([(1,2,3,4),(13,14,15,16),(21,22,23,24)])
print(a)
print(a[0:,3]) # 4 16 24
print(a[0:2,3])#4,16 row zero and one
# 5 values which are equally space between 1 and 3
a=np.linspace(1,3,5) # gives equal pioints between 1-3 5 points
print(a)
a=np.linspace(1,3,10)
print(a)

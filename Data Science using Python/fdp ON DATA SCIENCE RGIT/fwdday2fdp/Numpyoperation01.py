#Numpy operation
#dimension of array size byte
import numpy as np
a=np.array([1,2,3])
print(a)
print(a.ndim)#1
a=np.array([(1,2,3),(2,3,4)])
print(a)

print(a.ndim)#2
print(a.itemsize)#4
print(a.dtype)#int 32

#size of array
a=np.array([1,2,3])
print(a)
print(a.size)
a=np.array([1,2,3,4,5,6,7])
print(a)
print(a.size)

#shape of array
a=np.array([1,2,3])
print(a)
print(a.shape)
a=np.array([(1,2,3),(2,3,4)])
print(a)
print(a.shape)

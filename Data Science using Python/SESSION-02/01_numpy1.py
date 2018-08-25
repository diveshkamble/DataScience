'''numpy is core library for scientific computing, efficient multidimensional
comtainer for storing data'''

import numpy as np
import matplotlib.pyplot as plt

a= np.array([1,2,3])   #creating one dimensional array

print(a)

a= np.array([(1,2,3),(4,5,6)])   #creating two dimensional array

print(a)

#numpy is better than list as it takes less memory, it is fast and efficient and covinient#
#numpy takes less memory
import time

import sys

s=range(1000)       #create integer values between 0 to 1000 but will not include 1000.


print(sys.getsizeof(3)*len(s))  #get size of s

d=np.arange(1000)

print(d.size*d.itemsize)


#numpy is faster
size=10000

L1=range(size)
L2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start=time.time()
result=a1+a2


print((time.time()-start)*1000)

#numpy operations
#find dimension,byte size, datatype
a =np.array([(1,2,3),(2,3,4)])
print(a.ndim)

print(a.itemsize)

print(a.dtype)

#find size of array, shape of an array

print(a.size)

a =np.array([1,2,3])
print(a.shape)

#reshape(transpose) and slicing
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
a=a.reshape(4,2)


#extracting vertical elements of Array
a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2])
print(a[0:,3])

a=np.array([(1,2,3,4),(3,4,5,6),(7,8,9,10)])
print(a[0:2,3])#print 3 rd element from row 0 to 1

a = np.linspace(1,3,5)#print five values which are equally spaced between 1 to 3
print(a)

#min max and sum of numpy array
a=np.array([1,2,3,4])
print(a)
print(" Max : ",a.max())
print(" Min : ",a.min())
print(" sum : ",a.sum())

#2 D
a=np.array([(1,2,3,4),(5,6,7,8)])
print(a)
print(" Max : ",a.max())
print(" Min : ",a.min())
print(" sum : ",a.sum())

#axis 1 are rows, axis 0 is column

a=np.array([(1,2,3),(3,4,5)])
print(a.sum(axis=0)) #print sum of all columns
#print(" sum axis o:",a.sum(axis=0)) # colum sum  4,6,8
print(a.sum(axis=1))    #print sum of all rows
#print(" sum axis 1:",a.sum(axis=1)) #sum of row 1 and row 2 6,12



#standard deviation
#standard deviation is deviation of all elements from the mean value
a=np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a))
print(np.std(a))

#addition, multiplication,division, subtraction

a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#concatenate two arrays---vertical stacking, horizontal stacking

a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(np.vstack((a,b))) 
print(np.hstack((a,b)))

#single column
print(a.ravel()) #CONVERT n dimensional array into single column

#numpy special functions sine and cosine functions to print graph


x=np.arange(0,3*np.pi,0.1)

y=np.sin(x)

plt.plot(x,y) #only plot not display
plt.show()  #make graph visible


'''x=np.arange(0,3*np.pi,0.1)

y=np.cos(x)

plt.plot(x,y)
plt.show()'''



'''x=np.arange(0,3*np.pi,0.1)

y=np.tan(x)

plt.plot(x,y)
plt.show()'''''


#Numpy operation
import numpy as np
ar=np.array([1,2,3])
print("array :",ar)
print(np.exp(ar))
# natural log ie log base e
print(np.log(ar))
# log base 10
print(np.log10(ar))

























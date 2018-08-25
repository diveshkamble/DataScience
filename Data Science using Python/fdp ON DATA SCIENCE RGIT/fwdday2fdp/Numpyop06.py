#Numpy operation
# matrix operations
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#concatenate
#vertical stacking
print(np.vstack((a,b)))
# horizontzl stacking
print(np.hstack((a,b)))
print(a)
# convert np array to single column
print(a.ravel())

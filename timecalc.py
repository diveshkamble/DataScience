import numpy as np
import time

import sys

s=range(1000)       #create integer values between 0 to 1000 but will not include 1000.



#numpy is faster
size=1000

L1=range(size)
L2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print (result)
print((time.time()-start))

start=time.time()
result=a1+a2


print((time.time()-start))

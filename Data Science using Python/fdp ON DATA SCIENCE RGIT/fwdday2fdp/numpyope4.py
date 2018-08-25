#Numpy operation
# axis
import numpy as np
a=np.array([(1,2,3),(3,4,5)])
print("a :\n",a)
print("column sum")
print(" sum axis o:",a.sum(axis=0)) # colum sum  4,6,8
print("row sum")
print(" sum axis 1:",a.sum(axis=1)) #sum of row 1 and row 2 6,12

# numpy vs list
#less memory fast convinietn
import numpy as np
import sys # for system
s=list(range(1000)) # take 0-999

print (" memory occupied by list: ",sys.getsizeof(3)*len(s))
D=np.arange(1000)
#print (D)
print (" memory occupied by numpy array: ",D.size*D.itemsize)

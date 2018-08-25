#plotting bar horizontally

import numpy as np
import matplotlib.pyplot as plt

objects=('python','c++','java','perl','scala','List')
y_pos=np.arange(len(objects)) 
performance= [10,8,6,4,2,1]

plt.barh(y_pos, performance, align="center") #barh
plt.yticks(y_pos, objects)
plt.xlabel('Usage')
plt.title('Programming langugae usage-pyhtonspot.com')
    
plt.show()

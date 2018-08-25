import numpy as np
import matplotlib.pyplot as plt

objects=('python','c++','java','perl','scala','List')
y_pos=np.arange(len(objects)) 
performance= [10,8,6,4,2,1]

plt.bar(y_pos, performance, align="center") 
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming langugae usage')
    
plt.show()

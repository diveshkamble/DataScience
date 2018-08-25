import numpy as np
import matplotlib.pyplot as plt

# create data
N=50
x=np.random.rand(N)
y=np.random.rand(N)

#colors=(0,0,0)
area=np.pi*3

#plot
plt.scatter(x,y,s=area,c='g',alpha=0.5)#alpha defines brightness of dots range from 0-1
plt.title('scatter plot techniques')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

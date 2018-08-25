#Numpy operation
# sin cos tan
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-1,3*np.pi,0.1)
#x=np.arange(5,10,10)
y=np.sin(x)
print("x :",x)
print("y :",y)

# y= np.cos(x)
# y= np.tan(x)
plt.plot(x,y) # only plot not display
plt.show() # make graph visibl

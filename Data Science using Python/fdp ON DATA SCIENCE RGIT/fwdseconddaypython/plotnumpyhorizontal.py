import numpy as np
import matplotlib.pyplot as plt
#data to plot
n_groups=4
means_frank=(90,55,40,65)
means_guido=(85,62,54,20)
#create plot
fig,ax = plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
rects1 = plt.barh(index, means_frank, bar_width, alpha=opacity, color='b',label='franks')
rects2 = plt.barh(index+ bar_width, means_guido, bar_width, alpha=opacity, color='g',label='guido')

plt.xlabel('Person')
plt.ylabel('scores')
plt.title('scores by person')
plt.yticks(index+bar_width,('A','B','C','D'))
plt.legend()
plt.show()

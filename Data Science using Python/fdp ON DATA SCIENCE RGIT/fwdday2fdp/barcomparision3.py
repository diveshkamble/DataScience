import numpy as np
import matplotlib.pyplot as plt
#dat to plot
n_groups=4
means_freak=(90,55,40,65)
means_guido=(85,62,54,20)

fig, ax=plt.subplots()
index=np.arange(n_groups)
bar_width=0.35
opacity=0.8
#barh for horozontal
rects1=plt.bar(index,means_freak,bar_width,alpha=opacity,color='b',label='Frank')
rects2=plt.bar(index+bar_width,means_guido,bar_width,alpha=opacity,color='g',label='guido')
plt.xlabel('person')
plt.xlabel('score')
plt.xlabel('score by person')
#xticks for horizontal
plt.xticks(index+bar_width,('A','B','C','D'))
plt.legend()
plt.show()#plot tight layout

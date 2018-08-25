import matplotlib.pyplot as plt
#pie chart plot

labels=['python','c++','rubby','java']
sizes=[215,130,245,210]# size of each labels block
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=[0.5,0.0,0.0,0.0] # explode lst slide means seperate parts

#plot
#startangle is starting point of first labesl like python start from 180 degree
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.4f%%',shadow=True,startangle=100)# 1.4f%% defines 4 afterdecimal point
#plt.axis('equal') #changes limits of x or y axis so that equal increments of x and y have the same length

plt.show()



import numpy as np
import matplotlib.pyplot as plt

# create data
N=50
x=np.random.rand(N) #geneartes N points between 0 to 1
y=np.random.rand(N)

#colors=(0,0,0)
area=np.pi*3

#plot
plt.scatter(x,y,s=area,c='g',alpha=0.5)#alpha defines brightness of dots range from 0-1
plt.title('scatter plot techniques')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


from pylab import *

t=arange(0.0,2.0,0.01)# start from 0.0 goto 2.0 with increment 0.01 (x-axis)
s=sin(2.5*pi*t) #  y aixs
plot(t,s)

xlabel('time(s)')
ylabel('voltage(mv)')
title('sine wave')

grid (True)
show()


import numpy as np

#barchart data to plot
n_groups=4
means_freak=(90,55,40,65)
means_guido=(85,62,54,20)

fig,ax=plt.subplots()
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

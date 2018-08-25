import matplotlib.pyplot as plt
#data plot

labels=['python','c++','rubby','java']
sizes=[215,130,245,210]# size of each labels block
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=[0.2,0.0,0.0,0.0] # explode lst slide means seperate parts

#plot
#startangle is starting point of first labesl like python start from 180 degree
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.4f%%',shadow=True,startangle=180)# 1.4f%% defines 4 afterdecimal point
plt.axis('equal')
plt.show()

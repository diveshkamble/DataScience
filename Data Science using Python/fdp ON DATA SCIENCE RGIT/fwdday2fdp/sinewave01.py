from pylab import *

t=arange(0.0,2.0,0.01)# start from 0.0 goto 2.0 with increment 0.01 (x-axis)
s=sin(2.5*pi*t) #  y aixs
plot(t,s)

xlabel('time(s)')
ylabel('voltage(mv)')
title('sine wave')

grid (True)
show()

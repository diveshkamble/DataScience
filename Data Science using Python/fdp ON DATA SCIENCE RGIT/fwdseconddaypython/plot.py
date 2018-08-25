from pylab import *

t=arange(0.0,2.0,0.01)
s=sin(2.5*pi*t)
plot(t,s)

xlabel('time(s)')
ylabel('volatge')
title('sine wave')
grid(True)
show()

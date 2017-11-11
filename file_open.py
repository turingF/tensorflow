
failnum1 = []   #failure number
failtime1 = [] #time-to-failure

f = open('D:\\failure data\\CSR1.DAT','rb')

#read data from file
import string
while True:
    line = f.readline()
    line2 = line.strip().split('\t'.encode('utf-8'))
    if len(line) == 0:
        break
    failnum1.append(float(line2[0]))
    failtime1.append(float(line2[1]))
f.close()


import numpy as np
failnum = np.array(failnum1)[:,np.newaxis]
failtime = np.array(failtime1)[:,np.newaxis]
# for i in failnum1:
#     x1 = []
#     x1.append(i)
#     failnum.append(x1)
#
# for j in failtime1:
#     x2 = []
#     x2.append(j)
#     failtime.append(x2)


from pylab import *

plot(failnum,failtime)
show()
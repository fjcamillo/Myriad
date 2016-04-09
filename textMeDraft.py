__author__ = 'Francisc'

import serial
# import numpy as np
from matplotlib import pyplot as plt
ser = serial.Serial('COM8', 9600)
numberOfGets = 0
plt.ion() # set plot to animated

ydata = [0] * 50
ax1=plt.axes()

# make plot
line, = plt.plot(ydata)
# plt.ylim([10, 40])

# start data collection
while True:
    numberOfGets += 1
    data = ser.readline()[:2]
    # print data
    ymin = float(min(ydata))-10
    ymax = float(max(ydata))+10
    # plt.ylim([ymin,ymax])
    ydata.append(data)
    del ydata[0]
    line.set_xdata(numberOfGets)
    line.set_ydata(ydata)  # update the data
    plt.draw() # update the plot

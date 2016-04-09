__author__ = 'Francisc'
__author__ = 'Shella'
import matplotlib.pyplot as plt
import serial

arduino = serial.Serial('COM8', 9600, timeout = .1) #Serially Connect to the Arduino

# plt.ion()   #Turn Interactive On
fig = plt.figure()
gasSensorGraph = fig.add_subplot(1, 1, 1, axisbg='black')




__author__ = 'Francisc'

import serial
from chikka import Chikka

arduino = serial.Serial('COM8', 9600, timeout=.1)
x = ""
z=0
while z != 1:
    x = arduino.readline()[:-2]
    gasSensed = x.decode()
    # smokeSensed = x[1]
    y = x[:3]
    print(gasSensed)
    if gasSensed != "":
        if int(gasSensed) < 100:
            arduino.write("LOW Level")
        elif (int(gasSensed) > 600) and (int(gasSensed) < 700):
            c = Chikka(client_id='2b9be5d5c8ed8cc0f82e1a50605e895b86185f4e3be995f55bd5830bd12cd18c',
                       secret_key='f36247fb05d604a38294aa369d69cdb6e37e299e90080d642d9d489149b4e556',
                       shortcode='292901343')
            c.send('639292591950', "Please check your house kitchen, a Gas Leakage was sensed!")
            z = 1
        elif int(gasSensed) > 700:
            pass


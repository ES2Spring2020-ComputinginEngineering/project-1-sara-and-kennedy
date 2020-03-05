#Names: Kennedy May and Sara Morrison

import math
import time
import microbit as mb
import radio  # Needs to be imported separately


radio.on()  # Turn on radio
radio.config(channel=19, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

fout = open("data1.csv", "w")
# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        data_acc = incoming
        data_acc = data_acc.split(",")
        data_acc = [int(data_acc[0]), int(data_acc[1]), int(data_acc[2]), int(data_acc[3])]
        data_acc = tuple(data_acc)
        print(data_acc)
        fout.write(incoming)


        mb.sleep(10)

fout.close()
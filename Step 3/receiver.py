##################
# FILL IN HEADER
#################

#IMPORT STATMENTS
import microbit as mb
import radio  # Needs to be imported separately
import time
import math
from microbit import*

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=19, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')

fout = open("data1.csv", "w")

while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)

        data_acc = incoming
        data_acc = data_acc.split(',')
        data_acc = [int(data_acc[0]), int(data_acc[1]), int(data_acc[2]), int(data_acc[3]))
        data_acc = tuple(data_acc)
        print(data_acc)
        fout.write(incoming)

        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################

        mb.sleep(10)


fout.close()
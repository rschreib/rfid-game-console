#Names: Robert Schreibman & Robinson Merillat
#Date: 04/22/18
#Class: csci250 - Sensors
#Description: This code will...
# 1) Read an RFID tag
#   if: tag exists then player proxy settings & infor and  will be imported
#   from a file
#   else: game will ask for new player information
# 2) Then game will be played
# 3) Game stats will be saved into a file 

# import smbus
import time
from time import sleep
import RPi.GPIO as GPIO
import math

pin20 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin20,GPIO.IN)

# Get I2C bus - initial bus to channel 1
# bus = smbus.SMBus(1)
flag = 0
firstvalue = 9

try:
    while True:
        value = GPIO.input(pin20)
        print(value)
        if flag == 0:
            flag = 1
            firstvalue = GPIO.input(pin20)
        if value != firstvalue:
            break

# #!/usr/bin/env python
# import time
# import sys
#
# card = '0019171125'        # Stored good card number consider using a list or a file.
#
# def main():                # define a main function.
#     while True:            # loop until the program encounters an error.
#         sys.stdin = open('/dev/tty0', 'r')
#         RFID_input = input()
#         if RFID_input == card:      # compare the stored number to the input and if True execute code.
#             print "Access Granted"
#             print "Read code from RFID reader:{0}".format(RFID_input)
#         else:                    # and if the condition is false excecute this code.
#             print "Access Denied"
#
# # where is tty defined??
#             tty.close()

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... bye!")

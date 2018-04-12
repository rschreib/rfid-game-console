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
import serial
import UserClass as user
import usersFile
import PracticeGame as game

port = serial.Serial(
	"/dev/ttyUSB0",
	baudrate=9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	writeTimeout = 0,
	rtscts = False,
	dsrdtr = False,
	xonxoff = False)

data=bytes([0x0c, 0x80, 0x09, 0x00, 0xf0, 0xce, 0x61, 0x9d, 0x01, 0x00,
            0x01, 0x00, 0x00, 0x00])

print(port.isOpen())
print("Port opened...")
port.write(data)
print("Data sent")

pin20 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin20,GPIO.IN)

# Get I2C bus - initial bus to channel 1
# bus = smbus.SMBus(1)
flag = 0
firstvalue = 9

# fns that can eventually be offloaded to seperate file
def add_user(ID):
    # TODO ask user for user info
    newuser = user.User("aaaaaa", 21)
    users[ID] = newuser
    print(users)

def laod_user(ID):
    return users(ID)

def save_users(u):
	usersFile.users = u

def load_users():
	return usersFile.users


users = load_users() # load users dict from usersFile
print(users)

try:
    while True:
        save_users(users)
        response = str(port.read(16))
        if response in users:
            print("Welcome Back ", response)
			# call login fn and read user data
        else:
            print("Creating new user")
            print("Welcome User : ", response)
            add_user(response)
            # call call make new user fn

		game.StartGame()

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... bye!")

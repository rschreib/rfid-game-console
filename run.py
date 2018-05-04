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
import PracticeGame as game
import pickle

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

acceptedResponses = ['y','Y','yes','Yes','YES','']

print(port.isOpen())
print("Port opened...")
port.write(data)
print("Data sent")

pin20 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin20,GPIO.IN)

usersFile = 'users.txt'

# Get I2C bus - initial bus to channel 1
# bus = smbus.SMBus(1)
flag = 0
firstvalue = 9

# fns that can eventually be offloaded to seperate file later..... or never... who cares #coursework

# create new user account
def add_user(ID):
    # TODO ask user for user info
	if ID == "":  # if user was new and logged in w/o using card
		print("Card not used to scan")
		scanCard = input("Would you like to scan an RFID card?")
		if scanCard in acceptedResponses:
			response = str(port.read(16))
			name = input("Enter Username : ")
			age = input("Age : ")
			newuser = user.User(name, int(age))
    newuser = user.User("New User", 21)
    users[ID] = newuser
    print(users)

def laod_user(ID):
    return users(ID)

def save_users(u):
	pickle.dump(u, open(usersFile, 'wb'))
	print(u)

def load_users():
	try:
		return pickle.load(open(usersFile, 'rb'))
	except pickle.UnpicklingError:
		print("error loading file")
		data = {}
		return data

users = load_users() # load users dict from usersFile
if users == None:
	users = {}
print(users)

try:
    while True:
		print("Enter your password or scan:")
		response = str(port.read(16))    # gathers response from RFID
		if (response):                   # if response was given, then scan was entered
			if response in users:
            	print("Welcome Back ", response)
				game.startGame()
				# call login fn and read user data
        	else:
            	print("Creating new user")
            	print("Welcome User : ", response)
            	add_user(response)
            	save_users(users)
				game.StartGame()
            	# call call make new user fn
		userName = input("Username : ")
		for u in users:
			if userName == u.name:
				print("Welcome Back ", response)
				game.startGame()
				# call login fn and read user data
			else:
				print("Username doesn't exist yet")
				r = input("Would you like to create a new account? [Y/n] : ")
				if r in acceptedResponses:
					add_user("")

#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit):
    print("User requested exit... bye!")

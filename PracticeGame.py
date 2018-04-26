from time import sleep
from os import system
import numpy
import tictactoe
import fourinarow

def StartGame():
    response = input("Play a game? [Y/n] ")
    acceptedResponses = ['y','Y','yes','Yes','YES','']
    playGame = False
    gameStartCounter = 3

    for item in acceptedResponses:
        if (response == item):
            playGame = True
            print("playing game")

    if (not(playGame)):
        print("Okay, Cya Later!")
        exit()

    response = 1
    print("1: Tic Tac Toe\n")
    print("2: Four in a Row\n")
    response = input("Select a game:")

    print("Game starting in...")
    for i in range(gameStartCounter):
        print("{}".format(gameStartCounter-i))
        sleep(.5)

    if (response == '1'):
        tictactoe.main()
        input("\n\nPress the enter key to quit.")
    elif (response == '2'):
        fourinarow.main()
    else:
        exit()

def does_user_exist(userID):
    for user in open("usernames.txt").readlines():
        user = user.rstrip()
        if userID == user:
            return(True)
    return(False)

# print(does_user_exist("Robert"))

StartGame()

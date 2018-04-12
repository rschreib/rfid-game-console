
from time import sleep

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


    print("Game starting in...")
    for i in range(gameStartCounter):
        print("{}".format(gameStartCounter-i))
        sleep(.5)

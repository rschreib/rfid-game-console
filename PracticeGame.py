
from time import sleep

input = input("Play a game? [Y/n] ")
acceptedResponses = ['y','Y','yes','Yes','YES','']
playGame = False

for response in acceptedResponses:
    if (input == response):
        playGame = True
        print("playing game")

if (not(playGame)):
    print("Okay, Cya Later!")
    exit()


print("Game starting in...")
count = 3
for i in range(count):
    print("{}".format(count-i))
    sleep(.5)

player1 = raw_input("Username: ")


def startGame():
    loadPlayerData

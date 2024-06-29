#INPUTS
# value = input("Put in a value here:\n")
#
# print(value)
# print(type(value))

import sys
import random
from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3
#
#
# print("")
# playerchoice = input("Enter...."
#                      "\n1 for Rock, or \n2 for Paper, "
#                      "or \n3 for Scissors:\n\n")
#
# player = int(playerchoice)
#
# if 3 < player < 1:
#     sys.exit("You must enter either 1, 2 or 3.")
#
# computerchoice = random.choice("123") #Computer's choics of rps
#
# computer = int(computerchoice)

# print("")
# print("You chose " + str(RPS(player)).replace("RPS", "") + ",")
# print("Python chose " + str(RPS(computer)) + ".")
# print("")


def rps():
    tie, lose, win, count = 0, 0, 0, 0 #Initializes values to update later

    games = int(input("Enter the number of games to play: ")) #Number of games to play

    while count < games: #while loop for number of games
        p = int(input("Enter...."
                      "\n1 for Rock, or \n2 for Paper, "
                      "or \n3 for Scissors:\n\n"))
        cmp = int(random.choice("123"))
        #ALL SCENARIOS
        if (p == 1 and cmp == 3) or (p == 2 and cmp == 1) or (p == 3 and cmp == 2):
            print("🎉 You win!")
            count += 1
            win += 1
        elif (p == 3 and cmp == 1) or (p == 1 and cmp == 2) or (p == 2 and cmp == 3):
            print("🤖🐍 Computer python wins!")
            count += 1
            lose += 1
        elif p == cmp:
            print("👔 Tie game!")
            count += 1
            tie += 1
        else:
            print("That's not a valid input")
    print(f"Number of games played: {count}")
    print(f"Wins: {win}\nLosses: {lose}\nTied: {tie}\n")


rps()

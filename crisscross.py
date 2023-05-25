#to Do List
#make error for all input

import random
import sys

def main():

    def removeRandom():
        nonlocal player1
        randomNum = random.randint(0,len(RANDOMNUM)-1)
        x = RANDOMNUM[randomNum]
        player1 += x
        RANDOMNUM[randomNum] = 'x'

    RANDOMNUM = []
    GRIDSIZE = int(input('Enter Grid Size: '))
    player1 = 0
    player2 = 0
    generateRandomNum(RANDOMNUM,GRIDSIZE)
    layout(RANDOMNUM,GRIDSIZE)
    printScore(GRIDSIZE,player1,player2)
    askGameStart()
    removeRandom()
    layout(RANDOMNUM,GRIDSIZE)
    printScore(GRIDSIZE,player1,player2)


def generateRandomNum(randomNum,size):
    while len(randomNum) != size * size: #append all random number can create a func ~hx~ then return randomnum :)
        x = random.randint(-30,30)
        randomNum.append(x)
    

def layout(randomNum,size):
    i = 0
    for row in range(size):
        print("------" * size,end = "")
        print("-")
        for column in range(size):
            print("|",end = "")
            if randomNum[i] == 'x' or randomNum[i] >= 0 and randomNum[i] < 10:
                print(f"  {randomNum[i]}  ",end = "")
            elif randomNum[i] >= 10:
                print(f" {randomNum[i]}  ",end= '')
            elif randomNum[i] < 0 and randomNum[i] > -10:
                print(f" {randomNum[i]}  ", end = '')
            else:
                print(f" {randomNum[i]} ",end = '')
            i += 1                 #to loop through list
            if column == size-1 :
                print("|")
    print("------" * size,end = "")
    print("-")

def askGameStart():
    while True:
        start = input('Start?(Y/N): ')
        if start == 'N' or start == 'n':
            sys.exit()
        elif start == 'Y' or start == 'y':
            break
        else:
            print("Invalid!")

def printScore(size,p1,p2):
    center = (size * 5) + (size + 1)
    centerter = center // 2
    player = (centerter - 12) / 2
    space = ' ' * int(player)
    print(space+f'Player 1 : {p1}'+space+space+f'Player 2 : {p2}')

main()
#to Do List
#make error for all input

import random
import sys
temp = ['x','x','x',3,4,5,6,7,8]

def main():

    def checkColumn(random, size):
        nonlocal gameRunning
        for row in range(size):
            countX = 0
            for column in range(row, len(random), size):
                if random[column] != 'x':
                    break
                elif random[column] == 'x':
                    countX = countX + 1
                    if countX == size:
                        gameRunning = False
                        break

    def checkRow(random, size):
        for column in range(0,len(random),size):
            countX = 0
            for row in range(column, column+size):
                if random[row] != 'x':
                    break
                elif random[row] != 'x':
                    countX = countX + 1
                    if countX == size:
                        gameRunning = False
                        break

    def removeRandom(list):
        nonlocal player1
        randomNum = random.randint(0,len(list)-1)
        x = list[randomNum]
        player1 += x
        list[randomNum] = 'x'

    RANDOMNUM = []
    GRIDSIZE = int(input('Enter Grid Size: '))
    player1 = 0
    player2 = 0
    storeIndex = 0
    gameRunning = True
    checkColumn(temp,3)
    checkRow(temp,3)
    print(gameRunning)
    # generateRandomNum(RANDOMNUM,GRIDSIZE)
    # layout(RANDOMNUM,GRIDSIZE)
    # askGameStart()
    # removeRandom(RANDOMNUM)
    # layout(RANDOMNUM,GRIDSIZE)
    # printScore(GRIDSIZE,player1,player2)


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
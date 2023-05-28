#to Do List
#make error for all input
import random
import sys

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
        nonlocal gameRunning
        for column in range(0,len(random),size):
            countX = 0
            for row in range(column, column+size):
                if random[row] != 'x':
                    break
                elif random[row] == 'x':
                    countX = countX + 1
                    if countX == size:
                        gameRunning = False
                        break

    def selectColumn(random, size, index):
        nonlocal player2
        nonlocal storeIndex
        while True:
            chooseColumn = int(input('Enter Column Number: '))
            if chooseColumn <= 0 or chooseColumn > size:
                print("Please choose a valid number! ")
            else:
                while index >= size:   #to get first row index num
                    index -= size      #
                index = index + (size * (chooseColumn-1))
                if random[index] == 'x':
                    print("It's already chosen!")
                elif random[index] != 'x':
                    player2 += random[index]
                    random[index] = 'x'
                    storeIndex = index
                    break

    def selectRow(random, size, index):
        nonlocal player1
        nonlocal storeIndex    
        while True:
            chooseRow = int(input('Enter Row Number: '))
            if chooseRow <= 0 or chooseRow > size:
                print("Please choose a valid number! ")
            else:
                for x in range(size-1, size*size, size):
                    if index <= x :
                        index = x
                        index = index - size
                        break
                index += chooseRow
                if random[index] == 'x':
                    print("It's already chosen!")
                elif random[index] != 'x':
                    player1 += random[index]
                    random[index] = 'x'
                    storeIndex = index
                    break
    def gameplay():
        nonlocal gameRunning
        i = 0
        while gameRunning:
            selectColumn(RANDOMNUM,GRIDSIZE,storeIndex)
            currentColumn(storeIndex,GRIDSIZE)
            layout(RANDOMNUM,GRIDSIZE)
            printScore(GRIDSIZE,player1,player2)
            checkColumn(RANDOMNUM,GRIDSIZE)
            checkRow(RANDOMNUM,GRIDSIZE)
            selectRow(RANDOMNUM,GRIDSIZE,storeIndex)
            currentColumn(storeIndex,GRIDSIZE)
            layout(RANDOMNUM,GRIDSIZE)
            printScore(GRIDSIZE,player1,player2)
            checkColumn(RANDOMNUM,GRIDSIZE)
            checkRow(RANDOMNUM,GRIDSIZE)
            i += 1
        if player1 > player2:
            print("Player 1 WON!")
        elif player2 > player1:
            print("Player 2 WON!")
        while True:
            restart = input("Would you like to play again?(Y/N): ")
            if restart == 'y' or restart == 'Y':
                main()
            elif restart == 'n' or restart == 'N':
                sys.exit()
            else:
                print("Invalid! Please input again.")

    def removeRandom(list):
        nonlocal player1
        nonlocal storeIndex
        randomNum = random.randint(0,len(list)-1)
        storeIndex = storeIndex + randomNum
        x = list[randomNum]
        player1 += x
        list[randomNum] = 'x'

    RANDOMNUM = []
    GRIDSIZE = int(input('Enter Grid Size: '))
    player1 = 0
    player2 = 0
    storeIndex = 0
    gameRunning = True
    generateRandomNum(RANDOMNUM,GRIDSIZE)
    layout(RANDOMNUM,GRIDSIZE)
    askGameStart()
    removeRandom(RANDOMNUM)
    currentColumn(storeIndex,GRIDSIZE)
    layout(RANDOMNUM,GRIDSIZE)
    printScore(GRIDSIZE,player1,player2)
    gameplay()

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
            print("Invalid! Please input again.")

def printScore(size,p1,p2):
    center = (size * 5) + (size + 1)
    centerter = center // 2
    player = (centerter - 12) / 2
    space = ' ' * int(player)
    print(space+f'Player 1 : {p1}'+space+space+f'Player 2 : {p2}')

def currentColumn(index,size):
    whichColumn = 0
    space = "      "
    print("   ")
    while index > size:
        index -= size
    whichColumn = index
    space *= whichColumn
    print(space + '   '+ "V")
main()
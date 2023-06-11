import random
import sys

def main():
    randomNum = []
    GRIDSIZE = int(input('Enter Grid Size: ')) #should make a error
    player1,player2 = 0,0
    storeIndex = 0
    gameRunning = True
    shuffleChanceP1,shuffleChanceP2 = 1,1
    generateRandomNum(randomNum,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,"nothing")
    askGameStart()
    print("\n\n\nWELCOME TO THE GAME!!\n\n\n")
    player1, storeIndex = removeRandom(player1,storeIndex,randomNum)
    currentColumn(storeIndex,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,False)
    printScore(GRIDSIZE,player1,player2)
    while gameRunning:
        player2, storeIndex = selectColumn(player2,storeIndex,randomNum,GRIDSIZE)
        columnNum(GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,True)
        printScore(GRIDSIZE,player1,player2)
        print("-"*GRIDSIZE*7,"\n")
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
        shuffleChanceP2 = shuffle(storeIndex,randomNum,GRIDSIZE,shuffleChanceP2,True,gameRunning,player1,player2)
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
        if gameRunning == False: break
        player1, storeIndex = selectRow(player1,storeIndex,randomNum,GRIDSIZE)
        currentColumn(storeIndex,GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,False)
        printScore(GRIDSIZE,player1,player2)
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
        shuffleChanceP1 = shuffle(storeIndex,randomNum,GRIDSIZE,shuffleChanceP1,False,gameRunning,player1,player2)
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
    if player1 > player2:
        print("Player 1 WON!\n")
    elif player2 > player1:
        print("Player 2 WON!\n")
    while True:
        restart = input("Would you like to play again?(Y/N): ")
        restart = restart.lower()
        if restart == 'y':
            main()
        elif restart == 'n':
            sys.exit()
        else:
            print("Invalid! Please input again.")

def generateRandomNum(randomNum,size):
    while len(randomNum) != size * size: #append all random number can create a func ~hx~ then return randomnum :)
        x = random.randint(-30,30)
        randomNum.append(x)
    
def layout(index,randomNum,size,showRow):
    printingRow = 1
    whichRow = currentRow(index,randomNum,size)
    i = 0
    for row in range(size):
        print("------" * size + '-')
        for column in range(size):
            print("|",end = "")
            if randomNum[i] == 'x' or randomNum[i] >= 0 and randomNum[i] < 10:
                print(f"  {randomNum[i]}  ",end = '')
            elif randomNum[i] >= 10:
                print(f" {randomNum[i]}  ",end= '')
            elif randomNum[i] < 0 and randomNum[i] > -10:
                print(f" {randomNum[i]}  ", end = '')
            else:
                print(f" {randomNum[i]} ",end = '')
            i += 1                 #to loop through list
        print(f"|",end='')
        if showRow == "nothing":
            print()
        elif showRow == False:
            print("", printingRow)
        elif showRow == True:
            if whichRow == printingRow:
                print("<<<")
            elif whichRow != printingRow:
                print()
        printingRow += 1
    print("------" * size + '-')

def printScore(size,p1,p2):
    center = (size * 5) + (size + 1)
    centerter = center // 2
    player = (centerter - 12) / 2
    space = ' ' * int(player)
    print(space+f'Player 1 : {p1}'+space+space+f'Player 2 : {p2}\n')

def askGameStart():
    while True:
        start = input('Start?(Y/N): ')
        start = start.lower()
        if start == 'n':
            sys.exit()
        elif start == 'y':
            break
        else:
            print("Invalid! Please input again.")

def shuffle(index,list,size,chance,row,condition,p1,p2):
    if chance != 0 and condition != False:
        while True:
            if row == True:
                shuff = input("P2 do you want to shuffle?(Y/N): ")
            elif row == False:
                shuff = input("P1 do you want to shuffle?(Y/N): ")
            if shuff == 'n' or shuff == 'N':
                return 1
            elif shuff == 'y' or shuff == 'Y':
                break
            else:
                print("Invalid! Please input again.")
        random.shuffle(list)
        if row == True:
            columnNum(size)
        elif row == False:
            currentColumn(index,size)
        layout(index,list,size,row)
        printScore(size,p1,p2)
        return 0

def removeRandom(p1, index, list):
    randomNum = random.randint(0,len(list)-1)
    index += randomNum
    x = list[randomNum]
    p1 += x
    list[randomNum] = 'x'
    return p1, index

def checkColumn(random, size,condition):
    for row in range(0,size):
        countX = 0
        for column in range(row, len(random), size):
            if random[column] != 'x':
                break
            elif random[column] == 'x':
                countX = countX + 1
                if countX == size:
                    return False
    return condition

def checkRow(random, size,condition):
    for column in range(0,len(random),size):
        countX = 0
        for row in range(column, column+size):
            if random[row] != 'x':
                break
            elif random[row] == 'x':
                countX = countX + 1
                if countX == size:
                    return False
    return condition

def selectColumn(p2,index,random, size):
    while True:
        print('Now Player2 Turn')
        chooseColumn = int(input(f"Enter Column Number 1-{size}: "))
        if chooseColumn <= 0 or chooseColumn > size:
            print("Please choose a valid number! \n")
        else:
            while index >= size:   #to get first row index num
                index -= size      #
            index = index + (size * (chooseColumn-1))
            if random[index] == 'x':
                print("It's already chosen!\n")
            elif random[index] != 'x':
                p2 += random[index]
                random[index] = 'x'
                return p2, index

def selectRow(p1, index, random, size):
    while True:
        print('Now Player1 Turn')
        chooseRow = int(input(f"Enter Row Number 1-{size}: "))
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
                p1 += random[index]
                random[index] = 'x'
                return p1, index

def currentColumn(index,size):
    whichColumn = 0
    space = "      "
    print("   ",end='')
    while index >= size:
        index -= size
    whichColumn = index
    space *= whichColumn
    print(space + "V")

def currentRow(index, random, size):
    i = 1
    for x in range(size, len(random), size):
        if index < x :
            break
        i = i + 1
    return i

def columnNum(size):
    print('   ',end='')
    for x in range(1, size+1):
        print(x,end='')
        print('     ',end='')
    print()

main()
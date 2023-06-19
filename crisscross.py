import random
import sys


# Course: PSP0101 Problem Solving and Program Design
# Assignment: Crisscross
# Session : T2220
# Lab Class Code: TT1L
# ID & Name 1:1221105155, LIM WEI JUN
# Phone,Email:0182127780, 1221105155@student.mmu.edu.my

# Group Leader:
# Lab Class Code: TT1L
# ID & Name 1:1221105156, CHANG HOE HIN
# Phone,Email:0172453131, 1221105156@student.mmu.edu.my

def main():
    print('LIM WEI JUN, CHANG HOE HIN')
    randomNum = []
    GRIDSIZE = int(input('Enter Grid Size: ')) #should make a error
    player1,player2 = 0,0
    storeIndex = 0
    gameRunning = True
    shuffleChanceP1,shuffleChanceP2 = 1,1
    randomNum = generateRandomNum(randomNum,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,"nothing")
    askGameStart()
    print("\n\n\nWELCOME TO THE GAME!!\n\n\n")
    player1, storeIndex = removeRandom(player1,storeIndex,randomNum)
    currentColumn(storeIndex,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,False)
    printScore(GRIDSIZE,player1,player2)
    while gameRunning:
        player2, storeIndex, shuffleChanceP2 = selectColumn(storeIndex,randomNum,GRIDSIZE,player2,shuffleChanceP2)
        columnNum(GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,True)
        printScore(GRIDSIZE,player1,player2)
        print("-"*GRIDSIZE*7,"\n")
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
        if gameRunning == False: break
        player1, storeIndex, shuffleChanceP1 = selectRow(storeIndex,randomNum,GRIDSIZE,player1,shuffleChanceP1)
        currentColumn(storeIndex,GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,False)
        printScore(GRIDSIZE,player1,player2)
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
    randomNum = [random.randint(-30,30) for x in range((size*size)+1)]
    return randomNum
    
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

def removeRandom(p1, index, list):
    randomNum = random.randint(0,len(list)-1)
    index += randomNum
    x = list[randomNum]
    p1 += x
    list[randomNum] = 'x'
    return p1, index

def checkColumn(list, size,condition):
    for row in range(0,size):
        countX = 0
        for column in range(row, len(list), size):
            if list[column] != 'x':
                break
            elif list[column] == 'x':
                countX = countX + 1
                if countX == size:
                    return False
    return condition

def checkRow(list, size,condition):
    for column in range(0,len(list),size):
        countX = 0
        for row in range(column, size):
            print(row)
            if list[row] != 'x':
                break
            elif list[row] == 'x':
                countX = countX + 1
                if countX == size:
                    return False
    return condition

def selectColumn(index,list,size,p2,chance):
    while True:
        print('Now Player2 Turn')
        chooseColumn = input(f"Enter Column Number 1-{size}: ")
        try :
            chooseColumn = int(chooseColumn)
            if chooseColumn <= 0 or chooseColumn > size:
                print("Please choose a valid number! \n")
            else:
                while index >= size:   #to get first row index num
                    index -= size      #
                index = index + (size * (chooseColumn-1))
                if list[index] == 'x':
                    print("It's already chosen!\n")
                elif list[index] != 'x':
                    p2 += list[index]
                    list[index] = 'x'
                    return p2, index, chance
        except :
            if chance == 1:
                if chooseColumn == 'shuffle' or chooseColumn == 'Shuffle':
                    random.shuffle(list)
                    chance -= 1
                    return p2, index, chance
                else:
                    print('Error')
            else:
                print("Can't use shuffle again")

def selectRow(index,list,size,p1,chance):
    while True:
        print('Now Player1 Turn')
        chooseRow = input(f"Enter Row Number 1-{size}: ")
        try :
            chooseRow = int(chooseRow)
            if chooseRow <= 0 or chooseRow > size:
                print("Please choose a valid number! \n") 
            else:
                for x in range(size-1, size*size, size):
                    if index <= x :
                        index = x
                        index = index - size
                        break
                index += chooseRow
                if list[index] == 'x':
                    print("It's already chosen!\n")
                elif list[index] != 'x':
                    p1 += list[index]
                    list[index] = 'x'
                    return p1, index, chance
        except :
            if chance == 1:
                if chooseRow == 'shuffle' or chooseRow == 'Shuffle':
                    random.shuffle(list)
                    chance -= 1
                    return p1, index, chance
                else:
                    print('Error')
            else:
                print("Can't use shuffle again")

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
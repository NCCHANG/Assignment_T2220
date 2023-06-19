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
    player1Score = []
    player2Score = []
    while True:
        GRIDSIZE = int(input('Enter Grid Size: '))
        if GRIDSIZE < 11 and GRIDSIZE > 1:
            break
        else:
            print('Enter a Valid Integer')
    player1,player2 = 0,0
    storeIndex = 0
    gameRunning = True
    shuffleChanceP1,shuffleChanceP2 = 1,1
    randomNum = generateRandomNum(randomNum,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,"nothing")
    askGameStart()
    print("\n\n\nWELCOME TO THE GAME!!\n\n\n")
    player1, storeIndex = removeRandom(player1,storeIndex,randomNum,player1Score)
    currentColumn(storeIndex,GRIDSIZE)
    layout(storeIndex,randomNum,GRIDSIZE,False)
    printScore(player1,player2,player1Score,player2Score)
    while gameRunning:
        player2, storeIndex, shuffleChanceP2 = selectRow(storeIndex,randomNum,GRIDSIZE,player2,shuffleChanceP2,player2Score)
        columnNum(GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,True)
        printScore(player1,player2,player1Score,player2Score)
        gameRunning = checkColumn(randomNum,GRIDSIZE,gameRunning)
        gameRunning = checkRow(randomNum,GRIDSIZE,gameRunning)
        if gameRunning == False: break
        player1, storeIndex, shuffleChanceP1 = selectColumn(storeIndex,randomNum,GRIDSIZE,player1,shuffleChanceP1,player1Score)
        currentColumn(storeIndex,GRIDSIZE)
        layout(storeIndex,randomNum,GRIDSIZE,False)
        printScore(player1,player2,player1Score,player2Score)
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
    randomNum = [random.randint(-30,30) for x in range((size*size))]
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

def printScore(p1,p2,p1Score,p2Score):
    space = ' ' * 5
    print(space+f'Player 1 : {p1}'+space+space+f'Player 2 : {p2}\n')
    print(f'Player1: {p1Score} \n')
    print(f'Player2: {p2Score} \n')

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

def removeRandom(p1, index, list,p1Score):
    randomNum = random.randint(0,len(list)-1)
    index += randomNum
    x = list[randomNum]
    p1 += x
    p1Score.append(list[randomNum])
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
        for row in range(column, len(list)):
            if list[row] != 'x':
                break
            elif list[row] == 'x':
                countX = countX + 1
                if countX == size:
                    return False
    return condition

def selectRow(index,list,size,p2,chance,p2Score):
    print('Now Player2 Turn')
    while True:
        chooseRow = input(f"Enter Row Number 1-{size}: ")
        try :
            chooseRow = int(chooseRow)
            if chooseRow <= 0 or chooseRow > size:
                print("Please choose a valid number! \n")
            else:
                while index >= size:   #to get first row index num
                    index -= size      
                index = index + (size * (chooseRow-1))
                if list[index] == 'x':
                    print("It's already chosen!\n")
                elif list[index] != 'x':
                    p2 += list[index]
                    p2Score.append(list[index])
                    list[index] = 'x'
                    return p2, index, chance
        except :
            if chance == 1:
                if chooseRow == 'shuffle' or chooseRow == 'Shuffle':
                    random.shuffle(list)
                    chance -= 1 
                    return p2, index, chance
                else:
                    print('Invalid!')
            elif chooseRow == "shuffle" or chooseRow == 'Shuffle':
                print("You can't use shuffle again!")
            else:
                print("Invalid!")

def selectColumn(index,list,size,p1,chance,p1Score):
    print('Now Player1 Turn')
    while True:
        chooseColumn = input(f"Enter Column Number 1-{size}: ")
        try :
            chooseColumn = int(chooseColumn)
            if chooseColumn <= 0 or chooseColumn > size:
                print("Please choose a valid number! \n") 
            else:
                for x in range(size-1, size*size, size):
                    if index <= x :
                        index = x
                        index = index - size
                        break
                index += chooseColumn
                if list[index] == 'x':
                    print("It's already chosen!\n")
                elif list[index] != 'x':
                    p1 += list[index]
                    p1Score.append(list[index])
                    list[index] = 'x'
                    return p1, index, chance
        except :
            if chance == 1:
                if chooseColumn == 'shuffle' or chooseColumn == 'Shuffle':
                    random.shuffle(list)
                    chance -= 1 
                    return p1, index, chance
                else:
                    print('Invalid!')
            elif chooseColumn == "shuffle" or chooseColumn == 'Shuffle':
                print("You can't use shuffle again!")
            else:
                print("Invalid!")

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
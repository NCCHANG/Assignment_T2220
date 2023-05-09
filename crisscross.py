import random
def gridnNum():
    randomNum = []
    size = int(input('Enter Grid Size: '))
    i = 0
    while len(randomNum) != size * size: #append all random number
        x = random.randint(-30,30)
        randomNum.append(x)
    for row in range(size):
        print("------" * size,end = "")
        print("-")
        for column in range(size):
            print("|",end = "")
            if randomNum[i] >= 0 and randomNum[i] < 10:
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
gridnNum()

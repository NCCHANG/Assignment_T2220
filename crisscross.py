import random
def gridnNum():
    size = int(input('Enter Grid Size: '))
    for row in range(size):
        print("------" * size,end = "")
        print("-")
        for column in range(size):
            print("|",end = "")
            x = random.randint(-30,30)
            if x >= 0 and x < 10:
                print(f"  {x}  ",end = "")
            elif x >= 10:
                print(f" {x}  ",end= '')
            elif x < 0 and x > -10:
                print(f" {x}  ", end = '')
            else:
                print(f" {x} ",end = '')
            if column == size-1 :
                print("|")
    print("------" * size,end = "")
    print("-")    
gridnNum()

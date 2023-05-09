import random
def gridnNum():
    for row in range(6):
        print("--------")
        for column in range(6):
            print("|",end = "")
            x = random.randint(-30,31)
            if x >= 0 and x < 10:
                print(f"  {x}  ",end = "")
            elif x >= 10:
                print(f" {x}  ",end= '')
            elif x < 0 and x > -10:
                print(f" {x}  ", end = '')
            else:
                print(f" {x} ",end = '')
            if column == 5 :
                print("|")    
gridnNum()

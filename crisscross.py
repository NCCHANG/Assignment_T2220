import random
def grid():
    for row in range(6):
        print("--------")
        for column in range(6):
            print("|",end = " ")
            print(random.randint(-30,31),end = " ")
            if column == 5 :
                print("|")    
grid()

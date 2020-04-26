import random

x="y"
print("This is dice Project in console ")

while x == "y":
    n=random.randint(1,6)
    if n==1:
        print("----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("----------")

    elif n==2:
        print("----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("----------")

    elif n==3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")

    elif n==4:
        print("-----------")
        print("| 0    0  |")
        print("|         |")
        print("| 0    0  |")
        print("-----------")

    elif n==5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")
y
    elif n==6:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("-----------") 

    x=input("If you want to roll again ! enter 'y' : ")
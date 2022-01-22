import random
num = random.randint(1,100)
#print(num)
print("Hear is my first game \n")
print("So fisrt of all u have to gause a number between 1 - 100\n")
print("If it is corect u won other wise u will get a hint \n")
print("So lets start the game \n")
n1 = int(input("So enter the number:  "))

if num==n1:
    print("WOW! YOu won the game in the FIRST time ")
elif n1>num:
    print("UPS! You have predicted a larger num predict sum lesser number ")
    n2 = int(input("ENter the number again "))
elif n1<num:
    print("UPS! You have predicted a smaller num predict any biger number number ")
    n2 = int(input("ENter the number again "))
else:
    print("invalid input")

if num == n2:
    print("WOW! YOu won the game in the SECOND time ")
elif n2 > num:
    print("UPS! You have predicted a larger num predict sum lesser number ")
    n3 = int(input("ENter the number again "))
elif n2 < num:
    print("UPS! You have predicted a smaller num predict any biger number number ")
    n3 = int(input("ENter the number again "))
else:
    print("invalid input")

if num == n3:
    print("WOW! YOu won the game in the THIRD time ")
elif n3 > num:
    print("UPS! You have predicted a larger num predict sum lesser number ")
    n4 = int(input("ENter the number again "))
elif n3 < num:
    print("UPS! You have predicted a smaller num predict any biger number number ")
    n4 = int(input("ENter the number again "))
else:
    print("invalid input")

if num == n4:
    print("WOW! YOu won the game in the FORTH time ")
elif n4 > num:
    print("UPS! You have predicted a larger num predict sum lesser number ")
    n5 = int(input("ENter the number again "))
elif n4 < num:
    print("UPS! You have predicted a smaller num predict any biger number number ")
    n5 = int(input("ENter the number again "))
else:
    print("invalid input")


if num == n5:
    print("WOW! YOu won the game in the FIFTH time ")
elif n5 > num:
    print("UPS! You have predicted a larger num predict sum lesser number ")
    n6 = int(input("ENter the number again "))
elif n5 < num:
    print("UPS! You have predicted a smaller num predict any biger number number ")
    n6 = int(input("ENter the number again "))
else:
    print("invalid input")

if num == n6:
    print("WOW! YOu won the game in the SIXTH time ")
else:
    print("YOU LOOSE! yuu have exided the limit ")
print(num)

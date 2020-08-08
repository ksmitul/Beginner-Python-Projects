import random

command=input("do you wan to roll the dice?")

if command=="yes" or command=="y":
    print("you asked for it..")
    print(random.randint(1,6))
else:
    print("then, why are you here?")



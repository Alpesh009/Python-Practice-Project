import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
revserDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youStr]

print(f"You choose {revserDict[you]}\nComputer choose {revserDict[computer]}")
#print(f"{computer} and {you}")
if(computer == you):
    print("Its a Draw")
else:
    if(computer==-1 and you==1):
        print("You win!")

    elif(computer==-1 and you==0):
        print("You lose!")

    elif(computer==1 and you==-1):
        print("You lose!")

    elif(computer==-1 and you==0):
        print("You win!")

    elif(computer==0 and you==-1):
        print("You win!")

    elif(computer==0 and you==1):
        print("You lose!")
    
    elif(computer==1 and you==0):
        print("You Win!")

    else:
        print("Something went wrong!")

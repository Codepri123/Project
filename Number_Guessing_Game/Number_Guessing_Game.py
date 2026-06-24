import numpy as np
#NUMBER GUESSING GAME
print("Hello !!!!")
print("----------------------------------")
print("----------Welcome in the game---------")
c=input(":::::Enter your name:::::::")
print(f"-------HELLO {c.upper()}, WELCOME IN GAME---------")
print()
print("READ TERMS AND CONDITIONS")
print("You can guess upto 5 times")
print("If you guess wrong then you failed this match")
computer_choice=np.random.choice([1,2,3,4,5],1)
print(computer_choice)
choice=int(input("Enter a number:"))
for i in range(6):
    if choice==computer_choice:
        print("You won!!!!!!")
        break
    else:
     choice=int(input("Enter a number:")) 



        
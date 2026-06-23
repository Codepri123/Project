import numpy as np
def play():
 print("......................")
 choice=input("enter a  user choices:::")
 print("......................")
 computer_choice=np.random.choice(["Rock","Paper","Scissors"])
 print("......................")
 print("This is the computer_choice:::",computer_choice)
 print("......................")
 match choice:
    case "Rock":
        if computer_choice=="Scissors":
            print("Rock hits the scissors")
            print("User wins a match")
        elif computer_choice=="Paper":
            print("Paper beats rock")
            print("User loose a match")
        else:
            print("Tie of the match")
    case "Paper":
        if computer_choice=="Rock":
            print("Paper beats rock")
            print("User wins a match")
        elif computer_choice=="Scissors":
            print("Scissors beat paper")
            print("User loose a match")
        else:
           print("Tie")
    case "Scissors":
        if computer_choice=="Paper":
            print("Scissors beat paper")
            print("User wins a match")
        elif computer_choice=="Rock":
         print("Rocks hits the scissors")
         print("User loose a match")
        else:
           print("Tie")

print("---------------------------------")
print("you!!!!! want to play again")
print("-------------------------------------")
print("then click -------play again")
n=input("user enter a decision")
if n == "play_again":
        play() 
elif n == "game over":
    print("Game Over!")
else:
    print("Invalid input. Game Over!")

play()    
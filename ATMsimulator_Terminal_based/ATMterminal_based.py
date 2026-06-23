#ATM MACHINE
print("WELCOME TO MACHINE")
list=["arjun","ravi","vikram"]
NAME=input("enter the name of the bank:")
if NAME=="unique":
     print("INSERT ATM CARD........")
else:
     print("Sorry you are not insert card in this machine")

#after card inserted
a=input("Enter a card holder name=")
if a in list:
 print(a)
 print(" Click the  BELOW OPTIONS:")
 print("Check balance")
 print("Deposit Money")
 print("Withdraw Money")
 print("exit")

 option = int(input("Enter your preference: "))

 match option:
     case 1:
        int(input(("Check Balance")))
        print(" IT IS A total Money balance")

     case 2:
       int(input(("Deposit Money")))
       print(" Finally money is deposit")

     case 3:
        int(input(("Withdraw Money")))
        print(" Finally money is Withdraw")


     case 4:
        print("Exit")
 
else:
      print("SORRY YOU CANNOT USE MACHINE")        

    






     
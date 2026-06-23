print("DISCALIMER:")
print("1 TASKS YOU WILL ADD AT ONE TIME")
print()
print("WELCOME TO YOUR TO DO LIST")
print()
print("CLICK THE FOLLOWING OPTIONS")
print("1. ADD,VIEW AND SAVED YOUR DATA IN LIST")
print("2. DELETE IN A LIST")
result = int(input("enter a choice::"))
match result:
    case 1:
        print("ADD AND SAVE A TASK")
        data=input("enter a task")
        def task_assigned(data):
            return data
        print("All data is saved in Database")
    case 2:
        print("DELETE A TASK")
print()        
print("VIEW YOUR DATA")
print(task_assigned(data))
print()
print(f"ALL------data----- is saved")      
print("YOUR DATA IS SAFE AND SECURE...")
print("REVISIT IN OUR TO DO LIST.....")

print("\nYOUR DATA IS SAFE AND SECURE...")
print("THANK YOU FOR USING OUR TO-DO LIST")
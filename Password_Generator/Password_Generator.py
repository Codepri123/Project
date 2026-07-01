import numpy as np
user_password=int(input("ENTER WHAT LENGTH OF PASSWORD YOU WANT:"))
ar=np.random.choice(["a","ab@123","ab","1234@abcd"])
list=[]
for i in ar:
    if i not in list:
        list.append(i)
    else:
        pass
print("the random element in the ",list)    
if user_password==len(list):
    print(ar)
else:
    pass
import random
u_choice=0
c_choice=0
u_choice=input("enter your choice:").lower()
l=["rock","scissor","paper"]
c_choice=random.randint(0,2)
c_choice=l[c_choice]
if u_choice==c_choice:
    print("match drawn")
    print(c_choice)
elif c_choice=="rock" and u_choice=="scissor":
    print("computer win")
    c_choice+=1
    print(c_choice)
elif c_choice=="scissor" and u_choice=="paper":
    print("computer win")
    c_choice+=1
    print(c_choice)
elif c_choice=="paper" and u_choice=="rock":
    print("computer wins")
    c_choice+=1
    print(c_choice)
else:
    print("user wins")
    u_choice+=1
    print(u_choice)
    
if u_choice>c_choice:
    print("user wins")
elif u_choice==c_choice:
    print("compuer wins")
else:
    print("match drawn")

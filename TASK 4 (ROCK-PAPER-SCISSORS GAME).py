import random
choose=["rock","paper","scissors"]
user_choice=input("choose rock or paper or scissors\n")
computer_choice=random.choice(choose)
print("user choice:",user_choice)
print("computer_choice:",computer_choice)
if user_choice==computer_choice:
    print("its a draw\n")
elif user_choice=="rock" and computer_choice=="scissors" or user_choice=="paper" and computer_choice=="rock" or user_choice=="scissors" and computer_choice=="paper":
    print("user wins\n")
else:
    print("computer wins\n")

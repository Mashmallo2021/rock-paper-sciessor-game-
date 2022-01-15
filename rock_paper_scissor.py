import random

user= 0
computer=0
option=["rock","paper","scissor"]

while True:
    user_input =  input("type rock ,paper , scissor / q to quit :").lower()
    if user_input =="q"  :
        break
    if user_input not in option:
        continue

    random_number=random.randint(0,2)
    computer_pick=option[random_number]
    print("computer picked : ",computer_pick)
    
    if user_input == "rock" and computer_pick == "scissor":
        print("you won")
        user+=1
    elif user_input== "scissor" and computer_pick == "paper":
        print("you won")
        user+=1

    if user_input== "paper" and computer_pick == "rock":
        print("you won")
        user+=1
    elif user_input == computer_pick :
        print("you both draw this time")


    else:
        print("you lost ")
        computer+=1

print("your score is : ", user)
print("computer score : ",computer)
print("THANK YOU FOR PLAYING")
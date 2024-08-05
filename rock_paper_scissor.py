import random


list1 = ["rock","paper","scissor"]

while(True):
    user = str(input("Enter your choice: ").lower())
    if user not in list1:
        print("Wrong input")
        continue
    computer = random.choice(list1)
    if user == computer:
          print("Tie")
          continue
    elif (user == "rock" and computer == "scissor") or \
         (user == "scissor" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
            print(f"You win\nYour choice {user} and computer's choice was {computer}") 
            break
    elif (user == "scissor" and computer == "rock") or \
         (user == "paper" and computer == "scissor") or \
         (user == "rock" and computer == "paper"):
            print(f"You lost\nYour choice was {user} and computer's choice was {computer}")
            break
   
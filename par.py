import random

choice = ["Stone","Paper","Scissor"]

user = input("Enter Stone or Paper or Scissor :")
computer = random.choice(choice)

print("User choice :",user)
print("Computer choice :", computer)

if user == computer:
    print("It's a tie!")
elif user == "Stone" and computer == "Scissor" or user == "Paper" and computer == "Stone" or user == "Scissor" and computer == "Stone":
    print("User Win !")

else:
    print("Computer Win !")
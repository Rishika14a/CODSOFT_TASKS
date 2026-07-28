import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")

elif user_choice in choices:
    print("Computer wins!")

else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
    
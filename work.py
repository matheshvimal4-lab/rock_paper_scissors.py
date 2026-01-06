import random

print("🎮 Rock Paper Scissors Game 🎮")

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print("Computer choice:", computer)

if user == computer:
    print("Result: DRAW 🤝")

elif user == "rock" and computer == "scissors":
    print("You WIN 🎉")

elif user == "scissors" and computer == "paper":
    print("You WIN 🎉")

elif user == "paper" and computer == "rock":
    print("You WIN 🎉")

else:
    print("You LOSE ❌")

print("Name: Karim S Mulla")
print("USN: 1AY24AI052")
print("Section: M")
import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if user_choice == 'quit':
        break
    if user_choice not in options:
        print("Invalid choice, please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}")

print("Game Over!")
print(f"Final Score - You: {user_score}, Computer: {computer_score}")

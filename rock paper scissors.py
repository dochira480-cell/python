import random

while True:
    action = input("Enter rock, paper, or scissors: ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)
    print(f"\nYou chose {action}, computer chose {computer}.\n")

    if action == computer:
        print("It's a tie!")
    elif action == "rock":
        if computer == "scissors":
            print("You win!")

        else:
            print("Paper covers rock, you lose.")
    elif action == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("Scissors cuts paper, you lose.")

    play = input("Play again? (y/n): ")
    if play != "y":
        break
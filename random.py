import random
playing = True
number = (random.randint(0,9))

print("I will generate a random number between 0 and 9, can you guess it?")
print()
print("The game ends when you guess the number correctly")

while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print("You won the game.")
        print("The number was: ", number)
        break
    else:
        print("Try again.")
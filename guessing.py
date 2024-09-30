import random

def number_guessing_game():
    target = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number (1-100): "))
        if guess < target:
            print("Higher")
        elif guess > target:
            print("Lower")
        else:
            print("Correct! You guessed the number. ")

number_guessing_game()
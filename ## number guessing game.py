## number guessing game
import random

print("Welcome to the number guessing game.")
difficulty = input("Select difficulty(Easy, medium, or hard): ")

if difficulty == "easy":
    max_number = 25
elif difficulty == "medium":
    max_number = 50
elif difficulty == "hard":
    max_number = 100
else:
    print("fuck you then")
    max_number = 500_000

guess = None

answer = random.randint(1, max_number)

while guess != answer:
    guess = int(input("Guess a number between 1 and " + str(max_number)))

    if guess < answer:
        print("Higher")
    elif guess > answer:
        print("Lower")
    else:
        print("Ding ding ding! Correct! It was " + str(answer))
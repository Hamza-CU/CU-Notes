import random

generate = random.randint(1, 100)

guess = int(input("Guess a number from 1-100: "))

while guess != generate:
    if guess < generate:
        print("guess higher")
    elif guess > generate:
        print("guess lower")
    else:
        break
    guess = int(input("Guess a number from 1-100: "))

print("Correct guess!")

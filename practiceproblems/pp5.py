#Problem 7 (Simple Guessing Game - *)

import random
import time

print("This is the random number guessing game")
time.sleep(2)

generate = random.randint(1,100)
x = 0

while x==0:
    userInput = float(input("please guess a number from 1-100\n"))
    if userInput == generate:
        print("Correct guess! You had a 1% chance of guessing that number!")
        break
    else:
        range = abs(int(generate - userInput))
        print("Sorry that was incorrect. You were", range,"off. Please input the correct answer to close the program")

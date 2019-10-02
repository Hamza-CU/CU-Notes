# Problem 3 (Movie Expert System - *)

import time
print("""Think of a movie out of these 4
-Transformers
-Pacific Rim
-Lion King
-Aladdin""")

time.sleep(3)
print("Does your movie contain giant robots?")
response = str(input())

if response == "yes":
    response2 = str(input("Do people control the robots? "))
    if response2 == "yes":
        print("You're thinking of Pacific Rim")
    else:
        print("You're thinking of Transformers")
else:
    response3 = str(input("Is the main character a lion? "))
    if response3 == "yes":
        print("You're thinking about Lion King")
    else:
        print("You're thinking of Aladdin")

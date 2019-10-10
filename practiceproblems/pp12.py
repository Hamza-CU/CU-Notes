#Problem 2 (Vegetable Garden – **)

counter = 0

while counter != 3:
    response = str(input("Did it rain today? (t/f): "))
    if response == "t":
        counter = 0
    else:
        counter += 1

print("water your plants!")

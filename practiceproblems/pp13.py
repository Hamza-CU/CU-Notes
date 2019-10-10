#Problem 3 (Number of Digits - ***)

div = 1
number = int(input("enter a number: "))
digCount = 0

while div > 0:
    if (number / div) >= 1:
        digCount += 1
        div = div * 10
    else:
        break

print("This number has", digCount, "digits")

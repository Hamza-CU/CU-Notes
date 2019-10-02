#all the practice from the tutorial

a = float(input("side length: "))
b = float(input("side length: "))
c = float(input("side length: "))

import math

S = (a+b+c)/2

area = math.sqrt(S*(S-a)*(S-b)*(S-c))
print(area)

__________________________

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
num3 = int(input("enter number3: "))
num4 = int(input("enter number4: "))

list = [num1, num2, num3, num4]

print((max(list) - min(list)))

___________________________

cm = float(input("enter how many cm: "))

inches = round(cm / 2.54)

if inches >= 12:
    feet = inches//12
    inchesrem = inches % 12
    print(cm, "cm is approximatly", feet,"feet", inchesrem, "inches")
else:
    print(cm, "cm is approximatly", inches, "inches")
